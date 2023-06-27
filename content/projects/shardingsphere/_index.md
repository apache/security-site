---
title: Apache ShardingSphere security advisories
description: Security information for Apache ShardingSphere
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ShardingSphere? You can read more about the projects' security policy on their [security page](https://shardingsphere.apache.org/community/en/security/), and email your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://shardingsphere.apache.org/community/en/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## MySQL authentication bypass ## { #CVE-2022-45347 }

[CVE-2022-45347](./CVE-2022-45347.cve.json)

### Affected

* Apache ShardingSphere-Proxy before 5.3.0


### Description

Apache ShardingSphere-Proxy prior to 5.3.0 when using MySQL as database backend didn't cleanup the database session completely after client authentication failed, which allowed an attacker to execute normal commands by constructing a special MySQL client. This vulnerability has been fixed in Apache ShardingSphere 5.3.0.

### References
* https://lists.apache.org/thread/l5rz7j4rg10o7ywtgknh2f5hxnv6yw3l
