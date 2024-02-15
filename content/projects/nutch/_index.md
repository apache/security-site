---
title: Apache Nutch security advisories
description: Security information for Apache Nutch
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Nutch? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## An XML external entity (XXE) injection vulnerability exists in the Nutch DmozParser ## { #CVE-2021-23901 }

CVE-2021-23901 [\[CVE json\]](./CVE-2021-23901.cve.json)

_Last updated: 2021-01-25T09:22:41.311Z_

### Affected

* Apache Nutch from Apache Nutch through 1.17


### Description

An XML external entity (XXE) injection vulnerability was discovered in the Nutch DmozParser and is known to affect Nutch versions < 1.18. XML external entity injection (also known as XXE) is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data. It often allows an attacker to view files on the application server filesystem, and to interact with any back-end or external systems that the application itself can access.  This issue is fixed in Apache Nutch 1.18.

### References
* https://lists.apache.org/thread.html/r090321840b44cc91086c4e317bf2baffa270749dde6c1273b6567f7c%40%3Cdev.nutch.apache.org%3E
* https://issues.apache.org/jira/browse/NUTCH-2841


### Credits
* The Apache Nutch Project Management Committee would like to thank Martin Heyden for reporting this issue.
