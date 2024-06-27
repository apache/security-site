---
title: Apache Atlas security advisories
description: Security information for Apache Atlas
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Atlas? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## zip path traversal in import functionality ## { #CVE-2022-34271 }

CVE-2022-34271 [\[CVE json\]](./CVE-2022-34271.cve.json) [\[OSV json\]](./CVE-2022-34271.osv.json)



_Last updated: 2022-12-14T08:34:57.194Z_

### Affected

* Apache Atlas from 0.8.4 before 2.3.0


### Description

A vulnerability in import module of Apache Atlas allows an authenticated user to write to web server filesystem.  This issue affects Apache Atlas versions from 0.8.4 to 2.2.0.

### References
* https://lists.apache.org/thread/0rqvcxo6brmos9w3lzfsdn2lsmlblpw3


### Credits
* Huangzhicong (finder)
