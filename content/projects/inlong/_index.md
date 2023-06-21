---
title: Apache InLong security advisories
description: Security information for Apache InLong
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache InLong? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

## Jdbc Connection causes arbitrary file reading in InLong ## { #CVE-2023-24977 }

[CVE-2023-24977](./CVE-2023-24977.cve.json)

### Affected

* Apache InLong versions 1.1.0 including 1.5.0


### Description

Out-of-bounds Read vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.1.0 through 1.5.0.&nbsp;Users are advised to upgrade to Apache InLong's latest version or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7214">https://github.com/apache/inlong/pull/7214</a>&nbsp;to solve it.</p>

## Jdbc Connection Security Bypass ## { #CVE-2023-24997 }

[CVE-2023-24997](./CVE-2023-24997.cve.json)

### Affected

* Apache InLong versions 1.1.0 including 1.5.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.1.0 through 1.5.0.&nbsp;<span style="background-color: rgb(255, 255, 255);">Users are advised to upgrade to Apache InLong's latest version or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7223">https://github.com/apache/inlong/pull/7223</a></span><span style="background-color: rgb(255, 255, 255);">&nbsp;to solve it.</span></p>

## JDBC Deserialization Vulnerability in InLong ## { #CVE-2023-27296 }

[CVE-2023-27296](./CVE-2023-27296.cve.json)

### Affected

* Apache InLong versions 1.1.0 including 1.5.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Software Foundation Apache InLong.<br><br><span style="background-color: rgb(255, 255, 255);">It could be triggered by authenticated users of InLong,&nbsp;</span>you could refer&nbsp;to [1]&nbsp;to know more about this&nbsp;vulnerability.<br><br>This issue affects Apache InLong: from 1.1.0 through 1.5.0.  Users are advised to upgrade to Apache InLong's latest version or cherry-pick [2]&nbsp;to solve it.<br><br>

<span style="background-color: rgb(255, 255, 255);">[1]&nbsp;</span><a target="_blank" rel="nofollow" href="https://programmer.help/blogs/jdbc-deserialization-vulnerability-learning.html">https://programmer.help/blogs/jdbc-deserialization-vulnerability-learning.html<br><br></a>

<span style="background-color: rgb(255, 255, 255);">[2] </span><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7422">https://github.com/apache/inlong/pull/7422</a>

<br><br>

## SQL injection in apache inLong 1.5.0 ## { #CVE-2023-30465 }

[CVE-2023-30465](./CVE-2023-30465.cve.json)

### Affected

* Apache InLong versions 1.4.0 including 1.5.0


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.5.0.&nbsp;By manipulating the "orderType" parameter and the ordering of the returned content using an SQL injection attack, an attacker can extract the username of the&nbsp;&nbsp; user with ID 1 from the "user" table, one character at a time.&nbsp; Users are advised to upgrade to Apache InLong's 1.6.0 or cherry-pick [1] to solve it.<br><a target="_blank" rel="nofollow" href="https://programmer.help/blogs/jdbc-deserialization-vulnerability-learning.html"><br></a>

<span style="background-color: rgb(255, 255, 255);">[1] </span><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/issues/7529">https://github.com/apache/inlong/issues/7529</a></p>

## JDBC URL bypassing by adding blanks ## { #CVE-2023-31058 }

[CVE-2023-31058](./CVE-2023-31058.cve.json)

### Affected

* Apache InLong versions 1.4.0 including 1.6.0


### Description

Deserialization of Untrusted Data Vulnerability in Apache Software Foundation Apache InLong.<p><span style="background-color: var(--wht);">This issue affects Apache InLong: from 1.4.0 through 1.6.0. </span><span style="background-color: var(--wht);"><span style="background-color: rgb(255, 255, 255);">Attackers would bypass the
'autoDeserialize' option filtering by a<span style="background-color: var(--wht);">dding</span><span style="background-color: var(--wht);"><span style="background-color: rgb(255, 255, 255);">&nbsp;blanks</span></span></span>.  Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7674">

</a><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7674">https://github.com/apache/inlong/pull/7674</a> to solve it.</span></p>

## Privilege escalation vulnerability for InLong ## { #CVE-2023-31062 }

[CVE-2023-31062](./CVE-2023-31062.cve.json)

### Affected

* Apache InLong versions 1.2.0 including 1.6.0


### Description

Improper Privilege Management Vulnerabilities in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.2.0 through 1.6.0.&nbsp; When&nbsp;the attacker has access to a valid (but unprivileged) account, t<span style="background-color: rgb(255, 255, 255);">he exploit can be executed using Burp Suite by sending a login
request and following it with a subsequent HTTP request
using the returned cookie<span style="background-color: rgb(255, 255, 255);">.</span></span></p><p><span style="background-color: rgb(255, 255, 255);">Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <span style="background-color: rgb(255, 255, 255);"><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7836">https://github.com/apache/inlong/pull/7836</a></span> to solve it.</span><span style="background-color: rgb(255, 255, 255);"><br>

</span></p>

## Insecurity direct object references cancelling applications ## { #CVE-2023-31064 }

[CVE-2023-31064](./CVE-2023-31064.cve.json)

### Affected

* Apache InLong versions 1.2.0 including 1.6.0


### Description

Files or Directories Accessible to External Parties vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.2.0 through 1.6.0. the user in InLong could cancel an&nbsp;<span style="background-color: rgb(255, 255, 255);">application that doesn't belongs to it.&nbsp;</span>Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7799">https://github.com/apache/inlong/pull/7799</a> to solve it.<br></p>

## Insufficient Session Expiration in InLong ## { #CVE-2023-31065 }

[CVE-2023-31065](./CVE-2023-31065.cve.json)

### Affected

* Apache InLong versions 1.4.0 including 1.6.0


### Description

Insufficient Session Expiration vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.6.0.&nbsp;


<span style="background-color: rgb(255, 255, 255);">An old session can be used by an attacker even after the user has been deleted or the password has been changed.</span>


Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7836">https://github.com/apache/inlong/pull/7836</a>, <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7884">https://github.com/apache/inlong/pull/7884</a> to solve it.

<br></p>

## Insecure direct object references for inlong sources ## { #CVE-2023-31066 }

[CVE-2023-31066](./CVE-2023-31066.cve.json)

### Affected

* Apache InLong versions 1.4.0 including 1.6.0


### Description

Files or Directories Accessible to External Parties vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.6.0. Different users in InLong could&nbsp;<span style="background-color: rgb(255, 255, 255);">delete, edit, stop, and start others' sources!</span>&nbsp;Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7775">https://github.com/apache/inlong/pull/7775</a> to solve it.<br></p>

## Weak Password Implementation in InLong ## { #CVE-2023-31098 }

[CVE-2023-31098](./CVE-2023-31098.cve.json)

### Affected

* Apache InLong versions 1.1.0 including 1.6.0


### Description

Weak Password Requirements vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.1.0 through 1.6.0.&nbsp;

<span style="background-color: rgb(255, 255, 255);">When users change their password to a simple password (with any character or
symbol), attackers can easily guess the user's password and access the account.</span></p><p>Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7805">https://github.com/apache/inlong/pull/7805</a> to solve it.<br></p>

## Users who joined later can see the data of deleted users ## { #CVE-2023-31101 }

[CVE-2023-31101](./CVE-2023-31101.cve.json)

### Affected

* Apache InLong versions 1.5.0 including 1.6.0


### Description

Insecure Default Initialization of Resource Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.5.0 through 1.6.0.  Users registered in InLong who joined later can see deleted users' data. Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7836">https://github.com/apache/inlong/pull/7836</a> to solve it.<br></p>

## Attackers can change the immutable name and type of cluster ## { #CVE-2023-31103 }

[CVE-2023-31103](./CVE-2023-31103.cve.json)

### Affected

* Apache InLong versions 1.4.0 including 1.6.0


### Description

Exposure of Resource to Wrong Sphere Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.6.0.&nbsp;
Attackers can change the immutable name and type of cluster of InLong.&nbsp;Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7891">https://github.com/apache/inlong/pull/7891</a> to solve it.<br></p>

## Attackers can change the immutable name and type of nodes ## { #CVE-2023-31206 }

[CVE-2023-31206](./CVE-2023-31206.cve.json)

### Affected

* Apache InLong versions 1.4.0 including 1.6.0


### Description

Exposure of Resource to Wrong Sphere Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.4.0 through 1.6.0.&nbsp;<span style="background-color: var(--wht);">Attackers can change the immutable name and type of nodes of InLong. Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick [1] to solve it.</span></p><p><a target="_blank" rel="nofollow" href="https://cveprocess.apache.org/cve5/[1]%C2%A0https://github.com/apache/inlong/pull/7891">[1] </a><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7891">https://github.com/apache/inlong/pull/7891</a></p>

## IDOR make users can delete others' subscription ## { #CVE-2023-31453 }

[CVE-2023-31453](./CVE-2023-31453.cve.json)

### Affected

* Apache InLong versions 1.2.0 including 1.6.0


### Description

Incorrect Permission Assignment for Critical Resource Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.2.0 through 1.6.0. The&nbsp;<span style="background-color: rgb(255, 255, 255);">attacker can delete others' subscriptions, even if they are not the owner
of the deleted subscription</span><span style="background-color: rgb(255, 255, 255);">.&nbsp;</span>Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick [1] to solve it.</p><p>[1] <a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7949">

</a><a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7949">https://github.com/apache/inlong/pull/7949</a>

</p>

<p></p>

## IDOR make users can bind any cluster ## { #CVE-2023-31454 }

[CVE-2023-31454](./CVE-2023-31454.cve.json)

### Affected

* Apache InLong versions 1.2.0 including 1.6.0


### Description

Incorrect Permission Assignment for Critical Resource Vulnerability in Apache Software Foundation Apache InLong.<p>This issue affects Apache InLong: from 1.2.0 through 1.6.0.&nbsp;

<span style="background-color: rgb(255, 255, 255);">The attacker can bind any cluster, even if he is not the cluster owner. Users are advised to upgrade to Apache InLong's 1.7.0 or cherry-pick&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/inlong/pull/7947">https://github.com/apache/inlong/pull/7947</a> to solve it.</span><br>

</p>