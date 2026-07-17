---
title: Apache SeaTunnel security advisories
description: Security information for Apache SeaTunnel
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache SeaTunnel? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=%5BFINDING%5D%20Apache%20SeaTunnel).

You can read more about the security policy on:

- [Apache SeaTunnel security model](https://seatunnel.apache.org/security)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unauthenticated insecure access ## { #CVE-2025-32896 }

CVE-2025-32896 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-32896) [\[CVE json\]](./CVE-2025-32896.cve.json) [\[OSV json\]](./CVE-2025-32896.osv.json)



_Last updated: 2025-06-19T08:34:42.552Z_

### Affected

* Apache SeaTunnel from 2.3.1 through 2.3.10


### Description

# Summary<br><br>Unauthorized users can perform Arbitrary File Read and Deserialization<br>attack by submit job using restful api-v1.<br><br># Details<br>Unauthorized users can access `/hazelcast/rest/maps/submit-job` to submit<br>job.<br>An attacker can set extra params in mysql url to perform Arbitrary File<br>Read and Deserialization attack.<br><br>This issue affects Apache SeaTunnel: &lt;=2.3.10<br><br># Fixed<br><br>Users are recommended to upgrade to version 2.3.11, and enable restful api-v2 &amp; open https two-way authentication , which fixes the issue.

### References
* https://lists.apache.org/thread/qvh3zyt1jr25rgvw955rb8qjrnbxfro9
* https://github.com/apache/seatunnel/pull/9010


### Credits
* Owen Amadeus (reporter)
* liyiwei (reporter)


## Arbitrary file read vulnerability ## { #CVE-2023-49198 }

CVE-2023-49198 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49198) [\[CVE json\]](./CVE-2023-49198.cve.json) [\[OSV json\]](./CVE-2023-49198.osv.json)



_Last updated: 2024-08-21T09:37:50.824Z_

### Affected

* Apache SeaTunnel Web at 1.0.0


### Description

Mysql security vulnerability in Apache SeaTunnel.<br><br><tt><span style="background-color: rgb(255, 255, 255);">Attackers can read files on the MySQL server by modifying the information in the MySQL URL<br><br> allowLoadLocalInfile=true&amp;allowUrlInLocalInfile=true&amp;allowLoadLocalInfileInPath=/&amp;maxAllowedPacket=655360</span></tt><br><p>This issue affects Apache SeaTunnel: 1.0.0.</p><p>Users are recommended to upgrade to version [1.0.1], which fixes the issue.</p>

### References
* https://lists.apache.org/thread/48j9f1nsn037mgzc4j9o51nwglb1s08h


### Credits
* jiahua huang (reporter)


## Authentication bypass ## { #CVE-2023-48396 }

CVE-2023-48396 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-48396) [\[CVE json\]](./CVE-2023-48396.cve.json) [\[OSV json\]](./CVE-2023-48396.osv.json)



_Last updated: 2024-07-30T08:15:30.810Z_

### Affected

* Apache SeaTunnel Web at 1.0.0


### Description

Web Authentication vulnerability in Apache SeaTunnel.&nbsp;<span style="background-color: rgb(255, 255, 255);">Since the jwt key is hardcoded in the application, an attacker can forge
any token to log in any user.<br><br></span>Attacker can get&nbsp;<span style="background-color: rgb(255, 255, 255);">secret key in&nbsp;<span style="background-color: rgb(255, 255, 255);">/seatunnel-server/seatunnel-app/src/main/resources/application.yml and then create a token.</span></span><br><p>This issue affects Apache SeaTunnel: 1.0.0.</p><p>Users are recommended to upgrade to version 1.0.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/1tdxfjksx0vb9gtyt77wlr6rdcy1qwmw


### Credits
* jiahua huang / Joyh (reporter)
