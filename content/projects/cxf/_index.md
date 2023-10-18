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

CVE-2020-13954 [\[CVE json\]](./CVE-2020-13954.cve.json)

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

CVE-2021-22696 [\[CVE json\]](./CVE-2021-22696.cve.json)

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

CVE-2021-30468 [\[CVE json\]](./CVE-2021-30468.cve.json)

### Affected

* Apache CXF from Apache CXF before 3.4.4


### Description

A vulnerability in the JsonMapObjectReaderWriter of Apache CXF allows an attacker to submit malformed JSON to a web service, which results in the thread getting stuck in an infinite loop, consuming CPU indefinitely.  

This issue affects Apache CXF versions prior to 3.4.4; Apache CXF versions prior to 3.3.11.

### References
* http://cxf.apache.org/security-advisories.data/CVE-2021-30468.txt.asc


## Apache CXF directory listing / code exfiltration ## { #CVE-2022-46363 }

CVE-2022-46363 [\[CVE json\]](./CVE-2022-46363.cve.json)

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

CVE-2022-46364 [\[CVE json\]](./CVE-2022-46364.cve.json)

### Affected

* Apache CXF before 3.5.5
* Apache CXF before 3.4.10


### Description

A SSRF vulnerability in parsing the&nbsp;href attribute of XOP:Include in MTOM requests in versions of Apache CXF before 3.5.5 and 3.4.10 allows an attacker to perform SSRF style attacks on webservices that take at least one parameter of any type.&nbsp;

### References
* https://cxf.apache.org/security-advisories.data/CVE-2022-46364.txt?version=1&modificationDate=1670944472739&api=v2


### Credits
* thanat0s from Beijin Qihoo 360 adlab (finder)
