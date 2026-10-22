---
title: Apache Fesod (Incubating) security advisories
description: Security information for Apache Fesod (Incubating)
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache Fesod (Incubating)? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Fesod%20%28Incubating%29).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improper validation of user-supplied URLs leading to SSRF ## { #CVE-2026-49328 }

CVE-2026-49328 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49328) [\[CVE json\]](./CVE-2026-49328.cve.json) [\[OSV json\]](./CVE-2026-49328.osv.json)



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


## UrlImageConverter SSRF protection bypass via DNS rebinding ## { #CVE-2026-107460 }

CVE-2026-107460 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-107460) [\[CVE json\]](./CVE-2026-107460.cve.json) [\[OSV json\]](./CVE-2026-107460.osv.json)



_Last updated: 2026-10-13T14:16:01.206Z_

### Affected

* Apache Fesod (Incubating) at 2.0.2-incubating


### Description

Server-Side Request Forgery (SSRF) protection in the UrlImageConverter component of Apache Fesod (Incubating) fesod-sheet 2.0.2-incubating can be bypassed through DNS rebinding. When an application accepts an attacker-controlled image URL for spreadsheet writing, the converter checks the hostname's resolved IP addresses and then opens a separate connection that can resolve the hostname again. An attacker who controls DNS responses for the URL hostname may cause the connection to reach a restricted address after validation. CVE-2026-49328 covers SSRF in releases before 2.0.2-incubating; this issue is a DNS rebinding bypass of the protection in 2.0.2-incubating. Apache Fesod (Incubating) 2.1.0-incubating addresses the reported default-fetch scenario by disabling remote URL image fetching by default and requiring an explicit exact-host allowlist when the feature is enabled. Users should upgrade to 2.1.0-incubating. Applications enabling remote URL image fetching should allowlist only hostnames whose DNS and HTTP services are trusted.

### References
* https://github.com/apache/fesod/pull/1035
* https://github.com/apache/fesod/releases/tag/2.1.0-incubating
* https://cve.org/CVERecord?id=CVE-2026-49328
* https://lists.apache.org/thread/oh706yhm32hmw8vx4kh1948h952pfr83


### Credits
* Venkatraman Kumar (reporter)
* Wenhao Zeng (reporter)
* Wanxin Yin (reporter)
* George Chen (reporter)
* Zeka Irving (Thresh) (reporter)
