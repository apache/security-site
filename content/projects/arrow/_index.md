---
title: Apache Arrow security advisories
description: Security information for Apache Arrow
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Arrow? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Arbitrary code execution when loading a malicious data file ## { #CVE-2023-47248 }

CVE-2023-47248 [\[CVE json\]](./CVE-2023-47248.cve.json)

### Affected

* PyArrow from 0.14.0 through 14.0.0
* PyArrow from 0.14.0 through 14.0.0


### Description

<div>Deserialization of untrusted data in IPC and Parquet readers in PyArrow versions 0.14.0 to 14.0.0 allows arbitrary code execution. An application is vulnerable if it reads Arrow IPC, Feather or Parquet data from untrusted sources (for example user-supplied input files).</div><div><br></div><div>This vulnerability only affects PyArrow, not other Apache Arrow implementations or bindings.<br></div><div><br></div><div>It is recommended that users of PyArrow upgrade to 14.0.1. Similarly, it is recommended that downstream libraries upgrade their dependency requirements to PyArrow 14.0.1 or later. PyPI packages are already available, and we hope that conda-forge packages will be available soon.<br></div><div><br></div><div>If it is not possible to upgrade, we provide a separate package `pyarrow-hotfix` that disables the vulnerability on older PyArrow versions. See <a target="_blank" rel="nofollow" href="https://pypi.org/project/pyarrow-hotfix/">https://pypi.org/project/pyarrow-hotfix/</a> for instructions.<br></div><div><br></div>

### References
* https://lists.apache.org/thread/yhy7tdfjf9hrl9vfrtzo8p2cyjq87v7n
* https://github.com/apache/arrow/commit/f14170976372436ec1d03a724d8d3f3925484ecf
* https://pypi.org/project/pyarrow-hotfix/


### Credits
* Li Jiakun - laoquanshi (finder)
