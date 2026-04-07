---
title: Apache ZooKeeper security advisories
description: Security information for Apache ZooKeeper
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ZooKeeper? You can read more about the projects' security policy on their [security page](https://zookeeper.apache.org/security.html), and email your report to the [Apache ZooKeeper Security Team](mailto:security@zookeeper.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://zookeeper.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Sensitive information disclosure in client configuration handling ## { #CVE-2026-24308 }

CVE-2026-24308 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24308) [\[CVE json\]](./CVE-2026-24308.cve.json) [\[OSV json\]](./CVE-2026-24308.osv.json)



_Last updated: 2026-03-07T08:51:03.330Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.4
* Apache ZooKeeper from 3.8.0 through 3.8.5


### Description

<code>Improper handling of configuration values in ZKConfig in Apache ZooKeeper 3.8.5 and 3.9.4 on all platforms allows an attacker to expose sensitive information stored in client configuration in the client's logfile. Configuration values are exposed at INFO level logging rendering potential production systems affected by the issue.&nbsp;</code>Users are recommended to upgrade to version 3.8.6 or 3.9.5 which fixes this issue.

### References
* https://lists.apache.org/thread/qng3rtzv2pqkmko4rhv85jfplkyrgqdr


### Credits
* Youlong Chen <chenyoulong20g@ict.ac.cn> (reporter)


## Reverse-DNS fallback enables hostname verification bypass in ZooKeeper ZKTrustManager ## { #CVE-2026-24281 }

CVE-2026-24281 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24281) [\[CVE json\]](./CVE-2026-24281.cve.json) [\[OSV json\]](./CVE-2026-24281.osv.json)



_Last updated: 2026-03-07T08:50:30.345Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.4
* Apache ZooKeeper from 3.8.0 through 3.8.5


### Description

Hostname verification in Apache ZooKeeper ZKTrustManager falls back to reverse DNS (PTR) when IP SAN validation fails, allowing attackers who control or spoof PTR records to impersonate ZooKeeper servers or clients with a valid certificate for the PTR name. It's important to note that attacker must present a certificate which is trusted by ZKTrustManager which makes the attack vector harder to exploit. Users are recommended to upgrade to version 3.8.6 or 3.9.5, which fixes this issue by introducing a new configuration option to disable reverse DNS lookup in client and quorum protocols.<br><br><br><br><br><br>

### References
* https://lists.apache.org/thread/088ddsbrzhd5lxzbqf5n24yg0mwh9jt2


### Credits
* Nikita Markevich <markevich.nikita1@gmail.com> (reporter)


## Insufficient Permission Check in AdminServer Snapshot/Restore Commands ## { #CVE-2025-58457 }

CVE-2025-58457 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-58457) [\[CVE json\]](./CVE-2025-58457.cve.json) [\[OSV json\]](./CVE-2025-58457.osv.json)



_Last updated: 2025-09-24T09:29:42.132Z_

### Affected

* Apache ZooKeeper from 3.9.0 before 3.9.4


### Description

<p>Improper permission check in ZooKeeper AdminServer lets authorized clients to run snapshot and restore command with insufficient permissions.</p><p>This issue affects Apache ZooKeeper: from 3.9.0 before 3.9.4.</p><p>Users are recommended to upgrade to version 3.9.4, which fixes the issue.</p><p>The issue can be mitigated by disabling both commands (via <code>admin.snapshot.enabled</code> and <code>admin.restore.enabled</code>), disabling the whole AdminServer interface (via <code>admin.enableServer</code>), or ensuring that the root ACL does not provide open permissions. (Note that ZooKeeper ACLs are not recursive, so this does not impact operations on child nodes besides notifications from recursive watches.)</p>

### References
* https://lists.apache.org/thread/r5yol0kkhx2fzw22pxk1ozwm3oc6yxrx


### Credits
* Damien Diederen <ddiederen@apache.org> (reporter)


## Authentication bypass with IP-based authentication in Admin Server ## { #CVE-2024-51504 }

CVE-2024-51504 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-51504) [\[CVE json\]](./CVE-2024-51504.cve.json) [\[OSV json\]](./CVE-2024-51504.osv.json)



_Last updated: 2024-11-07T09:52:02.061Z_

### Affected

* Apache ZooKeeper from 3.9.0 before 3.9.3


### Description

When using IPAuthenticationProvider in ZooKeeper Admin Server there is a possibility of Authentication Bypass by Spoofing -- this only impacts IP based authentication implemented in ZooKeeper Admin Server. Default configuration of client's IP address detection in&nbsp;IPAuthenticationProvider, which uses HTTP request headers, is weak&nbsp;and allows an attacker to bypass authentication via spoofing client's IP address in request headers. Default configuration honors X-Forwarded-For HTTP header to read client's IP address. X-Forwarded-For request header is mainly used by proxy servers to identify the client and can be easily spoofed by an attacker pretending that the request comes from a different IP address. Admin Server commands, such as snapshot and restore arbitrarily can be executed on successful exploitation which could potentially lead to information leakage or service availability issues. Users are recommended to upgrade to version 3.9.3, which fixes this issue.

### References
* https://lists.apache.org/thread/b3qrmpkto5r6989qr61fw9y2x646kqlh


### Credits
* 4ra1n (reporter)
* Y4tacker (reporter)


## Information disclosure in persistent watcher handling ## { #CVE-2024-23944 }

CVE-2024-23944 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23944) [\[CVE json\]](./CVE-2024-23944.cve.json) [\[OSV json\]](./CVE-2024-23944.osv.json)



_Last updated: 2025-07-03T14:52:54.955Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.1
* Apache ZooKeeper from 3.8.0 through 3.8.3
* Apache ZooKeeper from 3.6.0 through 3.7.2


### Description

Information disclosure in persistent watchers handling in Apache ZooKeeper due to missing ACL check. It allows an attacker to monitor child znodes by attaching a persistent watcher (addWatch command) to a parent which the attacker has already access to. ZooKeeper server doesn't do ACL check when the persistent watcher is triggered and as a consequence, the full path of znodes that a watch event gets triggered upon is exposed to the owner of the watcher. It's important to note that only the path is exposed by this vulnerability, not the data of znode, but since znode path can contain sensitive information like user name or login ID, this issue is potentially critical.<br><br>Users are recommended to upgrade to version 3.9.2, 3.8.4 which fixes the issue.<br>

### References
* https://lists.apache.org/thread/96s5nqssj03rznz9hv58txdb2k1lr79k


### Credits
* 周吉安(寒泉) <zhoujian.zja@alibaba-inc.com> (reporter)


## Authorization bypass in SASL Quorum Peer Authentication ## { #CVE-2023-44981 }

CVE-2023-44981 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-44981) [\[CVE json\]](./CVE-2023-44981.cve.json) [\[OSV json\]](./CVE-2023-44981.osv.json)



_Last updated: 2023-10-11T11:55:41.759Z_

### Affected

* Apache ZooKeeper from 3.9.0 before 3.9.1
* Apache ZooKeeper from 3.8.0 through 3.8.2
* Apache ZooKeeper from 3.7.0 through 3.7.1
* Apache ZooKeeper before 3.7.0


### Description

Authorization Bypass Through User-Controlled Key vulnerability in Apache ZooKeeper. If SASL Quorum Peer authentication is enabled in ZooKeeper (<code>quorum.auth.enableSasl=</code><code>true)</code>, the authorization is done by verifying that the instance part in SASL authentication ID is listed in zoo.cfg server list. The instance part in SASL auth ID is optional and if it's missing, like 'eve@EXAMPLE.COM', the authorization check will be skipped.&nbsp;<span style="background-color: rgb(255, 255, 255);">As a result an arbitrary endpoint could join the cluster and begin propagating counterfeit changes to the leader, essentially giving it complete read-write access to the data tree.&nbsp;<span style="background-color: rgb(255, 255, 255);">Quorum Peer authentication is not enabled by default.</span><br><br></span><span style="background-color: var(--wht);">Users are recommended to upgrade to version 3.9.1, 3.8.3, 3.7.2, which fixes the issue.<br><br></span><span style="background-color: rgb(255, 255, 255);">Alternately ensure the ensemble election/quorum communication is protected by a firewall as this will mitigate the issue.<br><br><span style="background-color: rgb(255, 255, 255);">See the documentation for more details on correct cluster administration.</span></span><br>

### References
* https://lists.apache.org/thread/wf0yrk84dg1942z1o74kd8nycg6pgm5b


### Credits
* Damien Diederen <ddiederen@apache.org> (reporter)
