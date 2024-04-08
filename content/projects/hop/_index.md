---
title: Apache Hop security advisories
description: Security information for Apache Hop
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Hop? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## ID isn't escaped when generating HTML ## { #CVE-2024-24683 }

CVE-2024-24683 [\[CVE json\]](./CVE-2024-24683.cve.json)

_Last updated: 2024-03-19T08:20:12.966Z_

### Affected

* Apache Hop Engine before 2.8.0


### Description

Improper Input Validation vulnerability in Apache Hop Engine.<p>This issue affects Apache Hop Engine: before 2.8.0.</p><p>Users are recommended to upgrade to version 2.8.0, which fixes the issue.</p>When Hop Server writes links to the&nbsp;PrepareExecutionPipelineServlet page one of the parameters provided to the user was not properly escaped.<br>The variable not properly escaped is the "id", which is not directly accessible by users creating pipelines making the risk of exploiting this low.<br><br>This issue only affects users using the Hop Server component and does not directly affect the client.

### References
* https://lists.apache.org/thread/ts203zssv1n9qth1wdlhk2bhos3vcq6t


### Credits
* Jonathan Leitschuh (finder)
