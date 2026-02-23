---
title: Apache IoTDB security advisories
description: Security information for Apache IoTDB
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache IoTDB? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

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
