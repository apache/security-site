---
title: Apache Dubbo security advisories
description: Security information for Apache Dubbo
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Dubbo? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

## Apache Dubbo Deserialization Vulnerability Gadgets Bypass ## { #CVE-2023-23638 }

[CVE-2023-23638](./CVE-2023-23638.cve.json)

### Affected

* Apache Dubbo versions Apache Dubbo 2.7.x including 2.7.21Apache Dubbo 3.0.x including 3.0.13Apache Dubbo 3.1.x including 3.1.5


### Description

A deserialization vulnerability existed when dubbo generic invoke, which could lead to malicious code execution. <br><br>This issue affects Apache Dubbo 2.7.x version 2.7.21 and prior versions; Apache Dubbo 3.0.x version 3.0.13 and prior versions; Apache Dubbo 3.1.x version 3.1.5 and prior versions. 