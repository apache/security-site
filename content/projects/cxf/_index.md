---
title: Apache CXF security advisories
description: Security information for Apache CXF
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache CXF? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache CXF Reflected XSS in the services listing page via the styleSheetPath ## { #CVE-2020-13954 }

CVE-2020-13954 [\[CVE json\]](./CVE-2020-13954.cve.json) [\[OSV json\]](./CVE-2020-13954.osv.json)



_Last updated: 2020-11-12T12:45:31.751Z_

### Affected

* Apache CXF from unspecified before 3.4.1


### Description

By default, Apache CXF creates a /services page containing a listing of the available endpoint names and addresses. This webpage is vulnerable to a reflected Cross-Site Scripting (XSS) attack via the styleSheetPath, which allows a malicious actor to inject javascript into the web page.

This vulnerability affects all versions of Apache CXF prior to 3.4.1 and 3.3.8.

Please note that this is a separate issue to CVE-2019-17573.


### References
* http://cxf.apache.org/security-advisories.data/CVE-2020-13954.txt.asc?version=1&modificationDate=1605183670659&api=v2


### Credits
* Thanks to Ryan Lambeth for reporting this issue.


## OAuth 2 authorization service vulnerable to DDos attacks ## { #CVE-2021-22696 }

CVE-2021-22696 [\[CVE json\]](./CVE-2021-22696.cve.json) [\[OSV json\]](./CVE-2021-22696.osv.json)



_Last updated: 2021-04-02T09:58:49.120Z_

### Affected

* Apache CXF from unspecified before 3.4.3


### Description

CXF supports (via JwtRequestCodeFilter) passing OAuth 2 parameters via a JWT token as opposed to query parameters (see: The OAuth 2.0 Authorization Framework: JWT Secured Authorization Request (JAR)). Instead of sending a JWT token as a "request" parameter, the spec also supports specifying a URI from which to retrieve a JWT token from via the "request_uri" parameter.

CXF was not validating the "request_uri" parameter (apart from ensuring it uses "https) and was making a REST request to the parameter in the request to retrieve a token.

This means that CXF was vulnerable to DDos attacks on the authorization server, as specified in section 10.4.1 of the spec. 

This issue affects Apache CXF versions prior to 3.4.3; Apache CXF versions prior to 3.3.10.

### References
* https://cxf.apache.org/security-advisories.data/CVE-2021-22696.txt.asc


## Apache CXF Denial of service vulnerability in parsing JSON via JsonMapObjectReaderWriter ## { #CVE-2021-30468 }

CVE-2021-30468 [\[CVE json\]](./CVE-2021-30468.cve.json) [\[OSV json\]](./CVE-2021-30468.osv.json)



_Last updated: 2021-06-16T11:56:32.302Z_

### Affected

* Apache CXF from Apache CXF before 3.4.4


### Description

A vulnerability in the JsonMapObjectReaderWriter of Apache CXF allows an attacker to submit malformed JSON to a web service, which results in the thread getting stuck in an infinite loop, consuming CPU indefinitely.  

This issue affects Apache CXF versions prior to 3.4.4; Apache CXF versions prior to 3.3.11.

### References
* http://cxf.apache.org/security-advisories.data/CVE-2021-30468.txt.asc


## Apache CXF directory listing / code exfiltration ## { #CVE-2022-46363 }

CVE-2022-46363 [\[CVE json\]](./CVE-2022-46363.cve.json) [\[OSV json\]](./CVE-2022-46363.osv.json)



_Last updated: 2022-12-13T14:47:26.050Z_

### Affected

* Apache CXF from 3.5 before 3.5.5
* Apache CXF from 3.4 before 3.4.10


### Description

A vulnerability in Apache CXF before versions 3.5.5 and 3.4.10 allows an attacker to perform a remote directory listing or code exfiltration. The vulnerability only applies when the&nbsp;CXFServlet is configured with both the&nbsp;static-resources-list and&nbsp;redirect-query-check attributes. These attributes are not supposed to be used together, and so the vulnerability can only arise if the CXF service is misconfigured.<br><br>

### References
* https://lists.apache.org/thread/pdzo1qgyplf4y523tnnzrcm7hoco3l8c


### Credits
* thanat0s from Beijin Qihoo 360 adlab (finder)


## Apache CXF SSRF Vulnerability ## { #CVE-2022-46364 }

CVE-2022-46364 [\[CVE json\]](./CVE-2022-46364.cve.json) [\[OSV json\]](./CVE-2022-46364.osv.json)



_Last updated: 2022-12-13T15:44:20.951Z_

### Affected

* Apache CXF before 3.5.5
* Apache CXF before 3.4.10


### Description

A SSRF vulnerability in parsing the&nbsp;href attribute of XOP:Include in MTOM requests in versions of Apache CXF before 3.5.5 and 3.4.10 allows an attacker to perform SSRF style attacks on webservices that take at least one parameter of any type.&nbsp;

### References
* https://cxf.apache.org/security-advisories.data/CVE-2022-46364.txt?version=1&modificationDate=1670944472739&api=v2


### Credits
* thanat0s from Beijin Qihoo 360 adlab (finder)


## Apache CXF SSRF Vulnerability using the Aegis databinding ## { #CVE-2024-28752 }

CVE-2024-28752 [\[CVE json\]](./CVE-2024-28752.cve.json) [\[OSV json\]](./CVE-2024-28752.osv.json)



_Last updated: 2024-03-15T10:28:02.596Z_

### Affected

* Apache CXF before 4.0.4, 3.6.3, 3.5.8


### Description

A SSRF vulnerability using the Aegis DataBinding in versions of Apache CXF before 4.0.4, 3.6.3 and 3.5.8 allows an attacker to perform SSRF style attacks on webservices that take at least one parameter of any type. Users of other data bindings (including the default databinding) are not impacted.<br><br>

### References
* https://cxf.apache.org/security-advisories.data/CVE-2024-28752.txt


### Credits
* Tobias S. Fink (finder)


## SSRF vulnerability via WADL stylesheet parameter ## { #CVE-2024-29736 }

CVE-2024-29736 [\[CVE json\]](./CVE-2024-29736.cve.json) [\[OSV json\]](./CVE-2024-29736.osv.json)



_Last updated: 2024-07-19T08:50:06.520Z_

### Affected

* Apache CXF before 3.5.9, 3.6.4, 4.0.5


### Description

A SSRF vulnerability in WADL service description in versions of Apache CXF before 4.0.5, 3.6.4 and 3.5.9 allows an attacker to perform SSRF style attacks on REST webservices. The attack only applies if a custom stylesheet parameter is configured.

### References
* https://lists.apache.org/thread/4jtpsswn2r6xommol54p5mg263ysgdw2


### Credits
* Tobias S. Fink (finder)


## Apache CXF Denial of Service vulnerability in JOSE ## { #CVE-2024-32007 }

CVE-2024-32007 [\[CVE json\]](./CVE-2024-32007.cve.json) [\[OSV json\]](./CVE-2024-32007.osv.json)



_Last updated: 2024-07-19T08:50:30.464Z_

### Affected

* Apache CXF before 4.0.5, 3.6.4, 3.5.9


### Description

An improper input validation of the&nbsp;p2c parameter in the Apache CXF JOSE code before 4.0.5, 3.6.4 and 3.5.9&nbsp;allows an attacker to perform a denial of service attack by specifying a large value for this parameter in a token.&nbsp;<br>

### References
* https://lists.apache.org/thread/stwrgsr1llb73nkl16klv9vjqgmmx633


### Credits
* Jingcheng Yang and Jianjun Chen from Sichuan University and Zhongguancun Lab. (finder)


## Unrestricted memory consumption in CXF HTTP clients ## { #CVE-2024-41172 }

CVE-2024-41172 [\[CVE json\]](./CVE-2024-41172.cve.json) [\[OSV json\]](./CVE-2024-41172.osv.json)



_Last updated: 2024-07-19T08:50:42.522Z_

### Affected

* Apache CXF from 3.6.0, 4.0.0 before 3.6.4, 4.0.5


### Description

In versions of Apache CXF before 3.6.4 and 4.0.5 (3.5.x and lower versions are not impacted), a CXF HTTP client conduit may prevent HTTPClient instances from being garbage collected and it is possible that memory consumption will continue to increase, eventually causing the application to run  out of memory<br>

### References
* https://lists.apache.org/thread/n2hvbrgwpdtcqdccod8by28ynnolybl6


## Denial of Service vulnerability with temporary files ## { #CVE-2025-23184 }

CVE-2025-23184 [\[CVE json\]](./CVE-2025-23184.cve.json) [\[OSV json\]](./CVE-2025-23184.osv.json)



_Last updated: 2025-01-21T09:35:35.654Z_

### Affected

* Apache CXF before 3.5.10
* Apache CXF from 3.6.0 before 3.6.5
* Apache CXF from 4.0.0 before 4.0.6


### Description

A potential denial of service vulnerability is present in versions of Apache CXF before&nbsp;3.5.10, 3.6.5 and 4.0.6.&nbsp;In some edge cases, the CachedOutputStream instances may not be closed and, if backed by temporary files, may fill up the file system (it applies to servers and clients).<br><br>

### References
* https://lists.apache.org/thread/lfs8l63rnctnj2skfrxyys7v8fgnt122


## Denial of Service and sensitive data exposure in logs ## { #CVE-2025-48795 }

CVE-2025-48795 [\[CVE json\]](./CVE-2025-48795.cve.json) [\[OSV json\]](./CVE-2025-48795.osv.json)



_Last updated: 2025-07-15T14:26:43.340Z_

### Affected

* Apache CXF from 3.5.10 before 3.5.11
* Apache CXF from 3.6.5 before 3.6.6
* Apache CXF from 4.0.6 before 4.0.7
* Apache CXF from 4.1.0 before 4.1.1


### Description

Apache CXF stores large stream based messages as temporary files on the local filesystem. A bug was introduced which means that the entire temporary file is read into memory and then logged. An attacker might be able to exploit this to cause a denial of service attack by causing an out of memory exception. In addition, it is possible to configure CXF to encrypt temporary files to prevent sensitive credentials from being cached unencrypted on the local filesystem, however this bug means that the cached files are written out to logs unencrypted.<br><br>Users are recommended to upgrade to versions 3.5.11, 3.6.6, 4.0.7 or 4.1.1, which fixes this issue.

### References
* https://lists.apache.org/thread/vo5qv02mvv5plmb6z2xf1ktjmrpv3jmn


### Credits
* MAUGIN Thomas https://github.com/Thom-x, Qlik (finder)
