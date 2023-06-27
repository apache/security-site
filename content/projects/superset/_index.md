---
title: Apache Superset security advisories
description: Security information for Apache Superset
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Superset? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Dashboard metadata information leak ## { #CVE-2022-45438 }

CVE-2022-45438 [\[CVE json\]](./CVE-2022-45438.cve.json)

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

When explicitly enabling the feature flag DASHBOARD_CACHE (disabled by default), the system allowed for an unauthenticated user to access dashboard configuration metadata using a REST API Get endpoint.&nbsp;<span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.</span><br>

### References
* https://lists.apache.org/thread/snxbkf2x9kww7s0wkmydct9nhqqn9rv9


## SQL injection vulnerability in adhoc clauses ## { #CVE-2022-41703 }

CVE-2022-41703 [\[CVE json\]](./CVE-2022-41703.cve.json)

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

A vulnerability in the SQL Alchemy connector of Apache Superset allows an authenticated user with read access to a specific database to add subqueries to the WHERE and HAVING fields referencing tables on the same database that the user should not have access to, despite the user having the feature flag "ALLOW_ADHOC_SUBQUERY" disabled (default value).  <span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.
</span><br><br>

### References
* https://lists.apache.org/thread/g7jjw0okxjk5y57pbbxy19ydw42kqcos


## Cross-Site Scripting on dashboards ## { #CVE-2022-43717 }

CVE-2022-43717 [\[CVE json\]](./CVE-2022-43717.cve.json)

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

Dashboard rendering does not sufficiently sanitize the content of markdown components leading to possible XSS attack vectors that can be performed by authenticated users with create dashboard permissions.&nbsp;This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.

### References
* https://lists.apache.org/thread/g6zy6vkpvkbj5mj32vmyzwol5ldtg9pl


## Cross-Site Scripting vulnerability on upload forms ## { #CVE-2022-43718 }

CVE-2022-43718 [\[CVE json\]](./CVE-2022-43718.cve.json)

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

Upload data forms do not correctly render user input leading to possible XSS attack vectors that can be performed by authenticated users with database connection update permissions.&nbsp;<span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.</span><br>

### References
* https://lists.apache.org/thread/8615608jt2x7b3rmqrtngldy8pn3nz2r


## Cross Site Request Forgery (CSRF) on accept, request access API ## { #CVE-2022-43719 }

CVE-2022-43719 [\[CVE json\]](./CVE-2022-43719.cve.json)

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

Two legacy REST API endpoints for approval and request access are vulnerable to cross site request forgery. <span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.
</span><br><br>

### References
* https://lists.apache.org/thread/xc309h2dphrkg33154djf3nqlh2xc1c0


## Improper rendering of user input ## { #CVE-2022-43720 }

CVE-2022-43720 [\[CVE json\]](./CVE-2022-43720.cve.json)

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

An authenticated attacker with write CSS template permissions can create a record with specific HTML tags that will not get properly escaped by the toast message displayed when a user deletes that specific CSS template record.&nbsp;<span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.</span><br>

### References
* https://lists.apache.org/thread/jts6x56kghr9mbowb653bk70pl81jp8l


## Open Redirect Vulnerability ## { #CVE-2022-43721 }

CVE-2022-43721 [\[CVE json\]](./CVE-2022-43721.cve.json)

### Affected

* Apache Superset from 2.0.0 before 2.0.1
* Apache Superset through 1.5.2


### Description

An authenticated attacker with update datasets permission could change a dataset link to an untrusted site, users could be redirected to this site when clicking on that specific dataset.&nbsp;<span style="background-color: rgb(255, 255, 255);">This issue affects Apache Superset version 1.5.2 and prior versions and version 2.0.0.</span><br>

### References
* https://lists.apache.org/thread/s6sqt5jmcv6qxtvdot1t5tpt57v439kg


## Possible SSRF on import datasets ## { #CVE-2023-25504 }

CVE-2023-25504 [\[CVE json\]](./CVE-2023-25504.cve.json)

### Affected

* Apache Superset through 2.0.1


### Description

<span style="background-color: rgb(255, 255, 255);">A malicious actor who has been authenticated and granted specific permissions in Apache Superset may use the import dataset feature in order to conduct Server-Side Request Forgery
attacks and query internal resources on behalf of the server where Superset
is deployed. This vulnerability exists&nbsp;</span>in Apache Superset versions up to and including 2.0.1.<br>

### References
* https://lists.apache.org/thread/tdnzkocfsqg2sbbornnp9g492fn4zhtx


## Session validation vulnerability when using provided default SECRET_KEY ## { #CVE-2023-27524 }

CVE-2023-27524 [\[CVE json\]](./CVE-2023-27524.cve.json)

### Affected

* Apache Superset through 2.0.1


### Description

Session Validation attacks in Apache Superset versions up to and including 2.0.1. Installations that have not altered the default configured SECRET_KEY according to installation instructions allow for an attacker to authenticate and access unauthorized resources. This does not affect Superset administrators who have changed the default value for SECRET_KEY config.

### References
* https://lists.apache.org/thread/n0ftx60sllf527j7g11kmt24wvof8xyk


## Incorrect default permissions for Gamma role ## { #CVE-2023-27525 }

CVE-2023-27525 [\[CVE json\]](./CVE-2023-27525.cve.json)

### Affected

* Apache Superset through 2.0.1


### Description

An authenticated user with Gamma role authorization could have access to metadata information using non trivial methods in Apache Superset up to and including 2.0.1<br><br>

### References
* https://lists.apache.org/thread/wpv7b17zjg2pmvpfkdd6nn8sco8y2q77


## Database connection password leak ## { #CVE-2023-30776 }

CVE-2023-30776 [\[CVE json\]](./CVE-2023-30776.cve.json)

### Affected

* Apache Superset from 1.3.0 through 2.0.1


### Description

An authenticated user with specific data permissions could access database connections stored passwords by requesting a specific REST API.&nbsp;This issue affects Apache Superset version 1.3.0 up to 2.0.1.

### References
* https://lists.apache.org/thread/s9w9w10mt2sngk3solwnmq5k7md53tsz
