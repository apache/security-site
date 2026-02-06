---
title: Apache Continuum security advisories
description: Security information for Apache Continuum
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Continuum? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Command injection leading to RCE ## { #CVE-2016-15057 }

CVE-2016-15057 [\[CVE json\]](./CVE-2016-15057.cve.json) [\[OSV json\]](./CVE-2016-15057.osv.json)



_Last updated: 2026-02-06T10:50:44.556Z_

### Affected

* Apache Continuum before *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Continuum.</p><p>This issue affects Apache Continuum: all versions.</p><p>Attackers with access to the installations REST API can use this to invoke arbitrary commands on the server.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/hbvf1ztqw2kv51khvzm5nk3mml3nm4z1
