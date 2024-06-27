---
title: Apache DolphinScheduler security advisories
description: Security information for Apache DolphinScheduler
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache DolphinScheduler? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache DolphinScheduler (incubating) Permission vulnerability ## { #CVE-2020-13922 }

CVE-2020-13922 [\[CVE json\]](./CVE-2020-13922.cve.json) [\[OSV json\]](./CVE-2020-13922.osv.json)



_Last updated: 2021-01-11T09:18:42.255Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler before 1.3.2


### Description

Versions of Apache DolphinScheduler prior to 1.3.2 allowed an ordinary user under any tenant to override another users password through the API interface.

### References
* https://www.mail-archive.com/announce%40apache.org/msg06076.html


### Credits
* This issue was discovered by xuxiang of DtDream security


## DolphinScheduler mysql jdbc connector parameters deserialize remote code execution ## { #CVE-2021-27644 }

CVE-2021-27644 [\[CVE json\]](./CVE-2021-27644.cve.json) [\[OSV json\]](./CVE-2021-27644.osv.json)



_Last updated: 2021-11-01T09:12:08.670Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler before 1.3.6


### Description

In Apache DolphinScheduler before 1.3.6 versions, authorized users can use SQL injection in the data source center. (Only applicable to MySQL data source with internal login account password)


### References
* https://lists.apache.org/thread.html/r35d6acf021486a390a7ea09e6650c2fe19e72522bd484791d606a6e6%40%3Cdev.dolphinscheduler.apache.org%3E


### Credits
* This issue was discovered by Jinchen Sheng of Ant FG Security Lab


## Apache DolphinScheduler user registration is vulnerable to ReDoS attacks ## { #CVE-2022-25598 }

CVE-2022-25598 [\[CVE json\]](./CVE-2022-25598.cve.json) [\[OSV json\]](./CVE-2022-25598.osv.json)



_Last updated: 2022-11-01T03:18:38.664Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler before 2.0.5


### Description

Apache DolphinScheduler user registration is vulnerable to Regular express Denial of Service (ReDoS) attacks, Apache DolphinScheduler users should upgrade to version 2.0.5 or higher.Uncontrolled Resource Consumption vulnerability in __COMPONENT__ of Apache DolphinScheduler allows an attacker to __IMPACT__.  This issue affects Apache DolphinScheduler Apache DolphinScheduler versions prior to 2.0.5.

### References
* https://lists.apache.org/thread/hwnw7xr969sg5nv84wz75nfr2c76fl93


### Credits
* This issue was discovered by Zheng Wang of HIT


## Apache DolphinScheduler exposes files without authentication ## { #CVE-2022-26884 }

CVE-2022-26884 [\[CVE json\]](./CVE-2022-26884.cve.json) [\[OSV json\]](./CVE-2022-26884.osv.json)



_Last updated: 2022-10-28T01:44:55.028Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler before 2.0.6


### Description

Users can read any files by log server, Apache DolphinScheduler users should upgrade to version 2.0.6 or higher.

### References
* https://lists.apache.org/thread/xfdst5y4hnrm2ntmc5jzrgmw2htyyb9c


## Apache DolphinScheduler config file read by task risk ## { #CVE-2022-26885 }

CVE-2022-26885 [\[CVE json\]](./CVE-2022-26885.cve.json) [\[OSV json\]](./CVE-2022-26885.osv.json)



_Last updated: 2022-11-24T11:55:57.562Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler before 2.0.6


### Description

When using tasks to read config files, there is a risk of database password disclosure.   We recommend you upgrade to version 2.0.6 or higher.

### References
* https://lists.apache.org/thread/z7084r9cs2r26cszkkgjqpb5bhnxqssp


## Apache DolphinScheduler prior to 3.0.0 allows path traversal ## { #CVE-2022-34662 }

CVE-2022-34662 [\[CVE json\]](./CVE-2022-34662.cve.json) [\[OSV json\]](./CVE-2022-34662.osv.json)



_Last updated: 2022-11-01T15:28:47.599Z_

### Affected

* Apache DolphinScheduler from Apache DolphinScheduler through 3.0.0-beta-1


### Description

When users add resources to the resource center with a relation path will cause path traversal issues and only for logged-in users. You could upgrade to version 3.0.0 or higher

### References
* https://lists.apache.org/thread/pbdzqf9ntxyvs4cr0x2dgk9zlf43btz8


### Credits
* This issue was discovered by Jigang Dong of M1QLin Security Team


## Apache DolphinScheduler prior to 2.0.5 have command execution vulnerability ## { #CVE-2022-45462 }

CVE-2022-45462 [\[CVE json\]](./CVE-2022-45462.cve.json) [\[OSV json\]](./CVE-2022-45462.osv.json)



_Last updated: 2022-11-23T02:24:20.816Z_

### Affected

* Apache DolphinScheduler from unspecified through 2.0.5


### Description

Alarm instance management has command injection when there is a specific command configured. It is only for logged-in users. We recommend you upgrade to version 2.0.6 or higher

### References
* https://lists.apache.org/thread/2f126y32bf1v3mvxkdgt2jr5j3l1t01w


### Credits
* This issue was discovered by Jigang Dong of M1QLin Security Team


## Remote command execution Vulnerability in script alert plugin ## { #CVE-2022-45875 }

CVE-2022-45875 [\[CVE json\]](./CVE-2022-45875.cve.json) [\[OSV json\]](./CVE-2022-45875.osv.json)



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


## Apache DolphinScheduler 3.0.0 to 3.1.1 python gateway has improper authentication ## { #CVE-2023-25601 }

CVE-2023-25601 [\[CVE json\]](./CVE-2023-25601.cve.json) [\[OSV json\]](./CVE-2023-25601.osv.json)



_Last updated: 2023-04-20T15:06:54.846Z_

### Affected

* Apache DolphinScheduler from 3.0.0 before 3.1.2


### Description

On version 3.0.0 through 3.1.1, Apache DolphinScheduler's python gateway suffered from improper authentication: an attacker could use a socket bytes attack without authentication. This issue has been fixed from version 3.1.2 onwards. For users who use version 3.0.0 to 3.1.1, you can turn off the python-gateway function by changing the value `python-gateway.enabled=false` in configuration file `application.yaml`. If you are using the python gateway, please upgrade to version 3.1.2 or above.<br>

### References
* https://lists.apache.org/thread/25g77jqczp3t8cz56hk1p65q7m6c64rf


## Apache dolphinscheduler sensitive information disclosure ## { #CVE-2023-48796 }

CVE-2023-48796 [\[CVE json\]](./CVE-2023-48796.cve.json) [\[OSV json\]](./CVE-2023-48796.osv.json)



_Last updated: 2023-11-24T07:56:40.315Z_

### Affected

* Apache DolphinScheduler from 3.0.0 before 3.0.2


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache DolphinScheduler.<br><br>The information exposed to unauthorized actors may include sensitive data such as database credentials.<br><br>Users who can't upgrade to the fixed version can also set environment variable `MANAGEMENT_ENDPOINTS_WEB_EXPOSURE_INCLUDE=health,metrics,prometheus` to workaround this, or add the following section in the `application.yaml` file<br><br><br>```<br>management:<br>&nbsp; endpoints:<br>&nbsp; &nbsp; web:<br>&nbsp; &nbsp; &nbsp; exposure:<br>&nbsp; &nbsp; &nbsp; &nbsp; include: health,metrics,prometheus<br>```<br><p><br></p><p>This issue affects Apache DolphinScheduler: from 3.0.0 before 3.0.2.</p><p>Users are recommended to upgrade to version 3.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ffrmkcwgr2lcz0f5nnnyswhpn3fytsvo


## Information Leakage Vulnerability ## { #CVE-2023-49068 }

CVE-2023-49068 [\[CVE json\]](./CVE-2023-49068.cve.json) [\[OSV json\]](./CVE-2023-49068.osv.json)



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


## Remote Code Execution in Apache Dolphinscheduler ## { #CVE-2023-49109 }

CVE-2023-49109 [\[CVE json\]](./CVE-2023-49109.cve.json) [\[OSV json\]](./CVE-2023-49109.osv.json)



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


## Insecure TLS TrustManager used in HttpUtil ## { #CVE-2023-49250 }

CVE-2023-49250 [\[CVE json\]](./CVE-2023-49250.cve.json) [\[OSV json\]](./CVE-2023-49250.osv.json)



_Last updated: 2024-02-20T05:59:07.770Z_

### Affected

* Apache DolphinScheduler through 3.2.0


### Description

<p><span style="background-color: rgb(255, 255, 255);">Because the HttpUtils class did not verify certificates, an attacker that could perform a Man-in-the-Middle (MITM) attack on outgoing https connections could impersonate the server.</span><br></p><p>This issue affects Apache DolphinScheduler: before 3.2.0.</p><p>Users are recommended to upgrade to version 3.2.1, which fixes the issue.</p><br>

### References
* https://github.com/apache/dolphinscheduler/pull/15288
* https://lists.apache.org/thread/wgs2jvhbmq8xnd6rmg0ymz73nyj7b3qn


## Arbitrary js execute as root for authenticated users ## { #CVE-2023-49299 }

CVE-2023-49299 [\[CVE json\]](./CVE-2023-49299.cve.json) [\[OSV json\]](./CVE-2023-49299.osv.json)



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


## Authenticated users could delete UDFs in resource center they were not authorized for ## { #CVE-2023-49620 }

CVE-2023-49620 [\[CVE json\]](./CVE-2023-49620.cve.json) [\[OSV json\]](./CVE-2023-49620.osv.json)



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


## Session do not expire after password change ## { #CVE-2023-50270 }

CVE-2023-50270 [\[CVE json\]](./CVE-2023-50270.cve.json)

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


## Arbitrary File Read Vulnerability ## { #CVE-2023-51770 }

CVE-2023-51770 [\[CVE json\]](./CVE-2023-51770.cve.json) [\[OSV json\]](./CVE-2023-51770.osv.json)



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


## Arbitrary js execution as root for authenticated users ## { #CVE-2024-23320 }

CVE-2024-23320 [\[CVE json\]](./CVE-2024-23320.cve.json) [\[OSV json\]](./CVE-2024-23320.osv.json)



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
