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

## Login check vulnerability by session Id ## { #CVE-2022-38369 }

CVE-2022-38369 [\[CVE json\]](./CVE-2022-38369.cve.json)

### Affected

* Apache IoTDB at 0.13.0


### Description

Apache IoTDB version 0.13.0 is vulnerable by session id attack. Users should upgrade to version 0.13.1 which addresses this issue.

### References
* https://lists.apache.org/thread/7nk03ywvx3t3yjbcxzt7zy4nyc89y9b0


## No authorization of DatabaseConnectController in grafana-connector.  ## { #CVE-2022-38370 }

CVE-2022-38370 [\[CVE json\]](./CVE-2022-38370.cve.json)

### Affected

* Apache IoTDB at 0.13.0


### Description

Apache IoTDB grafana-connector version 0.13.0 contains an interface without authorization, which may expose the internal structure of database. Users should upgrade to version 0.13.1 which addresses this issue.

### References
* https://lists.apache.org/thread/kcpqgstvgf8sxy9ktxm1836nlwc8xy3j


## Apache IoTDB prior to 0.13.3 allows DoS ## { #CVE-2022-43766 }

CVE-2022-43766 [\[CVE json\]](./CVE-2022-43766.cve.json)

### Affected

* Apache IoTDB from unspecified through 0.13.2


### Description

Apache IoTDB version 0.12.2 to 0.12.6, 0.13.0 to 0.13.2 are vulnerable to a Denial of Service attack when accepting untrusted patterns for REGEXP queries with Java 8. Users should upgrade to 0.13.3 which addresses this issue or use a later version of Java to avoid it.

### References
* https://lists.apache.org/thread/9pgpb82p5brooy41n8l5q0y9h33db2zn


### Credits
* This issue was discovered by 4ra1n of Chaitin Tech


## apache/iotdb-web-workbench: forge the JWTToken to access workbench ## { #CVE-2023-24829 }

CVE-2023-24829 [\[CVE json\]](./CVE-2023-24829.cve.json)

### Affected

* Apache IoTDB Workbench from 0.13.0 before 0.13.3


### Description

Incorrect Authorization vulnerability in Apache Software Foundation Apache IoTDB.<p>This issue affects the iotdb-web-workbench component from 0.13.0 before 0.13.3. iotdb-web-workbench is an optional component of IoTDB, providing a web console of the database.<br><br>This problem is fixed from version 0.13.3 of iotdb-web-workbench onwards.<br></p>

### References
* https://lists.apache.org/thread/l0b59hh046tyn4gqot0bdrpg8gxlksmo


## apache/iotdb-web-workbench: create a user without authorization ## { #CVE-2023-24830 }

CVE-2023-24830 [\[CVE json\]](./CVE-2023-24830.cve.json)

### Affected

* Apache IoTDB Workbench from 0.13.0 before 0.13.3


### Description

Improper Authentication vulnerability in Apache Software Foundation Apache IoTDB.<p>This issue affects iotdb-web-workbench component: from 0.13.0 before 0.13.3.</p>

### References
* https://lists.apache.org/thread/l4fon37687jz5ohgsnz2ko9fv400915t


## Apache IoTDB grafana-connector Login Bypass Vulnerability ## { #CVE-2023-24831 }

CVE-2023-24831 [\[CVE json\]](./CVE-2023-24831.cve.json)

### Affected

* Apache IoTDB from 0.13.0 through 0.13.3


### Description

Improper Authentication vulnerability in Apache Software Foundation Apache IoTDB.<p>This issue affects Apache IoTDB Grafana Connector: from 0.13.0 through 0.13.3.</p>Attackers could login without authorization. This is fixed in 0.13.4.

### References
* https://lists.apache.org/thread/3dgvzgstycf8b5hyf4z3n7cqdhcyln3l


## apache/iotdb-web-workbench: forge the JWTToken to access workbench ## { #CVE-2023-30771 }

CVE-2023-30771 [\[CVE json\]](./CVE-2023-30771.cve.json)

### Affected

* Apache IoTDB Workbench from 0.13.3 before 0.13.4


### Description

Incorrect Authorization vulnerability in Apache Software Foundation Apache IoTDB.<p>This issue affects the iotdb-web-workbench component on 0.13.3. iotdb-web-workbench is an optional component of IoTDB, providing a web console of the database.<br><br>This problem is fixed from version 0.13.4 of iotdb-web-workbench onwards.</p>

### References
* https://lists.apache.org/thread/08nc3dr6lshfppx0pzmz5vbggdnzpojb


## Remote Code Execution (RCE) risk via the UDF ## { #CVE-2023-46226 }

CVE-2023-46226 [\[CVE json\]](./CVE-2023-46226.cve.json)

### Affected

* Apache IoTDB from 1.0.0 through 1.2.2


### Description

Remote Code Execution vulnerability in Apache IoTDB.<p>This issue affects Apache IoTDB: from 1.0.0 through 1.2.2.</p><p>Users are recommended to upgrade to version 1.3.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/293b4ob65ftnfwyf62fb9zh8gwdy38hg


### Credits
* Glassy of EagleCloud (finder)


## Unsafe deserialize map in Sync Tool ## { #CVE-2023-51656 }

CVE-2023-51656 [\[CVE json\]](./CVE-2023-51656.cve.json)

### Affected

* Apache IoTDB from 0.13.0 through 0.13.4


### Description

Deserialization of Untrusted Data vulnerability in Apache IoTDB.<p>This issue affects Apache IoTDB: from 0.13.0 through 0.13.4.</p><p>Users are recommended to upgrade to version 1.2.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zy3klwpv11vl5n65josbfo2fyzxg3dxc
