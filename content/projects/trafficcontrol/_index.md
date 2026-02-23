---
title: Apache Traffic Control security advisories
description: Security information for Apache Traffic Control
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Traffic Control? You can read more about the projects' security policy on their [security page](https://trafficcontrol.apache.org/security/index.html), and email your report to the [Apache Traffic Control Security Team](mailto:security@trafficcontrol.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://trafficcontrol.apache.org/security/index.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## ReDoS issue in Traffic Router configuration ## { #CVE-2025-61581 }

CVE-2025-61581 [\[CVE json\]](./CVE-2025-61581.cve.json) [\[OSV json\]](./CVE-2025-61581.osv.json)



_Last updated: 2025-10-16T08:40:10.117Z_

### Affected

* Apache Traffic Control before *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Inefficient Regular Expression Complexity vulnerability in Apache Traffic Control.</p><p>This issue affects Apache Traffic Control: all versions.</p><p>People with access to the management interface of the Traffic Router component could specify malicious patterns and cause unavailability.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/mx2jxgnlop2f4vbqnvmrldh4pqmobxvp


### Credits
* Chris Lemmons (finder)


## SQL Injection in Traffic Ops endpoint PUT deliveryservice_request_comments ## { #CVE-2024-45387 }

CVE-2024-45387 [\[CVE json\]](./CVE-2024-45387.cve.json)

_Last updated: 2024-12-23T15:30:11.661Z_

### Affected

* Apache Traffic Control from 8.0.0 through 8.0.1
* Apache Traffic Control from 7.0.0 before 8.0.0


### Description

<div>An SQL injection vulnerability in Traffic Ops in Apache Traffic Control &lt;= 8.0.1, &gt;= 8.0.0 allows a privileged user with role "admin", "federation", "operations", "portal", or "steering" to execute arbitrary SQL against the database by sending a specially-crafted PUT request.</div>Users are recommended to upgrade to version Apache Traffic Control 8.0.2 if you run an affected version of Traffic Ops.

### References
* https://lists.apache.org/thread/t38nk5n7t8w3pb66z7z4pqfzt4443trr


### Credits
* Yuan Luo from Tencent YunDing Security Lab (reporter)


## Server-Side Request Forgery in Traffic Ops endpoint POST /user/login/oauth ## { #CVE-2022-23206 }

CVE-2022-23206 [\[CVE json\]](./CVE-2022-23206.cve.json) [\[OSV json\]](./CVE-2022-23206.osv.json)



_Last updated: 2022-02-06T15:11:05.215Z_

### Affected

* Apache Traffic Control from Traffic Ops before 6.1.0


### Description

In Apache Traffic Control Traffic Ops prior to 6.1.0 or 5.1.6, an unprivileged user who can reach Traffic Ops over HTTPS can send a specially-crafted POST request to /user/login/oauth to scan a port of a server that Traffic Ops can reach.

### References
* https://lists.apache.org/thread/lsrd2mqj29vrvwsh8g0d560vvz8n126f


### Credits
* Apache Traffic Control would like to thank walkerxiong of SecCoder Security Lab for reporting this issue.


## LDAP filter injection vulnerability in Traffic Ops ## { #CVE-2021-43350 }

CVE-2021-43350 [\[CVE json\]](./CVE-2021-43350.cve.json) [\[OSV json\]](./CVE-2021-43350.osv.json)



_Last updated: 2021-11-11T20:52:57.271Z_

### Affected

* Apache Traffic Control from Traffic Ops before 6.0.1


### Description

An unauthenticated Apache Traffic Control Traffic Ops user can send a request with a specially-crafted username to the POST /login endpoint of any API version to inject unsanitized content into the LDAP filter.

### References
* https://trafficcontrol.apache.org/security/


### Credits
* This issue was discovered by Apache Traffic Control user pupiles.


## Apache Traffic Control Traffic Ops Email Injection Vulnerability ## { #CVE-2021-42009 }

CVE-2021-42009 [\[CVE json\]](./CVE-2021-42009.cve.json) [\[OSV json\]](./CVE-2021-42009.osv.json)



_Last updated: 2021-10-12T07:37:49.253Z_

### Affected

* Apache Traffic Control from 4.0.0 before Apache Traffic Control*


### Description

An authenticated Apache Traffic Control Traffic Ops user with Portal-level privileges can send a request with a specially-crafted email subject to the /deliveryservices/request Traffic Ops endpoint to send an email, from the Traffic Ops server, with an arbitrary body to an arbitrary email address. Apache Traffic Control 5.1.x users should upgrade to 5.1.3 or 6.0.0. 4.1.x users should upgrade to 5.1.3.

### References
* https://lists.apache.org/thread.html/re384fd0f44c6d230f31376153c6e8b59e4a669f927c1533d06d702af%40%3Cdev.trafficcontrol.apache.org%3E
* https://lists.apache.org/thread.html/rf0481b9e38ece1ece458d3ce7b2d671df819e3555597f31fc34f084e%40%3Ccommits.trafficcontrol.apache.org%3E


### Credits
* This issue was discovered by GitHub's CodeQL code scanning service.
