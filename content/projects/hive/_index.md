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

## SQL injection vulnerability when processing delete column statistics requests via the HMS Thrift APIs ## { #CVE-2025-62728 }

CVE-2025-62728 [\[CVE json\]](./CVE-2025-62728.cve.json) [\[OSV json\]](./CVE-2025-62728.osv.json)



_Last updated: 2025-11-26T10:29:43.944Z_

### Affected

* Apache Hive from 4.1.0 before 4.2.0


### Description

<p>SQL injection vulnerability in Hive Metastore Server (HMS) when processing delete column statistics requests via the Thrift APIs. The vulnerability is only exploitable by trusted/authorized users/applications that are allowed to call directly the Thrift APIs. In most real-world deployments, HMS is accessible to only a handful of applications (e.g., Hiveserver2) thus the vulnerability is not exploitable. Moreover, the vulnerable code cannot be reached when metastore.try.direct.sql property is set to false.</p><p>This issue affects Apache Hive: from 4.1.0 before 4.2.0.</p><p>Users are recommended to upgrade to version 4.2.0, which fixes the issue. Users who cannot upgrade directly are encouraged to set&nbsp;metastore.try.direct.sql property to false if the HMS Thrift APIs are exposed to general public.</p>

### References
* https://lists.apache.org/thread/yj65dd8dmzgy8p3nv8zy33v8knzg9o7g


### Credits
* WuKong (Tencent) (finder)


## Credentials file created with non restrictive permissions ## { #CVE-2024-29869 }

CVE-2024-29869 [\[CVE json\]](./CVE-2024-29869.cve.json) [\[OSV json\]](./CVE-2024-29869.osv.json)



_Last updated: 2025-01-28T19:57:18.085Z_

### Affected

* Apache Hive from 1.1.0 before 4.0.1


### Description

Hive creates a credentials file to a temporary directory in the file system with permissions 644 by default when the file permissions are not set explicitly. Any unauthorized user having access to the directory can read the sensitive information written into this file.&nbsp;Users are recommended to upgrade to version 4.0.1, which fixes this issue.<br>

### References
* https://github.com/apache/hive
* https://github.com/apache/hive/commit/20106e254527f7d71b2e34455c4322e14950c620
* https://issues.apache.org/jira/browse/HIVE-28134
* https://lists.apache.org/thread/h27ohpyrqf9w1m3c0tqr7x8jg59rcrv6


### Credits
* Andrea Cosentino (reporter)


## Timing Attack Against Signature in LLAP util ## { #CVE-2024-23953 }

CVE-2024-23953 [\[CVE json\]](./CVE-2024-23953.cve.json) [\[OSV json\]](./CVE-2024-23953.osv.json)



_Last updated: 2025-01-28T06:25:01.840Z_

### Affected

* Apache Hive from 2.2.0 before 4.0.0


### Description

Use of Arrays.equals() in <span style="background-color: rgb(255, 255, 255);">LlapSignerImpl in&nbsp;</span>Apache Hive to compare message signatures&nbsp;<span style="background-color: var(--wht);">allows attacker to forge a valid signature for an arbitrary message byte by byte. The attacker should be an authorized user of the product to perform this attack.&nbsp;</span>Users are recommended to upgrade to version 4.0.0, which fixes this issue.<br><br><span style="background-color: rgb(253, 253, 253);">The problem occurs when an application doesn’t use a constant-time algorithm for validating a signature.&nbsp;<span style="background-color: rgb(253, 253, 253);">The method </span><code>Arrays.equals()</code><span style="background-color: rgb(253, 253, 253);">&nbsp;returns </span><code>false</code><span style="background-color: rgb(253, 253, 253);">&nbsp;right away when it sees that one of the input’s bytes are different. It means that the comparison time depends on the contents of the arrays. This little thing may allow an attacker to forge a valid signature for an arbitrary message byte by byte.&nbsp;So it might allow malicious users to submit splits/work with selected signatures to LLAP without running as a privileged user, potentially leading to DDoS attack.</span><br><br></span>More details in the reference section.<br>

### References
* https://github.com/apache/hive
* https://github.com/apache/hive/commit/b418e3c9f479ba8e7d31e6470306111002ffa809
* https://issues.apache.org/jira/browse/HIVE-28030
* https://blog.gypsyengineer.com/en/security/preventing-timing-attacks-with-codeql.html
* https://cqr.company/web-vulnerabilities/timing-attacks/
* https://lists.apache.org/thread/0nloywj49nbtlc6l3c6363qvq7o1ztb7


### Credits
* Andrea Cosentino (reporter)


## CookieSigner exposes the correct signature when message verification fails ## { #CVE-2024-23945 }

CVE-2024-23945 [\[CVE json\]](./CVE-2024-23945.cve.json) [\[OSV json\]](./CVE-2024-23945.osv.json)



_Last updated: 2024-12-23T15:26:52.096Z_

### Affected

* Apache Hive from 1.2.0 before 4.0.0
* Apache Spark from 2.0.0 before 3.0.0
* Apache Spark from 3.0.0 before 3.3.4
* Apache Spark from 3.4.0 before 3.4.2
* Apache Spark at 3.5.0


### Description

Signing cookies is an application security feature that adds a digital signature to cookie data to verify its authenticity and integrity. The signature helps prevent malicious actors from modifying the cookie value, which can lead to security vulnerabilities and exploitation. Apache Hive’s service component accidentally exposes the signed cookie to the end user when there is a mismatch in signature between the current and expected cookie. Exposing the correct cookie signature can lead to further exploitation.<br><br>The vulnerable CookieSigner logic was introduced in Apache Hive by&nbsp;HIVE-9710 (1.2.0) and in Apache Spark by SPARK-14987 (2.0.0). The affected components are the following:<br>* org.apache.hive:hive-service<br>* org.apache.spark:spark-hive-thriftserver_2.11<br>* org.apache.spark:spark-hive-thriftserver_2.12<br><br>

### References
* https://github.com/apache/hive
* https://github.com/apache/spark
* https://github.com/apache/spark/commit/cf59b1f51c16301f689b4e0f17ba4dbd140e1b19
* https://github.com/apache/hive/commit/7638cb1a3b07713cc490aa2909a37037f89e08b4
* https://issues.apache.org/jira/browse/HIVE-9710
* https://issues.apache.org/jira/browse/SPARK-14987
* https://lists.apache.org/thread/59r4mv7glrxpwkkdjvjbdljfpx3f5zzc
* https://lists.apache.org/thread/5o2ljnzrv8zvhjw9vy7b4rwjpc32hgfc


### Credits
* Kostya Kortchinsky (reporter)
* Hamza Tahmi (reporter)


## Arbitrary command execution via JDBC driver ## { #CVE-2023-35701 }

CVE-2023-35701 [\[CVE json\]](./CVE-2023-35701.cve.json) [\[OSV json\]](./CVE-2023-35701.osv.json)



_Last updated: 2024-05-03T08:11:05.595Z_

### Affected

* Apache Hive from 4.0.0-alpha-1 before 4.0.0


### Description

Improper Control of Generation of Code ('Code Injection') vulnerability in Apache Hive.<br><br>The vulnerability affects the Hive JDBC driver component and it can potentially lead to arbitrary code execution on the machine/endpoint that the JDBC driver (client) is running. The malicious user must have sufficient permissions to specify/edit JDBC URL(s) in an endpoint relying on the Hive JDBC driver and the JDBC client process must run under a privileged user to fully exploit the vulnerability.&nbsp;<br><br>The attacker can setup a malicious HTTP server and specify a JDBC URL pointing towards this server. When a JDBC connection is attempted, the malicious HTTP server can provide a special response with customized payload that can trigger the execution of certain commands in the JDBC client.<p>This issue affects Apache Hive: from 4.0.0-alpha-1 before 4.0.0.</p><p>Users are recommended to upgrade to version 4.0.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7zcv6l63spl4r66xwz5jv9rtrg2opx81


### Credits
* Kostya Kortchinsky (reporter)


## Deserialization of untrusted data when fetching partitions from the Metastore ## { #CVE-2022-41137 }

CVE-2022-41137 [\[CVE json\]](./CVE-2022-41137.cve.json) [\[OSV json\]](./CVE-2022-41137.osv.json)



_Last updated: 2024-12-05T10:01:39.567Z_

### Affected

* Apache Hive from 4.0.0-alpha-1 before 4.0.0


### Description

Apache Hive&nbsp;Metastore (HMS) uses&nbsp;<span style="background-color: rgb(255, 255, 255);">SerializationUtilities#deserializeObjectWithTypeInformation</span><span style="background-color: rgb(255, 255, 255);">&nbsp;method when filtering and fetching partitions that is unsafe and</span>&nbsp;can lead&nbsp;to Remote Code Execution (RCE) since it allows the deserialization of arbitrary data.<br><br>In real deployments, the vulnerability can be exploited only by authenticated users/clients that were able to successfully establish&nbsp;a connection to the Metastore. From an API perspective any code that calls the unsafe method may be vulnerable unless it performs additional prerechecks on the input arguments.

### References
* https://github.com/apache/hive
* https://issues.apache.org/jira/browse/HIVE-26539
* https://github.com/apache/hive/commit/60027bb9c91a93affcfebd9068f064bc1f2a74c9
* https://lists.apache.org/thread/jwtr3d9yovf2wo0qlxvkhoxnwxxyzgts


### Credits
* Junjie Liao (reporter)


## Apache Hive Security vulnerability in Hive with UDFs ## { #CVE-2021-34538 }

CVE-2021-34538 [\[CVE json\]](./CVE-2021-34538.cve.json) [\[OSV json\]](./CVE-2021-34538.osv.json)



_Last updated: 2022-07-16T07:05:22.225Z_

### Affected

* Apache Hive from Apache Hive before 3.1.3


### Description

Apache Hive before 3.1.3 "CREATE" and "DROP" function operations does not check for necessary authorization of involved entities in the query. It was found that an unauthorized user can manipulate an existing UDF without having the privileges to do so. This allowed unauthorized or underprivileged users to drop and recreate UDFs pointing them to new jars that could be potentially malicious.

### References
* https://lists.apache.org/thread/oqqgnhz4c6nxsfd0xstosnk0g15f7354


### Credits
* This vulnerability was discovered and reported by Hideyuki Furue.


## Timing attack in Cookie signature verification ## { #CVE-2020-1926 }

CVE-2020-1926 [\[CVE json\]](./CVE-2020-1926.cve.json) [\[OSV json\]](./CVE-2020-1926.osv.json)



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
