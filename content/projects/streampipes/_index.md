---
title: Apache StreamPipes security advisories
description: Security information for Apache StreamPipes
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache StreamPipes? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Privilege escalation through non-admin user ## { #CVE-2023-31469 }

[CVE-2023-31469](./CVE-2023-31469.cve.json)

### Affected

* Apache StreamPipes from 0.69.0 through 0.91.0


### Description



A REST interface in Apache StreamPipes (versions 0.69.0 to 0.91.0) <span style="background-color: rgb(255, 255, 255);">was not properly restricted to admin-only access. This </span>allowed a non-admin user with valid login credentials to elevate privileges beyond the initially assigned roles.<br>The issue is resolved by upgrading to StreamPipes 0.92.0.



### References
* https://lists.apache.org/thread/c4y8kf9bzpf36v4bottfmd8tc9cxo19m
