---
title: Apache PDFBox security advisories
description: Security information for Apache PDFBox
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache PDFBox? You can read more about the projects' security policy on their [security page](https://pdfbox.apache.org/security.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://pdfbox.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Path Traversal in PDFBox ExtractEmbeddedFiles Example Code ## { #CVE-2026-23907 }

CVE-2026-23907 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-23907) [\[CVE json\]](./CVE-2026-23907.cve.json)

_Last updated: 2026-03-10T16:53:49.159Z_

### Affected

* Apache PDFBox Examples from 2.0.24 through 2.0.35
* Apache PDFBox Examples from 3.0.0 through 3.0.6


### Description

<p>This issue affects the 
ExtractEmbeddedFiles example in&nbsp;Apache PDFBox: from 2.0.24 through 2.0.35, from 3.0.0 through 3.0.6.</p><p>
The ExtractEmbeddedFiles example contains a path traversal vulnerability (CWE-22) because 
the filename that is obtained from 
PDComplexFileSpecification.getFilename() is appended to the extraction path.
<br>Users who have copied this example into their production code should 
review it to ensure that the extraction path is acceptable. The example 
has been changed accordingly, now the initial path and the extraction 
paths are converted into canonical paths and it is verified that 
extraction path contains the initial path. The documentation has also 
been adjusted.</p>

### References
* https://github.com/JoakimBulow/
* https://lists.apache.org/thread/gyfq5tcrxfv7rx0z2yyx4hb3h53ndffw


### Credits
* Joakim Bülow (Neo4j Security Team) (finder)


## A carefully crafted PDF file can trigger an infinite loop while loading the file ## { #CVE-2021-31812 }

CVE-2021-31812 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-31812) [\[CVE json\]](./CVE-2021-31812.cve.json) [\[OSV json\]](./CVE-2021-31812.osv.json)



_Last updated: 2021-06-12T09:40:30.803Z_

### Affected

* Apache PDFBox from Apache PDFBox before 2.0.24


### Description

In Apache PDFBox, a carefully crafted PDF file can trigger an infinite loop while loading the file. This issue affects Apache PDFBox version 2.0.23 and prior 2.0.x versions.

### References
* https://lists.apache.org/thread.html/ra2ab0ce69ce8aaff0773b8c1036438387ce004c2afc6f066626e205e%40%3Cusers.pdfbox.apache.org%3E


### Credits
* Apache PDFBox would like to thank Chaoyuan Peng for reporting this issue


## A carefully crafted PDF file can trigger an OutOfMemory-Exception while loading a tiny file ## { #CVE-2021-31811 }

CVE-2021-31811 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-31811) [\[CVE json\]](./CVE-2021-31811.cve.json) [\[OSV json\]](./CVE-2021-31811.osv.json)



_Last updated: 2021-06-12T09:40:36.582Z_

### Affected

* Apache PDFBox from Apache PDFBox before 2.0.24


### Description

In Apache PDFBox, a carefully crafted PDF file can trigger an OutOfMemory-Exception while loading the file. This issue affects Apache PDFBox version 2.0.23 and prior 2.0.x versions.

### References
* https://lists.apache.org/thread.html/re3bd16f0cc8f1fbda46b06a4b8241cd417f71402809baa81548fc20e%40%3Cusers.pdfbox.apache.org%3E


### Credits
* Apache PDFBox would like to thank Chaoyuan Peng for reporting this issue


## A carefully crafted PDF file can trigger an OutOfMemory-Exception while loading the file ## { #CVE-2021-27906 }

CVE-2021-27906 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-27906) [\[CVE json\]](./CVE-2021-27906.cve.json) [\[OSV json\]](./CVE-2021-27906.osv.json)



_Last updated: 2021-03-19T16:03:06.161Z_

### Affected

* Apache PDFBox from Apache PDFBox through 2.0.22


### Description

A carefully crafted PDF file can trigger an OutOfMemory-Exception while loading the file. This issue affects Apache PDFBox version 2.0.22 and prior 2.0.x versions.

### References
* https://lists.apache.org/thread.html/rf35026148ccc0e1af133501c0d003d052883fcc65107b3ff5d3b61cd%40%3Cusers.pdfbox.apache.org%3E


### Credits
* Apache PDFBox would like to thank Fabian Meumertzheim for reporting this issue


## A carefully crafted PDF file can trigger an infinite loop while loading the file ## { #CVE-2021-27807 }

CVE-2021-27807 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-27807) [\[CVE json\]](./CVE-2021-27807.cve.json) [\[OSV json\]](./CVE-2021-27807.osv.json)



_Last updated: 2021-03-19T16:02:02.671Z_

### Affected

* Apache PDFBox from Apache PDFBox through 2.0.22


### Description

A carefully crafted PDF file can trigger an infinite loop while loading the file. This issue affects Apache PDFBox version 2.0.22 and prior 2.0.x versions.

### References
* https://lists.apache.org/thread.html/r818058ff1e4b9f6bef4e5a2e74faff38cb3d3885c1e2db398bc55cfb%40%3Cusers.pdfbox.apache.org%3E


### Credits
* Apache PDFBox would like to thank Fabian Meumertzheim for reporting this issue
