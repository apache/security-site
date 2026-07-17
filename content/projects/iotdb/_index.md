---
title: Apache IoTDB security advisories
description: Security information for Apache IoTDB
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache IoTDB? You can read more about the projects' security policy on their [security page](https://github.com/apache/iotdb/blob/master/THREAT_MODEL.md), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://github.com/apache/iotdb/blob/master/THREAT_MODEL.md). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Out-of-bounds reads in C++ client TsBlock deserializer crash client process on malformed server data ## { #CVE-2026-40454 }

CVE-2026-40454 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40454) [\[CVE json\]](./CVE-2026-40454.cve.json) [\[OSV json\]](./CVE-2026-40454.osv.json)



_Last updated: 2026-07-10T07:18:58.462Z_

### Affected

* Apache IoTDB C++ client from 1.3.5 before 1.3.8
* Apache IoTDB C++ client from 2.0.5 before 2.0.10


### Description

<p>Out-of-bounds Read, Improper Input Validation vulnerability in Apache IoTDB C++ client.<br><span style="background-color: rgb(255, 255, 255);">Out-of-bounds reads in IoTDB C++ client TsBlock deserializer crash client
process on malformed server data.</span><br></p><p>This issue affects Apache IoTDB C++ client: from 1.3.5 before 1.3.8, from 2.0.5 before 2.0.10.</p><p>Users are recommended to upgrade to version 2.0.10, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/9wml325g6bpovw0jf5ymtc3xl7fwlkrn


### Credits
* bugbunny.ai (finder)


## Authorization bypass in /rest/v2/fastLastQuery exposes last-value data to unauthorized authenticated users ## { #CVE-2026-40452 }

CVE-2026-40452 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40452) [\[CVE json\]](./CVE-2026-40452.cve.json) [\[OSV json\]](./CVE-2026-40452.osv.json)



_Last updated: 2026-07-10T07:16:03.259Z_

### Affected

* Apache IoTDB from 1.3.5 before 1.3.8
* Apache IoTDB from 2.0.5 before 2.0.10


### Description

<p>Incorrect Authorization, Improper Access Control vulnerability in Apache IoTDB.<br>Authorization bypass in /rest/v2/fastLastQuery exposes last-value data to unauthorized authenticated users.<br></p><p>This issue affects Apache IoTDB: from 1.3.5 before 1.3.8, from 2.0.5 before 2.0.10.</p><p>Users are recommended to upgrade to version 2.0.10, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/04j2l6dosyboor4o2gvrzbrcrpllmh95


### Credits
* bugbunny.ai (finder)


## Authenticated users can escalate to full tree-path access by renaming themselves to __internal_auditor ## { #CVE-2026-40009 }

CVE-2026-40009 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40009) [\[CVE json\]](./CVE-2026-40009.cve.json) [\[OSV json\]](./CVE-2026-40009.osv.json)



_Last updated: 2026-07-10T07:15:02.989Z_

### Affected

* Apache IoTDB from 2.0.8 before 2.0.10


### Description

<p>Improper Privilege Management, Improper Access Control vulnerability in Apache IoTDB.<br><span style="background-color: rgb(255, 255, 255);">Authenticated users can escalate to full tree-path access by renaming
themselves to __internal_auditor.</span><br></p><p>This issue affects Apache IoTDB: from 2.0.8 before 2.0.10.</p><p>Users are recommended to upgrade to version 2.0.10, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/65hh7dh28rcxlzdzwdpt630321tr8b61


### Credits
* bugbunny.ai (finder)


## Arbitrary Class Instantiation via Pipe Transfer RPC ## { #CVE-2026-40008 }

CVE-2026-40008 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40008) [\[CVE json\]](./CVE-2026-40008.cve.json) [\[OSV json\]](./CVE-2026-40008.osv.json)



_Last updated: 2026-07-10T07:13:24.628Z_

### Affected

* Apache IoTDB from 1.0.0 before 2.0.10


### Description

<p>Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection') vulnerability in Apache IoTDB.<br><span style="background-color: rgb(255, 255, 255);">The pipe processor reads a fully
qualified Java class name and
instantiates it using Class.forName().newInstance() without any
validation or allowlisting.</span><br></p><p>This issue affects Apache IoTDB: from 1.0.0 before 2.0.10.</p><p>Users are recommended to upgrade to version 2.0.10, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/fm8cpvzbox2qqy99ztglm8wkk1nrg9ng


### Credits
* Andrea Cosentino (finder)


## Unauthenticated unbounded recursion in IoTDB AirGap receiver's E-language prefix parser causes per-connection StackOverflowError ## { #CVE-2026-40007 }

CVE-2026-40007 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40007) [\[CVE json\]](./CVE-2026-40007.cve.json) [\[OSV json\]](./CVE-2026-40007.osv.json)



_Last updated: 2026-07-10T07:12:27.092Z_

### Affected

* Apache IoTDB from 1.0.0 before 2.0.10


### Description

<p>Uncontrolled Recursion, Uncontrolled Resource Consumption vulnerability in Apache IoTDB.<br><span style="background-color: rgb(255, 255, 255);">When pipe_air_gap_receiver_enabled=true, the IoTDB AirGap receiver's
readLength method calls itself recursively each time it recognises the
E-language prefix in socket data, with no depth limit. An unauthenticated
attacker can send a stream of repeated E-language prefixes that drives the
recursion arbitrarily deep, exhausting the receiver thread's JVM stack and
raising StackOverflowError.</span><br></p><p>This issue affects Apache IoTDB: from 1.0.0 before 2.0.10.</p><p>Users are recommended to upgrade to version 2.0.10, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/tr23kh6kp8drrsv8ypv1mqm4v5kyy23m


### Credits
* bugbunny.ai (finder)


## Unauthenticated heap-exhaustion DoS via unbounded allocation in IoTDB AirGap pipe receiver ## { #CVE-2026-40006 }

CVE-2026-40006 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40006) [\[CVE json\]](./CVE-2026-40006.cve.json) [\[OSV json\]](./CVE-2026-40006.osv.json)



_Last updated: 2026-07-10T07:10:51.432Z_

### Affected

* Apache IoTDB from 1.0.0 before 2.0.10


### Description

<p>Memory Allocation with Excessive Size Value, Allocation of Resources Without Limits or Throttling, Missing Authentication for Critical Function vulnerability in Apache IoTDB.<br><span style="background-color: rgb(255, 255, 255);">When pipe_air_gap_receiver_enabled=true, the IoTDB AirGap pipe receiver
accepts raw TCP connections on port 9780 with no authentication. The
readLength method reads an attacker-controlled 32-bit integer from the
socket and readData passes it directly to new byte[length] with no
upper-bound check. An unauthenticated attacker can cause the JVM to attempt
an allocation of up to 2,147,483,647 bytes per connection, exhausting heap
memory and crashing or severely degrading the DataNode process.</span><br></p><p>This issue affects Apache IoTDB: from 1.0.0 before 2.0.10.</p><p>Users are recommended to upgrade to version 2.0.10, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/rfpt7m9fvdrw37r3ow5omp2n914z6zqk


### Credits
* bugbunny.ai (finder)


## Path Traversal in Pipe File Transfer Receiver ## { #CVE-2026-40005 }

CVE-2026-40005 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40005) [\[CVE json\]](./CVE-2026-40005.cve.json) [\[OSV json\]](./CVE-2026-40005.osv.json)



_Last updated: 2026-07-10T07:09:44.506Z_

### Affected

* Apache IoTDB from 1.0.0 before 2.0.10


### Description

<p>Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache IoTDB.<br><span style="background-color: rgb(255, 255, 255);">An attacker can write arbitrary files anywhere the IoTDB process has write permissions with unsafe API.</span><br></p><p>This issue affects Apache IoTDB: from 1.0.0 before 2.0.10.</p><p>Users are recommended to upgrade to version 2.0.10, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zw2vkbmy5xkf5y8g237v81hrs4c6b5lq


### Credits
* Andrea Cosentino (finder)


## REST Basic Authentication Accepts Stale Cached Credentials ## { #CVE-2026-28564 }

CVE-2026-28564 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-28564) [\[CVE json\]](./CVE-2026-28564.cve.json) [\[OSV json\]](./CVE-2026-28564.osv.json)



_Last updated: 2026-07-10T07:08:01.156Z_

### Affected

* Apache IoTDB from 1.0.0 before 2.0.10


### Description

<p>Insufficient Session Expiration, Authentication Bypass by Capture-replay vulnerability in Apache IoTDB.<br>REST Basic Authentication Accepts Stale Cached Credentials<br></p><p>This issue affects Apache IoTDB: from 1.0.0 before 2.0.10.</p><p>Users are recommended to upgrade to version 2.0.10, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/l38wpy7flvvfwv4rkps87l5z8gprnfy0


### Credits
* Aristore (https://github.com/aristorechina) (finder)


## JEXL Expression Injection Vulnerability ## { #CVE-2026-24713 }

CVE-2026-24713 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24713) [\[CVE json\]](./CVE-2026-24713.cve.json) [\[OSV json\]](./CVE-2026-24713.osv.json)



_Last updated: 2026-03-09T08:59:57.653Z_

### Affected

* Apache IoTDB from 1.0.0 before 1.3.7
* Apache IoTDB from 2.0.0 before 2.0.7


### Description

<p>Improper Input Validation vulnerability in Apache IoTDB.</p><p>This issue affects Apache IoTDB: from 1.0.0 before 1.3.7, from 2.0.0 before 2.0.7.</p><p>Users are recommended to upgrade to version 1.3.7 or 2.0.7, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/vopgv6y2ccw403b0zv7rvojjrh7x1j5p


### Credits
* Yongzhi Liu of Tencent YunDing Security Lab (finder)


## Insecure Default Configuration Vulnerability ## { #CVE-2026-24015 }

CVE-2026-24015 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24015) [\[CVE json\]](./CVE-2026-24015.cve.json) [\[OSV json\]](./CVE-2026-24015.osv.json)



_Last updated: 2026-03-09T08:57:43.961Z_

### Affected

* Apache IoTDB from 1.0.0 before 1.3.7
* Apache IoTDB from 2.0.0 before 2.0.7


### Description

<p>A vulnerability in Apache IoTDB.</p><p>This issue affects Apache IoTDB: from 1.0.0 before 1.3.7, from 2.0.0 before 2.0.7.</p><p>Users are recommended to upgrade to version 1.3.7 or 2.0.7, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/j769ywdqm46zl3oz5lbffsldklg0ow7p


### Credits
* Mapta / BugBunny_ai (finder)


## Path Traversal in DataNode Internal RPC Trigger JAR Upload Allows Arbitrary File Write ## { #CVE-2026-24014 }

CVE-2026-24014 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24014) [\[CVE json\]](./CVE-2026-24014.cve.json) [\[OSV json\]](./CVE-2026-24014.osv.json)



_Last updated: 2026-07-06T08:34:23.903Z_

### Affected

* Apache IoTDB from 1.3.3 before 2.0.8


### Description

<p>Apache IoTDB DataNode’s internal RPC interface for creating Trigger instances uses the uploaded Trigger JAR name to build a file path without sufficient validation. If the internal DataNode RPC port is exposed to an untrusted network, an attacker may use path traversal sequences in the JAR name to write files outside the intended Trigger installation directory. This could allow arbitrary file write with the permissions of the IoTDB process.</p><p>This issue affects Apache IoTDB: from 1.3.3 before 2.0.8.</p><p>Users are recommended to upgrade to version 2.0.8, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/38298f803gb5j9nlhf0l9zkf34o90h3m


### Credits
* Yan Nan (Detecon Security Lab). (finder)


## Authentication Bypass via Forged SessionID in Thrift RPC ## { #CVE-2026-24013 }

CVE-2026-24013 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24013) [\[CVE json\]](./CVE-2026-24013.cve.json) [\[OSV json\]](./CVE-2026-24013.osv.json)



_Last updated: 2026-07-06T07:17:46.194Z_

### Affected

* Apache IoTDB from 1.3.3 before 2.0.8


### Description

<p>Authentication Bypass by Spoofing vulnerability in Apache IoTDB.<br><span style="background-color: rgb(255, 255, 255);">Certain Thrift RPC query handlers lack strict validation of the sessionId
parameter. An attacker can construct requests with a forged sessionId and,
without performing openSession authentication, receive valid query results.
This allows authentication bypass and unauthorized reading of time-series
data.</span><br></p><p>This issue affects Apache IoTDB: from 1.3.3 before 2.0.8.</p><p>Users are recommended to upgrade to version 2.0.8, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/6pwkgnqhbm56mvn309f87snm84s0b75y


### Credits
* Yan Nan (Detecon Security Lab) (finder)


## Denial of Service via Resource Exhaustion in Aggregation Query ## { #CVE-2026-24012 }

CVE-2026-24012 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24012) [\[CVE json\]](./CVE-2026-24012.cve.json) [\[OSV json\]](./CVE-2026-24012.osv.json)



_Last updated: 2026-07-06T07:19:25.470Z_

### Affected

* Apache IoTDB from 1.3.3 before 2.0.8


### Description

<p>Uncontrolled Resource Consumption vulnerability in Apache IoTDB.&nbsp;</p><p>Some interface<span style="background-color: rgb(255, 255, 255);">&nbsp;fails to impose reasonable</span><span style="background-color: rgb(255, 255, 255);">
limits on the time span and aggregation interval of the query.&nbsp;</span><span style="background-color: rgb(255, 255, 255);">An attacker</span><span style="background-color: rgb(255, 255, 255);">
can construct a request with extreme parameters (e.g., a very large time</span><span style="background-color: rgb(255, 255, 255);">
range combined with a minimal interval).&nbsp;</span><span style="background-color: rgb(255, 255, 255);">This forces the DataNode to build</span><span style="background-color: rgb(255, 255, 255);">
an enormous result set in memory, which exhausts the Java heap and causes</span><span style="background-color: rgb(255, 255, 255);">
the DataNode process to crash.</span></p><p>This issue affects Apache IoTDB: from 1.3.3 before 2.0.8.</p><p>Users are recommended to upgrade to version 2.0.8, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/0g5th1t2vj6j8hm5t9w3xh9n6f6ht9z8


### Credits
* Yan Nan (Detecon Security Lab) (finder)


## Path Traversal Vulnerability ## { #CVE-2025-64152 }

CVE-2025-64152 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-64152) [\[CVE json\]](./CVE-2025-64152.cve.json) [\[OSV json\]](./CVE-2025-64152.osv.json)



_Last updated: 2026-06-26T12:16:26.834Z_

### Affected

* Apache IoTDB from 1.0.0 before 1.3.6
* Apache IoTDB from 2.0.0 before 2.0.7


### Description

<p>Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache IoTDB.</p><p>This issue affects Apache IoTDB: from 1.0.0 before 1.3.6, from 2.0.0 before 2.0.7.</p><p>Users are recommended to upgrade to version 1.3.6 and 2.0.7, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/sjms84rlt4g78fwmjcowxmtjp1q8b9q4


### Credits
* Yan Nan (Detecon Security Lab) (finder)


## Path Traversal Vulnerability ## { #CVE-2025-55017 }

CVE-2025-55017 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-55017) [\[CVE json\]](./CVE-2025-55017.cve.json) [\[OSV json\]](./CVE-2025-55017.osv.json)



_Last updated: 2026-06-26T12:15:51.835Z_

### Affected

* Apache IoTDB from 2.0.0 before 2.0.6
* Apache IoTDB from 1.0.0 before 1.3.6


### Description

<p>Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache IoTDB.</p><p>This issue affects Apache IoTDB: from 2.0.0 before 2.0.6, from 1.0.0 before 1.3.6.</p><p>Users are recommended to upgrade to version 1.3.6 and 2.0.6, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lk08wlxq9sp64mo8hw6wvjxd3bh3lpqg


### Credits
* qx (finder)


## Deserialization of untrusted Data ## { #CVE-2025-48459 }

CVE-2025-48459 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-48459) [\[CVE json\]](./CVE-2025-48459.cve.json) [\[OSV json\]](./CVE-2025-48459.osv.json)



_Last updated: 2025-09-24T07:57:20.978Z_

### Affected

* Apache IoTDB from 1.0.0 before 2.0.5


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache IoTDB.</p><p>This issue affects Apache IoTDB: from 1.0.0 before 2.0.5.</p><p>Users are recommended to upgrade to version 2.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/mr84n19nv8d0bmcrfsj3mm5ff5qn4q2f


### Credits
* Sanny (finder)
* 75Acol (finder)
* stan fang (finder)
* Wu Jiang (finder)


## DoS Vulnerability ## { #CVE-2025-48392 }

CVE-2025-48392 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-48392) [\[CVE json\]](./CVE-2025-48392.cve.json) [\[OSV json\]](./CVE-2025-48392.osv.json)



_Last updated: 2025-09-24T07:59:48.976Z_

### Affected

* Apache IoTDB from 1.3.3 through 1.3.4
* Apache IoTDB from 2.0.1-beta through 2.0.4


### Description

<p>A vulnerability in Apache IoTDB.</p><p>This issue affects Apache IoTDB: from 1.3.3 through 1.3.4, from 2.0.1-beta through 2.0.4.</p><p>Users are recommended to upgrade to version 2.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/1rn0637hptglmctf8cqd9425bj4q21td


### Credits
* yyjLF (finder)


## Exposure of Sensitive Information in IoTDB OpenID Authentication ## { #CVE-2025-26864 }

CVE-2025-26864 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-26864) [\[CVE json\]](./CVE-2025-26864.cve.json) [\[OSV json\]](./CVE-2025-26864.osv.json)



_Last updated: 2025-05-14T10:44:11.661Z_

### Affected

* Apache IoTDB from 0.10.0 through 1.3.3
* Apache IoTDB from 2.0.1-beta before 2.0.2


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor, Insertion of Sensitive Information into Log File vulnerability in the <span style="background-color: rgb(255, 255, 255);">OpenIdAuthorizer of</span> Apache IoTDB.</p><p>This issue affects Apache IoTDB: from 0.10.0 through 1.3.3, from 2.0.1-beta before 2.0.2.</p><p>Users are recommended to upgrade to version 1.3.4 and 2.0.2, which fix the issue.</p>

### References
* https://lists.apache.org/thread/2kcjnlypppk8qjh17dpz0jvkcpn6l162


### Credits
* Kyler Katz (finder)


## Exposure of Sensitive Information in IoTDB JDBC driver ## { #CVE-2025-26795 }

CVE-2025-26795 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-26795) [\[CVE json\]](./CVE-2025-26795.cve.json) [\[OSV json\]](./CVE-2025-26795.osv.json)



_Last updated: 2025-05-14T10:43:01.849Z_

### Affected

* Apache IoTDB JDBC driver from 0.10.0 through 1.3.3
* Apache IoTDB JDBC driver from 2.0.1-beta before 2.0.2


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor, Insertion of Sensitive Information into Log File vulnerability in Apache IoTDB JDBC driver.</p><p>This issue affects iotdb-jdbc: from 0.10.0 through 1.3.3, from 2.0.1-beta before 2.0.2.</p><p>Users are recommended to upgrade to version 2.0.2 and 1.3.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/bj0ytxr5wg0c4jw8xm7rhfd8ogho0r91


### Credits
* Kyler Katz (finder)


## SSRF Vulnerability (EOL) ## { #CVE-2024-36448 }

CVE-2024-36448 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-36448) [\[CVE json\]](./CVE-2024-36448.cve.json) [\[OSV json\]](./CVE-2024-36448.osv.json)



_Last updated: 2024-08-05T09:53:35.819Z_

### Affected

* Apache IoTDB Workbench from 0.13.0 through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Server-Side Request Forgery (SSRF) vulnerability in Apache IoTDB Workbench.</p><p>This issue affects Apache IoTDB Workbench: from 0.13.0.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/d19p0vsm7nogp43q9m3tzm5jl6mzjj1x


### Credits
* L0ne1y (finder)


## Remote Code Execution with untrusted URI of User-defined function ## { #CVE-2024-24780 }

CVE-2024-24780 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-24780) [\[CVE json\]](./CVE-2024-24780.cve.json) [\[OSV json\]](./CVE-2024-24780.osv.json)



_Last updated: 2025-05-14T10:42:18.799Z_

### Affected

* Apache IoTDB from 1.0.0 before 1.3.4


### Description

<p>Remote Code Execution with untrusted URI of UDF vulnerability in Apache IoTDB. The attacker who has&nbsp;privilege to create UDF can register malicious function from&nbsp;untrusted URI.</p><p>This issue affects Apache IoTDB: from 1.0.0 before 1.3.4.</p><p>Users are recommended to upgrade to version 1.3.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/xphtm98v3zsk9vlpfh481m1ry2ctxvmj


### Credits
* Y4 tacker (finder)
* Nbxiglk (finder)


## Unsafe deserialize map in Sync Tool ## { #CVE-2023-51656 }

CVE-2023-51656 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-51656) [\[CVE json\]](./CVE-2023-51656.cve.json) [\[OSV json\]](./CVE-2023-51656.osv.json)



_Last updated: 2023-12-21T11:47:55.799Z_

### Affected

* Apache IoTDB from 0.13.0 through 0.13.4


### Description

Deserialization of Untrusted Data vulnerability in Apache IoTDB.<p>This issue affects Apache IoTDB: from 0.13.0 through 0.13.4.</p><p>Users are recommended to upgrade to version 1.2.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zy3klwpv11vl5n65josbfo2fyzxg3dxc


## Remote Code Execution (RCE) risk via the UDF ## { #CVE-2023-46226 }

CVE-2023-46226 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-46226) [\[CVE json\]](./CVE-2023-46226.cve.json) [\[OSV json\]](./CVE-2023-46226.osv.json)



_Last updated: 2024-01-15T10:36:23.883Z_

### Affected

* Apache IoTDB from 1.0.0 through 1.2.2


### Description

Remote Code Execution vulnerability in Apache IoTDB.<p>This issue affects Apache IoTDB: from 1.0.0 through 1.2.2.</p><p>Users are recommended to upgrade to version 1.3.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/293b4ob65ftnfwyf62fb9zh8gwdy38hg


### Credits
* Glassy of EagleCloud (finder)


## apache/iotdb-web-workbench: forge the JWTToken to access workbench ## { #CVE-2023-30771 }

CVE-2023-30771 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-30771) [\[CVE json\]](./CVE-2023-30771.cve.json) [\[OSV json\]](./CVE-2023-30771.osv.json)



_Last updated: 2023-04-17T07:26:11.955Z_

### Affected

* Apache IoTDB Workbench from 0.13.3 before 0.13.4


### Description

Incorrect Authorization vulnerability in Apache Software Foundation Apache IoTDB.<p>This issue affects the iotdb-web-workbench component on 0.13.3. iotdb-web-workbench is an optional component of IoTDB, providing a web console of the database.<br><br>This problem is fixed from version 0.13.4 of iotdb-web-workbench onwards.</p>

### References
* https://lists.apache.org/thread/08nc3dr6lshfppx0pzmz5vbggdnzpojb


## Apache IoTDB grafana-connector Login Bypass Vulnerability ## { #CVE-2023-24831 }

CVE-2023-24831 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-24831) [\[CVE json\]](./CVE-2023-24831.cve.json) [\[OSV json\]](./CVE-2023-24831.osv.json)



_Last updated: 2023-04-18T01:31:44.944Z_

### Affected

* Apache IoTDB from 0.13.0 through 0.13.3


### Description

Improper Authentication vulnerability in Apache Software Foundation Apache IoTDB.<p>This issue affects Apache IoTDB Grafana Connector: from 0.13.0 through 0.13.3.</p>Attackers could login without authorization. This is fixed in 0.13.4.

### References
* https://lists.apache.org/thread/3dgvzgstycf8b5hyf4z3n7cqdhcyln3l


## apache/iotdb-web-workbench: create a user without authorization ## { #CVE-2023-24830 }

CVE-2023-24830 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-24830) [\[CVE json\]](./CVE-2023-24830.cve.json) [\[OSV json\]](./CVE-2023-24830.osv.json)



_Last updated: 2023-03-08T16:15:22.623Z_

### Affected

* Apache IoTDB Workbench from 0.13.0 before 0.13.3


### Description

Improper Authentication vulnerability in Apache Software Foundation Apache IoTDB.<p>This issue affects iotdb-web-workbench component: from 0.13.0 before 0.13.3.</p>

### References
* https://lists.apache.org/thread/l4fon37687jz5ohgsnz2ko9fv400915t


## apache/iotdb-web-workbench: forge the JWTToken to access workbench ## { #CVE-2023-24829 }

CVE-2023-24829 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-24829) [\[CVE json\]](./CVE-2023-24829.cve.json) [\[OSV json\]](./CVE-2023-24829.osv.json)



_Last updated: 2023-03-08T16:15:02.969Z_

### Affected

* Apache IoTDB Workbench from 0.13.0 before 0.13.3


### Description

Incorrect Authorization vulnerability in Apache Software Foundation Apache IoTDB.<p>This issue affects the iotdb-web-workbench component from 0.13.0 before 0.13.3. iotdb-web-workbench is an optional component of IoTDB, providing a web console of the database.<br><br>This problem is fixed from version 0.13.3 of iotdb-web-workbench onwards.<br></p>

### References
* https://lists.apache.org/thread/l0b59hh046tyn4gqot0bdrpg8gxlksmo


## Apache IoTDB prior to 0.13.3 allows DoS ## { #CVE-2022-43766 }

CVE-2022-43766 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-43766) [\[CVE json\]](./CVE-2022-43766.cve.json) [\[OSV json\]](./CVE-2022-43766.osv.json)



_Last updated: 2022-10-26T16:04:23.572Z_

### Affected

* Apache IoTDB from unspecified through 0.13.2


### Description

Apache IoTDB version 0.12.2 to 0.12.6, 0.13.0 to 0.13.2 are vulnerable to a Denial of Service attack when accepting untrusted patterns for REGEXP queries with Java 8. Users should upgrade to 0.13.3 which addresses this issue or use a later version of Java to avoid it.

### References
* https://lists.apache.org/thread/9pgpb82p5brooy41n8l5q0y9h33db2zn


### Credits
* This issue was discovered by 4ra1n of Chaitin Tech


## No authorization of DatabaseConnectController in grafana-connector.  ## { #CVE-2022-38370 }

CVE-2022-38370 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-38370) [\[CVE json\]](./CVE-2022-38370.cve.json) [\[OSV json\]](./CVE-2022-38370.osv.json)



_Last updated: 2022-09-05T09:43:12.381Z_

### Affected

* Apache IoTDB at 0.13.0


### Description

Apache IoTDB grafana-connector version 0.13.0 contains an interface without authorization, which may expose the internal structure of database. Users should upgrade to version 0.13.1 which addresses this issue.

### References
* https://lists.apache.org/thread/kcpqgstvgf8sxy9ktxm1836nlwc8xy3j


## Login check vulnerability by session Id ## { #CVE-2022-38369 }

CVE-2022-38369 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-38369) [\[CVE json\]](./CVE-2022-38369.cve.json) [\[OSV json\]](./CVE-2022-38369.osv.json)



_Last updated: 2022-09-05T09:42:50.630Z_

### Affected

* Apache IoTDB at 0.13.0


### Description

Apache IoTDB version 0.13.0 is vulnerable by session id attack. Users should upgrade to version 0.13.1 which addresses this issue.

### References
* https://lists.apache.org/thread/7nk03ywvx3t3yjbcxzt7zy4nyc89y9b0
