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

CVE-2023-47248 [\[CVE json\]](./CVE-2023-47248.cve.json) [\[OSV json\]](./CVE-2023-47248.osv.json)



_Last updated: 2023-11-10T14:10:15.590Z_

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


## AWS WebIdentityToken exposure in log files ## { #CVE-2024-41178 }

CVE-2024-41178 [\[CVE json\]](./CVE-2024-41178.cve.json) [\[OSV json\]](./CVE-2024-41178.osv.json)



_Last updated: 2024-07-23T17:07:57.878Z_

### Affected

* Apache Arrow Rust Object Store from 0.5.0 through 0.10.1


### Description

Exposure of temporary credentials in logs&nbsp;in Apache Arrow Rust Object Store (`object_store` crate), version 0.10.1 and earlier on all platforms using AWS WebIdentityTokens.&nbsp;<br><br>On certain error conditions, the logs may contain the OIDC token passed to <a target="_blank" rel="nofollow" href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html">AssumeRoleWithWebIdentity</a>. This allows someone with access to the logs to impersonate that identity, including performing their own calls to AssumeRoleWithWebIdentity, until the OIDC token expires. Typically OIDC tokens are valid for up to an hour, although this will vary depending on the issuer.<br><br>Users are recommended to use a different AWS authentication mechanism, disable logging or upgrade to version 0.10.2, which fixes this issue.<br><br>Details:<br><span style="background-color: var(--wht);"><br>When using AWS WebIdentityTokens with the object_store crate, in the event of a failure and automatic retry, </span><span style="background-color: var(--wht);">the underlying reqwest error, including the full URL with the credentials, potentially in the parameters, is written to the logs.&nbsp;<br></span><br>Thanks to <span style="background-color: rgb(255, 255, 255);">Paul&nbsp;</span>Hatcherian for reporting this vulnerability

### References
* https://lists.apache.org/thread/3t0povdppnt2czv6crlsqhvyko93kcrg


### Credits
* Paul Hatcherian (finder)


## Arbitrary code execution when loading a malicious data file ## { #CVE-2024-52338 }

CVE-2024-52338 [\[CVE json\]](./CVE-2024-52338.cve.json) [\[OSV json\]](./CVE-2024-52338.osv.json)



_Last updated: 2024-11-28T16:31:53.209Z_

### Affected

* Apache Arrow R package from 4.0.0 through 16.1.0


### Description

<p>Deserialization of untrusted data in IPC and Parquet readers in the Apache Arrow R package versions&nbsp;4.0.0 through 16.1.0 allows arbitrary code execution. An application is vulnerable if it 
reads Arrow IPC, Feather or Parquet data from untrusted sources (for 
example, user-supplied input files). This vulnerability only affects the arrow R package, not other Apache Arrow 
implementations or bindings unless those bindings are specifically used via the R package (for example, an R application that embeds a Python interpreter and uses PyArrow to read files from untrusted sources is still vulnerable if the arrow R package is an affected version). It is recommended that users of the arrow R package upgrade to 17.0.0 or later. Similarly, it
 is recommended that downstream libraries upgrade their dependency 
requirements to arrow 17.0.0 or later. If using an affected
version of the package, untrusted data can read into a Table and its internal to_data_frame() method can be used as a workaround (e.g., read_parquet(..., as_data_frame = FALSE)$to_data_frame()).<br></p><p>This issue affects the Apache Arrow R package: from 4.0.0 through 16.1.0.<br></p><p>Users are recommended to upgrade to version 17.0.0, which fixes the issue.</p>

### References
* https://github.com/apache/arrow/commit/801de2fbcf5bcbce0c019ed4b35ff3fc863b141b
* https://lists.apache.org/thread/0rcbvj1gdp15lvm23zm601tjpq0k25vt
