---
title: Apache OpenOffice security advisories
description: Security information for Apache OpenOffice
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache OpenOffice? You can read more about the projects' security policy on their [security page](https://openoffice.apache.org/security), and email your report to the  [Apache OpenOffice Security Team](mailto:security@openoffice.apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache OpenOffice since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. It may also lack details found on the [project security page](https://openoffice.apache.org/security).

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Empty entry in Java class path ## { #CVE-2022-38745 }

[CVE-2022-38745](./CVE-2022-38745.cve.json)

### Affected

* Apache OpenOffice before 4.1.14


### Description

<div>Apache OpenOffice versions before 4.1.14 may be configured to add an empty entry to the Java class path. This may lead to run arbitrary Java code from the current directory.<br></div>

### References
* https://lists.apache.org/thread/q3noq7m681kvtb29m28x74q8cnwnzzo0
* https://www.openoffice.org/security/cves/CVE-2022-38745.html


## Macro URL arbitrary script execution ## { #CVE-2022-47502 }

[CVE-2022-47502](./CVE-2022-47502.cve.json)

### Affected

* Apache OpenOffice through 4.1.13


### Description

<p>Apache OpenOffice documents can contain links that call internal macros with arbitrary arguments. Several URI Schemes are defined for this purpose.<br></p><p>Links can be activated by clicks, or by automatic document events.</p><p>The execution of such links must be subject to user approval.</p><p>In the affected versions of OpenOffice, approval for certain links is not   requested; when activated, such links could therefore result in arbitrary script execution.<br></p>

### References
* https://lists.apache.org/thread/xr6tl91jj2jgcq8pdbrc4d8w13s6xn80
* https://www.openoffice.org/security/cves/CVE-2022-47502.html
