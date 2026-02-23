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

## raft Hessian Deserialization Vulnerability allowing remote code execution ## { #CVE-2024-56180 }

CVE-2024-56180 [\[CVE json\]](./CVE-2024-56180.cve.json) [\[OSV json\]](./CVE-2024-56180.osv.json)



_Last updated: 2025-02-14T15:26:18.633Z_

### Affected

* Apache EventMesh from 1.10.1 before 1.11.0


### Description

<span style="background-color: rgb(255, 255, 255);">CWE-502 Deserialization of Untrusted Data at the eventmesh-meta-raft</span><span style="background-color: rgb(255, 255, 255);">&nbsp;plugin</span><span style="background-color: rgb(255, 255, 255);">&nbsp;module in Apache EventMesh master branch without release version on windows\linux\mac os e.g. platforms allows attackers to send controlled message and </span><span style="background-color: rgb(255, 255, 255);">remote code execute</span><span style="background-color: rgb(255, 255, 255);">&nbsp;via hessian d</span><span style="background-color: rgb(255, 255, 255);">eserialization rpc protocol</span><span style="background-color: rgb(255, 255, 255);">. Users can use the code under the master branch in project repo or version 1.11.0 to fix this issue.</span><br>

### References
* https://lists.apache.org/thread/k9fw0t5r7t1vbx53gs8d1r8c54rhx0wd


### Credits
* yulate (reporter)
* Au5t1n (reporter)
* h3h3qaq (reporter)
* X1r0z (reporter)


## SSRF ## { #CVE-2024-39954 }

CVE-2024-39954 [\[CVE json\]](./CVE-2024-39954.cve.json) [\[OSV json\]](./CVE-2024-39954.osv.json)



_Last updated: 2025-08-20T08:56:38.252Z_

### Affected

* Apache EventMesh Runtime from 1.6.0 through 1.11.0


### Description

CWE-918 Server-Side Request Forgery (SSRF) in eventmesh-runtime module in <span style="background-color: rgba(0, 0, 0, 0.06);">WebhookUtil.java</span> on windows\linux\mac os e.g. allows the attacker can abuse functionality on the server to read or update internal resources.<br>Users are recommended to upgrade to version 1.12.0 or use the master branch , which fixes this issue.

### References
* https://lists.apache.org/thread/v6c96zygqx8xc2k3n2d59mgnm5txhkon


### Credits
* Mak1r 808 <808mak1r@gmail.com> (reporter)


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
