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
from email.header import decode_header
from email.utils import getaddresses
from enum import Enum, auto
import hashlib
import json
import pathlib
from quart import current_app
import re

@dataclasses.dataclass(frozen=True)
class Reporter:
    name: str
    email: str

    @property
    def display_name(self) -> str:
        return self.name or self.email or "unknown"

    @property
    def tooltip(self) -> str:
        if self.name and self.email:
            return f"{self.name} <{self.email}>"
        return self.email or self.name or "unknown"

    @property
    def initials(self) -> str:
        source = self.name or self.email.split('@', 1)[0]
        letters = [w[0] for w in re.split(r'\s+', source) if w]
        if not letters:
            return '?'
        return ''.join(letters[:3]).upper()

    @property
    def color(self) -> str:
        digest = hashlib.md5(self.email.lower().encode()).hexdigest()
        hue = int(digest[:4], 16) % 360
        return f"hsl({hue}, 55%, 45%)"


@dataclasses.dataclass(frozen=True)
class Report:
    security_team_name: str
    """internal label the security team assigned to the thread,
       not to be exposed"""
    cves: list[str]
    jira: str
    """If this project tracks security issues in private jira issues, the Jira ID"""
    title: str
    asf_member_link: str
    """link to the first email in the thread. this might only be
       available to ASF members. make-report.py does something
       smarter to give a link that's likely to also be accessible
       by PMC members that are not ASF members."""
    link: str
    """link to the email archive for project members who may not
       necessarily be ASF members."""
    reporter: Reporter | None

    state: str

    timestamp: datetime.datetime

    @property
    def date(self) -> datetime.date:
        return self.timestamp.date()

    @property
    def sanitized_title(self) -> str:
        cleaned = re.sub(r"[^A-Za-z0-9 .\-()]", " ", self.title)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        return cleaned[:200]

def _apache_list_address(email):
    addresses = list(getaddresses([email['to']]))
    if 'cc' in email:
        addresses.extend(getaddresses([email['cc']]))
    for _, address in addresses:
        if address.endswith('.apache.org'):
            return address
    return None

def _asf_member_link(email):
    apache_list_address = _apache_list_address(email)
    if apache_list_address:
        listid = apache_list_address.replace('@', '.')
    else:
        listid = 'security.apache.org'
    messageid = email['message_id'].replace(' ', '+').replace('+', '%2B').replace('=', '%3D').replace('@', '%40')
    return f"https://lists.apache.org/thread/{messageid}?<{listid}>"

def _project_link(emails):
    for email in emails[:5]:
        if _apache_list_address(email):
            return _asf_member_link(email)
    return None

def _reporter(email) -> Reporter | None:
    addresses = [a for a in getaddresses([email.get('from', '')]) if a[1]]
    if not addresses:
        return None
    name, address = addresses[0]
    if ' via ' in name and address.endswith('apache.org'):
        reply_to_addresses = [a for a in getaddresses([email.get('reply_to', '')]) if a[1]]
        if not reply_to_addresses:
            return None
        name, address = reply_to_addresses[0]
    return Reporter(name=name, email=address)

def load_pmc_report(pmc: str, path: pathlib.Path) -> Report | None:
    with open(path) as f:
        emails = json.loads(f.read())

    m = re.match(r"(?:CVE-\S+\s+)*CVE-\S+", path.name)
    cves = m.group(0).split() if m else []

    jira = None
    if pmc in config.get().pmcs_using_jira:
        print(path.name)
        m = re.match(r"\S+ (\d+) .*", path.name)
        if m:
            jira = config.get().pmcs_using_jira[pmc] + "-" + m.group(1)
            print(jira)

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
    raw_subject = first_email['subj']
    try:
        title = "".join(
            s.decode(c or "ascii", errors="replace") if isinstance(s, bytes) else s
            for s, c in decode_header(raw_subject)
        )
    except Exception:
        title = raw_subject
    title = title.strip() or "(untitled)"
    if title.startswith("[SECURITY] "):
        title = title.removeprefix("[SECURITY] ")
    elif title.startswith("[Security] "):
        title = title.removeprefix("[Security] ")

    return Report(
        path.name,
        cves,
        jira,
        title,
        _asf_member_link(first_email),
        _project_link(emails) or _asf_member_link(first_email),
        _reporter(first_email),
        state,
        datetime.datetime.fromtimestamp(first_email['mailtime'], tz=datetime.timezone.utc),
    )

async def load_pmc_reports(pmc: str) -> list[Report]:
    if not re.fullmatch(r"[a-z0-9]+", pmc):
        raise ValueError("invalid PMC name: {pmc!r}")

    d = config.get().data_dir_path / pmc
    threads = list(d.glob('**/*.json'))

    return [ r for r in (load_pmc_report(pmc, t) for t in threads) if r is not None ]
