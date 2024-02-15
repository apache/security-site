---
title: Apache Cayenne security advisories
description: Security information for Apache Cayenne
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Cayenne? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Deserialization of untrusted data in the Hessian Component of Apache Cayenne 4.1 with older Java versions ## { #CVE-2022-24289 }

CVE-2022-24289 [\[CVE json\]](./CVE-2022-24289.cve.json)

_Last updated: 2022-02-11T22:06:23.179Z_

### Affected

* Apache Cayenne from 4.1 through 4.1


### Description

Hessian serialization is a network protocol that supports object-based transmission.
Apache Cayenne's optional Remote Object Persistence (ROP) feature is a web services-based technology that provides object persistence and query functionality to 'remote' applications.

In Apache Cayenne 4.1 and earlier, running on non-current patch versions of Java, an attacker with client access to Cayenne ROP can transmit a malicious payload to any vulnerable third-party dependency on the server.  This can result in arbitrary code execution.


### References
* https://lists.apache.org/thread/zthjy83t3o66x7xcbygn2vg3yjvlc9vc
* https://lists.apache.org/thread/6dbw9xmkmc32db057wnng0m93g3nbxkt


### Credits
* Panda
