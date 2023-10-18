---
title: Apache MyFaces security advisories
description: Security information for Apache MyFaces
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache MyFaces? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Cross-Site Request Forgery (CSRF) vulnerability in Apache MyFaces ## { #CVE-2021-26296 }

CVE-2021-26296 [\[CVE json\]](./CVE-2021-26296.cve.json)

### Affected

* Apache MyFaces Core from Apache MyFaces Core 2.2 before 2.2.14
* Apache MyFaces Core from Apache MyFaces Core 2.3 before 2.3.8
* Apache MyFaces Core from Apache MyFaces Core 2.3-next before 2.3-next-M5
* Apache MyFaces Core from Apache MyFaces Core 3.0 before 3.0.0


### Description

In the default configuration, Apache MyFaces Core versions 2.2.0 to 2.2.13, 2.3.0 to 2.3.7, 2.3-next-M1 to 2.3-next-M4, and 3.0.0-RC1 use cryptographically weak implicit and explicit cross-site request forgery (CSRF) tokens. Due to that limitation, it is possible (although difficult) for an attacker to calculate a future CSRF token value and to use that value to trick a user into executing unwanted actions on an application.

### References
* https://lists.apache.org/thread.html/r2b73e2356c6155e9ec78fdd8f72a4fac12f3e588014f5f535106ed9b%40%3Cannounce.apache.org%3E


### Credits
* Apache MyFaces would like to thank Wolfgang Ettlinger (Certitude Consulting GmbH)
