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

## Console XXE on Keymaster parameters ## { #CVE-2026-23795 }

CVE-2026-23795 [\[CVE json\]](./CVE-2026-23795.cve.json) [\[OSV json\]](./CVE-2026-23795.osv.json)



_Last updated: 2026-02-03T15:14:33.685Z_

### Affected

* Apache Syncope from 3.0 through 3.0.15
* Apache Syncope from 4.0 through 4.0.3


### Description

<p>Improper Restriction of XML External Entity Reference vulnerability in Apache Syncope Console.<br>An administrator with adequate entitlements to create or edit Keymaster parameters via Console can construct malicious XML text to launch an XXE attack, thereby causing sensitive data leakage occurs.</p><p>This issue affects Apache Syncope: from 3.0 through 3.0.15, from 4.0 through 4.0.3.</p><p>Users are recommended to upgrade to version 3.0.16 / 4.0.4, which fix this issue.</p>

### References
* https://lists.apache.org/thread/mzgbdn8hzk8vr94o660njcc7w62c2pos


### Credits
* follycat (finder)
* Y0n3er (finder)


## Reflected XSS on Enduser Login ## { #CVE-2026-23794 }

CVE-2026-23794 [\[CVE json\]](./CVE-2026-23794.cve.json) [\[OSV json\]](./CVE-2026-23794.osv.json)



_Last updated: 2026-02-03T15:15:22.918Z_

### Affected

* Apache Syncope from 3.0 through 3.0.15
* Apache Syncope from 4.0 through 4.0.3


### Description

<p>Reflected XSS in Apache Syncope's Enduser Login page.<br>An attacker that tricks a legitimate user into clicking a malicious link and logging in to Syncope Enduser could steal that user's credentials.</p><p>This issue affects Apache Syncope: from 3.0 through 3.0.15, from 4.0 through 4.0.3.</p><p>Users are recommended to upgrade to version 3.0.16 / 4.0.4, which fix this issue.</p>

### References
* https://lists.apache.org/thread/7h30ghqdsf3spl3h7gdmscxofrm8ygjo


### Credits
* Kasper Karlsson (finder)
* Karin Taliga (finder)


## Default AES key used for internal password encryption ## { #CVE-2025-65998 }

CVE-2025-65998 [\[CVE json\]](./CVE-2025-65998.cve.json) [\[OSV json\]](./CVE-2025-65998.osv.json)



_Last updated: 2025-11-24T13:46:58.386Z_

### Affected

* Apache Syncope from 2.1 through 2.1.14
* Apache Syncope from 3.0 through 3.0.14
* Apache Syncope from 4.0 through 4.0.2


### Description

<p>Apache Syncope can be configured to store the user password values in the internal database with AES encryption, though this is not the default option.</p><p>When AES is configured, the default key value, hard-coded in the source code, is always used. This allows a malicious attacker, once obtained access to the internal database content, to reconstruct the original cleartext password values.<br>This is not affecting encrypted plain attributes, whose values are also stored using AES encryption.</p><p>Users are recommended to upgrade to version 3.0.15 / 4.0.3, which fix this issue.</p>

### References
* https://lists.apache.org/thread/fjh0tb0d1xkbphc5ogdsc348ppz88cts


### Credits
* Clemens Bergmann (Technical University of Darmstadt) (finder)


## Remote Code Execution by delegated administrators ## { #CVE-2025-57738 }

CVE-2025-57738 [\[CVE json\]](./CVE-2025-57738.cve.json) [\[OSV json\]](./CVE-2025-57738.osv.json)



_Last updated: 2025-10-20T14:43:38.022Z_

### Affected

* Apache Syncope from 2.1 through 2.1.14
* Apache Syncope from 3.0 through 3.0.13
* Apache Syncope from 4.0 through 4.0.1


### Description

Apache Syncope offers the ability to extend / customize the base behavior on every deployment by allowing to provide custom implementations of a few Java interfaces; such implementations can be provided either as Java or Groovy classes, with the latter being particularly attractive as the machinery is set for runtime reload.<br>Such a feature has been available for a while, but recently it was discovered that a malicious administrator can inject Groovy code that can be executed remotely by a running Apache Syncope Core instance.<br>Users are recommended to upgrade to version 3.0.14 / 4.0.2, which fix this issue by forcing the Groovy code to run in a sandbox.

### References
* https://lists.apache.org/thread/x7cv6xv7z76y49grdr1hgj1pzw5zbby6


### Credits
* Mike Cole (Mantel Group) (finder)


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
