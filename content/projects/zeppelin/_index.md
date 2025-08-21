---
title: Apache Zeppelin security advisories
description: Security information for Apache Zeppelin
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Zeppelin? You can read more about the projects' security policy on their [security page](https://zeppelin.apache.org/security.html), and email your report to the [Apache Zeppelin Security Team](mailto:security@zeppelin.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://zeppelin.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## bash command injection in spark interpreter ## { #CVE-2019-10095 }

CVE-2019-10095 [\[CVE json\]](./CVE-2019-10095.cve.json) [\[OSV json\]](./CVE-2019-10095.osv.json)



_Last updated: 2022-12-08T11:51:05.587Z_

### Affected

* Apache Zeppelin from Apache Zeppelin through 0.9.0


### Description

bash command injection vulnerability in Apache Zeppelin allows an attacker to inject system commands into Spark interpreter settings.  This issue affects Apache Zeppelin Apache Zeppelin version 0.9.0 and prior versions.

### References
* https://lists.apache.org/thread.html/rdf06e8423833b3daadc30c56a2ff47c48920864d5199476daa897208%40%3Cusers.zeppelin.apache.org%3E


### Credits
* Apache Zeppelin would like to thank HERE Security team for reporting this issue 


## Notebook permissions bypass ## { #CVE-2020-13929 }

CVE-2020-13929 [\[CVE json\]](./CVE-2020-13929.cve.json) [\[OSV json\]](./CVE-2020-13929.osv.json)



_Last updated: 2021-09-02T16:10:15.351Z_

### Affected

* Apache Zeppelin from Apache Zeppelin through 0.9.0


### Description

Authentication bypass vulnerability in Apache Zeppelin allows an attacker to bypass Zeppelin authentication mechanism to act as another user.  This issue affects Apache Zeppelin Apache Zeppelin version 0.9.0 and prior versions.

### References
* https://lists.apache.org/thread.html/r768800925d6407a6a87ccae0ec98776b7bda50c0e3ed3d0130dad028%40%3Cusers.zeppelin.apache.org%3E


### Credits
* Apache Zeppelin would like to thank David Woodhouse for reporting this issue 


## Cross Site Scripting in markdown interpreter ## { #CVE-2021-27578 }

CVE-2021-27578 [\[CVE json\]](./CVE-2021-27578.cve.json) [\[OSV json\]](./CVE-2021-27578.osv.json)



_Last updated: 2021-09-02T16:11:07.660Z_

### Affected

* Apache Zeppelin from Apache Zeppelin before 0.9.0


### Description

Cross Site Scripting vulnerability in markdown interpreter of Apache Zeppelin allows an attacker to inject malicious scripts.  This issue affects Apache Zeppelin Apache Zeppelin versions prior to 0.9.0.

### References
* https://lists.apache.org/thread.html/r90590aa5ea788128ecc2e822e1e64d5200b4cb92b06707b38da4cb3d%40%3Cusers.zeppelin.apache.org%3E


### Credits
* Apache Zeppelin would like to thank Paulo Pacheco for reporting this issue 


## Arbitrary file deletion vulnerability ## { #CVE-2021-28655 }

CVE-2021-28655 [\[CVE json\]](./CVE-2021-28655.cve.json) [\[OSV json\]](./CVE-2021-28655.osv.json)



_Last updated: 2022-12-20T09:49:02.814Z_

### Affected

* Apache Zeppelin through 0.9.0


### Description

The improper Input Validation vulnerability in "”Move folder to Trash” feature of Apache Zeppelin allows an attacker to delete the arbitrary files.  This issue affects Apache Zeppelin Apache Zeppelin version 0.9.0 and prior versions.

### References
* https://lists.apache.org/thread/bxs056g3xlsofz0jb3wny9dw4llwptd2


### Credits
* Kai Zhao (finder)


## CSRF vulnerability in the Credentials page ## { #CVE-2021-28656 }

CVE-2021-28656 [\[CVE json\]](./CVE-2021-28656.cve.json) [\[OSV json\]](./CVE-2021-28656.osv.json)



_Last updated: 2024-04-09T09:12:56.855Z_

### Affected

* Apache Zeppelin through 0.9.0


### Description

Cross-Site Request Forgery (CSRF) vulnerability in Credential page of Apache Zeppelin allows an attacker to submit malicious request.  This issue affects Apache Zeppelin Apache Zeppelin version 0.9.0 and prior versions.

### References
* https://lists.apache.org/thread/dttzkkv4qyn1rq2fdv1r94otb1osxztc


### Credits
* Jiang Qingzhi (finder)


## Stored XSS in note permissions ## { #CVE-2022-46870 }

CVE-2022-46870 [\[CVE json\]](./CVE-2022-46870.cve.json) [\[OSV json\]](./CVE-2022-46870.osv.json)



_Last updated: 2022-12-16T12:54:56.815Z_

### Affected

* Apache Zeppelin before 0.8.2


### Description

An Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Zeppelin allows logged-in users to execute arbitrary javascript in other users' browsers.<br><p>This issue affects Apache Zeppelin before 0.8.2. Users are recommended to upgrade to a supported version of Zeppelin.<br></p>

### References
* https://lists.apache.org/thread/gb1wdnrm1095xw6qznpsycfrht4lwbwc


## connecting to a malicious SAP server allowed it to perform XXE ## { #CVE-2022-47894 }

CVE-2022-47894 [\[CVE json\]](./CVE-2022-47894.cve.json) [\[OSV json\]](./CVE-2022-47894.osv.json)



_Last updated: 2024-04-09T09:29:15.865Z_

### Affected

* Apache Zeppelin SAP from 0.8.0 before 0.11.0


### Description

Improper Input Validation vulnerability in Apache Zeppelin SAP.<p>This issue affects Apache Zeppelin SAP: from 0.8.0 before 0.11.0.</p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.<br><br>For more information, the fix already was merged in the source code but Zeppelin decided to retire the SAP component<br><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://github.com/apache/zeppelin/pull/4302
* https://lists.apache.org/thread/csf4k73kkn3nx58pm0p2qrylbox4fvyy


### Credits
* kuiplatain@knownsec 404 Team (finder)


## Path traversal vulnerability ## { #CVE-2024-31860 }

CVE-2024-31860 [\[CVE json\]](./CVE-2024-31860.cve.json) [\[OSV json\]](./CVE-2024-31860.osv.json)



_Last updated: 2025-05-06T13:12:30.032Z_

### Affected

* Apache Zeppelin from 0.9.0 before 0.11.0


### Description

Improper Input Validation vulnerability in Apache Zeppelin.<br><br>By adding relative path indicators(E.g ..), attackers can see the contents for any files in the filesystem that the server account can access.&nbsp;<br><p>This issue affects Apache Zeppelin: from 0.9.0 before 0.11.0.</p><p>Users are recommended to upgrade to version 0.11.0, which fixes the issue.</p>

### References
* https://github.com/apache/zeppelin/pull/4632
* https://lists.apache.org/thread/c0zfjnow3oc3dzc8w5rbkzj8lqj5jm5x


### Credits
* Kai Zhao (finder)


## Denial of service with invalid notebook name ## { #CVE-2024-31862 }

CVE-2024-31862 [\[CVE json\]](./CVE-2024-31862.cve.json) [\[OSV json\]](./CVE-2024-31862.osv.json)



_Last updated: 2024-04-09T09:40:37.681Z_

### Affected

* Apache Zeppelin from 0.10.1 before 0.11.0


### Description

Improper Input Validation vulnerability in Apache Zeppelin when creating a new note from Zeppelin's UI.<p>This issue affects Apache Zeppelin: from 0.10.1 before 0.11.0.</p><p>Users are recommended to upgrade to version 0.11.0, which fixes the issue.</p>

### References
* https://github.com/apache/zeppelin/pull/4632
* https://lists.apache.org/thread/73xdjx43yg4yz8bd4p3o8vzyybkysmn0


### Credits
* Esa Hiltunen (finder)
* https://teragrep.com (finder)


## Replacing other users notebook, bypassing any permissions ## { #CVE-2024-31863 }

CVE-2024-31863 [\[CVE json\]](./CVE-2024-31863.cve.json) [\[OSV json\]](./CVE-2024-31863.osv.json)



_Last updated: 2024-04-09T10:25:26.871Z_

### Affected

* Apache Zeppelin from 0.10.1 before 0.11.0


### Description

Authentication Bypass by Spoofing vulnerability by replacing to exsiting notes in Apache Zeppelin.<p>This issue affects Apache Zeppelin: from 0.10.1 before 0.11.0.</p><p>Users are recommended to upgrade to version 0.11.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/3od2gfpwllmtc9c5ggw04ohn8s7w3ct9


### Credits
* Esa Hiltunen (finder)
* https://teragrep.com (finder)


## Remote code execution by adding malicious JDBC connection string ## { #CVE-2024-31864 }

CVE-2024-31864 [\[CVE json\]](./CVE-2024-31864.cve.json) [\[OSV json\]](./CVE-2024-31864.osv.json)



_Last updated: 2024-04-11T07:54:22.052Z_

### Affected

* Apache Zeppelin before 0.11.1


### Description

Improper Control of Generation of Code ('Code Injection') vulnerability in Apache Zeppelin.<br><br>The attacker can inject sensitive configuration or malicious code when connecting MySQL database via JDBC driver.<br><p>This issue affects Apache Zeppelin: before 0.11.1.</p><p>Users are recommended to upgrade to version 0.11.1, which fixes the issue.</p>

### References
* https://github.com/apache/zeppelin/pull/4709
* https://www.cve.org/CVERecord?id=CVE-2020-11974
* https://lists.apache.org/thread/752qdk0rnkd9nqtornz734zwb7xdwcdb


### Credits
* rg (finder)
* Nbxiglk (finder)


## Cron arbitrary user impersonation with improper privileges ## { #CVE-2024-31865 }

CVE-2024-31865 [\[CVE json\]](./CVE-2024-31865.cve.json) [\[OSV json\]](./CVE-2024-31865.osv.json)



_Last updated: 2024-04-09T16:07:34.123Z_

### Affected

* Apache Zeppelin from 0.8.2 before 0.11.1


### Description

<p>Improper Input Validation vulnerability in Apache Zeppelin.</p><p>The attackers can call updating cron API with invalid or improper privileges so that the notebook can run with the privileges.</p><p>This issue affects Apache Zeppelin: from 0.8.2 before 0.11.1.</p><p>Users are recommended to upgrade to version 0.11.1, which fixes the issue.</p>

### References
* https://github.com/apache/zeppelin/pull/4631
* https://lists.apache.org/thread/slm1sf0slwc11f4m4r0nd6ot2rf7w81l


### Credits
* Esa Hiltunen (finder)
* https://teragrep.com (finder)


## Interpreter download command does not escape malicious code injection ## { #CVE-2024-31866 }

CVE-2024-31866 [\[CVE json\]](./CVE-2024-31866.cve.json) [\[OSV json\]](./CVE-2024-31866.osv.json)



_Last updated: 2024-04-09T16:09:09.746Z_

### Affected

* Apache Zeppelin from 0.8.2 before 0.11.1


### Description

Improper Encoding or Escaping of Output vulnerability in Apache Zeppelin.<br><br>The attackers can execute shell scripts or malicious code by overriding configuration like&nbsp;<span style="background-color: rgb(255, 255, 255);">ZEPPELIN_INTP_CLASSPATH_OVERRIDES.</span><br><p>This issue affects Apache Zeppelin: from 0.8.2 before 0.11.1.</p><p>Users are recommended to upgrade to version 0.11.1, which fixes the issue.</p>

### References
* https://github.com/apache/zeppelin/pull/4715
* https://lists.apache.org/thread/jpkbq3oktopt34x2n5wnhzc2r1410ddd


### Credits
* Esa Hiltunen (finder)
* https://teragrep.com (finder)


## LDAP search filter query Injection Vulnerability ## { #CVE-2024-31867 }

CVE-2024-31867 [\[CVE json\]](./CVE-2024-31867.cve.json) [\[OSV json\]](./CVE-2024-31867.osv.json)



_Last updated: 2024-04-09T16:15:46.165Z_

### Affected

* Apache Zeppelin from 0.8.2 before 0.11.1


### Description

Improper Input Validation vulnerability in Apache Zeppelin.<br><br>The attackers can execute malicious queries by setting improper configuration properties to LDAP search filter.<br><p>This issue affects Apache Zeppelin: from 0.8.2 before 0.11.1.</p><p>Users are recommended to upgrade to version 0.11.1, which fixes the issue.</p>

### References
* https://github.com/apache/zeppelin/pull/4714
* https://lists.apache.org/thread/s4scw8bxdhrjs0kg0lhb68xqd8y9lrtf


### Credits
* Qing Xu (finder)


## XSS vulnerability in the helium module ## { #CVE-2024-31868 }

CVE-2024-31868 [\[CVE json\]](./CVE-2024-31868.cve.json) [\[OSV json\]](./CVE-2024-31868.osv.json)



_Last updated: 2024-10-03T12:35:14.839Z_

### Affected

* Apache Zeppelin from 0.8.2 before 0.11.1


### Description

Improper Encoding or Escaping of Output vulnerability in Apache Zeppelin.<br><br>The attackers can modify helium.json and exposure XSS attacks to normal users.<br><p>This issue affects Apache Zeppelin: from 0.8.2 before 0.11.1.</p><p>Users are recommended to upgrade to version 0.11.1, which fixes the issue.</p>

### References
* https://github.com/apache/zeppelin/pull/4728
* https://lists.apache.org/thread/55mqs673plsxmgnq7fdf2flftpllyf11


### Credits
* H Ming (finder)


## raft directory listing and file read ## { #CVE-2024-41169 }

CVE-2024-41169 [\[CVE json\]](./CVE-2024-41169.cve.json) [\[OSV json\]](./CVE-2024-41169.osv.json)



_Last updated: 2025-07-12T16:22:30.823Z_

### Affected

* Apache Zeppelin from 0.10.1 before 0.12.0


### Description

<p>The attacker can use the raft server protocol in an unauthenticated way. The attacker can see the server's resources, including directories and files.</p><p>This issue affects Apache Zeppelin: from 0.10.1 up to 0.12.0.</p><p>Users are recommended to upgrade to version 0.12.0,&nbsp;<span style="background-color: rgb(255, 255, 255);">which fixes the issue by removing the Cluster Interpreter.</span></p>

### References
* https://github.com/apache/zeppelin/pull/4841
* https://issues.apache.org/jira/browse/ZEPPELIN-6101
* https://lists.apache.org/thread/moyym04993c8owh4h0qj98r43tbo8qdd


### Credits
* SuperX <superxyyang@gmail.com> (finder)


## XSS in the Helium module ## { #CVE-2024-41177 }

CVE-2024-41177 [\[CVE json\]](./CVE-2024-41177.cve.json) [\[OSV json\]](./CVE-2024-41177.osv.json)



_Last updated: 2025-08-03T10:09:33.254Z_

### Affected

* Apache Zeppelin before 0.12.0


### Description

<p>Incomplete Blacklist to Cross-Site Scripting vulnerability in Apache Zeppelin.</p><p>This issue affects Apache Zeppelin: before 0.12.0.</p><p>Users are recommended to upgrade to version 0.12.0, which fixes the issue.</p>

### References
* https://github.com/apache/zeppelin/pull/4755
* https://github.com/apache/zeppelin/pull/4795
* https://lists.apache.org/thread/nwh8vh9f3pnvt04n8z4g2kbddh62blr6


### Credits
* H Ming (finder)


## Command Injection via CSWSH ## { #CVE-2024-51775 }

CVE-2024-51775 [\[CVE json\]](./CVE-2024-51775.cve.json) [\[OSV json\]](./CVE-2024-51775.osv.json)



_Last updated: 2025-08-03T10:14:50.764Z_

### Affected

* Apache Zeppelin from 0.11.1 before 0.12.0


### Description

<p>Missing Origin Validation in WebSockets vulnerability in Apache Zeppelin.</p>The attacker could access the Zeppelin server from another origin without any restriction, and get internal information about paragraphs.&nbsp;<br><p>This issue affects Apache Zeppelin: from 0.11.1 before 0.12.0.</p><p>Users are recommended to upgrade to version 0.12.0, which fixes the issue.</p>

### References
* https://github.com/apache/zeppelin/pull/4823
* https://lists.apache.org/thread/bckm4y2ld5k5ro7bwh5yxbpxvslw0lm6


### Credits
* Calum Hutton (finder)


## Arbitrary file read by adding malicious JDBC connection string ## { #CVE-2024-52279 }

CVE-2024-52279 [\[CVE json\]](./CVE-2024-52279.cve.json) [\[OSV json\]](./CVE-2024-52279.osv.json)



_Last updated: 2025-08-03T10:01:35.245Z_

### Affected

* Apache Zeppelin from 0.11.1 before 0.12.0


### Description

<p>Improper Input Validation vulnerability in Apache Zeppelin. The fix for JDBC URL validation in CVE-2024-31864 did not account for URL encoded input.</p><p>This issue affects Apache Zeppelin: from 0.11.1 before 0.12.0.</p><p>Users are recommended to upgrade to version 0.12.0, which fixes the issue.</p>

### References
* https://github.com/apache/zeppelin/pull/4838
* https://issues.apache.org/jira/browse/ZEPPELIN-6095
* https://www.cve.org/CVERecord?id=CVE-2024-31864
* https://lists.apache.org/thread/dxb98vgrb21rrl3k0fzonpk66onr6o4q


### Credits
* H Ming (finder)
