---
title: Apache Syncope security advisories
description: Security information for Apache Syncope
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Syncope? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## HTML tags can be injected into Console or Enduser text fields ## { #CVE-2024-38503 }

CVE-2024-38503 [\[CVE json\]](./CVE-2024-38503.cve.json) [\[OSV json\]](./CVE-2024-38503.osv.json)



_Last updated: 2024-09-11T11:11:10.160Z_

### Affected

* Apache Syncope from 2.1 through 2.1.14
* Apache Syncope from 3.0 through 3.0.7


### Description

When editing a user, group or any object in the Syncope Console, HTML tags could be added to any text field and could lead to potential exploits.<br>The same vulnerability was found in the Syncope Enduser, when editing “Personal Information” or “User Requests”.<br><br>Users are recommended to upgrade to version 3.0.8, which fixes this issue.

### References
* https://syncope.apache.org/security#cve-2024-38503-html-tags-can-be-injected-into-console-or-enduser


### Credits
* Basalt IT-Security Team (finder)


## Stored XSS in Console and Enduser ## { #CVE-2024-45031 }

CVE-2024-45031 [\[CVE json\]](./CVE-2024-45031.cve.json) [\[OSV json\]](./CVE-2024-45031.osv.json)



_Last updated: 2025-09-01T09:41:27.665Z_

### Affected

* Apache Syncope from 2.1 through 2.1.14
* Apache Syncope from 3.0 through 3.0.8


### Description

When editing objects in the Syncope Console, incomplete HTML tags could be used to bypass HTML sanitization. This made it possible to inject stored XSS payloads which would trigger for other users during ordinary usage of the application.<br>XSS payloads could also be injected in Syncope Enduser when editing “Personal Information” or “User Requests”: such payloads would trigger for administrators in Syncope Console, thus enabling session hijacking.<br><br>Users are recommended to upgrade to version 3.0.9, which fixes this issue.

### References
* https://lists.apache.org/thread/fn567pfmo3s55ofkc42drz8b4kgbhp9m


### Credits
* Kasper Karlsson, Omegapoint (finder)
* Pontus Hanssen, Omegapoint (finder)
