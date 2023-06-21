---
title: Apache CXF security advisories
description: Security information for Apache CXF
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache CXF? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

## Apache CXF directory listing / code exfiltration ## { #CVE-2022-46363 }

[CVE-2022-46363](./CVE-2022-46363.cve.json)

### Affected

* Apache CXF versions 3.5 before 3.5.53.4 before 3.4.10


### Description

A vulnerability in Apache CXF before versions 3.5.5 and 3.4.10 allows an attacker to perform a remote directory listing or code exfiltration. The vulnerability only applies when the&nbsp;CXFServlet is configured with both the&nbsp;static-resources-list and&nbsp;redirect-query-check attributes. These attributes are not supposed to be used together, and so the vulnerability can only arise if the CXF service is misconfigured.<br><br>

## Apache CXF SSRF Vulnerability ## { #CVE-2022-46364 }

[CVE-2022-46364](./CVE-2022-46364.cve.json)

### Affected

* Apache CXF versions  before 3.5.5 before 3.4.10


### Description

A SSRF vulnerability in parsing the&nbsp;href attribute of XOP:Include in MTOM requests in versions of Apache CXF before 3.5.5 and 3.4.10 allows an attacker to perform SSRF style attacks on webservices that take at least one parameter of any type.&nbsp;