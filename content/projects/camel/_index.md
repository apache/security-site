---
title: Apache Camel security advisories
description: Security information for Apache Camel
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Camel? You can read more about the projects' security policy on their [security page](https://camel.apache.org/security/), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://camel.apache.org/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Temporary file information disclosure in Camel-Jira ## { #CVE-2023-34442 }

CVE-2023-34442 [\[CVE json\]](./CVE-2023-34442.cve.json) [\[OSV json\]](./CVE-2023-34442.osv.json)



_Last updated: 2023-07-10T09:31:01.757Z_

### Affected

* Apache Camel JIRA from 3.x through <=3.14.8
* Apache Camel JIRA from 3.18.x through <=3.18.7
* Apache Camel JIRA from 3.20.x through <= 3.20.5
* Apache Camel JIRA from 4.x through <= 4.0.0-M3


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Camel.<p>This issue affects Apache Camel: from 3.X through &lt;=3.14.8, from 3.18.X through &lt;=3.18.7, from 3.20.X through &lt;= 3.20.5, from 4.X through &lt;= 4.0.0-M3.</p><span style="background-color: rgb(255, 255, 255);">Users should upgrade to 3.14.9, 3.18.8, 3.20.6 or 3.21.0 and for users on Camel 4.x update to 4.0.0-M1</span><br>

### References
* https://lists.apache.org/thread/x4vy2hhbltb1xrvy1g6m8hpjgj2k7wgh


### Credits
* Jonathan Leitschuh of the Open Source Security Foundation: Project Alpha-Omega (reporter)


## Camel-SQL: Unsafe Deserialization from JDBCAggregationRepository ## { #CVE-2024-22369 }

CVE-2024-22369 [\[CVE json\]](./CVE-2024-22369.cve.json) [\[OSV json\]](./CVE-2024-22369.osv.json)



_Last updated: 2024-02-20T15:01:05.582Z_

### Affected

* Apache Camel from 3.0.0 before 3.21.4
* Apache Camel from 3.22.0 before 3.22.1
* Apache Camel from 4.0.0 before 4.0.4
* Apache Camel from 4.1.0 before 4.4.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Camel SQL Component<p>This issue affects Apache Camel: from 3.0.0 before 3.21.4, from 3.22.0 before 3.22.1, from 4.0.0 before 4.0.4, from 4.1.0 before 4.4.0.</p><p>Users are recommended to upgrade to version 4.4.0, which fixes the issue. If users are on the 4.0.x LTS releases stream, then they are suggested to upgrade to 4.0.4. If users are on 3.x, they are suggested to move to 3.21.4 or 3.22.1</p>

### References
* https://lists.apache.org/thread/3dko781dy2gy5l3fs48p56fgp429yb0f
* https://camel.apache.org/security/CVE-2024-22369.html


### Credits
* Ziyang Chen from HuaWei Open Source Management Center (finder)
* Pingtao Wei from HuaWei Open Source Management Center (finder)
* Haoran Zhi from HuaWei Open Source Management Center (finder)


## Apache Camel issue on ExchangeCreatedEvent ## { #CVE-2024-22371 }

CVE-2024-22371 [\[CVE json\]](./CVE-2024-22371.cve.json)

_Last updated: 2024-02-26T09:22:36.071Z_

### Affected

* Apache Camel from 1.x through 1.6.0
* Apache Camel from 3.21.x through 3.21.3
* Apache Camel from 3.22.x through 3.22.0
* Apache Camel from 4.0.x through 4.0.3
* Apache Camel from 4.x through 4.3.0


### Description

Exposure of sensitive data by by crafting a malicious EventFactory and providing a custom ExchangeCreatedEvent that exposes sensitive data. Vulnerability in Apache Camel.<p>This issue affects Apache Camel: from 3.21.X through 3.21.3, from 3.22.X through 3.22.0, from 4.0.X through 4.0.3, from 4.X through 4.3.0.</p><p>Users are recommended to upgrade to version 3.21.4, 3.22.1, 4.0.4 or 4.4.0, which fixes the issue.</p>

### References
* https://camel.apache.org/security/CVE-2024-22371.html


### Credits
* Otavio Rodolfo Piske from the Apache Software Foundation (finder)


## Camel-CassandraQL: Unsafe Deserialization from CassandraAggregationRepository ## { #CVE-2024-23114 }

CVE-2024-23114 [\[CVE json\]](./CVE-2024-23114.cve.json) [\[OSV json\]](./CVE-2024-23114.osv.json)



_Last updated: 2024-02-20T14:59:36.356Z_

### Affected

* Apache Camel from 3.0.0 before 3.21.4
* Apache Camel from 3.22.0 before 3.22.1
* Apache Camel from 4.0.0 before 4.0.4
* Apache Camel from 4.1.0 before 4.4.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Camel CassandraQL Component AggregationRepository which is vulnerable to unsafe deserialization. Under specific conditions it is possible to deserialize malicious payload.<p>This issue affects Apache Camel: from 3.0.0 before 3.21.4, from 3.22.0 before 3.22.1, from 4.0.0 before 4.0.4, from 4.1.0 before 4.4.0.</p><p>Users are recommended to upgrade to version 4.4.0, which fixes the issue.&nbsp;If users are on the 4.0.x LTS releases stream, then they are suggested to upgrade to 4.0.4. If users are on 3.x, they are suggested to move to 3.21.4 or 3.22.1</p>

### References
* https://camel.apache.org/security/CVE-2024-23114.html


### Credits
* Federico Mariani From Apache Software Foundation (finder)
* Andrea Cosentino from Apache Software Foundation (finder)
