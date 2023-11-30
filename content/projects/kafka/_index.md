---
title: Apache Kafka security advisories
description: Security information for Apache Kafka
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Kafka? You can read more about the projects' security policy on their [security page](https://kafka.apache.org/project-security.html), and email your report to the [Apache Kafka Security Team](mailto:security@kafka.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://kafka.apache.org/project-security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Timing Attack Vulnerability for Apache Kafka Connect and Clients ## { #CVE-2021-38153 }

CVE-2021-38153 [\[CVE json\]](./CVE-2021-38153.cve.json)

### Affected

* Apache Kafka from Apache Kafka 2.0.x through 2.0.1
* Apache Kafka from Apache Kafka 2.1.x through 2.1.1
* Apache Kafka from Apache Kafka 2.2.x through 2.2.2
* Apache Kafka from Apache Kafka 2.3.x through 2.3.1
* Apache Kafka from Apache Kafka 2.4.x through 2.4.1
* Apache Kafka from Apache Kafka 2.5.x through 2.5.1
* Apache Kafka from Apache Kafka 2.6.x through 2.6.2
* Apache Kafka from Apache Kafka 2.7.x through 2.7.1
* Apache Kafka from Apache Kafka 2.8.x through 2.8.0


### Description

Some components in Apache Kafka use `Arrays.equals` to validate a password or key, which is vulnerable to timing attacks that make brute force attacks for such credentials more likely to be successful. Users should upgrade to 2.8.1 or higher, or 3.0.0 or higher where this vulnerability has been fixed. The affected versions include Apache Kafka 2.0.0, 2.0.1, 2.1.0, 2.1.1, 2.2.0, 2.2.1, 2.2.2, 2.3.0, 2.3.1, 2.4.0, 2.4.1, 2.5.0, 2.5.1, 2.6.0, 2.6.1, 2.6.2, 2.7.0, 2.7.1, and 2.8.0.

### References
* https://kafka.apache.org/cve-list


### Credits
* Apache Kafka would like to thank J. Santilli for reporting this issue.


## Unauthenticated clients may cause OutOfMemoryError on Apache Kafka Brokers ## { #CVE-2022-34917 }

CVE-2022-34917 [\[CVE json\]](./CVE-2022-34917.cve.json)

### Affected

* Apache Kafka at Apache Kafka 2.8.0 2.8.0 
* Apache Kafka at Apache Kafka 2.8.1 2.8.1
* Apache Kafka at Apache Kafka 3.0.0 3.0.0
* Apache Kafka at Apache Kafka 3.0.1 3.0.1
* Apache Kafka at Apache Kafka 3.1.0 3.1.0
* Apache Kafka at Apache Kafka 3.1.1 3.1.1
* Apache Kafka at Apache Kafka 3.2.0 3.2.0
* Apache Kafka at Apache Kafka 3.2.1 3.2.1


### Description

A security vulnerability has been identified in Apache Kafka. It affects all releases since 2.8.0. The vulnerability allows malicious
unauthenticated clients to allocate large amounts of memory on brokers. This can lead to brokers hitting OutOfMemoryException and
causing denial of service.

Example scenarios:
- Kafka cluster without authentication: Any clients able to establish
a network connection to a broker can trigger the issue.
- Kafka cluster with SASL authentication: Any clients able to
establish a network connection to a broker, without the need for valid
SASL credentials, can trigger the issue.
- Kafka cluster with TLS authentication: Only clients able to
successfully authenticate via TLS can trigger the issue.

We advise the users to upgrade the Kafka installations to one of the 3.2.3, 3.1.2, 3.0.2, 2.8.2 versions.

### References
* https://kafka.apache.org/cve-list


### Credits
* Apache Kafka would like to thank Mickael Maison, Tom Bentley and Daniel Collins for reporting this issue.


## Possible RCE/Denial of service attack via SASL JAAS JndiLoginModule configuration using Kafka Connect  ## { #CVE-2023-25194 }

CVE-2023-25194 [\[CVE json\]](./CVE-2023-25194.cve.json)

### Affected

* Apache Kafka Connect API from 2.3.0 before 3.4.0


### Description

A possible security vulnerability has been identified in Apache Kafka Connect API.<br>This requires access to a Kafka Connect worker, and the ability to create/modify connectors on it with an arbitrary Kafka client SASL JAAS config<br>and a SASL-based security protocol, which has been possible on Kafka Connect clusters since Apache Kafka Connect 2.3.0.<br>When configuring the connector via the Kafka Connect REST API, an&nbsp;<span style="background-color: rgb(255, 255, 255);">authenticated operator</span>&nbsp;can set the <span style="background-color: rgb(255, 255, 255);">`sasl.jaas.config`<br></span>property for any of the connector's Kafka clients&nbsp;to "com.sun.security.auth.module.JndiLoginModule", which can be done via the<br>`producer.override.sasl.jaas.config`, `consumer.override.sasl.jaas.config`, or `admin.override.sasl.jaas.config` properties.<br>This will allow the server to connect to the attacker's LDAP server<br>and deserialize the LDAP response, which the attacker can use to execute java deserialization gadget chains on the Kafka connect server.<br>Attacker can cause <span style="background-color: rgb(255, 255, 255);">unrestricted deserialization of untrusted data (or)&nbsp;</span>RCE vulnerability when there are gadgets in the classpath.<br><br>Since Apache Kafka 3.0.0, users are allowed to specify these properties in connector configurations for Kafka Connect clusters running with out-of-the-box<br>configurations. Before Apache Kafka 3.0.0, users may not specify these properties unless the Kafka Connect cluster has been reconfigured with a connector<br>client override policy that permits them.<br><br>Since Apache Kafka 3.4.0, we have added a system property ("-Dorg.apache.kafka.disallowed.login.modules") to disable the problematic login modules usage<br>in SASL JAAS configuration. Also by default "com.sun.security.auth.module.JndiLoginModule" is disabled in Apache Kafka Connect 3.4.0. <br><br>We advise the Kafka Connect users to validate connector configurations and only allow trusted JNDI configurations. Also examine connector dependencies for <br>vulnerable versions and either upgrade their connectors, upgrading that specific dependency, or removing the connectors as options for remediation. Finally,<br><span style="background-color: rgb(255, 255, 255);">in addition to leveraging the "org.apache.kafka.disallowed.login.modules" system property, Kafka Connect users can also implement their own connector<br>client config override policy, which can be used to control which Kafka client properties can be overridden directly in a connector config and which cannot.</span><br>

### References
* https://kafka.apache.org/cve-list
* https://lists.apache.org/thread/vy1c7fqcdqvq5grcqp6q5jyyb302khyz
* http://packetstormsecurity.com/files/173151/Apache-Druid-JNDI-Injection-Remote-Code-Execution.html


### Credits
* Apache Kafka would like to thank to Jari Jääskelä (https://hackerone.com/reports/1529790) and 4ra1n and Y4tacker (they found vulnerabilities in other Apache projects. After discussion between PMC of the two projects, it was finally confirmed that it was the vulnerability of Kafka then they reported it to us) (finder)
