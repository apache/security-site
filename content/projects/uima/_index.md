---
title: Apache UIMA security advisories
description: Security information for Apache UIMA
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache UIMA? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache UIMA prior to 3.3.1 has a path traversal vulnerability when extracting (PEAR) archives ## { #CVE-2022-32287 }

CVE-2022-32287 [\[CVE json\]](./CVE-2022-32287.cve.json)

### Affected

* Apache UIMA from Java SDK through 3.3.0


### Description

A relative path traversal vulnerability in a FileUtil class used by the PEAR management component of Apache UIMA allows an attacker to create files outside the designated target directory using carefully crafted ZIP entry names. This issue affects Apache UIMA Apache UIMA version 3.3.0 and prior versions. 

Note that PEAR files should never be installed into an UIMA installation from untrusted sources because PEAR archives are executable plugins that will be able to perform any actions with the same privileges as the host Java Virtual Machine.

### References
* https://lists.apache.org/thread/57vk0d79j94d0lk0vol8xn935yv1shdd


### Credits
* Apache UIMA would like to thank Huangzhicong from CodeSafe Team of Legendsec at Qi'anxin Group


## DUCC (EOL) allows RCE ## { #CVE-2023-28935 }

CVE-2023-28935 [\[CVE json\]](./CVE-2023-28935.cve.json)

### Affected

* Apache UIMA DUCC through *


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache UIMA DUCC.<br></div><div>When using the "Distributed UIMA Cluster Computing" (DUCC) module of Apache UIMA, an authenticated user that has the permissions to modify core entities can cause command execution as the system user that runs the web process.<br></div><div>As the "Distributed UIMA Cluster Computing" module for UIMA is retired, we do not plan to release a fix for this issue.<br>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</div>

### References
* https://lists.apache.org/thread/r19z14b9rrfxv72r93q5trq5tyffo75g


### Credits
* Crilwa (finder)
