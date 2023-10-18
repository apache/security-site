---
title: Apache Parquet security advisories
description: Security information for Apache Parquet
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Parquet? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Parquet-MR potential DoS in case of malicious Parquet file ## { #CVE-2021-41561 }

CVE-2021-41561 [\[CVE json\]](./CVE-2021-41561.cve.json)

### Affected

* Apache Parquet from 1.9.0 before Parquet-MR*


### Description

Improper Input Validation vulnerability in Parquet-MR of Apache Parquet allows an attacker to DoS by malicious Parquet files. This issue affects Apache Parquet-MR version 1.9.0 and later versions.

### References
* https://lists.apache.org/thread/1bjlscbqtfzl160hrm9lnpjpppp5z3zr


### Credits
* This issue was discovered by Sergey Temnikov of the Amazon S3 team.
