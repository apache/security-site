---
title: Apache XML Graphics security advisories
description: Security information for Apache XML Graphics
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache XML Graphics? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=XML%20Graphics).

You can read more about the security policy on:

- [Apache XML Graphics security model](https://xmlgraphics.apache.org/security.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Temporary files on Unix-like systems are readable by other local users ## { #CVE-2026-126627 }

CVE-2026-126627 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-126627) [\[CVE json\]](./CVE-2026-126627.cve.json) [\[OSV json\]](./CVE-2026-126627.osv.json)



_Last updated: 2026-11-11T11:23:15.631Z_

### Affected

* Apache XML Graphics FOP through 2.11.0


### Description

<p>Creation of Temporary File With Insecure Permissions vulnerability in Apache XML Graphics FOP.</p><p>This issue affects Apache XML Graphics FOP: through 2.11.</p><p>Users are recommended to upgrade to version 2.12, which fixes the issue.</p>

### References
* https://issues.apache.org/jira/browse/FOP-3284
* https://lists.apache.org/thread.html/f8mys56y18wjmp1wzg4qmx6hhyjxgo0f


### Credits
* https://github.com/vlsi (finder)


## Denial of Service via SVG Element Reference Resolution ## { #CVE-2026-111792 }

CVE-2026-111792 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111792) [\[CVE json\]](./CVE-2026-111792.cve.json) [\[OSV json\]](./CVE-2026-111792.osv.json)



_Last updated: 2026-11-11T10:46:53.437Z_

### Affected

* Apache XML Graphics Batik through 1.19.0


### Description

<p>Uncontrolled Recursion vulnerability in Apache XML Graphics Batik.</p><p>This issue affects Apache XML Graphics Batik: through 1.19.</p><p>Users are recommended to upgrade to version 1.20, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/dn70ltz1o9sg88dd87wcyh4v73fk2tnm
* https://issues.apache.org/jira/browse/BATIK-1397


### Credits
* MopMonk-AI (finder)


## Harden validation in SAXDocumentFactory ## { #CVE-2026-90993 }

CVE-2026-90993 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90993) [\[CVE json\]](./CVE-2026-90993.cve.json) [\[OSV json\]](./CVE-2026-90993.osv.json)



_Last updated: 2026-11-11T10:20:07.846Z_

### Affected

* Apache XML Graphics Batik through 1.19.0


### Description

<p>XXE vulnerability in Apache XML Graphics Batik.</p><p>This issue affects Apache XML Graphics Batik: through 1.19.</p><p>Users are recommended to upgrade to version 1.20, which fixes the issue.</p>

### References
* https://issues.apache.org/jira/browse/BATIK-1399
* https://lists.apache.org/thread.html/cnl5g2os5w048h32x50v1xgjnyo8y6vs


## Check url protocol when loading document ## { #CVE-2026-89326 }

CVE-2026-89326 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-89326) [\[CVE json\]](./CVE-2026-89326.cve.json) [\[OSV json\]](./CVE-2026-89326.osv.json)



_Last updated: 2026-11-11T14:57:39.709Z_

### Affected

* Apache XML Graphics Batik through 1.19.0


### Description

<p>Origin Validation Error vulnerability in Apache XML Graphics Batik: the external resource same-origin check does not compare the URL protocol</p><p>This issue affects Apache XML Graphics Batik: through 1.19.</p><p>Users are recommended to upgrade to version 1.20, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/j52wbxhp9wmysor6kdyqjnjz7pqnsthj
* https://issues.apache.org/jira/browse/BATIK-1398


## CWE-502 unsafe deserialization in hyphenation loading ## { #CVE-2026-71395 }

CVE-2026-71395 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-71395) [\[CVE json\]](./CVE-2026-71395.cve.json) [\[OSV json\]](./CVE-2026-71395.osv.json)



_Last updated: 2026-11-11T14:53:50.662Z_

### Affected

* Apache XML Graphics FOP through 2.11.0


### Description

<p>unsafe deserialization in hyphenation loading vulnerability in Apache XML Graphics FOP.</p><p>This issue affects Apache XML Graphics FOP: through 2.11.</p><p>Users are recommended to upgrade to version 2.12, which fixes the issue.</p>

### References
* https://issues.apache.org/jira/browse/FOP-3332
* https://lists.apache.org/thread.html/nsb89to1r0vzdh3t4w7x10q4z3xk5jqf


## SVG color-profile xml:base bypasses Batik external resource same-origin checks ## { #CVE-2026-49236 }

CVE-2026-49236 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49236) [\[CVE json\]](./CVE-2026-49236.cve.json) [\[OSV json\]](./CVE-2026-49236.osv.json)



_Last updated: 2026-11-11T13:23:37.232Z_

### Affected

* Apache XML Graphics Batik through 1.19.0


### Description

<p>Server-Side Request Forgery (SSRF) vulnerability in Apache XML Graphics Batik.&nbsp;SVG color-profile xml:base bypasses Batik external resource same-origin checks</p><p>This issue affects Apache XML Graphics Batik: through 1.19.</p><p>Users are recommended to upgrade to version 1.20, which fixes the issue.</p>

### References
* https://issues.apache.org/jira/browse/BATIK-1394
* https://lists.apache.org/thread.html/xpysqx09ycpj23qk6b10k87pssqx0dk2


## SSRF Vulnerability in Apache Batik ## { #CVE-2026-44929 }

CVE-2026-44929 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44929) [\[CVE json\]](./CVE-2026-44929.cve.json) [\[OSV json\]](./CVE-2026-44929.osv.json)



_Last updated: 2026-11-11T14:46:31.641Z_

### Affected

* Apache XML Graphics Batik through 1.19.0


### Description

<p>Server-Side Request Forgery (SSRF) vulnerability in Apache XML Graphics Batik.</p><p>This issue affects Apache XML Graphics Batik: through 1.19.</p><p>Users are recommended to upgrade to version 1.20, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/d9zfzmjr8frhylopnq4r7ojwcfk9hbjg
* https://issues.apache.org/jira/browse/BATIK-1393


## Cross-Site Scripting via Unencoded Font Metadata in Apache Batik SVGFont ## { #CVE-2026-40853 }

CVE-2026-40853 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40853) [\[CVE json\]](./CVE-2026-40853.cve.json) [\[OSV json\]](./CVE-2026-40853.osv.json)



_Last updated: 2026-11-11T13:16:12.411Z_

### Affected

* Apache XML Graphics Batik through 1.19.0


### Description

<p>A&nbsp;Cross-Site Scripting via Unencoded Font Metadata in Apache Batik SVGFont.</p><p>This issue affects Apache XML Graphics Batik: through 1.19.</p><p>Users are recommended to upgrade to version 1.20, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/donct9w5lp5rlvl1p7m8cfx380d2wy4c


## XML External Entity (XXE) Processing ## { #CVE-2024-28168 }

CVE-2024-28168 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-28168) [\[CVE json\]](./CVE-2024-28168.cve.json) [\[OSV json\]](./CVE-2024-28168.osv.json)



_Last updated: 2024-10-09T12:04:02.004Z_

### Affected

* Apache XML Graphics FOP at 2.9


### Description

<p>Improper Restriction of XML External Entity Reference ('XXE') vulnerability in Apache XML Graphics FOP.</p><p>This issue affects Apache XML Graphics FOP: 2.9.</p><p>Users are recommended to upgrade to version 2.10, which fixes the issue.</p>

### References
* https://xmlgraphics.apache.org/security.html


### Credits
* c1gar of Shanxi Normal University (finder)


## Information disclosure vulnerability ## { #CVE-2022-44730 }

CVE-2022-44730 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-44730) [\[CVE json\]](./CVE-2022-44730.cve.json) [\[OSV json\]](./CVE-2022-44730.osv.json)



_Last updated: 2026-10-20T07:35:03.123Z_

### Affected

* Apache XML Graphics Batik at 1.16


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache Software Foundation Apache XML Graphics Batik.<p>This issue affects Apache XML Graphics Batik: 1.16.<br></p><p>A malicious SVG can probe user profile / data and send it directly as parameter to a URL.<br></p>

### References
* https://lists.apache.org/thread/58m5817jr059f4v1zogh0fngj9pwjyj0
* https://xmlgraphics.apache.org/security.html


## Information disclosure vulnerability ## { #CVE-2022-44729 }

CVE-2022-44729 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-44729) [\[CVE json\]](./CVE-2022-44729.cve.json) [\[OSV json\]](./CVE-2022-44729.osv.json)



_Last updated: 2026-11-11T08:14:13.183Z_

### Affected

* Apache XML Graphics Batik at 1.16


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache Software Foundation Apache XML Graphics Batik.<p>This issue affects Apache XML Graphics Batik: 1.16.</p><p>On version 1.16, a malicious SVG could trigger loading external resources by default, causing resource consumption or in some cases even information disclosure. Users are recommended to upgrade to version 1.17 or later.<br></p>

### References
* https://xmlgraphics.apache.org/security.html
* https://lists.apache.org/thread/hco2nw1typoorz33qzs0fcdx0ws6d6j2


### Credits
* nbxiglk (finder)


## Apache Batik prior to 1.16 allows RCE via scripting ## { #CVE-2022-42890 }

CVE-2022-42890 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-42890) [\[CVE json\]](./CVE-2022-42890.cve.json) [\[OSV json\]](./CVE-2022-42890.osv.json)



_Last updated: 2022-10-25T11:25:19.555Z_

### Affected

* Apache XML Graphics from Batik through 1.15


### Description

A vulnerability in Batik of Apache XML Graphics allows an attacker to run Java code from untrusted SVG via JavaScript.  This issue affects Apache XML Graphics prior to 1.16. Users are recommended to upgrade to version 1.16.

### References
* https://lists.apache.org/thread/pkvhy0nsj1h1mlon008wtzhosbtxjwly


### Credits
* This issue was independently reported by Y4tacker and 4ra1n of Chaitin Tech


## Apache Batik prior to 1.16 allows RCE when loading untrusted SVG input ## { #CVE-2022-41704 }

CVE-2022-41704 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-41704) [\[CVE json\]](./CVE-2022-41704.cve.json) [\[OSV json\]](./CVE-2022-41704.osv.json)



_Last updated: 2022-10-25T11:02:56.969Z_

### Affected

* Apache XML Graphics from Batik through 1.15


### Description

A vulnerability in Batik of Apache XML Graphics allows an attacker to run untrusted Java code from an SVG. This issue affects Apache XML Graphics prior to 1.16. It is recommended to update to version 1.16.

### References
* https://lists.apache.org/thread/hplhx0o74jb7blj39fm4kw3otcnjd6xf


### Credits
* This issue was independently reported by 4ra1n of Chaitin Tech and pwnull


## Jar url should be blocked by DefaultScriptSecurity ## { #CVE-2022-40146 }

CVE-2022-40146 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-40146) [\[CVE json\]](./CVE-2022-40146.cve.json) [\[OSV json\]](./CVE-2022-40146.osv.json)



_Last updated: 2022-11-23T18:09:53.965Z_

### Affected

* Apache XML Graphics at Batik 1.14


### Description

Server-Side Request Forgery (SSRF) vulnerability in Batik of Apache XML Graphics allows an attacker to access files using a Jar url.  This issue affects Apache XML Graphics Batik 1.14. Only affects the batik-bridge component.

### References
* https://lists.apache.org/thread/hxtddqjty2sbs12y97c8g7xfh17jzxsx


## PDFTranscoder does not block external resources ## { #CVE-2022-38648 }

CVE-2022-38648 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-38648) [\[CVE json\]](./CVE-2022-38648.cve.json) [\[OSV json\]](./CVE-2022-38648.osv.json)



_Last updated: 2022-09-22T14:37:30.540Z_

### Affected

* Apache XML Graphics at Batik 1.14


### Description

Server-Side Request Forgery (SSRF) vulnerability in Batik of Apache XML Graphics allows an attacker to fetch external resources.  This issue affects Apache XML Graphics Batik 1.14.

### References
* https://lists.apache.org/thread/gfsktxvj7jtwyovmhhbrw0bs13wfjd7b


## Server-Side Request Forgery Information Disclosure Vulnerability ## { #CVE-2022-38398 }

CVE-2022-38398 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-38398) [\[CVE json\]](./CVE-2022-38398.cve.json) [\[OSV json\]](./CVE-2022-38398.osv.json)



_Last updated: 2022-09-22T14:36:45.719Z_

### Affected

* Apache XML Graphics at Batik 1.14


### Description

Server-Side Request Forgery (SSRF) vulnerability in Batik of Apache XML Graphics allows an attacker to load a url thru the jar protocol.  This issue affects Apache XML Graphics Batik 1.14.

### References
* https://lists.apache.org/thread/712c9xwtmyghyokzrm2ml6sps4xlmbsx
