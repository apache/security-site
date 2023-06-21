---
title: Apache Atlas security advisories
description: Security information for Apache Atlas
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Atlas? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

## zip path traversal in import functionality ## { #CVE-2022-34271 }

[CVE-2022-34271](./CVE-2022-34271.cve.json)

### Affected

* Apache Atlas versions 0.8.4 before 2.3.0


### Description

A vulnerability in import module of Apache Atlas allows an authenticated user to write to web server filesystem.  This issue affects Apache Atlas versions from 0.8.4 to 2.2.0.