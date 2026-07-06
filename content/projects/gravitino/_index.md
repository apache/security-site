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
