---
title: Apache Guacamole security advisories
description: Security information for Apache Guacamole
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Guacamole? You can read more about the projects' security policy on their [security page](https://guacamole.apache.org/security/), and email your report to the  [Apache Guacamole Security Team](mailto:security@guacamole.apache.org).

# Advisories

## Incorrect calculation of Guacamole protocol element lengths ## { #CVE-2023-30575 }

[CVE-2023-30575](./CVE-2023-30575.cve.json)

### Affected

* Apache Guacamole versions  including 1.5.1


### Description

Apache Guacamole 1.5.1 and older may incorrectly calculate the lengths of instruction elements sent during the Guacamole protocol handshake, potentially allowing an attacker to inject Guacamole instructions during the handshake through specially-crafted data.<br><br>

## Use-after-free in handling of RDP audio input buffer ## { #CVE-2023-30576 }

[CVE-2023-30576](./CVE-2023-30576.cve.json)

### Affected

* Apache Guacamole versions 0.9.10 including 1.5.1


### Description

Apache Guacamole 0.9.10 through 1.5.1 may continue to reference a freed RDP audio input buffer. Depending on timing, this may allow an attacker to execute arbitrary code with the privileges of the guacd process.<br><br>