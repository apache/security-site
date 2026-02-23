---
title: Apache Kyuubi security advisories
description: Security information for Apache Kyuubi
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Kyuubi? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unauthorized directory access due to missing path normalization ## { #CVE-2025-66518 }

CVE-2025-66518 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-66518) [\[CVE json\]](./CVE-2025-66518.cve.json) [\[OSV json\]](./CVE-2025-66518.osv.json)



_Last updated: 2026-01-05T08:46:25.781Z_

### Affected

* Apache Kyuubi from 1.6.0 through 1.10.2


### Description

<p>Any client who can access to Apache Kyuubi Server via Kyuubi frontend protocols can bypass server-side config kyuubi.session.local.dir.allow.list and use local files which are not listed in the config.</p><p>This issue affects Apache Kyuubi: from 1.6.0 through 1.10.2.</p><p>Users are recommended to upgrade to version 1.10.3 or upper, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/xp460bwbyzdhho34ljd4nchyt2fmhodl


### Credits
* Hiroki Egawa (reporter)
* Hiroki Egawa (remediation developer)
