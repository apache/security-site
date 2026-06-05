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

"""Aggregate statistics across all projects, for the dashboard charts."""

from app import config
import dataclasses
import datetime
import json
import pathlib
import re

# Trees that sit at the data-dir root and mirror the per-project layout, holding
# issues that have since been closed: <data_dir>/<tree>/<project>/**/*.json
_CLOSED_TREES = (
    "zzz-resolved",
    "zzz-non-issues",
    "archive/zzz-resolved",
    "archive/zzz-non-issues",
)
# Top-level entries under the data dir that are not themselves projects.
_NON_PROJECT_DIRS = {"zzz-resolved", "zzz-non-issues", "archive"}


@dataclasses.dataclass(frozen=True)
class IssueWindow:
    """The time an issue was open: from `opened` until `closed` (None = still open)."""
    opened: datetime.date
    closed: datetime.date | None

    def is_open_at(self, when: datetime.date) -> bool:
        return self.opened <= when and (self.closed is None or self.closed > when)

    def debt_at(self, when: datetime.date) -> int:
        """Debt contribution at `when`: days since the issue was opened plus a constant."""
        return 100 + (when - self.opened).days


_CVE_PUSHED_SUFFIX = "was pushed to cve.org"


def _drop_repeat_cve_pushed(emails: list) -> list:
    """Keep only the first 'was pushed to cve.org' notification in a thread.

    These notifications can recur and would otherwise drag the close date
    (the last email's mailtime) later than the issue was really resolved.
    """
    result = []
    seen_pushed = False
    for email in emails:
        subj = (email.get("subj") or "").strip().lower()
        if subj.endswith(_CVE_PUSHED_SUFFIX):
            if seen_pushed:
                continue
            seen_pushed = True
        result.append(email)
    return result


def _issue_window(path: pathlib.Path, *, closed: bool) -> IssueWindow | None:
    """Extract the open/close dates from a thread JSON, or None if unusable.

    `opened` is the first email's mailtime; for closed issues `closed` is the
    last email's mailtime.
    """
    try:
        with open(path) as f:
            emails = json.loads(f.read())
    except (OSError, ValueError):
        return None
    if not emails:
        return None
    emails = _drop_repeat_cve_pushed(emails)
    opened_ts = emails[0].get("mailtime")
    if opened_ts is None:
        return None
    opened = datetime.datetime.fromtimestamp(opened_ts, tz=datetime.timezone.utc).date()
    closed_date: datetime.date | None = None
    if closed:
        closed_ts = emails[-1].get("mailtime", opened_ts)
        closed_date = datetime.datetime.fromtimestamp(
            closed_ts, tz=datetime.timezone.utc
        ).date()
        if closed_date < opened:
            closed_date = opened
    return IssueWindow(opened, closed_date)


def list_pmcs() -> list[str]:
    """All projects (PMCs), from both the open dir and the closed trees."""
    data_dir = config.get().data_dir_path
    if not data_dir.is_dir():
        return []
    names: set[str] = set()
    for p in data_dir.iterdir():
        if (
            p.is_dir()
            and p.name not in _NON_PROJECT_DIRS
            and re.fullmatch(r"[a-z0-9]+", p.name)
        ):
            names.add(p.name)
    for tree in _CLOSED_TREES:
        tree_path = data_dir / tree
        if tree_path.is_dir():
            for p in tree_path.iterdir():
                if p.is_dir() and re.fullmatch(r"[a-z0-9]+", p.name):
                    names.add(p.name)
    return sorted(names)


def _project_issue_windows(pmc: str) -> list[IssueWindow]:
    """Open/close windows for every issue of a project, open and closed alike."""
    data_dir = config.get().data_dir_path
    windows: list[IssueWindow] = []

    open_dir = data_dir / pmc
    if open_dir.is_dir():
        for path in open_dir.glob("**/*.json"):
            w = _issue_window(path, closed=False)
            if w is not None:
                windows.append(w)

    for tree in _CLOSED_TREES:
        tree_dir = data_dir / tree / pmc
        if tree_dir.is_dir():
            for path in tree_dir.glob("**/*.json"):
                w = _issue_window(path, closed=True)
                if w is not None:
                    windows.append(w)

    return windows


def _week_end_dates(now: datetime.datetime, weeks: int) -> list[datetime.date]:
    """`weeks` weekly boundaries over the past period, plus a final 'now' point."""
    today = now.date()
    boundaries = [today - datetime.timedelta(weeks=k) for k in range(weeks, 0, -1)]
    boundaries.append(today)
    return boundaries


def compute_debt_chart(
    now: datetime.datetime | None = None,
    weeks: int = 2 * 52,
    pmcs: "set[str] | list[str] | None" = None,
) -> dict:
    """Weekly project-debt series for every project over the past 2 years.

    Debt at the end of a period is the sum, over the issues open at that point,
    of the number of days since the issue was opened plus a constant. Issues from the closed trees
    stop contributing after their close date, so historical weeks reflect the
    issues that were genuinely open back then.

    If `pmcs` is given, only those projects are included; otherwise every
    project is included.
    """
    if now is None:
        now = datetime.datetime.now(tz=datetime.timezone.utc)
    boundaries = _week_end_dates(now, weeks)

    pmc_names = list_pmcs()
    if pmcs is not None:
        allowed = set(pmcs)
        pmc_names = [p for p in pmc_names if p in allowed]

    series: list[dict] = []
    for pmc in pmc_names:
        windows = _project_issue_windows(pmc)
        if not windows:
            continue
        values = [
            sum(w.debt_at(end) for w in windows if w.is_open_at(end))
            for end in boundaries
        ]
        if any(values):
            series.append({"name": pmc, "values": values})

    labels = [d.isoformat() for d in boundaries]
    labels[-1] = "now"
    return {"weeks": labels, "series": series}
