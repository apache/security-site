---
title: Apache EventMesh security advisories
description: Security information for Apache EventMesh
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache EventMesh? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache EventMesh RabbitMQ-Connector plugin allows RCE through deserialization of untrusted data ## { #CVE-2023-26512 }

CVE-2023-26512 [\[CVE json\]](./CVE-2023-26512.cve.json) [\[OSV json\]](./CVE-2023-26512.osv.json)



_Last updated: 2023-07-27T09:32:16.269Z_

### Affected

* Apache EventMesh (incubating) RabbitMQ connector from 1.7.0 through 1.8.0


### Description

CWE-502 Deserialization of Untrusted Data&nbsp;at the&nbsp;<span style="background-color: rgb(255, 255, 255);">rabbitmq-connector plugin</span>&nbsp;module in Apache EventMesh (incubating)&nbsp;V1.7.0\V1.8.0 on windows\linux\mac os e.g. platforms allows attackers&nbsp;to send controlled message and 

<span style="background-color: rgb(255, 255, 255);">remote code execute</span>&nbsp;via rabbitmq messages. Users can use the code under the master branch in project repo to fix this issue, we will release the new version as soon as possible.

### References
* https://lists.apache.org/thread/zb1d62wh8o8pvntrnx4t1hj8vz0pm39p


### Credits
* xuxiaoyu of HW GTS shengjian lab (reporter)
