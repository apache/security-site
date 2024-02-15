---
title: Apache jUDDI security advisories
description: Security information for Apache jUDDI
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache jUDDI? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Remote code execution via RMI ## { #CVE-2021-37578 }

CVE-2021-37578 [\[CVE json\]](./CVE-2021-37578.cve.json)

### Affected

* Apache jUDDI from unspecified before 3.3.10


### Description

Apache jUDDI uses several classes related to Java's Remote Method Invocation (RMI) which (as an extension to UDDI) provides an alternate transport for accessing UDDI services.

RMI uses the default Java serialization mechanism to pass parameters in RMI invocations. A remote attacker can send a malicious serialized object to the above RMI entries. The objects get deserialized without any check on the incoming data. In the worst case, it may let the attacker run arbitrary code remotely. 

For both jUDDI web service applications and jUDDI clients, the usage of RMI is disabled by default. Since this is an optional feature and an extension to the UDDI protocol, the likelihood of impact is low. Starting with 3.3.10, all RMI related code was removed.

### References
* https://lists.apache.org/thread.html/r82047b3ba774cf870ea8e1e9ec51c6107f6cd056d4e36608148c6e71%40%3Cprivate.juddi.apache.org%3E


### Credits
* Reported by Artem Smotrakov
