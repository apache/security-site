---
title: Apache HttpComponents security advisories
description: Security information for Apache HttpComponents
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache HttpComponents? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## PSL (Public Suffix List) validation bypass ## { #CVE-2025-27820 }

CVE-2025-27820 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27820) [\[CVE json\]](./CVE-2025-27820.cve.json) [\[OSV json\]](./CVE-2025-27820.osv.json)



_Last updated: 2025-06-04T11:19:13.066Z_

### Affected

* Apache HttpComponents from 5.4.0 before 5.4.3


### Description

<code>A bug in PSL validation logic in Apache HttpClient 5.4.x disables domain checks, affecting cookie management and host name verification. Discovered by the Apache HttpClient team. Fixed in the 5.4.3 release<br></code>

### References
* https://github.com/apache/httpcomponents-client/pull/574
* https://github.com/apache/httpcomponents-client/pull/621
* https://hc.apache.org/httpcomponents-client-5.4.x/index.html
* https://lists.apache.org/thread/55xhs40ncqv97qvoocok44995xp5kqn8


### Credits
* Joe Gallo (remediation developer)
