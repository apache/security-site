---
title: Apache Causeway security advisories
description: Security information for Apache Causeway
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Causeway? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Java deserialization vulnerability to authenticated attackers ## { #CVE-2025-64408 }

CVE-2025-64408 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-64408) [\[CVE json\]](./CVE-2025-64408.cve.json) [\[OSV json\]](./CVE-2025-64408.osv.json)



_Last updated: 2025-11-19T10:32:04.142Z_

### Affected

* Apache Causeway from 2.0.0 through 3.4.0
* Apache Causeway at 4.0.0-M1


### Description

<p>
Apache Causeway faces Java deserialization vulnerabilities that allow remote code execution (RCE) through&nbsp;user-controllable URL parameters. These vulnerabilities affect all&nbsp;applications using Causeway's ViewModel functionality and can be exploited&nbsp;by authenticated attackers to execute arbitrary code with application&nbsp;privileges.&nbsp;</p><p>This issue affects all current versions.</p><p>Users are recommended to upgrade to version 3.5.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/rjlg4spqhmgy1xgq9wq5h2tfnq4pm70b


### Credits
* Slain Nico (reporter)
