---
title: Apache Hive security advisories
description: Security information for Apache Hive
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Hive? You can read more about the projects' security policy on their [security page](https://hive.apache.org/mailing_lists.html), and email your report to the [Apache Hive Security Team](mailto:security@hive.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://hive.apache.org/mailing_lists.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Timing attack in Cookie signature verification ## { #CVE-2020-1926 }

CVE-2020-1926 [\[CVE json\]](./CVE-2020-1926.cve.json)

_Last updated: 2021-03-16T12:44:51.635Z_

### Affected

* Apache Hive from Apache Hive before 2.3.8


### Description

Apache Hive cookie signature verification used a non constant time comparison which is known to be vulnerable to timing attacks. This could allow recovery of another users cookie signature. The issue was addressed in Apache Hive 2.3.8

### References
* https://issues.apache.org/jira/browse/HIVE-22708
* https://lists.apache.org/thread.html/rd186eedff68102ba1e68059a808101c5aa587e11542c7dcd26e7b9d7%40%3Cuser.hive.apache.org%3E


### Credits
* Apache Hive would like to thank S. Wasin for reporting this issue.


## Apache Hive Security vulnerability in Hive with UDFs ## { #CVE-2021-34538 }

CVE-2021-34538 [\[CVE json\]](./CVE-2021-34538.cve.json)

_Last updated: 2022-07-16T07:05:22.225Z_

### Affected

* Apache Hive from Apache Hive before 3.1.3


### Description

Apache Hive before 3.1.3 "CREATE" and "DROP" function operations does not check for necessary authorization of involved entities in the query. It was found that an unauthorized user can manipulate an existing UDF without having the privileges to do so. This allowed unauthorized or underprivileged users to drop and recreate UDFs pointing them to new jars that could be potentially malicious.

### References
* https://lists.apache.org/thread/oqqgnhz4c6nxsfd0xstosnk0g15f7354


### Credits
* This vulnerability was discovered and reported by Hideyuki Furue.
