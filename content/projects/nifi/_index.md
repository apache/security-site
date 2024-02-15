---
title: Apache NiFi security advisories
description: Security information for Apache NiFi
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache NiFi? You can read more about the projects' security policy on their [security page](https://nifi.apache.org/security.html), and email your report to the [Apache NiFi Security Team](mailto:security@nifi.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://nifi.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## MiNiFi CPP arbitrary script execution is possible on the agent's host machine through the c2 protocol ## { #CVE-2021-33191 }

CVE-2021-33191 [\[CVE json\]](./CVE-2021-33191.cve.json)

_Last updated: 2021-08-24T11:14:05.278Z_

### Affected

* Apache NiFi - MiNiFi C++ from 0.5.0 before Apache NiFi - MiNiFi C++*


### Description

From Apache NiFi MiNiFi C++ version 0.5.0 the c2 protocol implements an "agent-update" command which was designed to patch the application binary. 
This "patching" command defaults to calling a trusted binary, but might be modified to an arbitrary value through a "c2-update"
command. Said command is then executed using the same privileges as the application binary.  This was addressed in version 0.10.0

### References
* https://www.openwall.com/lists/oss-security/2021/08/24/1


## Apache NiFi information disclosure by XXE ## { #CVE-2021-44145 }

CVE-2021-44145 [\[CVE json\]](./CVE-2021-44145.cve.json)

_Last updated: 2021-12-17T08:46:07.497Z_

### Affected

* Apache NiFi from Apache NiFi through 1.15.0


### Description

In the TransformXML processor of Apache NiFi before 1.15.1 an authenticated user could configure an XSLT file which, if it included malicious external entity calls, may reveal sensitive information.

### References
* https://nifi.apache.org/security.html#1.15.1-vulnerabilities


### Credits
* This issue was discovered by DangKhai at Viettel Cyber Security.


## Insufficiently protected credentials ## { #CVE-2022-26850 }

CVE-2022-26850 [\[CVE json\]](./CVE-2022-26850.cve.json)

_Last updated: 2022-04-06T20:48:13.265Z_

### Affected

* Apache NiFi at NiFi 1.14.0 to 1.15.3


### Description

When creating or updating credentials for single-user access, Apache NiFi wrote a copy of the Login Identity Providers configuration to the operating system temporary directory. On most platforms, the operating system temporary directory has global read permissions. NiFi immediately moved the temporary file to the final configuration directory, which significantly limited the window of opportunity for access.

NiFi 1.16.0 includes updates to replace the Login Identity Providers configuration without writing a file to the operating system temporary directory.


### References
* https://nifi.apache.org/security.html#CVE-2022-26850


### Credits
* This issue was discovered by Jonathan Leitschuh (https://twitter.com/jlleitschuh)


## Improper Restriction of XML External Entity References in Multiple Components ## { #CVE-2022-29265 }

CVE-2022-29265 [\[CVE json\]](./CVE-2022-29265.cve.json)

_Last updated: 2022-04-30T08:01:30.969Z_

### Affected

* Apache NiFi from 0.0.1 to 1.16.0 through 0.0.1 to 1.16.0


### Description

Multiple components in Apache NiFi 0.0.1 to 1.16.0 do not restrict XML External Entity references in the default configuration.

The Standard Content Viewer service attempts to resolve XML External Entity references when viewing formatted XML files.

The following Processors attempt to resolve XML External Entity references when configured with default property values:

- EvaluateXPath
- EvaluateXQuery
- ValidateXml

Apache NiFi flow configurations that include these Processors are vulnerable to malicious XML documents that contain Document Type Declarations with XML External Entity references.

The resolution disables Document Type Declarations in the default configuration for these Processors, and disallows XML External Entity resolution in standard services.

### References
* https://nifi.apache.org/security.html#CVE-2022-29265
* https://lists.apache.org/thread/47od9kr9n4cyv0mv81jh3pkyx815kyjl


### Credits
* David Handermann at exceptionfactory.com reported this issue.


## Improper Neutralization of Command Elements in Shell User Group Provider ## { #CVE-2022-33140 }

CVE-2022-33140 [\[CVE json\]](./CVE-2022-33140.cve.json)

_Last updated: 2022-06-15T14:21:09.085Z_

### Affected

* Apache NiFi from up to 1.16.2 through 1.16.2
* Apache NiFi from 1.10.0 before 1.10.0*
* Apache NiFi Registry from up to 1.16.2 through 1.16.2
* Apache NiFi Registry from 0.6.0 before 0.6.0*


### Description

The optional ShellUserGroupProvider in Apache NiFi 1.10.0 to 1.16.2 and Apache NiFi Registry 0.6.0 to 1.16.2 does not neutralize arguments for group resolution commands, allowing injection of operating system commands on Linux and macOS platforms.

The ShellUserGroupProvider is not included in the default configuration. Command injection requires ShellUserGroupProvider to be one of the enabled User Group Providers in the Authorizers configuration. Command injection also requires an authenticated user with elevated privileges.  Apache NiFi requires an authenticated user with authorization to modify access policies in order to execute the command. Apache NiFi Registry requires an authenticated user with authorization to read user groups in order to execute the command.

The resolution removes command formatting based on user-provided arguments.

### References
* https://lists.apache.org/thread/bzs2pcdjsdrh5039oslmfr9mbs9qqdhr
* https://nifi.apache.org/security.html#CVE-2022-33140


## Improper Restriction of XML External Entity References in ExtractCCDAAttributes ## { #CVE-2023-22832 }

CVE-2023-22832 [\[CVE json\]](./CVE-2023-22832.cve.json)

_Last updated: 2023-02-10T07:45:29.071Z_

### Affected

* Apache NiFi from 1.2.0 through 1.19.1


### Description

<div>The ExtractCCDAAttributes Processor in Apache NiFi 1.2.0 through 1.19.1 does not restrict XML External Entity references.</div><div>Flow configurations that include the ExtractCCDAAttributes Processor are vulnerable to malicious XML documents that contain Document Type Declarations with XML External Entity references.</div><div>The resolution disables Document Type Declarations and disallows XML External Entity resolution in the ExtractCCDAAttributes Processor.</div>

### References
* https://nifi.apache.org/security.html#CVE-2023-22832
* https://lists.apache.org/thread/b51qs6y7b7r58vovddkv6wc16g2xbl3w


### Credits
* Yi Cai of Chaitin Tech (finder)


## Potential Deserialization of Untrusted Data with JNDI in JMS Components ## { #CVE-2023-34212 }

CVE-2023-34212 [\[CVE json\]](./CVE-2023-34212.cve.json)

_Last updated: 2023-06-12T15:10:30.889Z_

### Affected

* Apache NiFi from 1.8.0 through 1.21.0


### Description

<div>The JndiJmsConnectionFactoryProvider Controller Service, along with the ConsumeJMS and PublishJMS Processors, in Apache NiFi 1.8.0 through 1.21.0 allow an authenticated and authorized user to configure URL and library properties that enable deserialization of untrusted data from a remote location.</div><div>The resolution validates the JNDI URL and restricts locations to a set of allowed schemes.</div><div>You are recommended to upgrade to version 1.22.0 or later which fixes this issue.<br></div>

### References
* https://nifi.apache.org/security.html#CVE-2023-34212
* https://lists.apache.org/thread/w5rm46fxmvxy216tglf0dv83wo6gnzr5


### Credits
* Veraxy00 of Qianxin TI Center (finder)
* Matei "Mal" Badanoiu (reporter)


## Potential Code Injection with Database Services using H2 ## { #CVE-2023-34468 }

CVE-2023-34468 [\[CVE json\]](./CVE-2023-34468.cve.json)

_Last updated: 2023-06-12T15:09:17.702Z_

### Affected

* Apache NiFi from 0.0.2 through 1.21.0


### Description

<div>The DBCPConnectionPool and HikariCPConnectionPool Controller Services in Apache NiFi 0.0.2 through 1.21.0 allow an authenticated and authorized user to configure a Database URL with the H2 driver that enables custom code execution.</div><div>The resolution validates the Database URL and rejects H2 JDBC locations.</div><div>You are recommended to upgrade to version 1.22.0 or later which fixes this issue.<br></div>

### References
* https://nifi.apache.org/security.html#CVE-2023-34468
* https://lists.apache.org/thread/7b82l4f5blmpkfcynf3y6z4x1vqo59h8


### Credits
* Matei "Mal" Badanoiu (finder)


## Potential Code Injection with Properties Referencing Remote Resources ## { #CVE-2023-36542 }

CVE-2023-36542 [\[CVE json\]](./CVE-2023-36542.cve.json)

_Last updated: 2023-07-29T07:12:37.941Z_

### Affected

* Apache NiFi from 0.0.2 through 1.22.0


### Description

Apache NiFi 0.0.2 through 1.22.0 include Processors and Controller Services that support HTTP URL references for retrieving drivers, which allows an authenticated and authorized user to configure a location that enables custom code execution. The resolution introduces a new Required Permission for referencing remote resources, restricting configuration of these components to privileged users. The permission prevents unprivileged users from configuring Processors and Controller Services annotated with the new Reference Remote Resources restriction. Upgrading to Apache NiFi 1.23.0 is the recommended mitigation.<br>

### References
* https://nifi.apache.org/security.html#CVE-2023-36542
* https://lists.apache.org/thread/swnly3dzhhq9zo3rofc8djq77stkhbof


### Credits
* nbxiglk (finder)


## Incomplete Validation of JDBC and JNDI Connection URLs ## { #CVE-2023-40037 }

CVE-2023-40037 [\[CVE json\]](./CVE-2023-40037.cve.json)

_Last updated: 2023-08-18T21:54:49.856Z_

### Affected

* Apache NiFi from 1.21.0 through 1.23.0


### Description

Apache NiFi 1.21.0 through 1.23.0 support JDBC and JNDI JMS access in several Processors and Controller Services with connection URL validation that does not provide sufficient protection against crafted inputs. An authenticated and authorized user can bypass connection URL validation using custom input formatting. The resolution enhances connection URL validation and introduces validation for additional related properties. Upgrading to Apache NiFi 1.23.1 is the recommended mitigation.<br>

### References
* https://nifi.apache.org/security.html#CVE-2023-40037
* https://lists.apache.org/thread/bqbjlrs2p5ghh8sbk5nsxb8xpf9l687q


### Credits
* Matei "Mal" Badanoiu (finder)


## Incorrect Certificate Validation in InvokeHTTP for MiNiFi C++ ## { #CVE-2023-41180 }

CVE-2023-41180 [\[CVE json\]](./CVE-2023-41180.cve.json)

_Last updated: 2023-09-03T15:52:48.640Z_

### Affected

* Apache NiFi MiNiFi C++ from 0.13.0 through 0.14.0


### Description

<div>Incorrect certificate validation in InvokeHTTP on Apache NiFi MiNiFi C++ versions 0.13 to 0.14 allows an intermediary to present a forged certificate during TLS handshake negotation. The Disable Peer Verification property of InvokeHTTP was effectively flipped,  disabling verification by default, when using HTTPS.<br></div><div><br></div><div>Mitigation: Set the Disable Peer Verification property of InvokeHTTP to true when using MiNiFi C++ versions 0.13.0 or 0.14.0. Upgrading to MiNiFi C++ 0.15.0 corrects the default behavior.<br></div>

### References
* https://lists.apache.org/thread/b51f8csysg1pvgs6xjjrq5hrjrvfot1y


### Credits
* Ferenc Gerlits (finder)


## Improper Neutralization of Input in Advanced User Interface for Jolt ## { #CVE-2023-49145 }

CVE-2023-49145 [\[CVE json\]](./CVE-2023-49145.cve.json)

_Last updated: 2023-11-27T22:29:16.184Z_

### Affected

* Apache NiFi from 0.7.0 through 1.23.2


### Description

Apache NiFi 0.7.0 through 1.23.2 include the JoltTransformJSON Processor, which provides an advanced configuration user interface that is vulnerable to DOM-based cross-site scripting. If an authenticated user, who is authorized to configure a JoltTransformJSON Processor, visits a crafted URL, then arbitrary
JavaScript code can be executed within the session context of the authenticated user. Upgrading to Apache NiFi 1.24.0 or 2.0.0-M1 is the recommended mitigation.

### References
* https://nifi.apache.org/security.html#CVE-2023-49145
* https://lists.apache.org/thread/j8rd0qsvgoj0khqck5f49jfbp0fm8r1o


### Credits
* Dr. Oliver Matula, DB Systel GmbH (finder)
