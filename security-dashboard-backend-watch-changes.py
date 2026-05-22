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
    with open(f"{options.target}/{label['name']}.json", "w") as f:
        json.dump(messages(label), f, indent=2)

def update_history_records(records):
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
        n = n + 1
        if label and is_thread_label(label['name']):
            print(f"Updating {label['name']} ({n}/{len(labelIds)})")
            refresh_thread(label)

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
    print("Got callback")
    with processing_lock:
        history_id = json.loads(message.data)['historyId']
        print(f"Got notified of new messages, starting at {history_id}")
        records = history(last_processed_history_id, history_id)
        print(f"Updating {len(records)} records")
        if records:
            update_history_records(records)
            update_last_processed_history_id(max(int(r['id']) for r in records))
        print(f"Updated, waiting for next pub/sub message")
        message.ack()

print("Subscribing")
streaming_pull = gmail_subscribe(subscription_callback)
print(streaming_pull.result())
