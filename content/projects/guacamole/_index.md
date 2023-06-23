---
title: Apache Guacamole security advisories
description: Security information for Apache Guacamole
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Guacamole? You can read more about the projects' security policy on their [security page](https://guacamole.apache.org/security/), and email your report to the  [Apache Guacamole Security Team](mailto:security@guacamole.apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Guacamole since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. It may also lack details found on the [project security page](https://guacamole.apache.org/security/).

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Incorrect calculation of Guacamole protocol element lengths ## { #CVE-2023-30575 }

[CVE-2023-30575](./CVE-2023-30575.cve.json)

### Affected

* Apache Guacamole through 1.5.1


### Description

Apache Guacamole 1.5.1 and older may incorrectly calculate the lengths of instruction elements sent during the Guacamole protocol handshake, potentially allowing an attacker to inject Guacamole instructions during the handshake through specially-crafted data.<br><br>

## Use-after-free in handling of RDP audio input buffer ## { #CVE-2023-30576 }

[CVE-2023-30576](./CVE-2023-30576.cve.json)

### Affected

* Apache Guacamole from 0.9.10 through 1.5.1


### Description

Apache Guacamole 0.9.10 through 1.5.1 may continue to reference a freed RDP audio input buffer. Depending on timing, this may allow an attacker to execute arbitrary code with the privileges of the guacd process.<br><br>