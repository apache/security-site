---
title: Apache Artemis security advisories
description: Security information for Apache Artemis
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Artemis? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Artemis).

You can read more about the security policy on:

- [Apache Artemis security model](https://github.com/apache/artemis/blob/main/docs/user-manual/threat-model.adoc)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Message selector wildcard handling could lead to denial of service ## { #CVE-2026-75880 }

CVE-2026-75880 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-75880) [\[CVE json\]](./CVE-2026-75880.cve.json) [\[OSV json\]](./CVE-2026-75880.osv.json)



_Last updated: 2026-09-10T04:33:09.851Z_

### Affected

* Apache Artemis from 2.50.0 through 2.56.0
* Apache ActiveMQ Artemis from 1.0.0 through 2.44.0


### Description

<p>An authenticated client could attach a consumer with a selector containing crafted wildcard usage that results in excessive evaluation during message delivery attempts, occupying a shared broker thread and leading to denial of service.</p><div>This issue affects Apache Artemis: from 2.50.0 through 2.56.0; Apache ActiveMQ Artemis: from 1.0.0 through 2.44.0.</div><div><br>Users are recommended to upgrade to version 2.57.0, which fixes this issue.</div>

### References
* https://lists.apache.org/thread/db34g9qoxd8p08086cr95683fkb8wm5r


### Credits
* Mike Read (finder)


## Pre-authentication Openwire protocol handling can result in queue deletion ## { #CVE-2026-67593 }

CVE-2026-67593 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67593) [\[CVE json\]](./CVE-2026-67593.cve.json) [\[OSV json\]](./CVE-2026-67593.osv.json)



_Last updated: 2026-09-10T04:40:11.068Z_

### Affected

* Apache Artemis from 2.50.0 through 2.56.0
* Apache Artemis from 2.50.0 through 2.56.0
* Apache ActiveMQ Artemis from 1.0.0 through 2.44.0
* Apache ActiveMQ Artemis from 2.32.0 through 2.44.0


### Description

<p>A remote attacker can craft an Openwire RemoveSubscriptionInfo command to cause the deletion of a queue on the Artemis broker before the connection authentication and authorization stage or at any time thereafter. </p><p>This issue affects Apache Artemis: from 2.50.0 through 2.56.0; Apache ActiveMQ Artemis: from 1.0.0 through 2.44.0.</p><p>Users are recommended to upgrade to version 2.57.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zlglnsg8s5xv8n56d15dm5mf00h2d8xs


### Credits
* Daniel Birtwhistle (finder)
* krsecurity(kongr) (reporter)
* Dilrevx, NSSL, SJTU (reporter)


## Missing authentication on CORE protocol session reattachment ## { #CVE-2026-57967 }

CVE-2026-57967 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57967) [\[CVE json\]](./CVE-2026-57967.cve.json) [\[OSV json\]](./CVE-2026-57967.osv.json)



_Last updated: 2026-09-10T04:42:57.322Z_

### Affected

* Apache Artemis from 2.50.0 through 2.56.0
* Apache ActiveMQ Artemis from 1.0.0 through 2.44.0


### Description

<p>An unauthenticated remote attacker can craft a CORE protocol SESSION_REATTACH packet to steal an existing session and assume ongoing execution of the previously authenticated session.</p><p>This issue affects Apache Artemis: from 2.50.0 through 2.56.0; Apache ActiveMQ Artemis: from 1.0.0 through 2.44.0.</p><p>Users are recommended to upgrade to version 2.57.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/fxfjqrdsnksw5f17zs3yqo864lblgv6y


### Credits
* Domenico Francesco Bruscino (finder)
* Fedrick Sequeira (reporter)


## Message-based management parameter deserialization may lead to denial of service ## { #CVE-2026-57822 }

CVE-2026-57822 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57822) [\[CVE json\]](./CVE-2026-57822.cve.json) [\[OSV json\]](./CVE-2026-57822.osv.json)



_Last updated: 2026-09-10T04:46:30.053Z_

### Affected

* Apache Artemis from 2.50.0 through 2.56.0
* Apache ActiveMQ Artemis from 1.3.0 through 2.44.0


### Description

<p>When the broker is processing message-based management requests, sent by an authenticated messaging client that is authorized with MANAGE permission to perform management-via-messaging, the parameter processing can trigger Java deserialization of certain method parameters that the broker will not utilise. The permitted types allow to craft a payload causing excessive computation and pinning the processing thread, leading to denial of service.<br></p><p><span>This issue affects Apache Artemis: from 2.50.0 through 2.56.0; Apache ActiveMQ Artemis: from 1.3.0 through 2.44.0.</span></p><p>Users are recommended to upgrade to version 2.57.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/0jmovbbvdo22zq1r91jrlhv02ck7jqzp


### Credits
* Clebert Suconic (finder)
* Mike Read (reporter)


## Pre-Authentication Cluster Credential Exposure to Discovered Peers ## { #CVE-2026-49364 }

CVE-2026-49364 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49364) [\[CVE json\]](./CVE-2026-49364.cve.json) [\[OSV json\]](./CVE-2026-49364.osv.json)



_Last updated: 2026-09-10T04:49:18.247Z_

### Affected

* Apache Artemis from 2.50.0 through 2.56.0
* Apache Artemis from 2.50.0 through 2.56.0
* Apache ActiveMQ Artemis from 1.0.0 through 2.44.0
* Apache ActiveMQ Artemis from 1.0.0 through 2.44.0


### Description

<p>An unauthenticated network-adjacent attacker can leverage discovery to capture cluster administrative credentials during the initial cluster connection handshake.<br><span><br>This issue affects Apache Artemis: from 2.50.0 through 2.56.0; Apache ActiveMQ Artemis: from 1.0.0 through 2.44.0.</span></p><p>Users are recommended to upgrade to version 2.57.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/4qbgcz3k38q30bfbf7hphtomrdc8l8n8


### Credits
* Domenico Francesco Bruscino (finder)


## Pre-Authentication Information Disclosure in CORE Protocol Topology Subscription ## { #CVE-2026-49363 }

CVE-2026-49363 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49363) [\[CVE json\]](./CVE-2026-49363.cve.json) [\[OSV json\]](./CVE-2026-49363.osv.json)



_Last updated: 2026-09-10T04:51:45.409Z_

### Affected

* Apache Artemis from 2.50.0 through 2.56.0
* Apache ActiveMQ Artemis from 1.0.0 through 2.44.0


### Description

<p>An unauthenticated remote attacker connecting with the CORE protocol can discover cluster node details by sending a SUBSCRIBE_TOPOLOGY request prior to authentication.</p><p>This issue affects Apache Artemis: from 2.50.0 through 2.56.0; Apache ActiveMQ Artemis: from 1.0.0 through 2.44.0.</p><p>Users are recommended to upgrade to version 2.57.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/syjch88zw6pfdoso9vs46m23xkgxjbxo


### Credits
* Domenico Francesco Bruscino (finder)


## Missing Authentication in CORE Protocol Handler Allows Unauthorized Queue Creation ## { #CVE-2026-49362 }

CVE-2026-49362 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49362) [\[CVE json\]](./CVE-2026-49362.cve.json) [\[OSV json\]](./CVE-2026-49362.osv.json)



_Last updated: 2026-09-10T10:11:10.956Z_

### Affected

* Apache Artemis from 2.50.0 through 2.56.0
* Apache ActiveMQ Artemis from 1.0.0 through 2.44.0


### Description

<p><span>An unauthenticated remote attacker can create arbitrary durable queues via the CORE protocol</span>, leading to unauthorized broker state manipulation and potential denial of service.<span><br></span><span><br>This issue affects Apache Artemis: from 2.50.0 through 2.56.0; Apache ActiveMQ Artemis: from 1.0.0 through 2.44.0.</span></p><p>Users are recommended to upgrade to version 2.57.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/3828w4tm5mfpflmoprb5oxfgwhq3xw0v


### Credits
* Domenico Francesco Bruscino (finder)
* Fedrick Sequeira (reporter)
* Mike Read (reporter)
* Tiago Ventura (reporter)


## Address routing-type can be updated by STOMP protocol user without the createAddress permission ## { #CVE-2026-40914 }

CVE-2026-40914 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40914) [\[CVE json\]](./CVE-2026-40914.cve.json) [\[OSV json\]](./CVE-2026-40914.osv.json)



_Last updated: 2026-05-28T12:28:55.897Z_

### Affected

* Apache Artemis Stomp Protocol from 2.50.0 through 2.53.0
* Apache ActiveMQ Artemis Stomp Protocol from 2.0.0 through 2.44.0


### Description

<p></p><p>A vulnerability exists in Apache Artemis whereby an application using the STOMP protocol with security credentials that grant either the consume or send permission on an address can augment the routing-type supported by that address even if said user doesn't have the createAddress permission for that particular address. A user could successfully send a message to an address or consume a message from a queue with a routing-type not supported by the corresponding address when that operation should actually be rejected on the basis that the user doesn't have permission to change the routing-type of the address. Even though the user was already granted permission to send and/or consume messages, they should not be able to augment the routing-type of the address without the createAddress permission.</p><p></p><p>This issue affects Apache Artemis: from 2.50.0 through 2.53.0; Apache ActiveMQ Artemis: from 2.0.0 through 2.44.0.</p><p>Users are recommended to upgrade to version 2.54.0, which fixes the issue.</p><p></p><p></p>

### References
* https://lists.apache.org/thread/6q3st8dlorz2q05svqn11k1xl7jkmm4c


### Credits
* bugbunny.ai (tool)
* Isaac David <isaac@bugbunny.ai> (reporter)
* Arthur Gervais <arthur@bugbunny.ai> (reporter)


## Temporary address auto-created for OpenWire consumer without createAddress permission ## { #CVE-2026-32642 }

CVE-2026-32642 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-32642) [\[CVE json\]](./CVE-2026-32642.cve.json) [\[OSV json\]](./CVE-2026-32642.osv.json)



_Last updated: 2026-03-24T07:54:40.342Z_

### Affected

* Apache Artemis from 2.50.0 through 2.52.0
* Apache ActiveMQ Artemis from 2.0.0 through 2.44.0


### Description

<p>Incorrect Authorization (CWE-863)&nbsp;vulnerability in Apache Artemis, Apache ActiveMQ Artemis exists when an application using the OpenWire protocol attempts to create a non-durable JMS topic subscription on an address that doesn't exist with an authenticated user which has the "createDurableQueue" permission but does not have the "createAddress" permission and address auto-creation is disabled. In this circumstance, a temporary address will be created whereas the attempt to create the non-durable subscription should instead fail since the user is not authorized to create the corresponding address. When the OpenWire connection is closed the address is removed.</p><p>This issue affects Apache Artemis: from 2.50.0 through 2.52.0; Apache ActiveMQ Artemis: from 2.0.0 through 2.44.0.</p><p>Users are recommended to upgrade to version 2.53.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/4wlrp31ngq2yb54sf4kjb3bl41t4xgtp


### Credits
* Stephen Higgs <shiggs@redhat.com> (reporter)


## Auth bypass for Core downstream federation ## { #CVE-2026-27446 }

CVE-2026-27446 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-27446) [\[CVE json\]](./CVE-2026-27446.cve.json) [\[OSV json\]](./CVE-2026-27446.osv.json)



_Last updated: 2026-03-17T15:30:04.446Z_

### Affected

* Apache Artemis from 2.50.0 through 2.51.0
* Apache ActiveMQ Artemis from 2.11.0 through 2.44.0


### Description

<p>Missing Authentication for Critical Function (CWE-306) vulnerability in Apache Artemis, Apache ActiveMQ Artemis. An unauthenticated remote attacker can use the Core protocol to force a target broker to establish an outbound Core federation connection to an attacker-controlled rogue broker. This could potentially result in message injection into any queue and/or message exfiltration from any queue via the rogue broker. This impacts environments that allow both:</p><p>- incoming Core protocol connections from untrusted sources to the broker</p><p>- outgoing Core protocol connections from the broker to untrusted targets</p><p>This issue affects:</p><p>- Apache Artemis from 2.50.0 through 2.51.0</p><p>- Apache ActiveMQ Artemis from 2.11.0 through 2.44.0.</p><p>Users are recommended to upgrade to Apache Artemis version 2.52.0, which fixes the issue.</p><p>The issue can be mitigated by one of the following:</p><p>- Remove Core protocol support from any acceptor receiving connections from untrusted sources. Incoming Core protocol connections are supported by default via the "artemis" acceptor listening on port 61616. See the "protocols" URL parameter configured for the acceptor. An acceptor URL without this parameter supports all protocols by default, including Core.</p><p>- Use two-way SSL (i.e. certificate-based authentication) in order to force every client to present the proper SSL certificate when establishing a connection before any message protocol handshake is attempted. This will prevent unauthenticated exploitation of this vulnerability.</p><p>- Implement and deploy a Core interceptor to deny all Core downstream federation connect packets. Such packets have a type of (int) -16 or (byte)&nbsp;0xfffffff0. Documentation for interceptors is available at&nbsp;<a target="_blank" rel="nofollow" href="https://artemis.apache.org/components/artemis/documentation/latest/intercepting-operations.html">https://artemis.apache.org/components/artemis/documentation/latest/intercepting-operations.html</a>.</p>

### References
* https://lists.apache.org/thread/jwpsdc8tdxotm98od8n8n30fqlzoc8gg


### Credits
* Hardik Mehta <mehtahardik@proton.me> (finder)
