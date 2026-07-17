---
title: Apache Fineract security advisories
description: Security information for Apache Fineract
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Fineract? Send your report to the [Apache Fineract Security Team](mailto:security%40fineract.apache.org?subject=%5BFINDING%5D%20Apache%20Fineract).

You can read more about the security policy on:

- [Apache Fineract security model](https://github.com/apache/fineract/security/policy)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Office list: SQL Injection via Subquery in orderBy ## { #CVE-2026-57821 }

CVE-2026-57821 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57821) [\[CVE json\]](./CVE-2026-57821.cve.json)

_Last updated: 2026-07-15T08:40:21.140Z_

### Affected

* Apache Fineract through 1.14.0
* Apache Fineract at 1.15.0 unaffected


### Description

A SQL Injection vulnerability exists in Apache Fineract's Office Search API (<code>GET /api/v1/offices</code>) in versions up to and including 1.14.0. The <code>orderBy</code> request parameter is concatenated into a SQL query without sufficient validation, allowing an authenticated user with permission to view offices to inject arbitrary SQL via a crafted <code>orderBy</code> value. This is a bypass of the <code>ColumnValidator</code> fix introduced for CVE-2024-32838, which does not detect bare subqueries in the <code>ORDER BY</code> position. This can be leveraged to perform time-based blind SQL injection for data exfiltration. Because the injected query blocks the database connection for its full duration, concurrent exploitation can exhaust the application's database connection pool, resulting in denial of service for other users. Users are recommended to upgrade to a version containing the fix.

### References
* https://github.com/apache/fineract/pull/6048
* https://lists.apache.org/thread/lb7zwdv7qntzy6z05gzf7m8mxw9cbgsj
* https://lists.apache.org/thread/rj5vwh3z2xcvsf0rqwj8kokpbrxkhq4n


### Credits
* Venkatraman Kumar (@r3dw0lfsec) at Securin (finder)
* Terence Monteiro (@terencemo) (remediation developer)
* Ádám Sághy (@adamsaghy) (remediation reviewer)


## Boolean SQL Injection in Client Search API (orderBy parameter) leading to Local File Disclosure ## { #CVE-2026-56287 }

CVE-2026-56287 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-56287) [\[CVE json\]](./CVE-2026-56287.cve.json) [\[OSV json\]](./CVE-2026-56287.osv.json)



_Last updated: 2026-07-15T09:19:36.672Z_

### Affected

* Apache Fineract through 1.14.0


### Description

A boolean-based SQL Injection vulnerability exists in Apache Fineract's Client Search API (<code>GET /api/v1/clients</code>) in versions up to and including 1.14.0. The <code>orderBy</code> and <code>sortOrder</code> request parameters are concatenated into a SQL query without sufficient validation, allowing an authenticated user with permission to view clients to inject arbitrary SQL via a crafted <code>orderBy</code> value. This can be leveraged to perform blind boolean-based data extraction and, on MySQL/MariaDB, to disclose arbitrary files readable by the database process via the <code>LOAD_FILE()</code> function. Users are recommended to upgrade to a version containing the fix

### References
* https://lists.apache.org/thread/l5klcj2v0dx63bssvb0gmw1nzzc47col
* https://github.com/apache/fineract/pull/6020


### Credits
* Anirudh Anand (finder)
* Aman Sapra (reporter)
* Terence Monteiro (@terencemo) (remediation developer)
* Ádám Sághy (@adamsaghy) (remediation reviewer)


## SQL injection in runreports endpoint ## { #CVE-2026-35152 }

CVE-2026-35152 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-35152) [\[CVE json\]](./CVE-2026-35152.cve.json) [\[OSV json\]](./CVE-2026-35152.osv.json)



_Last updated: 2026-07-15T09:19:53.550Z_

### Affected

* Apache Fineract through 1.14.0


### Description

A SQL Injection vulnerability exists in Apache Fineract's Report Execution API (<code>runreports</code> endpoint) in versions up to and including 1.14.0. Report parameter values are incorporated into the generated SQL query without sufficient validation, allowing an authenticated user with permission to run reports to inject arbitrary SQL via crafted parameter values. This can be leveraged to perform unauthorized access to data beyond what the report was designed to expose. Users are recommended to upgrade to a version containing the fix.<br>

### References
* https://github.com/apache/fineract/pull/5980
* https://lists.apache.org/thread/d3bzcwsbywz7wg9zxvtlkvgmffqjyfn0
* https://lists.apache.org/thread/658yddn0bpxqw2hpxnyk3vqd05bkchg9


### Credits
* JD Security Shenyi Team (finder)
* Geo Chen (reporter)
* Quac Tran (reporter)
* Terence Monteiro (@terencemo) (remediation developer)
* Ádám Sághy (@adamsaghy) (remediation reviewer)
* Aleksandar Vidakovic (@vidakovic) (remediation reviewer)


## IDOR via self-service API ## { #CVE-2025-58137 }

CVE-2025-58137 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-58137) [\[CVE json\]](./CVE-2025-58137.cve.json)

_Last updated: 2025-12-12T09:20:50.539Z_

### Affected

* Apache Fineract through 1.11.0
* Apache Fineract at 1.12.1 unaffected


### Description

<p>Authorization Bypass Through User-Controlled Key vulnerability in Apache Fineract.</p><p>This issue affects Apache Fineract: through 1.11.0. The issue is fixed in version 1.12.1.</p><p>Users are encouraged to upgrade to version 1.13.0, the latest release.</p>

### References
* https://lists.apache.org/thread/gz3zhoghlclch3rdnzyrdcf69c0507ww


### Credits
* Peter Chen (reporter)
* Ádám Sághy (remediation developer)
* Aleksandar Vidakovic (remediation reviewer)
* Víctor Romero (remediation reviewer)


## Server Key not masked ## { #CVE-2025-58130 }

CVE-2025-58130 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-58130) [\[CVE json\]](./CVE-2025-58130.cve.json)

_Last updated: 2025-12-12T09:20:05.211Z_

### Affected

* Apache Fineract through 1.11.0
* Apache Fineract at 1.12.1 unaffected


### Description

<p>Insufficiently Protected Credentials vulnerability in Apache Fineract.</p><p>This issue affects Apache Fineract: through 1.11.0.&nbsp;The issue is fixed in version 1.12.1.</p><p>Users are encouraged to upgrade to version 1.13.0, the latest release.<br></p>

### References
* https://lists.apache.org/thread/d9zpkc86zk265523tfvbr8w7gyr6onoy


### Credits
* Peter Chen (reporter)
* Jose Alberto Hernandez (remediation developer)
* Ádám Sághy (remediation reviewer)


## weak password policy ## { #CVE-2025-23408 }

CVE-2025-23408 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-23408) [\[CVE json\]](./CVE-2025-23408.cve.json)

_Last updated: 2025-12-12T09:18:57.063Z_

### Affected

* Apache Fineract through 1.10.1
* Apache Fineract at 1.11.0 unaffected


### Description

<p>Weak Password Requirements vulnerability in Apache Fineract.</p><p>This issue affects Apache Fineract: through 1.10.1.&nbsp;The issue is fixed in version 1.11.0.</p><p>Users are encouraged to upgrade to version 1.13.0, the latest release.<br></p>

### References
* https://lists.apache.org/thread/bdlb6wl968yh1n48mr5npsk2spo6dncf


### Credits
* Peter Chen, PayPal Security (finder)
* Kristof Jozsa, BaaSFlow (analyst)


## SQL injection vulnerabilities in offices API endpoint ## { #CVE-2024-32838 }

CVE-2024-32838 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-32838) [\[CVE json\]](./CVE-2024-32838.cve.json) [\[OSV json\]](./CVE-2024-32838.osv.json)



_Last updated: 2025-02-12T09:44:14.259Z_

### Affected

* Apache Fineract from 1.4 through 1.9


### Description

SQL Injection vulnerability in various API endpoints - offices, dashboards, etc. Apache Fineract versions 1.9 and before have a vulnerability that allows an authenticated attacker to inject malicious data into some of the REST API endpoints' query parameter.&nbsp;<div><br>Users are recommended to upgrade to version 1.10.1, which fixes this issue.<br><br>A SQL Validator has been implemented which allows us to configure a series of tests and checks against our SQL queries that will allow us to validate and protect against nearly all potential SQL injection attacks.&nbsp;<br><br></div>

### References
* https://lists.apache.org/thread/7l88h17pn9nf8zpx5bbojk7ko5oxo1dy


### Credits
* Kabilan S - Security engineer at Zoho (finder)
* Aleksandar Vidakovic (remediation developer)


## Under certain system configurations, the sqlSearch parameter for specific endpoints was vulnerable to SQL injection attacks, potentially allowing attackers to manipulate database queries.  ## { #CVE-2024-23539 }

CVE-2024-23539 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23539) [\[CVE json\]](./CVE-2024-23539.cve.json) [\[OSV json\]](./CVE-2024-23539.osv.json)



_Last updated: 2024-03-29T14:36:56.073Z_

### Affected

* Apache Fineract through 1.8.4


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Fineract.<p>This issue affects Apache Fineract: &lt;1.8.5.</p><p>Users are recommended to upgrade to version 1.8.5 or 1.9.0, which fix the issue.</p>

### References
* https://cwiki.apache.org/confluence/display/FINERACT/Apache+Fineract+Security+Report
* https://lists.apache.org/thread/g8sv1gnjv716lx2h89jbvjdgtrrjmy7h


### Credits
* Yash Sancheti of GH Solutions Consultants (finder)


## Under certain system configurations, the sqlSearch parameter was vulnerable to SQL injection attacks, potentially allowing attackers to manipulate database queries. ## { #CVE-2024-23538 }

CVE-2024-23538 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23538) [\[CVE json\]](./CVE-2024-23538.cve.json) [\[OSV json\]](./CVE-2024-23538.osv.json)



_Last updated: 2024-03-29T14:37:38.535Z_

### Affected

* Apache Fineract before 1.8.5


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Fineract.<p>This issue affects Apache Fineract: &lt;1.8.5.</p><p>Users are recommended to upgrade to version 1.8.5 or 1.9.0, which fix the issue.</p>

### References
* https://cwiki.apache.org/confluence/display/FINERACT/Apache+Fineract+Security+Report
* https://lists.apache.org/thread/by32w2dylzgbqm5940x3wj7519wolqxs


### Credits
* Yash Sancheti (reporter)
* Majd Alasfar of ProgressSoft (reporter)


## Under certain circumstances, this vulnerability allowed users, without specific permissions, to escalate their privileges to any role.  ## { #CVE-2024-23537 }

CVE-2024-23537 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23537) [\[CVE json\]](./CVE-2024-23537.cve.json) [\[OSV json\]](./CVE-2024-23537.osv.json)



_Last updated: 2024-03-29T14:38:03.872Z_

### Affected

* Apache Fineract before 1.9.0


### Description

Improper Privilege Management vulnerability in Apache Fineract.<p>This issue affects Apache Fineract: &lt;1.8.5.</p><p>Users are recommended to upgrade to version 1.9.0, which fixes the issue.</p>

### References
* https://cwiki.apache.org/confluence/display/FINERACT/Apache+Fineract+Security+Report
* https://lists.apache.org/thread/fq1ns4nprw2vqpkwwj9sw45jkwxmt9f1


### Credits
*  Yash Sancheti  (reporter)


## SQL injection vulnerability in certain procedure calls  ## { #CVE-2023-25197 }

CVE-2023-25197 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25197) [\[CVE json\]](./CVE-2023-25197.cve.json) [\[OSV json\]](./CVE-2023-25197.osv.json)



_Last updated: 2023-03-28T11:17:16.072Z_

### Affected

* apache fineract from 1.4 through 1.8.2


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Software Foundation apache fineract.<br><p>Authorized users may be able to exploit this for limited impact on components. &nbsp;</p><p>This issue affects apache fineract: from 1.4 through 1.8.2.</p>

### References
* https://lists.apache.org/thread/v0q9x86sx6f6l2nzr1z0nwm3y9qlng04


### Credits
* Eugene Lim at Cyber Security Group (CSG) Government Technology Agency GOVTECH.sg (reporter)
* aleks@apache.org (remediation developer)


## SQL injection vulnerability  ## { #CVE-2023-25196 }

CVE-2023-25196 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25196) [\[CVE json\]](./CVE-2023-25196.cve.json) [\[OSV json\]](./CVE-2023-25196.osv.json)



_Last updated: 2023-03-28T11:16:50.126Z_

### Affected

* Apache Fineract from 1.4 through 1.8.2


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Software Foundation Apache Fineract.<br><p>Authorized users may be able to change or add data in certain components. &nbsp;</p><p>This issue affects Apache Fineract: from 1.4 through 1.8.2.</p>

### References
* https://lists.apache.org/thread/m9x3vpn3bry4fympkzxnnz4qx0oc0w8m


### Credits
*  Zhang Baocheng at Leng Jing Qi Cai Security Lab (reporter)
* Aleks@apache.org (remediation developer)


## SSRF template type vulnerability in certain authenticated users ## { #CVE-2023-25195 }

CVE-2023-25195 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25195) [\[CVE json\]](./CVE-2023-25195.cve.json) [\[OSV json\]](./CVE-2023-25195.osv.json)



_Last updated: 2023-03-28T11:16:21.425Z_

### Affected

* Apache Fineract from 1.4 through 1.8.3


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache Software Foundation Apache Fineract.<br><p>Authorized users with limited permissions can gain access to server and may be able to use server for any outbound traffic.&nbsp;</p><p>This issue affects Apache Fineract: from 1.4 through 1.8.3.</p>

### References
* https://lists.apache.org/thread/m58fdjmtkfp9h4c0r4l48rv995w3qhb6


### Credits
* Huydoppa from GHTK  (reporter)
* Aleksander (remediation developer)


## Apache Fineract allowed an authenticated user to perform remote code execution due to path traversal ## { #CVE-2022-44635 }

CVE-2022-44635 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-44635) [\[CVE json\]](./CVE-2022-44635.cve.json) [\[OSV json\]](./CVE-2022-44635.osv.json)



_Last updated: 2022-11-29T14:22:31.295Z_

### Affected

* Apache Fineract from Apache Fineract 1.8 through 1.8.0
* Apache Fineract from Apache Fineract 1.7 through 1.7.0


### Description

Apache Fineract allowed an authenticated user to perform remote code execution due to a path traversal vulnerability in a file upload component of Apache Fineract, allowing an attacker to run remote code.  This issue affects Apache Fineract version 1.8.0 and prior versions. We recommend users to upgrade to 1.8.1.

### References
* https://lists.apache.org/thread/t8q6fmh3o6yqmy69qtqxppk9yg9wfybg


### Credits
* We would like to thank  Aman Sapra, co-captain of the Super Guesser CTF team & Security researcher at CRED, for reporting this issue, and the Apache Security team for their assistance.  We give kudos and karma to @Aleksandar Vidakovic for resolving this CVE. 


## disabled hostname verificiation ## { #CVE-2020-17514 }

CVE-2020-17514 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17514) [\[CVE json\]](./CVE-2020-17514.cve.json) [\[OSV json\]](./CVE-2020-17514.osv.json)



_Last updated: 2021-05-27T12:07:40.403Z_

### Affected

* Apache Fineract from Apache Fineract before 1.5.0


### Description

Apache Fineract prior to 1.5.0 disables HTTPS hostname verification in ProcessorHelper in the configureClient method. Under typical deployments, a man in the middle attack could be successful.

### References
* https://issues.apache.org/jira/browse/FINERACT-1211


### Credits
* We would like to thank Simon Gerst at https://github.com/intrigus-lgtm  for reporting this issue
