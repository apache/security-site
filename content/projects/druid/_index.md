---
title: Apache Druid security advisories
description: Security information for Apache Druid
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Druid? You can read more about the projects' security policy on their [security page](https://druid.apache.org/docs/latest/operations/security-overview.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://druid.apache.org/docs/latest/operations/security-overview.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Authenticated users can override system configurations in their requests which allows them to execute arbitrary code. ## { #CVE-2021-25646 }

CVE-2021-25646 [\[CVE json\]](./CVE-2021-25646.cve.json)

_Last updated: 2021-01-29T19:09:31.597Z_

### Affected

* Apache Druid from 0.20.0 and earlier through 0.20.0


### Description

Apache Druid includes the ability to execute user-provided JavaScript code embedded in various types of requests. This functionality is intended for use in high-trust environments, and is disabled by default. However, in Druid 0.20.0 and earlier, it is possible for an authenticated user to send a specially-crafted request that forces Druid to run user-provided JavaScript code for that request, regardless of server configuration. This can be leveraged to execute code on the target machine with the privileges of the Druid server process.


### References
* https://lists.apache.org/thread.html/rfda8a3aa6ac06a80c5cbfdeae0fc85f88a5984e32ea05e6dda46f866%40%3Cdev.druid.apache.org%3E


### Credits
* This issue was discovered by Litch1 from the Security Team of Alibaba Cloud.


## Apache Druid Authenticated users can execute arbitrary code from malicious MySQL database systems. ## { #CVE-2021-26919 }

CVE-2021-26919 [\[CVE json\]](./CVE-2021-26919.cve.json)

_Last updated: 2021-03-30T07:47:52.941Z_

### Affected

* Apache Druid from Apache Druid through 0.20.1


### Description

Apache Druid allows users to read data from other database systems using JDBC. This functionality is to allow trusted users with the proper permissions to set up lookups or submit ingestion tasks. The MySQL JDBC driver supports certain properties, which, if left unmitigated, can allow an attacker to execute arbitrary code from a hacker-controlled malicious MySQL server within Druid server processes.  This issue was addressed in Apache Druid 0.20.2

### References
* https://lists.apache.org/thread.html/rd87451fce34df54796e66321c40d743a68fb4553d72e7f6f0bc62ebd%40%3Cdev.druid.apache.org%3E


### Credits
* This issue was discovered by fantasyC4t from the Ant FG Security Lab.


## Apache Druid: The HTTP inputSource allows authenticated users to read data from other sources than intended ## { #CVE-2021-26920 }

CVE-2021-26920 [\[CVE json\]](./CVE-2021-26920.cve.json)

_Last updated: 2021-07-02T07:14:27.176Z_

### Affected

* Apache Druid from Apache Druid through 0.20.2


### Description

In the Druid ingestion system, the InputSource is used for reading data from a certain data source. However, the HTTP InputSource allows authenticated users to read data from other sources than intended, such as the local file system, with the privileges of the Druid server process. This is not an elevation of privilege when users access Druid directly, since Druid also provides the Local InputSource, which allows the same level of access. But it is problematic when users interact with Druid indirectly through an application that allows users to specify the HTTP InputSource, but not the Local InputSource. In this case, users could bypass the application-level restriction by passing a file URL to the HTTP InputSource.

### References
* https://lists.apache.org/thread.html/r29e45561343cc5cf7d3290ee0b0e94e565faab19c20d022df9b5e29c%40%3Cdev.druid.apache.org%3E


### Credits
* This issue was discovered by chybeta from the Security Team of Alibaba Cloud.


## Apache Druid: The HTTP inputSource allows authenticated users to read data from other sources than intended (incomplete fix of CVE-2021-26920) ## { #CVE-2021-36749 }

CVE-2021-36749 [\[CVE json\]](./CVE-2021-36749.cve.json)

_Last updated: 2021-09-23T23:08:21.915Z_

### Affected

* Apache Druid from 0.21.1 and earlier through 0.21.1


### Description

In the Druid ingestion system, the InputSource is used for reading data from a certain data source. However, the HTTP InputSource allows authenticated users to read data from other sources than intended, such as the local file system, with the privileges of the Druid server process. This is not an elevation of privilege when users access Druid directly, since Druid also provides the Local InputSource, which allows the same level of access. But it is problematic when users interact with Druid indirectly through an application that allows users to specify the HTTP InputSource, but not the Local InputSource. In this case, users could bypass the application-level restriction by passing a file URL to the HTTP InputSource.

This issue was previously mentioned as being fixed in 0.21.0 as per CVE-2021-26920 but was not fixed in 0.21.0 or 0.21.1.

### References
* https://lists.apache.org/thread.html/rc9400a70d0ec5cdb8a3486fc5ddb0b5282961c0b63e764abfbcb9f5d%40%3Cdev.druid.apache.org%3E


### Credits
* This issue was originally discovered by chybeta from the Security Team of Alibaba Cloud.
* ABKing and g0udan from the Security Team of Xiaomi discovered that it was still an issue after CVE-2021-26920.


## Reflected XSS on certain HTTP endpoints ## { #CVE-2021-44791 }

CVE-2021-44791 [\[CVE json\]](./CVE-2021-44791.cve.json)

_Last updated: 2022-07-07T18:29:34.319Z_

### Affected

* Apache Druid from Apache Druid through 0.22.1


### Description

In Apache Druid 0.22.1 and earlier, certain specially-crafted links result in unescaped URL parameters being sent back in HTML responses. This makes it possible to execute reflected XSS attacks.

### References
* https://lists.apache.org/thread/lh2kcl4j45q7xj4w6rqf6kwf0mvyp2o6


### Credits
* This issue was discovered by DangKhai from Viettel Cyber Security


## Clickjacking in the web console ## { #CVE-2022-28889 }

CVE-2022-28889 [\[CVE json\]](./CVE-2022-28889.cve.json)

_Last updated: 2022-07-07T18:30:27.570Z_

### Affected

* Apache Druid from unspecified through 0.22.1


### Description

In Apache Druid 0.22.1 and earlier, the server did not set appropriate headers to prevent clickjacking. Druid 0.23.0 and later prevent clickjacking using the Content-Security-Policy header.

### References
* https://lists.apache.org/thread/t3nsq4crdr8wqgmj721d2wg6pf26s5cw
