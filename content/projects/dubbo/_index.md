---
title: Apache Dubbo security advisories
description: Security information for Apache Dubbo
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Dubbo? You can read more about the projects' security policy on their [security page](https://dubbo.apache.org/en/docs/notices/security/), and email your report to the [Apache Dubbo Security Team](mailto:security@dubbo.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://dubbo.apache.org/en/docs/notices/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Dubbo Deserialization Vulnerability Gadgets Bypass ## { #CVE-2023-23638 }

CVE-2023-23638 [\[CVE json\]](./CVE-2023-23638.cve.json)

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x through 2.7.21
* Apache Dubbo from Apache Dubbo 3.0.x through 3.0.13
* Apache Dubbo from Apache Dubbo 3.1.x through 3.1.5


### Description

A deserialization vulnerability existed when dubbo generic invoke, which could lead to malicious code execution. <br><br>This issue affects Apache Dubbo 2.7.x version 2.7.21 and prior versions; Apache Dubbo 3.0.x version 3.0.13 and prior versions; Apache Dubbo 3.1.x version 3.1.5 and prior versions. 

### References
* https://lists.apache.org/thread/8h6zscfzj482z512d2v5ft63hdhzm0cb


### Credits
* yemoli、R1ckyZ、Koishi、cxc (reporter)
