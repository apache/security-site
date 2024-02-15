---
title: Apache OpenOffice security advisories
description: Security information for Apache OpenOffice
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache OpenOffice? You can read more about the projects' security policy on their [security page](https://openoffice.apache.org/security), and email your report to the [Apache OpenOffice Security Team](mailto:security@openoffice.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://openoffice.apache.org/security). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## DEB packaging for Apache OpenOffice 4.1.8 installed with a non-root userid and groupid ## { #CVE-2021-28129 }

CVE-2021-28129 [\[CVE json\]](./CVE-2021-28129.cve.json)

### Affected

* Apache OpenOffice at 4.1.8


### Description

While working on Apache OpenOffice 4.1.8 a developer discovered that the DEB package did not install using root, but instead used a userid and groupid of 500. This both caused issues with desktop integration and could allow a crafted attack on files owned by that user or group if they exist.

Users who installed the Apache OpenOffice 4.1.8 DEB packaging should upgrade to the latest version of Apache OpenOffice.

### References
* https://lists.apache.org/thread.html/rc9090ab48b4699494b63b35cd6d7414c52d665ecae12add3cdc56c9b%40%3Cusers.openoffice.apache.org%3E


### Credits
* Arrigo Marchiori


## Code execution in Apache OpenOffice via non-http(s) schemes in Hyperlinks ## { #CVE-2021-30245 }

CVE-2021-30245 [\[CVE json\]](./CVE-2021-30245.cve.json)

### Affected

* Apache OpenOffice from Apache OpenOffice through 4.1.9


### Description

The project received a report that all versions of Apache OpenOffice through 4.1.8 can open non-http(s) hyperlinks. The problem has existed since about 2006 and the issue is also in 4.1.9. If the link is specifically crafted this could lead to untrusted code execution. It is always best practice to be careful opening documents from unknown and unverified sources. The mitigation in Apache OpenOffice 4.1.10 (unreleased) assures that a security warning is displayed giving the user the option of continuing to open the hyperlink.

### References
* https://lists.apache.org/thread.html/r87ff11512e4883052991e6b725e20294224034ea8453b811fb3ee735%40%3Cusers.openoffice.apache.org%3E


### Credits
* Fabian Bräunlein and Lukas Euler of Positive Security


## Buffer overflow from a crafted DBF file ## { #CVE-2021-33035 }

CVE-2021-33035 [\[CVE json\]](./CVE-2021-33035.cve.json)

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


## Billion Laughs ## { #CVE-2021-40439 }

CVE-2021-40439 [\[CVE json\]](./CVE-2021-40439.cve.json)

### Affected

* Apache OpenOffice from Apache OpenOffice through 4.1.10
* Apache OpenOffice from OpenOffice.org through 3.4


### Description

Apache OpenOffice has a dependency on expat software. Versions prior to 2.1.0 were subject to CVE-2013-0340 a "Billion Laughs" entity expansion denial of service attack and exploit via crafted XML files. ODF files consist of a set of XML files.

All versions of Apache OpenOffice up to 4.1.10 are subject to this issue.

expat in version 4.1.11 is patched.

### References
* https://lists.apache.org/thread.html/rfb2c193360436e230b85547e85a41bea0916916f96c501f5b6fc4702%40%3Cusers.openoffice.apache.org%3E


## Double Certificate Attack ## { #CVE-2021-41830 }

CVE-2021-41830 [\[CVE json\]](./CVE-2021-41830.cve.json)

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


## Timestamp Manipulation with Signature Wrapping ## { #CVE-2021-41831 }

CVE-2021-41831 [\[CVE json\]](./CVE-2021-41831.cve.json)

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


## Content Manipulation with Certificate Validation Attack ## { #CVE-2021-41832 }

CVE-2021-41832 [\[CVE json\]](./CVE-2021-41832.cve.json)

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


## Apache OpenOffice Static Initialization Vector Allows to Recover Passwords for Web Connections Without Knowing the Master Password ## { #CVE-2022-37400 }

CVE-2022-37400 [\[CVE json\]](./CVE-2022-37400.cve.json)

### Affected

* Apache OpenOffice from Apache OpenOffice 4 before 4.1.13


### Description

Apache OpenOffice supports the storage of passwords for web connections in the user's configuration database. The stored passwords are encrypted with a single master key provided by the user. A flaw in OpenOffice existed where the required initialization vector for encryption was always the same which weakens the security of the encryption making them vulnerable if an attacker has access to the user's configuration data. This issue affects: Apache OpenOffice versions prior to 4.1.13.
Reference: CVE-2022-26306 - LibreOffice

### References
* https://www.openoffice.org/security/cves/CVE-2022-37400.html


### Credits
* OpenSource Security GmbH on behalf of the German Federal Office for Information Security


## Apache OpenOffice Weak Master Keys ## { #CVE-2022-37401 }

CVE-2022-37401 [\[CVE json\]](./CVE-2022-37401.cve.json)

### Affected

* Apache OpenOffice from Apache OpenOffice 4 before 4.1.13


### Description

Apache OpenOffice supports the storage of passwords for web connections in the user's configuration database. The stored passwords are encrypted with a single master key provided by the user. A flaw in OpenOffice existed where master key was poorly encoded resulting in weakening its entropy from 128 to 43 bits making the stored passwords vulnerable to a brute force attack if an attacker has access to the users stored config. This issue affects: Apache OpenOffice versions prior to 4.1.13.  Reference: CVE-2022-26307 - LibreOffice

### References
* https://www.openoffice.org/security/cves/CVE-2022-37401.html


### Credits
*  OpenSource Security GmbH on behalf of the German Federal Office for Information Security


## Empty entry in Java class path ## { #CVE-2022-38745 }

CVE-2022-38745 [\[CVE json\]](./CVE-2022-38745.cve.json)

### Affected

* Apache OpenOffice before 4.1.14


### Description

<div>Apache OpenOffice versions before 4.1.14 may be configured to add an empty entry to the Java class path. This may lead to run arbitrary Java code from the current directory.<br></div>

### References
* https://lists.apache.org/thread/q3noq7m681kvtb29m28x74q8cnwnzzo0
* https://www.openoffice.org/security/cves/CVE-2022-38745.html


### Credits
* European Commission's Open Source Programme Office (sponsor)


## Macro URL arbitrary script execution ## { #CVE-2022-47502 }

CVE-2022-47502 [\[CVE json\]](./CVE-2022-47502.cve.json)

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


## Macro URL arbitrary script execution ## { #CVE-2023-47804 }

CVE-2023-47804 [\[CVE json\]](./CVE-2023-47804.cve.json)

### Affected

* Apache OpenOffice through 4.1.14


### Description

<p>Apache OpenOffice documents can contain links that call internal macros with arbitrary arguments. Several URI Schemes are defined for this purpose.</p><p>Links can be activated by clicks, or by automatic document events.</p><p>The execution of such links must be subject to user approval.</p><p>In the affected versions of OpenOffice, approval for certain links is not requested; when activated, such links could therefore result in arbitrary script execution.</p><p>This is a corner case of CVE-2022-47502.</p>

### References
* https://lists.apache.org/thread/ygp59swfcy6g46jf8v9s6qpwmxn8fsvb
* https://www.openoffice.org/security/cves/CVE-2023-47804.html


### Credits
* Amel BOUZIANE-LEBLOND aka Icare Bug Bounty Hunter (reporter)
