---
title: Apache Ranger security advisories
description: Security information for Apache Ranger
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Ranger? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improper Neutralization of Formula Elements in a CSV File ## { #CVE-2024-55532 }

CVE-2024-55532 [\[CVE json\]](./CVE-2024-55532.cve.json) [\[OSV json\]](./CVE-2024-55532.osv.json)



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

CVE-2024-45479 [\[CVE json\]](./CVE-2024-45479.cve.json) [\[OSV json\]](./CVE-2024-45479.osv.json)



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

CVE-2024-45478 [\[CVE json\]](./CVE-2024-45478.cve.json) [\[OSV json\]](./CVE-2024-45478.osv.json)



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

CVE-2022-45048 [\[CVE json\]](./CVE-2022-45048.cve.json) [\[OSV json\]](./CVE-2022-45048.osv.json)



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

CVE-2021-40331 [\[CVE json\]](./CVE-2021-40331.cve.json) [\[OSV json\]](./CVE-2021-40331.osv.json)



_Last updated: 2023-05-05T07:55:02.663Z_

### Affected

* Apache Ranger Hive Plugin from 2.0.0 through 2.3.0


### Description

An Incorrect Permission Assignment for Critical Resource vulnerability was found in the Apache Ranger Hive Plugin. Any user with SELECT privilege on a database can alter the ownership of the table in Hive when Apache Ranger Hive Plugin is enabled<br><p>This issue affects Apache Ranger Hive Plugin: from 2.0.0 through 2.3.0. Users are recommended to upgrade to version 2.4.0 or later.<br></p>

### References
* https://lists.apache.org/thread/s68yls6cnkdmzn1k4hqt50vs6wjvt2rn
