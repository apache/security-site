---
title: Apache Ambari security advisories
description: Security information for Apache Ambari
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Ambari? Send your report to the [Apache Ambari Security Team](mailto:security@ambari.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Stored XSS in Apache Ambari ## { #CVE-2020-1936 }

CVE-2020-1936 [\[CVE json\]](./CVE-2020-1936.cve.json) [\[OSV json\]](./CVE-2020-1936.osv.json)



_Last updated: 2021-03-02T08:54:00.947Z_

### Affected

* Apache Ambari from Apache Ambari before 2.7.4


### Description

A cross-site scripting issue was found in Apache Ambari Views.  This was addressed in Apache Ambari 2.7.4.

### References
* https://lists.apache.org/thread.html/946a9d72e664ad8bc592168d9a2fed88100c6e9f1bdfea08e91a3184%40%3Cuser.ambari.apache.org%3E


### Credits
* Apache Ambari would like to thank Krzysztof Przybylski from STM Solutions


##  ## { #CVE-2020-13924 }

CVE-2020-13924 [\[CVE json\]](./CVE-2020-13924.cve.json) [\[OSV json\]](./CVE-2020-13924.osv.json)



_Last updated: 2021-03-17T09:01:22.529Z_

### Affected

* Apache Ambari from Apache Ambari through 2.6.2.2


### Description

In Apache Ambari versions 2.6.2.2 and earlier, malicious users can construct file names for directory traversal and traverse to other directories to download files.

### References
* https://mail-archives.apache.org/mod_mbox/ambari-user/202102.mbox/%3CCAEJYuxEQZ_aPwJdAaSxPu-Dva%3Dhc7zZUx3-pzBORbd23g%2BGH1A%40mail.gmail.com%3E


### Credits
* threedr3am


## A malicious authenticated user can remotely execute arbitrary code in the context of the application. ## { #CVE-2022-42009 }

CVE-2022-42009 [\[CVE json\]](./CVE-2022-42009.cve.json) [\[OSV json\]](./CVE-2022-42009.osv.json)



_Last updated: 2023-07-12T09:58:16.769Z_

### Affected

* Apache Ambari from 2.7.0 through 2.7.6


### Description

SpringEL injection in the server agent in Apache Ambari version 2.7.0 to 2.7.6 allows a malicious authenticated user to execute arbitrary code remotely. U<span style="background-color: rgb(255, 255, 255);">sers are recommended to upgrade to 2.7.7.</span><br>

### References
* https://lists.apache.org/thread/6xf477ttz1oxmg0bx0tpdoz2mlqd7sbc


### Credits
* Jecki Go (jecgo@visa.com) (finder)


## Allows authenticated metrics consumers to perform RCE ## { #CVE-2022-45855 }

CVE-2022-45855 [\[CVE json\]](./CVE-2022-45855.cve.json) [\[OSV json\]](./CVE-2022-45855.osv.json)



_Last updated: 2023-07-12T09:59:42.590Z_

### Affected

* Apache Ambari from 2.7.0 through 2.7.6


### Description

SpringEL injection in the metrics source in Apache Ambari version 2.7.0 to 2.7.6 allows a malicious authenticated user to execute arbitrary code remotely.&nbsp;U<span style="background-color: rgb(255, 255, 255);">sers are recommended to upgrade to 2.7.7.</span><br>

### References
* https://lists.apache.org/thread/302c4hwfjy9lx63jrbhcdx948pxc54l1


### Credits
* rg <18993610179@163.com> (finder)


## Various XSS problems ## { #CVE-2023-50378 }

CVE-2023-50378 [\[CVE json\]](./CVE-2023-50378.cve.json) [\[OSV json\]](./CVE-2023-50378.osv.json)



_Last updated: 2024-10-03T12:23:04.013Z_

### Affected

* Apache Ambari from 2.7.0 through 2.7.7


### Description

<span style="background-color: transparent;">Lack of proper input validation and constraint enforcement in Apache Ambari prior to 2.7.8&nbsp;&nbsp;<br><br>&nbsp;Impact : As it will be <span style="background-color: rgb(255, 255, 255);">stored XSS,&nbsp;</span>Could be exploited to perform unauthorized actions, varying from data access to session hijacking and delivering malicious payloads. <br><br></span><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version  2.7.8 which fixes this issue.</span><br><br><br><br>

### References
* https://lists.apache.org/thread/6hn0thq743vz9gh283s2d87wz8tqh37c


## authenticated users could perform command injection to perform RCE ## { #CVE-2023-50379 }

CVE-2023-50379 [\[CVE json\]](./CVE-2023-50379.cve.json) [\[OSV json\]](./CVE-2023-50379.osv.json)



_Last updated: 2024-02-27T08:26:54.321Z_

### Affected

* Apache Ambari from 2.7.0 through 2.7.7


### Description

<span style="background-color: transparent;">Malicious code injection in Apache Ambari in prior to 2.7.8.&nbsp;</span><span style="background-color: transparent;"><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 2.7.8, which fixes this issue.</span></span><b><span style="background-color: transparent;"><br><br></span></b><span style="background-color: transparent;">Impact:</span><b><span style="background-color: transparent;"><br></span></b><span style="background-color: transparent;">A Cluster Operator can manipulate the request by adding a malicious code injection and gain a root over the cluster main host.</span><br><br>

### References
* https://lists.apache.org/thread/jglww6h6ngxpo1r6r5fx7ff7z29lnvv8


## authenticated users could perform XXE to read arbitrary files on the server ## { #CVE-2023-50380 }

CVE-2023-50380 [\[CVE json\]](./CVE-2023-50380.cve.json) [\[OSV json\]](./CVE-2023-50380.osv.json)



_Last updated: 2024-02-27T16:51:31.875Z_

### Affected

* Apache Ambari from 2.7.0 through 2.7.7


### Description

<p><span style="background-color: transparent;">XML External Entity injection in apache ambari versions &lt;= 2.7.7,&nbsp;<span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 2.7.8, which fixes this issue.</span></span></p><p><span style="background-color: transparent;"><br></span></p><p><span style="background-color: transparent;">More Details:</span></p><p><span style="background-color: transparent;">Oozie Workflow Scheduler had a vulnerability that allowed for root-level file reading and privilege escalation from low-privilege users. The vulnerability was caused through lack of proper user input validation.</span></p><p><span style="background-color: transparent;">This vulnerability is known as an XML External Entity (XXE) injection attack. Attackers can exploit XXE vulnerabilities to read arbitrary files on the server, including sensitive system files. In theory, it might be possible to use this to escalate privileges.</span></p>

### References
* https://lists.apache.org/thread/qrt7mq7v7zyrh1qsh1gkg1m7clysvy32


## Remote Code Injection in Ambari Metrics and AMS Alerts ## { #CVE-2024-51941 }

CVE-2024-51941 [\[CVE json\]](./CVE-2024-51941.cve.json) [\[OSV json\]](./CVE-2024-51941.osv.json)



_Last updated: 2025-09-03T08:07:26.617Z_

### Affected

* Apache Ambari through 2.7.8


### Description

A remote code injection vulnerability exists in the Ambari Metrics and 
AMS Alerts feature, allowing authenticated users to inject and execute 
arbitrary code. The vulnerability occurs when processing alert 
definitions, where malicious input can be injected into the alert script
 execution path. An attacker with authenticated access can exploit this 
vulnerability to execute arbitrary commands on the server. The issue has
 been fixed in the latest versions of Ambari.

### References
* https://lists.apache.org/thread/xq50nlff7o7z1kq3y637clzzl6mjhl8j


### Credits
* 4ra1n (https://github.com/4ra1n) (finder)
* h4cking2thegate@gmail.com (reporter)


## XML External Entity (XXE) Vulnerability in Ambari/Oozie ## { #CVE-2025-23195 }

CVE-2025-23195 [\[CVE json\]](./CVE-2025-23195.cve.json) [\[OSV json\]](./CVE-2025-23195.osv.json)



_Last updated: 2025-01-21T21:22:31.147Z_

### Affected

* Apache Ambari before 2.7.9


### Description

An XML External Entity (XXE) vulnerability exists in the Ambari/Oozie 
project, allowing an attacker to inject malicious XML entities. This 
vulnerability occurs due to insecure parsing of XML input using the 
`DocumentBuilderFactory` class without disabling external entity 
resolution. An attacker can exploit this vulnerability to read arbitrary
 files on the server or perform server-side request forgery (SSRF) 
attacks. The issue has been fixed in both Ambari 2.7.9 and the trunk 
branch.

### References
* https://lists.apache.org/thread/hsb6mvxd7g37dq1ygtd0pd88gs9tfcwq


## Code Injection Vulnerability in Ambari Alert Definition ## { #CVE-2025-23196 }

CVE-2025-23196 [\[CVE json\]](./CVE-2025-23196.cve.json) [\[OSV json\]](./CVE-2025-23196.osv.json)



_Last updated: 2025-02-03T08:22:23.980Z_

### Affected

* Apache Ambari from 8 before 2.7.9


### Description

A code injection vulnerability exists in the Ambari Alert Definition 
feature, allowing authenticated users to inject and execute arbitrary 
shell commands. The vulnerability arises when defining alert scripts, 
where the script filename field is executed using `sh -c`. An attacker 
with authenticated access can exploit this vulnerability to inject 
malicious commands, leading to remote code execution on the server. The 
issue has been fixed in the latest versions of Ambari.

### References
* https://lists.apache.org/thread/70g1l5lxvko7kvhyxmtmklhhfrlon837


### Credits
* Liyw979 (reporter)
* robinzeng2015 (reporter)
* fcgboy (reporter)
* wk2025 (reporter)
