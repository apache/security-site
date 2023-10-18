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

CVE-2023-31039 [\[CVE json\]](./CVE-2023-31039.cve.json)

### Affected

* Apache bRPC from 0.9.0 before 1.5.0


### Description

<span style="background-color: rgb(255, 255, 255);">Security vulnerability&nbsp;</span>in Apache bRPC &lt;1.5.0 on all platforms allows attackers to execute arbitrary code via ServerOptions::pid_file.<br>An attacker that can influence the ServerOptions pid_file parameter with which the bRPC server is started can execute arbitrary code with the permissions of the bRPC process.<br><br>Solution:<br>1. upgrade to bRPC &gt;= 1.5.0, download link:&nbsp;<a target="_blank" rel="nofollow" href="https://dist.apache.org/repos/dist/release/brpc/1.5.0/">https://dist.apache.org/repos/dist/release/brpc/1.5.0/</a><br>2. If you are using an old version of bRPC and hard to upgrade, you can apply this patch:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/2218">https://github.com/apache/brpc/pull/2218</a>

### References
* https://lists.apache.org/thread/jqpttrqbc38yhckgp67xk399hqxnz7jn


## The builtin service rpcz page has an XSS attack vulnerability ## { #CVE-2023-45757 }

CVE-2023-45757 [\[CVE json\]](./CVE-2023-45757.cve.json)

### Affected

* Apache bRPC from 0.9.0 through 1.6.0


### Description

<span style="background-color: rgb(255, 255, 255);">Security vulnerability </span>in Apache bRPC &lt;=1.6.0 on all platforms allows attackers to inject XSS code to the builtin rpcz page.<br>An attacker that can send http request to bRPC server with rpcz enabled can&nbsp;inject arbitrary XSS code to the builtin rpcz page.<br><br>Solution<span style="background-color: rgba(0, 0, 0, 0.2);">&nbsp;(choose one of three)</span>:<br>1. upgrade to bRPC &gt; 1.6.0, download link: <a target="_blank" rel="nofollow" href="https://dist.apache.org/repos/dist/release/brpc/1.6.1/">https://dist.apache.org/repos/dist/release/brpc/1.6.1/</a><br>2. If you are using an old version of bRPC and hard to upgrade, you can apply this patch:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/2411">https://github.com/apache/brpc/pull/2411</a><br>3. disable rpcz feature

### References
* https://lists.apache.org/thread/6syxv32fqgl30brfpttrk4rfsb983hl4
