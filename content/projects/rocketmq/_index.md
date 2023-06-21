---
title: Apache RocketMQ security advisories
description: Security information for Apache RocketMQ
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache RocketMQ? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

## Possible remote code execution vulnerability when using the update configuration function ## { #CVE-2023-33246 }

[CVE-2023-33246](./CVE-2023-33246.cve.json)

### Affected

* Apache RocketMQ versions  including 5.1.0


### Description

<p>For RocketMQ versions 5.1.0 and below, under certain conditions, there is a risk of remote command execution.&nbsp;</p><p>Several components of RocketMQ, including NameServer, Broker, and Controller, are leaked on the extranet and lack permission verification, an attacker can exploit this vulnerability by using the update configuration function to execute commands as the system users that RocketMQ is running as. Additionally, an attacker can achieve the same effect by forging the RocketMQ protocol content.&nbsp;</p><p>To prevent these attacks, users are recommended to upgrade to version 5.1.1 or above&nbsp;for using RocketMQ 5.x&nbsp;or 4.9.6 or above for using RocketMQ 4.x .</p>






<p></p><br>