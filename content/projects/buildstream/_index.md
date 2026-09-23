---
title: Apache BuildStream security advisories
description: Security information for Apache BuildStream
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache BuildStream? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=BuildStream).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## tar source extraction escape ## { #CVE-2026-82331 }

CVE-2026-82331 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82331) [\[CVE json\]](./CVE-2026-82331.cve.json)

_Last updated: 2026-09-23T06:58:07.253Z_

### Affected

* Apache BuildStream through 2.8.0
* Apache BuildStream at 2.8.1 unaffected


### Description

Improper link resolution before file access ('link following') vulnerability in the `tar` source plugin of Apache BuildStream running on Python &lt; 3.12 allows malicious source tarballs to write files on the host, with the privileges of the user running BuildStream, via symlinks as part of source fetching.<br><div>The impact of this issue is mitigated by:</div>* BuildStream projects should only use trusted sources in their elements as otherwise the build output can also not be trusted<br>* Tracking a source tarball pins its SHA256 hash, which prevents MITM attacks of users that are fetching an already tracked project<br>* When running on Python &gt;= 3.12, BuildStream &gt;= 2.3.0 already makes use of the Python `tarfile` filter functionality, which blocks the symlink escape<br><br>Users are recommended to upgrade to version 2.8.1, which fixes this issue.

### References
* https://lists.apache.org/thread/9b342631x7bvtyg0pq7zgywtl2cmy34v


### Credits
* Gjoko Krstic of Zero Science Lab (finder)
