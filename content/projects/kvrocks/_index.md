---
title: Apache Kvrocks security advisories
description: Security information for Apache Kvrocks
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Kvrocks? You can read more about the projects' security policy on their [security page](https://github.com/apache/kvrocks/blob/unstable/THREAT_MODEL.md), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://github.com/apache/kvrocks/blob/unstable/THREAT_MODEL.md). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## RESTORE IntSet Integer Overflow Leads to Remote DoS ## { #CVE-2026-54226 }

CVE-2026-54226 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-54226) [\[CVE json\]](./CVE-2026-54226.cve.json) [\[OSV json\]](./CVE-2026-54226.osv.json)



_Last updated: 2026-06-25T07:59:22.966Z_

### Affected

* Apache Kvrocks from 2.6.0 through 2.15.0


### Description

<p>A vulnerability in Apache Kvrocks.</p><p>This issue affects Apache Kvrocks: from 2.6.0 through 2.15.0.</p><p>Users are recommended to upgrade to version 2.16.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/pnglz29zh804rd3257fbh56cqgy1q65g


### Credits
* 朱少扬 (reporter)


## Stack buffer overflow in Lua bit.tohex() ## { #CVE-2026-46752 }

CVE-2026-46752 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46752) [\[CVE json\]](./CVE-2026-46752.cve.json) [\[OSV json\]](./CVE-2026-46752.osv.json)



_Last updated: 2026-06-25T08:00:16.837Z_

### Affected

* Apache Kvrocks from 2.0.4 through 2.15.0


### Description

<p>Redis Lua HEAP overflow in cjson library vulnerability in Apache Kvrocks.</p><p>This issue affects Apache Kvrocks: from 2.0.4 through 2.15.0.</p><p>Users are recommended to upgrade to version 2.16.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/11sr3bkkhkk0q01odgw6ddsj7fzo31pt


### Credits
* Jincheng Yang (reporter)


## Does not remove the unsafe loadstring function from its Lua sandbox, allowing a user who can run EVAL scripts to load crafted, unvalidated bytecode that crashes the server process, resulting in a remote denial of service. ## { #CVE-2026-46751 }

CVE-2026-46751 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46751) [\[CVE json\]](./CVE-2026-46751.cve.json) [\[OSV json\]](./CVE-2026-46751.osv.json)



_Last updated: 2026-06-25T08:00:59.029Z_

### Affected

* Apache Kvrocks from 2.2.0 through 2.15.0


### Description

<p>A vulnerability in Apache Kvrocks.</p><p>This issue affects Apache Kvrocks: from 2.2.0 through 2.15.0.</p><p>Users are recommended to upgrade to version 2.16.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/cjjk4gq1nkb7pooqc37gz0blvdkqgv5z


### Credits
* 4ra2n (A code security AI agent) (finder)


## Replication Fullsync Path Traversal via Unvalidated Filename Handling ## { #CVE-2026-45188 }

CVE-2026-45188 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45188) [\[CVE json\]](./CVE-2026-45188.cve.json) [\[OSV json\]](./CVE-2026-45188.osv.json)



_Last updated: 2026-06-25T08:01:48.602Z_

### Affected

* Apache Kvrocks from 1.0.0 through 2.15.0


### Description

<p>Relative Path Traversal vulnerability in Apache Kvrocks.</p><p>This issue affects Apache Kvrocks: from 1.0.0 through 2.15.0.</p><p>Users are recommended to upgrade to version 2.16.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/hxw1zxmpm12x6dltpyr9fpmnbz632jft


### Credits
* @Brubbish of VARAS@IIE (reporter)


## Improper permission for the APPLYBATCH command ## { #CVE-2026-41566 }

CVE-2026-41566 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41566) [\[CVE json\]](./CVE-2026-41566.cve.json) [\[OSV json\]](./CVE-2026-41566.osv.json)



_Last updated: 2026-06-25T08:04:24.570Z_

### Affected

* Apache Kvrocks from 2.8.0 through 2.15.0


### Description

<p>Improper Handling of Insufficient Permissions or Privileges vulnerability in Apache Kvrocks.</p><p>This issue affects Apache Kvrocks: 2.8.0.</p><p>Users are recommended to upgrade to version 2.16.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zng5lp7psgkcv9jnm9tztdlm3rmzfydl


### Credits
* Qing Xu (reporter)


## MONITOR command reveals plaintext credentials to non-admins ## { #CVE-2025-59792 }

CVE-2025-59792 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-59792) [\[CVE json\]](./CVE-2025-59792.cve.json) [\[OSV json\]](./CVE-2025-59792.osv.json)



_Last updated: 2025-11-28T14:21:21.082Z_

### Affected

* Apache Kvrocks from 1.0.0 through 2.13.0


### Description

<p>Reveals plaintext credentials in the MONITOR command vulnerability in Apache Kvrocks.</p><p>This issue affects Apache Kvrocks: from 1.0.0 through 2.13.0.</p><p>Users are recommended to upgrade to version 2.14.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/h2pcvr5p9otc7dnj2dt2nr4b3omghddw


### Credits
* Mapta / BugBunny_ai (reporter)


## RESET command grants admin privileges ## { #CVE-2025-59790 }

CVE-2025-59790 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-59790) [\[CVE json\]](./CVE-2025-59790.cve.json) [\[OSV json\]](./CVE-2025-59790.osv.json)



_Last updated: 2025-11-28T14:20:28.481Z_

### Affected

* Apache Kvrocks from 2.9.0 through 2.13.0


### Description

<p>Improper Privilege Management vulnerability in Apache Kvrocks.</p><p>This issue affects Apache Kvrocks: from v2.9.0 through v2.13.0.</p><p>Users are recommended to upgrade to version 2.14.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/dlbz5hmm4ts3npzqnvhofxmqg9w9zt0o


### Credits
* Mapta / BugBunny_ai (reporter)


## The server was crashed by the negative offset ## { #CVE-2025-26413 }

CVE-2025-26413 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-26413) [\[CVE json\]](./CVE-2025-26413.cve.json) [\[OSV json\]](./CVE-2025-26413.osv.json)



_Last updated: 2025-04-22T10:35:30.358Z_

### Affected

* Apache Kvrocks through 2.11.1


### Description

<p>Improper Input Validation vulnerability in Apache Kvrocks.</p>The SETRANGE command didn't check if the `offset` input is a positive integer and use it as an index<br>of a string. So it will cause the server to crash due to its index is&nbsp; out of range.<br><p>This issue affects Apache Kvrocks: through 2.11.1.</p><p>Users are recommended to upgrade to version 2.12.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/388743qrr8yq8qm0go8tls6rf1kog8dw


### Credits
* ankki-zsyang, Shenzhen Ankki Technologies Co., Ltd. (reporter)


## Cross-Protocol Scripting Vulnerability ## { #CVE-2025-25069 }

CVE-2025-25069 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-25069) [\[CVE json\]](./CVE-2025-25069.cve.json) [\[OSV json\]](./CVE-2025-25069.osv.json)



_Last updated: 2025-02-07T12:46:01.975Z_

### Affected

* Apache Kvrocks through 2.11.0


### Description

<p>A Cross-Protocol Scripting vulnerability is found in Apache Kvrocks.</p>Since Kvrocks didn't detect if "Host:" or "POST" appears in RESP requests,<br>a valid HTTP request can also be sent to Kvrocks as a valid RESP request <br>and trigger some database operations, which can be<span style="background-color: rgb(255, 255, 255);">&nbsp;dangerous when <br>it is chained with SSRF.<br><br></span>It is similiar to&nbsp;CVE-2016-10517 in Redis.<br><br><p>This issue affects Apache Kvrocks: from the initial version to the latest version 2.11.0.</p><p>Users are recommended to upgrade to version 2.11.1, which fixes the issue.</p>

### References
* https://www.cve.org/CVERecord?id=CVE-2016-10517
* https://lists.apache.org/thread/gbxv9gpsskmdzg6z48zm3tvo8cyo9v3t


### Credits
* Sergey Volosatov (reporter)
