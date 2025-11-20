---
title: Apache Flink security advisories
description: Security information for Apache Flink
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Flink? You can read more about the projects' security policy on their [security page](https://flink.apache.org/what-is-flink/security/), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://flink.apache.org/what-is-flink/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Flink directory traversal attack: remote file writing through the REST API ## { #CVE-2020-17518 }

CVE-2020-17518 [\[CVE json\]](./CVE-2020-17518.cve.json) [\[OSV json\]](./CVE-2020-17518.osv.json)



_Last updated: 2021-01-05T11:32:09.849Z_

### Affected

* Apache Flink at 1.5.1 to 1.11.2


### Description

Apache Flink 1.5.1 introduced a REST handler that allows you to write an uploaded file to an arbitrary location on the local file system, through a maliciously modified HTTP HEADER. The files can be written to any location accessible by Flink 1.5.1.  All users should upgrade to Flink 1.11.3 or 1.12.0 if their Flink instance(s) are exposed.  The issue was fixed in commit a5264a6f41524afe8ceadf1d8ddc8c80f323ebc4 from apache/flink:master.

### References
* https://lists.apache.org/thread.html/rb43cd476419a48be89c1339b527a18116f23eec5b6df2b2acbfef261%40%3Cdev.flink.apache.org%3E


### Credits
* 0rich1 of Ant Security FG Lab


## Apache Flink directory traversal attack: reading remote files through the REST API ## { #CVE-2020-17519 }

CVE-2020-17519 [\[CVE json\]](./CVE-2020-17519.cve.json) [\[OSV json\]](./CVE-2020-17519.osv.json)



_Last updated: 2021-01-05T11:32:48.294Z_

### Affected

* Apache Flink at 1.11.0 to 1.11.2


### Description

A change introduced in Apache Flink 1.11.0 (and released in 1.11.1 and 1.11.2 as well) allows attackers to read any file on the local filesystem of the JobManager through the REST interface of the JobManager process. Access is restricted to files accessible by the JobManager process.
All users should upgrade to Flink 1.11.3 or 1.12.0 if their Flink instance(s) are exposed. The issue was fixed in commit b561010b0ee741543c3953306037f00d7a9f0801 from apache/flink:master.

### References
* https://lists.apache.org/thread.html/r6843202556a6d0bce9607ebc02e303f68fc88e9038235598bde3b50d%40%3Cdev.flink.apache.org%3E


### Credits
* 0rich1 of Ant Security FG Lab


## Apache Flink Stateful Functions allowed HTTP header injection due to Improper Neutralization of CRLF Sequences ## { #CVE-2023-41834 }

CVE-2023-41834 [\[CVE json\]](./CVE-2023-41834.cve.json) [\[OSV json\]](./CVE-2023-41834.osv.json)



_Last updated: 2023-09-19T12:34:13.497Z_

### Affected

* Apache Flink Stateful Functions from 3.1.0 through 3.2.0


### Description

Improper Neutralization of CRLF Sequences in HTTP Headers in Apache Flink Stateful Functions 3.1.0, 3.1.1 and 3.2.0 allows remote attackers to inject arbitrary HTTP headers and conduct HTTP response splitting attacks via crafted HTTP requests.&nbsp;Attackers could potentially inject malicious content into the HTTP response that is sent to the user's browser. <br><br>Users should upgrade to Apache Flink Stateful Functions version 3.3.0.

### References
* https://lists.apache.org/thread/cvxcsdyjqc3lysj1tz7s06zwm36zvwrm


### Credits
* Andrea Cosentino (finder)


## SQL injection via maliciously crafted identifiers ## { #CVE-2025-62228 }

CVE-2025-62228 [\[CVE json\]](./CVE-2025-62228.cve.json) [\[OSV json\]](./CVE-2025-62228.osv.json)



_Last updated: 2025-10-09T13:15:41.457Z_

### Affected

* Apache Flink CDC from 3.0.0 through 3.4.0
* Apache Flink CDC from 3.0.0 through 3.4.0
* Apache Flink CDC from 3.0.0 through 3.4.0
* Apache Flink CDC from 3.0.0 through 3.4.0
* Apache Flink CDC from 3.3.0 through 3.4.0


### Description

<div><div>Apache Flink CDC version 3.4.0 was vulnerable to a SQL injection via maliciously crafted identifiers eg. crafted database name or crafted table name. Even through only the logged-in database user can trigger the attack, we recommend users update Flink CDC version to 3.5.0 which address this issue.   </div></div><br>

### References
* https://lists.apache.org/thread/3dn0hc1wbc5sj0jbgdg33gtnwlw7qrl3


### Credits
* intSheep (reporter)
* Mapta/BugBunny_ai (reporter)
