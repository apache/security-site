---
title: Apache POI security advisories
description: Security information for Apache POI
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache POI? You can read more about the projects' security policy on their [security page](https://poi.apache.org/security.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://poi.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## parsing OOXML based files (xlsx, docx, etc.), poi-ooxml could read unexpected data if underlying zip has duplicate zip entry names ## { #CVE-2025-31672 }

CVE-2025-31672 [\[CVE json\]](./CVE-2025-31672.cve.json) [\[OSV json\]](./CVE-2025-31672.osv.json)



_Last updated: 2025-04-09T11:59:31.807Z_

### Affected

* Apache POI before 5.4.0


### Description

Improper Input Validation vulnerability in Apache POI. The issue affects the parsing of OOXML format files like xlsx, docx and pptx. These file formats are basically zip files and it is possible for malicious users to add zip entries with duplicate names (including the path) in the zip. In this case, products reading the affected file could read different data because 1 of the zip entries with the duplicate name is selected over another but different products may choose a different zip entry.<br>This issue affects Apache POI poi-ooxml before 5.4.0. poi-ooxml 5.4.0 has a check that throws an exception if zip entries with duplicate file names are found in the input file.<br>Users are recommended to upgrade to version poi-ooxml 5.4.0, which fixes the issue. Please read <a target="_blank" rel="nofollow" href="https://poi.apache.org/security.html">https://poi.apache.org/security.html</a> for recommendations about how to use the POI libraries securely.

### References
* https://bz.apache.org/bugzilla/show_bug.cgi?id=69620
* https://lists.apache.org/thread/k14w8vcjqy4h34hh5kzldko78kpylkq5


## A carefully crafted TNEF file can cause an out of memory exception ## { #CVE-2022-26336 }

CVE-2022-26336 [\[CVE json\]](./CVE-2022-26336.cve.json) [\[OSV json\]](./CVE-2022-26336.osv.json)



_Last updated: 2022-03-04T15:58:59.057Z_

### Affected

* poi-scratchpad from unspecified through 5.2.0


### Description

A shortcoming in the HMEF package of poi-scratchpad (Apache POI) allows an attacker to cause an Out of Memory exception. This package is used to read TNEF files (Microsoft Outlook and Microsoft Exchange Server). If an application uses poi-scratchpad to parse TNEF files and the application allows untrusted users to supply them, then a carefully crafted file can cause an Out of Memory exception. This issue affects poi-scratchpad version 5.2.0 and prior versions. Users are recommended to upgrade to poi-scratchpad 5.2.1.

### References
* https://lists.apache.org/thread/sprg0kq986pc2271dc3v2oxb1f9qx09j


### Credits
* Apache POI would like to thank Craig Haft of Yahoo Inc. for reporting and providing a patch for this issue.


## XMLBeans XML Entity Expansion ## { #CVE-2021-23926 }

CVE-2021-23926 [\[CVE json\]](./CVE-2021-23926.cve.json) [\[OSV json\]](./CVE-2021-23926.osv.json)



_Last updated: 2021-01-14T14:45:47.410Z_

### Affected

* Apache XMLBeans from Apache XMLBeans through 2.6.0


### Description

The XML parsers used by XMLBeans up to version 2.6.0 did not set the properties needed to protect the user from malicious XML input. Vulnerabilities include possibilities for XML Entity Expansion attacks.
Affects XMLBeans up to and including v2.6.0.

### References
* https://poi.apache.org/
* https://issues.apache.org/jira/browse/XMLBEANS-517
