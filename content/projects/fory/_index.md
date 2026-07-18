---
title: Apache Fory security advisories
description: Security information for Apache Fory
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Fory? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Fory).

You can read more about the security policy on:

- [Apache Fory security model](https://github.com/apache/fory/blob/main/docs/security/threat-model.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Java ReplaceResolverSerializer deserialization checks bypass ## { #CVE-2026-50076 }

CVE-2026-50076 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50076) [\[CVE json\]](./CVE-2026-50076.cve.json) [\[OSV json\]](./CVE-2026-50076.osv.json)



_Last updated: 2026-06-04T09:08:27.361Z_

### Affected

* Apache Fory before 1.1.0


### Description

<p>Deserialization of Untrusted Data in the Java replace-resolve path in Apache Fory fory-core Java SDK before 1.1.0 on Java/JVM platforms allows a remote attacker to bypass class registration, TypeChecker, and DisallowedList checks and invoke classpath-present readResolve/readExternal hooks via crafted Fory serialized data.</p><p>Users are recommended to upgrade to version 1.1.0 or later, which fixes this issue.</p><br>

### References
* https://fory.apache.org/security


### Credits
* Venkatraman Kumar (r3dw0lfsec), Securin (reporter)


## PyFory ReduceSerializer Incomplete Policy Enforcement ## { #CVE-2026-48207 }

CVE-2026-48207 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48207) [\[CVE json\]](./CVE-2026-48207.cve.json) [\[OSV json\]](./CVE-2026-48207.osv.json)



_Last updated: 2026-05-21T12:44:21.497Z_

### Affected

* Apache Fory from 0.13.0 before 1.0.0


### Description

<p><span style="background-color: rgb(255, 255, 255);">Deserialization of untrusted data in Apache Fory PyFory. PyFory's ReduceSerializer could bypass documented DeserializationPolicy validation hooks during reduce-state restoration and global-name resolution. An application is vulnerable if it deserializes attacker-controlled data using PyFory Python-native mode with strict mode disabled and relies on DeserializationPolicy to restrict unsafe classes, functions, or module attributes.</span></p><p>This issue affects Apache Fory: from before 1.0.0.</p><p><span style="background-color: rgb(255, 255, 255);">Mitigation: Users of Apache Fory are recommended to upgrade to version 1.0.0 or later, which enforces DeserializationPolicy validation for the affected ReduceSerializer paths and thus fixes this issue.</span><br><br><br></p>

### References
* https://fory.apache.org/security/#cve-2026-48207-pyfory-reduceserializer-deserializationpolicy-bypass


### Credits
* Lide Wen (reporter)


## Python RCE via unguarded pickle fallback serializer in pyfory ## { #CVE-2025-61622 }

CVE-2025-61622 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-61622) [\[CVE json\]](./CVE-2025-61622.cve.json) [\[OSV json\]](./CVE-2025-61622.osv.json)



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


## Denial of Service (DoS) due to Deserialization of Untrusted malicious large Data ## { #CVE-2025-59328 }

CVE-2025-59328 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-59328) [\[CVE json\]](./CVE-2025-59328.cve.json) [\[OSV json\]](./CVE-2025-59328.osv.json)



_Last updated: 2025-09-15T16:26:55.892Z_

### Affected

* Apache Fory from 0.5.0 through 0.12.1


### Description

<p></p><p>A vulnerability in Apache Fory allows a remote attacker to cause a Denial of Service (DoS). The issue stems from the insecure deserialization of untrusted data. An attacker can supply a <strong>large, specially crafted data payload</strong>&nbsp;that, when processed, consumes an excessive amount of CPU resources during the deserialization process. This leads to CPU exhaustion, rendering the application or system using the Apache Fory library unresponsive and unavailable to legitimate users.</p><p>Users of Apache Fory are strongly advised to upgrade to version <strong>0.12.2 or later</strong>&nbsp;to mitigate this vulnerability. Developers of libraries and applications that depend on Apache Fory should update their dependency requirements to Apache Fory <strong>0.12.2 or later</strong>&nbsp;and release new versions of their software.</p><p></p>

### References
* https://fory.apache.org/security/


### Credits
* r00t4dm of meituan security (reporter)
