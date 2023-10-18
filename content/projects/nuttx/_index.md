---
title: Apache NuttX security advisories
description: Security information for Apache NuttX
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache NuttX? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache NuttX (incubating) Out of Bound Write from invalid fragmentation offset value specified in the IP header ## { #CVE-2020-17529 }

CVE-2020-17529 [\[CVE json\]](./CVE-2020-17529.cve.json)

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

CVE-2020-17528 [\[CVE json\]](./CVE-2020-17528.cve.json)

### Affected

* Apache NuttX (incubating) at 10.0.0
* Apache NuttX (incubating) from unspecified before 9.1.1


### Description

Out-of-bounds Write vulnerability in TCP stack of Apache NuttX (incubating) versions up to and including 9.1.0 and 10.0.0 allows attacker to corrupt memory by supplying arbitrary urgent data pointer offsets within TCP packets including beyond the length of the packet.

### References
* https://lists.apache.org/thread.html/r7f4215aba288660b41b7e731b6262c8275fa476e91e527a74d2888ea%40%3Cdev.nuttx.apache.org%3E


### Credits
* Apache NuttX would like to thank Forescout for reporting the issue


## malloc, realloc and memalign implementations are vulnerable to integer wrap-arounds ## { #CVE-2021-26461 }

CVE-2021-26461 [\[CVE json\]](./CVE-2021-26461.cve.json)

### Affected

* Apache NuttX from Apache NuttX before 10.1.0


### Description

Apache Nuttx Versions prior to 10.1.0 are vulnerable to integer wrap-around in functions malloc, realloc and memalign. This improper memory assignment can lead to arbitrary memory allocation, resulting in unexpected behavior such as a crash or a remote code injection/execution. 

### References
* https://lists.apache.org/thread.html/r806fccf8b003ae812d807c6c7d97950d44ed29b2713418cbe3f2bddd%40%3Cdev.nuttx.apache.org%3E


### Credits
* Apache NuttX would like to thank Omri Ben-Bassat of Section 52 at Azure Defender for IoT of Microsoft Corp for bringing this issue to our attention.
