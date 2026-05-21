#!/usr/bin/env python3
"""Build the "Hall of Thanks" page from Apache CVE JSON files.

Walks a directory of *.cve.json (CVE 5.x or legacy 4.0), reads
``containers.cna.credits`` (or ``credit``), splits multi-person
values like "A and B", "A, B, and C", "A & B" into individual
entries, strips affiliations such as "(Org)" / "of Org",
ranks contributors and writes a Hugo markdown page.

Usage:
    python extract-credits.py [INPUT_DIR] [-o OUTPUT.md]
Defaults to scanning ../static/projects and writing
../content/hall-of-thanks/_index.md.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Iterator

# ---------------------------------------------------------------------------
# Regex helpers
# ---------------------------------------------------------------------------

# "Apache X would like to thank ... for reporting/discovering ..."
_THANK_PREFIX = re.compile(
    r"""^\s*
        (?:the\s+)?
        (?:Apache[\w\s\-]*?\s+(?:PMC|Team|project)?\s*)?
        (?:would\s+like\s+to\s+thank|wishes?\s+to\s+thank|thanks?)
        \s+
    """,
    re.IGNORECASE | re.VERBOSE,
)

# Lead-ins like "Reported by", "Discovered and reported by",
# "This issue was reported to the Apache X team by", etc.
_REPORTED_BY_PREFIX = re.compile(
    r"""^\s*
        (?:additionally|additoinally|also)?\s*
        (?:we\s+)?
        (?:would\s+like\s+to\s+thank\s+)?
        (?:this\s+(?:issue|vulnerability)\s+was\s+
            (?:reported|discovered|found)
            (?:\s+to\s+the\s+[\w\s\-]+?\s+team)?
            \s+by\s+
        |
            (?:independently\s+)?
            (?:reported|discovered|found|credited)
            (?:\s+and\s+(?:reported|discovered|found))?
            \s+by\s+
        )
    """,
    re.IGNORECASE | re.VERBOSE,
)

# Trailing boilerplate: "for (independently )?(reporting|discovering) this (issue|vulnerability)."
_THANK_SUFFIX = re.compile(
    r"""\s+for\s+
        (?:independently\s+)?
        (?:reporting|discovering|finding|disclosing)
        (?:\s+(?:and\s+(?:reporting|disclosing|fixing)))?
        \s+(?:this|the)\s+(?:issue|vulnerability|bug|flaw)\.?\s*$
    """,
    re.IGNORECASE | re.VERBOSE,
)

# Top-level splitters, applied only outside of () / [] / "" so we don't
# break things like "Sayooj B Kumar(Team bi0s & CRED Security team)".
# Order matters: handle ", and" / "; and" before plain "and".
_TOP_SPLITTERS = [
    re.compile(r",\s+and\s+", re.IGNORECASE),
    re.compile(r";\s+and\s+", re.IGNORECASE),
    re.compile(r"\s*;\s+"),
    re.compile(r"\s+and\s+", re.IGNORECASE),
    re.compile(r"\s+&\s+"),
    re.compile(r"\s+/\s+"),
]

# A name fragment is "too long" / sentence-like if it contains these markers,
# in which case we keep it as-is rather than risk wrong splits.
_SENTENCE_HINT = re.compile(r"https?://|github\.com|pull\s+request|commit\s+\w{6,}", re.I)

# Stray boilerplate sometimes left attached to a name fragment.
_LEADING_TO = re.compile(r"^\s*to\s+", re.IGNORECASE)
_FOR_REPORTING_TAIL = re.compile(
    r"\s+for\s+reporting(?:\s+this)?(?:\s+(?:issue|vulnerability))?\.?\s*$",
    re.IGNORECASE,
)
# "A of XX" / "A at XX" / "A from XX" / "A with XX" / "A in XX" tail.
_AFFILIATION_TAIL = re.compile(
    r"\s*,?\s+(?:of|at|from|with|in)\s+(?:the\s+)?\S.*$",
    re.IGNORECASE,
)


def _split_top_level(text: str, pattern: re.Pattern) -> list[str]:
    """Split *text* on *pattern* only at bracket/quote depth 0."""
    out: list[str] = []
    depth = 0
    in_quote: str | None = None
    last = 0
    i = 0
    while i < len(text):
        ch = text[i]
        if in_quote:
            if ch == in_quote:
                in_quote = None
            i += 1
            continue
        if ch in ("\"", "'"):
            in_quote = ch
            i += 1
            continue
        if ch in "([{":
            depth += 1
            i += 1
            continue
        if ch in ")]}":
            depth = max(0, depth - 1)
            i += 1
            continue
        if depth == 0:
            m = pattern.match(text, i)
            if m:
                out.append(text[last:i])
                last = m.end()
                i = m.end()
                continue
        i += 1
    out.append(text[last:])
    return out


# Strip wrapping quotes / stray punctuation from a name fragment.
_TRIM_CHARS = " \t\r\n.\"'`"


def _strip_affiliation(name: str) -> str:
    """Drop trailing affiliation: "A (XX)", "A [..]", "A <email>", "A of XX".

    Keeps a parenthesised handle like "(@foo)" since it identifies the person.
    If the whole fragment is just an email/handle, it is returned unchanged.
    """
    s = name.strip()
    s = _LEADING_TO.sub("", s)
    s = _FOR_REPORTING_TAIL.sub("", s)

    # Drop a trailing "<email@host>" git-author-style tag, but only if the
    # name has something else before it (so a bare "<x@y>" stays put).
    m = re.match(r"^(.+?)\s*<[^>\s]+@[^>\s]+>\s*$", s)
    if m and m.group(1).strip(_TRIM_CHARS):
        s = m.group(1).strip()

    # Repeatedly peel trailing [..] / (..) blocks; keep "(@handle)" but
    # always drop "(https://...)" / "(http://...)".
    while True:
        if s.endswith("]"):
            i = s.rfind("[")
            if i >= 0:
                s = s[:i].rstrip(" ,;")
                continue
        if s.endswith(")"):
            i = s.rfind("(")
            if i >= 0:
                inner = s[i + 1:-1].strip()
                is_url = bool(re.match(r"https?://", inner, re.I))
                if is_url or not inner.startswith("@"):
                    s = s[:i].rstrip(" ,;")
                    continue
        break

    # Strip "<name> of/at/from/with <org>" tail at top level only.
    stripped = _split_top_level(s, _AFFILIATION_TAIL)[0].strip(_TRIM_CHARS)
    # Guard against eating real names: if the stripped result is empty or a
    # meaningless stopword like "a"/"the"/"a team", keep the longer form.
    if not stripped or re.fullmatch(r"(?:a|an|the|a\s+team|the\s+team)", stripped, re.I):
        return s.strip(_TRIM_CHARS)
    return stripped



def _strip_boilerplate(value: str) -> str:
    """Remove leading thank/report phrases and trailing 'for reporting...'."""
    out = value.strip()
    # Repeatedly peel matching prefixes (some values have stacked phrases).
    for _ in range(3):
        new = _THANK_PREFIX.sub("", out)
        new = _REPORTED_BY_PREFIX.sub("", new)
        if new == out:
            break
        out = new
    out = _THANK_SUFFIX.sub("", out)
    return out.strip(_TRIM_CHARS)


def _split_names(value: str) -> list[str]:
    """Split a free-form credit value into individual names."""
    cleaned = _strip_boilerplate(value)
    if not cleaned:
        return []

    # If the fragment looks like a full sentence with URLs / PR refs,
    # don't try to atomize it; still try to strip a trailing URL or
    # affiliation so "Foo (https://...)" collapses to "Foo".
    if _SENTENCE_HINT.search(cleaned):
        single = _strip_affiliation(cleaned)
        return [single] if single else []

    parts: list[str] = [cleaned]
    for splitter in _TOP_SPLITTERS:
        next_parts: list[str] = []
        for p in parts:
            next_parts.extend(_split_top_level(p, splitter))
        parts = next_parts

    # A bare comma is ambiguous ("Lee, Wei" vs "Alice, Bob"). Only split on
    # commas when the original value already showed a multi-person pattern
    # (i.e. it produced >1 part above OR contained " and "/" & ").
    multi_person_signal = len(parts) > 1 or re.search(r"\s+(?:and|&)\s+", value, re.I)
    if multi_person_signal:
        comma_split: list[str] = []
        for p in parts:
            # Skip splitting "Last, First" style: comma followed by a single
            # short token (<=2 words, no role/affiliation marker).
            chunks = [c.strip() for c in _split_top_level(p, re.compile(r"\s*,\s*"))]
            rebuilt: list[str] = []
            i = 0
            while i < len(chunks):
                cur = chunks[i]
                nxt = chunks[i + 1] if i + 1 < len(chunks) else None
                if (
                    nxt is not None
                    and len(nxt.split()) <= 2
                    and not re.search(r"\b(of|at|from|the|inc|ltd|llc|gmbh|team|lab|university|corp)\b", nxt, re.I)
                ):
                    # Treat as a single "Last, First" name.
                    rebuilt.append(f"{cur}, {nxt}")
                    i += 2
                else:
                    rebuilt.append(cur)
                    i += 1
            comma_split.extend(rebuilt)
        parts = comma_split

    # Final cleanup & dedupe while preserving order.
    seen: set[str] = set()
    result: list[str] = []
    for p in parts:
        name = p.strip(_TRIM_CHARS)
        # Remove leading conjunctions left over from imperfect splits.
        name = re.sub(r"^(?:and|&|both)\s+", "", name, flags=re.I).strip(_TRIM_CHARS)
        # Drop trailing affiliation so "A of XX" / "A (XX)" -> "A".
        name = _strip_affiliation(name)
        if not name:
            continue
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(name)
    return result


# ---------------------------------------------------------------------------
# JSON traversal
# ---------------------------------------------------------------------------

def _iter_credit_entries(doc: dict) -> Iterator[tuple[str, str | None]]:
    """Yield (raw_value, type) tuples from a CVE JSON document."""
    cna = (doc.get("containers") or {}).get("cna") or {}

    # CVE 5.x style.
    for c in cna.get("credits") or []:
        if isinstance(c, dict):
            v = c.get("value")
            if isinstance(v, str) and v.strip():
                yield v, c.get("type")
        elif isinstance(c, str) and c.strip():
            yield c, None

    # Legacy CVE 4.0 style: usually empty, occasionally a list of strings.
    for c in cna.get("credit") or []:
        if isinstance(c, dict):
            v = c.get("value")
            if isinstance(v, str) and v.strip():
                yield v, c.get("type")
        elif isinstance(c, str) and c.strip():
            yield c, None


def _iter_cve_files(root: str) -> Iterator[str]:
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.endswith(".cve.json"):
                yield os.path.join(dirpath, name)


def _looks_like_name(name: str) -> bool:
    """Reject obvious non-name fragments: pure URLs, leftover boilerplate."""
    if not name:
        return False
    if re.match(r"^https?://", name, re.I):
        return False
    if re.match(r"^(?:this\s+(?:issue|vulnerability)|reported|discovered|found|the\s+\w)\b",
                name, re.I):
        return False
    return True


def extract(root: str) -> list[dict]:
    rows: list[dict] = []
    for path in _iter_cve_files(root):
        try:
            with open(path, "r", encoding="utf-8") as f:
                doc = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"[warn] cannot parse {path}: {exc}", file=sys.stderr)
            continue

        cve_id = ((doc.get("cveMetadata") or {}).get("cveId")
                  or os.path.basename(path).split(".")[0])
        # Project = parent directory name under static/projects/<pmc>/...
        project = os.path.basename(os.path.dirname(path))

        for raw_value, ctype in _iter_credit_entries(doc):
            for name in _split_names(raw_value):
                if not _looks_like_name(name):
                    continue
                rows.append({
                    "project": project,
                    "cve_id": cve_id,
                    "name": name,
                    "type": ctype or "",
                    "raw_value": raw_value,
                    "file": os.path.relpath(path, root),
                })
    return rows


# ---------------------------------------------------------------------------
# Hall of Thanks rendering
# ---------------------------------------------------------------------------

# Top N contributors and how many top projects to show per contributor.
TOP_N = 100
PROJECTS_PER_PERSON = 5

# Hand-curated set of well-known Apache projects. Membership is what matters;
# order inside the set is irrelevant. A contributor's projects are shown with
# members of this set first, the rest after, each group keeping alphabetical
# order. Add or remove slugs here to tune the page.
FAMOUS_PROJECTS: frozenset[str] = frozenset({
    "httpd", "tomcat", "kafka", "spark", "hadoop", "logging",
    "lucene", "solr", "maven", "subversion", "zookeeper",
    "struts", "flink", "airflow", "pulsar", "hive", "hbase",
    "shiro", "dubbo", "activemq", "cxf", "commons","superset",
    "groovy", "storm", "calcite"
})


# Known alias -> canonical display name mapping. Add an entry whenever there
# is concrete evidence (e.g. the researcher self-identified in a CVE credit,
# blog post, or social profile) that two credit spellings refer to the same
# person. Currently confirmed:
#   - "Qing Xu" is the same researcher as "4ra1n".
# Add new entries below as more identities are confirmed.
NAME_ALIASES: dict[str, str] = {
    "qing xu": "4ra1n (Qing Xu)",
    "4ra1n": "4ra1n (Qing Xu)",
}


def _load_project_names(scripts_dir: str) -> dict[str, str]:
    """Load slug -> display name from project-coordinates.json (best effort)."""
    path = os.path.join(scripts_dir, "project-coordinates.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}
    return {slug: (info.get("name") or slug) for slug, info in data.items() if isinstance(info, dict)}


# Slugs whose canonical Apache name differs from a simple Title-Case fallback.
# Used only when project-coordinates.json has no entry for the slug.
_SLUG_NAME_OVERRIDES: dict[str, str] = {
    "ofbiz": "Apache OFBiz",
    "cxf": "Apache CXF",
    "jspwiki": "Apache JSPWiki",
    "pdfbox": "Apache PDFBox",
    "plc4x": "Apache PLC4X",
    "openoffice": "Apache OpenOffice",
    "openmeetings": "Apache OpenMeetings",
    "couchdb": "Apache CouchDB",
    "rocketmq": "Apache RocketMQ",
    "activemq": "Apache ActiveMQ",
    "iotdb": "Apache IoTDB",
    "nuttx": "Apache NuttX",
    "mxnet": "Apache MXNet",
    "shardingsphere": "Apache ShardingSphere",
    "skywalking": "Apache SkyWalking",
    "trafficserver": "Apache Traffic Server",
    "trafficcontrol": "Apache Traffic Control",
    "httpcomponents": "Apache HttpComponents",
    "httpd": "Apache HTTP Server",
    "subversion": "Apache Subversion",
    "zookeeper": "Apache ZooKeeper",
    "dolphinscheduler": "Apache DolphinScheduler",
    "streampark": "Apache StreamPark",
    "streampipes": "Apache StreamPipes",
    "seatunnel": "Apache SeaTunnel",
    "hugegraph": "Apache HugeGraph",
    "kvrocks": "Apache Kvrocks",
    "eventmesh": "Apache EventMesh",
    "kyuubi": "Apache Kyuubi",
    "shenyu": "Apache ShenYu",
    "servicecomb": "Apache ServiceComb",
    "hertzbeat": "Apache HertzBeat",
    "uniffle": "Apache Uniffle",
    "mynewt": "Apache Mynewt",
    "lucenenet": "Apache Lucene.Net",
    "carbondata": "Apache CarbonData",
    "asterixdb": "Apache AsterixDB",
    "systemds": "Apache SystemDS",
    "manifoldcf": "Apache ManifoldCF",
    "any23": "Apache Any23",
    "apr": "Apache Portable Runtime (APR)",
    "db": "Apache DB",
    "ws": "Apache WS",
}


def _pretty_project_name(slug: str, project_names: dict[str, str]) -> str:
    """Resolve a slug to its display name.

    Priority: project-coordinates.json -> manual override -> "Apache <Title>".
    """
    if slug in project_names:
        return project_names[slug]
    if slug in _SLUG_NAME_OVERRIDES:
        return _SLUG_NAME_OVERRIDES[slug]
    return f"Apache {slug.capitalize()}"


def _aggregate(rows: list[dict]) -> dict[str, dict]:
    """Build per-contributor stats keyed by lowercase canonical name."""
    contributors: dict[str, dict] = {}
    for r in rows:
        # Apply known alias mapping so the same person under multiple names
        # collapses into one entry.
        canonical = NAME_ALIASES.get(r["name"].lower(), r["name"])
        key = canonical.lower()
        c = contributors.setdefault(key, {
            "display": canonical,
            "cves": set(),
            "projects": set(),
        })
        c["cves"].add(r["cve_id"])
        c["projects"].add(r["project"])
    return contributors


def _render_markdown(rows: list[dict], project_names: dict[str, str]) -> str:
    contributors = _aggregate(rows)

    # Rank: by CVE count desc, then alphabetical (case-insensitive).
    ranked = sorted(
        contributors.values(),
        key=lambda c: (-len(c["cves"]), c["display"].lower()),
    )[:TOP_N]

    # Generation timestamp in UTC so the page is unambiguous across regions.
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = [
        "---",
        "title: Hall of Thanks",
        "description: Top security researchers credited across Apache project advisories.",
        "layout: single",
        "---",
        "",
        "This page recognises external researchers credited in Apache project security "
        "advisories.",
        "",
        f"_Last updated: {generated_at}._",
        "",
        "_Names are extracted automatically from CVE records; if you spot an error, "
        "please [contact us](mailto:security@apache.org)._",
        "",
        "| # | Contributor | CVEs | Top projects |",
        "| ---: | --- | ---: | --- |",
    ]

    # Medal prefixes for the top 3; rest use a plain rank number.
    medals = {1: "🥇", 2: "🥈", 3: "🥉"}

    for idx, c in enumerate(ranked, start=1):
        # Show famous projects first (membership-based, no internal ranking),
        # then the rest; both groups alphabetical by display name.
        top_projects = sorted(
            c["projects"],
            key=lambda p: (0 if p in FAMOUS_PROJECTS else 1,
                           _pretty_project_name(p, project_names).lower()),
        )[:PROJECTS_PER_PERSON]
        pretty = ", ".join(_pretty_project_name(p, project_names) for p in top_projects)
        # Escape pipe characters that would break the markdown table.
        name_cell = c["display"].replace("|", "\\|")
        proj_cell = pretty.replace("|", "\\|")
        # Highlight the top 3 with a medal and bold name.
        if idx in medals:
            rank_cell = f"{medals[idx]} {idx}"
            name_cell = f"**{name_cell}**"
            cve_cell = f"**{len(c['cves'])}**"
        else:
            rank_cell = str(idx)
            cve_cell = str(len(c["cves"]))
        lines.append(f"| {rank_cell} | {name_cell} | {cve_cell} | {proj_cell} |")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    default_input = os.path.normpath(os.path.join(scripts_dir, "..", "static", "projects"))
    default_output = os.path.normpath(
        os.path.join(scripts_dir, "..", "content", "hall-of-thanks", "_index.md")
    )

    p = argparse.ArgumentParser(
        description="Build the Hall of Thanks page from Apache CVE JSON files."
    )
    p.add_argument("input_dir", nargs="?", default=default_input,
                   help=f"Root directory to scan (default: {default_input})")
    p.add_argument("-o", "--output", default=default_output,
                   help=f"Markdown file to write (default: {default_output})")
    args = p.parse_args(argv)

    if not os.path.isdir(args.input_dir):
        print(f"error: {args.input_dir} is not a directory", file=sys.stderr)
        return 2

    rows = extract(args.input_dir)
    project_names = _load_project_names(scripts_dir)
    md = _render_markdown(rows, project_names)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Scanned {args.input_dir}")
    # Distinct (cve, contributor) pairs are the true measure of contributions;
    # raw row count can be inflated when a CVE credits the same person under
    # multiple roles (finder + reporter, etc.).
    distinct_pairs = len({(r["cve_id"], r["name"].lower()) for r in rows})
    n_contributors = len({r["name"].lower() for r in rows})
    print(f"Extracted {distinct_pairs} distinct (CVE, contributor) pairs "
          f"from {len(rows)} raw rows; "
          f"top {min(TOP_N, n_contributors)} contributors "
          f"written to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
