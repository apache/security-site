---
title: Apache Abdera security advisories
description: Security information for Apache Abdera
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache Abdera? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Abdera).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## XML external entity expansion in Atom document parsing ## { #CVE-2026-113582 }

CVE-2026-113582 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-113582) [\[CVE json\]](./CVE-2026-113582.cve.json) [\[OSV json\]](./CVE-2026-113582.osv.json)



_Last updated: 2026-10-22T13:27:07.840Z_

### Affected

* Apache Abdera through *
* Apache Abdera through *
* Apache Abdera from cb5a3646fc8b2a620dba5bdde3a6b7a3753b1be2 through *


### Description

<p><strong>UNSUPPORTED WHEN ASSIGNED</strong> Improper restriction of XML external entity references in Apache Abdera allows an attacker to access sensitive data or make server-side requests when an application parses attacker-controlled XML with Abdera.</p><p>This issue affects Apache Abdera: all versions.</p><p>Apache Abdera is retired and no longer supported, so we do not plan to release a version that fixes this issue. Users are recommended to migrate to a maintained alternative. Applications that cannot migrate should ensure that untrusted XML cannot reach the affected Abdera parser or JDBC adapter parsing paths. Actively maintained downstream products may still be impacted if they include an affected Abdera artifact.</p><p><strong>NOTE:</strong> This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://attic.apache.org/projects/abdera.html
* https://lists.apache.org/thread.html/j32tow7bhfnn2p0obsqy1mhg1qs7hq91


### Credits
* Fabian Foerg of Addepar, Inc. (finder)
