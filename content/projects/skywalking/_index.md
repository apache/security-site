---
title: Apache SkyWalking security advisories
description: Security information for Apache SkyWalking
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache SkyWalking? You can read more about the projects' security policy on their [security page](https://skywalking.apache.org/docs/main/next/en/security/readme/), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://skywalking.apache.org/docs/main/next/en/security/readme/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Server-Side Request Forgery via SW-URL Header in MCP Server ## { #CVE-2026-34476 }

CVE-2026-34476 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34476) [\[CVE json\]](./CVE-2026-34476.cve.json) [\[OSV json\]](./CVE-2026-34476.osv.json)



_Last updated: 2026-04-13T13:00:58.883Z_

### Affected

* Apache SkyWalking MCP at 0.1.0


### Description

<div>Server-Side Request Forgery via SW-URL Header vulnerability in Apache SkyWalking MCP.<p></p><p>This issue affects Apache SkyWalking MCP: 0.1.0.</p>Users are recommended to upgrade to version 0.2.0, which fixes this issue.<br></div><br>

### References
* https://lists.apache.org/thread/v0k1xyzzbtnpyrwxwyn36pbspr8rhjnr


### Credits
* Andrea Cosentino <ancosen@gmail.com> (reporter)


## The SkyWalking OAP /debugging/config/dump endpoint may leak sensitive configuration information of MySQL/PostgreSQL. ## { #CVE-2026-30778 }

CVE-2026-30778 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-30778) [\[CVE json\]](./CVE-2026-30778.cve.json) [\[OSV json\]](./CVE-2026-30778.osv.json)



_Last updated: 2026-04-15T10:54:23.696Z_

### Affected

* Apache SkyWalking from 9.7.0 through 10.3.0


### Description

<p>The SkyWalking OAP /debugging/config/dump endpoint may leak sensitive configuration information of MySQL/PostgreSQL.</p><p>This issue affects Apache SkyWalking: from 9.7.0 through 10.3.0.</p><p>Users are recommended to upgrade to version 10.4.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/pvf35o3tp1rqhmrhzj6fg31gvqrqcvn3


### Credits
* shuiboye@gmail.com (reporter)


## Stored XSS vulnerability ## { #CVE-2025-54057 }

CVE-2025-54057 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-54057) [\[CVE json\]](./CVE-2025-54057.cve.json) [\[OSV json\]](./CVE-2025-54057.osv.json)



_Last updated: 2026-04-13T12:24:00.847Z_

### Affected

* Apache SkyWalking through 10.2.0


### Description

<p>Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in Apache SkyWalking.</p><p>This issue affects Apache SkyWalking: &lt;= 10.2.0.</p><p>Users are recommended to upgrade to version 10.3.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/sl2x2tx8y007x0mo746yddx2lvnv9tcr


### Credits
* Vinh Nguyễn Quang (vinhnq4902@gmail.com) (reporter)


## Service unavailability impact in NodeJS agent(version <= 0.5.0) ## { #CVE-2022-36127 }

CVE-2022-36127 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-36127) [\[CVE json\]](./CVE-2022-36127.cve.json) [\[OSV json\]](./CVE-2022-36127.osv.json)



_Last updated: 2022-07-18T11:24:38.575Z_

### Affected

* Apache SkyWalking NodeJS Agent from Apache SkyWalking NodeJS Agent through 0.5.0


### Description

A vulnerability in Apache SkyWalking NodeJS Agent prior to 0.5.1. The vulnerability will cause NodeJS services that has this agent installed to be unavailable if the OAP is unhealthy and NodeJS agent can't establish the connection.

### References
* https://lists.apache.org/thread/x238wo4r5goy39dxdjcmlofp6gcdnqr3
