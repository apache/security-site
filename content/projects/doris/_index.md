---
title: Apache Doris security advisories
description: Security information for Apache Doris
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Doris? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Doris hardcoded cryptography initialization ## { #CVE-2022-23942 }

CVE-2022-23942 [\[CVE json\]](./CVE-2022-23942.cve.json)

_Last updated: 2022-04-26T14:49:46.143Z_

### Affected

* Apache Doris(Incubating) at 0.15.0


### Description

Apache Doris, prior to 1.0.0, used a hardcoded key and IV to initialize the cipher used for ldap password, which may lead to information disclosure.

### References
* https://lists.apache.org/thread/com2dyzp3bn2rdrotry90q2zzord4tvt


### Credits
* We would like to thanks to Dwi Siswanto<me@dw1.io> for the report of this issue


## Missing API authentication allowed DoS ## { #CVE-2023-41314 }

CVE-2023-41314 [\[CVE json\]](./CVE-2023-41314.cve.json)

_Last updated: 2023-12-18T08:27:49.193Z_

### Affected

* Apache Doris from 1.2.0 through 2.0.3


### Description

The api /api/snapshot and /api/get_log_file would allow unauthenticated access.<br>It could allow a&nbsp;DoS attack or get arbitrary files from FE node.<br>Please&nbsp;upgrade to 2.0.3 to fix these issues.

### References
* https://lists.apache.org/thread/tgvpvz3yw7zgodl1sb3sv3jbbz8t5zb4
