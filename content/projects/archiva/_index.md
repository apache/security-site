---
title: Apache Archiva security advisories
description: Security information for Apache Archiva
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Archiva? You can read more about the projects' security policy on their [security page](https://archiva.apache.org/security.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://archiva.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Archiva Arbitrary user password reset vulnerability ## { #CVE-2022-29405 }

CVE-2022-29405 [\[CVE json\]](./CVE-2022-29405.cve.json)

### Affected

* Apache Archiva from 2.2 through 2.2.7


### Description

In Apache Archiva, any registered user can reset password for any users.  This is fixed in Archiva 2.2.8

### References
* https://archiva.apache.org/docs/2.2.8/release-notes.html


## Apache Archiva prior to 2.2.9 may allow the anonymous user to read arbitrary files ## { #CVE-2022-40308 }

CVE-2022-40308 [\[CVE json\]](./CVE-2022-40308.cve.json)

### Affected

* Apache Archiva from Apache Archiva through 2.2.8


### Description

If anonymous read enabled, it's possible to read the database file directly without logging in.


### References
* https://lists.apache.org/thread/x01pnn0jjsw512cscxsbxzrjmz64n4cc


### Credits
* Thanks to L3yx of Syclover Security Team


## Apache Archiva prior to 2.2.9 allows an authenticated user to delete arbitrary directories ## { #CVE-2022-40309 }

CVE-2022-40309 [\[CVE json\]](./CVE-2022-40309.cve.json)

### Affected

* Apache Archiva from unspecified through 2.2.8


### Description

Users with write permissions to a repository can delete arbitrary directories.

### References
* https://lists.apache.org/thread/1odl4p85r96n27k577jk6ftrp19xfc27


### Credits
* Thanks to L3yx of Syclover Security Team


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
