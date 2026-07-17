---
title: Apache Atlas security advisories
description: Security information for Apache Atlas
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Atlas? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=%5BFINDING%5D%20Apache%20Atlas).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Script injection allows access to unintended data ## { #CVE-2026-40563 }

CVE-2026-40563 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40563) [\[CVE json\]](./CVE-2026-40563.cve.json) [\[OSV json\]](./CVE-2026-40563.osv.json)



_Last updated: 2026-05-04T15:17:30.858Z_

### Affected

* Apache Atlas from 0.8 through 2.4.0


### Description

<p><b>Description:</b><br>Improper Control of Generation of Code ('Code Injection') vulnerability in Apache Atlas<br>Apache Atlas exposes a DSL search endpoint that accepts user-supplied query strings. Attacker can alter Gremlin traversal logic within grammar-allowed characters to access unintended data<br></p><p></p><p><b>Affect Version:</b><br>This issue affects Apache Atlas: from 0.8 through 2.4.0.</p><p></p><p>For the affect version &gt;= 2.0, vulnerability is only when Atlas is deployed with below non-default configuration.<br></p><div><pre>atlas.dsl.executor.traversal=false</pre></div><b>Mitigation:</b><br>Users are recommended to upgrade to version 2.5.0, which fixes the issue.<p></p>

### References
* https://lists.apache.org/thread/vd0oggmqxl2k1skm0z2f9p0plx7jhmfl


### Credits
* Khaled M. Alshammri (finder)
* qx L (finder)


## Stored XSS in Create Entity page ## { #CVE-2025-62198 }

CVE-2025-62198 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-62198) [\[CVE json\]](./CVE-2025-62198.cve.json) [\[OSV json\]](./CVE-2025-62198.osv.json)



_Last updated: 2026-06-22T07:47:10.790Z_

### Affected

* Apache Atlas through 2.4.0


### Description

<p>An authenticated user can perform XSS.</p><p>This issue affects Apache Atlas <span style="background-color: rgb(255, 255, 255);">versions </span>2.4.0 and earlier.</p><p>Users are recommended to upgrade to version 2.5.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/nv893lhz3ok08f25j3v4z1to5nrpdp7k


### Credits
* Grzegorz Misiun (finder)


## An authenticated user can perform XSS and potentially impersonate another user ## { #CVE-2024-46910 }

CVE-2024-46910 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-46910) [\[CVE json\]](./CVE-2024-46910.cve.json) [\[OSV json\]](./CVE-2024-46910.osv.json)



_Last updated: 2025-10-17T15:29:29.800Z_

### Affected

* Apache Atlas from 2.0.0 through 2.3.0


### Description

<p>An authenticated user can perform XSS and potentially impersonate another user.</p><p>This issue affects Apache Atlas <span style="background-color: rgb(255, 255, 255);">versions&nbsp;</span>2.3.0 and earlier.</p><p>Users are recommended to upgrade to version 2.4.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/sqzp34l4cdk21zoq5g31qlsvr7jvb1fy


### Credits
* SecIQ Technologies LLP (finder)
* Darpan Patel (SecIQ Technologies) (finder)


## zip path traversal in import functionality ## { #CVE-2022-34271 }

CVE-2022-34271 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-34271) [\[CVE json\]](./CVE-2022-34271.cve.json) [\[OSV json\]](./CVE-2022-34271.osv.json)



_Last updated: 2022-12-14T08:34:57.194Z_

### Affected

* Apache Atlas from 0.8.4 before 2.3.0


### Description

A vulnerability in import module of Apache Atlas allows an authenticated user to write to web server filesystem.  This issue affects Apache Atlas versions from 0.8.4 to 2.2.0.

### References
* https://lists.apache.org/thread/0rqvcxo6brmos9w3lzfsdn2lsmlblpw3


### Credits
* Huangzhicong (finder)
