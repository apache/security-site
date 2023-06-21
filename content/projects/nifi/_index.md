---
title: Apache NiFi security advisories
description: Security information for Apache NiFi
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache NiFi? You can read more about the projects' security policy on their [security page](https://nifi.apache.org/security.html), and email your report to the  [Apache NiFi Security Team](mailto:security@nifi.apache.org).

# Advisories

## Improper Restriction of XML External Entity References in ExtractCCDAAttributes ## { #CVE-2023-22832 }

[CVE-2023-22832](./CVE-2023-22832.cve.json)

### Affected

* Apache NiFi versions 1.2.0 including 1.19.1


### Description

<div>The ExtractCCDAAttributes Processor in Apache NiFi 1.2.0 through 1.19.1 does not restrict XML External Entity references.</div><div>Flow configurations that include the ExtractCCDAAttributes Processor are vulnerable to malicious XML documents that contain Document Type Declarations with XML External Entity references.</div><div>The resolution disables Document Type Declarations and disallows XML External Entity resolution in the ExtractCCDAAttributes Processor.</div>