---
title: Apache Any23 security advisories
description: Security information for Apache Any23
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Any23? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Possible excessive allocation of resources reading input. ## { #CVE-2023-34150 }

CVE-2023-34150 [\[CVE json\]](./CVE-2023-34150.cve.json) [\[OSV json\]](./CVE-2023-34150.osv.json)



_Last updated: 2023-07-14T08:51:32.515Z_

### Affected

* Apache Any23 through 2.7


### Description

<span style="background-color: rgb(255, 255, 255);">** UNSUPPORTED WHEN ASSIGNED **&nbsp;</span>Use of TikaEncodingDetector in Apache Any23 can cause excessive memory usage.

### References
* https://lists.apache.org/thread/713tk23khbtbg940pb2ql8ggd4cvh6j1


### Credits
* Liran Mendelovich (finder)


## An XML external entity (XXE) injection vulnerability exists in the Apache Any23 RDFa XSLTStylesheet extractor ## { #CVE-2022-25312 }

CVE-2022-25312 [\[CVE json\]](./CVE-2022-25312.cve.json) [\[OSV json\]](./CVE-2022-25312.osv.json)



_Last updated: 2022-03-04T23:18:57.830Z_

### Affected

* Apache Any23 from Apache Any23 2.6 through 2.6


### Description

An XML external entity (XXE) injection vulnerability was discovered in the Any23 RDFa XSLTStylesheet extractor and is known to affect Any23 versions < 2.7. XML external entity injection (also known as XXE) is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data. It often allows an attacker to view files on the application server filesystem, and to interact with any back-end or external systems that the application itself can access. This issue is fixed in Apache Any23 2.7.

### References
* https://lists.apache.org/thread/y6cm5n3ksohsrhzqknqhzy7p3mtkyk23


### Credits
* The Apache Any23 Project Management Committee would like to thank Lion Tree a.k.a liontree0110 for reporting this issue.


## A Remote Code Execution (RCE) vulnerability exists in Apache Any23 YAMLExtractor.java ## { #CVE-2021-40146 }

CVE-2021-40146 [\[CVE json\]](./CVE-2021-40146.cve.json) [\[OSV json\]](./CVE-2021-40146.osv.json)



_Last updated: 2021-09-11T10:59:07.858Z_

### Affected

* Apache Any23 from Apache Any23 before 2.5


### Description

A Remote Code Execution (RCE) vulnerability was discovered in the Any23 YAMLExtractor.java file and is known to affect Any23 versions < 2.5. RCE vulnerabilities allow a malicious actor to execute any code of their choice on a remote machine over LAN, WAN, or internet. RCE belongs to the broader class of arbitrary code execution (ACE) vulnerabilities.

### References
* https://lists.apache.org/thread.html/r7c521ed85c7ae1bad4fdf95b459f2aaa8a67eae338636b7b7ec35d86%40%3Cannounce.apache.org%3E


### Credits
* The Apache Any23 Project Management Committee would like to thank Zhuxuan Wu for reporting the security vulnerability.


## An XML external entity (XXE) injection vulnerability exists in Apache Any23 StreamUtils.java ## { #CVE-2021-38555 }

CVE-2021-38555 [\[CVE json\]](./CVE-2021-38555.cve.json) [\[OSV json\]](./CVE-2021-38555.osv.json)



_Last updated: 2021-09-11T10:55:48.141Z_

### Affected

* Apache Any23 from Apache Any23 before 2.5


### Description

An XML external entity (XXE) injection vulnerability was discovered in the Any23 StreamUtils.java file and is known to affect Any23 versions < 2.5. XML external entity injection (also known as XXE) is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data. It often allows an attacker to view files on the application server filesystem, and to interact with any back-end or external systems that the application itself can access.

### References
* https://lists.apache.org/thread.html/r589d1a9f94dbeee7a0f5dbe8513a0e300dfe669bd964ba2fbfe28e07%40%3Cannounce.apache.org%3E


### Credits
* The Apache Any23 Project Management Committee would like to thank Zhuxuan Wu for reporting the security vulnerability.
