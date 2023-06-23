---
title: Apache Jena security advisories
description: Security information for Apache Jena
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Jena? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Jena since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Exposure of arbitrary execution in script engine expressions. ## { #CVE-2023-22665 }

[CVE-2023-22665](./CVE-2023-22665.cve.json)

### Affected

* Apache Jena versions  including 4.7.0


### Description

There is insufficient checking of user queries in Apache Jena versions 4.7.0 and earlier, when invoking custom scripts. It allows a remote user to execute arbitrary javascript via a SPARQL query.