---
title: Apache OpenMeetings security advisories
description: Security information for Apache OpenMeetings
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache OpenMeetings? You can read more about the projects' security policy on their [security page](https://openmeetings.apache.org/security.html), and email your report to the  [Apache OpenMeetings Security Team](mailto:security@openmeetings.apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache OpenMeetings since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. It may also lack details found on the [project security page](https://openmeetings.apache.org/security.html).

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## allows user impersonation ## { #CVE-2023-28326 }

[CVE-2023-28326](./CVE-2023-28326.cve.json)

### Affected

* Apache OpenMeetings versions 2.0.0 before 7.0.0


### Description

<p>Vendor: The Apache Software Foundation</p><p>Versions Affected: Apache OpenMeetings from 2.0.0 before 7.0.0</p><p>Description: Attacker can elevate their privileges in any room</p><br>

## insufficient check of invitation hash ## { #CVE-2023-28936 }

[CVE-2023-28936](./CVE-2023-28936.cve.json)

### Affected

* Apache OpenMeetings versions 2.0.0 before 7.1.0


### Description

Attacker can access arbitrary recording/room<br><br>Vendor: The Apache Software Foundation<br><br>Versions&nbsp;Affected: Apache OpenMeetings from 2.0.0 before 7.1.0<br>

## allows bypass authentication ## { #CVE-2023-29032 }

[CVE-2023-29032](./CVE-2023-29032.cve.json)

### Affected

* Apache OpenMeetings versions 3.1.3 before 7.1.0


### Description

<span style="background-color: rgb(255, 255, 255);">An attacker that has gained access to certain private information can use this to act as other user.</span><br><br>Vendor: The Apache Software Foundation<br><br>Versions Affected: Apache OpenMeetings from 3.1.3 before 7.1.0

## allows null-byte Injection ## { #CVE-2023-29246 }

[CVE-2023-29246](./CVE-2023-29246.cve.json)

### Affected

* Apache OpenMeetings versions 2.0.0 before 7.1.0


### Description

<span style="background-color: rgb(255, 255, 255);">An attacker who has gained access to an admin account can perform RCE via null-byte injection</span><br><br>Vendor: The Apache Software Foundation<br><br>Versions Affected: Apache OpenMeetings from 2.0.0 before 7.1.0