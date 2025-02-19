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


## An authenticated user can perform XSS and potentially impersonate another user ## { #CVE-2024-46910 }

CVE-2024-46910 [\[CVE json\]](./CVE-2024-46910.cve.json) [\[OSV json\]](./CVE-2024-46910.osv.json)



_Last updated: 2025-02-13T08:52:51.188Z_

### Affected

* Apache Atlas from 2.0.0 through 2.3.0


### Description

<p>An authenticated user can perform XSS and potentially impersonate another user.</p><p>This issue affects Apache Atlas <span style="background-color: rgb(255, 255, 255);">versions&nbsp;</span>2.3.0 and earlier.</p><p>Users are recommended to upgrade to version 2.4.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/sqzp34l4cdk21zoq5g31qlsvr7jvb1fy


### Credits
* basavaraj@seciqtech.com (finder)
