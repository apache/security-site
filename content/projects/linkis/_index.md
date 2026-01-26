---
title: Apache Linkis security advisories
description: Security information for Apache Linkis
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Linkis? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## The Apache Linkis JDBC EngineConn module has a RCE Vulnerability ## { #CVE-2022-39944 }

CVE-2022-39944 [\[CVE json\]](./CVE-2022-39944.cve.json) [\[OSV json\]](./CVE-2022-39944.osv.json)



_Last updated: 2022-10-26T12:44:23.967Z_

### Affected

* Apache Linkis from Apache Linkis through 1.2.0


### Description

In Apache Linkis <=1.2.0 when used with the MySQL Connector/J, a deserialization vulnerability with possible remote code execution impact exists when an attacker has write access to a database and configures a JDBC EC with a MySQL data source and malicious parameters. Therefore, the parameters in the jdbc url should be blacklisted. Versions of Apache Linkis <= 1.2.0 will be affected, We recommend users to update to 1.3.0.


### References
* https://lists.apache.org/thread/rxytj48q17304snonjtyt5lnlw64gccc


### Credits
* This issue was discovered by 4ra1n and zac from ZAC Security Team


## The DatasourceManager module has a serialization attack vulnerability ## { #CVE-2022-44645 }

CVE-2022-44645 [\[CVE json\]](./CVE-2022-44645.cve.json) [\[OSV json\]](./CVE-2022-44645.osv.json)



_Last updated: 2023-02-03T07:43:51.516Z_

### Affected

* Apache Linkis (incubating) through 1.3.0


### Description



In Apache Linkis &lt;=1.3.0 when used with the MySQL Connector/J in the data source module, a deserialization vulnerability with possible remote code execution impact exists when an attacker has to write access to a database and configures new data source with a MySQL data source and malicious parameters. Therefore, the parameters in the JDBC URL should be blacklisted. Versions of Apache Linkis &lt;= 1.3.0 will be affected.<br><br>We recommend users upgrade the version of Linkis to version 1.3.1.<br>

### References
* https://lists.apache.org/thread/zlcfmvt65blqc4n6fxypg6f0ns8fqfz4


### Credits
* Tian Xin WU (Bearcat) , Vulnerability Researcher at Numen Cyber ​​​​Labs, Singapore. (reporter)
* Department of Cyber Security Research (Jumbo, Unc1e) (remediation developer)
* s3gundo of Hundsun Tech  (remediation developer)


## The DatasourceManager module has a Local File Read Vulnerability ## { #CVE-2022-44644 }

CVE-2022-44644 [\[CVE json\]](./CVE-2022-44644.cve.json) [\[OSV json\]](./CVE-2022-44644.osv.json)



_Last updated: 2023-03-15T08:36:49.053Z_

### Affected

* Apache Linkis (incubating) before 1.3.1


### Description

In Apache Linkis &lt;=1.3.0 when used with the MySQL Connector/J in the data source module, an authenticated attacker could read arbitrary local files by connecting a rogue MySQL server, By adding allowLoadLocalInfile to true in the JDBC parameter. Therefore, the parameters in the JDBC URL should be blacklisted. Versions of Apache Linkis &lt;= 1.3.0 will be affected.&nbsp;<br><br><span style="background-color: rgb(255, 255, 255);">We recommend users upgrade the version of Linkis to version 1.3.1</span><br>

### References
* https://lists.apache.org/thread/hwq9ytq6y1kdh9lz5znptkcrdll9x85h


### Credits
* Department of Cyber Security Research (Jumbo, Unc1e), Beijing Zhiqian Technology Co., LTD (reporter)
* s3gundo of Hundsun Tech  (reporter)


## Apache Linkis publicsercice module unrestricted upload of file ## { #CVE-2023-27602 }

CVE-2023-27602 [\[CVE json\]](./CVE-2023-27602.cve.json) [\[OSV json\]](./CVE-2023-27602.osv.json)



_Last updated: 2023-04-11T03:15:38.418Z_

### Affected

* Apache Linkis through 1.3.1


### Description



<span style="background-color: rgb(255, 255, 255);">

In Apache Linkis &lt;=1.3.1, The PublicService module uploads&nbsp;</span><span style="background-color: rgb(255, 255, 255);">files without restrictions on the path to the uploaded&nbsp;</span><span style="background-color: rgb(255, 255, 255);">files, and file types.<br>

We recommend users upgrade the version of Linkis to version 1.3.2.&nbsp;<br></span>

### References
* https://lists.apache.org/thread/wt70jfc0yfs6s5g0wg5dr5klnc48nsp1


### Credits
* Laihan (reporter)


## Apache Linkis Mangaer module engineConn material upload exists Zip Slip issue ## { #CVE-2023-27603 }

CVE-2023-27603 [\[CVE json\]](./CVE-2023-27603.cve.json)

_Last updated: 2023-04-14T07:17:48.297Z_

### Affected

* Apache Linkis through 1.3.1


### Description



<span style="background-color: rgb(255, 255, 255);">

In Apache Linkis &lt;=1.3.1, due to the Manager module engineConn material upload does not check the zip path,&nbsp;This is a Zip Slip issue, which will lead to a&nbsp;</span><span style="background-color: rgb(255, 255, 255);">potential RCE vulnerability.<br>

We recommend users upgrade the version of Linkis to version 1.3.2.

</span>



### References
* https://lists.apache.org/thread/6n1vlvnyn441rm02zdqc0wnpckj8ltn8
* https://www.openwall.com/lists/oss-security/2023/04/10/2


### Credits
* 4ra1n (reporter)


## Apache Linkis gateway module token authentication bypass ## { #CVE-2023-27987 }

CVE-2023-27987 [\[CVE json\]](./CVE-2023-27987.cve.json)

_Last updated: 2023-04-14T07:51:52.905Z_

### Affected

* Apache Linkis through 1.3.1


### Description



In Apache Linkis &lt;=1.3.1,&nbsp;due to the default token generated by Linkis Gateway deployment being too simple, it is easy for attackers to obtain the default token for the attack.&nbsp;Generation rules should add random values.<br>



We recommend users upgrade the version of Linkis to version 1.3.2 And modify the default token value. You can refer to Token authorization[1]<br><a target="_blank" rel="nofollow" href="https://linkis.apache.org/docs/latest/auth/token">https://linkis.apache.org/docs/latest/auth/token</a>



<br>

### References
* https://lists.apache.org/thread/3cr1cz3210wzwngldwrqzm43vwhghp0p
* https://www.openwall.com/lists/oss-security/2023/04/10/3


### Credits
* Laihan (reporter)


## Apache Linkis JDBC EngineCon  has a deserialization command execution ## { #CVE-2023-29215 }

CVE-2023-29215 [\[CVE json\]](./CVE-2023-29215.cve.json) [\[OSV json\]](./CVE-2023-29215.osv.json)



_Last updated: 2023-04-10T07:35:21.175Z_

### Affected

* Apache Linkis through 1.3.1


### Description

In Apache Linkis &lt;=1.3.1, due to the lack of effective filtering
of parameters, an attacker configuring malicious Mysql JDBC parameters in JDBC EengineConn Module will trigger a
deserialization vulnerability and eventually lead to remote code execution. Therefore, the parameters in the Mysql JDBC URL should be blacklisted. Versions of Apache Linkis &lt;= 1.3.0 will be affected.<br>We recommend users upgrade the version of Linkis to version 1.3.2.

<br>

### References
* https://lists.apache.org/thread/o682wz1ggq491ybvjwokxvcdtnzo76ls


### Credits
* sw0rd1ight (reporter)


## Apache Linkis DatasourceManager module has a deserialization command execution ## { #CVE-2023-29216 }

CVE-2023-29216 [\[CVE json\]](./CVE-2023-29216.cve.json) [\[OSV json\]](./CVE-2023-29216.osv.json)



_Last updated: 2024-07-13T14:57:28.538Z_

### Affected

* Apache Linkis through 1.3.1


### Description



In Apache Linkis &lt;=1.3.1, because the parameters are not
effectively filtered, the attacker uses the MySQL data source and malicious parameters to
configure a new data source to trigger a deserialization vulnerability, eventually leading to
remote code execution.<br> Versions of Apache Linkis &lt;= 1.3.0 will be affected.<br>We recommend users upgrade the version of Linkis to version 1.3.2.

<br>

### References
* https://lists.apache.org/thread/18vv0m32oy51nzk8tbz13qdl5569y55l


### Credits
* sw0rd1ight (reporter)


## DatasourceManager module has a  JDBC parameter judgment logic vulnerability that allows for arbitrary file reading ## { #CVE-2023-41916 }

CVE-2023-41916 [\[CVE json\]](./CVE-2023-41916.cve.json) [\[OSV json\]](./CVE-2023-41916.osv.json)



_Last updated: 2024-07-15T07:53:56.163Z_

### Affected

* Apache Linkis DataSource from 1.4.0 before 1.5.0


### Description



In Apache Linkis =1.4.0, due to the lack of effective filtering
of parameters, an attacker configuring malicious Mysql JDBC parameters in the DataSource Manager Module will trigger&nbsp;<span style="background-color: rgb(255, 255, 255);">arbitrary file reading</span>. Therefore, the parameters in the Mysql JDBC URL should be blacklisted. This attack requires the attacker to obtain an authorized account from Linkis before it can be carried out. Versions of Apache Linkis = 1.4.0 will be affected.&nbsp;<br>We recommend users upgrade the version of Linkis to version 1.5.0.

<br>



### References


### Credits
* Pho3n1x  (reporter)


## DataSource Remote code execution vulnerability ## { #CVE-2023-46801 }

CVE-2023-46801 [\[CVE json\]](./CVE-2023-46801.cve.json) [\[OSV json\]](./CVE-2023-46801.osv.json)



_Last updated: 2024-07-15T07:55:28.176Z_

### Affected

* Apache Linkis DataSource from 1.4.0 before 1.6.0


### Description



In Apache Linkis &lt;= 1.5.0, data source management module, when adding Mysql data source, exists remote code execution vulnerability for java version &lt; 1.8.0_241. The deserialization vulnerability exploited through jrmp can inject malicious files into the server and execute them. 

This attack requires the attacker to obtain an authorized account from Linkis before it can be carried out.&nbsp; We recommend that users upgrade the java version to &gt;= 1.8.0_241. Or users upgrade Linkis to version 1.6.0.



### References
* https://lists.apache.org/thread/0dnzh64xy1n7qo3rgo2loz9zn7m9xgdx


### Credits
* Pho3n1x  (reporter)


## JDBC Datasource Module with DB2 has JNDI Injection vulnerability ## { #CVE-2023-49566 }

CVE-2023-49566 [\[CVE json\]](./CVE-2023-49566.cve.json) [\[OSV json\]](./CVE-2023-49566.osv.json)



_Last updated: 2024-07-15T07:56:41.397Z_

### Affected

* Apache Linkis DataSource from * before 1.6.0


### Description



In Apache Linkis &lt;=1.5.0, due to the lack of effective filtering
of parameters, an attacker configuring malicious 

db2

 parameters in the DataSource Manager Module will result&nbsp;in jndi injection. Therefore, the parameters in the DB2 URL should be blacklisted.&nbsp;

This attack requires the attacker to obtain an authorized account from Linkis before it can be carried out.

 Versions of Apache Linkis 

&lt;=1.5.0

 will be affected.<br>We recommend users upgrade the version of Linkis to version 1.6.0.<br>

### References
* https://lists.apache.org/thread/t68yy52lmv7pxgrxnq6rw7rwvk9tb1xj


### Credits
* Joyh (reporter)
* L0ne1y (reporter)


## DataSource module Oracle SQL Database Password Logged ## { #CVE-2023-50740 }

CVE-2023-50740 [\[CVE json\]](./CVE-2023-50740.cve.json) [\[OSV json\]](./CVE-2023-50740.osv.json)



_Last updated: 2024-03-06T13:44:51.798Z_

### Affected

* Apache Linkis DataSource from * before 1.5.0


### Description

In Apache Linkis &lt;=1.4.0, The password is printed to the log when using the Oracle data source of the Linkis data source module.&nbsp;<br>We recommend users upgrade the version of Linkis to version 1.5.0<br>

### References


### Credits
* Jonathan Leitschuh (reporter)


## Privilege Escalation Attack vulnerability ## { #CVE-2024-27181 }

CVE-2024-27181 [\[CVE json\]](./CVE-2024-27181.cve.json) [\[OSV json\]](./CVE-2024-27181.osv.json)



_Last updated: 2024-08-02T09:27:34.414Z_

### Affected

* Apache Linkis Basic management services from 1.3.2 before 1.6.0


### Description



In Apache Linkis &lt;= 1.5.0,

Privilege Escalation in Basic management services where the attacking user is 

<span style="background-color: rgb(255, 255, 255);">a trusted account</span>

 allows access to Linkis's Token information. Users are advised to upgrade to version 1.6.0, which fixes this issue.

### References
* https://lists.apache.org/thread/hosd73l7hxb3rpt5rb0yg0ld11zph4c6


### Credits
* superx (reporter)


## Engine material management Arbitrary file deletion vulnerability ## { #CVE-2024-27182 }

CVE-2024-27182 [\[CVE json\]](./CVE-2024-27182.cve.json) [\[OSV json\]](./CVE-2024-27182.osv.json)



_Last updated: 2024-08-02T09:29:36.766Z_

### Affected

* Apache Linkis  Basic management services from 1.3.2 before 1.6.0


### Description





In Apache Linkis &lt;= 1.5.0,

Arbitrary file deletion in Basic management services on 

<span style="background-color: rgb(255, 255, 255);">A user with an administrator account could delete any file accessible by the Linkis system user</span>

.<br>Users are recommended to upgrade to version 1.6.0, which fixes this issue.



### References
* https://lists.apache.org/thread/2of1p433h8rbq2bx525rtftnk19oz38h


### Credits
* superx (reporter)


## Commons Lang's RandomStringUtils Random string security vulnerability ## { #CVE-2024-39928 }

CVE-2024-39928 [\[CVE json\]](./CVE-2024-39928.cve.json) [\[OSV json\]](./CVE-2024-39928.osv.json)



_Last updated: 2024-09-24T01:38:41.101Z_

### Affected

* Apache Linkis Spark EngineConn from 1.3.0 before 1.6.0


### Description



In Apache Linkis &lt;= 1.5.0, a Random string security vulnerability in Spark EngineConn,&nbsp;random string generated by the Token when starting Py4j uses the Commons Lang's RandomStringUtils.<br>Users are recommended to upgrade to version 1.6.0, which fixes this issue.



### References
* https://lists.apache.org/thread/g664n13nb17rsogcfrn8kjgd8m89p8nw


### Credits
* Hen (reporter)
* Pj fanning  (reporter)


## JDBC Datasource Module with Mysql has file read vulnerability ## { #CVE-2024-45627 }

CVE-2024-45627 [\[CVE json\]](./CVE-2024-45627.cve.json) [\[OSV json\]](./CVE-2024-45627.osv.json)



_Last updated: 2025-01-14T16:13:18.399Z_

### Affected

* Apache Linkis Metadata Query Service JDBC from 1.5.0 before 1.7.0


### Description

In Apache Linkis &lt;1.7.0, due to the lack of effective filtering
of parameters, an attacker configuring malicious Mysql JDBC parameters in the DataSource Manager Module will 

<span style="background-color: rgb(255, 255, 255);">allow the attacker to read arbitrary files from the Linkis server</span>. Therefore, the parameters in the Mysql JDBC URL should be blacklisted. This attack requires the attacker to obtain an authorized account from Linkis before it can be carried out. Versions of Apache Linkis &lt; 1.7.0 will be affected. <br>We recommend users upgrade the version of Linkis to version 1.7.0.

<br>

### References
* https://lists.apache.org/thread/0zzx8lldwoqgzq98mg61hojgpvn76xsh


### Credits
* Le1a (reporter)


## Arbitrary File Read via Double URL Encoding Bypass ## { #CVE-2025-29847 }

CVE-2025-29847 [\[CVE json\]](./CVE-2025-29847.cve.json) [\[OSV json\]](./CVE-2025-29847.osv.json)



_Last updated: 2026-01-19T08:36:04.753Z_

### Affected

* Apache Linkis from 1.3.0 through 1.7.0


### Description

<p>A vulnerability in Apache Linkis.<br><br><b>Problem Description</b><br>When using the JDBC engine and da<br>When using the JDBC engine and data source functionality, if the URL parameter configured on the frontend has undergone multiple rounds of URL encoding, it may bypass the system's checks. This bypass can trigger a vulnerability that allows unauthorized access to system files via JDBC parameters.</p><b>Scope of Impact</b><br>

<span style="background-color: rgb(255, 255, 255);">This issue affects Apache Linkis: from 1.3.0 through 1.7.0.<br><br><b>Severity level</b><br></span>

moderate<br><p><b>Solution</b><br>Continuously check if the connection information contains the "%" character; if it does, perform URL decoding.<br><br>Users are recommended to upgrade to version 1.8.0, which fixes the issue.<br></p><p>

<span style="background-color: rgb(255, 255, 255);">More questions about this vulnerability can be discussed here:</span>&nbsp;<a target="_blank" rel="nofollow" href="https://lists.apache.org/list?dev@linkis.apache.org:2025-9:cve">https://lists.apache.org/list?dev@linkis.apache.org:2025-9:cve</a><br></p>

### References
* https://lists.apache.org/thread/03l5rfkgdt022o75jp8x4tzpqxz8g057


### Credits
* Le1a and A1kaid from Threatbook (finder)
* kinghao (analyst)
* Le1a from Threatbook (remediation developer)
* kinghao (remediation reviewer)


## Password Exposure ## { #CVE-2025-59355 }

CVE-2025-59355 [\[CVE json\]](./CVE-2025-59355.cve.json) [\[OSV json\]](./CVE-2025-59355.osv.json)



_Last updated: 2026-01-19T08:37:22.783Z_

### Affected

* Apache Linkis from 1.0.0 through 1.7.0


### Description

<p>A vulnerability.<br><br>When org.apache.linkis.metadata.util.HiveUtils.decode() fails to perform Base64 decoding, it records the complete input parameter string in the log via logger.error(str + "decode failed", e). If the input parameter contains sensitive information such as Hive Metastore keys, plaintext passwords will be left in the log files when decoding fails, resulting in information leakage.</p><p><br><b>Affected Scope</b><br>Component: Sensitive fields in hive-site.xml (e.g., javax.jdo.option.ConnectionPassword) or other fields encoded in Base64.<br>Version: Apache Linkis 1.0.0 – 1.7.0</p><br><p><b>Trigger Conditions</b><br>The value of the configuration item is an invalid Base64 string.<br>Log files are readable by users other than hive-site.xml administrators.</p><p><br><b>Severity: Low</b><br>The probability of Base64 decoding failure is low.<br>The leakage is only triggered when logs at the Error level are exposed.<br><br><b>Remediation</b><br>Apache Linkis 1.8.0 and later versions have replaced the log with desensitized content.<br>logger.error("URL decode failed: {}", e.getMessage());   // 不再输出 str<br><br><br>Users are recommended to upgrade to version 1.8.0, which fixes the issue.<br></p>

### References
* https://lists.apache.org/thread/75z7vhftw6w1mllndgpkfmcj0fzo4lbj
* https://lists.apache.org/thread/4dcgmqdkk2p5y4k43ok5rgd4ylx8698h


### Credits
* Kyler (finder)
* kinghao (analyst)
* Le1a (remediation developer)
* kinghao (remediation reviewer)
