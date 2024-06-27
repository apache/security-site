---
title: Apache HugeGraph security advisories
description: Security information for Apache HugeGraph
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache HugeGraph? You can read more about the projects' security policy on their [security page](https://hugegraph.apache.org/docs/guides/security), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://hugegraph.apache.org/docs/guides/security). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## SSRF in Hubble connection page ## { #CVE-2024-27347 }

CVE-2024-27347 [\[CVE json\]](./CVE-2024-27347.cve.json)

_Last updated: 2024-04-22T14:07:30.816Z_

### Affected

* Apache HugeGraph-Hubble from 1.0.0 before 1.3.0


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache HugeGraph-Hubble.<p>This issue affects Apache HugeGraph-Hubble: from 1.0.0 before 1.3.0.</p><p>Users are recommended to upgrade to version 1.3.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/z0v71148slfkw60hsp35pl7ddjyvg01l


### Credits
* 6right of moresec (reporter)


## Command execution in gremlin ## { #CVE-2024-27348 }

CVE-2024-27348 [\[CVE json\]](./CVE-2024-27348.cve.json)

_Last updated: 2024-04-22T14:08:03.374Z_

### Affected

* Apache HugeGraph-Server from 1.0.0 before 1.3.0


### Description

RCE-Remote Command Execution vulnerability in Apache HugeGraph-Server.<p>This issue affects Apache HugeGraph-Server: from 1.0.0 before 1.3.0 in Java8 &amp; Java11</p><p>Users are recommended to upgrade to version 1.3.0 with Java11 &amp; enable the Auth system, which fixes the issue.</p>

### References
* https://hugegraph.apache.org/docs/config/config-authentication/#configure-user-authentication
* https://lists.apache.org/thread/nx6g6htyhpgtzsocybm242781o8w5kq9


### Credits
* 6right of moresec (reporter)


## Bypass whitelist in Auth mode ## { #CVE-2024-27349 }

CVE-2024-27349 [\[CVE json\]](./CVE-2024-27349.cve.json)

_Last updated: 2024-04-22T14:08:39.984Z_

### Affected

* Apache HugeGraph-Server from 1.0.0 before 1.3.0


### Description

Authentication Bypass by Spoofing vulnerability in Apache HugeGraph-Server.<p>This issue affects Apache HugeGraph-Server: from 1.0.0 before 1.3.0.</p><p>Users are recommended to upgrade to version 1.3.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/dz9n9lndqfsf64t72o73r7sttrc6ocsd


### Credits
* 6right of moresec (reporter)
