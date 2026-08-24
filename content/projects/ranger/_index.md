---
title: Apache Ranger security advisories
description: Security information for Apache Ranger
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Ranger? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Ranger).

You can read more about the security policy on:

- [Apache Ranger security model](https://github.com/apache/ranger/blob/master/THREAT_MODEL.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## UnixAuth lacks brute-force protection ## { #CVE-2026-65948 }

CVE-2026-65948 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-65948) [\[CVE json\]](./CVE-2026-65948.cve.json) [\[OSV json\]](./CVE-2026-65948.osv.json)



_Last updated: 2026-08-10T10:20:16.518Z_

### Affected

* Apache Ranger through 2.8.0


### Description

UnixAuth lacks brute-force protection in Apache Ranger versions &lt;= 2.8.0.&nbsp;<br>Note:&nbsp;&nbsp;UnixAuth is NOT a recommended option for production deployments.&nbsp;<br>Users are recommended to upgrade to version 2.9.0, which fixes this issue.

### References
* https://lists.apache.org/thread/cx53rbkxkn5hbvzv8ohwvndzrxhc06qf


### Credits
* Andrew Rukin (Arenadata) (finder)


## Logs contain replayable JWT bearer tokens ## { #CVE-2026-65945 }

CVE-2026-65945 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-65945) [\[CVE json\]](./CVE-2026-65945.cve.json) [\[OSV json\]](./CVE-2026-65945.osv.json)



_Last updated: 2026-08-10T10:20:39.245Z_

### Affected

* Apache Ranger through 2.8.0


### Description

Logs contain replayable JWT tokens in Apache Ranger versions &lt;= 2.8.0<br>Users are recommended to upgrade to version 2.9.0, which fixes this issue.

### References
* https://lists.apache.org/thread/ww4b3d59r3pnhosljcrq9b98qzqtnclk


### Credits
* Andrew Rukin (Arenadata) (finder)


## Clients accept TLS certificates issued for other hostnames ## { #CVE-2026-65942 }

CVE-2026-65942 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-65942) [\[CVE json\]](./CVE-2026-65942.cve.json) [\[OSV json\]](./CVE-2026-65942.osv.json)



_Last updated: 2026-08-10T10:21:03.965Z_

### Affected

* Apache Ranger through 2.8.0


### Description

<span style="background-color: rgb(255, 255, 255);">TLS hostname verification issue</span> in Apache Ranger Client Code in versions &lt;= 2.8.0.<br>Users are recommended to upgrade to version 2.9.0, which fixes this issue.

### References
* https://lists.apache.org/thread/pp6on4yyht3z8l0ktfo1xydhjzjbn4gt


### Credits
* Andrew Rukin (Arenadata) (finder)


## Download APIs expose plugin data without authentication ## { #CVE-2026-55814 }

CVE-2026-55814 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-55814) [\[CVE json\]](./CVE-2026-55814.cve.json) [\[OSV json\]](./CVE-2026-55814.osv.json)



_Last updated: 2026-08-10T10:21:26.393Z_

### Affected

* Apache Ranger through 2.8.0


### Description

Missing Authentication in Apache Ranger Download APIs on versions &lt;= 2.8.0.<br>Users are recommended to upgrade to version 2.9.0, which fixes this issue.

### References
* https://lists.apache.org/thread/yoorhnbxfydb5xoxlxlmms0f268rj9dh


### Credits
* Andrew Rukin (Arenadata) (finder)


## Remote Code Execution Vulnerability in GraalScriptEngineCreator ## { #CVE-2026-55799 }

CVE-2026-55799 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-55799) [\[CVE json\]](./CVE-2026-55799.cve.json) [\[OSV json\]](./CVE-2026-55799.osv.json)



_Last updated: 2026-08-10T10:23:27.092Z_

### Affected

* Apache Ranger through 2.8.0


### Description

Remote Code Execution Vulnerability in GraalScriptEngineCreator in Apache Ranger &lt;= 2.8.0<br>Users are recommended to upgrade to version 2.9.0, which fixes this issue.

### References
* https://lists.apache.org/thread/mqpdrqrvd47x5vhy03xok4ylbo9wbqgj


### Credits
* kippford Q. <k3ppf0r@gmail.com> (finder)


## Remote Code Execution via Arbitrary Class Instantiation ## { #CVE-2026-44416 }

CVE-2026-44416 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44416) [\[CVE json\]](./CVE-2026-44416.cve.json) [\[OSV json\]](./CVE-2026-44416.osv.json)



_Last updated: 2026-08-10T10:23:49.093Z_

### Affected

* Apache Ranger through 2.8.0


### Description

<span style="background-color: rgb(255, 255, 255);">Remote Code Execution via Arbitrary Class Instantiation</span> in&nbsp;<span style="background-color: rgb(255, 255, 255);">plugin-schema-registry</span>&nbsp;component in <span style="background-color: rgb(255, 255, 255);">Apache Ranger &lt;= 2.8.0</span>.<br>Users are recommended to upgrade to version 2.9.0, which fixes this issue.

### References
* https://lists.apache.org/thread/2gqssqhwkzbpd8jx8q6986cwldr7qkdn


### Credits
* Andrew Rukin (Arenadata) (finder)


## Remote Code Execution via JDBC URL Injection ## { #CVE-2026-42537 }

CVE-2026-42537 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42537) [\[CVE json\]](./CVE-2026-42537.cve.json) [\[OSV json\]](./CVE-2026-42537.osv.json)



_Last updated: 2026-08-10T10:24:33.165Z_

### Affected

* Apache Ranger through 2.8.0


### Description

<span style="background-color: rgb(255, 255, 255);">Remote Code Execution via JDBC URL Injection</span>&nbsp;in Apache Ranger &lt;= 2.8.0<br>Users are recommended to upgrade to version 2.9.0, which fixes this issue.

### References
* https://lists.apache.org/thread/ymwvz8cwv3wm8fq21pnd7fco0l1m4wrp


### Credits
* Andrew Rukin (Arenadata) (finder)


## Privilege Escalation via URL Parameter ## { #CVE-2026-40920 }

CVE-2026-40920 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40920) [\[CVE json\]](./CVE-2026-40920.cve.json) [\[OSV json\]](./CVE-2026-40920.osv.json)



_Last updated: 2026-08-10T10:25:48.184Z_

### Affected

* Apache Ranger through 2.8.0


### Description

Privilege Escalation via URL Parameter&nbsp;is reported in Apache Ranger versions &lt;= 2.8.0.<br><br>Users are recommended to upgrade to version 2.9.0, which fixes this issue.

### References
* https://lists.apache.org/thread/zh92fob9gqp196rvz3x9t0d2fnq9g27d


### Credits
* Andrew Rukin (Arenadata) (finder)


## SQL Injection vulnerability in lookup functionality ## { #CVE-2026-32227 }

CVE-2026-32227 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-32227) [\[CVE json\]](./CVE-2026-32227.cve.json)

_Last updated: 2026-08-10T10:26:05.115Z_

### Affected

* Apache Ranger from 2.0.0 through 2.8.0 unknown


### Description

<p>SQL Injection vulnerability vulnerability in Apache Ranger.</p><p>This issue affects .</p><p>Users are recommended to upgrade to version 2.9.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/1zltfzd6rp683omrlv1zkxvkwm9d0nd2


### Credits
* 罗鑫 <lx2317103712@gmail.com> (finder)


## OS Command Injection via Username in UnixUserGroupBuilder ## { #CVE-2026-28672 }

CVE-2026-28672 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-28672) [\[CVE json\]](./CVE-2026-28672.cve.json) [\[OSV json\]](./CVE-2026-28672.osv.json)



_Last updated: 2026-08-10T10:26:31.190Z_

### Affected

* Apache Ranger from 0.6 through 2.8


### Description

<p>Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Ranger.</p><p>This issue affects Apache Ranger: from 0.6 through 2.8.</p><p></p><div><br></div><br><p></p>

### References
* https://lists.apache.org/thread/99ysjqcmz950o3jgm6pqx1wb696onzq7


### Credits
* Andrea Cosentino (finder)


## Hostname verification bypass in NiFiRegistryClient ## { #CVE-2025-59060 }

CVE-2025-59060 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-59060) [\[CVE json\]](./CVE-2025-59060.cve.json) [\[OSV json\]](./CVE-2025-59060.osv.json)



_Last updated: 2026-08-21T20:11:10.266Z_

### Affected

* Apache Ranger through 2.7.0


### Description

<p>Hostname verification bypass issue in Apache Ranger NiFiRegistryClient/NiFiClient is reported in Apache Ranger versions &lt;= 2.7.0.</p>Users are recommended to upgrade to version 2.8.0, which fixes this issue.

### References
* https://lists.apache.org/thread/c4plx81z3xs86vgl3fd95y3q7hhtff05


### Credits
* Nikita Markevich <markevich.nikita1@gmail.com> (finder)


## Remote Code Execution Vulnerability in NashornScriptEngineCreator ## { #CVE-2025-59059 }

CVE-2025-59059 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-59059) [\[CVE json\]](./CVE-2025-59059.cve.json) [\[OSV json\]](./CVE-2025-59059.osv.json)



_Last updated: 2026-03-03T10:46:03.383Z_

### Affected

* Apache Ranger through 2.7.0


### Description

Remote Code Execution Vulnerability in NashornScriptEngineCreator is reported in Apache Ranger versions &lt;= 2.7.0.<br>Users are recommended to upgrade to version 2.8.0, which fixes this issue.

### References
* https://lists.apache.org/thread/z47q86rho80390lf2qcmoc2josvs0gtv


### Credits
* chengtianyi <chengtianyi@huawei.com> (finder)


## Improper Neutralization of Formula Elements in a CSV File ## { #CVE-2024-55532 }

CVE-2024-55532 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-55532) [\[CVE json\]](./CVE-2024-55532.cve.json) [\[OSV json\]](./CVE-2024-55532.osv.json)



_Last updated: 2025-03-03T16:17:53.766Z_

### Affected

* Apache Ranger through 2.5.0


### Description

Improper Neutralization of Formula Elements in Export CSV feature of Apache Ranger in Apache Ranger Version &lt; 2.6.0.<br>Users are recommended to upgrade to version 2.6.0, which fixes this issue.

### References
* https://cwiki.apache.org/confluence/display/RANGER/Vulnerabilities+found+in+Ranger


### Credits
* "김도균"<a2256014@naver.com> (finder)


## SSRF in Edit Service page - Add logic to filter requests to localhost ## { #CVE-2024-45479 }

CVE-2024-45479 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45479) [\[CVE json\]](./CVE-2024-45479.cve.json) [\[OSV json\]](./CVE-2024-45479.osv.json)



_Last updated: 2025-06-10T09:06:31.823Z_

### Affected

* Apache Ranger from 2.4.0 before 2.5.0


### Description

SSRF vulnerability in Edit Service Page of Apache Ranger UI in Apache Ranger Version 2.4.0.<br>Users are recommended to upgrade to version Apache Ranger 2.5.0, which fixes this issue.

### References
* https://cwiki.apache.org/confluence/display/RANGER/Vulnerabilities+found+in+Ranger


### Credits
* Gyujin (biz@web-us.kr) (finder)


## Stored XSS in Edit Service page - Add logic to validate user input ## { #CVE-2024-45478 }

CVE-2024-45478 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45478) [\[CVE json\]](./CVE-2024-45478.cve.json) [\[OSV json\]](./CVE-2024-45478.osv.json)



_Last updated: 2025-06-10T09:05:24.595Z_

### Affected

* Apache Ranger from 2.4.0 before 2.5.0


### Description

Stored XSS vulnerability in Edit Service Page of Apache Ranger UI in Apache Ranger Version 2.4.0.<br>Users are recommended to upgrade to version Apache Ranger 2.5.0, which fixes this issue.

### References
* https://cwiki.apache.org/confluence/display/RANGER/Vulnerabilities+found+in+Ranger


### Credits
* Gyujin (biz@web-us.kr) (finder)


## code execution vulnerability in policy expressions ## { #CVE-2022-45048 }

CVE-2022-45048 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-45048) [\[CVE json\]](./CVE-2022-45048.cve.json) [\[OSV json\]](./CVE-2022-45048.osv.json)



_Last updated: 2023-05-05T07:50:14.288Z_

### Affected

* Apache Ranger at 2.3.0


### Description

<p>Authenticated users with appropriate privileges can create policies having expressions that can exploit code execution vulnerability.&nbsp;This issue affects Apache Ranger: 2.3.0. Users are recommended to update to version 2.4.0.<br></p>

### References
* https://lists.apache.org/thread/6rpzwy1smdhr60tsh1ydknn3kdm45bb6


### Credits
* g1831767442@163.com (finder)


## Permissions problem in the Apache Ranger Hive Plugin ## { #CVE-2021-40331 }

CVE-2021-40331 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-40331) [\[CVE json\]](./CVE-2021-40331.cve.json) [\[OSV json\]](./CVE-2021-40331.osv.json)



_Last updated: 2023-05-05T07:55:02.663Z_

### Affected

* Apache Ranger Hive Plugin from 2.0.0 through 2.3.0


### Description

An Incorrect Permission Assignment for Critical Resource vulnerability was found in the Apache Ranger Hive Plugin. Any user with SELECT privilege on a database can alter the ownership of the table in Hive when Apache Ranger Hive Plugin is enabled<br><p>This issue affects Apache Ranger Hive Plugin: from 2.0.0 through 2.3.0. Users are recommended to upgrade to version 2.4.0 or later.<br></p>

### References
* https://lists.apache.org/thread/s68yls6cnkdmzn1k4hqt50vs6wjvt2rn
