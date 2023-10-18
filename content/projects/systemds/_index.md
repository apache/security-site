---
title: Apache SystemDS security advisories
description: Security information for Apache SystemDS
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache SystemDS? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Denial of service in readExternal method ## { #CVE-2022-26477 }

CVE-2022-26477 [\[CVE json\]](./CVE-2022-26477.cve.json)

### Affected

* Apache SystemDS from unspecified before 2.2.2


### Description

The Security Team noticed that the termination condition of the for loop in the readExternal method is a controllable variable, which, if tampered with, may lead to CPU exhaustion. As a fix, we added an upper bound and termination condition in the read and write logic. We classify it as a "low-priority but useful improvement". SystemDS is a distributed system and needs to serialize/deserialize data but in many code paths (e.g., on Spark broadcast/shuffle or writing to sequence files) the byte stream is anyway protected by additional CRC fingerprints. In this particular case though, the number of decoders is upper-bounded by twice the number of columns, which means an attacker would need to modify two entries in the byte stream in a consistent manner. By adding these checks robustness was strictly improved with almost zero overhead. These code changes are available in versions higher than 2.2.1.

### References
* https://lists.apache.org/thread/r4x2d2r6d4zykdrrx6s2l4qbxgzws0z3


### Credits
* Apache SystemDS is like to thank Apache Security Team for reporting this issue.
