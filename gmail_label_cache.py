from gmail_gcloud import gmail_service
from googleapiclient.errors import HttpError
import json
import os

_LABEL_NAME_EXTRA_CHARS = set("., /-_():=+#")

def validate_label_name(name):
    """Reject label names that would escape a target directory when used as a relative path.

    Raises ValueError on disallowed characters, absolute paths, or any '.'/'..'/empty
    path components. Uses an exception rather than `assert` so the check still runs
    under `python -O`.
    """
    for c in name:
        if not (c.isalnum() or c in _LABEL_NAME_EXTRA_CHARS):
            raise ValueError(f"label name {name!r} contains disallowed character {c!r}")
    if name.startswith("/"):
        raise ValueError(f"label name {name!r} must not be absolute")
    for part in name.split("/"):
        if part in ("", ".", ".."):
            raise ValueError(f"label name {name!r} contains invalid path component {part!r}")

_CACHE_FILENAME = "gmail_label_cache.json"
_loaded = False
labels = {}

def _cache_path(target_dir):
    return os.path.join(target_dir, _CACHE_FILENAME)

def _load_labels(target_dir):
    try:
        with open(_cache_path(target_dir)) as f:
            labels.update(json.load(f))
    except FileNotFoundError:
        pass

def _save_labels(target_dir):
    path = _cache_path(target_dir)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(labels, f, indent=2, sort_keys=True)
    os.replace(tmp, path)

# refreshes the cache and returns any labels
# whose names changed
def refresh_label_cache(target_dir):
    global _loaded
    if not _loaded:
        _load_labels(target_dir)
        _loaded = True

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

    _save_labels(target_dir)
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
    try:
        label = gmail_service.users().labels().get(
            userId=os.getenv('GMAIL_USER_ID'),
            id=labelId
        ).execute()
    except HttpError as e:
        if e.resp.status == 404:
            return None
        else:
            raise e

    new_name = label['name']

    return {
        'id': labelId,
        'name': new_name,
    }
