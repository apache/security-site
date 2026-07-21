---
title: Apache Syncope security advisories
description: Security information for Apache Syncope
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Syncope? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Syncope).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## RCE via Groovy Sandbox bypass ## { #CVE-2026-63071 }

CVE-2026-63071 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-63071) [\[CVE json\]](./CVE-2026-63071.cve.json) [\[OSV json\]](./CVE-2026-63071.osv.json)



_Last updated: 2026-07-20T14:19:15.560Z_

### Affected

* Apache Syncope from 3.0.0-M0 through 3.0.16
* Apache Syncope from 4.0.0-M0 through 4.0.6
* Apache Syncope from 4.1.0-M0 through 4.1.1


### Description

<p>Improper Isolation or Compartmentalization vulnerability in Apache Syncope.<br><br>An administrator with adequate entitlements for Implementations can create a malicious Groovy class containing untrusted code bypassing the Groovy security sandbox.</p><p>This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 through 4.0.6, from 4.1.0-M0 through 4.1.1.</p><p>Users are recommended to upgrade to version 4.0.7 / 4.1.2, which fix this issue by tightening the Groovy security sandbox.</p>

### References
* https://lists.apache.org/thread/2236mlm6hbvs6g16yqz5y9s8bb7q1lo1


### Credits
* elin kai (finder)
* 无聊 (finder)


## Low-privileged authenticated SSRF in Connectors and Resources check ## { #CVE-2026-62418 }

CVE-2026-62418 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-62418) [\[CVE json\]](./CVE-2026-62418.cve.json) [\[OSV json\]](./CVE-2026-62418.osv.json)



_Last updated: 2026-07-20T14:27:00.668Z_

### Affected

* Apache Syncope from 3.0.0-M0 through 3.0.16
* Apache Syncope from 4.0.0-M0 through 4.0.6
* Apache Syncope from 4.1.0-M0 through 4.1.1


### Description

<p></p><p>Low-privileged authenticated Server-Side Request Forgery (SSRF) 
vulnerability in Apache Syncope via Connectors and Resources check.</p>

<p>This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.6, from 4.1.0-M0 through 4.1.1.</p>

<p>Users are recommended to upgrade to version 4.0.7 / 4.1.2, which fix this issue.</p><p></p>

### References
* https://lists.apache.org/thread/n632drbsmfr6t3p6jt6jwbjvokqdyszb


### Credits
* Adrián Leal Castaño (finder)


## User self-service privilege escalation ## { #CVE-2026-62183 }

CVE-2026-62183 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-62183) [\[CVE json\]](./CVE-2026-62183.cve.json) [\[OSV json\]](./CVE-2026-62183.osv.json)



_Last updated: 2026-07-20T14:23:15.458Z_

### Affected

* Apache Syncope from 3.0.0-M0 through 3.0.16
* Apache Syncope from 4.0.0-M0 through 4.0.6
* Apache Syncope from 4.1.0-M0 through 4.1.1


### Description

<p>Improper Privilege Management vulnerability in Apache Syncope.<br><br>When:<br><br>* the all-Java user workflow adapter is configured, or<br>* the Flowable user workflow adapter is configured, bearing a BPMN definition not requiring admin approval for user self registration of self update requests</p>the following scenario could happen.<br><div>A REST API call can allow the user to grant themselves one or more of defined Roles, thus gaining their Entitlements and becoming in fact an administrator; the actual Entitlements gained depend on the Roles that are effectively defined on the specific Syncope deployment.</div><div><br>This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.6, from 4.1.0-M0 through 4.1.1.<br><br>Users are recommended to upgrade to version 4.0.7 / 4.1.2, which fix this issue.<br></div>

### References
* https://lists.apache.org/thread/6r8cngvy43y2yk4jj3w060dt8vx0yzpr


### Credits
* Nic Jones (finder)
* elin kai (finder)


## SQL injection vulnerability in Audit Events search ## { #CVE-2026-57308 }

CVE-2026-57308 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57308) [\[CVE json\]](./CVE-2026-57308.cve.json) [\[OSV json\]](./CVE-2026-57308.osv.json)



_Last updated: 2026-07-20T14:21:50.872Z_

### Affected

* Apache Syncope from 3.0.0-M0 through 3.0.16
* Apache Syncope from 4.0.0-M0 through 4.0.6
* Apache Syncope from 4.1.0-M0 through 4.1.1


### Description

<p>Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Syncope.</p><p>An administrator with adequate entitlements can achieve&nbsp;execution of arbitrary SQL via stacked queries, leveraging unsanitized sort parameters.</p><p>This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.6, from 4.1.0-M0 through 4.1.1.<br></p><p>Users are recommended to upgrade to version 4.0.7 / 4.1.2, which fix this issue.</p>

### References
* https://lists.apache.org/thread/g0gpctj90pbczbjl5jr33t8gr1gltg8v


### Credits
* Lennart Hostettler (finder)


## Remote Code Execution via Scripted Connector ## { #CVE-2026-53421 }

CVE-2026-53421 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-53421) [\[CVE json\]](./CVE-2026-53421.cve.json) [\[OSV json\]](./CVE-2026-53421.osv.json)



_Last updated: 2026-07-20T14:21:06.192Z_

### Affected

* Apache Syncope from 3.0.0-M0 through 3.0.16
* Apache Syncope from 4.0.0-M0 through 4.0.6
* Apache Syncope from 4.1.0-M0 through 4.1.1


### Description

<p>Improper Isolation or Compartmentalization vulnerability in Apache Syncope.</p><p></p><p>An administrator with adequate entitlements can achieve remote code execution through the connector subsystem by relying on scripted connectors' (REST and SQL) capability to run Groovy scripts.<br><br>This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.6, from 4.1.0-M0 through 4.1.1.<br></p><p></p><p>Users are recommended to upgrade to version 4.0.7 / 4.1.2, which fix this issue by hardening the Groovy security sandbox.</p><p></p>

### References
* https://lists.apache.org/thread/nmzvz6gb2ldm30wvyk613r8dfrb6r8yx


### Credits
* follycat, Y0n3er (finder)


## Remote Code Execution via Flowable BPMN Groovy ScriptTask ## { #CVE-2026-53405 }

CVE-2026-53405 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-53405) [\[CVE json\]](./CVE-2026-53405.cve.json) [\[OSV json\]](./CVE-2026-53405.osv.json)



_Last updated: 2026-07-20T14:20:04.039Z_

### Affected

* Apache Syncope from 3.0.0-M0 through 3.0.16
* Apache Syncope from 4.0.0-M0 through 4.0.6
* Apache Syncope from 4.1.0-M0 through 4.1.1


### Description

<p>Improper Isolation or Compartmentalization vulnerability in Apache Syncope.</p><p>An administrator with adequate entitlements can import arbitrary BPMN process definitions via the REST API and then start the process. When a BPMN process containing a Groovy scriptTask is imported and&nbsp;started, the Groovy script is executed directly on the server, with no sandbox.<br></p><p>This issue affects Apache Syncope: from 3.0.0-M0 through 3.0.16, from 4.0.0-M0 Through 4.0.6, from 4.1.0-M0 through 4.1.1.<br></p><p></p><p>Users are recommended to upgrade to version 4.0.7 / 4.1.2, which fix this issue by wrapping Flowable's&nbsp;Groovy scriptTasks with security sandbox.</p>

### References
* https://lists.apache.org/thread/vdq0tk6ylffz6trbgbllj9kb1ndzff7k


### Credits
* follycat, Y0n3er (finder)


## JexlContextBuilder Information Disclosure ## { #CVE-2026-42797 }

CVE-2026-42797 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42797) [\[CVE json\]](./CVE-2026-42797.cve.json) [\[OSV json\]](./CVE-2026-42797.osv.json)



_Last updated: 2026-05-25T15:01:00.581Z_

### Affected

* Apache Syncope from 3.0 through 3.0.16
* Apache Syncope from 4.0 through 4.0.5
* Apache Syncope from 4.1 through 4.1.0


### Description

<p>Exposure of Sensitive Information Through Data Queries vulnerability in Apache Syncope.</p><p>An administrator with adequate entitlements for Derived Schemas can create a malicious JEXL expression which allows any administrator with sufficient entitlements for User read to access User-related security-sensitive information.</p><p>This issue affects Apache Syncope: 3.0 through 3.0.16, 4.0 through 4.0.5, 4.1.0.</p><p>Users are recommended to upgrade to version 4.0.6 / 4.1.1, which fix this issue by further restricting the JEXL expression definition.</p>

### References
* https://lists.apache.org/thread/5y7d277sntyytrmxnx2tfjr9ftcpq1s6


### Credits
* elin kai (finder)


## Post-auth RCE via Groovy static ## { #CVE-2026-42782 }

CVE-2026-42782 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42782) [\[CVE json\]](./CVE-2026-42782.cve.json) [\[OSV json\]](./CVE-2026-42782.osv.json)



_Last updated: 2026-05-25T14:59:04.113Z_

### Affected

* Apache Syncope from 3.0 through 3.0.16
* Apache Syncope from 4.0 through 4.0.5
* Apache Syncope from 4.1 through 4.1.0


### Description

<p>Improper Isolation or Compartmentalization vulnerability in Apache Syncope.</p><p>An administrator with adequate entitlements for Implementations can create a malicious Groovy class containing&nbsp;untrusted code reaching a non-sandboxed execution path via the class static initializer.</p><p>This issue affects Apache Syncope: 3.0 through 3.0.16, 4.0 through 4.0.5, 4.1.0.</p><p></p><p>Users are recommended to upgrade to version 4.0.6 / 4.1.1, which fix this issue by forcing even the static initializer in Groovy code to run in a sandbox.</p>

### References
* https://lists.apache.org/thread/b869ms0ofrd129f7tgsn9flxgv9ztg2r


### Credits
* Trung Nguyen, CyStack (finder)


## Console XXE on Keymaster parameters ## { #CVE-2026-23795 }

CVE-2026-23795 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-23795) [\[CVE json\]](./CVE-2026-23795.cve.json) [\[OSV json\]](./CVE-2026-23795.osv.json)



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

CVE-2026-23794 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-23794) [\[CVE json\]](./CVE-2026-23794.cve.json) [\[OSV json\]](./CVE-2026-23794.osv.json)



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

CVE-2025-65998 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-65998) [\[CVE json\]](./CVE-2025-65998.cve.json) [\[OSV json\]](./CVE-2025-65998.osv.json)



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

CVE-2025-57738 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-57738) [\[CVE json\]](./CVE-2025-57738.cve.json) [\[OSV json\]](./CVE-2025-57738.osv.json)



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

CVE-2024-45031 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45031) [\[CVE json\]](./CVE-2024-45031.cve.json) [\[OSV json\]](./CVE-2024-45031.osv.json)



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

CVE-2024-38503 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-38503) [\[CVE json\]](./CVE-2024-38503.cve.json)

_Last updated: 2024-09-11T11:11:10.160Z_

### Affected

* Apache Syncope from 2.1 through 2.1.14
* Apache Syncope from 3.0 through 3.0.7


### Description

When editing a user, group or any object in the Syncope Console, HTML tags could be added to any text field and could lead to potential exploits.<br>The same vulnerability was found in the Syncope Enduser, when editing “Personal Information” or “User Requests”.<br><br>Users are recommended to upgrade to version 3.0.8, which fixes this issue.

### References
* https://syncope.apache.org/security#cve-2024-38503-html-tags-can-be-injected-into-console-or-enduser
* https://www.openwall.com/lists/oss-security/2024/07/22/3


### Credits
* Basalt IT-Security Team (finder)
