---
title: Apache bRPC security advisories
description: Security information for Apache bRPC
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache bRPC? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## ServerOptions.pid_file may cause arbitrary code execution ## { #CVE-2023-31039 }

CVE-2023-31039 [\[CVE json\]](./CVE-2023-31039.cve.json) [\[OSV json\]](./CVE-2023-31039.osv.json)



_Last updated: 2023-05-08T08:57:09.633Z_

### Affected

* Apache bRPC from 0.9.0 before 1.5.0


### Description

<span style="background-color: rgb(255, 255, 255);">Security vulnerability&nbsp;</span>in Apache bRPC &lt;1.5.0 on all platforms allows attackers to execute arbitrary code via ServerOptions::pid_file.<br>An attacker that can influence the ServerOptions pid_file parameter with which the bRPC server is started can execute arbitrary code with the permissions of the bRPC process.<br><br>Solution:<br>1. upgrade to bRPC &gt;= 1.5.0, download link:&nbsp;<a target="_blank" rel="nofollow" href="https://dist.apache.org/repos/dist/release/brpc/1.5.0/">https://dist.apache.org/repos/dist/release/brpc/1.5.0/</a><br>2. If you are using an old version of bRPC and hard to upgrade, you can apply this patch:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/2218">https://github.com/apache/brpc/pull/2218</a>

### References
* https://lists.apache.org/thread/jqpttrqbc38yhckgp67xk399hqxnz7jn


## The builtin service rpcz page has an XSS attack vulnerability ## { #CVE-2023-45757 }

CVE-2023-45757 [\[CVE json\]](./CVE-2023-45757.cve.json) [\[OSV json\]](./CVE-2023-45757.osv.json)



_Last updated: 2023-10-16T08:01:36.036Z_

### Affected

* Apache bRPC from 0.9.0 through 1.6.0


### Description

<span style="background-color: rgb(255, 255, 255);">Security vulnerability </span>in Apache bRPC &lt;=1.6.0 on all platforms allows attackers to inject XSS code to the builtin rpcz page.<br>An attacker that can send http request to bRPC server with rpcz enabled can&nbsp;inject arbitrary XSS code to the builtin rpcz page.<br><br>Solution<span style="background-color: rgba(0, 0, 0, 0.2);">&nbsp;(choose one of three)</span>:<br>1. upgrade to bRPC &gt; 1.6.0, download link: <a target="_blank" rel="nofollow" href="https://dist.apache.org/repos/dist/release/brpc/1.6.1/">https://dist.apache.org/repos/dist/release/brpc/1.6.1/</a><br>2. If you are using an old version of bRPC and hard to upgrade, you can apply this patch:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/2411">https://github.com/apache/brpc/pull/2411</a><br>3. disable rpcz feature

### References
* https://lists.apache.org/thread/6syxv32fqgl30brfpttrk4rfsb983hl4


## HTTP request smuggling vulnerability ## { #CVE-2024-23452 }

CVE-2024-23452 [\[CVE json\]](./CVE-2024-23452.cve.json) [\[OSV json\]](./CVE-2024-23452.osv.json)



_Last updated: 2024-02-08T09:00:00.820Z_

### Affected

* Apache bRPC from 0.9.5 before 1.8.0


### Description

Request smuggling vulnerability in HTTP server in Apache bRPC 0.9.5~1.7.0 on all platforms allows attacker to smuggle request.<br><br><p><b>Vulnerability Cause Description：</b><u></u><u></u></p><p>The http_parser does not comply with the RFC-7230 HTTP 1.1 specification.</p><br><b>Attack&nbsp;scenario:<br></b><span style="background-color: rgb(255, 255, 255);">If a message is received with both a Transfer-Encoding and a Content-Length header field, such a message might indicate an attempt to perform request smuggling or response splitting.</span><br><p>One particular attack scenario is that a bRPC made http server on the backend receiving requests in one persistent connection from frontend server that uses TE to parse request with the logic that 'chunk' is contained in the TE field. in that case an attacker can smuggle a request into the connection to the backend server.&nbsp;<br></p><br><b>Solution:<br></b>You can choose one solution from below:<br><span style="background-color: rgb(255, 255, 255);">1. Upgrade bRPC to version 1.8.0, which fixes this issue. Download link: </span><a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/releases/tag/1.8.0">https://github.com/apache/brpc/releases/tag/1.8.0<br></a>2. Apply this patch:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/2518">https://github.com/apache/brpc/pull/2518</a><br><br>

### References
* https://github.com/apache/brpc/releases/tag/1.8.0
* https://github.com/apache/brpc/pull/2518
* https://lists.apache.org/thread/kkvdpwyr2s2yt9qvvxfdzon012898vxd


### Credits
* Pingtao Wei of 2012 Laboratories (finder)
* Ziyang Chen of 2012 Laboratories (finder)
* Haoran Zhi of 2012 Laboratories (finder)
* Hongpei Li of 2012 Laboratories (finder)
