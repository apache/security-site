---
title: Apache NiFi security advisories
description: Security information for Apache NiFi
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache NiFi? You can read more about the projects' security policy on their [security page](https://nifi.apache.org/security.html), and email your report to the  [Apache NiFi Security Team](mailto:security@nifi.apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache NiFi since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. It may also lack details found on the [project security page](https://nifi.apache.org/security.html).

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Improper Restriction of XML External Entity References in ExtractCCDAAttributes ## { #CVE-2023-22832 }

[CVE-2023-22832](./CVE-2023-22832.cve.json)

### Affected

* Apache NiFi from 1.2.0 through 1.19.1


### Description

<div>The ExtractCCDAAttributes Processor in Apache NiFi 1.2.0 through 1.19.1 does not restrict XML External Entity references.</div><div>Flow configurations that include the ExtractCCDAAttributes Processor are vulnerable to malicious XML documents that contain Document Type Declarations with XML External Entity references.</div><div>The resolution disables Document Type Declarations and disallows XML External Entity resolution in the ExtractCCDAAttributes Processor.</div>

### References
* https://nifi.apache.org/security.html#CVE-2023-22832
* https://lists.apache.org/thread/b51qs6y7b7r58vovddkv6wc16g2xbl3w


## Potential Deserialization of Untrusted Data with JNDI in JMS Components ## { #CVE-2023-34212 }

[CVE-2023-34212](./CVE-2023-34212.cve.json)

### Affected

* Apache NiFi from 1.8.0 through 1.21.0


### Description

<div>The JndiJmsConnectionFactoryProvider Controller Service, along with the ConsumeJMS and PublishJMS Processors, in Apache NiFi 1.8.0 through 1.21.0 allow an authenticated and authorized user to configure URL and library properties that enable deserialization of untrusted data from a remote location.</div><div>The resolution validates the JNDI URL and restricts locations to a set of allowed schemes.</div><div>You are recommended to upgrade to version 1.22.0 or later which fixes this issue.<br></div>

### References
* https://nifi.apache.org/security.html#CVE-2023-34212
* https://lists.apache.org/thread/w5rm46fxmvxy216tglf0dv83wo6gnzr5


## Potential Code Injection with Database Services using H2 ## { #CVE-2023-34468 }

[CVE-2023-34468](./CVE-2023-34468.cve.json)

### Affected

* Apache NiFi from 0.0.2 through 1.21.0


### Description

<div>The DBCPConnectionPool and HikariCPConnectionPool Controller Services in Apache NiFi 0.0.2 through 1.21.0 allow an authenticated and authorized user to configure a Database URL with the H2 driver that enables custom code execution.</div><div>The resolution validates the Database URL and rejects H2 JDBC locations.</div><div>You are recommended to upgrade to version 1.22.0 or later which fixes this issue.<br></div>

### References
* https://nifi.apache.org/security.html#CVE-2023-34468
* https://lists.apache.org/thread/7b82l4f5blmpkfcynf3y6z4x1vqo59h8
