---
title: Apache ZooKeeper security advisories
description: Security information for Apache ZooKeeper
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache ZooKeeper? Send your report to the [Apache ZooKeeper Security Team](mailto:security@zookeeper.apache.org?subject=ZooKeeper).

You can read more about the security policy on:

- [Apache ZooKeeper security model](https://zookeeper.apache.org/security.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Operational log forgery via newline injection in EnsembleAuthenticationProvider ## { #CVE-2026-84501 }

CVE-2026-84501 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-84501) [\[CVE json\]](./CVE-2026-84501.cve.json) [\[OSV json\]](./CVE-2026-84501.osv.json)



_Last updated: 2026-09-16T09:28:09.271Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.5
* Apache ZooKeeper from 3.8.0 through 3.8.6


### Description

<p>An unauthenticated attacker can inject arbitrary fake log lines into Apache ZooKeeper's operational log by sending a crafted add_auth("ensemble", ...) request containing newline characters (\n). When the ensemble name doesn't match, EnsembleAuthenticationProvider.handleAuthentication() logs the raw, unsanitized name via LOG.warn(). Because SLF4J's {} placeholder preserves embedded newlines, the attacker can forge complete log entries — with arbitrary timestamps, log levels, class names, and messages — that are visually indistinguishable from genuine ZooKeeper log output.<br><span><br>This issue affects Apache ZooKeeper: from 3.9.0 through 3.9.5, from 3.8.0 through 3.8.6.<br></span><span><br>Users are recommended to upgrade to version 3.8.7 or 3.9.6, which fixes the issue.</span></p>

### References
* https://lists.apache.org/thread/ohby1g6zjt72p0w79rhbr41nczzvr33y


### Credits
* Youlong Chen Institute of Computing Technology <chenyoulong20g@ict.ac.cn> (finder)


## Audit log injection via unsanitized output from multiple sources ## { #CVE-2026-84439 }

CVE-2026-84439 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-84439) [\[CVE json\]](./CVE-2026-84439.cve.json) [\[OSV json\]](./CVE-2026-84439.osv.json)



_Last updated: 2026-09-16T09:27:45.211Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.5
* Apache ZooKeeper from 3.8.0 through 3.8.6


### Description

<p>When audit logging is enabled (<code>zookeeper.audit.enable=true</code>), an unauthenticated attacker can inject arbitrary fields into Apache ZooKeeper's audit log by sending a digest authentication request with tab characters (<code>\t</code>) embedded in the username. Because the audit log uses tab-separated&nbsp;<code>key=value</code>&nbsp;format, the injected tabs are parsed as legitimate field separators, allowing the attacker to spoof audit results (e.g., injecting&nbsp;<code>result=success</code>), forge operation types, and corrupt forensic evidence.<br><span><br>A log injection vulnerability in Apache ZooKeeper allows a client that can call&nbsp;</span><code>setACL</code><span>&nbsp;</span><span>to inject forged key-value fields into</span><span>&nbsp;</span><code>zookeeper_audit.log</code><span>. When audit logging is enabled, the server serializes attacker-controlled digest ACL ids into the</span><span>&nbsp;</span><code>acl=</code><span>&nbsp;</span><span>audit field without escaping tab characters. Because audit events are emitted as tab-separated</span><span>&nbsp;</span><code>key=value</code><span>&nbsp;</span><span>records, a crafted ACL id can make one successful</span><span>&nbsp;</span><code>setAcl</code><span>&nbsp;</span><span>event appear to contain forged fields such as</span><span>&nbsp;</span><code>operation=delete</code><span>&nbsp;</span><span>and</span><span>&nbsp;</span><code>znode=/forged</code><span>. This undermines the integrity of downstream audit parsing, alerting, and incident response.</span><span><br></span><span><br>This issue affects Apache ZooKeeper: from 3.9.0 through 3.9.5, from 3.8.0 through 3.8.6.<br></span><span><br>Users are recommended to upgrade to version 3.9.6 or 3.8.7, which fixes the issue.</span></p>

### References
* https://lists.apache.org/thread/b7qnjvqjh393l0j07tmnb5ggg40sx3m6


### Credits
* Youlong Chen Institute of Computing Technology <chenyoulong20g@ict.ac.cn> (reporter)


## Missing ACL check on deleteContainer opcode allows unauthorized deletion of any empty persistent/container znode ## { #CVE-2026-79993 }

CVE-2026-79993 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-79993) [\[CVE json\]](./CVE-2026-79993.cve.json) [\[OSV json\]](./CVE-2026-79993.osv.json)



_Last updated: 2026-09-16T09:27:21.440Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.5
* Apache ZooKeeper from 3.8.0 through 3.8.6


### Description

<p><span>The `deleteContainer` opcode (0x14/20) is processed without verifying the caller's ACL permissions, allowing any authenticated client to delete specific znodes in the data tree regardless of the ACL restrictions on the znode or its parent. This opcode is considered internal-only and the official client doesn't have API for it, but a&nbsp;</span><span>client that can open a plain TCP session on the ZooKeeper client port (2181 by default)&nbsp;</span><span>- with NO authentication and NO ACL permissions - can delete any</span><span>&nbsp;empty persistent znode (including regular persistent nodes, container&nbsp;</span><span>nodes, and TTL nodes) by issuing the raw protocol OpCode deleteContainer (20).&nbsp;</span><span>The deleteContainer request path completely skips both the session check and&nbsp;</span><span>the DELETE ACL check that are enforced by the regular delete (OpCode 2) path.&nbsp;</span><span>This is an authorization bypass / ACL enforcement bug.<br></span><span><br>This issue affects Apache ZooKeeper: from 3.9.0 through 3.9.5, from 3.8.0 through 3.8.6.<br></span><span><br>Users are recommended to upgrade to version 3.9.6 or 3.8.7, which fixes the issue.</span></p>

### References
* https://lists.apache.org/thread/9cw3rmrzhqpct26v8j18fy41bghlq8y5


### Credits
* K <sec-reports@outlook.com> (reporter)
* z f <tinkerzf@gmail.com> (reporter)
* 布豪 <1958304602@qq.com> (finder)


## Improper validation of certificate with host mismatch in FIPS mode ## { #CVE-2026-59969 }

CVE-2026-59969 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-59969) [\[CVE json\]](./CVE-2026-59969.cve.json) [\[OSV json\]](./CVE-2026-59969.osv.json)



_Last updated: 2026-09-16T09:26:59.171Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.5
* Apache ZooKeeper from 3.8.0 through 3.8.6


### Description

<p>Apache ZooKeeper quorum TLS fails to enforce peer hostname verification in FIPS-mode deployments. When <code>sslQuorum=true</code>, <code>zookeeper.fips-mode=true</code>, <code>ssl.quorum.hostnameVerification=true</code>, and <code>ssl.quorum.clientHostnameVerification=true</code>&nbsp;are enabled, the Java <code>SSLSocket</code>&nbsp;quorum path accepts a CA-trusted peer certificate whose SAN does not match the connected host. A malicious or misissued peer certificate can therefore join quorum traffic, participate in leader election, and enter replication flows.</p><p>Users are recommended to upgrade to version 3.8.7 or 3.9.6, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/qf9kwsgtgbgtvwls6f41281846xg0rss


### Credits
* Erichen <chenyoulong20g@ict.ac.cn> (reporter)


## Information disclosure via SetWatches reconnect replay ## { #CVE-2026-59739 }

CVE-2026-59739 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-59739) [\[CVE json\]](./CVE-2026-59739.cve.json) [\[OSV json\]](./CVE-2026-59739.osv.json)



_Last updated: 2026-09-16T09:26:36.333Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.5
* Apache ZooKeeper from 3.8.0 through 3.8.6


### Description

Information disclosure via SetWatches reconnect replay in Apache ZooKeeper due to missing ACL check.&nbsp;An attacker can discover ACL-restricted paths by registering exists-watches on non-existent paths, then reconnecting after the paths are created with restricted ACLs. Issue is caused by incomplete fix for&nbsp;CVE-2024-23944 (ZOOKEEPER-4799).&nbsp;The fix added ACL checking to WatchManager.triggerWatch(). However, DataTree.setWatches() — the SetWatches/SetWatches2 reconnect replay handler — still calls watcher.process(event) with null ACL, bypassing the check entirely. It's important to note that only the path is exposed by this vulnerability, not the data of znode, but since znode path can contain sensitive information like user name or login ID, this issue is potentially critical.<br><br>Users are recommended to upgrade to version 3.9.6, 3.8.7 which fixes the issue.

### References
* https://lists.apache.org/thread/v0lrwsbdxvx6w67p3z7fxf3hzyncq55l


### Credits
* NGUYEN HONG QUAN <hongquanvp11@gmail.com> (reporter)
* n0mi1k <nomilksec@gmail.com> (reporter)


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


## Unbounded recursion in snapshot serialization allows a client to render the server unrecoverable ## { #CVE-2026-115448 }

CVE-2026-115448 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-115448) [\[CVE json\]](./CVE-2026-115448.cve.json) [\[OSV json\]](./CVE-2026-115448.osv.json)



_Last updated: 2026-11-04T10:45:42.503Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.7
* Apache ZooKeeper from 3.8.0 through 3.8.8


### Description

Uncontrolled recursion in Apache ZooKeeper. The server serializes its data tree to a snapshot by recursing one stack frame per znode level, with no depth bound. A client permitted to create znodes (the default root ACL is open) can build a chain of nested znodes deep enough that taking a snapshot exhausts the JVM stack and kills the snapshot thread; sizes stay within jute.maxbuffer, so existing limits do not prevent it. This is a denial of service that becomes persistent: on restart the server rebuilds the deep tree from its transaction log and fails again while taking the startup snapshot, so it does not return to service, and recovery can entail data loss. The same log affects a leader and its followers, so it can spread across an ensemble.<br><br>This issue affects Apache ZooKeeper 3.8.0 through 3.8.7 and 3.9.0 through 3.9.6. Users are recommended to upgrade to 3.8.8 or 3.9.7, which fix the issue. As a workaround, use ACLs and authentication to restrict znode creation rather than relying on the default open root ACL.

### References
* https://lists.apache.org/thread.html/p892jm8qw0zqv8z152lpokyt7mp6gc41


### Credits
* Sai Sreewathsa Kovalluri, Shon Babu, and Kannan K of Innspark Solutions (https://innspark.in/) (reporter)
* Prasath Jayasundar & PayPal Cyber Security Team (reporter)


## Denial of service through unbounded memory allocation in multiRead request handling ## { #CVE-2026-100302 }

CVE-2026-100302 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-100302) [\[CVE json\]](./CVE-2026-100302.cve.json) [\[OSV json\]](./CVE-2026-100302.osv.json)



_Last updated: 2026-11-04T10:46:18.911Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.6
* Apache ZooKeeper from 3.8.0 through 3.8.7


### Description

<p>Allocation of Resources Without Limits or Throttling in the <code>multiRead</code> request handler of Apache ZooKeeper allows a remote attacker to crash the server (denial of service) with a single small request.<br><span><br>The </span><code>multiRead</code><span> handler places no limit on the number of bundled read operations or on the cumulative size of the response it builds in memory. Because each operation's result is fully materialized and retained before serialization, a request that is small on the wire — within the </span><code>jute.maxbuffer</code><span> limit — but that references a large znode many times can force the server to allocate far more heap than the request size implies, exhausting the JVM heap and terminating the server with an </span><code>OutOfMemoryError</code><span>. Neither </span><code>jute.maxbuffer</code><span> nor </span><code>largeRequestMaxBytes</code><span> prevents this, as both bound only the inbound request, not the response.<br></span><span><br>This issue affects Apache ZooKeeper from 3.7.0 through 3.9.6. Users are recommended to upgrade to version 3.9.7, which enforces configurable limits on the multiRead operation count and cumulative response size.</span></p>

### References
* https://lists.apache.org/thread.html/gj2vxwx8myq31js6tvb7bgls4nnxohj7


## Unauthenticated persistent denial of service via unvalidated quota-node data and paths crashing the transaction-apply thread ## { #CVE-2026-100300 }

CVE-2026-100300 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-100300) [\[CVE json\]](./CVE-2026-100300.cve.json) [\[OSV json\]](./CVE-2026-100300.osv.json)



_Last updated: 2026-11-04T10:45:13.777Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.6
* Apache ZooKeeper from 3.8.0 through 3.8.7


### Description

Improper handling of exceptional conditions in the quota subsystem of Apache ZooKeeper allows an attacker able to write under the <code>/zookeeper/quota</code> subtree — unauthenticated on default deployments, where that subtree is world-writable — to crash the server's critical request-processing thread and render the on-disk data directory permanently unbootable.<br><br>This issue affects Apache ZooKeeper up to and including 3.9.6. Users are recommended to upgrade to version 3.8.8 or 3.9.7, which fixes the issue.

### References
* https://lists.apache.org/thread.html/09pgg7rcpzz44noxgtvpzstwt8fmvsb0


### Credits
* cunyi li <xiaoheihei1107@gmail.com> (reporter)


## SASL authorization bypass on the client port through a client-supplied authorization ID ## { #CVE-2026-100252 }

CVE-2026-100252 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-100252) [\[CVE json\]](./CVE-2026-100252.cve.json) [\[OSV json\]](./CVE-2026-100252.osv.json)



_Last updated: 2026-11-04T10:44:16.258Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.6
* Apache ZooKeeper from 3.8.0 through 3.8.7


### Description

<p>Improper Authorization vulnerability in Apache ZooKeeper.<br><span><br>When SASL authentication is enabled on the client port, the server's SASL callback handler grants every authorization identity (authzid) that a client requests, without checking it against the principal the client authenticated as. The server then tries to replace the requested identity with a canonical form of the authenticated principal, derived from the </span><code>zookeeper.security.auth_to_local</code><span> rules. If no rule applies to the principal, canonicalization fails and the error is only logged. The client-requested authzid then becomes the session's SASL identity for all ACL checks.<br></span><span><br>An authenticated client whose principal is not covered by the </span><code>auth_to_local</code><span> rules can therefore claim any SASL identity. With the default rules, this includes any Kerberos principal from a realm other than the server's default realm, such as a principal from a cross-realm trusted realm. The client then gets the permissions granted to that identity in </span><code>sasl</code><span> ACLs. If the requested identity matches a configured </span><code>zookeeper.superUser</code><span>, it gets superuser access to the whole data tree.<br></span><span><br></span><span>Users are recommended to upgrade to version 3.8.8 or 3.9.7, which fixes the issue.</span></p>

### References
* https://lists.apache.org/thread.html/81rdyqlmlp3dtkkqgp8t5080g3b9r2pj


### Credits
* cunyi li <xiaoheihei1107@gmail.com> (reporter)
* Prasath Jayasundar & PayPal Cyber Security Team (reporter)


## ACL enforcement bypass allows unauthorized operations to commit after an ACL revocation ## { #CVE-2026-100235 }

CVE-2026-100235 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-100235) [\[CVE json\]](./CVE-2026-100235.cve.json) [\[OSV json\]](./CVE-2026-100235.osv.json)



_Last updated: 2026-11-04T10:43:19.921Z_

### Affected

* Apache ZooKeeper from 3.9.0 through 3.9.6
* Apache ZooKeeper from 3.8.0 through 3.8.7


### Description

<p>Incorrect authorization due to a time-of-check to time-of-use (TOCTOU) race condition in the <code>setACL</code> request handling of Apache ZooKeeper.<br><span><br>When a node's ACL is changed via </span><code>setACL</code><span>, the pending change is not published to the server's outstanding change record for that node. Any request that is prepared (and authorized) after the </span><code>setACL</code><span> is submitted but before it commits is therefore checked against the previous, pre-revocation ACL, yet is applied to the data tree after the ACL change has taken effect. A client that currently holds a permission can use this window to perform operations requiring that permission through and after its revocation — for example, committing writes or deletes after losing write access, or re-granting itself full permissions, which persistently defeats the revocation. In deployments transitioning from the default </span><code>OPEN_ACL_UNSAFE</code><span> ACL to a restrictive ACL, any unauthenticated client can exploit this during the transition.<br></span><span><br>This issue affects Apache ZooKeeper up to and including 3.9.6. Users are recommended to upgrade to version 3.8.8 or 3.9.7, which fixes the issue.</span></p>

### References
* https://lists.apache.org/thread.html/r40gp594o64mycwybc3v9dtvrm0vos0l


### Credits
* cunyi li <xiaoheihei1107@gmail.com> (reporter)


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
