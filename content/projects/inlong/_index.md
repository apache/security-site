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