---
title: Apache Oozie security advisories
description: Security information for Apache Oozie
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Oozie? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Oozie local privilege escalation ## { #CVE-2020-35451 }

CVE-2020-35451 [\[CVE json\]](./CVE-2020-35451.cve.json)

_Last updated: 2021-03-09T15:14:53.244Z_

### Affected

* Apache Oozie from unspecified before 5.2.1


### Description

There is a race condition in OozieSharelibCLI in Apache Oozie before version 5.2.1 which allows a malicious attacker to replace the files in Oozie's sharelib during it's creation. 

### References
* https://lists.apache.org/thread.html/r8688debdb8b586aab3e53dee2d675fc9212de0ec627a8d3cd43b5ab5%40%3Cuser.oozie.apache.org%3E


### Credits
* The Apache Oozie PMC would like to thank Jonathan Leitschuh for reporting the issue
