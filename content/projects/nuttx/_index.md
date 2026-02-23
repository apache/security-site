---
title: Apache NuttX security advisories
description: Security information for Apache NuttX
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache NuttX? You can read more about the projects' security policy on their [security page](https://nuttx.apache.org/docs/latest/security.html), and email your report to the [Apache NuttX Security Team](mailto:security@nuttx.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://nuttx.apache.org/docs/latest/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## fs/vfs/fs_rename: use after free ## { #CVE-2025-48769 }

CVE-2025-48769 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-48769) [\[CVE json\]](./CVE-2025-48769.cve.json) [\[OSV json\]](./CVE-2025-48769.osv.json)



_Last updated: 2026-01-01T16:14:32.107Z_

### Affected

* Apache NuttX RTOS from 7.20 before 12.11.0


### Description

<p>Use After Free vulnerability was discovered in fs/vfs/fs_rename code of the Apache NuttX RTOS, that due recursive implementation and single buffer use by two different pointer variables allowed arbitrary user provided size buffer reallocation and write to the previously freed heap chunk, that in specific cases could cause unintended virtual filesystem rename/move operation results.</p><p>This issue affects Apache NuttX RTOS: from 7.20 before 12.11.0.</p><p>Users of virtual filesystem based services with write access especially when exposed over the network (i.e. FTP) are affected and recommended to upgrade to version 12.11.0 that fixes the issue.</p>

### References
* https://github.com/apache/nuttx/pull/16455
* https://lists.apache.org/thread/7m83v11ldfq7bvw72n9t5sccocczocjn


### Credits
* Liu, Richard Jiayang <rjliu3@illinois.edu> (finder)
* Liu, Richard Jiayang <rjliu3@illinois.edu> (remediation developer)
* Tomek CEDRO <cederom@apache.org> (coordinator)
* Xiang Xiao <xiaoxiang@apache.org> (remediation reviewer)
* Jiuzhu Dong <jiuzhudong@apache.org> (remediation reviewer)


## fs/inode: fs_inoderemove root inode removal ## { #CVE-2025-48768 }

CVE-2025-48768 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-48768) [\[CVE json\]](./CVE-2025-48768.cve.json) [\[OSV json\]](./CVE-2025-48768.osv.json)



_Last updated: 2026-01-01T16:13:58.511Z_

### Affected

* Apache NuttX RTOS from 10.0.0 before 12.10.0


### Description

<p>Release of Invalid Pointer or Reference vulnerability was discovered in&nbsp;fs/inode/fs_inoderemove&nbsp;code of the Apache NuttX RTOS that allowed root filesystem inode removal leading to a debug assert trigger (that is disabled by default), NULL pointer dereference (handled differently depending on the target architecture), or in general, a Denial of Service.</p><p>This issue affects Apache NuttX RTOS: from 10.0.0 before 12.10.0.</p><p>Users of filesystem based services with write access that were exposed over the network (i.e. FTP) are affected and recommended to upgrade to version 12.10.0 that fixes the issue.</p>

### References
* https://github.com/apache/nuttx/pull/16437
* https://lists.apache.org/thread/nwo1kd08b7t3dyz082q2pghdxwvxwyvo


### Credits
* Liu, Richard Jiayang <rjliu3@illinois.edu> (finder)
* Liu, Richard Jiayang <rjliu3@illinois.edu> (remediation developer)
* Alan Carvalho de Assis <acassis@apache.org> (remediation reviewer)
* Tomek CEDRO <cederom@apache.org> (coordinator)
* Xiang Xiao <xiaoxiang@apache.org> (remediation reviewer)
* Jiuzhu Dong <jiuzhudong@apache.org> (remediation reviewer)


## examples/xmlrpc: Fix calls buffers size. ## { #CVE-2025-47869 }

CVE-2025-47869 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-47869) [\[CVE json\]](./CVE-2025-47869.cve.json) [\[OSV json\]](./CVE-2025-47869.osv.json)



_Last updated: 2025-06-14T22:55:02.542Z_

### Affected

* Apache NuttX RTOS from 6.22 before 12.9.0


### Description

<p>Improper Restriction of Operations within the Bounds of a Memory Buffer vulnerability was discovered in Apache NuttX RTOS apps/exapmles/xmlrpc application. In this example application device stats structure that stored remotely provided parameters had hardcoded buffer size which could lead to buffer overflow. Structure members buffers were updated to valid size of CONFIG_XMLRPC_STRINGSIZE+1.</p><p>This issue affects Apache NuttX RTOS users that may have used or base their code on example application as presented in releases from 6.22 before 12.9.0.</p><p>Users of XMLRPC in Apache NuttX RTOS are advised to review their code 
for this pattern and update buffer sizes as presented in the version of 
the example in release 12.9.0.<br></p>

### References
* https://github.com/apache/nuttx-apps/pull/3027
* https://lists.apache.org/thread/306qcqyc3bpb2ozh015yxjo9kqs4jbvj


### Credits
* Chánh Phạm <chanhphamviet@gmail.com> (reporter)
* Arnout Engelen <engelen@apache.org> (remediation developer)
* Tomek CEDRO <tomek@cedro.info> (coordinator)
* Alan Carvalho de Assis <acassis@gmail.com> (remediation reviewer)
* Alin Jerpelea <jerpelea@gmail.com> (remediation reviewer)
* Lee, Lup Yuen <luppy@appkaki.com> (remediation reviewer)
* Xiang Xiao <xiaoxiang781216@gmail.com> (remediation reviewer)
* JianyuWang <wangjianyu3@xiaomi.com> (remediation reviewer)


## tools/bdf-converter: Fix loop termination condition. ## { #CVE-2025-47868 }

CVE-2025-47868 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-47868) [\[CVE json\]](./CVE-2025-47868.cve.json) [\[OSV json\]](./CVE-2025-47868.osv.json)



_Last updated: 2025-06-14T22:53:54.263Z_

### Affected

* Apache NuttX RTOS: tools/bdf-converter. from 6.9 before 12.9.0


### Description

<p>Out-of-bounds Write resulting in possible Heap-based Buffer Overflow vulnerability was discovered in tools/bdf-converter font conversion utility that is part of Apache NuttX RTOS repository. This standalone program is optional and neither part of NuttX RTOS nor Applications runtime, but active bdf-converter users may be affected when this tool is exposed to external provided user data data (i.e. publicly available automation).</p><p>This issue affects Apache NuttX: from 6.9 before 12.9.0.</p><p>Users are recommended to upgrade to version 12.9.0, which fixes the issue.</p>

### References
* https://github.com/apache/nuttx/pull/16000
* https://lists.apache.org/thread/p4o2lcqgspx3ws1n2p4wmoqbqow1w1pw


### Credits
* Chánh Phạm <chanhphamviet@gmail.com> (finder)
* Nathan Hartman <hartman.nathan@gmail.com> (remediation developer)
* Tomek CEDRO <tomek@cedro.info> (coordinator)
* Alan Carvalho de Assis <acassis@gmail.com> (remediation reviewer)
* Alin Jerpelea <jerpelea@gmail.com> (remediation reviewer)
* Lee, Lup Yuen <luppy@appkaki.com> (remediation reviewer)
* Arnout Engelen <engelen@apache.org> (coordinator)


## NuttX Bluetooth Stack HCI and UART DoS/RCE Vulnerabilities. ## { #CVE-2025-35003 }

CVE-2025-35003 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-35003) [\[CVE json\]](./CVE-2025-35003.cve.json) [\[OSV json\]](./CVE-2025-35003.osv.json)



_Last updated: 2025-06-14T22:46:25.637Z_

### Affected

* Apache NuttX RTOS from 7.25 before 12.9.0


### Description

<p>Improper Restriction of Operations within the Bounds of a Memory Buffer and Stack-based Buffer Overflow vulnerabilities were discovered in Apache NuttX RTOS Bluetooth Stack (HCI and UART components) that may result in system crash, denial of service, or arbitrary code execution, after receiving maliciously crafted packets.</p><p>NuttX's Bluetooth HCI/UART stack users are advised to upgrade to version 12.9.0, which fixes the identified implementation issues.</p><p>This issue affects Apache NuttX: from 7.25 before 12.9.0. <br></p><p></p>

### References
* https://github.com/apache/nuttx/pull/16179
* https://lists.apache.org/thread/k4xzz3jhkx48zxw9vwmqrmm4hmg78vsj


### Credits
* Chongqing Lei <leicq@seu.edu.cn> (reporter)
* Zhen Ling <zhenling@seu.edu.cn> (reporter)
* Chongqing Lei <leicq@seu.edu.cn> (remediation developer)
* Tomek CEDRO <tomek@cedro.info> (coordinator)


## malloc, realloc and memalign implementations are vulnerable to integer wrap-arounds ## { #CVE-2021-26461 }

CVE-2021-26461 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-26461) [\[CVE json\]](./CVE-2021-26461.cve.json) [\[OSV json\]](./CVE-2021-26461.osv.json)



_Last updated: 2021-06-21T17:05:46.935Z_

### Affected

* Apache NuttX from Apache NuttX before 10.1.0


### Description

Apache Nuttx Versions prior to 10.1.0 are vulnerable to integer wrap-around in functions malloc, realloc and memalign. This improper memory assignment can lead to arbitrary memory allocation, resulting in unexpected behavior such as a crash or a remote code injection/execution. 

### References
* https://lists.apache.org/thread.html/r806fccf8b003ae812d807c6c7d97950d44ed29b2713418cbe3f2bddd%40%3Cdev.nuttx.apache.org%3E


### Credits
* Apache NuttX would like to thank Omri Ben-Bassat of Section 52 at Azure Defender for IoT of Microsoft Corp for bringing this issue to our attention.


## Apache NuttX (incubating) Out of Bound Write from invalid fragmentation offset value specified in the IP header ## { #CVE-2020-17529 }

CVE-2020-17529 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17529) [\[CVE json\]](./CVE-2020-17529.cve.json) [\[OSV json\]](./CVE-2020-17529.osv.json)



_Last updated: 2020-12-09T16:35:02.859Z_

### Affected

* Apache NuttX (incubating) at 10.0.0
* Apache NuttX (incubating) from unspecified through 9.1.0


### Description

Out-of-bounds Write vulnerability in TCP Stack of Apache NuttX (incubating) versions up to and including 9.1.0 and 10.0.0 allows attacker to corrupt memory by supplying and invalid fragmentation offset value specified in the IP header.  This is only impacts builds with both CONFIG_EXPERIMENTAL  and CONFIG_NET_TCP_REASSEMBLY build flags enabled.

### References
* https://lists.apache.org/thread.html/r4d71ae3ab96b589835b94ba7ac4cb88a704e7307bceefeab749366f3%40%3Cdev.nuttx.apache.org%3E


### Credits
* Apache NuttX would like to thank Forescout for reporting the issue


## Apache NuttX (incubating) Out of Bound Write from invalid TCP Urgent length ## { #CVE-2020-17528 }

CVE-2020-17528 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17528) [\[CVE json\]](./CVE-2020-17528.cve.json) [\[OSV json\]](./CVE-2020-17528.osv.json)



_Last updated: 2020-12-09T16:34:56.566Z_

### Affected

* Apache NuttX (incubating) at 10.0.0
* Apache NuttX (incubating) from unspecified before 9.1.1


### Description

Out-of-bounds Write vulnerability in TCP stack of Apache NuttX (incubating) versions up to and including 9.1.0 and 10.0.0 allows attacker to corrupt memory by supplying arbitrary urgent data pointer offsets within TCP packets including beyond the length of the packet.

### References
* https://lists.apache.org/thread.html/r7f4215aba288660b41b7e731b6262c8275fa476e91e527a74d2888ea%40%3Cdev.nuttx.apache.org%3E


### Credits
* Apache NuttX would like to thank Forescout for reporting the issue
