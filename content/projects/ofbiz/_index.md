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

CVE-2021-26295 [\[CVE json\]](./CVE-2021-26295.cve.json)

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

CVE-2021-29200 [\[CVE json\]](./CVE-2021-29200.cve.json)

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

CVE-2021-30128 [\[CVE json\]](./CVE-2021-30128.cve.json)

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

CVE-2021-37608 [\[CVE json\]](./CVE-2021-37608.cve.json)

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

CVE-2022-25370 [\[CVE json\]](./CVE-2022-25370.cve.json)

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

CVE-2022-25371 [\[CVE json\]](./CVE-2022-25371.cve.json)

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

CVE-2022-25813 [\[CVE json\]](./CVE-2022-25813.cve.json)

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

CVE-2022-29063 [\[CVE json\]](./CVE-2022-29063.cve.json)

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

CVE-2022-29158 [\[CVE json\]](./CVE-2022-29158.cve.json)

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

CVE-2022-47501 [\[CVE json\]](./CVE-2022-47501.cve.json)

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

CVE-2023-46819 [\[CVE json\]](./CVE-2023-46819.cve.json)

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

CVE-2023-49070 [\[CVE json\]](./CVE-2023-49070.cve.json)

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

CVE-2023-50968 [\[CVE json\]](./CVE-2023-50968.cve.json)

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

CVE-2023-51467 [\[CVE json\]](./CVE-2023-51467.cve.json)

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
