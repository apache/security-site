---
title: Apache Archiva security advisories
description: Security information for Apache Archiva
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Archiva? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Archiva privilege escalation ## { #CVE-2023-28158 }

CVE-2023-28158 [\[CVE json\]](./CVE-2023-28158.cve.json)

### Affected

* Apache Archiva from 2.0 before 2.2.10


### Description

Privilege escalation via stored XSS using the file upload service to upload malicious content.<br><span style="background-color: rgb(255, 255, 255);">The issue can be exploited only by authenticated users which can create directory name to inject some XSS content and gain some privileges such admin user.</span><br><br>

### References
* https://lists.apache.org/thread/8pm6d5y9cptznm0bdny3n8voovmm0dtt


### Credits
* sandr0 (sandr0.xyz)  (finder)
