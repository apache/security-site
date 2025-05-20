---
title: Apache Kvrocks security advisories
description: Security information for Apache Kvrocks
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Kvrocks? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Cross-Protocol Scripting Vulnerability ## { #CVE-2025-25069 }

CVE-2025-25069 [\[CVE json\]](./CVE-2025-25069.cve.json) [\[OSV json\]](./CVE-2025-25069.osv.json)



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


## The server was crashed by the negative offset ## { #CVE-2025-26413 }

CVE-2025-26413 [\[CVE json\]](./CVE-2025-26413.cve.json) [\[OSV json\]](./CVE-2025-26413.osv.json)



_Last updated: 2025-04-22T10:35:30.358Z_

### Affected

* Apache Kvrocks through 2.11.1


### Description

<p>Improper Input Validation vulnerability in Apache Kvrocks.</p>The SETRANGE command didn't check if the `offset` input is a positive integer and use it as an index<br>of a string. So it will cause the server to crash due to its index is&nbsp; out of range.<br><p>This issue affects Apache Kvrocks: through 2.11.1.</p><p>Users are recommended to upgrade to version 2.12.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/388743qrr8yq8qm0go8tls6rf1kog8dw


### Credits
* ankki-zsyang, Shenzhen Ankki Technologies Co., Ltd. (reporter)
