---
title: Apache Tika security advisories
description: Security information for Apache Tika
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Tika? You can read more about the projects' security policy on their [security page](https://tika.apache.org/security-model.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://tika.apache.org/security-model.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Infinite loop in Apache Tika's MP3 parser ## { #CVE-2021-28657 }

CVE-2021-28657 [\[CVE json\]](./CVE-2021-28657.cve.json) [\[OSV json\]](./CVE-2021-28657.osv.json)



_Last updated: 2021-03-31T07:34:07.284Z_

### Affected

* Apache Tika from Apache Tika before 1.26


### Description

A carefully crafted or corrupt file may trigger an infinite loop in Tika's MP3Parser up to and including Tika 1.25. Apache Tika users should upgrade to 1.26 or later.

### References
* https://lists.apache.org/thread.html/r915add4aa52c60d1b5cf085039cfa73a98d7fae9673374dfd7744b5a%40%3Cdev.tika.apache.org%3E


### Credits
* Apache Tika would like to thank Khaled Nassar for reporting this issue.


## Apache Tika BPGParser Memory Usage DoS ## { #CVE-2022-25169 }

CVE-2022-25169 [\[CVE json\]](./CVE-2022-25169.cve.json) [\[OSV json\]](./CVE-2022-25169.osv.json)



_Last updated: 2022-05-16T16:59:35.802Z_

### Affected

* Apache Tika from Apache Tika through 1.28.1


### Description

The BPG parser in versions of Apache Tika before 1.28.2 and 2.4.0 may allocate an unreasonable amount of memory on carefully crafted files.


### References
* https://lists.apache.org/thread/t3tb51sf0k2pmbnzsrrrm23z9r1c10rk


## Apache Tika Regular Expression Denial of Service in Standards Extractor ## { #CVE-2022-30126 }

CVE-2022-30126 [\[CVE json\]](./CVE-2022-30126.cve.json) [\[OSV json\]](./CVE-2022-30126.osv.json)



_Last updated: 2022-05-16T16:58:52.830Z_

### Affected

* Apache Tika from Apache Tika through 1.28.1


### Description

In Apache Tika, a regular expression in our StandardsText class, used by the StandardsExtractingContentHandler could lead to a denial of service caused by backtracking on a specially crafted file. This only affects users who are running the StandardsExtractingContentHandler, which is a non-standard handler.  This is fixed in 1.28.2 and 2.4.0

### References
* https://lists.apache.org/thread/dh3syg68nxogbmlg13srd6gjn3h2z6r4


### Credits
* This issue was discovered and reported by the CodeQL team members [@atorralba (Tony Torralba)](https://github.com/atorralba) and [@joefarebrother (Joseph Farebrother)](https://github.com/joefarebrother).


## Missing fix for CVE-2022-30126 in 1.28.2 ## { #CVE-2022-30973 }

CVE-2022-30973 [\[CVE json\]](./CVE-2022-30973.cve.json) [\[OSV json\]](./CVE-2022-30973.osv.json)



_Last updated: 2022-05-31T13:14:46.730Z_

### Affected

* Apache Tika from Apache Tika through 1.28.2


### Description

We failed to apply the fix for CVE-2022-30126 to the 1.x branch in the 1.28.2 release.  In Apache Tika, a regular expression in the StandardsText class, used by the StandardsExtractingContentHandler could lead to a denial of service caused by backtracking on a specially crafted file. This only affects users who are running the StandardsExtractingContentHandler, which is a non-standard handler.  This is fixed in 1.28.3.

### References
* https://lists.apache.org/thread/gqvb5t4p7tmdpl0y5bdbf72pgxj04h7p


### Credits
* This issue was reported by Cathy Hu, SUSE Software Solutions Germany GmbH.


## Incomplete fix and new regex DoS in StandardsExtractingContentHandler ## { #CVE-2022-33879 }

CVE-2022-33879 [\[CVE json\]](./CVE-2022-33879.cve.json) [\[OSV json\]](./CVE-2022-33879.osv.json)



_Last updated: 2022-06-27T21:35:12.489Z_

### Affected

* Apache Tika from Apache Tika before 2.4.1


### Description

The initial fixes in CVE-2022-30126 and CVE-2022-30973 for regexes in the StandardsExtractingContentHandler were insufficient, and we found a separate, new regex DoS in a different regex in the StandardsExtractingContentHandler. These are now fixed in 1.28.4 and 2.4.1.

### References
* https://lists.apache.org/thread/wfno8mf5nlcvbs78z93q9thgrm30wwfh


### Credits
* This incomplete fix was discovered and reported by the CodeQL team member [@atorralba (Tony Torralba)](https://github.com/atorralba) and [@jarlob (Jaroslav Lobačevski)](https://github.com/jarlob) from Github Security Lab.  The new ReDos was discovered by the Apache Tika team.


## XXE vulnerability in PDFParser's handling of XFA ## { #CVE-2025-54988 }

CVE-2025-54988 [\[CVE json\]](./CVE-2025-54988.cve.json) [\[OSV json\]](./CVE-2025-54988.osv.json)



_Last updated: 2025-08-20T20:08:47.852Z_

### Affected

* Apache Tika PDF parser module from 1.13 through 3.2.1


### Description

Critical XXE in Apache Tika (tika-parser-pdf-module) in Apache Tika 1.13 through and including 3.2.1 on all platforms allows an attacker to carry out XML External Entity injection via a crafted XFA file inside of a PDF. An attacker may be able to read sensitive data or trigger malicious requests to internal resources or third-party servers. Note that the tika-parser-pdf-module is used as a dependency in several Tika packages including at least: tika-parsers-standard-modules, tika-parsers-standard-package, tika-app, tika-grpc and tika-server-standard.<br><br>Users are recommended to upgrade to version 3.2.2, which fixes this issue.

### References
* https://lists.apache.org/thread/8xn3rqy6kz5b3l1t83kcofkw0w4mmj1w


### Credits
* Paras Jain and Yakov Shafranovich of Amazon. (reporter)
