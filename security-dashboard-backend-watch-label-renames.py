from dotenv import load_dotenv
load_dotenv()

from gmail_gcloud_subscriber import gmail_subscribe
from gmail_label_cache import refresh_label_cache, validate_label_name
from optparse import OptionParser
import os
import threading
from time import sleep
import subprocess

# This script watches for label renames and
# applies the corresponding file renames.

parser = OptionParser()
parser.add_option("-t", "--target", default="email-classification/", help="Directory to populate")
(options, args) = parser.parse_args()

def label_updated(labelId, old, new):
    validate_label_name(old)
    validate_label_name(new)
    if os.path.isfile(f"{options.target}/{old}.json"):
        if os.path.isfile(f"{options.target}/{new}.json"):
            # likely merged
            subprocess.run(["git", "rm", "-f", f"{old}.json"], cwd=options.target)
        else:
            os.makedirs(options.target + '/' + '/'.join(new.split('/')[:-1]), exist_ok=True)
            result = subprocess.run(["git", "mv", f"{old}.json", f"{new}.json"], cwd=options.target)
            if result.returncode != 0:
                print(f"Move of {labelId} ('{old}' to '{new}') failed (status code {result.returncode}), just removing")
                os.remove(f"{options.target}/{old}.json")


def poll_label_changes(interval=10):
    while True:
        print("Polling for label changes")
        for change in refresh_label_cache(options.target):
            old = change['old_name']
            new = change['name']
            if old != new:
                label_updated(change['id'], old, new)
        sleep(interval)

thread = threading.Thread(target=poll_label_changes)
thread.start()
