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

CVE-2024-24746 [\[CVE json\]](./CVE-2024-24746.cve.json)

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
