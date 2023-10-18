---
title: Apache Santuario security advisories
description: Security information for Apache Santuario
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Santuario? You can read more about the projects' security policy on their [security page](https://santuario.apache.org/secadv.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://santuario.apache.org/secadv.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Bypass of the secureValidation property ## { #CVE-2021-40690 }

CVE-2021-40690 [\[CVE json\]](./CVE-2021-40690.cve.json)

### Affected

* Apache Santuario from XML Security for Java before 2.2.3,2.1.7


### Description

All versions of Apache Santuario - XML Security for Java prior to 2.2.3 and 2.1.7 are vulnerable to an issue where the "secureValidation" property is not passed correctly when creating a KeyInfo from a KeyInfoReference element. This allows an attacker to abuse an XPath Transform to extract any local .xml files in a RetrievalMethod element.

### References
* https://lists.apache.org/thread.html/r8848751b6a5dd78cc9e99d627e74fecfaffdfa1bb615dce827aad633%40%3Cdev.santuario.apache.org%3E


### Credits
* An Trinh, Calif.
