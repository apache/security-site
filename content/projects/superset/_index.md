---
title: Apache Superset security advisories
description: Security information for Apache Superset
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Superset? You can read more about the projects' security policy on their [security page](https://superset.apache.org/docs/security/), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://superset.apache.org/docs/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Superset stored XSS on Dashboard markdown ## { #CVE-2021-27907 }

CVE-2021-27907 [\[CVE json\]](./CVE-2021-27907.cve.json) [\[OSV json\]](./CVE-2021-27907.osv.json)



_Last updated: 2021-03-05T11:29:37.298Z_

### Affected

* Apache Superset from Apache Superset  through 0.38.0


### Description

Apache Superset up to and including 0.38.0 allowed the creation of a Markdown component on a Dashboard page for describing chart's related information. Abusing this functionality, a malicious user could inject javascript code executing unwanted action in the context of the user's browser. The javascript code will be automatically executed (Stored XSS) when a legitimate user surfs on the dashboard page. The vulnerability is exploitable creating a “div” section and embedding in it a “svg” element with javascript code.

### References
* https://lists.apache.org/thread.html/r09293fb09f1d617f0d2180c42210e739e2211f8da9bc5c1873bea67a%40%3Cdev.superset.apache.org%3E


### Credits
* This issue was reported by Gianluca Veltri and Dario Castrogiovanni of Cuebiq


## Apache Superset Open Redirect  ## { #CVE-2021-28125 }

CVE-2021-28125 [\[CVE json\]](./CVE-2021-28125.cve.json) [\[OSV json\]](./CVE-2021-28125.osv.json)



_Last updated: 2021-04-27T09:22:22.370Z_

### Affected

* Apache Superset from Apache Superset through 1.0.1


### Description

Apache Superset up to and including 1.0.1 allowed for the creation of an external URL that could be malicious. By not checking user input for open redirects the URL shortener functionality would allow for a malicious user to create a short URL for a dashboard that could convince the user to click the link.

  

### References
* https://lists.apache.org/thread.html/r89b5d0dd35c1adc9624b48d6247729c73b2641b32754226661368434%40%3Cdev.superset.apache.org%3E


### Credits
* Found and reported by Gianluca Veltri, Dario Castrogiovanni


## XSS vulnerability on Explore page ## { #CVE-2021-32609 }

CVE-2021-32609 [\[CVE json\]](./CVE-2021-32609.cve.json) [\[OSV json\]](./CVE-2021-32609.osv.json)



_Last updated: 2021-10-15T15:41:12.188Z_

### Affected

* Apache Superset from unspecified through 1.1


### Description

Apache Superset up to and including 1.1 does not sanitize titles correctly on the Explore page. This allows an attacker with Explore access to save a chart with a malicious title, injecting html (including scripts) into the page.

### References
* https://lists.apache.org/thread.html/r2c09254e98b4f8b3deb422762bd0e2aa6d743b72d96c2f90cbaae31a%40%3Cdev.superset.apache.org%3E


### Credits
* Apache Superset team would like to thank Oscar Arnflo for reporting this issue


## Improper access to dataset metadata information  ## { #CVE-2021-37839 }

CVE-2021-37839 [\[CVE json\]](./CVE-2021-37839.cve.json) [\[OSV json\]](./CVE-2021-37839.osv.json)



_Last updated: 2022-07-06T12:31:11.639Z_

### Affected

* Apache Superset from Apache Superset before 1.5.1


### Description

Apache Superset up to 1.5.1 allowed for authenticated users to access metadata information related to datasets they have no permission on. This metadata included the dataset name, columns and metrics.

### References
* https://lists.apache.org/thread/pwqyxxmn5gh7cnw3qsp66v0lt4xojt82


### Credits
* Apache Superset would like to thank Dinesh for reporting this issue


## Possible SQL Injection when template processing is enabled ## { #CVE-2021-41971 }

CVE-2021-41971 [\[CVE json\]](./CVE-2021-41971.cve.json) [\[OSV json\]](./CVE-2021-41971.osv.json)



_Last updated: 2021-10-15T15:41:52.156Z_

### Affected

* Apache Superset from Apache Superset before 1.3.1


### Description

Apache Superset up to and including 1.3.0 when configured with ENABLE_TEMPLATE_PROCESSING on (disabled by default) allowed SQL injection when a malicious authenticated user sends an http request with a custom URL.


### References
* https://lists.apache.org/thread.html/rf7292731268c6c6e2196ae1583e32ac7189385364268f8d9215e8e6d%40%3Cdev.superset.apache.org%3E


### Credits
* Apache Superset would like to thank Kevin Kusnardi for reporting this issue


## Credentials leak ## { #CVE-2021-41972 }

CVE-2021-41972 [\[CVE json\]](./CVE-2021-41972.cve.json) [\[OSV json\]](./CVE-2021-41972.osv.json)



_Last updated: 2021-11-12T15:41:43.888Z_

### Affected

* Apache Superset from Apache Superset through 1.3.1


### Description

Apache Superset up to and including 1.3.1 allowed for database connections password leak for authenticated users. This information could be accessed in a non-trivial way.


### References
* https://lists.apache.org/thread/xpdl2r538o695o7r9gd9qrwqb17bdd3v
* https://seclists.org/oss-sec/2021/q4/106


### Credits
* Apache Superset team would like to thank Ke Zhu for reporting this issue


## Possible log injection ## { #CVE-2021-42250 }

CVE-2021-42250 [\[CVE json\]](./CVE-2021-42250.cve.json) [\[OSV json\]](./CVE-2021-42250.osv.json)



_Last updated: 2021-11-17T15:04:59.176Z_

### Affected

* Apache Superset from Apache Superset through 1.3.1


### Description

Improper output neutralization for Logs. A specific Apache Superset HTTP endpoint allowed for an authenticated user to forge log entries or inject malicious content into logs.

### References
* https://lists.apache.org/thread/53lkszw6d3tybp5t99nvgcj538b9trw9


### Credits
* Found and reported by Duxiaoman Financial Security Team


## API sensitive information leak ## { #CVE-2021-44451 }

CVE-2021-44451 [\[CVE json\]](./CVE-2021-44451.cve.json) [\[OSV json\]](./CVE-2021-44451.osv.json)



_Last updated: 2022-02-01T11:29:10.593Z_

### Affected

* Apache Superset from Apache Superset through 1.3.2


### Description

Apache Superset up to and including 1.3.2 allowed for registered database connections password leak for authenticated users. This information could be accessed in a non-trivial way.  Users should upgrade to Apache Superset 1.4.0 or higher.

### References
* https://lists.apache.org/thread/xww1pccs2ckb5506wrf1v4lmxg198vkb


### Credits
* Found and reported by Cesar Santos


## SQL injection vulnerability in chart data API ## { #CVE-2022-27479 }

CVE-2022-27479 [\[CVE json\]](./CVE-2022-27479.cve.json) [\[OSV json\]](./CVE-2022-27479.osv.json)



_Last updated: 2022-04-13T19:02:41.528Z_

### Affected

* Apache Superset from unspecified before 1.4.2


### Description

Apache Superset before 1.4.2 is vulnerable to SQL injection in chart data requests. Users should update to 1.4.2 or higher which addresses this issue.

### References
* https://lists.apache.org/thread/94th50j5d0y2fw7ysx0g7w3t6jk3z7q6
* https://lists.apache.org/thread/ztb9b6jd9rngoxwvq8r4fhpp401o613y


## Dashboard metadata information leak ## { #CVE-2022-45438 }

CVE-2022-45438 [\[CVE json\]](./CVE-2022-45438.cve.json) [\[OSV json\]](./CVE-2022-45438.osv.json)



_Last updated: 2023-01-25T08:27:38.187Z_

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

When explicitly enabling the feature flag DASHBOARD_CACHE (disabled by default), the system allowed for an unauthenticated user to access dashboard configuration metadata using a REST API Get endpoint.&nbsp;<span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.</span><br>

### References
* https://lists.apache.org/thread/snxbkf2x9kww7s0wkmydct9nhqqn9rv9


### Credits
* Sunny Alexli (finder)


## SQL injection vulnerability in adhoc clauses ## { #CVE-2022-41703 }

CVE-2022-41703 [\[CVE json\]](./CVE-2022-41703.cve.json) [\[OSV json\]](./CVE-2022-41703.osv.json)



_Last updated: 2023-04-11T14:58:41.701Z_

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

A vulnerability in the SQL Alchemy connector of Apache Superset allows an authenticated user with read access to a specific database to add subqueries to the WHERE and HAVING fields referencing tables on the same database that the user should not have access to, despite the user having the feature flag "ALLOW_ADHOC_SUBQUERY" disabled (default value).  <span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.
</span><br><br>

### References
* https://lists.apache.org/thread/g7jjw0okxjk5y57pbbxy19ydw42kqcos


### Credits
* Mingyu Son (finder)


## Cross-Site Scripting on dashboards ## { #CVE-2022-43717 }

CVE-2022-43717 [\[CVE json\]](./CVE-2022-43717.cve.json) [\[OSV json\]](./CVE-2022-43717.osv.json)



_Last updated: 2023-02-02T10:14:19.691Z_

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

Dashboard rendering does not sufficiently sanitize the content of markdown components leading to possible XSS attack vectors that can be performed by authenticated users with create dashboard permissions.&nbsp;This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.

### References
* https://lists.apache.org/thread/g6zy6vkpvkbj5mj32vmyzwol5ldtg9pl


### Credits
* Vladimir Razov (Positive Technologies) (finder)


## Cross-Site Scripting vulnerability on upload forms ## { #CVE-2022-43718 }

CVE-2022-43718 [\[CVE json\]](./CVE-2022-43718.cve.json) [\[OSV json\]](./CVE-2022-43718.osv.json)



_Last updated: 2023-02-02T10:15:07.131Z_

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

Upload data forms do not correctly render user input leading to possible XSS attack vectors that can be performed by authenticated users with database connection update permissions.&nbsp;<span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.</span><br>

### References
* https://lists.apache.org/thread/8615608jt2x7b3rmqrtngldy8pn3nz2r


### Credits
* Vladimir Razov (Positive Technologies) (finder)


## Cross Site Request Forgery (CSRF) on accept, request access API ## { #CVE-2022-43719 }

CVE-2022-43719 [\[CVE json\]](./CVE-2022-43719.cve.json) [\[OSV json\]](./CVE-2022-43719.osv.json)



_Last updated: 2023-02-02T10:16:06.095Z_

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

Two legacy REST API endpoints for approval and request access are vulnerable to cross site request forgery. <span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.
</span><br><br>

### References
* https://lists.apache.org/thread/xc309h2dphrkg33154djf3nqlh2xc1c0


### Credits
* Vladimir Razov (Positive Technologies) (finder)


## Improper rendering of user input ## { #CVE-2022-43720 }

CVE-2022-43720 [\[CVE json\]](./CVE-2022-43720.cve.json) [\[OSV json\]](./CVE-2022-43720.osv.json)



_Last updated: 2023-02-02T10:16:28.581Z_

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

An authenticated attacker with write CSS template permissions can create a record with specific HTML tags that will not get properly escaped by the toast message displayed when a user deletes that specific CSS template record.&nbsp;<span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.</span><br>

### References
* https://lists.apache.org/thread/jts6x56kghr9mbowb653bk70pl81jp8l


### Credits
* Anton Vaychikauskas (Positive Technologies) (finder)


## Open Redirect Vulnerability ## { #CVE-2022-43721 }

CVE-2022-43721 [\[CVE json\]](./CVE-2022-43721.cve.json) [\[OSV json\]](./CVE-2022-43721.osv.json)



_Last updated: 2023-02-02T10:16:45.887Z_

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

An authenticated attacker with update datasets permission could change a dataset link to an untrusted site, users could be redirected to this site when clicking on that specific dataset.&nbsp;<span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.</span><br>

### References
* https://lists.apache.org/thread/s6sqt5jmcv6qxtvdot1t5tpt57v439kg


### Credits
* Vladimir Razov (Positive Technologies) (finder)


## Possible SSRF on import datasets ## { #CVE-2023-25504 }

CVE-2023-25504 [\[CVE json\]](./CVE-2023-25504.cve.json) [\[OSV json\]](./CVE-2023-25504.osv.json)



_Last updated: 2023-04-17T16:29:38.744Z_

### Affected

* Apache Superset through 2.0.1


### Description

<span style="background-color: rgb(255, 255, 255);">A malicious actor who has been authenticated and granted specific permissions in Apache Superset may use the import dataset feature in order to conduct Server-Side Request Forgery
attacks and query internal resources on behalf of the server where Superset
is deployed. This vulnerability exists&nbsp;</span>in Apache Superset versions up to and including 2.0.1.<br>

### References
* https://lists.apache.org/thread/tdnzkocfsqg2sbbornnp9g492fn4zhtx


### Credits
* Alexey Sabadash, VK (finder)


## Improper data permission validation on Jinja templated queries ## { #CVE-2023-27523 }

CVE-2023-27523 [\[CVE json\]](./CVE-2023-27523.cve.json) [\[OSV json\]](./CVE-2023-27523.osv.json)



_Last updated: 2023-09-06T09:50:25.921Z_

### Affected

* Apache Superset through 2.1.0


### Description

Improper data authorization check on Jinja templated queries in Apache Superset&nbsp;up to and including 2.1.0 allows for an authenticated user to issue queries on database tables they may not have access to.<br><br>

### References
* https://lists.apache.org/thread/3y97nmwm956b6zg3l8dh9oj0w7dj945h


### Credits
* Jingjing Hu (finder)


## Session validation vulnerability when using provided default SECRET_KEY ## { #CVE-2023-27524 }

CVE-2023-27524 [\[CVE json\]](./CVE-2023-27524.cve.json) [\[OSV json\]](./CVE-2023-27524.osv.json)



_Last updated: 2024-04-08T09:07:29.864Z_

### Affected

* Apache Superset through 2.0.1


### Description

Session Validation attacks in Apache Superset versions up to and including 2.0.1. Installations that have not altered the default configured SECRET_KEY according to installation instructions allow for an attacker to authenticate and access unauthorized resources. This does not affect Superset administrators who have changed the default value for SECRET_KEY config.

### References
* https://lists.apache.org/thread/n0ftx60sllf527j7g11kmt24wvof8xyk


### Credits
* Naveen Sunkavally (Horizon3.ai) (finder)


## Incorrect default permissions for Gamma role ## { #CVE-2023-27525 }

CVE-2023-27525 [\[CVE json\]](./CVE-2023-27525.cve.json) [\[OSV json\]](./CVE-2023-27525.osv.json)



_Last updated: 2023-04-17T16:27:58.172Z_

### Affected

* Apache Superset through 2.0.1


### Description

An authenticated user with Gamma role authorization could have access to metadata information using non trivial methods in Apache Superset up to and including 2.0.1<br><br>

### References
* https://lists.apache.org/thread/wpv7b17zjg2pmvpfkdd6nn8sco8y2q77


### Credits
* NTT DATA (finder)


## Improper Authorization check on import charts ## { #CVE-2023-27526 }

CVE-2023-27526 [\[CVE json\]](./CVE-2023-27526.cve.json) [\[OSV json\]](./CVE-2023-27526.osv.json)



_Last updated: 2023-09-06T09:49:27.778Z_

### Affected

* Apache Superset through 2.1.0


### Description

A non Admin authenticated user could incorrectly create resources using the import charts feature, on Apache Superset up to and including 2.1.0.&nbsp;<br>

### References
* https://lists.apache.org/thread/ndww89yl2jd98lvn23n9cj722lfdg8dv


### Credits
* NTT DATA (finder)


## Database connection password leak ## { #CVE-2023-30776 }

CVE-2023-30776 [\[CVE json\]](./CVE-2023-30776.cve.json)

_Last updated: 2023-06-15T07:29:48.154Z_

### Affected

* Apache Superset from 1.3.0 through 2.0.1


### Description

An authenticated user with specific data permissions could access database connections stored passwords by requesting a specific REST API.&nbsp;This issue affects Apache Superset version 1.3.0 up to 2.0.1.

### References
* https://lists.apache.org/thread/s9w9w10mt2sngk3solwnmq5k7md53tsz
* http://www.openwall.com/lists/oss-security/2023/04/24/3


### Credits
* Naveen Sunkavally (Horizon3.ai) (finder) (finder)


## SQL parser edge case bypasses data access authorization ## { #CVE-2023-32672 }

CVE-2023-32672 [\[CVE json\]](./CVE-2023-32672.cve.json) [\[OSV json\]](./CVE-2023-32672.osv.json)



_Last updated: 2023-09-06T13:15:55.981Z_

### Affected

* Apache Superset through 2.1.0


### Description

An Incorrect authorisation check in SQLLab in Apache Superset versions up to and including 2.1.0. This vulnerability allows an authenticated user to query tables that they do not have proper access to within Superset. The vulnerability can be exploited by leveraging a SQL parsing vulnerability.<br><br>

### References
* https://lists.apache.org/thread/ococ6nlj80f0okkwfwpjczy3q84j3wkp


### Credits
* Arnaud Pascal @ Vaadata (finder)


## Improper API permission for low privilege users ## { #CVE-2023-36387 }

CVE-2023-36387 [\[CVE json\]](./CVE-2023-36387.cve.json) [\[OSV json\]](./CVE-2023-36387.osv.json)



_Last updated: 2023-10-17T07:53:17.128Z_

### Affected

* Apache Superset through 2.1.0


### Description

An improper default REST API permission for Gamma users in Apache Superset up to and including 2.1.0 allows for an authenticated Gamma user to test database connections.<br>

### References
* https://lists.apache.org/thread/tt6s6hm8nv6s11z8bfsk3r3d9ov0ogw3
* https://github.com/apache/superset/pull/24185


### Credits
* Miguel Segovia Gil (finder)


## Improper API permission for low privilege users allows for SSRF ## { #CVE-2023-36388 }

CVE-2023-36388 [\[CVE json\]](./CVE-2023-36388.cve.json) [\[OSV json\]](./CVE-2023-36388.osv.json)



_Last updated: 2023-09-06T12:53:55.132Z_

### Affected

* Apache Superset through 2.1.0


### Description

Improper REST API permission in Apache Superset up to and including 2.1.0 allows for an authenticated Gamma users to test network connections, possible SSRF.<br><br>

### References
* https://lists.apache.org/thread/ccmjjz4jp17yc2kcd18qshmdtf7qorfs


### Credits
* https://github.com/vin01 (finder)


## Metadata db write access can lead to remote code execution ## { #CVE-2023-37941 }

CVE-2023-37941 [\[CVE json\]](./CVE-2023-37941.cve.json) [\[OSV json\]](./CVE-2023-37941.osv.json)



_Last updated: 2023-09-29T16:22:05.089Z_

### Affected

* Apache Superset from 1.5.0 through 2.1.0


### Description

<div>If an attacker gains write access to the Apache Superset metadata database, they could persist a specifically crafted Python object that may lead to remote code execution on Superset's web backend.</div><div><br></div><div>The Superset metadata db is an 'internal' component that is typically 
only accessible directly by the system administrator and the superset 
process itself. Gaining access to that database should
 be difficult and require significant privileges.<br></div><div><br></div><div>This vulnerability impacts Apache Superset versions 1.5.0 up to and including 2.1.0. Users are recommended to upgrade to version 2.1.1 or later.<br></div>

### References
* https://lists.apache.org/thread/6qk1zscc06yogxxfgz2bh2bvz6vh9g7h


### Credits
* Dinis Cruz, cruzdinis@ua.pt (finder)
* Naveen Sunkavally (Horizon3.ai) (finder)


## Stack traces enabled by default ## { #CVE-2023-39264 }

CVE-2023-39264 [\[CVE json\]](./CVE-2023-39264.cve.json) [\[OSV json\]](./CVE-2023-39264.osv.json)



_Last updated: 2023-09-06T12:58:57.264Z_

### Affected

* Apache Superset through 2.1.0


### Description

By default, stack traces for errors were enabled, which resulted in the exposure of internal traces on REST API endpoints to users.&nbsp;<span style="background-color: rgb(255, 255, 255);">This vulnerability exists </span>in Apache Superset versions up to and including 2.1.0.

### References
* https://lists.apache.org/thread/y65t1of7hb445n86o1vdzjct7rfwlx75


### Credits
* Miguel Segovia Gil (finder)


## Possible Unauthorized Registration of SQLite Database Connections ## { #CVE-2023-39265 }

CVE-2023-39265 [\[CVE json\]](./CVE-2023-39265.cve.json) [\[OSV json\]](./CVE-2023-39265.osv.json)



_Last updated: 2023-09-06T13:00:09.688Z_

### Affected

* Apache Superset through 2.1.0


### Description

Apache Superset would allow for SQLite database connections to be incorrectly registered when an attacker uses alternative driver names like&nbsp;sqlite+pysqlite or by using database imports. This could allow for unexpected file creation on Superset webservers. Additionally, if Apache Superset is using a SQLite database for its metadata (not advised for production use) it could result in more severe vulnerabilities related to confidentiality and integrity.&nbsp;<span style="background-color: rgb(255, 255, 255);">This vulnerability exists </span>in Apache Superset versions up to and including 2.1.0.

### References
* https://lists.apache.org/thread/pwdzsdmv4g5g1n2h9m7ortfnxmhr7nfy


### Credits
* Naveen Sunkavally (Horizon3.ai) (finder)


## Privilege escalation with default examples database ## { #CVE-2023-40610 }

CVE-2023-40610 [\[CVE json\]](./CVE-2023-40610.cve.json) [\[OSV json\]](./CVE-2023-40610.osv.json)



_Last updated: 2023-11-27T10:22:38.966Z_

### Affected

* Apache Superset before 2.1.2


### Description

Improper authorization check and possible privilege escalation on Apache Superset&nbsp;up to but excluding 2.1.2. Using the default examples database connection that allows access to both the examples schema and Apache Superset's metadata database, an attacker using a specially crafted CTE SQL statement could change data on the metadata database. This weakness could result on tampering with the authentication/authorization data.<br><br>

### References
* https://lists.apache.org/thread/jvgxpk4dbxyqtsgtl4pdgbd520rc0rot


### Credits
* LEXFO for Orange Innovation and Orange CERT-CC  at Orange group (finder)


## Unnecessary read permissions within the Gamma role ## { #CVE-2023-42501 }

CVE-2023-42501 [\[CVE json\]](./CVE-2023-42501.cve.json) [\[OSV json\]](./CVE-2023-42501.osv.json)



_Last updated: 2023-11-27T10:23:45.368Z_

### Affected

* Apache Superset before 2.1.2


### Description

Unnecessary read permissions within the Gamma role would allow authenticated users to read configured CSS templates and annotations.<br>This issue affects Apache Superset: before 2.1.2.<br>Users should upgrade to version or above 2.1.2 and run `superset init` to reconstruct the Gamma role or remove `can_read` permission from the mentioned resources.<br><br>

### References
* https://lists.apache.org/thread/vk1rmrh9kz0chjmc9tk7o3md6zpz4ygh


### Credits
* Miguel Segovia Gil (finder)


## Open Redirect Vulnerability ## { #CVE-2023-42502 }

CVE-2023-42502 [\[CVE json\]](./CVE-2023-42502.cve.json) [\[OSV json\]](./CVE-2023-42502.osv.json)



_Last updated: 2023-11-28T16:25:40.797Z_

### Affected

* Apache Superset before 3.0.0


### Description

An authenticated attacker with update datasets permission could change a dataset link to an untrusted site by spoofing the <span style="background-color: rgb(255, 255, 255);">HTTP Host header</span>, users could be redirected to this site when clicking on that specific dataset. <span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset versions before 3.0.0.</span><br>

### References
* https://lists.apache.org/thread/n8348f194d8o8mln3oxd0s8jdl5bxbmn


### Credits
* Amit Laish – GE Vernova (finder)


## Lack of rate limiting allows for possible denial of service ## { #CVE-2023-42504 }

CVE-2023-42504 [\[CVE json\]](./CVE-2023-42504.cve.json) [\[OSV json\]](./CVE-2023-42504.osv.json)



_Last updated: 2023-11-29T09:18:09.316Z_

### Affected

* Apache Superset before 3.0.0


### Description

<p>An authenticated malicious user could initiate multiple concurrent requests, each requesting multiple dashboard exports, leading to a possible denial of service.</p><p>This issue affects Apache Superset: before 3.0.0</p>

### References
* https://lists.apache.org/thread/yzq5gk1y9lyw6nxwd3xdkxg1djqw1h6l


### Credits
* Amit Laish – GE Vernova (finder)


## Sensitive information disclosure on db connection details ## { #CVE-2023-42505 }

CVE-2023-42505 [\[CVE json\]](./CVE-2023-42505.cve.json) [\[OSV json\]](./CVE-2023-42505.osv.json)



_Last updated: 2023-11-28T16:26:56.352Z_

### Affected

* Apache Superset before 3.0.0


### Description

<p>An authenticated user with read permissions on database connections metadata could potentially access sensitive information such as the connection's username.<br><br></p><p>This issue affects Apache Superset before 3.0.0.<br></p>

### References
* https://lists.apache.org/thread/bd0fhtfzrtgo1q8x35tpm8ms144d1t2y


### Credits
*  Leonel John Erik Angel Torres (finder)


## Stored XSS on API endpoint ## { #CVE-2023-43701 }

CVE-2023-43701 [\[CVE json\]](./CVE-2023-43701.cve.json) [\[OSV json\]](./CVE-2023-43701.osv.json)



_Last updated: 2025-02-06T14:29:43.997Z_

### Affected

* Apache Superset before 2.1.2


### Description

Improper payload validation and an improper REST API response type, made it possible for an authenticated malicious actor to store malicious code into Chart's metadata, this code could get executed if a user specifically accesses a specific deprecated API endpoint.&nbsp;This issue affects Apache Superset versions prior to 2.1.2.&nbsp;<br>Users are recommended to upgrade to version 2.1.2, which fixes this issue.

### References
* https://lists.apache.org/thread/4dnr1knk50fw60jxkjgqj228f0xcc892


### Credits
* Amit Laish – GE Vernova (finder)


## Allows for uncontrolled resource consumption via a ZIP bomb ## { #CVE-2023-46104 }

CVE-2023-46104 [\[CVE json\]](./CVE-2023-46104.cve.json) [\[OSV json\]](./CVE-2023-46104.osv.json)



_Last updated: 2023-12-19T09:30:51.642Z_

### Affected

* Apache Superset before 2.1.3
* Apache Superset from 3.0.0 before 3.0.1


### Description

Uncontrolled resource consumption can be triggered by authenticated attacker that uploads a malicious ZIP to import database, dashboards or datasets.&nbsp;&nbsp;<br><span style="background-color: rgb(255, 255, 255);">This vulnerability exists </span>in Apache Superset versions up to and including 2.1.2 and versions 3.0.0, 3.0.1.<br>

### References
* https://lists.apache.org/thread/yxbxg4wryb7cb7wyybk11l5nqy0rsrvl


### Credits
* Dor Konis – GE Vernova (finder)


## Stored XSS in Dashboard Title and Chart Title ## { #CVE-2023-49657 }

CVE-2023-49657 [\[CVE json\]](./CVE-2023-49657.cve.json) [\[OSV json\]](./CVE-2023-49657.osv.json)



_Last updated: 2024-01-29T08:35:36.887Z_

### Affected

* Apache Superset before 3.0.3


### Description

<span style="background-color: rgb(255, 255, 255);">A stored cross-site scripting (XSS) vulnerability exists in Apache Superset before 3.0.3.&nbsp;</span>An authenticated attacker with create/update permissions on charts or dashboards could store a script or add a specific HTML snippet that would act as a stored XSS.<br><br>For 2.X versions, users should change their config to include:<br><br>TALISMAN_CONFIG = {<br>&nbsp; &nbsp; "content_security_policy": {<br>&nbsp; &nbsp; &nbsp; &nbsp; "base-uri": ["'self'"],<br>&nbsp; &nbsp; &nbsp; &nbsp; "default-src": ["'self'"],<br>&nbsp; &nbsp; &nbsp; &nbsp; "img-src": ["'self'", "blob:", "data:"],<br>&nbsp; &nbsp; &nbsp; &nbsp; "worker-src": ["'self'", "blob:"],<br>&nbsp; &nbsp; &nbsp; &nbsp; "connect-src": [<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "'self'",<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "<a target="_blank" rel="nofollow" href="https://api.mapbox.com&quot;">https://api.mapbox.com"</a>;,<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "<a target="_blank" rel="nofollow" href="https://events.mapbox.com&quot;">https://events.mapbox.com"</a>;,<br>&nbsp; &nbsp; &nbsp; &nbsp; ],<br>&nbsp; &nbsp; &nbsp; &nbsp; "object-src": "'none'",<br>&nbsp; &nbsp; &nbsp; &nbsp; "style-src": [<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "'self'",<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "'unsafe-inline'",<br>&nbsp; &nbsp; &nbsp; &nbsp; ],<br>&nbsp; &nbsp; &nbsp; &nbsp; "script-src": ["'self'", "'strict-dynamic'"],<br>&nbsp; &nbsp; },<br>&nbsp; &nbsp; "content_security_policy_nonce_in": ["script-src"],<br>&nbsp; &nbsp; "force_https": False,<br>&nbsp; &nbsp; "session_cookie_secure": False,<br>}<br><br>

### References
* https://lists.apache.org/thread/wjyvz8om9nwd396lh0bt156mtwjxpsvx


### Credits
* Nick Barnes, Praetorian Security Inc. (reporter)
* Amit Laish – GE Vernova (reporter)


## Privilege Escalation Vulnerability ## { #CVE-2023-49734 }

CVE-2023-49734 [\[CVE json\]](./CVE-2023-49734.cve.json) [\[OSV json\]](./CVE-2023-49734.osv.json)



_Last updated: 2023-12-19T09:52:11.087Z_

### Affected

* Apache Superset before 2.1.2
* Apache Superset from 3.0.0 before 3.0.2


### Description

An authenticated Gamma user has the ability to create a dashboard and add charts to it, this user would automatically become one of the owners of the charts allowing him to incorrectly have write permissions to these charts.<p>This issue affects Apache Superset: before 2.1.2, from 3.0.0 before 3.0.2.</p><p>Users are recommended to upgrade to version 3.0.2 or 2.1.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/985h6ltvtbvdoysso780kkj7x744cds5


### Credits
* Jordan Velich (finder)


## SQL Injection on where_in JINJA macro ## { #CVE-2023-49736 }

CVE-2023-49736 [\[CVE json\]](./CVE-2023-49736.cve.json) [\[OSV json\]](./CVE-2023-49736.osv.json)



_Last updated: 2023-12-19T09:33:08.370Z_

### Affected

* Apache Superset before 2.1.2
* Apache Superset from 3.0.0 before 3.0.2


### Description

A where_in JINJA macro <span style="background-color: rgb(255, 255, 255);">allows users to specify a quote, which combined with a carefully crafted statement&nbsp;would allow for SQL injection&nbsp;</span>in Apache Superset.<p>This issue affects Apache Superset: before 2.1.2, from 3.0.0 before 3.0.2.</p><p>Users are recommended to upgrade to version 3.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/1kf481bgs3451qcz6hfhobs7xvhp8n1p


### Credits
* Jack Prince-Fulls ( jf@incyan.com ) (finder)


## Allows for uncontrolled resource consumption via a ZIP bomb (version range fix for CVE-2023-46104) ## { #CVE-2024-23952 }

CVE-2024-23952 [\[CVE json\]](./CVE-2024-23952.cve.json) [\[OSV json\]](./CVE-2024-23952.osv.json)



_Last updated: 2024-02-14T11:09:45.113Z_

### Affected

* Apache Superset before 2.1.3
* Apache Superset from 3.0.0 before 3.0.2


### Description

This is a duplicate for CVE-2023-46104. With correct CVE version ranges for affected Apache Superset.<br> <br>Uncontrolled resource consumption can be triggered by authenticated attacker that uploads a malicious ZIP to import database, dashboards or datasets. &nbsp;<br><span style="background-color: rgb(255, 255, 255);">This vulnerability exists </span>in Apache Superset versions up to and including 2.1.2 and versions 3.0.0, 3.0.1.<br><br><br>

### References
* https://lists.apache.org/thread/zc58zvm4414molqn2m4d4vkrbrsxdksx


### Credits
* Dor Konis – GE Vernova (finder)


## Improper Neutralisation of custom SQL on embedded context ## { #CVE-2024-24772 }

CVE-2024-24772 [\[CVE json\]](./CVE-2024-24772.cve.json) [\[OSV json\]](./CVE-2024-24772.osv.json)



_Last updated: 2025-02-12T09:26:35.721Z_

### Affected

* Apache Superset before 3.0.4
* Apache Superset from 3.1.0 before 3.1.1


### Description

A guest user could exploit a chart data REST API and send arbitrary SQL statements that on error could leak information from the underlying analytics database.<p><span style="background-color: var(--wht);">This issue affects Apache Superset: before 3.0.4, from 3.1.0 before 3.1.1.</span><br></p><p>Users are recommended to upgrade to version 3.1.1 or 3.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/gfl3ckwy6y9tpz9jmpv62orh2q346sn5


### Credits
* Beto Ferreira De Almeida (remediation developer)
* Linden Haynes (finder)


## Improper validation of SQL statements allows for unauthorized access to data  ## { #CVE-2024-24773 }

CVE-2024-24773 [\[CVE json\]](./CVE-2024-24773.cve.json) [\[OSV json\]](./CVE-2024-24773.osv.json)



_Last updated: 2024-02-28T11:24:56.349Z_

### Affected

* Apache Superset before 3.0.4
* Apache Superset from 3.1.0 before 3.1.1


### Description

Improper parsing of nested SQL statements on SQLLab would allow authenticated users to surpass their data authorization scope.<br><p>This issue affects Apache Superset: before 3.0.4, from 3.1.0 before 3.1.1.</p><p>Users are recommended to upgrade to version 3.1.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/h66fy6nj41cfx07zh7l552w6dmtjh501


### Credits
* Beto Ferreira De Almeida (remediation developer)
* Daniel Vaz Gaspar (coordinator)


## Improper data authorization when creating a new dataset ## { #CVE-2024-24779 }

CVE-2024-24779 [\[CVE json\]](./CVE-2024-24779.cve.json) [\[OSV json\]](./CVE-2024-24779.osv.json)



_Last updated: 2024-02-28T11:28:00.354Z_

### Affected

* Apache Superset before 3.0.4
* Apache Superset from 3.1.0 before 3.1.1


### Description

Apache Superset with custom roles that include `can write on dataset` and without all data access permissions, allows for users to create virtual datasets to data they don't have access to. These users could then use those virtual datasets to get access to unauthorized data.<br><p>This issue affects Apache Superset: before 3.0.4, from 3.1.0 before 3.1.1.</p><p>Users are recommended to upgrade to version 3.1.1 or 3.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/xzhz1m5bb9zxhyqgoy4q2d689b3zp4pq


### Credits
* Daniel Pedro Vaz Gaspar (remediation developer)
* @DLT1412 (finder)


## Improper authorization validation on dashboards and charts import ## { #CVE-2024-26016 }

CVE-2024-26016 [\[CVE json\]](./CVE-2024-26016.cve.json) [\[OSV json\]](./CVE-2024-26016.osv.json)



_Last updated: 2024-02-28T11:28:36.984Z_

### Affected

* Apache Superset before 3.0.4
* Apache Superset from 3.1.0 before 3.1.1


### Description

A low privilege authenticated user <span style="background-color: rgb(255, 255, 255);">could import an existing dashboard or chart that they do not have access to and then modify its metadata, thereby gaining ownership of the object. However, it's important to note that access to the analytical data of these charts and dashboards would still be subject to validation based on data access privileges.</span><br><br><span style="background-color: var(--wht);">This issue affects Apache Superset: before 3.0.4, from 3.1.0 before 3.1.1.</span><p>Users are recommended to upgrade to version 3.1.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/76v1jjcylgk4p3m0258qr359ook3vl8s


### Credits
* Daniel Vaz Gaspar (remediation developer)
* Matt Freyre (finder)


## Improper error handling on alerts ## { #CVE-2024-27315 }

CVE-2024-27315 [\[CVE json\]](./CVE-2024-27315.cve.json) [\[OSV json\]](./CVE-2024-27315.osv.json)



_Last updated: 2024-10-03T12:30:58.178Z_

### Affected

* Apache Superset before 3.0.4
* Apache Superset from 3.1.0 before 3.1.1


### Description

<p>An authenticated user with privileges to create Alerts on Alerts &amp; Reports has the capability to generate a specially crafted SQL statement that triggers an error on the database. This error is not properly handled by Apache Superset and may inadvertently surface in the error log of the Alert exposing possibly sensitive data.<br></p><p>This issue affects Apache Superset: before 3.0.4, from 3.1.0 before 3.1.1.</p><p>Users are recommended to upgrade to version 3.1.1 or 3.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/qcwbx7q2s3ynsd405895bx3wcwq32j7z


### Credits
* Anastasios Stasinopoulos - OBRELA LABS (finder)
* Beto de Almeida (remediation developer)


## Incorrect datasource authorization on explore REST API  ## { #CVE-2024-28148 }

CVE-2024-28148 [\[CVE json\]](./CVE-2024-28148.cve.json) [\[OSV json\]](./CVE-2024-28148.osv.json)



_Last updated: 2024-05-08T08:31:47.011Z_

### Affected

* Apache Superset before 3.1.2


### Description

<span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">An authenticated user could potentially access metadata for a datasource they are not authorized to view by submitting a targeted REST API request.</span></span><p>This issue affects Apache Superset: before 3.1.2.</p><p>Users are recommended to upgrade to version 3.1.2 or above, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/n27wlbd05oc6bgjh28d5pxzsrrph8dgo


### Credits
* Daniel Pedro Vaz Gaspar (remediation developer)
* Krishna Nadh (finder)


## Server arbitrary file read ## { #CVE-2024-34693 }

CVE-2024-34693 [\[CVE json\]](./CVE-2024-34693.cve.json) [\[OSV json\]](./CVE-2024-34693.osv.json)



_Last updated: 2024-06-20T08:51:53.358Z_

### Affected

* Apache Superset before 3.1.3
* Apache Superset from 4.0.0 before 4.0.1


### Description

Improper Input Validation vulnerability in Apache Superset, allows for an authenticated attacker to create a MariaDB connection with local_infile enabled. If both the MariaDB server (off by default) and the local mysql client on the web server are set to allow for local infile, it's possible for the attacker to execute a specific MySQL/MariaDB SQL command that is able to read files from the server and insert their content on a MariaDB database table.<p>This issue affects Apache Superset: before 3.1.3 and version 4.0.0</p><p>Users are recommended to upgrade to version 4.0.1 or 3.1.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/1803x1s34m7r71h1k0q1njol8k6fmyon


### Credits
* Matei "Mal" Badanoiu (finder)
* Daniel Vaz Gaspar (remediation developer)


## Improper SQL authorisation, parse not checking for specific engine functions ## { #CVE-2024-39887 }

CVE-2024-39887 [\[CVE json\]](./CVE-2024-39887.cve.json) [\[OSV json\]](./CVE-2024-39887.osv.json)



_Last updated: 2024-07-16T09:20:08.872Z_

### Affected

* Apache Superset before 4.0.2


### Description

<p>An SQL Injection vulnerability in Apache Superset exists due to improper neutralization of special elements used in SQL commands. Specifically, certain engine-specific functions are not checked, which allows attackers to bypass Apache Superset's SQL authorization. To mitigate this, a new configuration key named <code>DISALLOWED_SQL_FUNCTIONS</code> has been introduced. This key disallows the use of the following PostgreSQL functions: <code>version</code>, <code>query_to_xml</code>, <code>inet_server_addr</code>, and <code>inet_client_addr</code>. Additional functions can be added to this list for increased protection.</p><p>This issue affects Apache Superset: before 4.0.2.</p><p>Users are recommended to upgrade to version 4.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/j55vm41jg3l0x6w49zrmvbf3k0ts5fqz


### Credits
* Mike Yushkovskiy (finder)
* Daniel Vaz Gaspar (remediation developer)


## Improper SQL authorisation, parse not checking for specific postgres functions ## { #CVE-2024-53947 }

CVE-2024-53947 [\[CVE json\]](./CVE-2024-53947.cve.json) [\[OSV json\]](./CVE-2024-53947.osv.json)



_Last updated: 2024-12-09T13:35:08.136Z_

### Affected

* Apache Superset before 4.1.0


### Description

<p>Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Superset. Specifically, certain engine-specific functions are not checked, which allows attackers to bypass Apache Superset's SQL authorization. This issue is a follow-up to&nbsp;CVE-2024-39887 with additional disallowed PostgreSQL functions now included:&nbsp;query_to_xml_and_xmlschema,&nbsp;table_to_xml,&nbsp;table_to_xml_and_xmlschema.</p><p>This issue affects Apache Superset: &lt;4.1.0.</p><p>Users are recommended to upgrade to version 4.1.0, which fixes the issue or add these Postgres functions to the config set&nbsp;DISALLOWED_SQL_FUNCTIONS.</p>

### References
* https://lists.apache.org/thread/hj3gfsjh67vqw12nlrshlsym4bkopjmn


### Credits
* Iván Arce (Quarkslab) (reporter)
* Daniel Gaspar (remediation developer)
* Mathieu Farrell (Quarkslab) (finder)


## Error verbosity exposes metadata in analytics databases ## { #CVE-2024-53948 }

CVE-2024-53948 [\[CVE json\]](./CVE-2024-53948.cve.json) [\[OSV json\]](./CVE-2024-53948.osv.json)



_Last updated: 2024-12-09T13:35:29.219Z_

### Affected

* Apache Superset before 4.1.0


### Description

<p>Generation of Error Message Containing analytics metadata Information in Apache Superset.</p><p>This issue affects Apache Superset: before 4.1.0.</p><p>Users are recommended to upgrade to version 4.1.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/8howpf3png0wrgpls46ggk441oczlfvf


### Credits
* Bartosz Galaszewski (reporter)
* Daniel Gaspar (remediation developer)


## Lower privilege users are able to create Role when FAB_ADD_SECURITY_API is enabled ## { #CVE-2024-53949 }

CVE-2024-53949 [\[CVE json\]](./CVE-2024-53949.cve.json) [\[OSV json\]](./CVE-2024-53949.osv.json)



_Last updated: 2025-02-12T09:34:35.897Z_

### Affected

* Apache Superset from 2.0.0 before 4.1.0


### Description

<p>Improper Authorization vulnerability in Apache Superset when&nbsp;<span style="background-color: rgb(255, 255, 255);">FAB_ADD_SECURITY_API is enabled (disabled by default). Allows for lower privilege users to use this API.</span></p><p>&nbsp;issue affects Apache Superset: from 2.0.0 before 4.1.0.</p><p>Users are recommended to upgrade to version 4.1.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/d3scbwmfpzbpm6npnzdw5y4owtqqyq8d


### Credits
* Jonathan Zimmerman (reporter)
* Hugh Miles (remediation developer)


## SQLLab Improper readonly query validation allows unauthorized write access ## { #CVE-2024-55633 }

CVE-2024-55633 [\[CVE json\]](./CVE-2024-55633.cve.json) [\[OSV json\]](./CVE-2024-55633.osv.json)



_Last updated: 2025-02-12T09:35:41.246Z_

### Affected

* Apache Superset before 4.1.0


### Description

<p>Improper Authorization vulnerability in Apache Superset. On Postgres analytic databases an attacker with SQLLab access can&nbsp;craft a specially designed SQL DML statement<span style="background-color: rgb(255, 255, 255);">&nbsp;that is Incorrectly identified as a read-only query, enabling its execution. Non postgres analytics database connections and postgres analytics database connections set with a readonly user (advised) are not vulnerable.&nbsp;</span></p><p>This issue affects Apache Superset: before 4.1.0.</p><p>Users are recommended to upgrade to version 4.1.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/bwmd17fcvljt9q4cgctp4v09zh3qs7fb


### Credits
* Beto de Almeida (remediation developer)
* Daniel Gaspar (coordinator)
* James Ford (Striveworks) (finder)
