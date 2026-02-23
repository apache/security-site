---
title: Apache Uniffle security advisories
description: Security information for Apache Uniffle
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Uniffle? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Insecure SSL Configuration in Uniffle HTTP Client ## { #CVE-2025-68637 }

CVE-2025-68637 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-68637) [\[CVE json\]](./CVE-2025-68637.cve.json) [\[OSV json\]](./CVE-2025-68637.osv.json)



_Last updated: 2026-01-07T09:39:02.164Z_

### Affected

* Apache Uniffle before 0.10.0


### Description

<p>The Uniffle HTTP client is configured to trust all SSL certificates and</p><p><span style="background-color: rgb(255, 255, 255);">disables hostname verification by default. This insecure configuration</span><br><span style="background-color: rgb(255, 255, 255);">exposes all REST API communication between the Uniffle CLI/client and the</span><br><span style="background-color: rgb(255, 255, 255);">Uniffle Coordinator service to potential Man-in-the-Middle (MITM) attacks.</span><br></p><p>This issue affects all versions from before 0.10.0.</p><p>Users are recommended to upgrade to version 0.10.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/trvdd11hmpbjno3t8rc9okr4t036ox2v


### Credits
* omkar parkhe. (finder)
