---
title: Apache Fesod (Incubating) security advisories
description: Security information for Apache Fesod (Incubating)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Fesod (Incubating)? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Fesod%20%28Incubating%29).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improper validation of user-supplied URLs leading to SSRF ## { #CVE-2026-49328 }

CVE-2026-49328 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49328) [\[CVE json\]](./CVE-2026-49328.cve.json)

_Last updated: 2026-06-01T10:10:32.924Z_

### Affected

* Apache Fesod (Incubating) before 2.0.2-incubating


### Description

Server-Side Request Forgery (SSRF) in the UrlImageConverter component of Apache Fesod (Incubating) fesod-sheet before 2.0.2-incubating allows attackers to cause outbound network requests to internal or otherwise restricted resources via a user-supplied image URL. Users are recommended to upgrade to version 2.0.2-incubating, which fixes this issue.

### References
* https://github.com/apache/fesod/pull/917
* https://github.com/apache/fesod/releases/tag/2.0.2-incubating
* https://fesod.apache.org/docs/download
* https://lists.apache.org/thread/c1pb5b66h02p9tlrnfbwcgcz85v16fkj


### Credits
* Xu Han (finder)
