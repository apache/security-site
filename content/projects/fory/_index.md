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
