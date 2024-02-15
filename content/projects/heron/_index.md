---
title: Apache Heron (Incubating) security advisories
description: Security information for Apache Heron (Incubating)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Heron (Incubating)? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## CRLF log injection ## { #CVE-2021-42010 }

CVE-2021-42010 [\[CVE json\]](./CVE-2021-42010.cve.json)

### Affected

* Apache Heron (Incubating) from Apache Heron 0.20.4-incubating through 0.20.4-incubating


### Description

Heron versions <= 0.20.4-incubating allows CRLF log injection because of the lack of escaping in the log statements.  Please update to version 0.20.5-incubating which addresses this issue. 

### References
* https://lists.apache.org/thread/j65nwr8n7jchngwqptzh100drcr4ry2q


### Credits
* The Apache Heron (Incubating) project would like to thank Bo Yu for bringing this matter to our attention.
