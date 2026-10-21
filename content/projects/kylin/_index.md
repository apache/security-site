---
title: Apache Kylin security advisories
description: Security information for Apache Kylin
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache Kylin? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Kylin).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Broken Access Control in QuerySQLBlacklistController ## { #CVE-2026-69080 }

CVE-2026-69080 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-69080) [\[CVE json\]](./CVE-2026-69080.cve.json) [\[OSV json\]](./CVE-2026-69080.osv.json)



_Last updated: 2026-10-16T19:37:48.573Z_

### Affected

* Apache Kylin from 4..0.0 through 5.0.4


### Description

<p>Exposure of SQL Black List to an Unauthorized Actor vulnerability in Apache Kylin.</p><p>This issue affects Apache Kylin: from 4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/zrt6z545y8z9qtsbyzfy55sdpf75osnp


### Credits
* Haoran Zhao, Yicheng Yu, and Lei Zhang  (System and Software Security Lab in Fudan University) (finder)
* Yan Xu (finder)


## JobController allows unauthorized cross-project manipulation ## { #CVE-2026-69077 }

CVE-2026-69077 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-69077) [\[CVE json\]](./CVE-2026-69077.cve.json) [\[OSV json\]](./CVE-2026-69077.osv.json)



_Last updated: 2026-10-16T19:33:18.593Z_

### Affected

* Apache Kylin from 4..0.0 through 5.0.4


### Description

<p>Exposure of&nbsp;unauthorized cross-project job manipulation vulnerability in Apache Kylin.&nbsp;Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted.</p><p>This issue affects Apache Kylin: from 4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/wcc7w3lbhfcgb51p867shv1d513z7x1t


### Credits
* Harry <h9408400@gmail.com> (finder)


## Unauthorized cross-project job discard ## { #CVE-2026-69076 }

CVE-2026-69076 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-69076) [\[CVE json\]](./CVE-2026-69076.cve.json) [\[OSV json\]](./CVE-2026-69076.osv.json)



_Last updated: 2026-10-16T19:32:38.215Z_

### Affected

* Apache Kylin from 4..0.0 through 5.0.4


### Description

<p>Exposure of Job Discard to an Unauthorized Actor vulnerability in Apache Kylin.&nbsp;Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted.</p><p>This issue affects Apache Kylin: from 4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/w4cpyg5q4h2152bx9zmbh739skwqm35h


### Credits
* Yicheng Yu (finder)
* Haoran Zhao (finder)
* Lei Zhang (finder)


## Unauthenticated Metastore Cleanup ## { #CVE-2026-68573 }

CVE-2026-68573 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68573) [\[CVE json\]](./CVE-2026-68573.cve.json) [\[OSV json\]](./CVE-2026-68573.osv.json)



_Last updated: 2026-10-16T19:32:20.962Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.4


### Description

<p>Improper Authentication vulnerability in Apache Kylin. Unauthenticated user may access to system cleanup actions.&nbsp;Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted. </p><p>This issue affects Apache Kylin: from 4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/4n3qt477rtvwnko2olb3hjwjll1yry8j


### Credits
* Fabian Fleischer (finder)
* MopMonk-AI (finder)
* Wanxin Yin (finder)


## Unauthorized SQL execution to Spark SQL env ## { #CVE-2026-68572 }

CVE-2026-68572 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68572) [\[CVE json\]](./CVE-2026-68572.cve.json) [\[OSV json\]](./CVE-2026-68572.osv.json)



_Last updated: 2026-10-16T19:32:01.398Z_

### Affected

* Apache Kylin from 4..0.0 through 5.0.4


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Kylin.</p><p>This issue affects Apache Kylin: from 4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/r0boyqp211s7316oclh666bq40vbs9n7


### Credits
* Yicheng <yyc2569580673@gmail.com> (finder)


## JDBC URL Whitelist Verification Bypass ## { #CVE-2026-68571 }

CVE-2026-68571 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68571) [\[CVE json\]](./CVE-2026-68571.cve.json) [\[OSV json\]](./CVE-2026-68571.osv.json)



_Last updated: 2026-10-16T12:16:11.183Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.4


### Description

<p>Improper Control of Generation of Code ('Code Injection') vulnerability in Apache Kylin. Special parameter in JDBC URL can lead to code injection.&nbsp;
Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted.

</p><p>This issue affects Apache Kylin: from 4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/vmjozo864ss37c1jbdlld9m6d84ndpbs


### Credits
* Fushuling, RacerZ, yulate (finder)


## Missing authentication on certain cache API endpoints ## { #CVE-2026-64959 }

CVE-2026-64959 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-64959) [\[CVE json\]](./CVE-2026-64959.cve.json) [\[OSV json\]](./CVE-2026-64959.osv.json)



_Last updated: 2026-10-16T12:15:59.053Z_

### Affected

* Apache Kylin from 5.0.0 through 5.0.4


### Description

<p>Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection'), Missing Authentication for Critical Function vulnerability in Apache Kylin.&nbsp;Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted.</p><p>This issue affects Apache Kylin: from 5 through 5.0.4. Certain backend cache API misses required authentication and can cause execution of injected SQL.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/oho4tw8kvxkybwpjykzl49zx6o17tkdt


### Credits
* zx (Jace) <g.mygenie@gmail.com> (finder)
* baozongwi <baozongwi@qq.com> (finder)
* chennbnbnb (finder)


## Redis unsafe Java deserialization ## { #CVE-2026-64610 }

CVE-2026-64610 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-64610) [\[CVE json\]](./CVE-2026-64610.cve.json) [\[OSV json\]](./CVE-2026-64610.osv.json)



_Last updated: 2026-10-16T12:13:17.132Z_

### Affected

* Apache Kylin from 4..0.0 through 5.0.4


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Kylin.&nbsp;Unsafe Java deserialization could happen from a broken external cache service.</p><p>This issue affects Apache Kylin: from 4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/5jwj20t50wc6x9pw0zmlj8tzfl37dpry


### Credits
* Andrew Ridings <ridingsa@gmail.com> (finder)


## Missing authorization and path-confinement on system meta dump ## { #CVE-2026-63619 }

CVE-2026-63619 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-63619) [\[CVE json\]](./CVE-2026-63619.cve.json) [\[OSV json\]](./CVE-2026-63619.osv.json)



_Last updated: 2026-10-16T12:11:49.760Z_

### Affected

* Apache Kylin from 4..0.0 through 5.0.4


### Description

<p>Missing Authorization vulnerability in Apache Kylin. A backend metadata dump API misses the enough authorization and the path-confinement.&nbsp;Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted.</p><p>This issue affects Apache Kylin: from 4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/p3rzz43h1kqc55wjshxmx2dbbmx76qrg


### Credits
* "George Chen" <http://github.com/geo-chen> (finder)
* n0mi1k Security (finder)
* MopMonk-AI (finder)


## Low-Privilege Config Exposure ## { #CVE-2026-63618 }

CVE-2026-63618 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-63618) [\[CVE json\]](./CVE-2026-63618.cve.json) [\[OSV json\]](./CVE-2026-63618.osv.json)



_Last updated: 2026-10-16T12:11:33.595Z_

### Affected

* Apache Kylin from 4..0.0 through 5.0.4


### Description

<p>Exposure of Sensitive Information (system level configuration info) to an Unauthorized Actor vulnerability in Apache Kylin.</p><p>This issue affects Apache Kylin: from 4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/5zrg002omkynt3hsjobvkp61yznr6qg3


### Credits
* IcySun <icysun@qq.com> (finder)
* "George Chen" <http://github.com/geo-chen> (finder)


## Improper authorization in job information retrieval ## { #CVE-2026-62393 }

CVE-2026-62393 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-62393) [\[CVE json\]](./CVE-2026-62393.cve.json) [\[OSV json\]](./CVE-2026-62393.osv.json)



_Last updated: 2026-07-14T12:19:26.389Z_

### Affected

* Apache Kylin from 4 through 5.0.3


### Description

<p>Improper Handling of Insufficient Permissions or Privileges vulnerability in Apache Kylin.&nbsp;Improper authorization in job information retrieval, where an attacker may get access to unauthorized jobs in other projects.</p><p>This issue affects Apache Kylin: from 4 through 5.0.3.</p><p>Users are recommended to upgrade to version 5.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/xg8dcyjw0nkq5y8dhq3r25x3rxc62x9j


### Credits
* Yicheng <yyc2569580673@gmail.com> (finder)
* Haoran Zhao (finder)
* Lei Zhang (finder)


## OS Command Injection via Async Query API ## { #CVE-2026-62392 }

CVE-2026-62392 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-62392) [\[CVE json\]](./CVE-2026-62392.cve.json) [\[OSV json\]](./CVE-2026-62392.osv.json)



_Last updated: 2026-07-14T12:18:55.913Z_

### Affected

* Apache Kylin from 4 through 5.0.3


### Description

<p>Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Kylin. A backend API may bring job config parameters to OS command line.</p><p>This issue affects Apache Kylin: from 4 through 5.0.3.</p><p>Users are recommended to upgrade to version 5.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/9hof8lxo3mzshsh5r77mskzqlkns09gn


### Credits
* Suraj Kattimuttathu Suresh <sksuraj@ucsb.edu> (finder)


## SQL Injection Vulnerability in Catalog Cache Refresh API ## { #CVE-2026-62390 }

CVE-2026-62390 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-62390) [\[CVE json\]](./CVE-2026-62390.cve.json) [\[OSV json\]](./CVE-2026-62390.osv.json)



_Last updated: 2026-07-14T12:09:39.268Z_

### Affected

* Apache Kylin from 4 through 5.0.3


### Description

<p>Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Kylin. A backend API refreshing table catalog may cause the injection to the generated SQL.</p><p>This issue affects Apache Kylin: from 4 through 5.0.3.</p><p>Users are recommended to upgrade to version 5.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zdrj93txvdjj07f88s43d2pcg2gomvjc


### Credits
* 罗鑫 <lx2317103712@gmail.com> (finder)


## Potential computed-column resource exhaustion ## { #CVE-2026-108837 }

CVE-2026-108837 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108837) [\[CVE json\]](./CVE-2026-108837.cve.json) [\[OSV json\]](./CVE-2026-108837.osv.json)



_Last updated: 2026-10-19T09:22:02.755Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.4


### Description

<p>Allocation of resources without limits or throttling vulnerability in Apache Kylin. Given an attacker has got project admin permission, an cache API maybe used to cause&nbsp;computed-column resource exhaustion.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/qgpgkx6zh37tlys28qlysrffo6pz614v


### Credits
* HRsGIT (https://github.com/HRsGIT) (finder)


## default startup profile miss security settings ## { #CVE-2026-108833 }

CVE-2026-108833 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108833) [\[CVE json\]](./CVE-2026-108833.cve.json) [\[OSV json\]](./CVE-2026-108833.osv.json)



_Last updated: 2026-10-19T09:21:52.936Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.4


### Description

<p>Default startup profile miss security settings&nbsp;in Apache Kylin. Any deployment has security setting profile turned on does not impact.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/lqb36tsyp3fdsg5x4qvz4fy3hkzcr2wz


### Credits
* Hari (Harikrishna KP) (finder)


## Potential unauthenticated job metadata replacement ## { #CVE-2026-108823 }

CVE-2026-108823 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108823) [\[CVE json\]](./CVE-2026-108823.cve.json) [\[OSV json\]](./CVE-2026-108823.osv.json)



_Last updated: 2026-10-19T09:21:29.601Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.4


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor during job manipulation in Apache Kylin. The impact is minor unless job services are exposed to public network, which is uncommon.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/bhcvh3oxcqcjklxfr2mn1j3f7pzxqz4b


### Credits
* garymao (finder)
* Wanxin Yin (finder)


## Potential JDBC source configuration validation issue ## { #CVE-2026-108780 }

CVE-2026-108780 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108780) [\[CVE json\]](./CVE-2026-108780.cve.json) [\[OSV json\]](./CVE-2026-108780.osv.json)



_Last updated: 2026-10-19T09:21:18.887Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.4


### Description

<p>Potential JDBC source configuration validation&nbsp;vulnerability in Apache Kylin. The impact is minor, unless the kylin backend services are open to public network.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/vyc83rb5t0f4nyvn1dzggshcqdqf9lj0


### Credits
* An academic team studying incomplete security fixes (finder)


## tables/names SparkSQL injection ## { #CVE-2026-108776 }

CVE-2026-108776 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108776) [\[CVE json\]](./CVE-2026-108776.cve.json) [\[OSV json\]](./CVE-2026-108776.osv.json)



_Last updated: 2026-10-19T09:21:07.955Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.4


### Description

<p>Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Kylin. The impact is moderate if kylin service is in query only mode, which is the default and most common mode.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/x3m1k00f6470238mw51jbnpnh642jv0d


### Credits
* MopMonk-AI (finder)


## unauthenticated broadcast API and polymorphic deserialization ## { #CVE-2026-108771 }

CVE-2026-108771 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108771) [\[CVE json\]](./CVE-2026-108771.cve.json) [\[OSV json\]](./CVE-2026-108771.osv.json)



_Last updated: 2026-10-19T09:20:58.077Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.4


### Description

<p>Missing authentication for in-house broadcast and&nbsp;polymorphic deserialization&nbsp;vulnerability in Apache Kylin.&nbsp;Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/d77s7dh3bxf02l4rjbgb6807g605zskx


### Credits
* MopMonk-AI (finder)
* Wanxin Yin (finder)
* Dilrevx (finder)


## missing JDBC-config authorization ## { #CVE-2026-108766 }

CVE-2026-108766 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108766) [\[CVE json\]](./CVE-2026-108766.cve.json) [\[OSV json\]](./CVE-2026-108766.osv.json)



_Last updated: 2026-10-19T09:20:46.793Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.4


### Description

<p>Missing authorization on jdbc source config update in Apache Kylin.&nbsp;Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/50447hzwyz8r9xwtfbylsphv4ylq9yhj


### Credits
* n0mi1k Security (finder)
* kta1kri (finder)


## delete metadata backup path-confinement bypass ## { #CVE-2026-108762 }

CVE-2026-108762 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108762) [\[CVE json\]](./CVE-2026-108762.cve.json) [\[OSV json\]](./CVE-2026-108762.osv.json)



_Last updated: 2026-10-19T09:16:24.632Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.4


### Description

<p>Path-confinement bypass&nbsp;during metadata backup deletion in Apache Kylin. Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/6n1o1t14ssc5x4dg18hlv30crwbhwdpd


### Credits
* n0mi1k Security (finder)


## spark job OS command injection ## { #CVE-2026-108743 }

CVE-2026-108743 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108743) [\[CVE json\]](./CVE-2026-108743.cve.json) [\[OSV json\]](./CVE-2026-108743.osv.json)



_Last updated: 2026-10-16T19:44:36.454Z_

### Affected

* Apache Kylin from 4.0.4 through 5.0.4


### Description

<p>Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Kylin.&nbsp;Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted.</p><p>This issue affects Apache Kylin: from 4.0.4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/6x2v755lrxf72xcrzjq4t2b1sd56ywb7


### Credits
* n0mi1k Security (finder)


## Unauthenticated Metadata Broadcast (inside in-house network) ## { #CVE-2026-108709 }

CVE-2026-108709 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108709) [\[CVE json\]](./CVE-2026-108709.cve.json) [\[OSV json\]](./CVE-2026-108709.osv.json)



_Last updated: 2026-10-16T19:38:20.115Z_

### Affected

* Apache Kylin from 4.0.4 through 5.0.4


### Description

<p>Authentication bypass within in-house network in Apache Kylin.&nbsp;Impact most to the kylin services that are directly exposed to public network, which is not common. In-house kylin deployments are mostly not impacted.</p><p>This issue affects Apache Kylin: from 4.0.4 through 5.0.4.</p><p>Users are recommended to upgrade to version 5.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/okkvcvoj1007f6cxhwp9v6j6t4ynfnwb


### Credits
* RunningSnail (finder)


## Server-Side Request Forgery ## { #CVE-2025-61735 }

CVE-2025-61735 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-61735) [\[CVE json\]](./CVE-2025-61735.cve.json) [\[OSV json\]](./CVE-2025-61735.osv.json)



_Last updated: 2026-02-02T07:35:53.853Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.2


### Description

<p>Server-Side Request Forgery (SSRF) vulnerability in Apache Kylin.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.2.&nbsp;You are fine as long as the Kylin's system and project admin access is well protected.</p><p>Users are recommended to upgrade to version 5.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/yscobmx869zvprsykb94r24jtmb58ckh


### Credits
* liuhuajin <liuhuajin1@huawei.com> (finder)
* 75Acol (finder)
* fcgboy (finder)
* stan fang (finder)
* zer0duck (finder)


## improper restriction of file read ## { #CVE-2025-61734 }

CVE-2025-61734 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-61734) [\[CVE json\]](./CVE-2025-61734.cve.json) [\[OSV json\]](./CVE-2025-61734.osv.json)



_Last updated: 2026-02-02T07:35:03.252Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.2


### Description

<p>Files or Directories Accessible to External Parties vulnerability in Apache Kylin.
 You are fine as long as the Kylin's system and project admin access is well protected.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.2.</p><p>Users are recommended to upgrade to version 5.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/z705g7sn3g0bkchlqbo1hz1tyqorn4d2


### Credits
* liuhuajin <liuhuajin1@huawei.com> (finder)
* 75Acol (finder)
* fcgboy (finder)
* stan fang (finder)
* zer0duck (finder)


## Authentication bypass ## { #CVE-2025-61733 }

CVE-2025-61733 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-61733) [\[CVE json\]](./CVE-2025-61733.cve.json) [\[OSV json\]](./CVE-2025-61733.osv.json)



_Last updated: 2026-02-02T07:33:38.093Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.2


### Description

<p>Authentication Bypass Using an Alternate Path or Channel vulnerability in Apache Kylin.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.2.</p><p>Users are recommended to upgrade to version 5.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/8wmcffly6gp50nmfw8j4w3hlmv843yo0


### Credits
* liuhuajin <liuhuajin1@huawei.com> (finder)
* 75Acol (finder)
* fcgboy (finder)
* stan fang (finder)
* zer0duck (finder)


## The remote code execution via jdbc url ## { #CVE-2025-30067 }

CVE-2025-30067 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-30067) [\[CVE json\]](./CVE-2025-30067.cve.json) [\[OSV json\]](./CVE-2025-30067.osv.json)



_Last updated: 2025-03-27T15:06:34.995Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.1


### Description

<p>Improper Control of Generation of Code ('Code Injection') vulnerability in Apache Kylin. 
If an attacker gets access to Kylin's system or project admin permission, the JDBC connection configuration maybe altered to execute arbitrary code from the remote. You are fine as long as the Kylin's system and project admin access is well protected.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.1.</p><p>Users are recommended to upgrade to version 5.0.2 or above, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/6j19pt8yoqfphf1lprtrzoqkvz1gwbnc


### Credits
* Pho3n1x <ph03n1x@qq.com> (finder)


## SSRF vulnerability in the diagnosis api ## { #CVE-2024-48944 }

CVE-2024-48944 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-48944) [\[CVE json\]](./CVE-2024-48944.cve.json) [\[OSV json\]](./CVE-2024-48944.osv.json)



_Last updated: 2025-04-28T14:59:34.758Z_

### Affected

* Apache Kylin from 5.0.0 through 5.0.1


### Description

<p>Server-Side Request Forgery (SSRF) vulnerability in Apache Kylin. Through a kylin server, an attacker may forge a request to invoke "/kylin/api/xxx/diag" api on another internal host and possibly get leaked information. There are two preconditions: 1) The attacker has got admin access to a kylin server; 2) Another internal host has the "/kylin/api/xxx/diag" api

endpoint open for service.<br></p><p>This issue affects Apache Kylin: from 5.0.0 
through 

5.0.1.</p><p>Users are recommended to upgrade to version 5.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/1xxxtdfh9hzqsqgb1pd9grb8hvqdyc9x


### Credits
* Zevi <linzmgx@gmail.com> (finder)


## Session fixation in web interface ## { #CVE-2024-23590 }

CVE-2024-23590 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23590) [\[CVE json\]](./CVE-2024-23590.cve.json) [\[OSV json\]](./CVE-2024-23590.osv.json)



_Last updated: 2024-11-04T09:27:04.256Z_

### Affected

* Apache Kylin from 2.0.0 before 5.0.0


### Description

<p>Session Fixation vulnerability in Apache Kylin.</p><p>This issue affects Apache Kylin: from 2.0.0 through 4.x.</p><p>Users are recommended to upgrade to version 5.0.0 or above, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7161154h0k6zygr9917qq0g95p39szml


### Credits
* XJB Security Team (reporter)


## Insufficiently protected credentials in config file ## { #CVE-2023-29055 }

CVE-2023-29055 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-29055) [\[CVE json\]](./CVE-2023-29055.cve.json) [\[OSV json\]](./CVE-2023-29055.osv.json)



_Last updated: 2024-01-29T12:20:52.048Z_

### Affected

* Apache Kylin from 2.0.0 through 4.0.3


### Description

<div>In Apache Kylin version 2.0.0 to 4.0.3, there is a Server Config web interface that displays the content of file 'kylin.properties', that may contain serverside credentials. When the kylin service runs over HTTP (or other plain text protocol), it is possible for network sniffers to hijack the HTTP payload and get access to the content of kylin.properties and potentially the containing credentials.<br></div><div><br></div><div>To avoid this threat, users are recommended to&nbsp;</div><div><ol><li>Always turn on HTTPS so that network payload is encrypted.<br></li><li>Avoid putting credentials in kylin.properties, or at least not in plain text.</li><li>Use network firewalls to protect the serverside such that it is not accessible to external attackers.<br></li><li>Upgrade to version Apache Kylin 4.0.4, which filters out the sensitive content that goes to the Server Config web interface.</li></ol><br></div>

### References
* https://lists.apache.org/thread/o1bvyv9wnfkx7dxpfjlor20nykgsoh6r


### Credits
* Li Jiakun <2839549219@qq.com> (reporter)


## Command injection by Diagnosis Controller ## { #CVE-2022-44621 }

CVE-2022-44621 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-44621) [\[CVE json\]](./CVE-2022-44621.cve.json) [\[OSV json\]](./CVE-2022-44621.osv.json)



_Last updated: 2022-12-30T10:31:39.045Z_

### Affected

* Apache Kylin from Apache Kylin 4  through 4.0.2


### Description

Diagnosis Controller miss parameter validation, so user may attacked by command injection via HTTP Request.

### References
* https://lists.apache.org/thread/7ctchj24dofgsj9g1rg1245cms9myb34


### Credits
* Messy God <godimessy@gmail.com> (finder)


## Command injection by Useless configuration ## { #CVE-2022-43396 }

CVE-2022-43396 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-43396) [\[CVE json\]](./CVE-2022-43396.cve.json) [\[OSV json\]](./CVE-2022-43396.osv.json)



_Last updated: 2022-12-30T10:30:28.434Z_

### Affected

* Apache Kylin from Apache Kylin 4 through 4.0.2


### Description

In the fix for CVE-2022-24697, a blacklist is used to filter user input commands. But there is a risk of being bypassed. The user can control the command by controlling the&nbsp;kylin.engine.spark-cmd&nbsp;parameter of conf.

### References
* https://lists.apache.org/thread/ob2ks04zl5ms0r44cd74y1xdl1rzfd1r


### Credits
* Yasax1 Li <pp1ove.lit@gmail.com> (finder)


## Apache Kylin prior to 4.0.2 allows command injection when the configuration overwrites function overwrites system parameters ## { #CVE-2022-24697 }

CVE-2022-24697 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-24697) [\[CVE json\]](./CVE-2022-24697.cve.json) [\[OSV json\]](./CVE-2022-24697.osv.json)



_Last updated: 2022-10-13T13:05:28.696Z_

### Affected

* Apache Kylin from Apache Kylin 2 before 2.6.6
* Apache Kylin from Apache Kylin 3 through 3.1.2
* Apache Kylin from Apache Kylin 4 through 4.0.1


### Description

Kylin's cube designer function has a command injection vulnerability when overwriting system parameters in the configuration overwrites menu. RCE can be implemented by closing the single quotation marks around the parameter value of “-- conf=” to inject any operating system command into the command line parameters. This vulnerability affects Kylin 2 version 2.6.5 and earlier, Kylin 3 version 3.1.2 and earlier, and Kylin 4 version 4.0.1 and earlier.

### References
* https://lists.apache.org/thread/07mnn9c7o314wrhrwjr10w9j5s82voj4


### Credits
* Kylin Team would like to thanks Kai Zhao of ToTU Secruity Team.


## Hardcoded credentials ## { #CVE-2021-45458 }

CVE-2021-45458 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-45458) [\[CVE json\]](./CVE-2021-45458.cve.json) [\[OSV json\]](./CVE-2021-45458.osv.json)



_Last updated: 2022-01-06T12:33:02.681Z_

### Affected

* Apache Kylin from Apache Kylin 2 through 2.6.6
* Apache Kylin from Apache Kylin 3 through 3.1.2
* Apache Kylin from Apache Kylin 4 through 4.0.0


### Description

Apache Kylin provides encryption classes PasswordPlaceholderConfigurer to help users encrypt their passwords. In the encryption algorithm used by this encryption class, the cipher is initialized with a hardcoded key and IV.  If users use class PasswordPlaceholderConfigurer to encrypt their password and configure it into kylin's configuration file, there is a risk that the password may be decrypted.
This issue affects Apache Kylin 2 version 2.6.6 and prior versions; Apache Kylin 3 version 3.1.2 and prior versions; Apache Kylin 4 version 4.0.0 and prior versions.

### References
* https://lists.apache.org/thread/oof215qz188k16vhlo97cm1jksxdowfy


### Credits
* Alvaro Munoz <pwntester@github.com>


## Overly broad CORS configuration  ## { #CVE-2021-45457 }

CVE-2021-45457 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-45457) [\[CVE json\]](./CVE-2021-45457.cve.json) [\[OSV json\]](./CVE-2021-45457.osv.json)



_Last updated: 2022-01-06T12:32:08.962Z_

### Affected

* Apache Kylin from Apache Kylin 2 through 2.6.6
* Apache Kylin from Apache Kylin 3 through 3.1.2
* Apache Kylin from Apache Kylin 4 through 4.0.0


### Description

In Apache Kylin, Cross-origin requests with credentials are allowed to be sent from any origin.

This issue affects Apache Kylin 2 version 2.6.6 and prior versions; Apache Kylin 3 version 3.1.2 and prior versions; Apache Kylin 4 version 4.0.0 and prior versions.

### References
* https://lists.apache.org/thread/rzv4mq58okwj1n88lry82ol2wwm57q1m


### Credits
* Alvaro Munoz <pwntester@github.com>


## Command injection ## { #CVE-2021-45456 }

CVE-2021-45456 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-45456) [\[CVE json\]](./CVE-2021-45456.cve.json) [\[OSV json\]](./CVE-2021-45456.osv.json)



_Last updated: 2022-01-06T12:30:40.650Z_

### Affected

* Apache Kylin at Apache Kylin 4 4.0.0


### Description

Apache kylin checks the legitimacy of the project before executing some commands with the project name passed in by the user. There is a mismatch between what is being checked and what is being used as the shell command argument in DiagnosisService. This may cause an illegal project name to pass the check and perform the following steps, resulting in a command injection vulnerability.
This issue affects Apache Kylin 4.0.0.

### References
* https://lists.apache.org/thread/70fkf9w1swt2cqdcz13rwfjvblw1fcpf


### Credits
* Alvaro Munoz <pwntester@github.com>


## Mysql JDBC Connector Deserialize RCE ## { #CVE-2021-36774 }

CVE-2021-36774 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-36774) [\[CVE json\]](./CVE-2021-36774.cve.json) [\[OSV json\]](./CVE-2021-36774.osv.json)



_Last updated: 2022-01-06T12:29:47.699Z_

### Affected

* Apache Kylin from Apache Kylin 2 through 2.6.6
* Apache Kylin from Apache Kylin 3 through 3.1.2


### Description

Apache Kylin allows users to read data from other database systems using JDBC. The MySQL JDBC driver supports certain properties, which, if left unmitigated, can allow an attacker to execute arbitrary code from a hacker-controlled malicious MySQL server within Kylin server processes. 
This issue affects Apache Kylin 2 version 2.6.6 and prior versions; Apache Kylin 3 version 3.1.2 and prior versions.

### References
* https://lists.apache.org/thread/lchpcvoolc6w8zc6vo1wstk8zbfqv2ow


### Credits
* jinchen sheng <jincsheng@gmail.com>


## Apache Kylin unsafe class loading ## { #CVE-2021-31522 }

CVE-2021-31522 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-31522) [\[CVE json\]](./CVE-2021-31522.cve.json) [\[OSV json\]](./CVE-2021-31522.osv.json)



_Last updated: 2022-01-06T12:28:58.641Z_

### Affected

* Apache Kylin from Apache Kylin 2 through 2.6.6
* Apache Kylin from Apache Kylin 3 through 3.1.2
* Apache Kylin from Apache Kylin 4 through 4.0.0


### Description

Kylin can receive user input and load any class through Class.forName(...).
This issue affects Apache Kylin 2 version 2.6.6 and prior versions; Apache Kylin 3 version 3.1.2 and prior versions; Apache Kylin 4 version 4.0.0 and prior versions.

### References
* https://lists.apache.org/thread/hh5crx3yr701zd8wtpqo1mww2rlkvznw


### Credits
* bo yu <forhaby0@gmail.com>


## Improper Access Control to Streaming Coordinator & SSRF ## { #CVE-2021-27738 }

CVE-2021-27738 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-27738) [\[CVE json\]](./CVE-2021-27738.cve.json) [\[OSV json\]](./CVE-2021-27738.osv.json)



_Last updated: 2022-01-06T12:26:35.086Z_

### Affected

* Apache Kylin from Apache Kylin 3 before 3.1.2


### Description

All request mappings in `StreamingCoordinatorController.java` handling `/kylin/api/streaming_coordinator/*` REST API endpoints did not include any security checks, which allowed an unauthenticated user to issue arbitrary requests, such as assigning/unassigning of streaming cubes, creation/modification and deletion of replica sets, to the Kylin Coordinator.

For endpoints accepting node details in HTTP message body, unauthenticated (but limited) server-side request forgery (SSRF) can be achieved.

This issue affects Apache Kylin Apache Kylin 3 versions prior to 3.1.2.

### References
* https://lists.apache.org/thread/vkohh0to2vzwymyb2x13fszs3cs3vd70


### Credits
* Wei Lin Ngo <ngo.weilin@starlabs.sg>
