---
title: Apache Ignite security advisories
description: Security information for Apache Ignite
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Ignite? You can read more about the projects' security policy on their [security page](https://ignite.apache.org/docs/latest/security/security-model), and email your report to the [Apache Ignite Security Team](mailto:security@ignite.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://ignite.apache.org/docs/latest/security/security-model). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Possible RCE when deserializing incoming messages by the server node ## { #CVE-2024-52577 }

CVE-2024-52577 [\[CVE json\]](./CVE-2024-52577.cve.json) [\[OSV json\]](./CVE-2024-52577.osv.json)



_Last updated: 2025-02-14T09:55:31.279Z_

### Affected

* Apache Ignite from 2.6.0 before 2.17.0


### Description

<p>In Apache Ignite versions from 2.6.0 and before 2.17.0, configured Class Serialization Filters are ignored for some Ignite endpoints. The vulnerability could be exploited if an attacker manually crafts an Ignite message containing a vulnerable object whose class is present in the Ignite server classpath and sends it to Ignite server endpoints. Deserialization of such a message by the Ignite server may result in the execution of arbitrary code on the Apache Ignite server side.<br></p><p><br></p>

### References
* https://lists.apache.org/thread/1bst0n27m9kb3b6f6hvlghn182vqb2hh


### Credits
* zhattatey (zhattatey@gmail.com) (finder)
* zhattatey (zhattatey@gmail.com) (reporter)
* Mikhail Petrov (mpetrov@apache.org) (remediation developer)
* Alex Plehanov (plehanov.alex@gmail.com) (remediation reviewer)
