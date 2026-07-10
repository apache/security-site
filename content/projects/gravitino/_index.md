---
title: Apache Gravitino security advisories
description: Security information for Apache Gravitino
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Gravitino? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unauthenticated callers can supply a malicious H2 JDBC URL through the testConnection API, which executes arbitrary Java code on the server via H2's INIT parameter ## { #CVE-2026-41042 }

CVE-2026-41042 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41042) [\[CVE json\]](./CVE-2026-41042.cve.json) [\[OSV json\]](./CVE-2026-41042.osv.json)



_Last updated: 2026-07-08T11:38:53.337Z_

### Affected

* Apache Gravitino before 1.2.1


### Description

<p>Unauthenticated callers can supply a malicious H2 JDBC URL through the testConnection API, which executes arbitrary Java code on the server via H2's INIT parameter. Vulnerability in Apache Gravitino.</p><p>This issue affects Apache Gravitino: before 1.2.1.</p><p>Users are recommended to upgrade to version 1.2.1, which fixes the issue.</p>This issue only happens when using H2, and H2 is mainly used for testing and local development. Also, Gravitino is typically deployed in the internal environment, so the severity is low.

### References
* https://lists.apache.org/thread/vdh88wc6j5b38v65ncb111wbbnkf6bvm


### Credits
* Junjie Li (Xidian University, https://github.com/jackieya) (reporter)


## SQL misconfiguration can access or truncate files ## { #CVE-2025-53648 }

CVE-2025-53648 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-53648) [\[CVE json\]](./CVE-2025-53648.cve.json) [\[OSV json\]](./CVE-2025-53648.osv.json)



_Last updated: 2026-06-30T13:35:54.650Z_

### Affected

* Apache Gravitino from 0.5.0 before 1.0.0


### Description

<p></p>SQL misconfiguration in the Gravitino UI, in versions 1.0.0 and below, can allow a malicious user to read or truncate files.<br>Users are recommended to upgrade to version 1.0.0, which fixes this issue.<p></p>

### References
* https://lists.apache.org/thread/s0hytcv17z52dwp5dojjjwgrtqtyh2xk


### Credits
* A1kaid@ThreatBook VulTeam (reporter)
* Le1a@ThreatBook VulTeam (finder)
