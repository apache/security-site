---
title: Apache Hama security advisories
description: Security information for Apache Hama
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Hama? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Hama allows XSS and information disclosure ## { #CVE-2022-45470 }

CVE-2022-45470 [\[CVE json\]](./CVE-2022-45470.cve.json)

### Affected

* Apache Hama from 1.7.1 before Apache Hama*


### Description

missing input validation in Apache Hama may cause information disclosure through path traversal and XSS. Since Apache Hama is EOL, we do not expect these issues to be fixed

### References
* https://lists.apache.org/thread/ztvoshd4kxvp5vlro52mpgpfxct4ft8l


### Credits
* Apache would like to thank QSec-Team for reporting this issue
