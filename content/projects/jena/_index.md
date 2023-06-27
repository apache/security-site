---
title: Apache Jena security advisories
description: Security information for Apache Jena
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Jena? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Exposure of arbitrary execution in script engine expressions. ## { #CVE-2023-22665 }

[CVE-2023-22665](./CVE-2023-22665.cve.json)

### Affected

* Apache Jena through 4.7.0


### Description

There is insufficient checking of user queries in Apache Jena versions 4.7.0 and earlier, when invoking custom scripts. It allows a remote user to execute arbitrary javascript via a SPARQL query.

### References
* https://lists.apache.org/thread/s0dmpsxcwqs57l4qfs415klkgmhdxq7s
