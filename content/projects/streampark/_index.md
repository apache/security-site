---
title: Apache StreamPark (Incubating) security advisories
description: Security information for Apache StreamPark (Incubating)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache StreamPark (Incubating)? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## LDAP Injection Vulnerability ## { #CVE-2022-45801 }

[CVE-2022-45801](./CVE-2022-45801.cve.json)

### Affected

* Apache StreamPark (incubating) from 1.0.0 before 2.0.0


### Description

<div><div><span style="background-color: rgb(255, 255, 255);">Apache StreamPark 1.0.0 to 2.0.0 have a LDAP injection vulnerability.</span><br><span style="background-color: rgb(255, 255, 255);">LDAP Injection is an attack used to exploit web based applications</span><br><span style="background-color: rgb(255, 255, 255);">that construct LDAP statements based on user input. When an</span><br><span style="background-color: rgb(255, 255, 255);">application fails to properly sanitize user input, it's possible to</span><br><span style="background-color: rgb(255, 255, 255);">modify LDAP statements through techniques similar to SQL Injection.</span><br><span style="background-color: rgb(255, 255, 255);">LDAP injection attacks could result in the granting of permissions to</span><br><span style="background-color: rgb(255, 255, 255);">unauthorized queries, and content modification inside the LDAP tree.</span><br><span style="background-color: rgb(255, 255, 255);">This risk may only occur when the user logs in with ldap, and the user</span><br><span style="background-color: rgb(255, 255, 255);">name and password login will not be affected, Users of the affected</span><br><span style="background-color: rgb(255, 255, 255);">versions should upgrade to Apache StreamPark 2.0.0 or later.</span><br><br></div></div><br>

### References
* https://lists.apache.org/thread/xbkwwpkp3n2rs2wcxg8l26mhsftxwwr9


## Upload any file to any directory ## { #CVE-2022-45802 }

[CVE-2022-45802](./CVE-2022-45802.cve.json)

### Affected

* Apache StreamPark (incubating) from 1.0.0 before 2.0.0


### Description

<div><div><span style="background-color: var(--wht);">Streampark allows any users to upload a jar as application, but there is no mandatory verification of the uploaded file type, causing users to upload some high-risk files, and may upload them to any directory,&nbsp;</span><span style="background-color: var(--wht);">Users of the affected versions should upgrade to Apache StreamPark 2.0.0 or later</span></div><br></div><br><br>

### References
* https://lists.apache.org/thread/thwl1v2h6r3c21x1qwff08o57qzjnst6


## Logic error causing any account reset ## { #CVE-2022-46365 }

[CVE-2022-46365](./CVE-2022-46365.cve.json)

### Affected

* Apache StreamPark (incubating) from 1.0.0 before 2.0.0


### Description

<span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);"><div><div>Apache StreamPark 1.0.0 <span style="background-color: rgb(255, 255, 255);">before</span> 2.0.0 When the user successfully logs in, to modify his profile, the username will be passed to the server-layer&nbsp;as a parameter, but not verified whether the user name is the currently logged user and whether the user is legal, This will allow malicious attackers to send any username to modify and reset the account,&nbsp;<span style="background-color: rgb(255, 255, 255);">Users of the affected&nbsp;</span><span style="background-color: rgb(255, 255, 255);">versions should upgrade to Apache StreamPark 2.0.0 or later.</span></div></div></span></span><br>

### References
* https://lists.apache.org/thread/f68lcwrp8pcdc4yrbpcm8j7m0f5mjn7h
