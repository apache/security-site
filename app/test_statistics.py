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

import datetime
import json
import types

from app import statistics
from app.statistics import IssueWindow


def _ts(d: datetime.date) -> float:
    return datetime.datetime(d.year, d.month, d.day, tzinfo=datetime.timezone.utc).timestamp()


def test_is_open_at_window():
    w = IssueWindow(datetime.date(2025, 1, 1), datetime.date(2025, 1, 10))
    assert not w.is_open_at(datetime.date(2024, 12, 31))  # before opening
    assert w.is_open_at(datetime.date(2025, 1, 1))        # opened that day
    assert w.is_open_at(datetime.date(2025, 1, 9))        # mid-window
    assert not w.is_open_at(datetime.date(2025, 1, 10))   # closed that day
    assert not w.is_open_at(datetime.date(2025, 1, 11))


def test_is_open_at_still_open():
    w = IssueWindow(datetime.date(2025, 1, 1), None)
    assert not w.is_open_at(datetime.date(2024, 12, 31))
    assert w.is_open_at(datetime.date(2025, 1, 1))
    assert w.is_open_at(datetime.date(2030, 1, 1))


def test_debt_at_is_constant_plus_age():
    w = IssueWindow(datetime.date(2025, 1, 1), None)
    assert w.debt_at(datetime.date(2025, 1, 1)) == 100
    assert w.debt_at(datetime.date(2025, 1, 6)) == 105


def test_week_end_dates_last_point_is_today():
    now = datetime.datetime(2026, 6, 5, tzinfo=datetime.timezone.utc)
    dates = statistics._week_end_dates(now, weeks=52)
    assert len(dates) == 53
    assert dates[-1] == now.date()
    assert dates[0] == now.date() - datetime.timedelta(weeks=52)
    assert dates[1] - dates[0] == datetime.timedelta(weeks=1)


def test_issue_window_reads_first_and_last_mailtime(tmp_path):
    path = tmp_path / "thread.json"
    path.write_text(json.dumps([
        {"mailtime": _ts(datetime.date(2025, 1, 1))},
        {"mailtime": _ts(datetime.date(2025, 1, 20))},
    ]))
    assert statistics._issue_window(path, closed=False) == IssueWindow(
        datetime.date(2025, 1, 1), None
    )
    assert statistics._issue_window(path, closed=True) == IssueWindow(
        datetime.date(2025, 1, 1), datetime.date(2025, 1, 20)
    )


def test_issue_window_skips_empty(tmp_path):
    path = tmp_path / "empty.json"
    path.write_text("[]")
    assert statistics._issue_window(path, closed=False) is None


def test_issue_window_ignores_repeat_cve_pushed(tmp_path):
    # only the first "was pushed to cve.org" notification should count; the
    # later one must not drag the close date forward.
    path = tmp_path / "thread.json"
    path.write_text(json.dumps([
        {"mailtime": _ts(datetime.date(2025, 1, 1)), "subj": "[SECURITY] something"},
        {"mailtime": _ts(datetime.date(2025, 1, 20)), "subj": "CVE-2025-1 was pushed to cve.org"},
        {"mailtime": _ts(datetime.date(2025, 6, 1)), "subj": "CVE-2025-1 was pushed to cve.org"},
    ]))
    assert statistics._issue_window(path, closed=True) == IssueWindow(
        datetime.date(2025, 1, 1), datetime.date(2025, 1, 20)
    )


def _write_thread(path, opened, last=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    emails = [{"mailtime": _ts(opened)}]
    if last is not None:
        emails.append({"mailtime": _ts(last)})
    path.write_text(json.dumps(emails))


def test_compute_debt_chart_end_to_end(tmp_path, monkeypatch):
    # proj1: one still-open issue, plus one issue closed within the past year.
    # proj2: a non-issue (in archive) closed within the past year.
    proj1_open = IssueWindow(datetime.date(2026, 1, 1), None)
    proj1_closed = IssueWindow(datetime.date(2025, 8, 1), datetime.date(2026, 4, 1))
    proj2_ni = IssueWindow(datetime.date(2025, 9, 1), datetime.date(2026, 3, 1))

    _write_thread(tmp_path / "proj1" / "open.json", proj1_open.opened)
    _write_thread(
        tmp_path / "zzz-resolved" / "proj1" / "done.json",
        proj1_closed.opened, proj1_closed.closed,
    )
    _write_thread(
        tmp_path / "archive" / "zzz-non-issues" / "proj2" / "ni.json",
        proj2_ni.opened, proj2_ni.closed,
    )

    fake_cfg = types.SimpleNamespace(data_dir_path=tmp_path)
    monkeypatch.setattr(statistics.config, "get", lambda: fake_cfg)

    # 'archive' is not itself a project; the two real projects are discovered
    assert statistics.list_pmcs() == ["proj1", "proj2"]

    now = datetime.datetime(2026, 6, 5, tzinfo=datetime.timezone.utc)
    chart = statistics.compute_debt_chart(now=now, weeks=52)

    assert chart["weeks"][-1] == "now"
    boundaries = statistics._week_end_dates(now, weeks=52)
    series = {s["name"]: s["values"] for s in chart["series"]}
    assert set(series) == {"proj1", "proj2"}

    def debt(windows, end):
        return sum(w.debt_at(end) for w in windows if w.is_open_at(end))

    expected1 = [debt([proj1_open, proj1_closed], e) for e in boundaries]
    expected2 = [debt([proj2_ni], e) for e in boundaries]
    assert series["proj1"] == expected1
    assert series["proj2"] == expected2

    # sanity: the open issue keeps proj1 non-zero at 'now'; proj2's only issue is closed
    assert series["proj1"][-1] == 100 + (now.date() - proj1_open.opened).days
    assert series["proj2"][-1] == 0

    # restricting to a pmc set only returns those projects
    restricted = statistics.compute_debt_chart(now=now, weeks=52, pmcs=["proj1"])
    assert {s["name"] for s in restricted["series"]} == {"proj1"}
    # an empty allow-list yields no series
    assert statistics.compute_debt_chart(now=now, weeks=52, pmcs=[])["series"] == []
