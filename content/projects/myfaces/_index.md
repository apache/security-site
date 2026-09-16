---
title: Apache MyFaces security advisories
description: Security information for Apache MyFaces
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache MyFaces? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=MyFaces).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Denial of Service via Unbounded Request Parsing ## { #CVE-2026-76646 }

CVE-2026-76646 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-76646) [\[CVE json\]](./CVE-2026-76646.cve.json) [\[OSV json\]](./CVE-2026-76646.osv.json)



_Last updated: 2026-09-16T19:16:17.245Z_

### Affected

* Apache MyFaces from 2.2.0-beta through 2.2.15
* Apache MyFaces at 2.3.0
* Apache MyFaces from 2.3-next-M1 through 2.3-next-M8
* Apache MyFaces from 2.3.1 through 2.3.11
* Apache MyFaces from 3.0.0 through 3.0.3
* Apache MyFaces from 4.0.0 through 4.0.3
* Apache MyFaces from 4.1.0 through 4.1.3


### Description

<div><div><div><div><div><div><div><div><div><div><div><div><div><div><div><div><p>A remote attacker could cause excessive resource consumption by supplying specially crafted request parameters, potentially resulting in a denial of service condition.<br><br>
Older unsupported versions may also be affected.<br><br>Users are recommended to upgrade to versions 2.3.12, 2.3-next-M9, 3.0.4, 4.0.4, or 4.1.4, which fix this issue.</p></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div>

### References
* https://lists.apache.org/thread/q8zxrdhbmmx8ofgr9s7ymnqo8l2x8oy9


### Credits
* n0mi1k (reporter)


## Server-Side Request Forgery / Local File Inclusion Vulnerability ## { #CVE-2026-68536 }

CVE-2026-68536 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68536) [\[CVE json\]](./CVE-2026-68536.cve.json) [\[OSV json\]](./CVE-2026-68536.osv.json)



_Last updated: 2026-09-16T18:24:40.274Z_

### Affected

* Apache MyFaces from 2.2.0-beta through 2.2.15
* Apache MyFaces at 2.3.0
* Apache MyFaces from 2.3-next-M1 before 2.3-next-M9
* Apache MyFaces from 2.3.1 before 2.3.12
* Apache MyFaces from 3.0.0 before 3.0.4
* Apache MyFaces from 4.0.0 before 4.0.4
* Apache MyFaces from 4.1.0 before 4.1.4


### Description

Server-Side Request Forgery / Local File Inclusion in Apache MyFace Core.<br><br>Older unsupported versions may also be affected.&nbsp;<br><br>Users are recommended to upgrade to versions 2.3.12, 2.3-next-M9, 3.0.4, 4.0.4, or 4.1.4, which fix this issue.<br><br>

### References
* https://lists.apache.org/thread/4kwh2dys1sdcm3o4pbk41t2lt9or72qq


## Cross-Site Request Forgery (CSRF) vulnerability in Apache MyFaces ## { #CVE-2021-26296 }

CVE-2021-26296 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-26296) [\[CVE json\]](./CVE-2021-26296.cve.json) [\[OSV json\]](./CVE-2021-26296.osv.json)



_Last updated: 2021-02-19T08:27:26.368Z_

### Affected

* Apache MyFaces Core from Apache MyFaces Core 2.2 before 2.2.14
* Apache MyFaces Core from Apache MyFaces Core 2.3 before 2.3.8
* Apache MyFaces Core from Apache MyFaces Core 2.3-next before 2.3-next-M5
* Apache MyFaces Core from Apache MyFaces Core 3.0 before 3.0.0


### Description

In the default configuration, Apache MyFaces Core versions 2.2.0 to 2.2.13, 2.3.0 to 2.3.7, 2.3-next-M1 to 2.3-next-M4, and 3.0.0-RC1 use cryptographically weak implicit and explicit cross-site request forgery (CSRF) tokens. Due to that limitation, it is possible (although difficult) for an attacker to calculate a future CSRF token value and to use that value to trick a user into executing unwanted actions on an application.

### References
* https://lists.apache.org/thread.html/r2b73e2356c6155e9ec78fdd8f72a4fac12f3e588014f5f535106ed9b%40%3Cannounce.apache.org%3E


### Credits
* Apache MyFaces would like to thank Wolfgang Ettlinger (Certitude Consulting GmbH)
