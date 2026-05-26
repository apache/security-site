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

from app import config
import dataclasses
import datetime
from email.utils import parseaddr
from enum import Enum, auto
import json
import pathlib
from quart import current_app
import re

@dataclasses.dataclass(frozen=True)
class Report:
    security_team_name: str
    """internal label the security team assigned to the thread,
       not to be exposed"""
    cves: list[str]
    title: str
    asf_member_link: str
    """link to the first email in the thread. this might only be
       available to ASF members. make-report.py does something
       smarter to give a link that's likely to also be accessible
       by PMC members that are not ASF members."""

    state: str

    timestamp: datetime.datetime

    @property
    def date(self) -> datetime.date:
        return self.timestamp.date()

def _asf_member_link(email):
    _, address = parseaddr(email['to'])
    listid = address.replace('@', '.')
    messageid = email['message_id'].replace(' ', '+').replace('+', '%2B').replace('=', '%3D').replace('@', '%40')
    return f"https://lists.apache.org/thread/{messageid}?<{listid}>"

def load_project_report(path: pathlib.Path) -> Report | None:
    with open(path) as f:
        emails = json.loads(f.read())

    m = re.match(r"(?:CVE-\S+\s+)*CVE-\S+", path.name)
    cves = m.group(0).split() if m else []

    if cves:
        state = "confirmed"
    else:
        m = re.match(r".*wf (.*).json", path.name)
        if not m:
            state = "untriaged"
        elif m.groups()[0] == "cve-allocation":
            state = "confirmed"
        else:
            state = m.groups()[0]

    if not emails:
        print(f"Empty label: {path.name}")
        return None

    first_email = emails[0]
    title = first_email['subj'].strip() or "(untitled)"
    if title.startswith("[SECURITY] "):
        title = title.removeprefix("[SECURITY] ")
    elif title.startswith("[Security] "):
        title = title.removeprefix("[Security] ")

    return Report(
        path.name,
        cves,
        title,
        _asf_member_link(first_email),
        state,
        datetime.datetime.fromtimestamp(first_email['mailtime'], tz=datetime.timezone.utc),
    )

async def load_project_reports(project: str) -> list[Report]:
    if not re.fullmatch(r"[a-z0-9]+", project):
        raise ValueError("invalid project name: {project!r}")

    d = config.get().data_dir_path / project
    threads = list(d.glob('**/*.json'))

    return [ r for r in (load_project_report(t) for t in threads) if r is not None ]
