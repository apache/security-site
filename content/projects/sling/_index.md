---
title: Apache Sling security advisories
description: Security information for Apache Sling
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Sling? You can read more about the projects' security policy on their [security page](https://sling.apache.org/site/security.html), and email your report to the  [Apache Sling Security Team](mailto:security@sling.apache.org).

# Advisories

## Include-based XSS ## { #CVE-2022-45064 }

[CVE-2022-45064](./CVE-2022-45064.cve.json)

### Affected

* Apache Sling Engine versions   before 2.14.0


### Description

<div>The SlingRequestDispatcher doesn't correctly implement the RequestDispatcher API resulting in a generic type of include-based cross-site scripting issues on the Apache Sling level. The vulnerability is exploitable by an attacker that is able to include a resource with specific content-type and control the include path (i.e. writing content). The impact of a successful attack is privilege escalation to administrative power.</div><div><br></div><div>Please update to Apache Sling Engine &gt;= 2.14.0 and enable the "Check Content-Type overrides" configuration option.<br><br><br></div>

## XSS in CMS Site Group Detail ## { #CVE-2022-46769 }

[CVE-2022-46769](./CVE-2022-46769.cve.json)

### Affected

* Apache Sling App CMS versions  before 1.1.4


### Description

An improper neutralization of input during web page generation ('Cross-site Scripting') [CWE-79] vulnerability in Sling App CMS version 1.1.2 and prior may allow an authenticated remote attacker to perform a reflected cross-site scripting (XSS) attack in the site group feature.<br><br><span style="background-color: rgb(255, 255, 255);">Upgrade to Apache Sling App CMS &gt;= 1.1.4</span> <br>

## XSS in CMS Reference / UI Components ## { #CVE-2023-22849 }

[CVE-2023-22849](./CVE-2023-22849.cve.json)

### Affected

* Apache Sling App CMS versions  before 1.1.6


### Description

An improper neutralization of input during web page generation ('Cross-site Scripting') [CWE-79] vulnerability in Sling App CMS version 1.1.4 and prior may allow an authenticated remote attacker to perform a reflected cross-site scripting (XSS) attack in multiple features.<br><br><span style="background-color: rgb(255, 255, 255);">Upgrade to Apache Sling App CMS &gt;= 1.1.6</span><br>

## JNDI injection into Apache sling-org-apache-sling-jcr-base ## { #CVE-2023-25141 }

[CVE-2023-25141](./CVE-2023-25141.cve.json)

### Affected

* Apache Sling JCR Base versions 2.0.6 before 3.1.12


### Description

<div>Apache Sling JCR Base &lt; 3.1.12 has a critical injection vulnerability when running on old JDK versions (JDK 1.8.191 or earlier) through utility functions in RepositoryAccessor. The functions getRepository and getRepositoryFromURL allow an application to access data stored in a remote location via JDNI and RMI.</div><div><br></div><div>Users of Apache Sling JCR Base are recommended to upgrade to Apache Sling JCR Base 3.1.12 or later, or to run on a more recent JDK.</div>

## Apache Sling does not allow to handle i18n content in a secure way ## { #CVE-2023-25621 }

[CVE-2023-25621](./CVE-2023-25621.cve.json)

### Affected

* Apache Sling versions Apache Sling i18n including 2.5.18


### Description

Privilege Escalation vulnerability in Apache Software Foundation Apache Sling.<br>Any content author is able to create i18n dictionaries in the repository in a location the author has write access to. As these translations are used across the whole product, it allows an author to change any text or dialog in the product. For example an attacker might fool someone by changing the text on a delete button to "Info".<br><p>This issue affects the i18n module of Apache Sling up to version 2.5.18. Version 2.6.2 and higher limit by default i18m dictionaries to certain paths in the repository (/libs and /apps).</p><p>Users of the module are advised to update to version 2.6.2 or higher, check the configuration for resource loading and then adjust the access permissions for the configured path accordingly.<br></p>

## Requests to certain paths managed by the Apache Sling Resource Merger can lead to DoS ## { #CVE-2023-26513 }

[CVE-2023-26513](./CVE-2023-26513.cve.json)

### Affected

* Apache Sling Resource Merger versions 1.2.0 before 1.4.2


### Description

Excessive Iteration vulnerability in Apache Software Foundation Apache Sling Resource Merger.<p>This issue affects Apache Sling Resource Merger: from 1.2.0 before 1.4.2.</p>