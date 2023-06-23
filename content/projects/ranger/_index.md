---
title: Apache Ranger security advisories
description: Security information for Apache Ranger
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Ranger? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Ranger since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## code execution vulnerability in policy expressions ## { #CVE-2022-45048 }

[CVE-2022-45048](./CVE-2022-45048.cve.json)

### Affected

* Apache Ranger versions 2.3.0


### Description

<p>Authenticated users with appropriate privileges can create policies having expressions that can exploit code execution vulnerability.&nbsp;This issue affects Apache Ranger: 2.3.0. Users are recommended to update to version 2.4.0.<br></p>

## Permissions problem in the Apache Ranger Hive Plugin ## { #CVE-2021-40331 }

[CVE-2021-40331](./CVE-2021-40331.cve.json)

### Affected

* Apache Ranger Hive Plugin versions 2.0.0 including 2.3.0


### Description

An Incorrect Permission Assignment for Critical Resource vulnerability was found in the Apache Ranger Hive Plugin. Any user with SELECT privilege on a database can alter the ownership of the table in Hive when Apache Ranger Hive Plugin is enabled<br><p>This issue affects Apache Ranger Hive Plugin: from 2.0.0 through 2.3.0. Users are recommended to upgrade to version 2.4.0 or later.<br></p>