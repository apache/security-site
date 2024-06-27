---
title: Apache XML Graphics security advisories
description: Security information for Apache XML Graphics
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache XML Graphics? You can read more about the projects' security policy on their [security page](https://xmlgraphics.apache.org/security.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://xmlgraphics.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Server-Side Request Forgery Information Disclosure Vulnerability ## { #CVE-2022-38398 }

CVE-2022-38398 [\[CVE json\]](./CVE-2022-38398.cve.json) [\[OSV json\]](./CVE-2022-38398.osv.json)



_Last updated: 2022-09-22T14:36:45.719Z_

### Affected

* Apache XML Graphics at Batik 1.14


### Description

Server-Side Request Forgery (SSRF) vulnerability in Batik of Apache XML Graphics allows an attacker to load a url thru the jar protocol.  This issue affects Apache XML Graphics Batik 1.14.

### References
* https://lists.apache.org/thread/712c9xwtmyghyokzrm2ml6sps4xlmbsx


## PDFTranscoder does not block external resources ## { #CVE-2022-38648 }

CVE-2022-38648 [\[CVE json\]](./CVE-2022-38648.cve.json) [\[OSV json\]](./CVE-2022-38648.osv.json)



_Last updated: 2022-09-22T14:37:30.540Z_

### Affected

* Apache XML Graphics at Batik 1.14


### Description

Server-Side Request Forgery (SSRF) vulnerability in Batik of Apache XML Graphics allows an attacker to fetch external resources.  This issue affects Apache XML Graphics Batik 1.14.

### References
* https://lists.apache.org/thread/gfsktxvj7jtwyovmhhbrw0bs13wfjd7b


## Jar url should be blocked by DefaultScriptSecurity ## { #CVE-2022-40146 }

CVE-2022-40146 [\[CVE json\]](./CVE-2022-40146.cve.json) [\[OSV json\]](./CVE-2022-40146.osv.json)



_Last updated: 2022-11-23T18:09:53.965Z_

### Affected

* Apache XML Graphics at Batik 1.14


### Description

Server-Side Request Forgery (SSRF) vulnerability in Batik of Apache XML Graphics allows an attacker to access files using a Jar url.  This issue affects Apache XML Graphics Batik 1.14. Only affects the batik-bridge component.

### References
* https://lists.apache.org/thread/hxtddqjty2sbs12y97c8g7xfh17jzxsx


## Apache Batik prior to 1.16 allows RCE when loading untrusted SVG input ## { #CVE-2022-41704 }

CVE-2022-41704 [\[CVE json\]](./CVE-2022-41704.cve.json) [\[OSV json\]](./CVE-2022-41704.osv.json)



_Last updated: 2022-10-25T11:02:56.969Z_

### Affected

* Apache XML Graphics from Batik through 1.15


### Description

A vulnerability in Batik of Apache XML Graphics allows an attacker to run untrusted Java code from an SVG. This issue affects Apache XML Graphics prior to 1.16. It is recommended to update to version 1.16.

### References
* https://lists.apache.org/thread/hplhx0o74jb7blj39fm4kw3otcnjd6xf


### Credits
* This issue was independently reported by 4ra1n of Chaitin Tech and pwnull


## Apache Batik prior to 1.16 allows RCE via scripting ## { #CVE-2022-42890 }

CVE-2022-42890 [\[CVE json\]](./CVE-2022-42890.cve.json) [\[OSV json\]](./CVE-2022-42890.osv.json)



_Last updated: 2022-10-25T11:25:19.555Z_

### Affected

* Apache XML Graphics from Batik through 1.15


### Description

A vulnerability in Batik of Apache XML Graphics allows an attacker to run Java code from untrusted SVG via JavaScript.  This issue affects Apache XML Graphics prior to 1.16. Users are recommended to upgrade to version 1.16.

### References
* https://lists.apache.org/thread/pkvhy0nsj1h1mlon008wtzhosbtxjwly


### Credits
* This issue was independently reported by Y4tacker and 4ra1n of Chaitin Tech


## Information disclosure vulnerability ## { #CVE-2022-44729 }

CVE-2022-44729 [\[CVE json\]](./CVE-2022-44729.cve.json)

_Last updated: 2023-08-22T14:12:19.621Z_

### Affected

* Apache XML Graphics Batik at 1.16


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache Software Foundation Apache XML Graphics Batik.<p>This issue affects Apache XML Graphics Batik: 1.16.</p><p>On version 1.16, a malicious SVG could trigger loading external resources by default, causing resource consumption or in some cases even information disclosure. Users are recommended to upgrade to version 1.17 or later.<br></p>

### References
* https://xmlgraphics.apache.org/security.html
* https://lists.apache.org/thread/hco2nw1typoorz33qzs0fcdx0ws6d6j2


### Credits
* nbxiglk (finder)


## Information disclosure vulnerability ## { #CVE-2022-44730 }

CVE-2022-44730 [\[CVE json\]](./CVE-2022-44730.cve.json)

_Last updated: 2023-08-22T14:04:18.758Z_

### Affected

* Apache XML Graphics Batik at 1.16


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache Software Foundation Apache XML Graphics Batik.<p>This issue affects Apache XML Graphics Batik: 1.16.<br></p><p>A malicious SVG can probe user profile / data and send it directly as parameter to a URL.<br></p>

### References
* https://lists.apache.org/thread/58m5817jr059f4v1zogh0fngj9pwjyj0
* https://xmlgraphics.apache.org/security.html
