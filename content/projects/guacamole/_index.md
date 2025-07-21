---
title: Apache Guacamole security advisories
description: Security information for Apache Guacamole
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Guacamole? You can read more about the projects' security policy on their [security page](https://guacamole.apache.org/security/), and email your report to the [Apache Guacamole Security Team](mailto:security@guacamole.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://guacamole.apache.org/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Private tunnel identifier may be included in the non-private details of active connections ## { #CVE-2021-41767 }

CVE-2021-41767 [\[CVE json\]](./CVE-2021-41767.cve.json) [\[OSV json\]](./CVE-2021-41767.osv.json)



_Last updated: 2022-01-11T22:07:33.145Z_

### Affected

* Apache Guacamole from unspecified through 1.3.0


### Description

Apache Guacamole 1.3.0 and older may incorrectly include a private tunnel identifier in the non-private details of some REST responses. This may allow an authenticated user who already has permission to access a particular connection to read from or interact with another user's active use of that same connection.

### References
* https://lists.apache.org/thread/5l31k4jmzdsfz0xt8osrbl878gb3b7ro


### Credits
* We would like to thank Damian Velardo (Australia and New Zealand Banking Group) for reporting this issue.


## Improper validation of SAML responses ## { #CVE-2021-43999 }

CVE-2021-43999 [\[CVE json\]](./CVE-2021-43999.cve.json) [\[OSV json\]](./CVE-2021-43999.osv.json)



_Last updated: 2022-01-11T22:07:28.747Z_

### Affected

* Apache Guacamole at 1.3.0
* Apache Guacamole at 1.2.0


### Description

Apache Guacamole 1.2.0 and 1.3.0 do not properly validate responses received from a SAML identity provider. If SAML support is enabled, this may allow a malicious user to assume the identity of another Guacamole user.

### References
* https://lists.apache.org/thread/4dt9h5mo4o9rxlgxm3rp8wfqdtdjn2z9


### Credits
* We would like to thank Finn Steglich (ETAS) for reporting this issue.


## Incorrect calculation of Guacamole protocol element lengths ## { #CVE-2023-30575 }

CVE-2023-30575 [\[CVE json\]](./CVE-2023-30575.cve.json) [\[OSV json\]](./CVE-2023-30575.osv.json)



_Last updated: 2023-06-15T07:27:08.313Z_

### Affected

* Apache Guacamole through 1.5.1


### Description

Apache Guacamole 1.5.1 and older may incorrectly calculate the lengths of instruction elements sent during the Guacamole protocol handshake, potentially allowing an attacker to inject Guacamole instructions during the handshake through specially-crafted data.<br><br>

### References
* https://lists.apache.org/thread/tn63n2lon0h5p45oft834t1dqvvxownv


### Credits
* Stefan Schiller (Sonar) (finder)


## Use-after-free in handling of RDP audio input buffer ## { #CVE-2023-30576 }

CVE-2023-30576 [\[CVE json\]](./CVE-2023-30576.cve.json) [\[OSV json\]](./CVE-2023-30576.osv.json)



_Last updated: 2023-06-06T17:26:55.108Z_

### Affected

* Apache Guacamole from 0.9.10 through 1.5.1


### Description

Apache Guacamole 0.9.10 through 1.5.1 may continue to reference a freed RDP audio input buffer. Depending on timing, this may allow an attacker to execute arbitrary code with the privileges of the guacd process.<br><br>

### References
* https://lists.apache.org/thread/vgtvxb3w7mm84hx6v8dfc0onsoz05gb6


### Credits
* Stefan Schiller (Sonar) (finder)


## Integer overflow in handling of VNC image buffers ## { #CVE-2023-43826 }

CVE-2023-43826 [\[CVE json\]](./CVE-2023-43826.cve.json) [\[OSV json\]](./CVE-2023-43826.osv.json)



_Last updated: 2023-12-19T19:50:08.611Z_

### Affected

* Apache Guacamole through 1.5.3


### Description

<div>Apache Guacamole 1.5.3 and older do not consistently ensure that values received from a VNC server will not result in integer overflow. If a user connects to a malicious or compromised VNC server, specially-crafted data could result in memory corruption, possibly allowing arbitrary code to be executed with the privileges of the running guacd process.<br></div><div>Users are recommended to upgrade to version 1.5.4, which fixes this issue.</div>

### References
* https://lists.apache.org/thread/23gzwftpfgtq97tj6ttmbclry53kmwv6


### Credits
* Joseph Surin (Elttam) (reporter)
* Matt Jones (Elttam) (reporter)


## Improper input validation of console codes ## { #CVE-2024-35164 }

CVE-2024-35164 [\[CVE json\]](./CVE-2024-35164.cve.json) [\[OSV json\]](./CVE-2024-35164.osv.json)



_Last updated: 2025-07-02T11:23:12.067Z_

### Affected

* Apache Guacamole from 0.8.0 through 1.5.5


### Description

<div>The terminal emulator of Apache Guacamole 1.5.5 and older does not properly validate console codes received from servers via text-based protocols like SSH. If a malicious user has access to a text-based connection, a specially-crafted sequence of console codes could allow arbitrary code to be executed
with the privileges of the running guacd process.</div><div><br></div><div>Users are recommended to upgrade to version 1.6.0, which fixes this issue.</div>

### References
* https://lists.apache.org/thread/sgs8lplbkrpvd3hrvcnnxh3028h4py70


### Credits
* Tizian Seehaus (Tibotix) (reporter)
