---
title: Apache Atlas security advisories
description: Security information for Apache Atlas
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Atlas? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Atlas since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## zip path traversal in import functionality ## { #CVE-2022-34271 }

[CVE-2022-34271](./CVE-2022-34271.cve.json)

### Affected

* Apache Atlas from 0.8.4 before 2.3.0


### Description

A vulnerability in import module of Apache Atlas allows an authenticated user to write to web server filesystem.  This issue affects Apache Atlas versions from 0.8.4 to 2.2.0.

### References
* https://lists.apache.org/thread/0rqvcxo6brmos9w3lzfsdn2lsmlblpw3
