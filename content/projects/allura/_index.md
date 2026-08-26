---
title: Apache Allura security advisories
description: Security information for Apache Allura
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Allura? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Allura).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unauthenticated REST disclosure ## { #CVE-2026-75099 }

CVE-2026-75099 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-75099) [\[CVE json\]](./CVE-2026-75099.cve.json) [\[OSV json\]](./CVE-2026-75099.osv.json)



_Last updated: 2026-08-24T16:42:15.529Z_

### Affected

* Apache Allura through 1.19.1


### Description

<p><span>Unauthenticated REST disclosure</span>&nbsp;of certain content items in Apache Allura.</p><p>This issue affects Apache Allura: through 1.19.1.</p><p>Users are recommended to upgrade to version 1.20.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lnsfx58o6mx6m44qk4vzqrq8ccmrywcy


### Credits
* Venkatraman Kumar, securin.io (finder)


## Git command injection ## { #CVE-2026-73240 }

CVE-2026-73240 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73240) [\[CVE json\]](./CVE-2026-73240.cve.json) [\[OSV json\]](./CVE-2026-73240.osv.json)



_Last updated: 2026-08-12T16:41:16.893Z_

### Affected

* Apache Allura before 1.19.1


### Description

<p>Specifically crafted inputs may lead to git argument injection in Apache Allura.</p><p>This issue affects Apache Allura: before 1.19.1.</p><p>Users are recommended to upgrade to version 1.19.1, which fixes the issue.</p>

### References
* https://allura.apache.org/posts/2026-allura-1.19.1.html
* https://lists.apache.org/thread/10gnxblhomk2z4gxcyyb4t3p4zxsdddv


## Missing permission checks IDOR ## { #CVE-2026-73239 }

CVE-2026-73239 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73239) [\[CVE json\]](./CVE-2026-73239.cve.json) [\[OSV json\]](./CVE-2026-73239.osv.json)



_Last updated: 2026-08-12T16:41:39.780Z_

### Affected

* Apache Allura before 1.19.1


### Description

<p>Insecure Direct Object Reference (IDOR) due to missing permission checks for multiple Artifact types&nbsp;in Apache Allura.</p><p>This issue affects Apache Allura: before 1.19.1.</p><p>Users are recommended to upgrade to version 1.19.1, which fixes the issue.</p>

### References
* https://allura.apache.org/posts/2026-allura-1.19.1.html
* https://lists.apache.org/thread/ryn6yomo897d43ovrd47g02t8ycmbxb3


## XSS in code display ## { #CVE-2026-73238 }

CVE-2026-73238 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73238) [\[CVE json\]](./CVE-2026-73238.cve.json) [\[OSV json\]](./CVE-2026-73238.osv.json)



_Last updated: 2026-08-12T16:41:57.464Z_

### Affected

* Apache Allura before 1.19.1


### Description

<p>XSS vulnerability in code display in Apache Allura.</p><p>This issue affects Apache Allura: before 1.19.1.</p><p>Users are recommended to upgrade to version 1.19.1, which fixes the issue.</p>

### References
* https://allura.apache.org/posts/2026-allura-1.19.1.html
* https://lists.apache.org/thread/bbzhnvqlwvwbprnfg4g41s8wkc5bdfmk


## XSS in markdown pipeline ## { #CVE-2026-73237 }

CVE-2026-73237 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73237) [\[CVE json\]](./CVE-2026-73237.cve.json) [\[OSV json\]](./CVE-2026-73237.osv.json)



_Last updated: 2026-08-12T16:42:26.194Z_

### Affected

* Apache Allura from 1.10.0 before 1.19.1


### Description

<p>XSS vulnerability in Markdown handling in Apache Allura.</p><p>This issue affects Apache Allura: from 1.10.0 before 1.19.1.</p><p>Users are recommended to upgrade to version 1.19.1, which fixes the issue.</p>

### References
* https://allura.apache.org/posts/2026-allura-1.19.1.html
* https://lists.apache.org/thread/p7bd1yz9v9wbsbc6hz3tjxozxnwyzqz0


## Server-side request forgery ## { #CVE-2026-69223 }

CVE-2026-69223 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-69223) [\[CVE json\]](./CVE-2026-69223.cve.json) [\[OSV json\]](./CVE-2026-69223.osv.json)



_Last updated: 2026-08-11T17:03:03.256Z_

### Affected

* Apache Allura before 1.19.1


### Description

<p>Apache Allura's webhooks are vulnerable to&nbsp;Server-Side Request Forgery (SSRF).</p><p>This issue affects Apache Allura: before 1.19.1.</p><p>Users are recommended to upgrade to version 1.19.1, which fixes the issue.</p>

### References
* https://allura.apache.org/posts/2026-allura-1.19.1.html
* https://lists.apache.org/thread/9xpltfm6nombd7rdrx5o0hh8kxmm82pb


## Stored authenticated XSS ## { #CVE-2024-38379 }

CVE-2024-38379 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-38379) [\[CVE json\]](./CVE-2024-38379.cve.json) [\[OSV json\]](./CVE-2024-38379.osv.json)



_Last updated: 2025-02-06T14:32:32.361Z_

### Affected

* Apache Allura from 1.4.0 through 1.17.0


### Description

<p>Apache Allura's neighborhood settings are vulnerable to a stored XSS attack.&nbsp; Only neighborhood admins can access these settings, so the scope of risk is limited to configurations where neighborhood admins are not fully trusted.<br></p><p>This issue affects Apache Allura: from 1.4.0 through 1.17.0.</p><p>Users are recommended to upgrade to version 1.17.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/2lb6vp00sj2b2snpmhff5lyortxjsnrp


### Credits
* Ömer "WASP" Akincir (finder)


## sensitive information exposure via DNS rebinding ## { #CVE-2024-36471 }

CVE-2024-36471 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-36471) [\[CVE json\]](./CVE-2024-36471.cve.json) [\[OSV json\]](./CVE-2024-36471.osv.json)



_Last updated: 2024-06-10T21:55:03.113Z_

### Affected

* Apache Allura from 1.0.1 through 1.16.0


### Description

<div>Import functionality is vulnerable to DNS rebinding attacks between verification and processing of the URL.&nbsp; Project administrators can run these imports, which could cause Allura to read from internal services and expose them.<br></div><div><br></div><div>This issue affects Apache Allura from 1.0.1 through 1.16.0.</div><p></p><p>Users are recommended to upgrade to version 1.17.0, which fixes the issue.  If you are unable to upgrade, set "disable_entry_points.allura.importers = forge-tracker, forge-discussion" in your .ini config file.<br></p><br>

### References
* https://lists.apache.org/thread/g43164t4bcp0tjwt4opxyks4svm8kvbh


### Credits
* truff https://x.com/truffzor (finder)


## sensitive information exposure via import ## { #CVE-2023-46851 }

CVE-2023-46851 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-46851) [\[CVE json\]](./CVE-2023-46851.cve.json) [\[OSV json\]](./CVE-2023-46851.osv.json)



_Last updated: 2023-11-07T08:56:30.662Z_

### Affected

* Apache Allura from 1.0.1 through 1.15.0


### Description

<div>Allura Discussion and Allura Forum importing does not restrict URL values specified in attachments. Project administrators can run these imports, which could cause Allura to read local files and expose them.&nbsp; Exposing internal files then can lead to other exploits, like session hijacking, or remote code execution.<br></div><div><br></div><div>This issue affects Apache Allura from 1.0.1 through 1.15.0.</div><p></p><p>Users are recommended to upgrade to version 1.16.0, which fixes the issue.&nbsp; If you are unable to upgrade, set "disable_entry_points.allura.importers = forge-tracker, forge-discussion" in your .ini config file.<br></p>

### References
* https://allura.apache.org/posts/2023-allura-1.16.0.html
* https://lists.apache.org/thread/hqk0vltl7qgrq215zgwjfoj0khbov0gx


### Credits
* Stefan Schiller (Sonar) (finder)
