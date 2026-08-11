from dotenv import load_dotenv
load_dotenv()

import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from gmail_gcloud import gmail_service, history, messages_by_label
from gmail_gcloud_subscriber import gmail_subscribe
from gmail_label_cache import refresh_label_cache, get_label_by_name, get_label_by_id, validate_label_name
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
(options, args) = parser.parse_args()

def is_thread_label(label):
    return (not label == label.upper() and
        not label.startswith('[Gmail]') and
        not "000-ignore" in label and
        not "/github" in label)

def messages(label):
    msgs = messages_by_label(label['id'])

    result = []
    
    def get_relevant_fields(m):
        subject = "";
        frm = "";
        to = "";
        message_id = "";
        for header in m['payload']['headers']:
            if header['name'].lower() == "subject":
                subject = header['value'];
            if header['name'].lower() == "from":
                frm = header['value'];
            if header['name'].lower() == "to":
                to = header['value'];
            if header['name'].lower() == "message-id":
                message_id = header['value'];
        return {
                'mailtime': int(m['internalDate'][:-3]),
                'subj': subject,
                'from': frm,
                'to': to,
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
    messageIds = set()
    for record in records:
        for msg in record['messages']:
            messageIds.add(msg['id'])

    print(f"Getting labels for {len(messageIds)} message id's")
    labelIds = set()
    for messageId in messageIds:
        try:
            msg = gmail_service.users().messages().get(
                    userId=os.getenv('GMAIL_USER_ID'),
                    id=messageId,
                    format="full"
            ).execute()
            if 'labelIds' in msg:
                labelIds = labelIds.union(msg['labelIds'])
        except HttpError as e:
            if e.resp.status != 404:
                raise e

    print(f"Updating {len(labelIds)} labels")
    for labelId in labelIds:
        label = get_label_by_id(labelId)
        print(f"Updating {label}")
        if is_thread_label(label['name']):
            if already_refreshed(label, history_id):
                print(f"Label {label['name']} already current as of {history_id}")
                continue
            print(f"Label {label['name']}")
            refresh_thread(label)
            # Only after the file is durably in place: dying in between costs
            # one redundant refresh next time, which is the safe direction.
            record_refreshed(label, history_id)

# Refreshing a single label:
#refresh_label_cache()
#label = get_label_by_name("zzz-admin")
#print(f"Refreshing {label}")
#refresh_thread(label)
#print(f"done")
#exit(1)

#update_history_records(history.get('history', []))
#print("done")

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

streaming_pull = gmail_subscribe(subscription_callback)
print(streaming_pull.result())
