---
title: Apache RocketMQ security advisories
description: Security information for Apache RocketMQ
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache RocketMQ? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Possible remote code execution vulnerability when using the update configuration function ## { #CVE-2023-33246 }

CVE-2023-33246 [\[CVE json\]](./CVE-2023-33246.cve.json) [\[OSV json\]](./CVE-2023-33246.osv.json)



_Last updated: 2023-05-24T14:45:21.368Z_

### Affected

* Apache RocketMQ through 5.1.0


### Description

<p>For RocketMQ versions 5.1.0 and below, under certain conditions, there is a risk of remote command execution.&nbsp;</p><p>Several components of RocketMQ, including NameServer, Broker, and Controller, are leaked on the extranet and lack permission verification, an attacker can exploit this vulnerability by using the update configuration function to execute commands as the system users that RocketMQ is running as. Additionally, an attacker can achieve the same effect by forging the RocketMQ protocol content.&nbsp;</p><p>To prevent these attacks, users are recommended to upgrade to version 5.1.1 or above&nbsp;for using RocketMQ 5.x&nbsp;or 4.9.6 or above for using RocketMQ 4.x .</p>






<p></p><br>

### References
* https://lists.apache.org/thread/1s8j2c8kogthtpv3060yddk03zq0pxyp


### Credits
* lvyyevd@gmail.com (reporter)


## Possible remote code execution when using the update configuration function ## { #CVE-2023-37582 }

CVE-2023-37582 [\[CVE json\]](./CVE-2023-37582.cve.json) [\[OSV json\]](./CVE-2023-37582.osv.json)



_Last updated: 2023-07-12T09:26:16.623Z_

### Affected

* Apache RocketMQ from 5.0.0 through 5.1.1
* Apache RocketMQ through 4.9.6


### Description

<span style="background-color: rgb(255, 255, 255);">The RocketMQ NameServer component still has a remote command execution vulnerability as the CVE-2023-33246 issue was not completely fixed in version 5.1.1. <br><br>When NameServer address </span>are leaked on the extranet and lack permission verification, a<span style="background-color: rgb(255, 255, 255);">n attacker can exploit this vulnerability by using the update configuration function on the NameServer component to execute commands as the system users that RocketMQ is running as. <br><br>It is recommended for users to upgrade their NameServer version to 5.1.2 or above for RocketMQ 5.x or 4.9.7 or above for RocketMQ 4.x to prevent these attacks.</span><br>

### References
* https://lists.apache.org/thread/m614czxtpvlztd7mfgcs2xcsg36rdbnc


### Credits
* soreatu@gmail.com (finder)
* yuansec@outlook.com  (finder)
