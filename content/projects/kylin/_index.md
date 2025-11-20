---
title: Apache Kylin security advisories
description: Security information for Apache Kylin
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Kylin? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improper Access Control to Streaming Coordinator & SSRF ## { #CVE-2021-27738 }

CVE-2021-27738 [\[CVE json\]](./CVE-2021-27738.cve.json) [\[OSV json\]](./CVE-2021-27738.osv.json)



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


## Apache Kylin unsafe class loading ## { #CVE-2021-31522 }

CVE-2021-31522 [\[CVE json\]](./CVE-2021-31522.cve.json) [\[OSV json\]](./CVE-2021-31522.osv.json)



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


## Mysql JDBC Connector Deserialize RCE ## { #CVE-2021-36774 }

CVE-2021-36774 [\[CVE json\]](./CVE-2021-36774.cve.json) [\[OSV json\]](./CVE-2021-36774.osv.json)



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


## Command injection ## { #CVE-2021-45456 }

CVE-2021-45456 [\[CVE json\]](./CVE-2021-45456.cve.json) [\[OSV json\]](./CVE-2021-45456.osv.json)



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


## Overly broad CORS configuration  ## { #CVE-2021-45457 }

CVE-2021-45457 [\[CVE json\]](./CVE-2021-45457.cve.json) [\[OSV json\]](./CVE-2021-45457.osv.json)



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


## Hardcoded credentials ## { #CVE-2021-45458 }

CVE-2021-45458 [\[CVE json\]](./CVE-2021-45458.cve.json) [\[OSV json\]](./CVE-2021-45458.osv.json)



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


## Apache Kylin prior to 4.0.2 allows command injection when the configuration overwrites function overwrites system parameters ## { #CVE-2022-24697 }

CVE-2022-24697 [\[CVE json\]](./CVE-2022-24697.cve.json) [\[OSV json\]](./CVE-2022-24697.osv.json)



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


## Command injection by Useless configuration ## { #CVE-2022-43396 }

CVE-2022-43396 [\[CVE json\]](./CVE-2022-43396.cve.json) [\[OSV json\]](./CVE-2022-43396.osv.json)



_Last updated: 2022-12-30T10:30:28.434Z_

### Affected

* Apache Kylin from Apache Kylin 4 through 4.0.2


### Description

In the fix for CVE-2022-24697, a blacklist is used to filter user input commands. But there is a risk of being bypassed. The user can control the command by controlling the&nbsp;kylin.engine.spark-cmd&nbsp;parameter of conf.

### References
* https://lists.apache.org/thread/ob2ks04zl5ms0r44cd74y1xdl1rzfd1r


### Credits
* Yasax1 Li <pp1ove.lit@gmail.com> (finder)


## Command injection by Diagnosis Controller ## { #CVE-2022-44621 }

CVE-2022-44621 [\[CVE json\]](./CVE-2022-44621.cve.json) [\[OSV json\]](./CVE-2022-44621.osv.json)



_Last updated: 2022-12-30T10:31:39.045Z_

### Affected

* Apache Kylin from Apache Kylin 4  through 4.0.2


### Description

Diagnosis Controller miss parameter validation, so user may attacked by command injection via HTTP Request.

### References
* https://lists.apache.org/thread/7ctchj24dofgsj9g1rg1245cms9myb34


### Credits
* Messy God <godimessy@gmail.com> (finder)


## Insufficiently protected credentials in config file ## { #CVE-2023-29055 }

CVE-2023-29055 [\[CVE json\]](./CVE-2023-29055.cve.json) [\[OSV json\]](./CVE-2023-29055.osv.json)



_Last updated: 2024-01-29T12:20:52.048Z_

### Affected

* Apache Kylin from 2.0.0 through 4.0.3


### Description

<div>In Apache Kylin version 2.0.0 to 4.0.3, there is a Server Config web interface that displays the content of file 'kylin.properties', that may contain serverside credentials. When the kylin service runs over HTTP (or other plain text protocol), it is possible for network sniffers to hijack the HTTP payload and get access to the content of kylin.properties and potentially the containing credentials.<br></div><div><br></div><div>To avoid this threat, users are recommended to&nbsp;</div><div><ol><li>Always turn on HTTPS so that network payload is encrypted.<br></li><li>Avoid putting credentials in kylin.properties, or at least not in plain text.</li><li>Use network firewalls to protect the serverside such that it is not accessible to external attackers.<br></li><li>Upgrade to version Apache Kylin 4.0.4, which filters out the sensitive content that goes to the Server Config web interface.</li></ol><br></div>

### References
* https://lists.apache.org/thread/o1bvyv9wnfkx7dxpfjlor20nykgsoh6r


### Credits
* Li Jiakun <2839549219@qq.com> (reporter)


## Session fixation in web interface ## { #CVE-2024-23590 }

CVE-2024-23590 [\[CVE json\]](./CVE-2024-23590.cve.json) [\[OSV json\]](./CVE-2024-23590.osv.json)



_Last updated: 2024-11-04T09:27:04.256Z_

### Affected

* Apache Kylin from 2.0.0 before 5.0.0


### Description

<p>Session Fixation vulnerability in Apache Kylin.</p><p>This issue affects Apache Kylin: from 2.0.0 through 4.x.</p><p>Users are recommended to upgrade to version 5.0.0 or above, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7161154h0k6zygr9917qq0g95p39szml


### Credits
* XJB Security Team (reporter)


## SSRF vulnerability in the diagnosis api ## { #CVE-2024-48944 }

CVE-2024-48944 [\[CVE json\]](./CVE-2024-48944.cve.json) [\[OSV json\]](./CVE-2024-48944.osv.json)



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


## The remote code execution via jdbc url ## { #CVE-2025-30067 }

CVE-2025-30067 [\[CVE json\]](./CVE-2025-30067.cve.json) [\[OSV json\]](./CVE-2025-30067.osv.json)



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


## Authentication bypass ## { #CVE-2025-61733 }

CVE-2025-61733 [\[CVE json\]](./CVE-2025-61733.cve.json) [\[OSV json\]](./CVE-2025-61733.osv.json)



_Last updated: 2025-10-02T09:47:37.237Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.2


### Description

<p>Authentication Bypass Using an Alternate Path or Channel vulnerability in Apache Kylin.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.2.</p><p>Users are recommended to upgrade to version 5.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/8wmcffly6gp50nmfw8j4w3hlmv843yo0


### Credits
* liuhuajin <liuhuajin1@huawei.com> (finder)


## improper restriction of file read ## { #CVE-2025-61734 }

CVE-2025-61734 [\[CVE json\]](./CVE-2025-61734.cve.json) [\[OSV json\]](./CVE-2025-61734.osv.json)



_Last updated: 2025-10-02T09:47:13.137Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.2


### Description

<p>Files or Directories Accessible to External Parties vulnerability in Apache Kylin.
 You are fine as long as the Kylin's system and project admin access is well protected.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.2.</p><p>Users are recommended to upgrade to version 5.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/z705g7sn3g0bkchlqbo1hz1tyqorn4d2


### Credits
* liuhuajin <liuhuajin1@huawei.com> (finder)


## Server-Side Request Forgery ## { #CVE-2025-61735 }

CVE-2025-61735 [\[CVE json\]](./CVE-2025-61735.cve.json) [\[OSV json\]](./CVE-2025-61735.osv.json)



_Last updated: 2025-10-02T09:47:48.059Z_

### Affected

* Apache Kylin from 4.0.0 through 5.0.2


### Description

<p>Server-Side Request Forgery (SSRF) vulnerability in Apache Kylin.</p><p>This issue affects Apache Kylin: from 4.0.0 through 5.0.2.&nbsp;You are fine as long as the Kylin's system and project admin access is well protected.</p><p>Users are recommended to upgrade to version 5.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/yscobmx869zvprsykb94r24jtmb58ckh


### Credits
* liuhuajin <liuhuajin1@huawei.com> (finder)
