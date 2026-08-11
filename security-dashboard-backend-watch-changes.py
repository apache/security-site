from dotenv import load_dotenv
load_dotenv()

import json
from email.header import decode_header, make_header
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from gmail_gcloud import gmail_service, history, messages_by_label
from gmail_gcloud_subscriber import gmail_subscribe
from gmail_label_cache import refresh_label_cache, get_label_by_name, get_label_by_id, get_labels_by_prefix, validate_label_name, delete_label_file
import threading
from optparse import OptionParser
import os
import subprocess

# Watch the feed of GMail changes and keep
# email-classification updated.

# When a label is renamed, this script only
# sees (and updates) the new label. The old
# label is removed by a separate job,
# email-classification-watch-label-renames.py

parser = OptionParser()
parser.add_option("-t", "--target", default="email-classification", help="Directory to populate")
parser.add_option("-s", "--single")
parser.add_option("-p", "--project", help="Refresh all known labels under this project prefix")
(options, args) = parser.parse_args()

def is_thread_label(label):
    return (not label == label.upper() and
        not label.startswith('[Gmail]') and
        not "000-ignore" in label and
        not "/github" in label)

def decode_rfc2047(value):
    # Untrusted: fall back to the raw value on malformed encoded-words
    # or unknown charsets rather than crashing the daemon.
    try:
        return str(make_header(decode_header(value)))
    except Exception:
        return value

def messages(label):
    msgs = messages_by_label(label['id'])

    result = []

    def get_relevant_fields(m):
        subject = "";
        frm = "";
        to = "";
        cc = "";
        reply_to = "";
        message_id = "";
        for header in m['payload']['headers']:
            if header['name'].lower() == "subject":
                subject = decode_rfc2047(header['value']);
            if header['name'].lower() == "from":
                # Store raw: decoding before RFC 5322 parsing lets encoded-words
                # smuggle address syntax (<, >, @, ,) into the display-name slot.
                frm = header['value'];
            if header['name'].lower() == "to":
                to = header['value'];
            if header['name'].lower() == "cc":
                cc = header['value'];
            if header['name'].lower() == "reply-to":
                reply_to = header['value'];
            if header['name'].lower() == "message-id":
                message_id = header['value'];
        return {
                'mailtime': int(m['internalDate'][:-3]),
                'subj': subject,
                'from': frm,
                'to': to,
                'cc': cc,
                'reply_to': reply_to,
                'message_id': message_id
        }

    for msg in reversed(msgs):
        m = gmail_service.users().messages().get(
                userId=os.getenv('GMAIL_USER_ID'),
                id=msg['id'],
                format="full"
        ).execute()
        result.append(get_relevant_fields(m))

    return result

def refresh_thread(label):
    if not label:
        return;

    validate_label_name(label['name'])
    os.makedirs(options.target + '/' + '/'.join(label['name'].split('/')[:-1]), exist_ok=True)
    # Build the whole list before touching the file: messages() makes one API
    # call per message and can fail partway (rate limit), which would otherwise
    # leave a truncated .json behind for consumers to read.
    msgs = messages(label)
    path = f"{options.target}/{label['name']}.json"
    with open(path + ".tmp", "w") as f:
        json.dump(msgs, f, indent=2)
    os.replace(path + ".tmp", path)

# labelId -> {"name": ..., "history_id": ...}, meaning: the on-disk JSON for
# this label reflects the mailbox at least as of history_id. Lets a retry of a
# batch that died partway (typically on the rate limit) skip the labels it
# already finished, instead of replaying the whole batch and burning the same
# quota again.
_LEDGER_PATH = f"{options.target}/refreshed_labels.json"

def _load_ledger():
    try:
        with open(_LEDGER_PATH) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

refreshed_labels = _load_ledger()

def _save_ledger():
    with open(_LEDGER_PATH + ".tmp", "w") as f:
        json.dump(refreshed_labels, f, indent=2, sort_keys=True)
    os.replace(_LEDGER_PATH + ".tmp", _LEDGER_PATH)

def already_refreshed(label, history_id):
    entry = refreshed_labels.get(label['id'])
    # A rename moves the file this entry describes, and a rename onto an
    # existing label deletes it (see email-classification-watch-label-renames.py),
    # so a name mismatch invalidates the entry whatever its history_id says.
    return (entry is not None and
            entry['name'] == label['name'] and
            entry['history_id'] >= history_id)

def record_refreshed(label, history_id):
    refreshed_labels[label['id']] = {
        'name': label['name'],
        'history_id': history_id,
    }
    _save_ledger()

def update_history_records(records, history_id):
    labelIds = set()
    for record in records:
        for event in [ "messagesAdded", "messagesDeleted", "labelsAdded", "labelsRemoved" ]:
            if event in record:
                for msg in record[event]:
                    if 'labelIds' in msg:
                        for labelId in msg['labelIds']:
                            labelIds.add(labelId)

    print(f"Updating {len(labelIds)} labels")
    n = 0
    for labelId in labelIds:
        label = get_label_by_id(labelId)
        if not label:
            print(f"Label {labelId} no longer found - TODO remove it?")
        elif is_thread_label(label['name']):
            print(f"Updating {label['name']} ({n}/{len(labelIds)})")
            if already_refreshed(label, history_id):
                print(f"Label {label['name']} already current as of {history_id}")
                continue
            print(f"Label {label['name']}")
            refresh_thread(label)
            # Only after the file is durably in place: dying in between costs
            # one redundant refresh next time, which is the safe direction.
            record_refreshed(label, history_id)
        n = n + 1

with open(f"{options.target}/last_processed_history_id.txt") as f:
    last_processed_history_id = int(f.read().strip())
def update_last_processed_history_id(i):
    global last_processed_history_id
    last_processed_history_id = i
    with open(f"{options.target}/last_processed_history_id.txt", "w") as f:
        f.write(str(last_processed_history_id))

processing_lock = threading.Lock()

def subscription_callback(message):
    global last_processed_history_id
    print("Got callback")
    with processing_lock:
        history_id = json.loads(message.data)['historyId']
        print(f"Got notified of new messages, starting at {history_id}")
        records = history(last_processed_history_id, history_id)
        print(f"Updating {len(records)} records")
        if records:
            target_history_id = max(int(r['id']) for r in records)
            update_history_records(records, target_history_id)
            update_last_processed_history_id(target_history_id)
        print(f"Updated, waiting for next pub/sub message")
        message.ack()

if options.single:
    # Refreshing a single label:
    refresh_label_cache(options.target)
    label = get_label_by_name(options.single)
    if label:
        print(f"Refreshing {label}")
        refresh_thread(label)
    else:
        if delete_label_file(options.target, options.single):
            print(f"Label {options.single} no longer found upstream, deleted")
        else:
            print(f"Label {options.single} not found")

elif options.project:
    refresh_label_cache(options.target)
    prefix = options.project.rstrip("/")
    prefix_labels = get_labels_by_prefix(options.project)
    upstream_names = {l['name'] for l in prefix_labels}

    # Remove thread files on disk under this project that no longer
    # correspond to an upstream label (deleted or renamed away). Only
    # the project's own directory (and its own label file) is scanned.
    project_dir = os.path.join(options.target, prefix)
    on_disk = []
    if os.path.isfile(project_dir + ".json"):
        on_disk.append(prefix)
    for root, dirs, files in os.walk(project_dir):
        for fn in files:
            if fn.endswith(".json"):
                on_disk.append(os.path.relpath(os.path.join(root, fn), options.target)[:-len(".json")])
    for name in on_disk:
        if name not in upstream_names:
            print(f"Thread '{name}' no longer in upstream list, removing")
            delete_label_file(options.target, name)

    project_labels = [l for l in prefix_labels if is_thread_label(l['name'])]
    print(f"Refreshing {len(project_labels)} labels under {options.project}")
    for n, label in enumerate(project_labels, 1):
        print(f"Refreshing {label['name']} ({n}/{len(project_labels)})")
        refresh_thread(label)

else:
    print("Subscribing")
    streaming_pull = gmail_subscribe(subscription_callback)
    print(streaming_pull.result())
