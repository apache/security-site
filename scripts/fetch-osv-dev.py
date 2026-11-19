#!/usr/bin/env -S uv run --script
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///

# Downloads the osv.dev versions of our CVE records, for comparison with
# the OSV records we generate ourselves:
#
# - <output>/cve-osv/: the raw output of osv.dev's CVE conversion
#   (gs://cve-osv-conversion/osv-output/)
# - <output>/api/: the records as served by api.osv.dev,
#   after osv.dev added versions from Git tags, aliases, etc.
#
# CVEs that osv.dev does not have are skipped.
# Records are stored with sorted keys so that re-running the script only shows actual changes.
#
# Usage: uv run scripts/fetch-osv-dev.py [-o <output>] <public.json>
#
# where <public.json> is the advisory index downloaded from https://cveprocess.apache.org/publicjson

import argparse
import json
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SOURCES = {
  'cve-osv': 'https://storage.googleapis.com/cve-osv-conversion/osv-output/%s.json',
  'api': 'https://api.osv.dev/v1/vulns/%s',
}

parser = argparse.ArgumentParser(description='Download the osv.dev versions of our CVE records.')
parser.add_argument('publicjson', type=Path, help='advisory index downloaded by fetch-data.sh')
parser.add_argument('-o', '--output', type=Path, default=Path(__file__).resolve().parent.parent / 'osv-dev',
                    help='output directory (default: ../osv-dev relative to this script)')
args = parser.parse_args()

def fetch(url):
  try:
    with urllib.request.urlopen(url, timeout=60) as response:
      return json.load(response)
  except urllib.error.HTTPError as e:
    if e.code == 404:
      return None
    raise

def path(source, advisory):
  # Same layout as static/projects/
  return args.output / source / advisory['owner'] / (advisory['ID'] + '.json')

def download(source, advisory):
  doc = fetch(SOURCES[source] % advisory['ID'])
  if doc is not None:
    path(source, advisory).parent.mkdir(parents=True, exist_ok=True)
    with path(source, advisory).open('w') as f:
      json.dump(doc, f, ensure_ascii=True, indent=2, sort_keys=True)
      f.write('\n')
  return doc is not None

with args.publicjson.open() as f:
  advisories = sorted(json.load(f), key=lambda advisory: advisory['ID'])

for source in SOURCES:
  with ThreadPoolExecutor(max_workers=8) as executor:
    found = list(executor.map(lambda advisory: download(source, advisory), advisories))
  # Remove records that are no longer available
  keep = {path(source, advisory) for advisory, ok in zip(advisories, found) if ok}
  for record in (args.output / source).glob('*/*.json'):
    if record not in keep:
      record.unlink()
  for project in (args.output / source).glob('*'):
    if project.is_dir() and not any(project.iterdir()):
      project.rmdir()
  print('%s: %d of %d records found' % (source, sum(found), len(advisories)))
