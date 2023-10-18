---
title: Apache Airavata security advisories
description: Security information for Apache Airavata
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Airavata? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## airavata-django-portal allows CRLF log injection because of the lack of escaping in the log statements ## { #CVE-2021-43410 }

CVE-2021-43410 [\[CVE json\]](./CVE-2021-43410.cve.json)

### Affected

* Apache Airavata Django Portal from master branch before commit 3c5d8c7


### Description

Apache Airavata Django Portal allows CRLF log injection because of lack of escaping log statements. In particular, some HTTP request parameters are logged without first being escaped.

Versions affected:
master branch before commit 3c5d8c7 [1] of airavata-django-portal

[1] https://github.com/apache/airavata-django-portal/commit/3c5d8c72bfc3eb0af8693a655a5d60f9273f8170

### References
* https://lists.apache.org/thread/q64h16ofdxk29soz3jj561nysnzcrl31


### Credits
* Apache Airavata would like to thank haby0 of Duxiaoman Financial Security Team for reporting this vulnerability.
