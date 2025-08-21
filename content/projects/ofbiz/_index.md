---
title: Apache OFBiz security advisories
description: Security information for Apache OFBiz
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache OFBiz? You can read more about the projects' security policy on their [security page](https://ofbiz.apache.org/download.html#security), and email your report to the [Apache OFBiz Security Team](mailto:security@ofbiz.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://ofbiz.apache.org/download.html#security). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## RCE vulnerability in latest Apache OFBiz due to Java serialisation using RMI ## { #CVE-2021-26295 }

CVE-2021-26295 [\[CVE json\]](./CVE-2021-26295.cve.json) [\[OSV json\]](./CVE-2021-26295.osv.json)



_Last updated: 2021-03-22T11:54:40.746Z_

### Affected

* Apache OFBiz at 17.12.01 to 17.12.05


### Description

Apache OFBiz has unsafe deserialization prior to 17.12.06. An unauthenticated attacker can use this vulnerability to successfully take over Apache OFBiz.


### References
* https://lists.apache.org/thread.html/r3c1802eaf34aa78a61b4e8e044c214bc94accbd28a11f3a276586a31%40%3Cuser.ofbiz.apache.org%3E


### Credits
* Apache OFBiz would like to thank the first report from "r00t4dm at Cloud-Penetrating Arrow Lab and Longofo at Knownsec 404 Team" and the second report by MagicZero from SGLAB of Legendsec at Qi'anxin Group.


## RCE vulnerability in latest Apache OFBiz due to Java serialisation using RMI ## { #CVE-2021-29200 }

CVE-2021-29200 [\[CVE json\]](./CVE-2021-29200.cve.json) [\[OSV json\]](./CVE-2021-29200.osv.json)



_Last updated: 2021-04-27T19:46:30.140Z_

### Affected

* Apache OFBiz from Apache OFBiz before 17.12.07


### Description

Apache OFBiz has unsafe deserialization prior to 17.12.07 version
An unauthenticated user can perform an RCE attack


### References
* https://lists.apache.org/thread.html/re21d25d9fb89e36cea910633779c23f144b9b60596b113b7bf1e8097%40%3Cdev.ofbiz.apache.org%3E


### Credits
* Apache OFBiz would like to thank the first report from "r00t4dm at Cloud-Penetrating Arrow Lab, asd of MoyunSec V-Lab <root@thiscode.cc> and 赖涵 <1044309102@qq.com>  a bit later


## Unsafe deserialization in Apache OFBiz ## { #CVE-2021-30128 }

CVE-2021-30128 [\[CVE json\]](./CVE-2021-30128.cve.json) [\[OSV json\]](./CVE-2021-30128.osv.json)



_Last updated: 2021-04-27T19:47:04.244Z_

### Affected

* Apache OFBiz from Apache OFBiz before 17.12.07


### Description

Apache OFBiz has unsafe deserialization prior to 17.12.07 version

### References
* https://lists.apache.org/thread.html/rb3f5cd65f3ddce9b9eb4d6ea6e2919933f0f89b15953769d11003743%40%3Cdev.ofbiz.apache.org%3E


### Credits
* Apache OFBiz would like to thank Litch1 from the Security Team of Alibaba Cloud <litch1chk@gmail.com> for report


## Arbitrary file upload vulnerability in OFBiz ## { #CVE-2021-37608 }

CVE-2021-37608 [\[CVE json\]](./CVE-2021-37608.cve.json) [\[OSV json\]](./CVE-2021-37608.osv.json)



_Last updated: 2021-08-18T07:45:08.867Z_

### Affected

* Apache OFBiz from unspecified through 17.12.07


### Description

Unrestricted Upload of File with Dangerous Type vulnerability in Apache OFBiz allows an attacker to execute remote commands. This issue affects Apache OFBiz version 17.12.07 and prior versions. Upgrade to at least 17.12.08 or apply patches at https://issues.apache.org/jira/browse/OFBIZ-12297.

### References
* https://ofbiz.apache.org/security.html


### Credits
* Zhujie from Galaxy Security Laboratory <galaxylab@sina.com>


## Unauth Stored XSS vulnerability in the Birt plugin of Apache OFBiz ## { #CVE-2022-25370 }

CVE-2022-25370 [\[CVE json\]](./CVE-2022-25370.cve.json) [\[OSV json\]](./CVE-2022-25370.osv.json)



_Last updated: 2022-09-02T06:58:56.611Z_

### Affected

* Apache OFBiz from Apache OFBiz through 18.12.05


### Description

Apache OFBiz uses the Birt plugin (https://eclipse.github.io/birt-website/) to create data visualizations and reports.
In Apache OFBiz release 18.12.05, and earlier versions, by leveraging a vulnerability in Birt (https://bugs.eclipse.org/bugs/show_bug.cgi?id=538142), an unauthenticated malicious user could perform a stored XSS attack in order to inject a malicious payload and execute it using the stored XSS.


### References
* https://lists.apache.org/thread/vrvzokvxqtc4t6d7g8xgz89xpxcvjofh


### Credits
* Nikita Podotykin from Positive Technologies <npodotykin@ptsecurity.com>
* Positive Technologies  zeroday <zeroday@ptsecurity.com>


## Unauth Path Traversal with file corruption affecting the Birt plugin of Apache OFBiz ## { #CVE-2022-25371 }

CVE-2022-25371 [\[CVE json\]](./CVE-2022-25371.cve.json) [\[OSV json\]](./CVE-2022-25371.osv.json)



_Last updated: 2022-09-02T07:00:04.371Z_

### Affected

* Apache OFBiz from Apache OFBiz through 18.12.05


### Description

Apache OFBiz uses the Birt project plugin (https://eclipse.github.io/birt-website/) to create data visualizations and reports.
By leveraging a bug in Birt (https://bugs.eclipse.org/bugs/show_bug.cgi?id=538142) it is possible to perform a remote code execution (RCE) attack in Apache OFBiz, release 18.12.05 and earlier.


### References
* https://lists.apache.org/thread/bvp3sczqq863lxr1wh7wjvdtjbkcwspq


### Credits
* Nikita Podotykin from Positive Technologies <npodotykin@ptsecurity.com>
* Positive Technologies  zeroday <zeroday@ptsecurity.com>


## Server-Side Template Injection affecting the ecommerce plugin of Apache OFBiz ## { #CVE-2022-25813 }

CVE-2022-25813 [\[CVE json\]](./CVE-2022-25813.cve.json) [\[OSV json\]](./CVE-2022-25813.osv.json)



_Last updated: 2022-09-02T07:01:21.926Z_

### Affected

* Apache OFBiz from Apache OFBiz through 18.12.05


### Description

In Apache OFBiz, versions 18.12.05 and earlier, an attacker acting as an anonymous user of the ecommerce plugin, can insert a malicious content in a message “Subject” field from the "Contact us" page. Then a party
manager needs to list the communications in the party component to activate the SSTI. A RCE is then possible.

### References
* https://lists.apache.org/thread/vmj5s0qb59t0lvzf3vol3z1sc3sgyb2b


### Credits
*  Matei "Mal" Badanoiu


## Java Deserialization via RMI Connection from the Solr plugin of Apache OFBiz ## { #CVE-2022-29063 }

CVE-2022-29063 [\[CVE json\]](./CVE-2022-29063.cve.json) [\[OSV json\]](./CVE-2022-29063.osv.json)



_Last updated: 2022-09-02T07:04:01.683Z_

### Affected

* Apache OFBiz from Apache OFBiz through 18.12.05


### Description

The Solr plugin of Apache OFBiz is configured by default to automatically make a RMI request on localhost, port 1099. In version 18.12.05 and earlier, by hosting a malicious RMI server on localhost, an attacker may exploit this behavior, at server start-up or on a server restart, in order to run arbitrary code.
Upgrade to at least 18.12.06 or apply patches at https://issues.apache.org/jira/browse/OFBIZ-12646.

### References
* https://lists.apache.org/thread/ytzrjc16pf357zntwk8tjby13kbx9105


### Credits
* Matei "Mal" Badanoiu


## Regular Expression Denial of Service (ReDoS) vulnerability in Apache OFBiz ## { #CVE-2022-29158 }

CVE-2022-29158 [\[CVE json\]](./CVE-2022-29158.cve.json) [\[OSV json\]](./CVE-2022-29158.osv.json)



_Last updated: 2022-09-02T07:05:27.871Z_

### Affected

* Apache OFBiz from Apache OFBiz through 18.12.05


### Description

Apache OFBiz up to version 18.12.05 is vulnerable to Regular Expression Denial of Service (ReDoS) in the way it handles URLs provided by external, unauthenticated users.
Upgrade to 18.12.06 or apply patches at https://issues.apache.org/jira/browse/OFBIZ-12599

### References
* https://lists.apache.org/thread/7k92rg1o4ql2yw3o0vttkcl2jhq7j928


### Credits
* Tony Torralba and Joseph Farebrother from the GitHub CodeQL team.


## Arbitrary file reading vulnerability ## { #CVE-2022-47501 }

CVE-2022-47501 [\[CVE json\]](./CVE-2022-47501.cve.json) [\[OSV json\]](./CVE-2022-47501.osv.json)



_Last updated: 2023-04-14T15:00:25.628Z_

### Affected

* Apache OFBiz from 18.12.06 before 18.12.07


### Description

Arbitrary file reading vulnerability in Apache Software Foundation Apache OFBiz when using the Solr plugin. This is a&nbsp;
pre-authentication attack.<br><p>This issue affects Apache OFBiz: before 18.12.07.</p>

### References
* https://lists.apache.org/thread/k8s76l0whydy45bfm4b69vq0mf94p3wc
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html


### Credits
* Skay <lhcaomail@gmail.com> (finder)


## Execution of Solr plugin queries without authentication ## { #CVE-2023-46819 }

CVE-2023-46819 [\[CVE json\]](./CVE-2023-46819.cve.json) [\[OSV json\]](./CVE-2023-46819.osv.json)



_Last updated: 2023-12-04T16:11:06.466Z_

### Affected

* Apache OFBiz before 18.12.09


### Description

Missing Authentication in Apache Software Foundation Apache OFBiz when using the Solr plugin.<br><p>This issue affects Apache OFBiz: before 18.12.09.&nbsp;

<span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 18.12.09</span></p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.09.html
* https://lists.apache.org/thread/mm5j0rsbl22q7yb0nmb6h2swbfjbwv99


### Credits
* Anonymous by demand (finder)


## Pre-auth RCE in Apache Ofbiz 18.12.09 due to XML-RPC still present ## { #CVE-2023-49070 }

CVE-2023-49070 [\[CVE json\]](./CVE-2023-49070.cve.json) [\[OSV json\]](./CVE-2023-49070.osv.json)



_Last updated: 2023-12-20T10:48:11.952Z_

### Affected

* Apache OFBiz before 18.12.10


### Description



Pre-auth RCE in Apache Ofbiz 18.12.09.<br><br>It's due to XML-RPC&nbsp;<span style="background-color: rgb(255, 255, 255);">no longer maintained</span>&nbsp;still present.<br><p>This issue affects Apache OFBiz: before 18.12.10.&nbsp;<br><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 18.12.10</span></p>



### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.10.html
* https://issues.apache.org/jira/browse/OFBIZ-12812
* https://lists.apache.org/thread/jmbqk2lp4t4483whzndp5xqlq4f3otg3


### Credits
* Siebene@ (finder)


## Arbitrary file properties reading and SSRF attack ## { #CVE-2023-50968 }

CVE-2023-50968 [\[CVE json\]](./CVE-2023-50968.cve.json) [\[OSV json\]](./CVE-2023-50968.osv.json)



_Last updated: 2023-12-26T10:21:57.552Z_

### Affected

* Apache OFBiz through 18.12.10


### Description

<div>Arbitrary file properties reading vulnerability in Apache Software Foundation Apache OFBiz when user operates an uri call without authorizations.<br></div><div><br></div><div>The same uri can be operated to realize a SSRF attack also  without  authorizations.<br></div><div><br></div>Users are recommended to upgrade to version 18.12.11, which fixes this issue.

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.11.html
* https://issues.apache.org/jira/browse/OFBIZ-12875
* https://lists.apache.org/thread/x5now4bk3llwf3k58kl96qvtjyxwp43q


### Credits
* Yun Peng - 郭 运鹏 <puata123@outlook.com> (finder)


## Pre-authentication Remote Code Execution (RCE) vulnerability ## { #CVE-2023-51467 }

CVE-2023-51467 [\[CVE json\]](./CVE-2023-51467.cve.json) [\[OSV json\]](./CVE-2023-51467.osv.json)



_Last updated: 2024-02-02T10:13:56.898Z_

### Affected

* Apache OFBiz before 18.12.11


### Description

<div><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">The vulnerability permits attackers to circumvent authentication processes, enabling them to remotely <span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">execute arbitrary code</span></span><br></span></span></div>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.11.html
* https://issues.apache.org/jira/browse/OFBIZ-12873
* https://lists.apache.org/thread/9tmf9qyyhgh6m052rhz7lg9vxn390bdv
* https://lists.apache.org/thread/oj2s6objhdq72t6g29omqpcbd1wlp48o
* https://www.openwall.com/lists/oss-security/2023/12/26/3


### Credits
* Hasib Vhora, Senior Threat Researcher, SonicWall  (finder)
* Gao Tian (finder)
* L0ne1y (finder)


## Path traversal or file inclusion ## { #CVE-2024-23946 }

CVE-2024-23946 [\[CVE json\]](./CVE-2024-23946.cve.json) [\[OSV json\]](./CVE-2024-23946.osv.json)



_Last updated: 2024-02-28T15:44:32.259Z_

### Affected

* Apache OFBiz before 18.12.12


### Description

Possible path traversal in Apache OFBiz allowing file inclusion.<br>Users are recommended to upgrade to version 18.12.12, that fixes the issue.

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.12.html
* https://issues.apache.org/jira/browse/OFBIZ-12884
* https://lists.apache.org/thread/w4lp5ncpzttf41hn5bsc04mzq4o6lw3g


### Credits
* Arun Shaji from trendmicro.com (finder)


## Path traversal allowing authentication bypass. ## { #CVE-2024-25065 }

CVE-2024-25065 [\[CVE json\]](./CVE-2024-25065.cve.json) [\[OSV json\]](./CVE-2024-25065.osv.json)



_Last updated: 2024-02-28T15:42:48.263Z_

### Affected

* Apache OFBiz before 18.12.12


### Description



Possible path traversal in Apache OFBiz allowing authentication bypass.<br>Users are recommended to upgrade to version 18.12.12, that fixes the issue.



### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.12.html
* https://issues.apache.org/jira/browse/OFBIZ-12887
* https://lists.apache.org/thread/rplfjp7ppn9ro49oo7jsrpj99m113lfc


### Credits
* YunPeng - 郭 运鹏 <puata123@outlook.com> (finder)


## Path traversal leading to RCE ## { #CVE-2024-32113 }

CVE-2024-32113 [\[CVE json\]](./CVE-2024-32113.cve.json) [\[OSV json\]](./CVE-2024-32113.osv.json)



_Last updated: 2024-05-08T14:49:53.237Z_

### Affected

* Apache OFBiz before 18.12.13


### Description

Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache OFBiz.<p>This issue affects Apache OFBiz: before 18.12.13.</p><p>Users are recommended to upgrade to version 18.12.13, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13006
* https://lists.apache.org/thread/w6s60okgkxp2th1sr8vx0ndmgk68fqrd


### Credits
* Qiyi Zhang (RacerZ) @secsys from Fudan (finder)


## Path traversal leading to a RCE ## { #CVE-2024-36104 }

CVE-2024-36104 [\[CVE json\]](./CVE-2024-36104.cve.json) [\[OSV json\]](./CVE-2024-36104.osv.json)



_Last updated: 2024-06-03T06:55:24.928Z_

### Affected

* Apache OFBiz before 18.12.14


### Description

Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache OFBiz.&nbsp;<p>This issue affects Apache OFBiz: before 18.12.14.</p><p>Users are recommended to upgrade to version 18.12.14, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13092
* https://lists.apache.org/thread/sv0xr8b1j7mmh5p37yldy9vmnzbodz2o


### Credits
* godspeed (AAA@ZJU) (finder)


## Unauthenticated endpoint could allow execution of screen rendering code ## { #CVE-2024-38856 }

CVE-2024-38856 [\[CVE json\]](./CVE-2024-38856.cve.json) [\[OSV json\]](./CVE-2024-38856.osv.json)



_Last updated: 2024-08-05T08:20:16.193Z_

### Affected

* Apache OFBiz through 18.12.14


### Description

<p>Incorrect Authorization vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: through 18.12.14.</p><p>Users are recommended to upgrade to version 18.12.15, which fixes the issue.</p>Unauthenticated endpoints could allow execution of screen rendering code of screens if some preconditions are met (such as when the screen definitions don't explicitly check user's permissions because they rely on the configuration of their endpoints).<br>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://lists.apache.org/thread/olxxjk6b13sl3wh9cmp0k2dscvp24l7w
* https://issues.apache.org/jira/browse/OFBIZ-13128


### Credits
* unam4 (finder)
* ruozhi (finder)
* m1sn0w (finder)
* kuiplatain (finder)
* PaperPen@Timeline Sec (finder)
* RacerZ (finder)
* e0mlja (finder)
* Donghyun (finder)
* 4ra1n (finder)
* godspeed (finder)
* Hasib Vhora (finder)
* pwnull (finder)
* blckder02-YHLab (finder)
* Xenc from SGLAB of Legendsec at Qi'anxin Group (finder)
* Nicholas Zubrisky. (finder)
* Y4tacker  (finder)


## Confused controller-view authorization logic (forced browsing) ## { #CVE-2024-45195 }

CVE-2024-45195 [\[CVE json\]](./CVE-2024-45195.cve.json) [\[OSV json\]](./CVE-2024-45195.osv.json)



_Last updated: 2024-09-04T08:08:57.418Z_

### Affected

* Apache OFBiz before 18.12.16


### Description

<p>Direct Request ('Forced Browsing') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 18.12.16.</p><p>Users are recommended to upgrade to version 18.12.16, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13130
* https://lists.apache.org/thread/o90dd9lbk1hh3t2557t2y2qvrh92p7wy


### Credits
* shin24 from National Cyber Security Vietnam (finder)
* LuanPV from National Cyber Security Vietnam (finder)
* Ryan Emmons, Lead Security Researcher at Rapid7 (finder)
* Hasib Vhora, Senior Threat Researcher, SonicWall (finder)
* Xenc from SGLAB of Legendsec at Qi'anxin Group (finder)


## Prevent use of URLs in files when loading them from Java or Groovy, leading to a RCE ## { #CVE-2024-45507 }

CVE-2024-45507 [\[CVE json\]](./CVE-2024-45507.cve.json) [\[OSV json\]](./CVE-2024-45507.osv.json)



_Last updated: 2024-09-04T08:08:31.094Z_

### Affected

* Apache OFBiz before 18.12.16


### Description

<p>Server-Side Request Forgery (SSRF), Improper Control of Generation of Code ('Code Injection') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 18.12.16.</p><p>Users are recommended to upgrade to version 18.12.16, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13132
* https://lists.apache.org/thread/o90dd9lbk1hh3t2557t2y2qvrh92p7wy


### Credits
* 孙相 (Sun Xiang) (finder)


## URLs allowing remote use of Groovy expressions, leading to RCE ## { #CVE-2024-47208 }

CVE-2024-47208 [\[CVE json\]](./CVE-2024-47208.cve.json) [\[OSV json\]](./CVE-2024-47208.osv.json)



_Last updated: 2024-11-18T08:43:11.961Z_

### Affected

* Apache OFBiz before 18.12.17


### Description

<p>Server-Side Request Forgery (SSRF), Improper Control of Generation of Code ('Code Injection') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 18.12.17.</p><p>Users are recommended to upgrade to version 18.12.17, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13158
* https://lists.apache.org/thread/022r19skfofhv3lzql33vowlrvqndh11


### Credits
* 孙相 (Sun Xiang) (finder)


## Bypass SameSite restrictions with target redirection using URL parameters (SSTI and CSRF leading to RCE) ## { #CVE-2024-48962 }

CVE-2024-48962 [\[CVE json\]](./CVE-2024-48962.cve.json) [\[OSV json\]](./CVE-2024-48962.osv.json)



_Last updated: 2025-02-17T11:17:10.834Z_

### Affected

* Apache OFBiz before 18.12.17


### Description

<p>Improper Control of Generation of Code ('Code Injection'), Cross-Site Request Forgery (CSRF), : Improper Neutralization of Special Elements Used in a Template Engine vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 18.12.17.</p><p>Users are recommended to upgrade to version 18.12.17, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13162
* https://lists.apache.org/thread/6sddh4pts90cp8ktshqb4xykdp6lb6q6


### Credits
* Sebastiano Sartor <s@sebsrt.xyz> (finder)
* Ryan <marimoo.eth@gmail.com> (finder)


## Server-Side Template Injection affecting the ecommerce plugin leading to possible RCE ## { #CVE-2025-26865 }

CVE-2025-26865 [\[CVE json\]](./CVE-2025-26865.cve.json) [\[OSV json\]](./CVE-2025-26865.osv.json)



_Last updated: 2025-03-10T14:00:48.257Z_

### Affected

* Apache OFBiz from 18.12.17 before 18.12.18


### Description

<p>Improper Neutralization of Special Elements Used in a Template Engine vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: from 18.12.17 before 18.12.18.&nbsp;&nbsp;</p>It's a regression between 18.12.17 and 18.12.18.<br>In case you use something like that, which is not recommended!<br>For security, only official releases should be used.<br><br>In other words, if you use 18.12.17 you are still safe.<br>The version 18.12.17 is not a affected.<br>But something between 18.12.17 and 18.12.18 is.<br><br>In that case, users are recommended to upgrade to version 18.12.18, which fixes the issue.<br>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-12594
* https://lists.apache.org/thread/prb48ztk01bflyyjbl6p56wlcc1n5sz7


### Credits
* Matei "Mal" Badanoiu (finder)


## Stored XSS Vulnerability ## { #CVE-2025-30676 }

CVE-2025-30676 [\[CVE json\]](./CVE-2025-30676.cve.json) [\[OSV json\]](./CVE-2025-30676.osv.json)



_Last updated: 2025-04-01T14:43:47.266Z_

### Affected

* Apache OFBiz before 18.12.19


### Description

<p>Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 18.12.19.</p><p>Users are recommended to upgrade to version 18.12.19, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13219
* https://lists.apache.org/thread/8d718qt8dqthnw1gmyxsq8glfdjklnjf


### Credits
* Khaled Nassar  (@mindpatch) (finder)


## RCE Vulnerability in scrum plugin ## { #CVE-2025-54466 }

CVE-2025-54466 [\[CVE json\]](./CVE-2025-54466.cve.json) [\[OSV json\]](./CVE-2025-54466.osv.json)



_Last updated: 2025-08-15T14:13:40.046Z_

### Affected

* Apache OFBiz before 24.09.02


### Description

<p>Improper Control of Generation of Code ('Code Injection') vulnerability leading to a possible RCE in Apache OFBiz&nbsp;scrum plugin.<br><br>This issue affects Apache OFBiz: before 24.09.02 only when the&nbsp;scrum plugin is used.</p><p>Even unauthenticated attackers can exploit this vulnerability.<br></p><p>Users are recommended to upgrade to version 24.09.02, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-24.09.02.html
* https://issues.apache.org/jira/browse/OFBIZ-13276
* https://lists.apache.org/thread/14d0yd9co9gx2mctd3vyz1cc8d39n915


### Credits
* Teeramet Eakwilai <teeramet@datafarm.co.th> (finder)
* Thanasin Luangpipat (finder)
* Jarukit Auikritskul (finder)
