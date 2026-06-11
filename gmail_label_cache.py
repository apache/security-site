from gmail_gcloud import gmail_service
from googleapiclient.errors import HttpError
import json
import os
import subprocess

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

def delete_label_file(target_dir, name):
    """Remove a label's classification file from target_dir.

    Stages the deletion with `git rm` (falling back to a plain remove if
    git fails, e.g. the file is untracked). No-op if the file is absent.
    Returns True if a file was removed.
    """
    validate_label_name(name)
    path = os.path.join(target_dir, f"{name}.json")
    if not os.path.isfile(path):
        return False
    result = subprocess.run(["git", "rm", "-f", f"{name}.json"], cwd=target_dir)
    if result.returncode != 0:
        print(f"Git remove of '{name}' failed (status code {result.returncode}), just removing")
        os.remove(path)
    return True

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

# refreshes the cache and returns any labels that changed.
# Each change is a dict with 'id' and 'old_name'. A rename
# also has the new 'name'; a deletion (the label disappeared
# upstream) has 'name' set to None.
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
    current_ids = set()
    for l in label_list['labels']:
        current_ids.add(l['id'])
        if l['id'] in old_labels and old_labels[l['id']] != l['name']:
            result.append({
                'id': l['id'],
                'old_name': old_labels[l['id']],
                'name': l['name']
            })
        labels[l['id']] = l['name']

    # Detect cached labels that are no longer returned upstream
    # (deleted) and drop them from the cache.
    for labelId in list(labels):
        if labelId not in current_ids:
            result.append({
                'id': labelId,
                'old_name': labels[labelId],
                'name': None,
            })
            del labels[labelId]

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

def get_labels_by_prefix(prefix):
    prefix_slash = prefix.rstrip("/") + "/"
    return [
        {'id': k, 'name': labels[k]}
        for k in labels
        if labels[k] == prefix or labels[k].startswith(prefix_slash)
    ]

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
