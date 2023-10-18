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

### Affected

* Apache Doris(Incubating) at 0.15.0


### Description

Apache Doris, prior to 1.0.0, used a hardcoded key and IV to initialize the cipher used for ldap password, which may lead to information disclosure.

### References
* https://lists.apache.org/thread/com2dyzp3bn2rdrotry90q2zzord4tvt


### Credits
* We would like to thanks to Dwi Siswanto<me@dw1.io> for the report of this issue
