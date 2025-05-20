---
title: Apache ORC security advisories
description: Security information for Apache ORC
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ORC? You can read more about the projects' security policy on their [security page](https://orc.apache.org/security/), and email your report to the [Apache ORC Security Team](mailto:security@orc.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://orc.apache.org/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Potential Heap Buffer Overflow during C++ LZO Decompression ## { #CVE-2025-47436 }

CVE-2025-47436 [\[CVE json\]](./CVE-2025-47436.cve.json) [\[OSV json\]](./CVE-2025-47436.osv.json)



_Last updated: 2025-05-14T13:11:33.684Z_

### Affected

* Apache ORC through 1.8.8
* Apache ORC from 1.9.0 through 1.9.5
* Apache ORC from 2.0.0 through 2.0.4
* Apache ORC from 2.1.0 through 2.1.1


### Description

<p>Heap-based Buffer Overflow vulnerability in Apache ORC.</p><p>A vulnerability has been identified in the ORC C++ LZO decompression logic, where specially crafted malformed ORC files can cause the decompressor to&nbsp;<span style="background-color: rgb(255, 255, 255);">allocate a 250-byte buffer but then attempts to copy 295 bytes into it. It causes memory corruption.</span></p><p>This issue affects Apache ORC C++ library: through 1.8.8, from 1.9.0 through 1.9.5, from 2.0.0 through 2.0.4, from 2.1.0 through 2.1.1.</p><p>Users are recommended to upgrade to version 1.8.9, 1.9.6, 2.0.5, and 2.1.2, which fix the issue.</p>

### References
* https://orc.apache.org/security/CVE-2025-47436/
* https://lists.apache.org/thread/kd6tlv8fs5jybmsgxr4vrkdxyc866wrn


### Credits
* Jason Villaluna (reporter)
