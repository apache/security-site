---
title: Apache Fory security advisories
description: Security information for Apache Fory
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Fory? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Denial of Service (DoS) due to Deserialization of Untrusted malicious large Data ## { #CVE-2025-59328 }

CVE-2025-59328 [\[CVE json\]](./CVE-2025-59328.cve.json) [\[OSV json\]](./CVE-2025-59328.osv.json)



_Last updated: 2025-09-15T16:26:55.892Z_

### Affected

* Apache Fory from 0.5.0 through 0.12.1


### Description

<p></p><p>A vulnerability in Apache Fory allows a remote attacker to cause a Denial of Service (DoS). The issue stems from the insecure deserialization of untrusted data. An attacker can supply a <strong>large, specially crafted data payload</strong>&nbsp;that, when processed, consumes an excessive amount of CPU resources during the deserialization process. This leads to CPU exhaustion, rendering the application or system using the Apache Fory library unresponsive and unavailable to legitimate users.</p><p>Users of Apache Fory are strongly advised to upgrade to version <strong>0.12.2 or later</strong>&nbsp;to mitigate this vulnerability. Developers of libraries and applications that depend on Apache Fory should update their dependency requirements to Apache Fory <strong>0.12.2 or later</strong>&nbsp;and release new versions of their software.</p><p></p>

### References
* https://fory.apache.org/security/


### Credits
* r00t4dm of meituan security (reporter)


## Python RCE via unguarded pickle fallback serializer in pyfory ## { #CVE-2025-61622 }

CVE-2025-61622 [\[CVE json\]](./CVE-2025-61622.cve.json) [\[OSV json\]](./CVE-2025-61622.osv.json)



_Last updated: 2025-10-04T14:58:38.087Z_

### Affected

* Apache Fory from 0.12.0 through 0.12.2
* Apache Fory from 0.1.0 through 0.10.3


### Description

<span style="background-color: rgb(255, 255, 255);">Deserialization of untrusted data in&nbsp;python in <span style="background-color: rgb(255, 255, 255);">pyfory&nbsp;</span>versions 0.12.0 through 0.12.2, or the&nbsp;<span style="background-color: rgb(255, 255, 255);">legacy&nbsp;<span style="background-color: rgb(255, 255, 255);">pyfury versions from</span></span><span style="background-color: rgb(255, 255, 255);">&nbsp;0.1.0 through 0.10.3:</span> allows arbitrary code execution. An application is vulnerable if it reads pyfory serialized data from untrusted sources.&nbsp;<span style="background-color: rgb(255, 255, 255);">An attacker can craft a data stream that selects pickle-fallback serializer during deserialization, leading to the execution of `pickle.loads`, which is&nbsp;vulnerable to&nbsp;<span style="background-color: rgb(255, 255, 255);">remote code execution.<br><br>Users are recommended to upgrade to pyfory version 0.12.3 or later, which has removed pickle fallback serializer and thus fixes this issue.<br></span></span></span><br>

### References
* https://lists.apache.org/thread/vfn9hp9qt06db5yo1gmj3l114o3o2csd


### Credits
* bugbunny.ai (reporter)
