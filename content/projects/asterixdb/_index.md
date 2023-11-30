---
title: Apache AsterixDB security advisories
description: Security information for Apache AsterixDB
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache AsterixDB? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## unzip directory traversal ## { #CVE-2020-9479 }

CVE-2020-9479 [\[CVE json\]](./CVE-2020-9479.cve.json)

### Affected

* Apache AsterixDB at git


### Description

When loading a UDF, a specially crafted zip file could allow files to be placed outside of the UDF deployment directory. This issue affected Apache AsterixDB unreleased builds between commits 580b81aa5e8888b8e1b0620521a1c9680e54df73 and 28c0ee84f1387ab5d0659e9e822f4e3923ddc22d.

Note: this CVE may be REJECTed as the issue did not affect any released versions of Apache AsterixDB

### References
* https://www.openwall.com/lists/oss-security/2020/08/08/2


### Credits
* This issue was discovered by Yiming Xiang of NSFOCUS
