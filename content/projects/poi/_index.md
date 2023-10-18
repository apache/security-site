---
title: Apache POI security advisories
description: Security information for Apache POI
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache POI? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## XMLBeans XML Entity Expansion ## { #CVE-2021-23926 }

CVE-2021-23926 [\[CVE json\]](./CVE-2021-23926.cve.json)

### Affected

* Apache XMLBeans from Apache XMLBeans through 2.6.0


### Description

The XML parsers used by XMLBeans up to version 2.6.0 did not set the properties needed to protect the user from malicious XML input. Vulnerabilities include possibilities for XML Entity Expansion attacks.
Affects XMLBeans up to and including v2.6.0.

### References
* https://poi.apache.org/
* https://issues.apache.org/jira/browse/XMLBEANS-517


## A carefully crafted TNEF file can cause an out of memory exception ## { #CVE-2022-26336 }

CVE-2022-26336 [\[CVE json\]](./CVE-2022-26336.cve.json)

### Affected

* poi-scratchpad from unspecified through 5.2.0


### Description

A shortcoming in the HMEF package of poi-scratchpad (Apache POI) allows an attacker to cause an Out of Memory exception. This package is used to read TNEF files (Microsoft Outlook and Microsoft Exchange Server). If an application uses poi-scratchpad to parse TNEF files and the application allows untrusted users to supply them, then a carefully crafted file can cause an Out of Memory exception. This issue affects poi-scratchpad version 5.2.0 and prior versions. Users are recommended to upgrade to poi-scratchpad 5.2.1.

### References
* https://lists.apache.org/thread/sprg0kq986pc2271dc3v2oxb1f9qx09j


### Credits
* Apache POI would like to thank Craig Haft of Yahoo Inc. for reporting and providing a patch for this issue.
