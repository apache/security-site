---
title: Apache Archiva security advisories
description: Security information for Apache Archiva
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Archiva? You can read more about the projects' security policy on their [security page](https://archiva.apache.org/security.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://archiva.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Archiva Arbitrary user password reset vulnerability ## { #CVE-2022-29405 }

CVE-2022-29405 [\[CVE json\]](./CVE-2022-29405.cve.json) [\[OSV json\]](./CVE-2022-29405.osv.json)



_Last updated: 2022-05-25T07:11:14.322Z_

### Affected

* Apache Archiva from 2.2 through 2.2.7


### Description

In Apache Archiva, any registered user can reset password for any users.  This is fixed in Archiva 2.2.8

### References
* https://archiva.apache.org/docs/2.2.8/release-notes.html


## Apache Archiva prior to 2.2.9 may allow the anonymous user to read arbitrary files ## { #CVE-2022-40308 }

CVE-2022-40308 [\[CVE json\]](./CVE-2022-40308.cve.json) [\[OSV json\]](./CVE-2022-40308.osv.json)



_Last updated: 2022-11-15T13:08:09.007Z_

### Affected

* Apache Archiva from Apache Archiva through 2.2.8


### Description

If anonymous read enabled, it's possible to read the database file directly without logging in.


### References
* https://lists.apache.org/thread/x01pnn0jjsw512cscxsbxzrjmz64n4cc


### Credits
* Thanks to L3yx of Syclover Security Team


## Apache Archiva prior to 2.2.9 allows an authenticated user to delete arbitrary directories ## { #CVE-2022-40309 }

CVE-2022-40309 [\[CVE json\]](./CVE-2022-40309.cve.json) [\[OSV json\]](./CVE-2022-40309.osv.json)



_Last updated: 2022-11-15T13:09:01.491Z_

### Affected

* Apache Archiva from unspecified through 2.2.8


### Description

Users with write permissions to a repository can delete arbitrary directories.

### References
* https://lists.apache.org/thread/1odl4p85r96n27k577jk6ftrp19xfc27


### Credits
* Thanks to L3yx of Syclover Security Team


## Apache Archiva privilege escalation ## { #CVE-2023-28158 }

CVE-2023-28158 [\[CVE json\]](./CVE-2023-28158.cve.json) [\[OSV json\]](./CVE-2023-28158.osv.json)



_Last updated: 2023-03-29T12:21:30.415Z_

### Affected

* Apache Archiva from 2.0 before 2.2.10


### Description

Privilege escalation via stored XSS using the file upload service to upload malicious content.<br><span style="background-color: rgb(255, 255, 255);">The issue can be exploited only by authenticated users which can create directory name to inject some XSS content and gain some privileges such admin user.</span><br><br>

### References
* https://lists.apache.org/thread/8pm6d5y9cptznm0bdny3n8voovmm0dtt


### Credits
* sandr0 (sandr0.xyz)  (finder)


## disabling user registration is not effective ## { #CVE-2024-27138 }

CVE-2024-27138 [\[CVE json\]](./CVE-2024-27138.cve.json) [\[OSV json\]](./CVE-2024-27138.osv.json)



_Last updated: 2024-03-01T15:41:11.276Z_

### Affected

* Apache Archiva from 2.0.0 through *


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** Incorrect Authorization vulnerability in Apache Archiva.</div><div><br></div><div>Apache Archiva has a setting to disable user registration, however this restriction can be bypassed. As Apache Archiva has been retired, we do not expect to release a version of Apache Archiva that fixes this issue. You are recommended to look into migrating to a different solution, or isolate your instance from any untrusted users.<br></div><p></p><div>NOTE: This vulnerability only affects products that are no longer supported by the maintainer</div><div><br></div><br><p></p>

### References
* https://lists.apache.org/thread/070qcpclcb3sqk1hn8j5lvzohp30k1m2


### Credits
* Florian Hauser, @frycos (reporter)


## incorrect authentication potentially leading to account takeover ## { #CVE-2024-27139 }

CVE-2024-27139 [\[CVE json\]](./CVE-2024-27139.cve.json) [\[OSV json\]](./CVE-2024-27139.osv.json)



_Last updated: 2024-03-01T15:40:48.119Z_

### Affected

* Apache Archiva from 2.0.0 through *


### Description

** UNSUPPORTED WHEN ASSIGNED **<br><div><br></div><div>Incorrect Authorization vulnerability in Apache Archiva: a vulnerability in Apache Archiva allows an unauthenticated attacker to modify account data, potentially leading to account takeover.<br></div><p>This issue affects Apache Archiva: from 2.0.0.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.<br></p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.<br></p>

### References
* https://lists.apache.org/thread/qr8b7r86p1hkn0dc0q827s981kf1bgd8


### Credits
* 1uHrm of cyberkl (reporter)


## reflected XSS ## { #CVE-2024-27140 }

CVE-2024-27140 [\[CVE json\]](./CVE-2024-27140.cve.json) [\[OSV json\]](./CVE-2024-27140.osv.json)



_Last updated: 2024-03-01T15:40:06.489Z_

### Affected

* Apache Archiva from 2.0.0 through *


### Description

<div>** UNSUPPORTED WHEN ASSIGNED **<br></div><div><br></div><div>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Archiva.</div><p>This issue affects Apache Archiva: from 2.0.0.</p><p></p><p></p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users. Alternatively, you could configure a HTTP proxy in front of your Archiva instance to only forward requests that do not have malicious characters in the URL.<br></p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p><p></p>

### References
* https://lists.apache.org/thread/xrn6nt904ozh3jym60c3f5hj2fb75pjy


### Credits
* sandr0 / Sandro Bauer (sandr0.xyz) (finder)
* BTullis / Ben Tullis (wikimedia.org) (finder)
* sbassett / Scott Bassett (wikimedia.org) (finder)
* L0ne1y (finder)
