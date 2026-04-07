---
title: Apache Artemis security advisories
description: Security information for Apache Artemis
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Artemis? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

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
