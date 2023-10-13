---
title: Apache Johnzon security advisories
description: Security information for Apache Johnzon
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Johnzon? You can read more about the projects' security policy on their [security page](https://johnzon.apache.org/security.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://johnzon.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Prevent inefficient internal conversion from BigDecimal at large scale ## { #CVE-2023-33008 }

CVE-2023-33008 [\[CVE json\]](./CVE-2023-33008.cve.json)

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
