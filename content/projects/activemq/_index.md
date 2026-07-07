---
title: Apache ActiveMQ security advisories
description: Security information for Apache ActiveMQ
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ActiveMQ? You can read more about the projects' security policy on their [security page](https://github.com/apache/activemq/security/policy), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://github.com/apache/activemq/security/policy). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Temporary destination ownership takeover ## { #CVE-2026-54475 }

CVE-2026-54475 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-54475) [\[CVE json\]](./CVE-2026-54475.cve.json) [\[OSV json\]](./CVE-2026-54475.osv.json)



_Last updated: 2026-06-30T09:48:27.404Z_

### Affected

* Apache ActiveMQ Broker before 5.19.8
* Apache ActiveMQ Broker from 6.0.0 before 6.2.7
* Apache ActiveMQ All before 5.19.8
* Apache ActiveMQ All from 6.0.0 before 6.2.7
* Apache ActiveMQ before 5.19.8
* Apache ActiveMQ from 6.0.0 before 6.2.7


### Description

<p>Missing Authorization vulnerability in Apache ActiveMQ Broker, Apache ActiveMQ All, Apache ActiveMQ.</p>Apache ActiveMQ Classic temporary destinations are expected to be isolated to the connection that created them. The isolation can be broken as this is only checked in the client, allowing a&nbsp;different connection to consume from another connection's temporary<br>destination.<br><p>This issue affects Apache ActiveMQ Broker: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ All: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ: before 5.19.8, from 6.0.0 before 6.2.7.</p><p>Users are recommended to upgrade to version 6.2.7, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/85f3q7mkh71y7qwyn6wvgw0bw4jl06ys


### Credits
* Leon Johnson (github: lokerxx) (finder)


## Unbounded memory allocation in OpenWire property unmarshalling ## { #CVE-2026-53917 }

CVE-2026-53917 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-53917) [\[CVE json\]](./CVE-2026-53917.cve.json) [\[OSV json\]](./CVE-2026-53917.osv.json)



_Last updated: 2026-06-30T09:49:16.202Z_

### Affected

* Apache ActiveMQ before 5.19.8
* Apache ActiveMQ from 6.0.0 before 6.2.7
* Apache ActiveMQ All before 5.19.8
* Apache ActiveMQ All from 6.0.0 before 6.2.7
* Apache ActiveMQ Client before 5.19.8
* Apache ActiveMQ Client from 6.0.0 before 6.2.7
* Apache ActiveMQ Broker before 5.19.8
* Apache ActiveMQ Broker from 6.0.0 before 6.2.7


### Description

<p>Memory Allocation with Excessive Size Value vulnerability in Apache ActiveMQ, Apache ActiveMQ All, Apache ActiveMQ Client, Apache ActiveMQ Broker.</p>An authenticated user can cause a broker DoS by sending a crafted OpenWire Message with a large encoded size value for the map. <span style="background-color: rgb(255, 255, 255);">OpenWire message property maps are unmarshaled without size validation</span>&nbsp;which can trigger OOM and crash the broker.<br><p>This issue affects Apache ActiveMQ: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ All: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ Client: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ Broker: before 5.19.8, from 6.0.0 before 6.2.7.</p><p>Users are recommended to upgrade to version 6.2.7 or 5.19.8, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/grrd1mwgkgblqjbwkkq6dvmdxd9ov2dx


### Credits
* tonghuaroot (finder)


## Unbounded header buffer in STOMP NIO codec ## { #CVE-2026-53916 }

CVE-2026-53916 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-53916) [\[CVE json\]](./CVE-2026-53916.cve.json) [\[OSV json\]](./CVE-2026-53916.osv.json)



_Last updated: 2026-06-30T09:49:54.244Z_

### Affected

* Apache ActiveMQ before 5.19.8
* Apache ActiveMQ from 6.0.0 before 6.2.7
* Apache ActiveMQ All before 5.19.8
* Apache ActiveMQ All from 6.0.0 before 6.2.7
* Apache ActiveMQ Stomp before 5.19.8
* Apache ActiveMQ Stomp from 6.0.0 before 6.2.7


### Description

<p>Memory Allocation with Excessive Size Value vulnerability in Apache ActiveMQ, Apache ActiveMQ All, Apache ActiveMQ Stomp.<br></p>An unauthenticated client that opens a STOMP NIO connection can send header bytes that never terminate which makes the broker buffer them without limit,&nbsp;exhausting&nbsp;the JVM heap. <br><p>This issue affects Apache ActiveMQ: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ All: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ Stomp: before 5.19.8, from 6.0.0 before 6.2.7.</p><p>Users are recommended to upgrade to version 6.2.7 or 5.19.8, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/07hjsj88hqgsb7vvg6ttsj56ts9vjs5n


### Credits
* tonghuaroot (finder)


## Stored XSS via Unescaped values in ActiveMQ Web Console ## { #CVE-2026-52760 }

CVE-2026-52760 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-52760) [\[CVE json\]](./CVE-2026-52760.cve.json) [\[OSV json\]](./CVE-2026-52760.osv.json)



_Last updated: 2026-06-30T09:50:28.410Z_

### Affected

* Apache ActiveMQ before 5.19.8
* Apache ActiveMQ from 6.0.0 before 6.2.7
* Apache ActiveMQ Web Console before 5.19.8
* Apache ActiveMQ Web Console from 6.0.0 before 6.2.7


### Description

<p>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache ActiveMQ, Apache ActiveMQ Web Console.</p>The browse page in the web console renders a message Id directly without sanitization. This allows an authenticated producer to send a&nbsp;message with a JMS message ID that has been&nbsp;crafted to contain HTML/JavaScript such that when&nbsp;an administrator browses the queue in the Web Console, the payload executes in their browser.<br><p>This issue affects Apache ActiveMQ: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ Web Console: before 5.19.8, from 6.0.0 before 6.2.7.</p><p>Users are recommended to upgrade to version 6.2.7 or 5.19.8, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/d3mhyo2116nomz2lwxppyy4pclvdxq3n


### Credits
* Biswajeet Ray (finder)


## Pre-authentication OpenWire DoS following fix for CVE-2026-49270 ## { #CVE-2026-50750 }

CVE-2026-50750 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50750) [\[CVE json\]](./CVE-2026-50750.cve.json) [\[OSV json\]](./CVE-2026-50750.osv.json)



_Last updated: 2026-06-30T09:51:55.636Z_

### Affected

* Apache ActiveMQ Broker from 5.19.7 before 5.19.8
* Apache ActiveMQ Broker from 6.2.6 before 6.2.7
* Apache ActiveMQ from 5.19.7 before 5.19.8
* Apache ActiveMQ from 6.2.6 before 6.2.7
* Apache ActiveMQ All from 5.19.7 before 5.19.8
* Apache ActiveMQ All from 6.2.6 before 6.2.7


### Description

<p>Denial of Service via Out of Memory vulnerability in Apache ActiveMQ Broker, Apache ActiveMQ, Apache ActiveMQ All.</p>Following the fix for  CVE-2026-49270&nbsp;an unauthenticated attacker can now cause broker OOM by sending an repeated BrokerInfo commands without sending&nbsp;a ConnectionInfo, until the broker will crash with OOM.<br><p>This issue affects Apache ActiveMQ Broker: from 5.19.7 before 5.19.8, from 6.2.6 before 6.2.7; Apache ActiveMQ: from 5.19.7 before 5.19.8, from 6.2.6 before 6.2.7; Apache ActiveMQ All: from 5.19.7 before 5.19.8, from 6.2.6 before 6.2.7.</p><p>Users are recommended to upgrade to version 6.2.7, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/nhkmbdym61yp6wwy0dny8w1p46sm87kr


## Pre-authentication OpenWire memory-allocation DoS during wire format negotiation ## { #CVE-2026-50734 }

CVE-2026-50734 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50734) [\[CVE json\]](./CVE-2026-50734.cve.json) [\[OSV json\]](./CVE-2026-50734.osv.json)



_Last updated: 2026-06-30T09:53:02.137Z_

### Affected

* Apache ActiveMQ Client before 5.19.8
* Apache ActiveMQ Client from 6.0.0 before 6.2.7
* Apache ActiveMQ before 5.19.8
* Apache ActiveMQ from 6.0.0 before 6.2.7
* Apache ActiveMQ All before 5.19.8
* Apache ActiveMQ All from 6.0.0 before 6.2.7


### Description

<p>Memory Allocation with Excessive Size Value vulnerability in Apache ActiveMQ Client, Apache ActiveMQ, Apache ActiveMQ All.</p><span style="background-color: rgb(255, 255, 255);">An unauthenticated network attacker can cause a broker DoS by sending a crafted WireFormatInfo frame with a malicious large size value. The value is not validate and causes the broker to attempt allocation during pre-auth negotiation which can trigger OOM and crash the broker.</span><br><p>This issue affects Apache ActiveMQ Client: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ All: before 5.19.8, from 6.0.0 before 6.2.7.</p><p>Users are recommended to upgrade to version 6.2.7 or 5.19.8, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/nxso951fnvf72qf9m475mpz4yf931xk0


### Credits
* Andrej Tomci (finder)


## Authenticated web users retain admin access by default in the Web Console ## { #CVE-2026-49877 }

CVE-2026-49877 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49877) [\[CVE json\]](./CVE-2026-49877.cve.json) [\[OSV json\]](./CVE-2026-49877.osv.json)



_Last updated: 2026-06-30T09:53:41.777Z_

### Affected

* Apache ActiveMQ before 5.19.8
* Apache ActiveMQ from 6.0.0 before 6.2.7


### Description

<p>Improper Authorization vulnerability in Apache ActiveMQ.</p><span style="background-color: rgb(255, 255, 255);">An authenticated low-privilege Web Console user by default can access /admin/* paths in the Web Console. The default Jetty settings incorrectly did not limit those paths to only admins.</span><br><p>This issue affects Apache ActiveMQ: before 5.19.8, from 6.0.0 before 6.2.7.</p><p>Users are recommended to upgrade to version 6.2.7 or 5.19.8, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/w82vtc3q02j5ot94tnyy1197y3wb98hl


### Credits
* Leon Johnson (github: lokerxx) (finder)


## LdapNetworkConnector instantiates denied transports and a remote-properties broker ## { #CVE-2026-49434 }

CVE-2026-49434 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49434) [\[CVE json\]](./CVE-2026-49434.cve.json) [\[OSV json\]](./CVE-2026-49434.osv.json)



_Last updated: 2026-06-30T09:55:28.407Z_

### Affected

* Apache ActiveMQ Broker before 5.19.8
* Apache ActiveMQ Broker from 6.0.0 before 6.2.7
* Apache ActiveMQ before 5.19.8
* Apache ActiveMQ from 6.0.0 before 6.2.7
* Apache ActiveMQ All before 5.19.8
* Apache ActiveMQ All from 6.0.0 before 6.2.7


### Description

<p>Improper Input Validation vulnerability in Apache ActiveMQ Broker, Apache ActiveMQ, Apache ActiveMQ All.</p><span style="background-color: rgb(255, 255, 255);">An attacker that has access to publish or modify entries in LDAP that match the configured </span><span style="background-color: rgb(255, 255, 255);">searchBase and searchFilter can instantiate denied transports inside the broker JVM. This can be used to <span style="background-color: rgb(255, 255, 255);">fetch an attacker URL and spawn a </span><span style="background-color: rgb(255, 255, 255);">second BrokerService inside the same JVM.</span></span><br><p>This issue affects Apache ActiveMQ Broker: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ All: before 5.19.8, from 6.0.0 before 6.2.7.<br></p><p>Users are recommended to upgrade to version 6.2.7 or 5.19.8, which fixes the issue.</p><p></p>

### References
* https://lists.apache.org/thread/hcjh7kdk4l85tb9ksmvcnkhso1ngj50o


### Credits
* @Add Content (finder)


## STOMP negative content-length enables denial of service ## { #CVE-2026-49432 }

CVE-2026-49432 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49432) [\[CVE json\]](./CVE-2026-49432.cve.json) [\[OSV json\]](./CVE-2026-49432.osv.json)



_Last updated: 2026-06-30T09:54:37.498Z_

### Affected

* Apache ActiveMQ before 5.19.8
* Apache ActiveMQ from 6.0.0 before 6.2.7
* Apache ActiveMQ All before 5.19.8
* Apache ActiveMQ All from 6.0.0 before 6.2.7
* Apache ActiveMQ Stomp before 5.19.8
* Apache ActiveMQ Stomp from 6.0.0 before 6.2.7


### Description

<p>Improper Input Validation vulnerability in Apache ActiveMQ, Apache ActiveMQ All, Apache ActiveMQ Stomp.</p><span style="background-color: rgb(255, 255, 255);">A remote unauthenticated peer that can reach an exposed STOMP connector can trigger denial-of-service behavior by sending a negative content-length. For the NIO STOMP transport, an attacker can keep streaming body bytes and grow the per-connection command buffer beyond configured limits to cause OOM. For the blocking STOMP protocol, an error will instead force abnormal transport exception handling for the affected connection and closure.</span><br><p>This issue affects Apache ActiveMQ: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ All: before 5.19.8, from 6.0.0 before 6.2.7; Apache ActiveMQ Stomp: before 5.19.8, from 6.0.0 before 6.2.7.<br></p><p></p><p>Users are recommended to upgrade to version 6.2.7 or 5.19.8, which fixes the issue.</p><p></p>

### References
* https://lists.apache.org/thread/fsjb26605syqr8xks249h8gkp86t55d2


### Credits
* Youngjoon Kim (finder)


## Durable Subscription Disclosure via Crafted BrokerInfo (OpenWire) ## { #CVE-2026-49270 }

CVE-2026-49270 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49270) [\[CVE json\]](./CVE-2026-49270.cve.json) [\[OSV json\]](./CVE-2026-49270.osv.json)



_Last updated: 2026-06-01T07:19:32.927Z_

### Affected

* Apache ActiveMQ Broker from 5.14.0 before 5.19.7
* Apache ActiveMQ Broker from 6.0.0 before 6.2.6
* Apache ActiveMQ from 5.14.0 before 5.19.7
* Apache ActiveMQ from 6.0.0 before 6.2.6
* Apache ActiveMQ All from 5.14.0 before 5.19.7
* Apache ActiveMQ All from 6.0.0 before 6.2.6


### Description

<p>Exposure of Sensitive Information Through Metadata vulnerability in Apache ActiveMQ Broker, Apache ActiveMQ, Apache ActiveMQ All.</p><span style="background-color: rgb(255, 255, 255);">Brokers that are configured with a network connector with syncDurableSubs set to true, are vulnerable to an unauthenticated attacker who can receive a list of all durable topic subscriptions in the broker,&nbsp;</span><span style="background-color: rgb(255, 255, 255);">including client identifiers, subscription names, topic destinations, and&nbsp;</span><span style="background-color: rgb(255, 255, 255);">JMS selector expressions, by sending a BrokerInfo command. The broker incorrectly responds without first ensuring the connection is authenticated.</span><br><p>This issue affects Apache ActiveMQ Broker: before 5.19.7, from 6.0.0 before 6.2.6; Apache ActiveMQ: before 5.19.7, from 6.0.0 before 6.2.6; Apache ActiveMQ All: before 5.19.7, from 6.0.0 before 6.2.6.</p><p>Users are recommended to upgrade to version 6.2.6 or 5.19.7, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/k3233c1x506z3w7x4z0dqvd86d4v2fr2


### Credits
* Basel Khaled (finder)


## Authenticated low-privilege Web users retain Jolokia broker-management capability by default ## { #CVE-2026-49157 }

CVE-2026-49157 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49157) [\[CVE json\]](./CVE-2026-49157.cve.json) [\[OSV json\]](./CVE-2026-49157.osv.json)



_Last updated: 2026-06-01T07:20:09.394Z_

### Affected

* Apache ActiveMQ before 5.19.7
* Apache ActiveMQ from 6.0.0 before 6.2.6


### Description

<p>Incorrect Default Permissions vulnerability in Apache ActiveMQ.</p><p>This issue affects Apache ActiveMQ: before 5.19.7, from 6.0.0 before 6.2.6.</p><p>The default Jolokia authorization settings granted&nbsp;<span style="background-color: rgb(255, 255, 255);">non-admin (low-privilege) web-login accounts</span>&nbsp;access to Jolokia operations which allowed executing broker management operations meant for admins such as <code>addQueue</code> and <code>removeQueue</code>.</p><p>Users are recommended to upgrade to version 6.2.6 or 5.19.7, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/rrcsf6s90hj4tdh89nvkko75q5505rj8


### Credits
* Leon Johnson (github: lokerxx) (finder)


## Incomplete authorization during destination removal ## { #CVE-2026-46605 }

CVE-2026-46605 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46605) [\[CVE json\]](./CVE-2026-46605.cve.json) [\[OSV json\]](./CVE-2026-46605.osv.json)



_Last updated: 2026-06-01T07:21:11.500Z_

### Affected

* Apache ActiveMQ Broker before 5.19.7
* Apache ActiveMQ Broker from 6.0.0 before 6.2.6
* Apache ActiveMQ All before 5.19.7
* Apache ActiveMQ All from 6.0.0 before 6.2.6
* Apache ActiveMQ before 5.19.7
* Apache ActiveMQ from 6.0.0 before 6.2.6


### Description

<p>Incomplete authorization by Apache ActiveMQ server before versions v6.2.6 and v5.19.7 allows authenticated connections to remove existing destinations with proper permissions.</p><p>This issue affects Apache ActiveMQ Broker: before 5.19.7, from 6.0.0 before 6.2.6; Apache ActiveMQ All: before 5.19.7, from 6.0.0 before 6.2.6; Apache ActiveMQ: before 5.19.7, from 6.0.0 before 6.2.6.</p><p>Users are recommended to upgrade to version v6.2.6 or v5.19.7, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/l4lxgr2s73g9pb218f180psfyskf8ldm


### Credits
* Leon Johnson (github: lokerxx) (finder)


## Jolokia `addNetworkConnector` Discovery Wrapper Bypass ## { #CVE-2026-45505 }

CVE-2026-45505 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45505) [\[CVE json\]](./CVE-2026-45505.cve.json) [\[OSV json\]](./CVE-2026-45505.osv.json)



_Last updated: 2026-06-01T07:22:30.266Z_

### Affected

* Apache ActiveMQ Broker before 5.19.7
* Apache ActiveMQ Broker from 6.0.0 before 6.2.6
* Apache ActiveMQ All before 5.19.7
* Apache ActiveMQ All from 6.0.0 before 6.2.6
* Apache ActiveMQ before 5.19.7
* Apache ActiveMQ from 6.0.0 before 6.2.6


### Description

<p>Improper Input Validation, Improper Control of Generation of Code ('Code Injection') vulnerability in Apache ActiveMQ Broker, Apache ActiveMQ All, Apache ActiveMQ.<br></p><span style="background-color: rgb(255, 255, 255);">Non-parenthesized discovery wrappers such as `masterslave:vm://...,...`
and `static:vm://...` incorrectly pass validation allowing bypass of fix in&nbsp;<span style="background-color: rgb(255, 255, 255);">CVE-2026-34197.&nbsp;<br></span></span><br>Original description from&nbsp;CVE-2026-34197.<br><br><span style="background-color: rgb(255, 255, 255);">Apache ActiveMQ exposes the Jolokia JMX-HTTP bridge at /api/jolokia/ on the web console. The default Jolokia access policy permits exec operations on all ActiveMQ MBeans (org.apache.activemq:*), including BrokerService.addNetworkConnector(String) and BrokerService.addConnector(String).&nbsp;</span><span style="background-color: rgb(255, 255, 255);">An authenticated attacker can invoke these operations with a crafted discovery UR that triggers the VM transport's brokerConfig parameter to load a remote Spring XML application context using ResourceXmlApplicationContext. Because Spring's ResourceXmlApplicationContext instantiates all singleton beans before the BrokerService validates the configuration, arbitrary code execution occurs on the broker's JVM through bean factory methods such as Runtime.exec(). </span><br><p>This issue affects Apache ActiveMQ Broker: before 5.19.7, from 6.0.0 before 6.2.6; Apache ActiveMQ All: before 5.19.7, from 6.0.0 before 6.2.6; Apache ActiveMQ: before 5.19.7, from 6.0.0 before 6.2.6.</p><p>Users are recommended to upgrade to version 5.19.7 or 6.2.6, which fixes the issue.</p>

### References
* https://nvd.nist.gov/vuln/detail/CVE-2026-34197
* https://lists.apache.org/thread/7n97nddyw96w6ykldjv1h40jx86xdo0w


### Credits
* lokerxx (finder)


## Remote Code Execution via Jolokia addNetworkConnector ## { #CVE-2026-42588 }

CVE-2026-42588 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42588) [\[CVE json\]](./CVE-2026-42588.cve.json) [\[OSV json\]](./CVE-2026-42588.osv.json)



_Last updated: 2026-06-01T07:23:15.963Z_

### Affected

* Apache ActiveMQ Broker before 5.19.7
* Apache ActiveMQ Broker from 6.0.0 before 6.2.6
* Apache ActiveMQ All before 5.19.7
* Apache ActiveMQ All from 6.0.0 before 6.2.6
* Apache ActiveMQ before 5.19.7
* Apache ActiveMQ from 6.0.0 before 6.2.6


### Description

<p>Improper Input Validation, Improper Control of Generation of Code ('Code Injection') vulnerability in Apache ActiveMQ Broker, Apache ActiveMQ All, Apache ActiveMQ.</p>Apache ActiveMQ Classic exposes the Jolokia JMX-HTTP bridge at /api/jolokia/ on the web console. The default Jolokia access policy permits exec operations on all ActiveMQ MBeans (org.apache.activemq:*), including<br>BrokerService.addNetworkConnector(String).<br><br>An authenticated attacker can invoke these operations with a crafted discovery URI that triggers the VM transport's brokerConfig parameter using the "<span style="background-color: rgb(255, 255, 255);">masterslave:// " URL which can allow loading a</span>&nbsp;Spring XML application context using ResourceXmlApplicationContext.<br>Because Spring's ResourceXmlApplicationContext instantiates all singleton beans before the BrokerService validates the configuration, arbitrary code execution occurs on the broker's JVM through bean factory methods such as Runtime.exec().<br><p>This issue affects Apache ActiveMQ Broker: before 5.19.7, from 6.0.0 before 6.2.6; Apache ActiveMQ All: before 5.19.7, from 6.0.0 before 6.2.6; Apache ActiveMQ: before 5.19.7, from 6.0.0 before 6.2.6.</p><p>Users are recommended to upgrade to version 5.19.7 or 6.2.6, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ns0zktfo16s9ql2mmtqtlb6p6xcs45xm


### Credits
* pyn3rd (finder)
* uname (finder)
* 4ra1n (finder)


## HTTP Response Header Injection via JMS Message Properties ## { #CVE-2026-42253 }

CVE-2026-42253 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42253) [\[CVE json\]](./CVE-2026-42253.cve.json) [\[OSV json\]](./CVE-2026-42253.osv.json)



_Last updated: 2026-06-03T09:26:01.816Z_

### Affected

* Apache ActiveMQ before 5.19.7
* Apache ActiveMQ from 6.0.0 before 6.2.6
* Apache ActiveMQ Web before 5.19.7
* Apache ActiveMQ Web from 6.0.0 before 6.2.6


### Description

<p>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache ActiveMQ, Apache ActiveMQ Web.</p><span style="background-color: rgb(255, 255, 255);">The MessageServlet in the ActiveMQ web console API copies every JMS message
property into an HTTP response header without any validation. This can allow overwriting and injecting security headers by setting them on JMS messages that are returned by the servlet.<br></span><br><p>This issue affects Apache ActiveMQ: before 5.19.7, from 6.0.0 before 6.2.6; Apache ActiveMQ Web: before 5.19.7, from 6.0.0 before 6.2.6.</p><p>Users are recommended to upgrade to version 5.19.7 or 6.2.6, which fixes the issue.&nbsp;<span style="background-color: rgb(255, 255, 255);">The MessageServlet has now been deprecated and disabled by default.</span></p>

### References
* https://lists.apache.org/thread/j9vmlc410ht5f28fc98gx75jcbq62j00


### Credits
* Vishal Shukla (finder)
* pyn3rd (finder)
* uname (finder)
* 4ra1n (finder)
* kikayli (finder)


## Authenticated user can perform RCE via DestinationView MBean exposed by Jolokia ## { #CVE-2026-41044 }

CVE-2026-41044 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41044) [\[CVE json\]](./CVE-2026-41044.cve.json) [\[OSV json\]](./CVE-2026-41044.osv.json)



_Last updated: 2026-04-24T10:16:51.999Z_

### Affected

* Apache ActiveMQ before 5.19.6
* Apache ActiveMQ from 6.0.0 before 6.2.5
* Apache ActiveMQ Broker before 5.19.6
* Apache ActiveMQ Broker from 6.0.0 before 6.2.5
* Apache ActiveMQ All before 5.19.6
* Apache ActiveMQ All from 6.0.0 before 6.2.5


### Description

<p></p><p>Improper Input Validation, Improper Control of Generation of Code ('Code Injection') vulnerability in Apache ActiveMQ, Apache ActiveMQ Broker, Apache ActiveMQ All.</p>An authenticated attacker can use the admin web console page to construct a malicious broker name that bypasses name validation to include an xbean binding that can be later used by a VM transport to load a remote Spring XML application.<br>The attacker can then use the DestinationView mbean to send a message to trigger a VM transport creation that will reference this malicious broker name which can lead to loading the malicious Spring XML context file.<br>

Because Spring's ResourceXmlApplicationContext instantiates all singleton beans before the BrokerService validates the configuration, arbitrary code execution occurs on the broker's JVM through bean factory methods such as Runtime.exec().<p></p><p>This issue affects Apache ActiveMQ: before 5.19.6, from 6.0.0 before 6.2.5; Apache ActiveMQ Broker: before 5.19.6, from 6.0.0 before 6.2.5; Apache ActiveMQ All: before 5.19.6, from 6.0.0 before 6.2.5.</p><p>Users are recommended to upgrade to version 6.2.5 or 5.19.6, which fixes the issue.</p>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2026-41044-announcement.txt


### Credits
* jsjcw (finder)


## ActiveMQ Web Console -  XSS vulnerability when browsing queues ## { #CVE-2026-41043 }

CVE-2026-41043 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41043) [\[CVE json\]](./CVE-2026-41043.cve.json) [\[OSV json\]](./CVE-2026-41043.osv.json)



_Last updated: 2026-06-26T22:01:21.682Z_

### Affected

* Apache ActiveMQ before 5.19.6
* Apache ActiveMQ from 6.0.0 before 6.2.5
* Apache ActiveMQ Web before 5.19.6
* Apache ActiveMQ Web from 6.0.0 before 6.2.5


### Description

<p></p><p>Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in Apache ActiveMQ, Apache ActiveMQ Web.</p>An authenticated attacker can show malicious content when browsing queues in the web console by overriding the content type to be HTML (instead of XML) and by injecting HTML into a JMS selector field.<p></p><p>This issue affects Apache ActiveMQ: before 5.19.6, from 6.0.0 before 6.2.5; Apache ActiveMQ Web: before 5.19.6, from 6.0.0 before 6.2.5.</p><p>Users are recommended to upgrade to version 6.2.5 or 5.19.6, which fixes the issue.</p>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2026-41043-announcement.txt


### Credits
* Khaled Alshammri (finder)


## Possible bypass of CVE-2026-34197 via HTTP discovery second-stage URI ## { #CVE-2026-40466 }

CVE-2026-40466 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40466) [\[CVE json\]](./CVE-2026-40466.cve.json) [\[OSV json\]](./CVE-2026-40466.osv.json)



_Last updated: 2026-04-24T10:15:42.912Z_

### Affected

* Apache ActiveMQ Broker before 5.19.6
* Apache ActiveMQ Broker from 6.0.0 before 6.2.5
* Apache ActiveMQ All before 5.19.6
* Apache ActiveMQ All from 6.0.0 before 6.2.5
* Apache ActiveMQ before 5.19.6
* Apache ActiveMQ from 6.0.0 before 6.2.5


### Description

<p>Improper Input Validation, Improper Control of Generation of Code ('Code Injection') vulnerability in Apache ActiveMQ Broker, Apache ActiveMQ All, Apache ActiveMQ.</p>

An authenticated attacker may bypass the fix in CVE-2026-34197 by adding a connector using an HTTP Discovery transport via&nbsp;<span style="background-color: rgb(255, 255, 255);">BrokerView.addNetworkConnector or&nbsp;BrokerView.addConnector through&nbsp;</span><span style="background-color: rgb(255, 255, 255);">Jolokia if the activemq-http module is on the classpath.</span><br>A malicious HTTP endpoint can return a VM transport through the HTTP URI which will bypass the validation added in CVE-2026-34197. The attacker can then use the VM transport's brokerConfig parameter to load a remote Spring XML application context using ResourceXmlApplicationContext.<br>Because Spring's ResourceXmlApplicationContext instantiates all singleton beans before the BrokerService validates the configuration, arbitrary code execution occurs on the broker's JVM through bean factory methods such as Runtime.exec().

<br><p>This issue affects Apache ActiveMQ Broker: before 5.19.6, from 6.0.0 before 6.2.5; Apache ActiveMQ All: before 5.19.6, from 6.0.0 before 6.2.5; Apache ActiveMQ: before 5.19.6, from 6.0.0 before 6.2.5.</p><p>Users are recommended to upgrade to version 5.19.6 or 6.2.5, which fixes the issue.</p>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2026-34197-announcement.txt


### Credits
* Fatih Ersinadim (finder)
* gggggggga (finder)


## Missing fix for CVE-2025-66168: MQTT control packet remaining length field is not properly validated ## { #CVE-2026-40046 }

CVE-2026-40046 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40046) [\[CVE json\]](./CVE-2026-40046.cve.json) [\[OSV json\]](./CVE-2026-40046.osv.json)



_Last updated: 2026-04-09T15:58:31.486Z_

### Affected

* Apache ActiveMQ from 6.0.0 before 6.2.4
* Apache ActiveMQ All from 6.0.0 before 6.2.4
* Apache ActiveMQ MQTT from 6.0.0 before 6.2.4


### Description

<p>

</p><p>Integer Overflow or Wraparound vulnerability in Apache ActiveMQ, Apache ActiveMQ All, Apache ActiveMQ MQTT.</p>The fix for "CVE-2025-66168: MQTT control packet remaining length field is not properly validated" was only applied to 5.19.2 (and future 5.19.x) releases but was missed for all 6.0.0+ versions.<br><p>

<span style="background-color: rgb(255, 255, 255);">This issue affects Apache ActiveMQ: from 6.0.0 before 6.2.4; Apache ActiveMQ All: from 6.0.0 before 6.2.4; Apache ActiveMQ MQTT: from 6.0.0 before 6.2.4.</span>

</p><p>Users are recommended to upgrade to version 6.2.4 or a 5.19.x version starting with 5.19.2 or later (currently latest is 5.19.5), which fixes the issue.</p><p></p>

### References
* https://www.cve.org/CVERecord?id=CVE-2025-66168
* https://activemq.apache.org/security-advisories.data/CVE-2026-40046-announcement.txt
* https://lists.apache.org/thread/zdntj5rcgjjzrpow84o339lzldy68zrg


### Credits
* Adrien Bernard (finder)


## Incorrect handling of TLSv1.3 KeyUpdate can be exploited to cause DoS via OOM ## { #CVE-2026-39304 }

CVE-2026-39304 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-39304) [\[CVE json\]](./CVE-2026-39304.cve.json) [\[OSV json\]](./CVE-2026-39304.osv.json)



_Last updated: 2026-04-10T10:54:02.870Z_

### Affected

* Apache ActiveMQ Client before 5.19.4
* Apache ActiveMQ Client from 6.0.0 before 6.2.4
* Apache ActiveMQ Broker before 5.19.4
* Apache ActiveMQ Broker from 6.0.0 before 6.2.4
* Apache ActiveMQ All before 5.19.4
* Apache ActiveMQ All from 6.0.0 before 6.2.4
* Apache ActiveMQ before 5.19.4
* Apache ActiveMQ from 6.0.0 before 6.2.4


### Description

<p>Denial of Service via Out of Memory vulnerability in Apache ActiveMQ Client, Apache ActiveMQ Broker, Apache ActiveMQ.</p>ActiveMQ NIO SSL transports do not correctly handle TLSv1.3 handshake KeyUpdates triggered by clients. This makes it possible for a client to rapidly trigger updates which causes the broker to exhaust all its memory in the SSL engine leading to DoS.<br><br>Note: TLS versions before TLSv1.3 (such as TLSv1.2) are broken but are not vulnerable to OOM. Previous TLS versions require a full handshake renegotiation which causes a connection to hang but not OOM. This is fixed as well.<br><p>This issue affects Apache ActiveMQ Client: before 5.19.4, from 6.0.0 before 6.2.4; Apache ActiveMQ Broker: before 5.19.4, from 6.0.0 before 6.2.4; Apache ActiveMQ: before 5.19.4, from 6.0.0 before 6.2.4.</p><p>Users are recommended to upgrade to version 6.2.4 or 5.19.5, which fixes the issue.</p>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2026-39304-announcement.txt


## Authenticated users could perform RCE via Jolokia MBeans ## { #CVE-2026-34197 }

CVE-2026-34197 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34197) [\[CVE json\]](./CVE-2026-34197.cve.json) [\[OSV json\]](./CVE-2026-34197.osv.json)



_Last updated: 2026-04-08T15:39:05.835Z_

### Affected

* Apache ActiveMQ Broker before 5.19.4
* Apache ActiveMQ Broker from 6.0.0 before 6.2.3
* Apache ActiveMQ All before 5.19.4
* Apache ActiveMQ All from 6.0.0 before 6.2.3
* Apache ActiveMQ before 5.19.4
* Apache ActiveMQ from 6.0.0 before 6.2.3


### Description

Improper Input Validation, Improper Control of Generation of Code ('Code Injection') vulnerability in Apache ActiveMQ Broker, Apache ActiveMQ.<br><br>Apache ActiveMQ Classic exposes the Jolokia JMX-HTTP bridge at /api/jolokia/ on the web console. The default Jolokia access policy permits exec operations on all ActiveMQ MBeans (org.apache.activemq:*), including<br>BrokerService.addNetworkConnector(String) and BrokerService.addConnector(String).<br><br>An authenticated attacker can invoke these operations with a crafted discovery URI that triggers the VM transport's brokerConfig parameter to load a remote Spring XML application context using ResourceXmlApplicationContext.<br>Because Spring's ResourceXmlApplicationContext instantiates all singleton beans before the BrokerService validates the configuration, arbitrary code execution occurs on the broker's JVM through bean factory methods such as Runtime.exec().<br><br>

<span style="background-color: rgb(255, 255, 255);">This issue affects Apache ActiveMQ Broker: before 5.19.4, from 6.0.0 before 6.2.3; Apache ActiveMQ All: before 5.19.4, from 6.0.0 before 6.2.3; Apache ActiveMQ: before 5.19.4, from 6.0.0 before 6.2.3.</span>

<br><br>Users are recommended to upgrade to version 5.19.4 or 6.2.3, which fixes the issue<br><br>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2026-34197-announcement.txt


### Credits
* Naveen Sunkavally (Horizon3.ai) (finder)


## Improper Limitation of a Pathname to a Restricted Classpath Directory ## { #CVE-2026-33227 }

CVE-2026-33227 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33227) [\[CVE json\]](./CVE-2026-33227.cve.json) [\[OSV json\]](./CVE-2026-33227.osv.json)



_Last updated: 2026-04-08T15:44:44.530Z_

### Affected

* Apache ActiveMQ Client before 5.19.3
* Apache ActiveMQ Client from 6.0.0 before 6.2.2
* Apache ActiveMQ Broker before 5.19.3
* Apache ActiveMQ Broker from 6.0.0 before 6.2.2
* Apache ActiveMQ All before 5.19.3
* Apache ActiveMQ All from 6.0.0 before 6.2.2
* Apache ActiveMQ Web before 5.19.3
* Apache ActiveMQ Web from 6.0.0 before 6.2.2
* Apache ActiveMQ before 5.19.3
* Apache ActiveMQ from 6.0.0 before 6.2.2


### Description

<p>Improper validation and restriction of a classpath path name vulnerability in 

 Apache ActiveMQ Client, Apache ActiveMQ Broker, Apache ActiveMQ All, Apache ActiveMQ Web, Apache ActiveMQ.

<br><br>In two instances (when creating a Stomp consumer and also browsing messages in the Web console) an authenticated user provided "key" value could be constructed to traverse the classpath due to path concatenation. As a result, the application is exposed to a classpath path resource loading vulnerability that could potentially be chained together with another attack to lead to exploit.</p><p>

</p><p>This issue affects Apache ActiveMQ Client: before 5.19.3, from 6.0.0 before 6.2.2; Apache ActiveMQ Broker: before 5.19.3, from 6.0.0 before 6.2.2; Apache ActiveMQ All: before 5.19.3, from 6.0.0 before 6.2.2; Apache ActiveMQ Web: before 5.19.3, from 6.0.0 before 6.2.2; Apache ActiveMQ: before 5.19.3, from 6.0.0 before 6.2.2.</p>Users are recommended to upgrade to version 5.19.4 or 6.2.3, which fixes the issue. Note: 5.19.3 and 6.2.2 also fix this issue, but that is limited to non-Windows environments due to a path separator resolution bug fixed in 5.19.4 and 6.2.3.<br><p></p>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2026-33227-announcement.txt


### Credits
* Dawei Wang (finder)


## MQTT control packet remaining length field is not properly validated ## { #CVE-2025-66168 }

CVE-2025-66168 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-66168) [\[CVE json\]](./CVE-2025-66168.cve.json) [\[OSV json\]](./CVE-2025-66168.osv.json)



_Last updated: 2026-04-10T10:52:26.234Z_

### Affected

* Apache ActiveMQ before 5.19.2
* Apache ActiveMQ from 6.0.0 before 6.1.9
* Apache ActiveMQ from 6.2.0 before 6.2.1
* Apache ActiveMQ All Module before 5.19.2
* Apache ActiveMQ All Module from 6.0.0 before 6.1.9
* Apache ActiveMQ All Module from 6.2.0 before 6.2.1
* Apache ActiveMQ MQTT Module before 5.19.2
* Apache ActiveMQ MQTT Module from 6.0.0 before 6.1.9
* Apache ActiveMQ MQTT Module from 6.2.0 before 6.2.1


### Description

<p><span style="background-color: rgb(255, 255, 255);"><b>WARNING:</b><br><br></span><span style="background-color: rgb(239, 250, 102);">Users of 6.x should upgrade to 6.2.4 or later as the fix was missed in previous 6.x releases.</span><span style="background-color: rgb(255, 255, 255);"><br><br>See the&nbsp; following for more details:<br><a target="_blank" rel="nofollow" href="https://activemq.apache.org/security-advisories.data/CVE-2026-40046-announcement.txt">https://activemq.apache.org/security-advisories.data/CVE-2026-40046-announcement.txt</a><br><a target="_blank" rel="nofollow" href="https://www.cve.org/CVERecord?id=CVE-2026-40046">https://www.cve.org/CVERecord?id=CVE-2026-40046</a><br></span><span style="background-color: rgb(255, 255, 255);"><br></span></p><p><span style="background-color: rgb(255, 255, 255);"><b>Original Report:</b></span></p><p><span style="background-color: rgb(255, 255, 255);">Apache ActiveMQ does not properly validate the remaining length field which may lead to an overflow during the decoding of malformed packets.&nbsp;</span><span style="background-color: rgb(255, 255, 255);">When this integer overflow occurs, ActiveMQ may incorrectly compute the total Remaining Length and subsequently misinterpret the payload as multiple MQTT control packets which makes<span style="background-color: rgb(255, 255, 255);">&nbsp;the broker susceptible to unexpected behavior when interacting with non-compliant clients.</span>&nbsp;</span><span style="background-color: rgb(255, 255, 255);">This behavior violates the MQTT v3.1.1 specification, which restricts Remaining Length to a maximum of 4 bytes.</span>&nbsp;The scenario occurs on established connections after the authentication process. Brokers that are not enabling mqtt transport connectors are not impacted.</p><p>This issue affects Apache ActiveMQ: before 5.19.2, 6.0.0 to 6.1.8, and 6.2.0</p><p>Users are recommended to upgrade to version 5.19.2, 6.1.9, or 6.2.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/13n8mkrb2jf2y6yyhpgrkmpqcm7djyto
* https://www.cve.org/CVERecord?id=CVE-2026-40046
* https://activemq.apache.org/security-advisories.data/CVE-2026-40046-announcement.txt


### Credits
* Gai Tanaka <641.work123@gmail.com> (finder)


## Deserialization of Untrusted Data ## { #CVE-2025-54539 }

CVE-2025-54539 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-54539) [\[CVE json\]](./CVE-2025-54539.cve.json) [\[OSV json\]](./CVE-2025-54539.osv.json)



_Last updated: 2025-10-16T08:26:04.874Z_

### Affected

* Apache ActiveMQ NMS AMQP Client through 2.3.0


### Description

A Deserialization of Untrusted Data vulnerability exists in the Apache ActiveMQ NMS AMQP Client.<br><br>This issue affects all versions of Apache ActiveMQ NMS AMQP up to and including 2.3.0, when establishing connections to untrusted AMQP servers. Malicious servers could exploit unbounded deserialization logic present in the client to craft responses that may lead to arbitrary code execution on the client side.<br><br>Although version 2.1.0 introduced a mechanism to restrict deserialization via allow/deny lists, the protection was found to be bypassable under certain conditions.<br><br>In line with Microsoft’s deprecation of binary serialization in .NET 9, the project is evaluating the removal of .NET binary serialization support from the NMS API entirely in future releases.<br><br>Mitigation and Recommendations:<br>Users are strongly encouraged to upgrade to version 2.4.0 or later, which resolves the issue. Additionally, projects depending on NMS-AMQP should migrate away from .NET binary serialization as part of a long-term hardening strategy.

### References
* https://lists.apache.org/thread/9k684j07ljrshy3hxwhj5m0xjmkz1g2n


### Credits
* Security Research Team @ Endor Labs (finder)


## deserialization allowlist bypass ## { #CVE-2025-29953 }

CVE-2025-29953 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-29953) [\[CVE json\]](./CVE-2025-29953.cve.json) [\[OSV json\]](./CVE-2025-29953.osv.json)



_Last updated: 2025-04-18T15:23:28.244Z_

### Affected

* Apache ActiveMQ NMS OpenWire Client before 2.1.1


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache ActiveMQ NMS OpenWire Client.</p><p>This issue affects Apache ActiveMQ NMS OpenWire Client before 2.1.1 when performing connections to untrusted servers. Such servers could abuse the unbounded deserialization in the client to provide malicious responses that may eventually cause arbitrary code execution on the client. Version 2.1.0 introduced a allow/denylist feature to restrict deserialization, but this feature could be bypassed.</p><p>The .NET team has deprecated the built-in .NET binary serialization feature starting with .NET 9 and suggests migrating away from binary serialization. The project is considering to follow suit and drop this part of the NMS API altogether.</p><p>Users are recommended to upgrade to version 2.1.1, which fixes the issue. We also recommend to migrate away from relying on .NET binary serialization as a hardening method for the future.</p>

### References
* https://lists.apache.org/thread/vc1sj9y3056d3kkhcvrs9fyw5w8kpmlx


### Credits
* g7shot working with Trend Zero Day Initiative (finder)


## Unchecked buffer length can cause excessive memory allocation ## { #CVE-2025-27533 }

CVE-2025-27533 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27533) [\[CVE json\]](./CVE-2025-27533.cve.json) [\[OSV json\]](./CVE-2025-27533.osv.json)



_Last updated: 2025-05-07T08:58:58.430Z_

### Affected

* Apache ActiveMQ from 6.0.0 before 6.1.6
* Apache ActiveMQ from 5.18.0 before 5.18.7
* Apache ActiveMQ from 5.17.0 before 5.17.7
* Apache ActiveMQ from 5.16.0 before 5.16.8


### Description

<p>Memory Allocation with Excessive Size Value vulnerability in Apache ActiveMQ.</p><span style="background-color: rgb(255, 255, 255);">During unmarshalling of OpenWire commands the size value of buffers was not properly validated which could lead to excessive memory allocation and be exploited to cause a denial of service (DoS) by depleting process memory, thereby affecting applications and services that rely on the availability of the ActiveMQ broker when not using mutual TLS connections.</span><br><p>This issue affects Apache ActiveMQ: from 6.0.0 before 6.1.6, from 5.18.0 before 5.18.7, from 5.17.0 before 5.17.7, before 5.16.8. ActiveMQ 5.19.0 is not affected.</p><p>Users are recommended to upgrade to version 6.1.6+, 5.19.0+,  5.18.7+, 5.17.7, or 5.16.8 or which fixes the issue.</p><p>Existing users may implement mutual TLS to mitigate the risk on affected brokers.</p>

### References
* https://lists.apache.org/thread/8hcm25vf7mchg4zbbhnlx2lc5bs705hg


## Address routing-type can be updated by user without the createAddress permission ## { #CVE-2025-27427 }

CVE-2025-27427 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27427) [\[CVE json\]](./CVE-2025-27427.cve.json) [\[OSV json\]](./CVE-2025-27427.osv.json)



_Last updated: 2025-04-01T07:26:53.803Z_

### Affected

* Apache ActiveMQ Artemis from 2.0.0 through 2.39.0


### Description

<p>A vulnerability exists in Apache ActiveMQ Artemis whereby a user with the createDurableQueue or createNonDurableQueue permission on an address can augment the routing-type supported by that address even if said user doesn't have the createAddress permission for that particular address. When combined with the send permission and automatic queue creation a user could successfully send a message with a routing-type not supported by the address when that message should actually be rejected on the basis that the user doesn't have permission to change the routing-type of the address.</p><p>This issue affects Apache ActiveMQ Artemis from 2.0.0 through 2.39.0.</p><p>Users are recommended to upgrade to version 2.40.0 which fixes the issue.</p>

### References
* https://lists.apache.org/thread/8dzlm2vkqphyrnkrby8r8kzndsm5o6x8


### Credits
* Eojin Lee <djwls7179@gmail.com> (reporter)
* Dain Lee <ledain5094@gmail.com> (finder)
* WooJin Park <1203kids@gmail.com> (finder)
* MinJung Lee <whitney2319@gmail.com> (finder)
* SeChang Oh <osc010524@gmail.com> (finder)


## Passwords leaking from broker properties in the debug log ## { #CVE-2025-27391 }

CVE-2025-27391 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27391) [\[CVE json\]](./CVE-2025-27391.cve.json) [\[OSV json\]](./CVE-2025-27391.osv.json)



_Last updated: 2025-04-09T14:42:30.509Z_

### Affected

* Apache ActiveMQ Artemis from 1.5.1 before 2.40.0


### Description

<p>Insertion of Sensitive Information into Log File vulnerability in Apache ActiveMQ Artemis. All the values of the broker properties are&nbsp;logged when the org.apache.activemq.artemis.core.config.impl.ConfigurationImpl <span style="background-color: rgb(255, 255, 255);">logger has the&nbsp;</span>debug level enabled.</p><p>This issue affects Apache ActiveMQ Artemis: from 1.5.1 before 2.40.0. It can be mitigated by restricting log access to only trusted users.</p><p>Users are recommended to upgrade to version 2.40.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/25p96cvzl1mkt29lwm2d8knklkoqolps


### Credits
* Rafael Yanez Illescas <ryanezil@redhat.com> (finder)


## Jolokia and REST API were not secured with default configuration ## { #CVE-2024-32114 }

CVE-2024-32114 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-32114) [\[CVE json\]](./CVE-2024-32114.cve.json) [\[OSV json\]](./CVE-2024-32114.osv.json)



_Last updated: 2024-05-01T16:07:22.140Z_

### Affected

* Apache ActiveMQ from 6.0.0 through 6.1.1


### Description

In Apache ActiveMQ 6.x, the default configuration doesn't secure the API web context (where the Jolokia JMX REST API and the Message REST API are located).<br>It means that anyone can use these layers without any required authentication. Potentially, anyone can interact with the broker (using Jolokia JMX REST API) and/or produce/consume messages or purge/delete destinations (using the Message REST API).<br><br>To mitigate, users can update the default conf/jetty.xml configuration file to add authentication requirement:<br><blockquote><pre>&lt;bean id="securityConstraintMapping" class="org.eclipse.jetty.security.ConstraintMapping"&gt;
&nbsp; &lt;property name="constraint" ref="securityConstraint" /&gt;
&nbsp; &lt;property name="pathSpec" value="/" /&gt;
&lt;/bean&gt;</pre></blockquote>Or we encourage users to upgrade to Apache ActiveMQ 6.1.2 where the default configuration has been updated with authentication by default.<br>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2024-32114-announcement.txt


### Credits
* Martin Zeissig (finder)


## Authenticated users could perform RCE via Jolokia MBeans ## { #CVE-2023-50780 }

CVE-2023-50780 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-50780) [\[CVE json\]](./CVE-2023-50780.cve.json) [\[OSV json\]](./CVE-2023-50780.osv.json)



_Last updated: 2024-10-14T16:03:33.323Z_

### Affected

* Apache ActiveMQ Artemis before 2.29.0


### Description

<p>Apache ActiveMQ Artemis allows access to diagnostic information and controls through MBeans, which are also exposed through the authenticated Jolokia endpoint. Before version 2.29.0, this also included the Log4J2 MBean. This MBean is not meant for exposure to non-administrative users. This could eventually allow an authenticated attacker to write arbitrary files to the filesystem and indirectly achieve RCE.<br></p><p>Users are recommended to upgrade to version 2.29.0 or later, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/63b78shqz312phsx7v1ryr7jv7bprg58


### Credits
* Matei "Mal" Badanoiu (finder)


## Unbounded deserialization causes ActiveMQ to be vulnerable to a remote code execution (RCE) attack ## { #CVE-2023-46604 }

CVE-2023-46604 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-46604) [\[CVE json\]](./CVE-2023-46604.cve.json)

_Last updated: 2023-11-28T15:02:26.708Z_

### Affected

* Apache ActiveMQ from 5.18.0 before 5.18.3
* Apache ActiveMQ from 5.17.0 before 5.17.6
* Apache ActiveMQ from 5.16.0 before 5.16.7
* Apache ActiveMQ before 5.15.16
* Apache ActiveMQ Legacy OpenWire Module from 5.18.0 before 5.18.3
* Apache ActiveMQ Legacy OpenWire Module from 5.17.0 before 5.17.6
* Apache ActiveMQ Legacy OpenWire Module from 5.16.0 before 5.16.7
* Apache ActiveMQ Legacy OpenWire Module from 5.8.0 before 5.15.16


### Description

<div>The Java OpenWire protocol marshaller is vulnerable to Remote Code 
Execution. This vulnerability may allow a remote attacker with network 
access to either a Java-based OpenWire broker or client to run arbitrary
 shell commands by manipulating serialized class types in the OpenWire 
protocol to cause either the client or the broker (respectively) to 
instantiate any class on the classpath.</div><div><br></div><div>Users are recommended to upgrade
 both brokers and clients to version 5.15.16, 5.16.7, 5.17.6, or 5.18.3 
which fixes this issue.</div>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2023-46604-announcement.txt
* https://www.openwall.com/lists/oss-security/2023/10/27/5
* https://security.netapp.com/advisory/ntap-20231110-0010/
* https://packetstormsecurity.com/files/175676/Apache-ActiveMQ-Unauthenticated-Remote-Code-Execution.html
* https://lists.debian.org/debian-lts-announce/2023/11/msg00013.html


### Credits
* yejie@threatbook.cn (finder)


## Insufficient API restrictions on Jolokia allow authenticated users to perform RCE ## { #CVE-2022-41678 }

CVE-2022-41678 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-41678) [\[CVE json\]](./CVE-2022-41678.cve.json)

_Last updated: 2024-05-31T08:42:39.786Z_

### Affected

* Apache ActiveMQ before 5.16.6
* Apache ActiveMQ from 5.17.0 before 5.17.4
* Apache ActiveMQ at 5.18.0 unaffected
* Apache ActiveMQ at 6.0.0 unaffected


### Description

<span style="background-color: rgb(255, 255, 255);">Once an user is authenticated on Jolokia, he can potentially trigger arbitrary code execution.&nbsp;<br><br>In details, in ActiveMQ configurations, jetty allows
org.jolokia.http.AgentServlet to handler request to /api/jolokia<br><br>org.jolokia.http.HttpRequestHandler#handlePostRequest is able to
create JmxRequest through JSONObject. And calls to
org.jolokia.http.HttpRequestHandler#executeRequest.<br><br>Into deeper calling stacks,
org.jolokia.handler.ExecHandler#doHandleRequest can be invoked
through refection. This could lead to RCE through via
various mbeans. One example is unrestricted deserialization in jdk.management.jfr.FlightRecorderMXBeanImpl which exists on Java version above 11.
<br><br>
1 Call newRecording.
<br>
2 Call setConfiguration. And a webshell data hides in it.
<br>
3 Call startRecording.
<br>
4 Call copyTo method. The webshell will be written to a .jsp file.<br><br></span>The mitigation is to restrict (by default) the actions authorized on Jolokia, or disable Jolokia.<br>A more restrictive Jolokia configuration has been defined in default ActiveMQ distribution. We encourage users to upgrade to ActiveMQ distributions version including updated Jolokia configuration: 5.16.6, 5.17.4, 5.18.0, 6.0.0.<br>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2022-41678-announcement.txt
* https://lists.apache.org/thread/7g17kwbtjl011mm4tr8bn1vnoq9wh4sl
* https://www.openwall.com/lists/oss-security/2023/11/28/1
* https://security.netapp.com/advisory/ntap-20240216-0004/


### Credits
* wangxin@threatbook.cn (finder)
* wangzhendong@threatbook.cn (finder)
* honglonglong@threatbook.cn (finder)
* Matei "Mal" Badanoiu (finder)


## HTML Injection in ActiveMQ Artemis Web Console ## { #CVE-2022-35278 }

CVE-2022-35278 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-35278) [\[CVE json\]](./CVE-2022-35278.cve.json) [\[OSV json\]](./CVE-2022-35278.osv.json)



_Last updated: 2022-08-18T07:52:49.472Z_

### Affected

* Apache ActiveMQ Artemis from unspecified through 2.23.1


### Description

In Apache ActiveMQ Artemis prior to 2.24.0, an attacker could show malicious content and/or redirect users to a malicious URL in the web console by using HTML in the name of an address or queue.

### References
* https://lists.apache.org/thread/bh6y81wtotg75337bpvxcjy436zfgf3n


### Credits
* Apache ActiveMQ would like to thank Yash Pandya (Digital14), Rajatkumar Karmarkar (Digital14), and Likhith Cheekatipalle (Digital14) for reporting this issue.


## Apache ActiveMQ Artemis DoS ## { #CVE-2022-23913 }

CVE-2022-23913 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-23913) [\[CVE json\]](./CVE-2022-23913.cve.json) [\[OSV json\]](./CVE-2022-23913.osv.json)



_Last updated: 2022-02-04T08:26:48.236Z_

### Affected

* Apache ActiveMQ Artemis from 2.19.0 before 2.20.0


### Description

In Apache ActiveMQ Artemis prior to 2.20.0 or 2.19.1, an attacker could partially disrupt availability (DoS) through uncontrolled resource consumption of memory.

### References
* https://lists.apache.org/thread/fjynj57rd99s814rdn5hzvmx8lz403q2


## Flaw in ActiveMQ Artemis OpenWire support ## { #CVE-2021-26118 }

CVE-2021-26118 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-26118) [\[CVE json\]](./CVE-2021-26118.cve.json) [\[OSV json\]](./CVE-2021-26118.osv.json)



_Last updated: 2021-01-27T18:47:25.710Z_

### Affected

* Apache ActiveMQ Artemis from unspecified before 2.16.0


### Description

While investigating ARTEMIS-2964 it was found that the creation of advisory messages in the OpenWire protocol head of Apache ActiveMQ Artemis 2.15.0 bypassed policy based access control for the entire session. Production of advisory messages was not subject to access control in error.

### References
* https://mail-archives.apache.org/mod_mbox/activemq-users/202101.mbox/%3CCAH%2BvQmMUNnkiXv2-d3ucdErWOsdnLi6CgnK%2BVfixyJvTgTuYig%40mail.gmail.com%3E


### Credits
* Apache ActiveMQ  would like to thank Francesco Marchioni (Red Hat) for reporting this issue.


## ActiveMQ: LDAP-Authentication does not verify passwords on servers with anonymous bind ## { #CVE-2021-26117 }

CVE-2021-26117 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-26117) [\[CVE json\]](./CVE-2021-26117.cve.json) [\[OSV json\]](./CVE-2021-26117.osv.json)



_Last updated: 2021-01-27T18:47:20.605Z_

### Affected

* Apache ActiveMQ from Apache ActiveMQ Artemis before 2.16.0
* Apache ActiveMQ from Apache ActiveMQ before 5.16.1


### Description

The optional ActiveMQ LDAP login module can be configured to use anonymous access to the LDAP server. In this case, for Apache ActiveMQ Artemis prior to version 2.16.0 and Apache ActiveMQ prior to versions 5.16.1 and 5.15.14, the anonymous context is used to verify a valid users password in error, resulting in no check on the password.

### References
* https://mail-archives.apache.org/mod_mbox/activemq-users/202101.mbox/%3cCAH+vQmMeUEiKN4wYX9nLBbqmFZFPXqajNvBKmzb2V8QZANcSTA%40mail.gmail.com%3e


### Credits
* Apache ActiveMQ would like to thank Gregor Tudan <gregor.tudan@cofinpro.de> for reporting this issue.


##  ## { #CVE-2020-13947 }

CVE-2020-13947 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-13947) [\[CVE json\]](./CVE-2020-13947.cve.json) [\[OSV json\]](./CVE-2020-13947.osv.json)



_Last updated: 2021-02-10T09:16:00.641Z_

### Affected

* Apache ActiveMQ from Apache ActiveMQ before 5.15.13


### Description

An instance of a cross-site scripting vulnerability was identified to be present in the web based administration console on the message.jsp page of Apache ActiveMQ versions 5.15.12 through 5.16.0.

### References
* http://activemq.apache.org/security-advisories.data/CVE-2020-13947-announcement.txt
