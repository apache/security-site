---
title: Apache Nutch security advisories
description: Security information for Apache Nutch
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Nutch? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Nutch).

You can read more about the security policy on:

- [Apache Nutch security model](https://github.com/apache/nutch/blob/master/THREAT_MODEL.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unauthenticated reflection-based job execution in Nutch Server (Nutch REST API) ## { #CVE-2026-41871 }

CVE-2026-41871 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41871) [\[CVE json\]](./CVE-2026-41871.cve.json) [\[OSV json\]](./CVE-2026-41871.osv.json)



_Last updated: 2026-09-09T10:45:42.132Z_

### Affected

* Apache Nutch from 1.10 through 1.22


### Description

<p>Missing Authorization, Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection') vulnerability&nbsp;in Apache Nutch Server  (Nutch REST API).</p><p>This issue affects Apache Nutch: from 1.10 through 1.22.</p><p>Users are recommended to upgrade to version 1.23, which removes the Nutch Server.<br>If an upgrade is not possible, user must restrict access to instances running the Nutch Service to trusted users only.<br>Please, also visit the <a target="_blank" rel="nofollow" href="https://nutch.apache.org/documentation/security/">Apache Nutch security advisories</a>.<br></p>

### References
* https://lists.apache.org/thread/rbr63fx8vlrhzrfknq2l0mg0d0blsl54


### Credits
* The Apache Nutch Project Management Committee would like to thank Th1nk for reporting this issue. (finder)


## Unauthenticated remote code execution (RCE) via JEXL injection in Nutch Server (Nutch REST API) ## { #CVE-2026-41870 }

CVE-2026-41870 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41870) [\[CVE json\]](./CVE-2026-41870.cve.json) [\[OSV json\]](./CVE-2026-41870.osv.json)



_Last updated: 2026-09-09T10:42:40.050Z_

### Affected

* Apache Nutch from 1.11 through 1.22


### Description

<p>Missing Authorization, Improper Control of Generation of Code ('Code Injection'), Improper Control of Dynamically-Managed Code Resources, Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection') vulnerability&nbsp;in Apache Nutch Server  (Nutch REST API).</p><p>This issue affects Apache Nutch: from 1.11 through 1.22.</p><p>Users are recommended to upgrade to version 1.23, which removes the Nutch Server.<br>If an upgrade is not possible, user must restrict access to instances running the Nutch Service to trusted users only.<br>Please, also visit the <a target="_blank" rel="nofollow" href="https://nutch.apache.org/documentation/security/">Apache Nutch security advisories</a>.</p>

### References
* https://lists.apache.org/thread/3pl59g0jzqx1bdh5w92qoftzn7c3x8j2


### Credits
* The Apache Nutch Project Management Committee would like to thank Th1nk for reporting this issue. (reporter)


## Unauthenticated forced shutdown and job interruption in Nutch Server (Nutch REST API) ## { #CVE-2026-41869 }

CVE-2026-41869 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41869) [\[CVE json\]](./CVE-2026-41869.cve.json) [\[OSV json\]](./CVE-2026-41869.osv.json)



_Last updated: 2026-09-09T10:44:25.733Z_

### Affected

* Apache Nutch from 1.10 through 1.22


### Description

<p>Missing Authorization, Improper Resource Shutdown and Job Interruption vulnerability in Apache Nutch Server  (Nutch REST API).</p><p>This issue affects Apache Nutch: from 1.10 through 1.22.</p><p>Users are recommended to upgrade to version 1.23, which removes the Nutch Server.<br>If an upgrade is not possible, user must restrict access to instances running the Nutch Service to trusted users only.<br>Please, also visit the <a target="_blank" rel="nofollow" href="https://nutch.apache.org/documentation/security/">Apache Nutch security advisories</a>.</p>

### References
* https://lists.apache.org/thread/ps4yhlvo6kdgmksdgb9lv1h4p0oy5fdj


### Credits
* The Apache Nutch Project Management Committee would like to thank Th1nk for reporting this issue. (reporter)


## An XML external entity (XXE) injection vulnerability exists in the Nutch DmozParser ## { #CVE-2021-23901 }

CVE-2021-23901 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-23901) [\[CVE json\]](./CVE-2021-23901.cve.json) [\[OSV json\]](./CVE-2021-23901.osv.json)



_Last updated: 2021-01-25T09:22:41.311Z_

### Affected

* Apache Nutch from Apache Nutch through 1.17


### Description

An XML external entity (XXE) injection vulnerability was discovered in the Nutch DmozParser and is known to affect Nutch versions < 1.18. XML external entity injection (also known as XXE) is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data. It often allows an attacker to view files on the application server filesystem, and to interact with any back-end or external systems that the application itself can access.  This issue is fixed in Apache Nutch 1.18.

### References
* https://lists.apache.org/thread.html/r090321840b44cc91086c4e317bf2baffa270749dde6c1273b6567f7c%40%3Cdev.nutch.apache.org%3E
* https://issues.apache.org/jira/browse/NUTCH-2841


### Credits
* The Apache Nutch Project Management Committee would like to thank Martin Heyden for reporting this issue.
