---
title: Apache DolphinScheduler security advisories
description: Security information for Apache DolphinScheduler
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache DolphinScheduler? You can read more about the projects' security policy on their [security page](https://github.com/apache/dolphinscheduler/blob/dev/docs/docs/en/contribute/join/security.md), and email your report to the [Apache DolphinScheduler Security Team](mailto:security@dolphinscheduler.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://github.com/apache/dolphinscheduler/blob/dev/docs/docs/en/contribute/join/security.md). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## General user can mint admin access tokens via /access-tokens ## { #CVE-2026-49050 }

CVE-2026-49050 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49050) [\[CVE json\]](./CVE-2026-49050.cve.json) [\[OSV json\]](./CVE-2026-49050.osv.json)



_Last updated: 2026-06-17T01:46:54.058Z_

### Affected

* Apache DolphinScheduler before 3.4.2


### Description

<p>General user can mint admin access tokens via /access-tokens</p><p>This issue affects Apache DolphinScheduler: before 3.4.2.</p><p>Users are recommended to upgrade to version 3.4.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/0lc4t5k6h6nhd8t4hshgjk6yp3cl8sb0


### Credits
* George Chen(https://github.com/geo-chen) (finder)


## An incorrect authorization vulnerability allows authenticated users to access alert instances associated with alert groups they do not have permission to access. ## { #CVE-2026-47340 }

CVE-2026-47340 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-47340) [\[CVE json\]](./CVE-2026-47340.cve.json) [\[OSV json\]](./CVE-2026-47340.osv.json)



_Last updated: 2026-06-17T01:44:26.990Z_

### Affected

* Apache DolphinScheduler before 3.4.2


### Description

<p>Allow authenticated users to access alert instances associated with alert groups they do not have permission to access. in Apache DolphinScheduler.</p><p>This issue affects Apache DolphinScheduler: before 3.4.2.</p><p>Users are recommended to upgrade to version 3.4.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/gx6v1wjb6qg3fzksxomysspy2gw54ooc


### Credits
* thesecguy45@gmail.com (finder)
* udolemi (S2W) (finder)


## Incorrect Authorization vulnerability allows users to access workflow instance information belonging to projects they do not have permission to access. ## { #CVE-2026-42357 }

CVE-2026-42357 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42357) [\[CVE json\]](./CVE-2026-42357.cve.json) [\[OSV json\]](./CVE-2026-42357.osv.json)



_Last updated: 2026-06-17T06:31:34.851Z_

### Affected

* Apache DolphinScheduler before 3.4.1


### Description

<p>Incorrect Authorization vulnerability allows users to access workflow instance information belonging to projects they do not have permission to access.<br><br>This issue affects Apache DolphinScheduler versions prior to 3.4.2.<br></p><p>Users are recommended to upgrade to version 3.4.2, which fixes this issue.<br></p><br>

### References
* https://lists.apache.org/thread/74l2rrz32w2chn7vz64313gk7ox5wjtr


### Credits
* Yicheng Yu(https://github.com/FHMTT) (finder)


## Incorrect Authorization vulnerability allows users with system login privileges to delete task definitions in unauthorized projects ## { #CVE-2026-41280 }

CVE-2026-41280 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41280) [\[CVE json\]](./CVE-2026-41280.cve.json) [\[OSV json\]](./CVE-2026-41280.osv.json)



_Last updated: 2026-06-17T06:32:49.794Z_

### Affected

* Apache DolphinScheduler before 3.4.2


### Description

<p>Incorrect Authorization vulnerability allows users with system login privileges to delete task definitions in unauthorized projects<br><br>This issue affects Apache DolphinScheduler versions prior to 3.4.2. </p><p>Users are recommended to upgrade to version 3.4.2, which fixes this issue.<br></p><br>

### References
* https://lists.apache.org/thread/5bv1njp3lbbbj11y20td5yz1b4nmrtvw


### Credits
* Yicheng Yu(https://github.com/FHMTT) (finder)


## The `/v2` experimental interface lacks permission checks ## { #CVE-2026-32967 }

CVE-2026-32967 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-32967) [\[CVE json\]](./CVE-2026-32967.cve.json) [\[OSV json\]](./CVE-2026-32967.osv.json)



_Last updated: 2026-06-17T01:41:50.516Z_

### Affected

* Apache DolphinScheduler before 3.4.2


### Description

<p>Incorrect Authorization vulnerability of `/v2` experimental interface in Apache DolphinScheduler.</p><p>This issue affects Apache DolphinScheduler: before 3.4.2.</p><p>Users are recommended to upgrade to version 3.4.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/5o5jrg1snkmrto96wg015wgbh7hyckzc


### Credits
* b0b0haha (603571786@qq.com) (finder)
* j311yl0v3u (2439839508@qq.com) (finder)


## DataSource API Missing Authorization Check Leads to Arbitrary Data Source Metadata Disclosure ## { #CVE-2026-32966 }

CVE-2026-32966 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-32966) [\[CVE json\]](./CVE-2026-32966.cve.json) [\[OSV json\]](./CVE-2026-32966.osv.json)



_Last updated: 2026-06-17T08:48:15.528Z_

### Affected

* Apache DolphinScheduler before 3.4.2


### Description

<p>DataSource API Missing Authorization Check Leads to Arbitrary Data Source Metadata Disclosure in Apache DolphinScheduler.</p><p>This issue affects Apache DolphinScheduler: before 3.4.2.</p><p>Users are recommended to upgrade to version 3.4.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/4f1fojpj26z9y5nd1ko845gcknpn75g2


### Credits
* b0b0haha (603571786@qq.com) (finder)
* j311yl0v3u (2439839508@qq.com) (finder)


## Users are able to use tenants that are not defined on the platform during workflow execution. ## { #CVE-2026-23902 }

CVE-2026-23902 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-23902) [\[CVE json\]](./CVE-2026-23902.cve.json) [\[OSV json\]](./CVE-2026-23902.osv.json)



_Last updated: 2026-04-24T10:56:16.919Z_

### Affected

* Apache DolphinScheduler before 3.4.1


### Description

<p>Incorrect Authorization vulnerability in Apache DolphinScheduler allows authenticated users with system login permissions to use tenants that are not defined on the platform during workflow execution.<br><br>This issue affects Apache DolphinScheduler versions prior to 3.4.1.&nbsp;</p><p>Users are recommended to upgrade to version 3.4.1, which fixes this issue.<br></p>

### References
* https://lists.apache.org/thread/hy4ntb2gys8150zfmnxhsd5ph0hoh7s9


### Credits
* Jihang Yu (reporter)


## Deserialization of untrusted data in RPC ## { #CVE-2025-62233 }

CVE-2025-62233 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-62233) [\[CVE json\]](./CVE-2025-62233.cve.json) [\[OSV json\]](./CVE-2025-62233.osv.json)



_Last updated: 2026-04-24T10:54:53.855Z_

### Affected

* Apache DolphinScheduler from 3.2.0 before 3.3.1


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache DolphinScheduler RPC module.</p><p>This issue affects Apache DolphinScheduler:&nbsp;</p><p>Version &gt;= 3.2.0 and &lt; 3.3.1.</p>Attackers who can access the Master or Worker nodes can compromise the system by creating a StandardRpcRequest, injecting a malicious class type into it, and sending RPC requests to the DolphinScheduler Master/Worker nodes.<br><p>Users are recommended to upgrade to version [3.3.1], which fixes the issue.</p>

### References
* https://lists.apache.org/thread/79s80h51r4z5d4l2xs5xy364rmmo1bw0


### Credits
* 75Acol, fcgboy, ch0wn, zer0duck (finder)


## Users can access sensitive information through the actuator endpoint. ## { #CVE-2025-62188 }

CVE-2025-62188 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-62188) [\[CVE json\]](./CVE-2025-62188.cve.json)

_Last updated: 2026-04-08T09:09:06.393Z_

### Affected

* Apache DolphinScheduler from 3.1.0 before 3.2.0


### Description

<p>An <strong>Exposure of Sensitive Information to an Unauthorized Actor</strong> vulnerability exists in Apache DolphinScheduler.<br>
This vulnerability may allow unauthorized actors to access sensitive information, including database credentials.</p>
<p>This issue affects <strong>Apache DolphinScheduler versions 3.1.*</strong>.</p>
<p>Users are recommended to upgrade to:<br></p>


<p></p><ul><li><strong>version ≥ 3.2.0</strong> if using <strong>3.1.x</strong></li></ul><p></p>

<p>As a temporary workaround, users who cannot upgrade immediately may restrict the exposed management endpoints by setting the following environment variable:</p>
```<br>MANAGEMENT_ENDPOINTS_WEB_EXPOSURE_INCLUDE=health,metrics,prometheus<br>```<br>
<p>Alternatively, add the following configuration to the <code>application.yaml</code> file:</p>
```<br>management:<br>&nbsp; &nbsp;endpoints:<br>&nbsp; &nbsp; &nbsp;web:<br>&nbsp; &nbsp; &nbsp; &nbsp; exposure:<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; include: health,metrics,prometheus<br>```<br>
<p>This issue has been reported as <strong>CVE-2023-48796</strong>:<br>
<a target="_blank" rel="nofollow" href="https://cveprocess.apache.org/cve5/CVE-2023-48796">https://cveprocess.apache.org/cve5/CVE-2023-48796</a></p><br>

### References
* https://lists.apache.org/thread/ffrmkcwgr2lcz0f5nnnyswhpn3fytsvo
* https://www.cve.org/CVERecord?id=CVE-2023-48796


### Credits
* w aiyou (finder)
* 魏大创 (reporter)


## Remote Code Execution Vulnerability ## { #CVE-2024-43202 }

CVE-2024-43202 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-43202) [\[CVE json\]](./CVE-2024-43202.cve.json) [\[OSV json\]](./CVE-2024-43202.osv.json)



_Last updated: 2024-08-20T07:29:41.648Z_

### Affected

* Apache DolphinScheduler from 3.0.0 before 3.2.2


### Description

Exposure of Remote Code Execution in Apache Dolphinscheduler.<br><br>This issue affects Apache DolphinScheduler: before 3.2.2. <br><br>We recommend users to upgrade Apache DolphinScheduler to version 3.2.2, which fixes the issue. 

### References
* https://github.com/apache/dolphinscheduler/pull/15758
* https://lists.apache.org/thread/nlmdp7q7l7o3l27778vxc5px24ncr5r5
* https://lists.apache.org/thread/qbhk9wqyxhrn4z7m4m343wqxpwg926nh
* https://www.cve.org/CVERecord?id=CVE-2023-49109


### Credits
* an4er (reporter)


## CWE-276 Incorrect Default Permissions ## { #CVE-2024-43166 }

CVE-2024-43166 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-43166) [\[CVE json\]](./CVE-2024-43166.cve.json) [\[OSV json\]](./CVE-2024-43166.osv.json)



_Last updated: 2025-09-18T09:38:13.985Z_

### Affected

* Apache DolphinScheduler before 3.2.2


### Description

<p>Incorrect Default Permissions vulnerability in Apache DolphinScheduler.</p><p>This issue affects Apache DolphinScheduler: before 3.2.2.</p><p>Users are recommended to upgrade to version <span style="background-color: rgb(255, 255, 255);">3.3.1</span>, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/8zd69zkkx55qp365xp4tml1xh9og5lhk


### Credits
* L0ne1y (reporter)


## Alert Script Attack ## { #CVE-2024-43115 }

CVE-2024-43115 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-43115) [\[CVE json\]](./CVE-2024-43115.cve.json) [\[OSV json\]](./CVE-2024-43115.osv.json)



_Last updated: 2025-09-03T08:38:26.012Z_

### Affected

* Apache DolphinScheduler before 3.2.2


### Description

<div>Improper Input Validation vulnerability in Apache DolphinScheduler. An <span style="background-color: rgb(255, 255, 255);">authenticated user can execute any shell script server by alert script.</span><br></div><p>This issue affects Apache DolphinScheduler: before 3.2.2.</p><p>Users are recommended to upgrade to version <span style="background-color: rgb(255, 255, 255);">3.3.1</span>, which fixes the issue.</p><br>

### References
* https://lists.apache.org/thread/qm36nrsv1vrr2j4o5q2wo75h3686hrnj


### Credits
* L0ne1y (reporter)


## Resource File Read And Write Vulnerability ## { #CVE-2024-30188 }

CVE-2024-30188 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-30188) [\[CVE json\]](./CVE-2024-30188.cve.json) [\[OSV json\]](./CVE-2024-30188.osv.json)



_Last updated: 2024-08-09T12:45:43.623Z_

### Affected

* Apache DolphinScheduler from 3.1.0 before 3.2.2


### Description

File read and write vulnerability in Apache DolphinScheduler ,&nbsp; authenticated users can illegally access additional resource files.<br><p>This issue affects Apache DolphinScheduler: from 3.1.0 before 3.2.2.</p><p>Users are recommended to upgrade to version 3.2.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/tbrt42mnr42bq6scxwt6bjr3s2pwyd07


### Credits
* L0ne1y (reporter)
* drun1baby (reporter)
* Zevi (reporter)
* Xun Bai (reporter)


## RCE by arbitrary js execution ## { #CVE-2024-29831 }

CVE-2024-29831 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-29831) [\[CVE json\]](./CVE-2024-29831.cve.json) [\[OSV json\]](./CVE-2024-29831.osv.json)



_Last updated: 2024-08-09T14:21:46.981Z_

### Affected

* Apache DolphinScheduler through 3.2.1


### Description

Improper Input Validation vulnerability in Apache DolphinScheduler. An <span style="background-color: rgb(255, 255, 255);">authenticated user can cause arbitrary, unsandboxed javascript to be executed on the server. If you are using the switch task plugin, please upgrade to version 3.2.2.<br></span>

### References
* https://lists.apache.org/thread/x1ch0x5om3srtbnp7rtsvdszho3mdrq0


### Credits
* yerest (reporter)
* L0ne1y (reporter)
* My Long (reporter)


## Arbitrary js execution as root for authenticated users ## { #CVE-2024-23320 }

CVE-2024-23320 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23320) [\[CVE json\]](./CVE-2024-23320.cve.json) [\[OSV json\]](./CVE-2024-23320.osv.json)



_Last updated: 2024-02-23T16:36:40.046Z_

### Affected

* Apache DolphinScheduler before 3.2.1


### Description

Improper Input Validation vulnerability in Apache DolphinScheduler. An <span style="background-color: rgb(255, 255, 255);">authenticated user can cause arbitrary, unsandboxed javascript to be executed on the server.<br></span><br><br>This issue is a legacy of CVE-2023-49299. We didn't fix it completely in CVE-2023-49299, and we added one more patch to fix it.<p><br></p><p>This issue affects Apache DolphinScheduler: until 3.2.1.</p><p><br></p><p>Users are recommended to upgrade to version 3.2.1, which fixes the issue.</p><br><br>

### References
* https://github.com/apache/dolphinscheduler/pull/15487
* https://lists.apache.org/thread/tnf99qoc6tlnwrny4t1zk6mfszgdsokm
* https://lists.apache.org/thread/25qhfvlksozzp6j9y8ozznvjdjp3lxqq
* https://lists.apache.org/thread/p7rwzdgrztdfps8x1bwx646f1mn0x6cp


### Credits
* xuesong.zhou (finder)
* Nbxiglk (finder)
* Huang Atao (finder)


## Arbitrary File Read Vulnerability ## { #CVE-2023-51770 }

CVE-2023-51770 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-51770) [\[CVE json\]](./CVE-2023-51770.cve.json) [\[OSV json\]](./CVE-2023-51770.osv.json)



_Last updated: 2024-02-20T06:00:50.765Z_

### Affected

* Apache DolphinScheduler from 1.2.0 before 3.2.1


### Description

Arbitrary File Read Vulnerability in Apache Dolphinscheduler.<br><br>This issue affects Apache DolphinScheduler: before 3.2.1. <br><br>We recommend users to upgrade Apache DolphinScheduler to version 3.2.1, which fixes the issue.

### References
* https://github.com/apache/dolphinscheduler/pull/15433
* https://lists.apache.org/thread/4t8bdjqnfhldh73gy9p0whlgvnnbtn7g
* https://lists.apache.org/thread/gpks573kn00ofxn7n9gkg6o47d03p5rw


### Credits
* zhiwei (finder)
* rg (finder)


## Session do not expire after password change ## { #CVE-2023-50270 }

CVE-2023-50270 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-50270) [\[CVE json\]](./CVE-2023-50270.cve.json)

_Last updated: 2024-02-23T10:17:33.021Z_

### Affected

* Apache DolphinScheduler from 1.3.8 through 3.2.0


### Description

Session Fixation Apache DolphinScheduler before version 3.2.0, which session is still valid after the password change.<br><br>Users are recommended to upgrade to version 3.2.1, which fixes this issue.

### References
* https://github.com/apache/dolphinscheduler/pull/15219
* https://lists.apache.org/thread/lmnf21obyos920dnvbfpwq29c1sd2r9r
* https://lists.apache.org/thread/94prw8hyk60vvw7s6cs3tr708qzqlwl6
* https://www.openwall.com/lists/oss-security/2024/02/20/3


### Credits
* lujiefsi (finder)
* Qing Xu (finder)


## Authenticated users could delete UDFs in resource center they were not authorized for ## { #CVE-2023-49620 }

CVE-2023-49620 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49620) [\[CVE json\]](./CVE-2023-49620.cve.json) [\[OSV json\]](./CVE-2023-49620.osv.json)



_Last updated: 2023-11-30T08:16:57.761Z_

### Affected

* Apache DolphinScheduler from 2.0.0 before 3.1.0


### Description

Before DolphinScheduler version 3.1.0, the login user could delete UDF function in the resource center unauthorized (which almost used in sql task), with&nbsp;unauthorized&nbsp;access vulnerability (IDOR), but after version 3.1.0 we fixed this issue. We mark this cve as moderate level because it still requires user login to operate, please upgrade to version 3.1.0 to avoid this&nbsp;vulnerability

### References
* https://github.com/apache/dolphinscheduler/pull/10307
* https://lists.apache.org/thread/zm4t1ykj4cro1c8183q7y32z0yzfz8yj


### Credits
* Yuanheng Lab of zhongfu (finder)


## Arbitrary js execute as root for authenticated users ## { #CVE-2023-49299 }

CVE-2023-49299 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49299) [\[CVE json\]](./CVE-2023-49299.cve.json) [\[OSV json\]](./CVE-2023-49299.osv.json)



_Last updated: 2023-12-30T16:30:14.065Z_

### Affected

* Apache DolphinScheduler before 3.1.9


### Description

Improper Input Validation vulnerability in Apache DolphinScheduler. An&nbsp;<span style="background-color: rgb(255, 255, 255);">authenticated user can cause arbitrary, unsandboxed javascript to be executed on the server.</span><p>This issue affects Apache DolphinScheduler: until 3.1.9.</p><p>Users are recommended to upgrade to version 3.1.9, which fixes the issue.</p>

### References
* https://github.com/apache/dolphinscheduler/pull/15228
* https://lists.apache.org/thread/tnf99qoc6tlnwrny4t1zk6mfszgdsokm


### Credits
* Eluen Siebene (finder)


## Insecure TLS TrustManager used in HttpUtil ## { #CVE-2023-49250 }

CVE-2023-49250 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49250) [\[CVE json\]](./CVE-2023-49250.cve.json) [\[OSV json\]](./CVE-2023-49250.osv.json)



_Last updated: 2024-02-20T05:59:07.770Z_

### Affected

* Apache DolphinScheduler through 3.2.0


### Description

<p><span style="background-color: rgb(255, 255, 255);">Because the HttpUtils class did not verify certificates, an attacker that could perform a Man-in-the-Middle (MITM) attack on outgoing https connections could impersonate the server.</span><br></p><p>This issue affects Apache DolphinScheduler: before 3.2.0.</p><p>Users are recommended to upgrade to version 3.2.1, which fixes the issue.</p><br>

### References
* https://github.com/apache/dolphinscheduler/pull/15288
* https://lists.apache.org/thread/wgs2jvhbmq8xnd6rmg0ymz73nyj7b3qn


## Remote Code Execution in Apache Dolphinscheduler ## { #CVE-2023-49109 }

CVE-2023-49109 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49109) [\[CVE json\]](./CVE-2023-49109.cve.json) [\[OSV json\]](./CVE-2023-49109.osv.json)



_Last updated: 2024-02-20T06:02:40.133Z_

### Affected

* Apache DolphinScheduler from 3.0.0 before 3.2.1


### Description

Exposure of Remote Code Execution in Apache Dolphinscheduler.<br><br>This issue affects Apache DolphinScheduler: before 3.2.1. <br><br>We recommend users to upgrade Apache DolphinScheduler to version 3.2.1, which fixes the issue. 

### References
* https://github.com/apache/dolphinscheduler/pull/14991
* https://lists.apache.org/thread/6kgsl93vtqlbdk6otttl0d8wmlspk0m5
* https://lists.apache.org/thread/5b6yq2gov0fsy9x5dkvo8ws4rr45vkn8


### Credits
* Y4tacker and 4ra1n from Y4secTeam (finder)


## Information Leakage Vulnerability ## { #CVE-2023-49068 }

CVE-2023-49068 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49068) [\[CVE json\]](./CVE-2023-49068.cve.json) [\[OSV json\]](./CVE-2023-49068.osv.json)



_Last updated: 2023-11-27T09:49:38.223Z_

### Affected

* Apache DolphinScheduler before 3.2.1


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache DolphinScheduler.<p>This issue affects Apache DolphinScheduler: before 3.2.1.<br></p><p>Users are recommended to upgrade to version 3.2.1, which fixes the issue. At the time of disclosure of this advisory, this version has not yet been released. In the mean time, we recommend you make sure the logs are only available to trusted operators.<br></p>

### References
* https://github.com/apache/dolphinscheduler/pull/15192
* https://lists.apache.org/thread/jn6kr6mjdgtfgpxoq9j8q4pkfsq8zmpq


### Credits
* Y4tacker and 4ra1n from Y4secTeam (finder)


## Sensitive information disclosure ## { #CVE-2023-48796 }

CVE-2023-48796 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-48796) [\[CVE json\]](./CVE-2023-48796.cve.json) [\[OSV json\]](./CVE-2023-48796.osv.json)



_Last updated: 2025-11-28T05:01:20.066Z_

### Affected

* Apache DolphinScheduler before < 3.0.2 and 3.1.0 < 3.2.0.


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache DolphinScheduler.<br><br>The information exposed to unauthorized actors may include sensitive data such as database credentials.<br><br>Users who can't upgrade to the fixed version can also set environment variable `MANAGEMENT_ENDPOINTS_WEB_EXPOSURE_INCLUDE=health,metrics,prometheus` to workaround this, or add the following section in the `application.yaml` file<br><br><br>```<br>management:<br>&nbsp; endpoints:<br>&nbsp; &nbsp; web:<br>&nbsp; &nbsp; &nbsp; exposure:<br>&nbsp; &nbsp; &nbsp; &nbsp; include: health,metrics,prometheus<br>```<br><p><br></p><p>This issue affects Apache DolphinScheduler: <span style="background-color: rgb(255, 255, 255);">&lt; 3.0.2 and&nbsp;<span style="background-color: rgb(255, 255, 255);">3.1.0 &lt; 3.2.0</span></span>.</p><p>Users are recommended to upgrade to version 3.0.6 or 3.3.2</p>

### References
* https://lists.apache.org/thread/ffrmkcwgr2lcz0f5nnnyswhpn3fytsvo


### Credits
* whobushibaby (finder)


## Apache DolphinScheduler 3.0.0 to 3.1.1 python gateway has improper authentication ## { #CVE-2023-25601 }

CVE-2023-25601 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25601) [\[CVE json\]](./CVE-2023-25601.cve.json) [\[OSV json\]](./CVE-2023-25601.osv.json)



_Last updated: 2023-04-20T15:06:54.846Z_

### Affected

* Apache DolphinScheduler from 3.0.0 before 3.1.2


### Description

On version 3.0.0 through 3.1.1, Apache DolphinScheduler's python gateway suffered from improper authentication: an attacker could use a socket bytes attack without authentication. This issue has been fixed from version 3.1.2 onwards. For users who use version 3.0.0 to 3.1.1, you can turn off the python-gateway function by changing the value `python-gateway.enabled=false` in configuration file `application.yaml`. If you are using the python gateway, please upgrade to version 3.1.2 or above.<br>

### References
* https://lists.apache.org/thread/25g77jqczp3t8cz56hk1p65q7m6c64rf


## Remote command execution Vulnerability in script alert plugin ## { #CVE-2022-45875 }

CVE-2022-45875 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-45875) [\[CVE json\]](./CVE-2022-45875.cve.json) [\[OSV json\]](./CVE-2022-45875.osv.json)



_Last updated: 2023-11-22T08:37:58.550Z_

### Affected

* Apache DolphinScheduler from 3.0 through 3.0.1
* Apache DolphinScheduler from 3.1 through 3.1.0


### Description

Improper validation of script alert plugin parameters in Apache DolphinScheduler to avoid remote command execution vulnerability.  This issue affects Apache DolphinScheduler version 3.0.1 and prior versions; version 3.1.0 and prior versions.<br><span style="background-color: rgb(255, 255, 255);">This attack can be performed only by authenticated users which can login to DS.</span><br><br>

### References
* https://lists.apache.org/thread/r0wqzkjsoq17j6ww381kmpx3jjp9hb6r


### Credits
* 4ra1n of Chaitin Tech (finder)


## Apache DolphinScheduler prior to 2.0.5 have command execution vulnerability ## { #CVE-2022-45462 }

CVE-2022-45462 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-45462) [\[CVE json\]](./CVE-2022-45462.cve.json) [\[OSV json\]](./CVE-2022-45462.osv.json)



_Last updated: 2022-11-23T02:24:20.816Z_

### Affected

* Apache DolphinScheduler from unspecified through 2.0.5


### Description

Alarm instance management has command injection when there is a specific command configured. It is only for logged-in users. We recommend you upgrade to version 2.0.6 or higher

### References
* https://lists.apache.org/thread/2f126y32bf1v3mvxkdgt2jr5j3l1t01w


### Credits
* This issue was discovered by Jigang Dong of M1QLin Security Team


## Apache DolphinScheduler prior to 3.0.0 allows path traversal ## { #CVE-2022-34662 }

CVE-2022-34662 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-34662) [\[CVE json\]](./CVE-2022-34662.cve.json) [\[OSV json\]](./CVE-2022-34662.osv.json)



_Last updated: 2022-11-01T15:28:47.599Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler through 3.0.0-beta-1


### Description

When users add resources to the resource center with a relation path will cause path traversal issues and only for logged-in users. You could upgrade to version 3.0.0 or higher

### References
* https://lists.apache.org/thread/pbdzqf9ntxyvs4cr0x2dgk9zlf43btz8


### Credits
* This issue was discovered by Jigang Dong of M1QLin Security Team


## Apache DolphinScheduler config file read by task risk ## { #CVE-2022-26885 }

CVE-2022-26885 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-26885) [\[CVE json\]](./CVE-2022-26885.cve.json) [\[OSV json\]](./CVE-2022-26885.osv.json)



_Last updated: 2022-11-24T11:55:57.562Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler before 2.0.6


### Description

When using tasks to read config files, there is a risk of database password disclosure.   We recommend you upgrade to version 2.0.6 or higher.

### References
* https://lists.apache.org/thread/z7084r9cs2r26cszkkgjqpb5bhnxqssp


## Apache DolphinScheduler exposes files without authentication ## { #CVE-2022-26884 }

CVE-2022-26884 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-26884) [\[CVE json\]](./CVE-2022-26884.cve.json) [\[OSV json\]](./CVE-2022-26884.osv.json)



_Last updated: 2022-10-28T01:44:55.028Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler before 2.0.6


### Description

Users can read any files by log server, Apache DolphinScheduler users should upgrade to version 2.0.6 or higher.

### References
* https://lists.apache.org/thread/xfdst5y4hnrm2ntmc5jzrgmw2htyyb9c


## Apache DolphinScheduler user registration is vulnerable to ReDoS attacks ## { #CVE-2022-25598 }

CVE-2022-25598 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-25598) [\[CVE json\]](./CVE-2022-25598.cve.json) [\[OSV json\]](./CVE-2022-25598.osv.json)



_Last updated: 2022-11-01T03:18:38.664Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler before 2.0.5


### Description

Apache DolphinScheduler user registration is vulnerable to Regular express Denial of Service (ReDoS) attacks, Apache DolphinScheduler users should upgrade to version 2.0.5 or higher.Uncontrolled Resource Consumption vulnerability in __COMPONENT__ of Apache DolphinScheduler allows an attacker to __IMPACT__.  This issue affects Apache DolphinScheduler Apache DolphinScheduler versions prior to 2.0.5.

### References
* https://lists.apache.org/thread/hwnw7xr969sg5nv84wz75nfr2c76fl93


### Credits
* This issue was discovered by Zheng Wang of HIT


## DolphinScheduler mysql jdbc connector parameters deserialize remote code execution ## { #CVE-2021-27644 }

CVE-2021-27644 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-27644) [\[CVE json\]](./CVE-2021-27644.cve.json) [\[OSV json\]](./CVE-2021-27644.osv.json)



_Last updated: 2021-11-01T09:12:08.670Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler before 1.3.6


### Description

In Apache DolphinScheduler before 1.3.6 versions, authorized users can use SQL injection in the data source center. (Only applicable to MySQL data source with internal login account password)


### References
* https://lists.apache.org/thread.html/r35d6acf021486a390a7ea09e6650c2fe19e72522bd484791d606a6e6%40%3Cdev.dolphinscheduler.apache.org%3E


### Credits
* This issue was discovered by Jinchen Sheng of Ant FG Security Lab


## Apache DolphinScheduler (incubating) Permission vulnerability ## { #CVE-2020-13922 }

CVE-2020-13922 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-13922) [\[CVE json\]](./CVE-2020-13922.cve.json) [\[OSV json\]](./CVE-2020-13922.osv.json)



_Last updated: 2021-01-11T09:18:42.255Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler before 1.3.2


### Description

Versions of Apache DolphinScheduler prior to 1.3.2 allowed an ordinary user under any tenant to override another users password through the API interface.

### References
* https://www.mail-archive.com/announce%40apache.org/msg06076.html


### Credits
* This issue was discovered by xuxiang of DtDream security
