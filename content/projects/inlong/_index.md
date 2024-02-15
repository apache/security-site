---
title: Apache InLong security advisories
description: Security information for Apache InLong
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache InLong? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Deserialization attack in Apache InLong prior to version 1.3.0 allows RCE via JDBC ## { #CVE-2022-40955 }

CVE-2022-40955 [\[CVE json\]](./CVE-2022-40955.cve.json)

### Affected

* Apache InLong from Apache InLong before 1.3.0


### Description

In versions of Apache InLong prior to 1.3.0, an attacker with sufficient privileges to specify MySQL JDBC connection URL parameters and to write arbitrary data to the MySQL database, could cause this data to be deserialized by Apache InLong, potentially leading to Remote Code Execution on the Apache InLong server.

Users are advised to upgrade to Apache InLong 1.3.0 or newer.

### References
* https://lists.apache.org/thread/r1r34y7bchrpmp9jhfdoohzdmk7pj1q1


### Credits
* This issue was discovered by 4ra1n of Chaitin Tech.


## Jdbc Connection causes arbitrary file reading in InLong ## { #CVE-2023-24977 }

CVE-2023-24977 [\[CVE json\]](./CVE-2023-24977.cve.json)

### Affected

* Apache InLong from 1.1.0 through 1.5.0


### Description

Out-of-bounds Read vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.1.0 through 1.5.0.&nbsp;Users are advised to upgrade to Apache InLong's latest version or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7214">https://github.com/apache/inlong/pull/7214</a>&nbsp;to solve it.</p>

### References
* https://lists.apache.org/thread/ggozxorctn3tdll7bgmpwwcbjnd0s6w7


### Credits
* This issue was discovered by s3gundo of Hundsun Tech (finder)


## Jdbc Connection Security Bypass ## { #CVE-2023-24997 }

CVE-2023-24997 [\[CVE json\]](./CVE-2023-24997.cve.json)

### Affected

* Apache InLong from 1.1.0 through 1.5.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.1.0 through 1.5.0.&nbsp;<span style="background-color: rgb(255, 255, 255);">Users are advised to upgrade to Apache InLong's latest version or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7223">https://github.com/apache/inlong/pull/7223</a></span><span style="background-color: rgb(255, 255, 255);">&nbsp;to solve it.</span></p>

### References
* https://lists.apache.org/thread/nxvtxq7oxhwyzo9ty2hqz8rvh5r7ngd8


### Credits
* This issue was discovered by s3gundo of Hundsun Tech (finder)


## JDBC Deserialization Vulnerability in InLong ## { #CVE-2023-27296 }

CVE-2023-27296 [\[CVE json\]](./CVE-2023-27296.cve.json)

### Affected

* Apache InLong from 1.1.0 through 1.5.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Software Foundation Apache InLong.<br><br><span style="background-color: rgb(255, 255, 255);">It could be triggered by authenticated users of InLong,&nbsp;</span>you could refer&nbsp;to [1]&nbsp;to know more about this&nbsp;vulnerability.<br><br>This issue affects Apache InLong: from 1.1.0 through 1.5.0.  Users are advised to upgrade to Apache InLong's latest version or cherry-pick [2]&nbsp;to solve it.<br><br>

<span style="background-color: rgb(255, 255, 255);">[1]&nbsp;</span><a target="_blank" rel="nofollow" href="https://programmer.help/blogs/jdbc-deserialization-vulnerability-learning.html">https://programmer.help/blogs/jdbc-deserialization-vulnerability-learning.html<br><br></a>

<span style="background-color: rgb(255, 255, 255);">[2] </span><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7422">https://github.com/apache/inlong/pull/7422</a>

<br><br>

### References
* https://lists.apache.org/thread/xbvtjw9bwzgbo9fp1by8o3p49nf59xzt


### Credits
* escape Wang (finder)


## SQL injection in apache inLong 1.5.0 ## { #CVE-2023-30465 }

CVE-2023-30465 [\[CVE json\]](./CVE-2023-30465.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.5.0


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.5.0.&nbsp;By manipulating the "orderType" parameter and the ordering of the returned content using an SQL injection attack, an attacker can extract the username of the&nbsp;&nbsp; user with ID 1 from the "user" table, one character at a time.&nbsp; Users are advised to upgrade to Apache InLong's 1.6.0 or cherry-pick [1] to solve it.<br><a target="_blank" rel="nofollow" href="https://programmer.help/blogs/jdbc-deserialization-vulnerability-learning.html"><br></a>

<span style="background-color: rgb(255, 255, 255);">[1] </span><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/issues/7529">https://github.com/apache/inlong/issues/7529</a></p>

### References
* https://lists.apache.org/thread/mrh4nr3jrlbj6nxkn4q8hddbfh1pnok0


### Credits
* escape Wang (finder)


## JDBC URL bypassing by adding blanks ## { #CVE-2023-31058 }

CVE-2023-31058 [\[CVE json\]](./CVE-2023-31058.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.6.0


### Description

Deserialization of Untrusted Data Vulnerability in Apache Software Foundation Apache InLong.<p><span style="background-color: var(--wht);">This issue affects Apache InLong: from 1.4.0 through 1.6.0. </span><span style="background-color: var(--wht);"><span style="background-color: rgb(255, 255, 255);">Attackers would bypass the
'autoDeserialize' option filtering by a<span style="background-color: var(--wht);">dding</span><span style="background-color: var(--wht);"><span style="background-color: rgb(255, 255, 255);">&nbsp;blanks</span></span></span>.  Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7674">

</a><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7674">https://github.com/apache/inlong/pull/7674</a> to solve it.</span></p>

### References
* https://lists.apache.org/thread/bkcgbn9l61croxfyspf7xd42qb189s3z


### Credits
* sw0rd1ight of Caiji Sec Team (finder)
* 4ra1n of Chaitin Tech (finder)
* H Ming (finder)


## Privilege escalation vulnerability for InLong ## { #CVE-2023-31062 }

CVE-2023-31062 [\[CVE json\]](./CVE-2023-31062.cve.json)

### Affected

* Apache InLong from 1.2.0 through 1.6.0


### Description

Improper Privilege Management Vulnerabilities in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.2.0 through 1.6.0.&nbsp; When&nbsp;the attacker has access to a valid (but unprivileged) account, t<span style="background-color: rgb(255, 255, 255);">he exploit can be executed using Burp Suite by sending a login
request and following it with a subsequent HTTP request
using the returned cookie<span style="background-color: rgb(255, 255, 255);">.</span></span></p><p><span style="background-color: rgb(255, 255, 255);">Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <span style="background-color: rgb(255, 255, 255);"><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7836">https://github.com/apache/inlong/pull/7836</a></span> to solve it.</span><span style="background-color: rgb(255, 255, 255);"><br>

</span></p>

### References
* https://lists.apache.org/thread/btorjbo9o71h22tcvxzy076022hjdzq0


### Credits
* escape Wang (finder)


## Insecurity direct object references cancelling applications ## { #CVE-2023-31064 }

CVE-2023-31064 [\[CVE json\]](./CVE-2023-31064.cve.json)

### Affected

* Apache InLong from 1.2.0 through 1.6.0


### Description

Files or Directories Accessible to External Parties vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.2.0 through 1.6.0. the user in InLong could cancel an&nbsp;<span style="background-color: rgb(255, 255, 255);">application that doesn't belongs to it.&nbsp;</span>Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7799">https://github.com/apache/inlong/pull/7799</a> to solve it.<br></p>

### References
* https://lists.apache.org/thread/1osd2k3t3qol2wdsswqtr9gxdkf78n00


### Credits
* lujie.ac.cn (finder)


## Insufficient Session Expiration in InLong ## { #CVE-2023-31065 }

CVE-2023-31065 [\[CVE json\]](./CVE-2023-31065.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.6.0


### Description

Insufficient Session Expiration vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.6.0.&nbsp;


<span style="background-color: rgb(255, 255, 255);">An old session can be used by an attacker even after the user has been deleted or the password has been changed.</span>


Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7836">https://github.com/apache/inlong/pull/7836</a>, <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7884">https://github.com/apache/inlong/pull/7884</a> to solve it.

<br></p>

### References
* https://lists.apache.org/thread/to7o0n2cks0omtwo6mhh5cs2vfdbplqf


### Credits
* lujie.ac.cn (finder)


## Insecure direct object references for inlong sources ## { #CVE-2023-31066 }

CVE-2023-31066 [\[CVE json\]](./CVE-2023-31066.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.6.0


### Description

Files or Directories Accessible to External Parties vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.6.0. Different users in InLong could&nbsp;<span style="background-color: rgb(255, 255, 255);">delete, edit, stop, and start others' sources!</span>&nbsp;Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7775">https://github.com/apache/inlong/pull/7775</a> to solve it.<br></p>

### References
* https://lists.apache.org/thread/x7y05wo37sq5l9fnmmsjh2dr9kcjrcxf


### Credits
* lujie.ac.cn (finder)


## Weak Password Implementation in InLong ## { #CVE-2023-31098 }

CVE-2023-31098 [\[CVE json\]](./CVE-2023-31098.cve.json)

### Affected

* Apache InLong from 1.1.0 through 1.6.0


### Description

Weak Password Requirements vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.1.0 through 1.6.0.&nbsp;

<span style="background-color: rgb(255, 255, 255);">When users change their password to a simple password (with any character or
symbol), attackers can easily guess the user's password and access the account.</span></p><p>Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7805">https://github.com/apache/inlong/pull/7805</a> to solve it.<br></p>

### References
* https://lists.apache.org/thread/1fvloc3no1gbffzrcsx9ltsg08wr2d1w


### Credits
* lujie.ac.cn (finder)


## Users who joined later can see the data of deleted users ## { #CVE-2023-31101 }

CVE-2023-31101 [\[CVE json\]](./CVE-2023-31101.cve.json)

### Affected

* Apache InLong from 1.5.0 through 1.6.0


### Description

Insecure Default Initialization of Resource Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.5.0 through 1.6.0.  Users registered in InLong who joined later can see deleted users' data. Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7836">https://github.com/apache/inlong/pull/7836</a> to solve it.<br></p>

### References
* https://lists.apache.org/thread/shvwwr6toqz5rr39rwh4k03z08sh9jmr


### Credits
* lujie.ac.cn (finder)


## Attackers can change the immutable name and type of cluster ## { #CVE-2023-31103 }

CVE-2023-31103 [\[CVE json\]](./CVE-2023-31103.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.6.0


### Description

Exposure of Resource to Wrong Sphere Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.6.0.&nbsp;
Attackers can change the immutable name and type of cluster of InLong.&nbsp;Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7891">https://github.com/apache/inlong/pull/7891</a> to solve it.<br></p>

### References
* https://lists.apache.org/thread/bv51zhjookcnfbz8b0xsl9wv78sn0j1p


## Attackers can change the immutable name and type of nodes ## { #CVE-2023-31206 }

CVE-2023-31206 [\[CVE json\]](./CVE-2023-31206.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.6.0


### Description

Exposure of Resource to Wrong Sphere Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.6.0.&nbsp;<span style="background-color: var(--wht);">Attackers can change the immutable name and type of nodes of InLong. Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick [1] to solve it.</span></p><p><a target="_blank" rel="nofollow" href="https://cveprocess.apache.org/cve5/[1]%C2%A0https://github.com/apache/inlong/pull/7891">[1] </a><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7891">https://github.com/apache/inlong/pull/7891</a></p>

### References
* https://lists.apache.org/thread/qb7zffo785wzpmsobjqcypodngw6kg6x


## IDOR make users can delete others' subscription ## { #CVE-2023-31453 }

CVE-2023-31453 [\[CVE json\]](./CVE-2023-31453.cve.json)

### Affected

* Apache InLong from 1.2.0 through 1.6.0


### Description

Incorrect Permission Assignment for Critical Resource Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.2.0 through 1.6.0. The&nbsp;<span style="background-color: rgb(255, 255, 255);">attacker can delete others' subscriptions, even if they are not the owner
of the deleted subscription</span><span style="background-color: rgb(255, 255, 255);">.&nbsp;</span>Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick [1] to solve it.</p><p>[1] <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7949">

</a><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7949">https://github.com/apache/inlong/pull/7949</a>

</p>

<p></p>

### References
* https://lists.apache.org/thread/9nz8o2skgc5230w276h4w92j0zstnl06


## IDOR make users can bind any cluster ## { #CVE-2023-31454 }

CVE-2023-31454 [\[CVE json\]](./CVE-2023-31454.cve.json)

### Affected

* Apache InLong from 1.2.0 through 1.6.0


### Description

Incorrect Permission Assignment for Critical Resource Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.2.0 through 1.6.0.&nbsp;

<span style="background-color: rgb(255, 255, 255);">The attacker can bind any cluster, even if he is not the cluster owner. Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7947">https://github.com/apache/inlong/pull/7947</a> to solve it.</span><br>

</p>

### References
* https://lists.apache.org/thread/nqt1tr6pbq8q4b033d7sg5gltx5pmjgl


## General user can delete and update process ## { #CVE-2023-34189 }

CVE-2023-34189 [\[CVE json\]](./CVE-2023-34189.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.7.0


### Description

Exposure of Resource to Wrong Sphere Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.7.0. The attacker could use general users to delete and update the process, which only the admin can operate occurrences.&nbsp;

Users are advised to upgrade to Apache InLong's 1.8.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/8109">https://github.com/apache/inlong/pull/8109</a>&nbsp;to solve it.

</p>

### References
* https://lists.apache.org/thread/smxqyx43hxjvzv4w71n2n3rfho9p378s


## JDBC URL bypassing by allowLoadLocalInfileInPath param ## { #CVE-2023-34434 }

CVE-2023-34434 [\[CVE json\]](./CVE-2023-34434.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.7.0


### Description

Deserialization of Untrusted Data Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.7.0.&nbsp;

The attacker could bypass the current logic and achieve arbitrary file reading. To solve it, users are advised to upgrade to Apache InLong's 1.8.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/8130">https://github.com/apache/inlong/pull/8130</a>.

</p>

### References
* https://lists.apache.org/thread/7f1o71w5r732cspltmtdydn01gllf4jo


### Credits
* sw0rd1ight and 4ra1n of Chaitin Tech (finder)


## SQL injection in audit endpoint ## { #CVE-2023-35088 }

CVE-2023-35088 [\[CVE json\]](./CVE-2023-35088.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.7.0


### Description

Improper Neutralization of Special Elements Used in an SQL Command ('SQL Injection') vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.7.0.&nbsp;
In the toAuditCkSql method, the groupId, streamId, auditId, and dt are directly concatenated into the SQL query statement, which may lead to SQL injection attacks.
Users are advised to upgrade to Apache InLong's 1.8.0 or cherry-pick [1] to solve it.

</p><p>

<span style="background-color: rgb(255, 255, 255);">[1] </span><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/8198">https://github.com/apache/inlong/pull/8198</a>

<br></p>

### References
* https://lists.apache.org/thread/os7b66x4n8dbtrdpb7c6x37bb1vjb0tk


## General user Unauthorized access User Management ## { #CVE-2023-43666 }

CVE-2023-43666 [\[CVE json\]](./CVE-2023-43666.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.8.0


### Description

Insufficient Verification of Data Authenticity vulnerability in Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.8.0,&nbsp;

<span style="background-color: rgb(255, 255, 255);">General user can view all user data like Admin account.</span>

<span style="background-color: var(--wht);">Users are advised to upgrade to Apache InLong's 1.9.0 or cherry-pick [1] to solve it.</span></p><p>

[1]&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/8623">https://github.com/apache/inlong/pull/8623</a></p><p></p>

### References
* https://lists.apache.org/thread/scbgh3ty3xcxm3q33r2t9f42gwwo1why


## Log Injection in Global functions ## { #CVE-2023-43667 }

CVE-2023-43667 [\[CVE json\]](./CVE-2023-43667.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.8.0


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.8.0, the a<span style="background-color: rgb(255, 255, 255);">ttacker can create misleading or false records, making it harder to audit
and trace malicious activities.&nbsp;</span>Users are advised to upgrade to Apache InLong's 1.8.0 or cherry-pick [1] to solve it.</p><p>

<span style="background-color: rgb(255, 255, 255);">[1] </span><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/8628">https://github.com/apache/inlong/pull/8628</a></p><p></p>

### References
* https://lists.apache.org/thread/spnb378g268p1f902fr9kqyph2k8n543


## Jdbc Connection Security Bypass in InLong ## { #CVE-2023-43668 }

CVE-2023-43668 [\[CVE json\]](./CVE-2023-43668.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.8.0


### Description

Authorization Bypass Through User-Controlled Key vulnerability in Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.8.0,&nbsp;

<span style="background-color: rgb(255, 255, 255);">some sensitive params  checks will be </span><span style="background-color: rgb(255, 255, 255);">bypassed, <span style="background-color: rgb(255, 255, 255);">like "autoDeserizalize","</span><span style="background-color: rgb(255, 255, 255);">allowLoadLocalInfile"....</span>

.</span>&nbsp;&nbsp;


<span style="background-color: var(--wht);">Users are advised to upgrade to Apache InLong's 1.9.0 or cherry-pick [1] to solve it.</span>

</p><p>[1]&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/8604">https://github.com/apache/inlong/pull/8604</a></p>

### References
* https://lists.apache.org/thread/16gtk7rpdm1rof075ro83fkrnhbzn5sh


### Credits
* nbxiglk (finder)


## Apache inlong has an Arbitrary File Read Vulnerability ## { #CVE-2023-46227 }

CVE-2023-46227 [\[CVE json\]](./CVE-2023-46227.cve.json)

### Affected

* Apache InLong from 1.4.0 through 1.8.0


### Description



<span style="background-color: rgb(255, 255, 255);">

Deserialization of Untrusted Data Vulnerability in Apache Software Foundation Apache InLong.

</span><p>This issue affects Apache InLong: from 1.4.0 through 1.8.0, the a<span style="background-color: rgb(255, 255, 255);">ttacker can use \t to bypass.&nbsp;</span>Users are advised to upgrade to Apache InLong's 1.9.0 or cherry-pick [1] to solve it.</p><p><span style="background-color: rgb(255, 255, 255);">[1] </span><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/8814"></a><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/8814">https://github.com/apache/inlong/pull/8814</a></p>



### References
* https://lists.apache.org/thread/m8txor4f76tmrxksrmc87tw42g57nz33


### Credits
* Snakinya (finder)
* s3gundo (finder)


## Remote Code Execution vulnerability in Apache InLong Manager ## { #CVE-2023-51784 }

CVE-2023-51784 [\[CVE json\]](./CVE-2023-51784.cve.json)

### Affected

* Apache InLong from 1.5.0 through 1.9.0


### Description

Improper Control of Generation of Code ('Code Injection') vulnerability in Apache InLong.<p>This issue affects Apache InLong: from 1.5.0 through 1.9.0, which could lead to Remote Code Execution.&nbsp;<span style="background-color: var(--wht);">Users are advised to upgrade to Apache InLong's 1.10.0 or cherry-pick [1] to solve it.</span></p><p><span style="background-color: rgb(255, 255, 255);">[1] </span><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/8814"></a><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/9329">https://github.com/apache/inlong/pull/9329</a></p><p></p>

### References
* https://lists.apache.org/thread/4nxbyl6mh5jgh0plk0qposbxwn6w9h8j


### Credits
* X1r0z (finder)


## Arbitrary File Read Vulnerability in Apache InLong Manager ## { #CVE-2023-51785 }

CVE-2023-51785 [\[CVE json\]](./CVE-2023-51785.cve.json)

### Affected

* Apache InLong from 1.7.0 through 1.9.0


### Description

Deserialization of Untrusted Data vulnerability in Apache InLong.<p>This issue affects Apache InLong: from 1.7.0 through 1.9.0, the attackers&nbsp;can make a arbitrary file read attack using mysql driver.&nbsp;<span style="background-color: var(--wht);">Users are advised to upgrade to Apache InLong's 1.10.0 or cherry-pick [1] to solve it.</span></p><p><span style="background-color: rgb(255, 255, 255);">[1]&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/9331">https://github.com/apache/inlong/pull/9331</a></span></p>

<p></p>

### References
* https://lists.apache.org/thread/g0yjmtjqvp8bnf1j0tdsk0nhfozjdjno


### Credits
* X1r0z (finder)
