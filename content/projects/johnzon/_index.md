---
title: Apache Johnzon security advisories
description: Security information for Apache Johnzon
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache Johnzon? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Johnzon).

You can read more about the security policy on:

- [Apache Johnzon security model](https://johnzon.apache.org/security.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## ClassConverter loads & static-initializes an attacker-named class from untrusted JSON ## { #CVE-2026-71253 }

CVE-2026-71253 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-71253) [\[CVE json\]](./CVE-2026-71253.cve.json) [\[OSV json\]](./CVE-2026-71253.osv.json)



_Last updated: 2026-10-19T10:36:35.470Z_

### Affected

* Apache Johnzon from 2.0.0 before 2.2.0
* Apache Johnzon from 1.0.0 before 1.3.1


### Description

<p>Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection') vulnerability in Apache Johnzon.</p><p>ClassConverter loads &amp; static-initializes an attacker-named class from untrusted JSON.<br></p><p>This issue affects Apache Johnzon: from 1.0.0 before 2.2.0.</p><p>Users are recommended to upgrade to version 1.3.1 (javax namespace) or 2.2.0 (jakarta specification namespace), which fixes the issue.</p>

### References
* https://github.com/apache/johnzon/commit/dd3d00634c746a2173a2518e882e85e8a151bf30
* https://github.com/apache/johnzon/commit/91e7b0d21d08d138944e2570691939739422a3d6
* https://lists.apache.org/thread.html/3vgm1yo2sn9yhkvvs9lc4ro01vl3zt68


### Credits
* n0mi1k Security (finder)


## Prevent inefficient internal conversion from BigDecimal at large scale ## { #CVE-2023-33008 }

CVE-2023-33008 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-33008) [\[CVE json\]](./CVE-2023-33008.cve.json) [\[OSV json\]](./CVE-2023-33008.osv.json)



_Last updated: 2023-07-07T09:07:15.097Z_

### Affected

* Apache Johnzon through 1.2.20


### Description

<div>Deserialization of Untrusted Data vulnerability in Apache Software Foundation Apache Johnzon.<br></div><p>A malicious attacker can craft up some JSON input that uses large numbers (numbers such as&nbsp;1e20000000) that Apache Johnzon will deserialize into BigDecimal and maybe use numbers too large which may result in a slow conversion (Denial of service risk). Apache Johnzon 1.2.21 mitigates this by setting a scale limit of 1000 (by default) to the BigDecimal. <br></p><p>This issue affects Apache Johnzon: through 1.2.20.</p>

### References
* https://lists.apache.org/thread/qbg14djo95gfpk7o560lr8wcrzfyw43l


### Credits
* PJ Fanning (reporter)
* Jean-Louis Monteiro (remediation developer)
* Romain Manni-Bucau (remediation reviewer)
