---
title: Apache Avro security advisories
description: Security information for Apache Avro
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Avro? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Code injection on Java generated code ## { #CVE-2025-33042 }

CVE-2025-33042 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-33042) [\[CVE json\]](./CVE-2025-33042.cve.json) [\[OSV json\]](./CVE-2025-33042.osv.json)



_Last updated: 2026-02-13T11:47:01.866Z_

### Affected

* Apache Avro Java SDK through 1.11.4
* Apache Avro Java SDK at 1.12.0


### Description

<p>Improper Control of Generation of Code ('Code Injection') vulnerability in Apache Avro Java SDK when generating specific records from untrusted Avro schemas.</p><p>This issue affects Apache Avro Java SDK: all versions through 1.11.4 and version&nbsp;1.12.0.</p><p>Users are recommended to upgrade to version 1.12.1 or 1.11.5, which fix the issue.</p>

### References
* https://lists.apache.org/thread/fy88wmgf1lj9479vrpt12cv8x73lroj1


### Credits
* Brant Eckert (finder)


## Arbitrary Code Execution when reading Avro schema (Java SDK) ## { #CVE-2024-47561 }

CVE-2024-47561 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-47561) [\[CVE json\]](./CVE-2024-47561.cve.json) [\[OSV json\]](./CVE-2024-47561.osv.json)



_Last updated: 2024-10-21T08:50:48.382Z_

### Affected

* Apache Avro Java SDK before 1.11.4


### Description

Schema parsing in the Java SDK of Apache Avro 1.11.3 and previous versions allows bad actors to execute arbitrary code.<br>Users are recommended to upgrade to version 1.11.4&nbsp; or 1.12.0, which fix this issue.

### References
* https://lists.apache.org/thread/c2v7mhqnmq0jmbwxqq3r5jbj1xg43h5x


### Credits
* Kostya Kortchinsky, from the Databricks Security Team (finder)


## Memory when deserializing untrusted data in Avro Java SDK ## { #CVE-2023-39410 }

CVE-2023-39410 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-39410) [\[CVE json\]](./CVE-2023-39410.cve.json)

_Last updated: 2025-02-06T14:33:53.747Z_

### Affected

* Apache Avro Java SDK before 1.11.3


### Description

<div>When deserializing untrusted or corrupted data, it is possible for a reader to consume memory beyond the allowed constraints and thus lead to out of memory on the system.</div><div><br></div><div>This issue affects Java applications using Apache Avro Java SDK up to and including 1.11.2.  Users should update to apache-avro version 1.11.3 which addresses this issue.</div><div><br></div>

### References
* https://lists.apache.org/thread/q142wj99cwdd0jo5lvdoxzoymlqyjdds
* https://www.openwall.com/lists/oss-security/2023/09/29/6


### Credits
* Adam Korczynski at ADA Logics Ltd (finder)


## Integer overflow when reading corrupted .avro file in Avro Rust SDK ## { #CVE-2022-36125 }

CVE-2022-36125 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-36125) [\[CVE json\]](./CVE-2022-36125.cve.json) [\[OSV json\]](./CVE-2022-36125.osv.json)



_Last updated: 2022-08-09T06:44:50.447Z_

### Affected

* Apache Avro from unspecified before 0.14.0


### Description

It is possible to crash (panic) an application by providing a corrupted data to be read. This issue affects Rust applications using Apache Avro Rust SDK prior to 0.14.0 (previously known as avro-rs).  Users should update to apache-avro version 0.14.0 which addresses this issue.

### References
* https://lists.apache.org/thread/t1r5xz0pvhm4tosqopjpj6dz8zlsht07


### Credits
* This issue was reported to the Apache Avro team by Evan Richter at ForAllSecure and found with Mayhem.


## Memory overconsumption in Avro Rust SDK ## { #CVE-2022-36124 }

CVE-2022-36124 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-36124) [\[CVE json\]](./CVE-2022-36124.cve.json) [\[OSV json\]](./CVE-2022-36124.osv.json)



_Last updated: 2022-08-09T06:46:06.388Z_

### Affected

* Apache Avro from unspecified before 0.14.0


### Description

It is possible for a Reader to consume memory beyond the allowed constraints and thus lead to out of memory on the system. This issue affects Rust applications using Apache Avro Rust SDK prior to 0.14.0 (previously known as avro-rs).  Users should update to apache-avro version 0.14.0 which addresses this issue.

### References
* https://lists.apache.org/thread/kj429rzo1xxjgz058qqqg0y7c0p512zo


### Credits
* This issue was reported to the Apache Avro team by Evan Richter at ForAllSecure and found with Mayhem.


## Denial of service while reading data in Avro Rust SDK ## { #CVE-2022-35724 }

CVE-2022-35724 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-35724) [\[CVE json\]](./CVE-2022-35724.cve.json) [\[OSV json\]](./CVE-2022-35724.osv.json)



_Last updated: 2022-08-09T06:43:41.354Z_

### Affected

* Apache Avro from unspecified before 0.14.0


### Description

It is possible to provide data to be read that leads the reader to loop in cycles endlessly, consuming CPU.  This issue affects Rust applications using Apache Avro Rust SDK prior to 0.14.0 (previously known as avro-rs).  Users should update to apache-avro version 0.14.0 which addresses this issue.

### References
* https://lists.apache.org/thread/771z1nwrpkn1ovmyfb2fm65mchdxgy7p


### Credits
* This issue was reported to the Apache Avro team by Evan Richter at ForAllSecure and found with Mayhem.


## Possible DOS vulnerabilities in C# Avro SDK ## { #CVE-2021-43045 }

CVE-2021-43045 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-43045) [\[CVE json\]](./CVE-2021-43045.cve.json) [\[OSV json\]](./CVE-2021-43045.osv.json)



_Last updated: 2022-01-06T17:58:30.429Z_

### Affected

* Apache Avro from Apache Avro through 1.10.2


### Description

A vulnerability in the .NET SDK of Apache Avro allows an attacker to allocate excessive resources, potentially causing a denial-of-service attack.  This issue affects .NET applications using Apache Avro version 1.10.2 and prior versions.  Users should update to version 1.11.0 which addresses this issue.

### References
* https://lists.apache.org/thread/5fttw9vk6gd2p3b846nox7hcj5469xfd


### Credits
* Apache Avro would like to thank Philip Sanetra for reporting this issue.
