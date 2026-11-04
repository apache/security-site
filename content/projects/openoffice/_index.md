---
title: Apache OpenOffice security advisories
description: Security information for Apache OpenOffice
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache OpenOffice? Send your report to the [Apache OpenOffice Security Team](mailto:security@openoffice.apache.org?subject=OpenOffice).

You can read more about the security policy on:

- [Apache OpenOffice security model](https://openoffice.apache.org/security)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Out-of-bounds write when importing encrypted PDF files ## { #CVE-2026-90634 }

CVE-2026-90634 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90634) [\[CVE json\]](./CVE-2026-90634.cve.json) [\[OSV json\]](./CVE-2026-90634.osv.json)



_Last updated: 2026-11-04T11:04:36.913Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

An uncontrolled memory access in the PDF import code of Apache OpenOffice versions through 4.1.16 allows a crafted PDF to cause an out-of-bounds memory write, causing program crash or memory corruption.<br>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/1c0lropx46w8ozwk29p5yw1xlq4wnbll


### Credits
* Anonymous working with TrendAI Zero Day Initiative (finder)


## Local file inclusion via GStreamer plugin ## { #CVE-2026-90632 }

CVE-2026-90632 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90632) [\[CVE json\]](./CVE-2026-90632.cve.json) [\[OSV json\]](./CVE-2026-90632.osv.json)



_Last updated: 2026-11-04T11:04:59.711Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

<div>Apache OpenOffice documents can include multimedia content (audio, video, etc.)</div><div>A crafted document could exploit the GStreamer multimedia component of Apache OpenOffice version through 4.1.16 to load the contents of any local file, and include them when the document is saved or exported, for example as PDF.</div>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/9rrjtmlnmg47m6soyrl83rz28dbsyqvk


### Credits
* Edoardo Geraci and Thomas Rinsma of Codean Labs (finder)


## Remote document loaded without prompt, possibiy leaking environment variables ## { #CVE-2026-90631 }

CVE-2026-90631 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90631) [\[CVE json\]](./CVE-2026-90631.cve.json) [\[OSV json\]](./CVE-2026-90631.osv.json)



_Last updated: 2026-11-04T11:04:27.889Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

<p>Apache OpenOffice documents can contain links. A missing Authorization vulnerability in Apache OpenOffice allowed an attacker to craft a document that would cause external links 
to be loaded without prompt, possibly transferring the contents of environment variables in the process.</p><p>This issue affects Apache OpenOffice: through 4.1.16.</p><p>Users are recommended to upgrade to version 4.1.17, which fixes the issue.</p><br>

### References
* https://lists.apache.org/thread.html/j19rrk8jwrlg41tj6rfdcccj8cyyxhz9


### Credits
* Edoardo Geraci and Thomas Rinsma of Codean Labs (finder)


## Out of bounds memory access during WMF import ## { #CVE-2026-90629 }

CVE-2026-90629 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90629) [\[CVE json\]](./CVE-2026-90629.cve.json) [\[OSV json\]](./CVE-2026-90629.osv.json)



_Last updated: 2026-11-04T11:04:05.916Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

An uncontrolled memory access in the WMF import code of Apache OpenOffice versions through 4.1.16 allows a crafted WMF file to cause an invalid memory access, causing program crash or memory corruption.<br>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/lbmfms02205zbpwq3pm39qrx4m1czy2k


### Credits
* Anthropic and Ada Logics (finder)


## Stack overflow in CFF hint handling ## { #CVE-2026-90628 }

CVE-2026-90628 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90628) [\[CVE json\]](./CVE-2026-90628.cve.json) [\[OSV json\]](./CVE-2026-90628.osv.json)



_Last updated: 2026-11-04T11:03:40.199Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

<div>An uncontrolled memory access in the PDF export code of Apache OpenOffice versions through 4.1.16 allows a crafted CFF font to cause a stack overflow problem, causing program crash or memory corruption, or even running other code.</div>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/15onpdrzqny5y5qtmdv4lnvptxlvmg05


### Credits
* Anthropic and Ada Logics (finder)


## Local file inclusion via SQL provider and flat file database references ## { #CVE-2026-90627 }

CVE-2026-90627 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90627) [\[CVE json\]](./CVE-2026-90627.cve.json) [\[OSV json\]](./CVE-2026-90627.osv.json)



_Last updated: 2026-11-04T11:03:28.895Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

The flat file database driver in Apache Openoffice versions through 4.1.16 allows a crafted document to read the contents of any local file without asking the user.<br>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/s7y9fspdysqojnr1z7ppltxtc48b4ljf


### Credits
* Edoardo Geraci and Thomas Rinsma of Codean Labs (finder)


## Out-of-bounds write when importing encrypted PDF files ## { #CVE-2026-90626 }

CVE-2026-90626 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90626) [\[CVE json\]](./CVE-2026-90626.cve.json) [\[OSV json\]](./CVE-2026-90626.osv.json)



_Last updated: 2026-11-04T11:03:16.894Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

An uncontrolled memory access in the PDF import code of Apache OpenOffice versions through 4.1.16 allows a crafted PDF to cause an out-of-bounds memory write, causing program crash or memory corruption.<br>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/n2qgb44t8lom9s9z4xwqs3dt3mx0cggy


### Credits
* Anthropic and Ada Logics (finder)


## PDF File Parsing Heap based Buffer-Overflow-Remote Code Execution Vulnerability ## { #CVE-2026-90624 }

CVE-2026-90624 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90624) [\[CVE json\]](./CVE-2026-90624.cve.json) [\[OSV json\]](./CVE-2026-90624.osv.json)



_Last updated: 2026-11-04T11:03:05.239Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

An unchecked memory access in the PDF import code of Apache OpenOffice versions through 4.1.16 on allows a crafted PDF to execute an out-of-bounds memory write. This could crash the program or cause memory corruption.<br>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/w1047xm52vyfjt79kw2n0d3ln6sq9g5s


### Credits
* Anonymous working with TrendAI Zero Day Initiative (finder)
* Anthropic and Ada Logics (finder)


## Heap out-of-bounds write in WW8 PLCF reader ## { #CVE-2026-59268 }

CVE-2026-59268 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-59268) [\[CVE json\]](./CVE-2026-59268.cve.json) [\[OSV json\]](./CVE-2026-59268.osv.json)



_Last updated: 2026-11-04T11:02:52.848Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

<div>An out-of-bounds Write vulnerability in Apache OpenOffice versions through 4.1.16 could allow an attacker to craft a Microsoft Word document that would crash the program, or otherwise corrupt other memory areas.</div>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/xw6x0y35f3qlk4pqsc1pf0sv7481yvlk


### Credits
* Yukihiro Nakamura (reporter)


## Heap Buffer Overflow in DXF LWPOLYLINE import could cause memory corruption ## { #CVE-2026-59267 }

CVE-2026-59267 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-59267) [\[CVE json\]](./CVE-2026-59267.cve.json) [\[OSV json\]](./CVE-2026-59267.osv.json)



_Last updated: 2026-11-04T11:05:58.448Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

A crafted DXF document causes a heap buffer overflow in Draw in Apache OpenOffice 4.1.16 and earlier. This could cause a crash or otherwise a corruption of memory areas.<br>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/pwcm02dq2cy42qq2owzlvf48s8258499


### Credits
* Trail of Bits, in collaboration with Anthropic (reporter)


## Opening a malicious document can lead to system takeover ## { #CVE-2026-59265 }

CVE-2026-59265 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-59265) [\[CVE json\]](./CVE-2026-59265.cve.json) [\[OSV json\]](./CVE-2026-59265.osv.json)



_Last updated: 2026-10-02T18:02:37.660Z_

### Affected

* Apache OpenOffice through 4.1.16
* Apache OpenOffice before 95923fd437e06edd38a4f0e139a27c755a6f3ba6
* Apache OpenOffice before 181421139242694b309751fb666406eddc203c50


### Description

<p>A code execution issue in the Java integration in Apache OpenOffice v4.1.16 and earlier allows a crafted untrusted document to trigger executing arbitrary (even remote) code when opened by the user.</p><p>This issue is expected to be fixed in version 4.1.17, which is in the release candidate phase.</p><p>Until then, users can mitigate this issue by disabling Java runtime integration in the Preferences dialog. This prevents the attack. If this is not possible, or as an extra precaution, you can avoid opening&nbsp;open untrusted files entirely.&nbsp;Once 4.1.17 is released, upgrade to that version to fix the issue.</p>

### References
* https://github.com/apache/openoffice/commit/c699bed3f75e79bd64ddec9dec49f9e210eed281.patch
* https://github.com/apache/openoffice/commit/95923fd437e06edd38a4f0e139a27c755a6f3ba6.patch
* https://lists.apache.org/thread.html/svfdc1jtpqlw7mo6lgg9fthcmf754pl5


### Credits
* Thomas Rinsma and Edoardo Geraci from Codean Labs (finder)
* Rick de Jager of the V12 security team (finder)


## Uncontrolled search path element vulnerability in Windows installer ## { #CVE-2026-59264 }

CVE-2026-59264 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-59264) [\[CVE json\]](./CVE-2026-59264.cve.json) [\[OSV json\]](./CVE-2026-59264.osv.json)



_Last updated: 2026-11-04T11:02:40.422Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

The Windows installers of Apache OpenOffice 4.1.16 and earlier allow an already manipulated system to run external code with elevated access.<br>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/d4n33sjk8jgrr78jj5cq5r51fvxv6nnv


### Credits
* Kazuma Matsumoto, from GMO Cybersecurity by IERAE, Inc. (reporter)


## Carefully crafted documents could display different data when opened with different programs, instead of being reported as corrupt. ## { #CVE-2026-59263 }

CVE-2026-59263 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-59263) [\[CVE json\]](./CVE-2026-59263.cve.json) [\[OSV json\]](./CVE-2026-59263.osv.json)



_Last updated: 2026-11-04T11:01:50.194Z_

### Affected

* Apache OpenOffice through 4.1.16


### Description

A manipulated document opened in Apache OpenOffice 4.1.16 or earlier may allow substituted content to be displayed manipulating the user. Such documents are corrupt and should not be opened.<br>Users are recommended to upgrade to version 4.1.17, which fixes this issue.

### References
* https://lists.apache.org/thread.html/drr0ss9wrkq0omlrwjhcm8738pjx3xgd


### Credits
* Yufan You from Tsinghua University (finder)


## URL fetching can be used to exfiltrate arbitrary INI file values and environment variables ## { #CVE-2025-64407 }

CVE-2025-64407 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-64407) [\[CVE json\]](./CVE-2025-64407.cve.json) [\[OSV json\]](./CVE-2025-64407.osv.json)



_Last updated: 2025-11-12T09:12:41.931Z_

### Affected

* Apache OpenOffice through 4.1.15


### Description

<p>Apache OpenOffice documents can contain links. A missing Authorization vulnerability in Apache OpenOffice allowed an attacker to craft a document that would cause external links 
to be loaded without prompt. Such links could also be used to transmit system information, such as environment variables or configuration settings.</p><p>In the affected versions of Apache OpenOffice, documents that used a certain URI scheme linking to external files would 
load the contents of such files without prompting the user for 
permission to do so. Such URI scheme allows to include system configuration data, that is not supposed to be transmitted externally.</p><p>This issue affects Apache OpenOffice: through 4.1.15.</p><p>Users are recommended to upgrade to version 4.1.16, which fixes the issue.</p><p></p><p></p><p>The LibreOffice suite reported this issue as&nbsp;CVE-2024-12426.</p><p></p>

### References
* https://www.openoffice.org/security/cves/CVE-2025-64407.html
* https://lists.apache.org/thread/4yg1gv71f14fw4ky4ds50o6xjq49594g


### Credits
* Thomas Rinsma of Codean Labs (finder)


## Possible memory corruption during CSV import ## { #CVE-2025-64406 }

CVE-2025-64406 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-64406) [\[CVE json\]](./CVE-2025-64406.cve.json) [\[OSV json\]](./CVE-2025-64406.osv.json)



_Last updated: 2025-11-12T09:11:45.438Z_

### Affected

* Apache OpenOffice through 4.1.15


### Description

<p>An out-of-bounds Write vulnerability in Apache OpenOffice could allow an attacker to craft a document that would crash the program, or otherwise corrupt other memory areas.</p><p>This issue affects Apache OpenOffice: through 4.1.15.</p><p>Users are recommended to upgrade to version 4.1.16, which fixes the issue.</p>

### References
* https://www.openoffice.org/security/cves/CVE-2025-64406.html
* https://lists.apache.org/thread/py89gpogxfb2yo9c5vwv2h9x3m85pfmm


### Credits
* Damjan Jovanovic for discovering, reporting and fixing the issue (finder)


## Remote documents loaded without prompt via DDE function ## { #CVE-2025-64405 }

CVE-2025-64405 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-64405) [\[CVE json\]](./CVE-2025-64405.cve.json) [\[OSV json\]](./CVE-2025-64405.osv.json)



_Last updated: 2025-11-12T09:10:33.592Z_

### Affected

* Apache OpenOffice through 4.1.15


### Description

<p>Apache OpenOffice documents can contain links. A missing Authorization vulnerability in Apache OpenOffice allowed an attacker to craft a document that would cause external links 
to be loaded without prompt. In the affected versions of Apache OpenOffice, Calc spreadsheet containing DDE links to external files would 
load the contents of those files without prompting the user for 
permission to do so.</p><p>This issue affects Apache OpenOffice: through 4.1.15.</p><p>Users are recommended to upgrade to version 4.1.16, which fixes the issue.</p>

### References
* https://www.openoffice.org/security/cves/CVE-2025-64405.html
* https://lists.apache.org/thread/0jjftxkcc4l9kt7jjn630hfrh2ygfcbk


### Credits
* Louis Bettels, Technische Universität Braunschweig (finder)


## Remote documents loaded without prompt via background and bullet images ## { #CVE-2025-64404 }

CVE-2025-64404 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-64404) [\[CVE json\]](./CVE-2025-64404.cve.json) [\[OSV json\]](./CVE-2025-64404.osv.json)



_Last updated: 2025-11-12T09:08:28.789Z_

### Affected

* Apache OpenOffice through 4.1.15


### Description

<p>Apache OpenOffice documents can contain links to other files. A missing Authorization vulnerability in Apache OpenOffice allowed an attacker to craft a document that would cause external links 
to be loaded without prompt. In the affected versions of Apache OpenOffice, documents that used background fill images, or bullet images, linked to external files would 
load the contents of those files without prompting the user for 
permission to do so.</p><p>This issue affects Apache OpenOffice: through 4.1.15.</p><p>Users are recommended to upgrade to version 4.1.16, which fixes the issue.</p>

### References
* https://www.openoffice.org/security/cves/CVE-2025-64404.html
* https://lists.apache.org/thread/08n4mdx0pnhqsllnkc63d27sdgq3tygc


### Credits
* Reginaldo Silva of ubercomp.com (finder)


## Remote documents loaded without prompt via "external data sources" in Calc ## { #CVE-2025-64403 }

CVE-2025-64403 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-64403) [\[CVE json\]](./CVE-2025-64403.cve.json) [\[OSV json\]](./CVE-2025-64403.osv.json)



_Last updated: 2025-11-12T09:04:48.789Z_

### Affected

* Apache OpenOffice through 4.1.15


### Description

<p>Apache OpenOffice Calc spreadsheet can contain links to other files, in the form of "external data sources". A missing Authorization vulnerability in Apache OpenOffice allowed an attacker to craft a document that would cause such links 
to be loaded without prompt.</p><p>This issue affects Apache OpenOffice: through 4.1.15.</p><p>Users are recommended to upgrade to version 4.1.16, which fixes the issue.</p>

### References
* https://www.openoffice.org/security/cves/CVE-2025-64403.html
* https://lists.apache.org/thread/t7c6jhvdb00xtgd9vvn7h5sq9f4h5trt


### Credits
* Reginaldo Silva of ubercomp.com (finder)


## Remote documents loaded without prompt via OLE objects ## { #CVE-2025-64402 }

CVE-2025-64402 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-64402) [\[CVE json\]](./CVE-2025-64402.cve.json) [\[OSV json\]](./CVE-2025-64402.osv.json)



_Last updated: 2025-11-12T09:03:00.298Z_

### Affected

* Apache OpenOffice through 4.1.15


### Description

<p>Apache OpenOffice documents can contain links. A missing Authorization vulnerability in Apache OpenOffice allowed an attacker to craft a document that would cause external links 
to be loaded without prompt. In the affected versions of Apache OpenOffice, documents that used "OLE objects" linked to external files would 
load the contents of those files without prompting the user for 
permission to do so.</p><p>This issue affects Apache OpenOffice: through 4.1.15.</p><p>Users are recommended to upgrade to version 4.1.16, which fixes the issue.</p>

### References
* https://www.openoffice.org/security/cves/CVE-2025-64402.html
* https://lists.apache.org/thread/tssrl88tygjsgk6csllm6p2fb6tlv8d8


### Credits
* Dawid Golunski, Doyensec LLC (finder)


## Remote documents loaded without prompt via IFrame ## { #CVE-2025-64401 }

CVE-2025-64401 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-64401) [\[CVE json\]](./CVE-2025-64401.cve.json) [\[OSV json\]](./CVE-2025-64401.osv.json)



_Last updated: 2025-11-12T13:57:23.255Z_

### Affected

* Apache OpenOffice through 4.1.15


### Description

<p>Apache OpenOffice documents can contain links. A missing Authorization vulnerability in Apache OpenOffice&nbsp;allowed an attacker to craft a document that would cause external links 
to be loaded without prompt.&nbsp;In the affected versions of Apache OpenOffice, documents that used "floating frames" linked to external files would 
load the contents of those frames without prompting the user for 
permission to do so.</p><p>This issue affects Apache OpenOffice: through 4.1.15.</p><p>Users are recommended to upgrade to version 4.1.16, which fixes the issue.</p><p>The LibreOffice suite reported this issue as&nbsp;CVE-2023-2255</p>

### References
* https://www.openoffice.org/security/cves/CVE-2025-64401.html
* https://lists.apache.org/thread/o00dtgvhr9tx8r4y8vf6y2mg7nn6mx6c


### Credits
* Amel Bouziane-Leblond for discovering and reporting the issue (finder)


## Macro URL arbitrary script execution ## { #CVE-2023-47804 }

CVE-2023-47804 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-47804) [\[CVE json\]](./CVE-2023-47804.cve.json) [\[OSV json\]](./CVE-2023-47804.osv.json)



_Last updated: 2023-12-29T14:31:22.075Z_

### Affected

* Apache OpenOffice through 4.1.14


### Description

<p>Apache OpenOffice documents can contain links that call internal macros with arbitrary arguments. Several URI Schemes are defined for this purpose.</p><p>Links can be activated by clicks, or by automatic document events.</p><p>The execution of such links must be subject to user approval.</p><p>In the affected versions of OpenOffice, approval for certain links is not requested; when activated, such links could therefore result in arbitrary script execution.</p><p>This is a corner case of CVE-2022-47502.</p>

### References
* https://lists.apache.org/thread/ygp59swfcy6g46jf8v9s6qpwmxn8fsvb
* https://www.openoffice.org/security/cves/CVE-2023-47804.html


### Credits
* Amel BOUZIANE-LEBLOND aka Icare Bug Bounty Hunter (reporter)


## Macro URL arbitrary script execution ## { #CVE-2022-47502 }

CVE-2022-47502 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-47502) [\[CVE json\]](./CVE-2022-47502.cve.json) [\[OSV json\]](./CVE-2022-47502.osv.json)



_Last updated: 2023-04-05T12:45:10.294Z_

### Affected

* Apache OpenOffice through 4.1.13


### Description

<p>Apache OpenOffice documents can contain links that call internal macros with arbitrary arguments. Several URI Schemes are defined for this purpose.<br></p><p>Links can be activated by clicks, or by automatic document events.</p><p>The execution of such links must be subject to user approval.</p><p>In the affected versions of OpenOffice, approval for certain links is not   requested; when activated, such links could therefore result in arbitrary script execution.<br></p>

### References
* https://lists.apache.org/thread/xr6tl91jj2jgcq8pdbrc4d8w13s6xn80
* https://www.openoffice.org/security/cves/CVE-2022-47502.html


### Credits
* Altin Thartori (tin-z) (reporter)
* Joachim Mammele (reporter)


## Empty entry in Java class path ## { #CVE-2022-38745 }

CVE-2022-38745 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-38745) [\[CVE json\]](./CVE-2022-38745.cve.json) [\[OSV json\]](./CVE-2022-38745.osv.json)



_Last updated: 2023-03-24T15:56:44.525Z_

### Affected

* Apache OpenOffice before 4.1.14


### Description

<div>Apache OpenOffice versions before 4.1.14 may be configured to add an empty entry to the Java class path. This may lead to run arbitrary Java code from the current directory.<br></div>

### References
* https://lists.apache.org/thread/q3noq7m681kvtb29m28x74q8cnwnzzo0
* https://www.openoffice.org/security/cves/CVE-2022-38745.html


### Credits
* European Commission's Open Source Programme Office (sponsor)


## Apache OpenOffice Weak Master Keys ## { #CVE-2022-37401 }

CVE-2022-37401 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-37401) [\[CVE json\]](./CVE-2022-37401.cve.json) [\[OSV json\]](./CVE-2022-37401.osv.json)



_Last updated: 2022-08-13T06:35:06.833Z_

### Affected

* Apache OpenOffice from Apache OpenOffice 4 before 4.1.13


### Description

Apache OpenOffice supports the storage of passwords for web connections in the user's configuration database. The stored passwords are encrypted with a single master key provided by the user. A flaw in OpenOffice existed where master key was poorly encoded resulting in weakening its entropy from 128 to 43 bits making the stored passwords vulnerable to a brute force attack if an attacker has access to the users stored config. This issue affects: Apache OpenOffice versions prior to 4.1.13.  Reference: CVE-2022-26307 - LibreOffice

### References
* https://www.openoffice.org/security/cves/CVE-2022-37401.html


### Credits
*  OpenSource Security GmbH on behalf of the German Federal Office for Information Security


## Apache OpenOffice Static Initialization Vector Allows to Recover Passwords for Web Connections Without Knowing the Master Password ## { #CVE-2022-37400 }

CVE-2022-37400 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-37400) [\[CVE json\]](./CVE-2022-37400.cve.json) [\[OSV json\]](./CVE-2022-37400.osv.json)



_Last updated: 2022-08-13T06:33:55.145Z_

### Affected

* Apache OpenOffice from Apache OpenOffice 4 before 4.1.13


### Description

Apache OpenOffice supports the storage of passwords for web connections in the user's configuration database. The stored passwords are encrypted with a single master key provided by the user. A flaw in OpenOffice existed where the required initialization vector for encryption was always the same which weakens the security of the encryption making them vulnerable if an attacker has access to the user's configuration data. This issue affects: Apache OpenOffice versions prior to 4.1.13.
Reference: CVE-2022-26306 - LibreOffice

### References
* https://www.openoffice.org/security/cves/CVE-2022-37400.html


### Credits
* OpenSource Security GmbH on behalf of the German Federal Office for Information Security


## Content Manipulation with Certificate Validation Attack ## { #CVE-2021-41832 }

CVE-2021-41832 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-41832) [\[CVE json\]](./CVE-2021-41832.cve.json) [\[OSV json\]](./CVE-2021-41832.osv.json)



_Last updated: 2021-10-11T08:06:50.243Z_

### Affected

* Apache OpenOffice from Apache OpenOffice through 4.1.10
* Apache OpenOffice from OpenOffice.org through 3.4


### Description

It is possible for an attacker to manipulate documents to appear to be signed by a trusted source.

All versions of Apache OpenOffice up to 4.1.10 are affected. Users are advised to update to version 4.1.11.

See CVE-2021-25635 for the LibreOffice advisory.


### References
* https://lists.apache.org/thread.html/rd3214a568b43dd335b5d558f521377f4bff750684dea18eb041fc1bb%40%3Cusers.openoffice.apache.org%3E


### Credits
* Apache OpenOffice would like to thank Simon Rohlmann, Vladislav Mladenov, Christian Mainka, and Jorg Schwenk of Ruhr University Bochum, Germany


## Timestamp Manipulation with Signature Wrapping ## { #CVE-2021-41831 }

CVE-2021-41831 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-41831) [\[CVE json\]](./CVE-2021-41831.cve.json) [\[OSV json\]](./CVE-2021-41831.osv.json)



_Last updated: 2021-10-11T08:05:48.311Z_

### Affected

* Apache OpenOffice from Apache OpenOffice through 4.1.10
* Apache OpenOffice from OpenOffice.org through 3.4


### Description

It is possible for an attacker to manipulate the timestamp of signed documents.

All versions of Apache OpenOffice up to 4.1.10 are affected. Users are advised to update to version 4.1.11.

See CVE-2021-25634 for the LibreOffice advisory.


### References
* https://lists.apache.org/thread.html/ra74d5057cdc781a36286a83e8bcbc90a7678f030ae73339c35dfc4f9%40%3Cusers.openoffice.apache.org%3E


### Credits
* Apache OpenOffice would like to thank Simon Rohlmann, Vladislav Mladenov, Christian Mainka, and Jorg Schwenk of Ruhr University Bochum, Germany


## Double Certificate Attack ## { #CVE-2021-41830 }

CVE-2021-41830 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-41830) [\[CVE json\]](./CVE-2021-41830.cve.json) [\[OSV json\]](./CVE-2021-41830.osv.json)



_Last updated: 2021-10-11T08:05:11.193Z_

### Affected

* Apache OpenOffice from Apache OpenOffice through 4.1.10
* Apache OpenOffice from OpenOffice.org through 3.4


### Description

It is possible for an attacker to manipulate signed documents and macros to appear to come from a trusted source.

All versions of Apache OpenOffice up to 4.1.10 are affected. Users are advised to update to version 4.1.11.

See CVE-2021-25633 for the LibreOffice advisory.



### References
* https://lists.apache.org/thread.html/r97d287c88881aa581f1b18cb01e2cbedc4e6eae85958491acb89b12e%40%3Cusers.openoffice.apache.org%3E


### Credits
* Apache OpenOffice would like to thank Simon Rohlmann, Vladislav Mladenov, Christian Mainka, and Jorg Schwenk of Ruhr University Bochum, Germany


## Billion Laughs ## { #CVE-2021-40439 }

CVE-2021-40439 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-40439) [\[CVE json\]](./CVE-2021-40439.cve.json) [\[OSV json\]](./CVE-2021-40439.osv.json)



_Last updated: 2021-10-07T15:23:25.432Z_

### Affected

* Apache OpenOffice from Apache OpenOffice through 4.1.10
* Apache OpenOffice from OpenOffice.org through 3.4


### Description

Apache OpenOffice has a dependency on expat software. Versions prior to 2.1.0 were subject to CVE-2013-0340 a "Billion Laughs" entity expansion denial of service attack and exploit via crafted XML files. ODF files consist of a set of XML files.

All versions of Apache OpenOffice up to 4.1.10 are subject to this issue.

expat in version 4.1.11 is patched.

### References
* https://lists.apache.org/thread.html/rfb2c193360436e230b85547e85a41bea0916916f96c501f5b6fc4702%40%3Cusers.openoffice.apache.org%3E


## Buffer overflow from a crafted DBF file ## { #CVE-2021-33035 }

CVE-2021-33035 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-33035) [\[CVE json\]](./CVE-2021-33035.cve.json) [\[OSV json\]](./CVE-2021-33035.osv.json)



_Last updated: 2021-10-07T15:21:31.403Z_

### Affected

* Apache OpenOffice from Apache OpenOffice through 4.1.10
* Apache OpenOffice from OpenOffice.org through 3.4


### Description

Apache OpenOffice opens dBase/DBF documents and shows the contents as spreadsheets.  DBF are database files with data organized in fields.  When reading DBF data the size of certain fields is not checked: the data is just copied into local variables. A carefully crafted document could overflow the allocated space, leading to the execution of arbitrary code by altering the contents of the program stack.  

This issue affects Apache OpenOffice up to and including version 4.1.10

This issue is fixed in Apache OpenOffice 4.1.11


### References
* https://github.com/apache/openoffice/commit/efddaef0151af3be16078cc4d88c6bae0f911e56#diff-ea66e734dd358922aba12ad4ba39c96bdc6cbde587d07dbc63d04daa0a30e90f


### Credits
* Apache OpenOffice would like to thank Eugene Lim, Government Technology Agency of Singapore for reporting this issue.


## Code execution in Apache OpenOffice via non-http(s) schemes in Hyperlinks ## { #CVE-2021-30245 }

CVE-2021-30245 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-30245) [\[CVE json\]](./CVE-2021-30245.cve.json) [\[OSV json\]](./CVE-2021-30245.osv.json)



_Last updated: 2021-04-15T19:28:07.363Z_

### Affected

* Apache OpenOffice from Apache OpenOffice through 4.1.9


### Description

The project received a report that all versions of Apache OpenOffice through 4.1.8 can open non-http(s) hyperlinks. The problem has existed since about 2006 and the issue is also in 4.1.9. If the link is specifically crafted this could lead to untrusted code execution. It is always best practice to be careful opening documents from unknown and unverified sources. The mitigation in Apache OpenOffice 4.1.10 (unreleased) assures that a security warning is displayed giving the user the option of continuing to open the hyperlink.

### References
* https://lists.apache.org/thread.html/r87ff11512e4883052991e6b725e20294224034ea8453b811fb3ee735%40%3Cusers.openoffice.apache.org%3E


### Credits
* Fabian Bräunlein and Lukas Euler of Positive Security


## DEB packaging for Apache OpenOffice 4.1.8 installed with a non-root userid and groupid ## { #CVE-2021-28129 }

CVE-2021-28129 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-28129) [\[CVE json\]](./CVE-2021-28129.cve.json) [\[OSV json\]](./CVE-2021-28129.osv.json)



_Last updated: 2021-10-07T15:24:31.592Z_

### Affected

* Apache OpenOffice at 4.1.8


### Description

While working on Apache OpenOffice 4.1.8 a developer discovered that the DEB package did not install using root, but instead used a userid and groupid of 500. This both caused issues with desktop integration and could allow a crafted attack on files owned by that user or group if they exist.

Users who installed the Apache OpenOffice 4.1.8 DEB packaging should upgrade to the latest version of Apache OpenOffice.

### References
* https://lists.apache.org/thread.html/rc9090ab48b4699494b63b35cd6d7414c52d665ecae12add3cdc56c9b%40%3Cusers.openoffice.apache.org%3E


### Credits
* Arrigo Marchiori
