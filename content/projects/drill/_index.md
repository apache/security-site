---
title: Apache Drill security advisories
description: Security information for Apache Drill
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Drill? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## XXE Vulnerability in XML Format Reader ## { #CVE-2023-48362 }

CVE-2023-48362 [\[CVE json\]](./CVE-2023-48362.cve.json) [\[OSV json\]](./CVE-2023-48362.osv.json)



_Last updated: 2024-07-24T07:45:42.417Z_

### Affected

* Apache Drill from 1.19.0 before 1.21.2


### Description

XXE in the XML Format Plugin in Apache Drill version 1.19.0 and greater allows a user to read any file on a remote file system or execute commands via a malicious XML file.<br>Users are recommended to upgrade to version 1.21.2, which fixes this issue.

### References
* https://lists.apache.org/thread/9tt0q4bdjwgw0dz0l9knqxjnpb5y6zsl


### Credits
* Yuzhe Huang (finder)
