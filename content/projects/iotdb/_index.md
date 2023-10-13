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
