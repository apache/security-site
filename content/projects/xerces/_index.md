---
title: Apache Xerces security advisories
description: Security information for Apache Xerces
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Xerces? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Infinite loop within Apache XercesJ xml parser ## { #CVE-2022-23437 }

CVE-2022-23437 [\[CVE json\]](./CVE-2022-23437.cve.json)

_Last updated: 2022-01-24T14:59:39.857Z_

### Affected

* Apache Xerces from Apache XercesJ through 2.12.1


### Description

There's a vulnerability within the Apache Xerces Java (XercesJ) XML parser when handling specially crafted XML document payloads. This causes, the XercesJ XML parser to wait in an infinite loop, which may sometimes consume system resources for prolonged duration. This vulnerability is present within XercesJ version 2.12.1 and the previous versions.

### References
* https://lists.apache.org/thread/6pjwm10bb69kq955fzr1n0nflnjd27dl


### Credits
* This issue was discovered by Sergey Temnikov and Ziyi Luo, from Amazon Corretto/JDK Team
