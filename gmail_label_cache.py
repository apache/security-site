from gmail_gcloud import gmail_service
import os

# TODO load from disk
labels = {}

# refreshes the cache and returns any labels
# whose names changed
def refresh_label_cache():
    old_labels = labels

    label_list = gmail_service.users().labels().list(
        userId=os.getenv('GMAIL_USER_ID'),
    ).execute()
    result = []
    if not 'labels' in label_list:
        print(label_list)
    for l in label_list['labels']:
        if l['id'] in old_labels and old_labels[l['id']] != l['name']:
            result.append({
                'id': l['id'],
                'old_name': old_labels[l['id']],
                'name': l['name']
            })
        labels[l['id']] = l['name']

    # TODO write to disk
    return result

def get_label_by_name(name):
    for k in labels:
        if labels[k] == name:
            return {
                'id': k,
                'name': name,
            }

    return None

def get_label_by_id(labelId):
    old_name = None
    if labelId in labels:
        old_name = labels['labelId']

    label = gmail_service.users().labels().get(
        userId=os.getenv('GMAIL_USER_ID'),
        id=labelId
    ).execute()
    new_name = label['name']

    return {
        'id': labelId,
        'old_name': old_name,
        'name': new_name,
    }
