---
title: Apache Dubbo security advisories
description: Security information for Apache Dubbo
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Dubbo? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Dubbo since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Apache Dubbo Deserialization Vulnerability Gadgets Bypass ## { #CVE-2023-23638 }

[CVE-2023-23638](./CVE-2023-23638.cve.json)

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x through 2.7.21
* Apache Dubbo from Apache Dubbo 3.0.x through 3.0.13
* Apache Dubbo from Apache Dubbo 3.1.x through 3.1.5


### Description

A deserialization vulnerability existed when dubbo generic invoke, which could lead to malicious code execution. <br><br>This issue affects Apache Dubbo 2.7.x version 2.7.21 and prior versions; Apache Dubbo 3.0.x version 3.0.13 and prior versions; Apache Dubbo 3.1.x version 3.1.5 and prior versions. 

### References
* https://lists.apache.org/thread/8h6zscfzj482z512d2v5ft63hdhzm0cb
