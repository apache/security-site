---
title: Apache Ranger security advisories
description: Security information for Apache Ranger
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Ranger? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## code execution vulnerability in policy expressions ## { #CVE-2022-45048 }

CVE-2022-45048 [\[CVE json\]](./CVE-2022-45048.cve.json)

### Affected

* Apache Ranger at 2.3.0


### Description

<p>Authenticated users with appropriate privileges can create policies having expressions that can exploit code execution vulnerability.&nbsp;This issue affects Apache Ranger: 2.3.0. Users are recommended to update to version 2.4.0.<br></p>

### References
* https://lists.apache.org/thread/6rpzwy1smdhr60tsh1ydknn3kdm45bb6


### Credits
* g1831767442@163.com (finder)


## Permissions problem in the Apache Ranger Hive Plugin ## { #CVE-2021-40331 }

CVE-2021-40331 [\[CVE json\]](./CVE-2021-40331.cve.json)

### Affected

* Apache Ranger Hive Plugin from 2.0.0 through 2.3.0


### Description

An Incorrect Permission Assignment for Critical Resource vulnerability was found in the Apache Ranger Hive Plugin. Any user with SELECT privilege on a database can alter the ownership of the table in Hive when Apache Ranger Hive Plugin is enabled<br><p>This issue affects Apache Ranger Hive Plugin: from 2.0.0 through 2.3.0. Users are recommended to upgrade to version 2.4.0 or later.<br></p>

### References
* https://lists.apache.org/thread/s68yls6cnkdmzn1k4hqt50vs6wjvt2rn
