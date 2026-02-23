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

## Incorrect handling of SMP Security Request could lead to undesirable pairing ## { #CVE-2025-62235 }

CVE-2025-62235 [\[CVE json\]](./CVE-2025-62235.cve.json) [\[OSV json\]](./CVE-2025-62235.osv.json)



_Last updated: 2026-01-10T09:42:36.935Z_

### Affected

* Apache Mynewt NimBLE through 1.8.0


### Description

<p>Authentication Bypass by Spoofing vulnerability in Apache NimBLE.</p>Receiving specially crafted Security Request could lead to removal of original bond<span style="background-color: rgb(255, 255, 255);">&nbsp;and re-bond with impostor.</span><br><p>This issue affects Apache NimBLE: through 1.8.0.</p><p>Users are recommended to upgrade to version 1.9.0, which fixes the issue.</p>

### References
* https://github.com/apache/mynewt-nimble/commit/41f67e391e788c5feef9030026cc5cbc5431838a
* https://lists.apache.org/thread/rw2mrpfwb9d9wmq4h4b6ctcd6gpkk2ho


### Credits
* Tommaso Sacchetti <tommaso.sacchetti@gmail.com> (reporter)


## NULL Pointer Dereference in NimBLE host HCI layer ## { #CVE-2025-53477 }

CVE-2025-53477 [\[CVE json\]](./CVE-2025-53477.cve.json) [\[OSV json\]](./CVE-2025-53477.osv.json)



_Last updated: 2026-01-10T09:45:08.352Z_

### Affected

* Apache Mynewt NimBLE through 1.8.0


### Description

<p>NULL Pointer Dereference vulnerability in Apache Nimble.</p><span style="background-color: rgb(255, 255, 255);">Missing validation of HCI connection complete or HCI command TX buffer could lead to NULL pointer dereference.</span><br>This issue requires disabled asserts and broken or bogus Bluetooth controller and thus severity is considered low.<br><br><p>This issue affects Apache NimBLE: through 1.8.0.</p><p>Users are recommended to upgrade to version 1.9.0, which fixes the issue.</p>

### References
* https://github.com/apache/mynewt-nimble/commit/0caf9baeb271ede85fcc5237ab87ddbf938600da
* https://github.com/apache/mynewt-nimble/commit/3160b8c4c7ff8db4e0f9badcdf7df684b151e077
* https://lists.apache.org/thread/1dxthc132hwm2tzvjblrtnschcsbw2vo


### Credits
* 雷重庆 <leicq@seu.edu.cn> (reporter)


## Out-of-Bounds Write Vulnerability in NimBLE HCI H4 driver ## { #CVE-2025-53470 }

CVE-2025-53470 [\[CVE json\]](./CVE-2025-53470.cve.json) [\[OSV json\]](./CVE-2025-53470.osv.json)



_Last updated: 2026-01-10T09:46:32.072Z_

### Affected

* Apache Mynewt NimBLE through 1.8


### Description

<p>Out-of-bounds Read vulnerability in Apache  NimBLE HCI H4 driver. Specially crafted HCI event could lead to invalid memory read in H4 driver.</p><p>This issue affects Apache NimBLE: through 1.8.&nbsp;</p><p>This issue requires a broken or bogus Bluetooth controller and thus severity is considered low.</p><p>Users are recommended to upgrade to version 1.9, which fixes the issue.</p>

### References
* https://github.com/apache/mynewt-nimble/commit/b973df0c6cf7b30efbf8eb2cafdc1ee843464b76
* https://lists.apache.org/thread/32sm0944dyod4sdql77stgyw9xb2msc0


### Credits
* 雷重庆 <leicq@seu.edu.cn> (reporter)


## Invalid error handling in pause encryption procedure in NimBLE controller ## { #CVE-2025-52435 }

CVE-2025-52435 [\[CVE json\]](./CVE-2025-52435.cve.json) [\[OSV json\]](./CVE-2025-52435.osv.json)



_Last updated: 2026-01-10T09:47:08.833Z_

### Affected

* Apache Mynewt NimBLE through 1.8.0


### Description

<p>J2EE Misconfiguration: Data Transmission Without Encryption vulnerability in Apache NimBLE.</p>Improper handling of Pause Encryption procedure on Link Layer results in a previously encrypted connection being left in un-encrypted state <span style="background-color: rgb(255, 255, 255);">allowing an eavesdropper to observe the remainder of the exchange</span>.<br><p>This issue affects Apache NimBLE: through &lt;= 1.8.0.</p><p>Users are recommended to upgrade to version 1.9.0, which fixes the issue.</p>

### References
* https://github.com/apache/mynewt-nimble/commit/164f1c23c18a290908df76ed83fe848bfe4a4903
* https://github.com/apache/mynewt-nimble/commit/ec3d75e909fa6dcadf1836fefc4432794a673d18
* https://lists.apache.org/thread/ow8dzpsqfh9llfclh5fzh6z237brzc0s


### Credits
* Henrik Schnor <henrik.schnor@mailbox.org> (reporter)


## Lack of input sanitization leading to out-of-bound reads in Number of Completed Packets HCI event handler ## { #CVE-2024-51569 }

CVE-2024-51569 [\[CVE json\]](./CVE-2024-51569.cve.json) [\[OSV json\]](./CVE-2024-51569.osv.json)



_Last updated: 2024-12-06T07:50:42.419Z_

### Affected

* Apache NimBLE through 1.7.0


### Description

<p></p><p>Out-of-bounds Read vulnerability in Apache NimBLE.</p><span style="background-color: rgb(255, 255, 255);">Missing proper validation of HCI Number Of Completed Packets could lead to out-of-bound access when parsing HCI event and invalid read from HCI transport memory.<br></span>This issue requires broken or bogus Bluetooth controller and thus severity is considered low.<br><p>This issue affects Apache NimBLE: through 1.7.0.<br></p><p>Users are recommended to upgrade to version 1.8.0, which fixes the issue.</p><p></p>

### References
* https://lists.apache.org/thread/q0vs5rddx1lho30xnpsrvpzgxqmywnhs


### Credits
* Eunkyu Lee (reporter)


## Lack of input validation in HCI advertising report could lead to potential out-of-bound access ## { #CVE-2024-47250 }

CVE-2024-47250 [\[CVE json\]](./CVE-2024-47250.cve.json) [\[OSV json\]](./CVE-2024-47250.osv.json)



_Last updated: 2024-12-06T07:50:00.629Z_

### Affected

* Apache NimBLE through 1.7.0


### Description

<p>Out-of-bounds Read vulnerability in Apache NimBLE.</p><span style="background-color: rgb(255, 255, 255);">Missing proper validation of HCI advertising report could lead to out-of-bound access when parsing HCI event and thus bogus G</span>AP 'device found' events being sent.<br>This issue requires broken or bogus Bluetooth controller and thus severity is considered low.<br><p>This issue affects Apache NimBLE: through 1.7.0.<br></p><p>Users are recommended to upgrade to version 1.8.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zdb50spojlqbn0yxd866mbzqjt2vpt85


### Credits
* Eunkyu Lee (reporter)


## Lack of input sanitization leading to out-of-bound reads in multiple advertisement handler ## { #CVE-2024-47249 }

CVE-2024-47249 [\[CVE json\]](./CVE-2024-47249.cve.json) [\[OSV json\]](./CVE-2024-47249.osv.json)



_Last updated: 2024-12-06T07:49:57.242Z_

### Affected

* Apache NimBLE through 1.7.0


### Description

<p>Improper Validation of Array Index vulnerability in Apache NimBLE.</p>Lack of input validation for HCI events from controller could result in out-of-bound memory corruption and crash.<br>This issue requires broken or bogus Bluetooth controller and thus severity is considered low.<br><p>This issue affects Apache NimBLE: through 1.7.0.</p><p>Users are recommended to upgrade to version 1.8.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7ckxw6481dp68ons627pjcb27c75n0mq


### Credits
* Eunkyu Lee (reporter)


## Buffer overflow in NimBLE MESH Bluetooth stack ## { #CVE-2024-47248 }

CVE-2024-47248 [\[CVE json\]](./CVE-2024-47248.cve.json) [\[OSV json\]](./CVE-2024-47248.osv.json)



_Last updated: 2024-12-06T07:39:45.067Z_

### Affected

* Apache NimBLE through 1.7.0


### Description

<p>Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') vulnerability in Apache NimBLE.</p>Specially crafted MESH message could result in memory corruption when non-default build configuration is used.<br><p>This issue affects Apache NimBLE: through 1.7.0.</p><p>Users are recommended to upgrade to version 1.8.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/z8m7jqh54xybf9kz8q2l3tz92zsj7tmz


### Credits
* Wei Che Kao (Xiaobye), graduate student from National Yang Ming Chiao Tung University, Dept. of CS, Security and Systems Lab. (reporter)


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
