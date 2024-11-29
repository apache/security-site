---
title: Apache Mynewt security advisories
description: Security information for Apache Mynewt
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Mynewt? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Denial of service in NimBLE Bluetooth stack ## { #CVE-2024-24746 }

CVE-2024-24746 [\[CVE json\]](./CVE-2024-24746.cve.json) [\[OSV json\]](./CVE-2024-24746.osv.json)



_Last updated: 2024-04-10T07:39:33.115Z_

### Affected

* Apache NimBLE through 1.6.0


### Description

Loop with Unreachable Exit Condition ('Infinite Loop') vulnerability in Apache NimBLE.&nbsp;<br><br>Specially crafted GATT operation can cause infinite loop in GATT server leading to denial of service in Bluetooth stack or device.<br><br><span style="background-color: var(--wht);">This issue affects Apache NimBLE: through 1.6.0.<br></span><span style="background-color: var(--wht);">Users are recommended to upgrade to version 1.7.0, which fixes the issue.</span>

### References
* https://lists.apache.org/thread/bptkzc0o2ymjk8qqzqdmy39kcmh27078
* https://github.com/apache/mynewt-nimble/commit/d42a0ebe6632bd0c318560e4293a522634f60594


### Credits
* Iván Arce from Quarkslab Vulnerability Reports team (reporter)


## Buffer overflow in NimBLE MESH Bluetooth stack ## { #CVE-2024-47248 }

CVE-2024-47248 [\[CVE json\]](./CVE-2024-47248.cve.json) [\[OSV json\]](./CVE-2024-47248.osv.json)



_Last updated: 2024-11-26T11:15:41.242Z_

### Affected

* Apache NimBLE through 1.7.0


### Description

<p>Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') vulnerability in Apache NimBLE.</p>Specially crafted MESH message could result in memory corruption when non-default build configuration is used.<br><p>This issue affects Apache NimBLE: through 1.7.0.</p><p>Users are recommended to upgrade to version 1.8.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/z8m7jqh54xybf9kz8q2l3tz92zsj7tmz


### Credits
* Wei Che Kao (Xiaobye), graduate student from National Yang Ming Chiao Tung University, Dept. of CS, Security and Systems Lab. (reporter)


## Lack of input sanitization leading to out-of-bound reads in multiple advertisement handler ## { #CVE-2024-47249 }

CVE-2024-47249 [\[CVE json\]](./CVE-2024-47249.cve.json) [\[OSV json\]](./CVE-2024-47249.osv.json)



_Last updated: 2024-11-26T11:16:32.616Z_

### Affected

* Apache NimBLE through 1.7.0


### Description

<p>Improper Validation of Array Index vulnerability in Apache NimBLE.</p>Lack of input validation for HCI events from controller could result in out-of-bound memory corruption and crash.<br>This issue requires broken or bogus Bluetooth controller and thus severity is considered low.<br><p>This issue affects Apache NimBLE: through 1.7.0.</p><p>Users are recommended to upgrade to version 1.8.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7ckxw6481dp68ons627pjcb27c75n0mq


### Credits
* Eunkyu Lee (reporter)


## Lack of input validation in HCI advertising report could lead to potential out-of-bound access ## { #CVE-2024-47250 }

CVE-2024-47250 [\[CVE json\]](./CVE-2024-47250.cve.json) [\[OSV json\]](./CVE-2024-47250.osv.json)



_Last updated: 2024-11-26T11:17:18.104Z_

### Affected

* Apache NimBLE through 1.7.0


### Description

<p>Out-of-bounds Read vulnerability in Apache NimBLE.</p><span style="background-color: rgb(255, 255, 255);">Missing proper validation of HCI advertising report could lead to out-of-bound access when parsing HCI event and thus bogus G</span>AP 'device found' events being sent.<br>This issue requires broken or bogus Bluetooth controller and thus severity is considered low.<br><p>This issue affects Apache NimBLE: through 1.7.0.<br></p><p>Users are recommended to upgrade to version 1.8.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zdb50spojlqbn0yxd866mbzqjt2vpt85


### Credits
* Eunkyu Lee (reporter)


## Lack of input sanitization leading to out-of-bound reads in Number of Completed Packets HCI event handler ## { #CVE-2024-51569 }

CVE-2024-51569 [\[CVE json\]](./CVE-2024-51569.cve.json) [\[OSV json\]](./CVE-2024-51569.osv.json)



_Last updated: 2024-11-26T11:17:54.727Z_

### Affected

* Apache NimBLE through 1.7.0


### Description

<p></p><p>Out-of-bounds Read vulnerability in Apache NimBLE.</p><span style="background-color: rgb(255, 255, 255);">Missing proper validation of HCI Number Of Completed Packets could lead to out-of-bound access when parsing HCI event and invalid read from HCI transport memory.<br></span>This issue requires broken or bogus Bluetooth controller and thus severity is considered low.<br><p>This issue affects Apache NimBLE: through 1.7.0.<br></p><p>Users are recommended to upgrade to version 1.8.0, which fixes the issue.</p><p></p>

### References
* https://lists.apache.org/thread/q0vs5rddx1lho30xnpsrvpzgxqmywnhs


### Credits
* Eunkyu Lee (reporter)
