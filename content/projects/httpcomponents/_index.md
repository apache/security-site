---
title: Apache HttpComponents security advisories
description: Security information for Apache HttpComponents
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache HttpComponents? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=%5BFINDING%5D%20Apache%20HttpComponents).

You can read more about the security policy on:

- [Apache HttpComponents security model](https://hc.apache.org/security.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## HPackDecoder Unlimited Header List Size Before SETTINGS ACK ## { #CVE-2026-54428 }

CVE-2026-54428 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-54428) [\[CVE json\]](./CVE-2026-54428.cve.json) [\[OSV json\]](./CVE-2026-54428.osv.json)



_Last updated: 2026-07-01T17:05:28.114Z_

### Affected

* Apache HttpComponents Core from 5.5-alpha through 5.5-beta1
* Apache HttpComponents Core from 5.0-alpha through 5.4.2


### Description

Allocation of resources without limits or throttling in the HTTP/2 HPACK decoder in Apache HttpComponents Core (5.4.2 and earlier, 5.5-beta1 and earlier) allows an remote attacker to cause a denial of service through memory exhaustion by sending oversized compressed header blocks before the HTTP/2 SETTINGS acknowledgement causes the configured header list size limit to be applied.<br><br>

### References
* https://lists.apache.org/thread/5zjp8vczvxq19pw2rvhs21q446bhl0sd


### Credits
* Henry Huang <zhuang3@paypal.com> (finder)


## Unbounded HTTP Header/Line Length in Default Configuration ## { #CVE-2026-54399 }

CVE-2026-54399 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-54399) [\[CVE json\]](./CVE-2026-54399.cve.json) [\[OSV json\]](./CVE-2026-54399.osv.json)



_Last updated: 2026-07-01T17:05:54.930Z_

### Affected

* Apache HttpComponents Core from 5.5-alpha through 5.5-beta1
* Apache HttpComponents Core from 5.0-alpha through 5.4.2


### Description

<p>Uncontrolled Resource Consumption vulnerability in the HTTP/1.1 message parser&nbsp;in Apache HttpComponents Core (5.4.2 and earlier, 5.5-beta1 and earlier) allows&nbsp;an remote attacker to cause a denial of service through memory exhaustion by sending messages with excessive number of headers / excessive header length</p><p></p>

### References
* https://lists.apache.org/thread/zmxh1pl2zohov5ntdh4lt85gfrlchgpy


### Credits
* Henry Huang <zhuang3@paypal.com> (finder)


## SCRAM-SHA-256 mutual authentication bypass may cause the client to accept authentication without proper mutual authentication verification ## { #CVE-2026-40542 }

CVE-2026-40542 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40542) [\[CVE json\]](./CVE-2026-40542.cve.json) [\[OSV json\]](./CVE-2026-40542.osv.json)



_Last updated: 2026-04-22T07:07:19.055Z_

### Affected

* Apache HttpClient from 5.6 before 5.6.1


### Description

<code>Missing critical step in authentication in Apache HttpClient 5.6 allows an attacker to cause the client to accept SCRAM-SHA-256 authentication without proper mutual authentication verification. Users are recommended to upgrade to version 5.6.1, which fixes this issue.</code><br>

### References
* https://lists.apache.org/thread/tfmgv86xr0z1y096vs3z0y315t1v3o97


### Credits
* Rasmus Moorats (finder)


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
