---
title: Apache Calcite security advisories
description: Security information for Apache Calcite
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Calcite? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Calcite Avatica JDBC driver `httpclient_impl` connection property can be used as an RCE vector ## { #CVE-2022-36364 }

CVE-2022-36364 [\[CVE json\]](./CVE-2022-36364.cve.json)

_Last updated: 2022-07-28T08:30:13.087Z_

### Affected

* Apache Calcite Avatica from Apache Calcite Avatica before 1.22.0


### Description

Apache Calcite Avatica JDBC driver creates HTTP client instances based on class names provided via `httpclient_impl` connection property; however, the driver does not verify if the class implements the expected interface before instantiating it, which can lead to code execution loaded via arbitrary classes and in rare cases remote code execution.

To exploit the vulnerability:
1) the attacker needs to have privileges to control JDBC connection parameters;
2) and there should be a vulnerable class (constructor with URL parameter and ability to execute code) in the classpath.

From Apache Calcite Avatica 1.22.0 onwards, it will be verified that the class implements the expected interface before invoking its constructor.

### References
* https://lists.apache.org/thread/5csdj8bv4h3hfgw27okm84jh1j2fyw0c


### Credits
* Apache Calcite Avatica would like to thank Peter M (https://twitter.com/h1pmnh) for reporting this issue


## Apache Calcite: potential XEE attacks ## { #CVE-2022-39135 }

CVE-2022-39135 [\[CVE json\]](./CVE-2022-39135.cve.json)

_Last updated: 2023-09-18T12:55:46.886Z_

### Affected

* Apache Calcite from Apache Calcite before 1.32.0


### Description

Apache Calcite 1.22.0 introduced the SQL operators EXISTS_NODE, EXTRACT_XML, XML_TRANSFORM and EXTRACT_VALUE, which do not restrict XML External Entity references in their configuration, making them vulnerable to a potential XML External Entity (XXE) attack. Therefore any client exposing these operators, typically by using Oracle dialect (the first three) or MySQL dialect (the last one), is affected by this vulnerability (the extent of it will depend on the user under which the application is running).

From Apache Calcite 1.32.0 onwards, Document Type Declarations and XML External Entity resolution are disabled on the impacted operators.

### References
* https://lists.apache.org/thread/ohdnhlgm6jvt3srw8l7spkm2d5vwm082


### Credits
* Apache Calcite would like to thank David Handermann for reporting this issue
