---
title: Apache Cassandra security advisories
description: Security information for Apache Cassandra
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Cassandra? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Privilege escalation when enabling FQL/Audit logs ## { #CVE-2023-30601 }

CVE-2023-30601 [\[CVE json\]](./CVE-2023-30601.cve.json)

### Affected

* Apache Cassandra from 4.0.0 through 4.0.9
* Apache Cassandra from 4.1.0 through 4.1.1


### Description

Privilege escalation when enabling FQL/Audit logs allows user with JMX access to run arbitrary commands as the user running Apache Cassandra<br><p>This issue affects Apache Cassandra: from 4.0.0 through 4.0.9, from 4.1.0 through 4.1.1.</p>WORKAROUND<br>The vulnerability requires nodetool/JMX access to be exploitable, disable access for any non-trusted users.<br><br>MITIGATION<br>Upgrade to 4.0.10 or 4.1.2 and leave the new FQL/Auditlog configuration property&nbsp;allow_nodetool_archive_command as false.

### References
* https://lists.apache.org/thread/f74p9jdhmmp7vtrqd8lgm8bq3dhxl8vn


### Credits
* Gal Elbaz at Oligo (finder)
