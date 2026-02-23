---
title: Apache Sling security advisories
description: Security information for Apache Sling
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Sling? You can read more about the projects' security policy on their [security page](https://sling.apache.org/project-information/security.html), and email your report to the [Apache Sling Security Team](mailto:security@sling.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://sling.apache.org/project-information/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Malicious code execution via path traversal ## { #CVE-2024-23673 }

CVE-2024-23673 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23673) [\[CVE json\]](./CVE-2024-23673.cve.json) [\[OSV json\]](./CVE-2024-23673.osv.json)



_Last updated: 2024-02-06T10:04:18.646Z_

### Affected

* Apache Sling Servlets Resolver before 2.11.0


### Description



Malicious code execution via path traversal in Apache Software Foundation Apache Sling Servlets Resolver.<p>This issue affects all version of Apache Sling Servlets Resolver before 2.11.0. However, whether a system is vulnerable to this attack depends on the exact configuration of the system.<br>If the system is vulnerable, a user with write access to the repository might be able to trick the Sling Servlet Resolver to load a previously uploaded script.&nbsp;</p>

Users are recommended to upgrade to version 2.11.0, which fixes this issue. It is recommended to upgrade, regardless of whether your system configuration currently allows this attack or not.

### References
* https://lists.apache.org/thread/5zzx8ztwc6tmbwlw80m2pbrp3913l2kl


## Requests to certain paths managed by the Apache Sling Resource Merger can lead to DoS ## { #CVE-2023-26513 }

CVE-2023-26513 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-26513) [\[CVE json\]](./CVE-2023-26513.cve.json) [\[OSV json\]](./CVE-2023-26513.osv.json)



_Last updated: 2023-03-20T12:19:53.778Z_

### Affected

* Apache Sling Resource Merger from 1.2.0 before 1.4.2


### Description

Excessive Iteration vulnerability in Apache Software Foundation Apache Sling Resource Merger.<p>This issue affects Apache Sling Resource Merger: from 1.2.0 before 1.4.2.</p>

### References
* https://lists.apache.org/thread/xpcpo1y88ldss5hgmvogsf6h3735l5zb


### Credits
*  Alex Collignon (reporter)


## Apache Sling does not allow to handle i18n content in a secure way ## { #CVE-2023-25621 }

CVE-2023-25621 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25621) [\[CVE json\]](./CVE-2023-25621.cve.json) [\[OSV json\]](./CVE-2023-25621.osv.json)



_Last updated: 2023-02-23T08:41:12.080Z_

### Affected

* Apache Sling from Apache Sling i18n through 2.5.18


### Description

Privilege Escalation vulnerability in Apache Software Foundation Apache Sling.<br>Any content author is able to create i18n dictionaries in the repository in a location the author has write access to. As these translations are used across the whole product, it allows an author to change any text or dialog in the product. For example an attacker might fool someone by changing the text on a delete button to "Info".<br><p>This issue affects the i18n module of Apache Sling up to version 2.5.18. Version 2.6.2 and higher limit by default i18m dictionaries to certain paths in the repository (/libs and /apps).</p><p>Users of the module are advised to update to version 2.6.2 or higher, check the configuration for resource loading and then adjust the access permissions for the configured path accordingly.<br></p>

### References
* https://sling.apache.org/news.html


## JNDI injection into Apache sling-org-apache-sling-jcr-base ## { #CVE-2023-25141 }

CVE-2023-25141 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25141) [\[CVE json\]](./CVE-2023-25141.cve.json) [\[OSV json\]](./CVE-2023-25141.osv.json)



_Last updated: 2023-02-14T10:19:00.558Z_

### Affected

* Apache Sling JCR Base from 2.0.6 before 3.1.12


### Description

<div>Apache Sling JCR Base &lt; 3.1.12 has a critical injection vulnerability when running on old JDK versions (JDK 1.8.191 or earlier) through utility functions in RepositoryAccessor. The functions getRepository and getRepositoryFromURL allow an application to access data stored in a remote location via JDNI and RMI.</div><div><br></div><div>Users of Apache Sling JCR Base are recommended to upgrade to Apache Sling JCR Base 3.1.12 or later, or to run on a more recent JDK.</div>

### References
* https://sling.apache.org/news.html


### Credits
* Xun Bai from LJQC Open Source Security Institute  (reporter)


## XSS in CMS Reference / UI Components ## { #CVE-2023-22849 }

CVE-2023-22849 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-22849) [\[CVE json\]](./CVE-2023-22849.cve.json) [\[OSV json\]](./CVE-2023-22849.osv.json)



_Last updated: 2023-02-03T23:38:07.612Z_

### Affected

* Apache Sling App CMS before 1.1.6


### Description

An improper neutralization of input during web page generation ('Cross-site Scripting') [CWE-79] vulnerability in Sling App CMS version 1.1.4 and prior may allow an authenticated remote attacker to perform a reflected cross-site scripting (XSS) attack in multiple features.<br><br><span style="background-color: rgb(255, 255, 255);">Upgrade to Apache Sling App CMS &gt;= 1.1.6</span><br>

### References
* https://sling.apache.org/news.html


### Credits
* Apache Sling would like to thank Eugene Lim and Sng Jay Kai from GOVTECH for reporting this issue (finder)


## Multiple parsing problems in the Apache Sling Commons JSON module ## { #CVE-2022-47937 }

CVE-2022-47937 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-47937) [\[CVE json\]](./CVE-2022-47937.cve.json) [\[OSV json\]](./CVE-2022-47937.osv.json)



_Last updated: 2024-03-29T09:39:29.809Z_

### Affected

* org.apache.sling.commons.json through 2.0.20


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** <br></div><div><br></div><div>Improper input validation in the Apache Sling Commons JSON bundle allows an attacker to trigger unexpected errors by supplying specially-crafted input.</div><div><br></div><div><div>NOTE: This vulnerability 
only affects products that are no longer supported by the maintainer</div><div><br></div><div>The org.apache.sling.commons.json bundle has been deprecated as of March
 2017 and should not be used anymore. Consumers are encouraged to 
consider the Apache Sling Commons Johnzon OSGi bundle provided by the 
Apache Sling project, but may of course use other JSON libraries.<br></div></div>

### References
* https://issues.apache.org/jira/browse/SLING-6536
* https://github.com/apache/sling-org-apache-sling-commons-johnzon
* https://lists.apache.org/thread/sws7z50x47gv0c38q4kx6ktqrvrrg1pm


### Credits
* The vulnerability was discovered and reported by BIngDiAn. (finder)


## XSS in CMS Site Group Detail ## { #CVE-2022-46769 }

CVE-2022-46769 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-46769) [\[CVE json\]](./CVE-2022-46769.cve.json) [\[OSV json\]](./CVE-2022-46769.osv.json)



_Last updated: 2023-01-25T03:51:12.925Z_

### Affected

* Apache Sling App CMS before 1.1.4


### Description

An improper neutralization of input during web page generation ('Cross-site Scripting') [CWE-79] vulnerability in Sling App CMS version 1.1.2 and prior may allow an authenticated remote attacker to perform a reflected cross-site scripting (XSS) attack in the site group feature.<br><br><span style="background-color: rgb(255, 255, 255);">Upgrade to Apache Sling App CMS &gt;= 1.1.4</span> <br>

### References
* https://sling.apache.org/news.html


### Credits
* Apache Sling would like to thank Sam Bagheri for reporting this issue (finder)


## Include-based XSS ## { #CVE-2022-45064 }

CVE-2022-45064 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-45064) [\[CVE json\]](./CVE-2022-45064.cve.json) [\[OSV json\]](./CVE-2022-45064.osv.json)



_Last updated: 2023-04-13T10:01:10.930Z_

### Affected

* Apache Sling Engine from   before 2.14.0


### Description

<div>The SlingRequestDispatcher doesn't correctly implement the RequestDispatcher API resulting in a generic type of include-based cross-site scripting issues on the Apache Sling level. The vulnerability is exploitable by an attacker that is able to include a resource with specific content-type and control the include path (i.e. writing content). The impact of a successful attack is privilege escalation to administrative power.</div><div><br></div><div>Please update to Apache Sling Engine &gt;= 2.14.0 and enable the "Check Content-Type overrides" configuration option.<br><br><br></div>

### References
* https://lists.apache.org/thread/hhp611hltby3whk03vx2mv7cmy3vs0ok


### Credits
* Lars Krapf (reporter)


## XSS in Sling CMS Reference App Taxonomy Path ## { #CVE-2022-43670 }

CVE-2022-43670 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-43670) [\[CVE json\]](./CVE-2022-43670.cve.json) [\[OSV json\]](./CVE-2022-43670.osv.json)



_Last updated: 2022-11-02T12:20:10.764Z_

### Affected

* Apache Sling App CMS from unspecified before 1.1.2


### Description

An improper neutralization of input during web page generation ('Cross-site Scripting') [CWE-79] vulnerability in Sling App CMS version 1.1.0 and prior may allow an authenticated remote attacker to perform a reflected cross site scripting (XSS) attack in the taxonomy management feature. 

### References
* https://lists.apache.org/thread/o68l3l3crfxz107fr9dm74y8vg8kj2cs


### Credits
* Apache Sling would like to thank QSec-Team for reporting this issue


## log injection in Sling logging ## { #CVE-2022-32549 }

CVE-2022-32549 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-32549) [\[CVE json\]](./CVE-2022-32549.cve.json) [\[OSV json\]](./CVE-2022-32549.osv.json)



_Last updated: 2022-06-22T14:22:34.319Z_

### Affected

* Apache Sling from Apache Sling API through 2.25.0
* Apache Sling from Apache Sling Commons Log through 5.4.0


### Description

Apache Sling Commons Log <= 5.4.0 and Apache Sling API <= 2.25.0 are vulnerable to log injection. The ability to forge logs may allow an attacker to cover tracks by injecting fake logs and potentially corrupt log files.

### References
* https://lists.apache.org/thread/7z6h3806mwcov5kx6l96pq839sn0po1v


### Credits
* Apache Sling would like to thank Alex Collignon for reporting this issue.


## SMTPS server hostname not checked when making TLS connection to SMTPS server ## { #CVE-2021-44549 }

CVE-2021-44549 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-44549) [\[CVE json\]](./CVE-2021-44549.cve.json) [\[OSV json\]](./CVE-2021-44549.osv.json)



_Last updated: 2021-12-14T15:10:31.167Z_

### Affected

* Apache Sling Commons Messaging Mail at Apache Sling Commons Messaging Mail 1.0.0 1.0.0


### Description

Apache Sling Commons Messaging Mail provides a simple layer on top of JavaMail/Jakarta Mail for OSGi to send mails via SMTPS.

To reduce the risk of "man in the middle" attacks additional server identity checks must be performed when accessing mail servers.

For compatibility reasons these additional checks are disabled by default in JavaMail/Jakarta Mail.

The SimpleMailService in Apache Sling Commons Messaging Mail 1.0 lacks an option to enable these checks for the shared mail session.
A user could enable these checks nevertheless by accessing the session via the message created by SimpleMessageBuilder and setting the property mail.smtps.ssl.checkserveridentity to true.

Apache Sling Commons Messaging Mail 2.0 adds support for enabling server identity checks and these checks are enabled by default.
- https://javaee.github.io/javamail/docs/SSLNOTES.txt
- https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html
- https://github.com/eclipse-ee4j/mail/issues/429

### References
* https://lists.apache.org/thread/l8p9h2bqvkj6rhv4w8kzctb817415b7f


### Credits
* The issue was reported by Michael Lescisin.
