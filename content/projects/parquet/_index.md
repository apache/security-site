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

## Potential malicious code execution from trusted packages in the parquet-avro module when reading an Avro schema from a Parquet file metadata ## { #CVE-2025-46762 }

CVE-2025-46762 [\[CVE json\]](./CVE-2025-46762.cve.json) [\[OSV json\]](./CVE-2025-46762.osv.json)



_Last updated: 2025-05-06T09:08:12.043Z_

### Affected

* Apache Parquet Java through 1.15.1


### Description

<p><span style="background-color: rgb(252, 252, 252);">Schema parsing in the parquet-avro module of Apache Parquet 1.15.0 and previous versions allows bad actors to execute arbitrary code.</span></p><p><span style="background-color: rgb(252, 252, 252);">While 1.15.1 introduced a fix to restrict untrusted packages, the default setting of trusted packages still allows malicious classes from these packages to be executed.</span></p><p><span style="background-color: rgb(252, 252, 252);"><span style="background-color: rgb(255, 255, 255);">The exploit is only applicable if the client code of parquet-avro uses the "specific" or the "reflect" models deliberately for reading Parquet files. ("generic" model is not impacted)</span><br></span><br>Users are recommended to <span style="background-color: rgb(255, 255, 255);">upgrade to 1.15.2 or set the system property "org.apache.parquet.avro.</span><span style="background-color: rgb(255, 255, 255);">SERIALIZABLE_PACKAGES" to an empty string on 1.15.1. Both are sufficient to fix the issue.</span><br></p>

### References
* https://lists.apache.org/thread/t7724lpvl110xsbgqwsmrdsns0rhycdp


### Credits
* Andrew Pikler (reporter)
* David Handermann (reporter)
* Nándor Kollár (reporter)


## Arbitrary code execution in the parquet-avro module when reading an Avro schema from a Parquet file metadata ## { #CVE-2025-30065 }

CVE-2025-30065 [\[CVE json\]](./CVE-2025-30065.cve.json) [\[OSV json\]](./CVE-2025-30065.osv.json)



_Last updated: 2025-07-11T10:32:31.431Z_

### Affected

* Apache Parquet Java through 1.15.0


### Description

<p><span style="background-color: rgb(252, 252, 252);">Schema parsing in the parquet-avro module of Apache Parquet 1.15.0 and previous versions allows bad actors to execute arbitrary code</span><br></p><p>Users are recommended to upgrade to version 1.15.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/okzqb3kn479gqzxm21gg5vqr35om9gw5


### Credits
* Keyi Li (Amazon) (finder)


## Apache Parquet-MR potential DoS in case of malicious Parquet file ## { #CVE-2021-41561 }

CVE-2021-41561 [\[CVE json\]](./CVE-2021-41561.cve.json) [\[OSV json\]](./CVE-2021-41561.osv.json)



_Last updated: 2021-12-20T11:09:26.601Z_

### Affected

* Apache Parquet from 1.9.0 before Parquet-MR*


### Description

Improper Input Validation vulnerability in Parquet-MR of Apache Parquet allows an attacker to DoS by malicious Parquet files. This issue affects Apache Parquet-MR version 1.9.0 and later versions.

### References
* https://lists.apache.org/thread/1bjlscbqtfzl160hrm9lnpjpppp5z3zr


### Credits
* This issue was discovered by Sergey Temnikov of the Amazon S3 team.
