---
title: Apache Camel security advisories
description: Security information for Apache Camel
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Camel? You can read more about the projects' security policy on their [security page](https://camel.apache.org/manual/security-model.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://camel.apache.org/manual/security-model.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Camel-CXF Message Header Injection via Missing Inbound Filtering ## { #CVE-2026-47323 }

CVE-2026-47323 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-47323) [\[CVE json\]](./CVE-2026-47323.cve.json) [\[OSV json\]](./CVE-2026-47323.osv.json)



_Last updated: 2026-05-19T12:25:47.873Z_

### Affected

* Apache Camel from 3.18.0 before 4.14.6
* Apache Camel from 4.15.0 before 4.18.2


### Description

<p><span style="background-color: rgb(255, 255, 255);">Camel-CXF and Camel-Knative Message Header Injection via Missing Inbound Filtering</span></p><p><span style="background-color: rgb(255, 255, 255);">The CXF and Knative HeaderFilterStrategy implementations (CxfRsHeaderFilterStrategy in camel-cxf-rest, CxfHeaderFilterStrategy in camel-cxf-transport, and KnativeHttpHeaderFilterStrategy in camel-knative-http) only filter outbound Camel-internal headers via setOutFilterStartsWith, while not configuring inbound filtering via setInFilterStartsWith. As a result, an unauthenticated attacker can inject Camel-internal headers (e.g. CamelExecCommandExecutable, CamelFileName) via HTTP requests to CXF-RS or CXF-SOAP endpoints. When a route forwards messages from these endpoints to header-driven components such as camel-exec or camel-file, the injected headers override configured values, enabling remote code execution or arbitrary file writes. This is the same pattern that was previously addressed in camel-undertow (CVE-2025-30177), the broader incoming-header filter (CVE-2025-27636 and CVE-2025-29891), and non-HTTP strategies (CVE-2026-40453).<br></span></p><p>This issue affects Apache Camel: from 3.18.0 before 4.14.6, from 4.15.0 before 4.18.2.</p><p><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 4.19.0, which fixes the issue. If users are on the 4.18.x LTS releases stream, then they are suggested to upgrade to 4.18.2. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.6.</span></p>

### References
* https://camel.apache.org/security/CVE-2026-47323.html


### Credits
* Quac Tran (finder)


## Camel K Cross-Namespace Build Deputy Attack ## { #CVE-2026-45760 }

CVE-2026-45760 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45760) [\[CVE json\]](./CVE-2026-45760.cve.json) [\[OSV json\]](./CVE-2026-45760.osv.json)



_Last updated: 2026-05-21T11:43:39.236Z_

### Affected

* Apache Camel K from 2.0.0 before 2.8.1
* Apache Camel K from 2.9.0 before 2.9.2
* Apache Camel K from 2.10.0 before 2.10.1


### Description

<p>(Externally Controlled Reference to a Resource in Another Sphere), (Authorization Bypass Through User-Controlled Key) vulnerability in Apache Camel K. Authorized users in a Kubernetes namespace can create a Build resource, controlling the Pod generation in a namespace of their choice, including the operator namespace.</p><p>This issue affects Apache Camel K: from 2.0.0 before 2.8.1, from 2.9.0 before 2.9.2, from 2.10.0 before 2.10.1.</p><p>Users are recommended to upgrade to version 2.10.1 (or 2.8.1 or 2.9.2), which fixes the issue.</p>

### References
* https://camel.apache.org/security/CVE-2026-45760.html


### Credits
* @j311yl0v3u (2439839508@qq.com) (finder)
* @b0b0haha (603571786@qq.com) (finder)


## Unsafe Deserialization of JMS ObjectMessage in camel-jms, camel-sjms, camel-sjms2 and camel-amqp ## { #CVE-2026-40860 }

CVE-2026-40860 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40860) [\[CVE json\]](./CVE-2026-40860.cve.json) [\[OSV json\]](./CVE-2026-40860.osv.json)



_Last updated: 2026-04-27T08:03:17.126Z_

### Affected

* Apache Camel from 3.0.0 before 4.14.7
* Apache Camel from 4.15.0 before 4.18.2
* Apache Camel from 4.19.0 before 4.20.0


### Description

<p>JmsBinding.extractBodyFromJms() in camel-jms, and the equivalent JmsBinding class in camel-sjms, deserialized the payload of incoming JMS ObjectMessage values via javax.jms.ObjectMessage.getObject() without applying any ObjectInputFilter, class allowlist or class denylist. Because this code path is reached whenever the mapJmsMessage option is enabled (the default) and Camel acts as a JMS consumer, an attacker able to publish a crafted ObjectMessage to a queue or topic consumed by a Camel application could achieve remote code execution when a deserialization gadget chain was present on the classpath. The same handling was reached transitively through camel-sjms2 (whose Sjms2Endpoint extends SjmsEndpoint) and through camel-amqp (whose AMQPJmsBinding extends JmsBinding), and by other JMS-family components built on JmsComponent such as camel-activemq and camel-activemq6.</p><p>This issue affects Apache Camel: from 3.0.0 before 4.14.7, from 4.15.0 before 4.18.2, from 4.19.0 before 4.20.0.</p><p>Users are recommended to upgrade to version 4.20.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.7. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.2.</p>

### References
* https://camel.apache.org/security/CVE-2026-40860.html


### Credits
* Venkatraman Kumar from Securin (finder)


## Camel-Infinispan: Unsafe Deserialization in Remote Aggregation Repository ## { #CVE-2026-40858 }

CVE-2026-40858 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40858) [\[CVE json\]](./CVE-2026-40858.cve.json) [\[OSV json\]](./CVE-2026-40858.osv.json)



_Last updated: 2026-04-27T09:38:53.977Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.7
* Apache Camel from 4.15.0 before 4.18.2
* Apache Camel from 4.19.0 before 4.20.0


### Description

<p>The camel-infinispan component's ProtoStream-based remote aggregation repository deserializes data read from a remote Infinispan cache using java.io.ObjectInputStream without applying any ObjectInputFilter. An attacker who can write to the Infinispan cache used by a Camel application can inject a crafted serialized Java object that, when read during normal aggregation repository operations such as get or recover, results in arbitrary code execution in the context of the application.</p><p>This issue affects Apache Camel: from 4.0.0 before 4.14.7, from 4.15.0 before 4.18.2, from 4.19.0 before 4.20.0.</p><p>Users are recommended to upgrade to version 4.20.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.7. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.2.</p><p>The JIRA ticket: <a target="_blank" rel="nofollow" href="https://issues.apache.org/jira/browse/CAMEL-23322">https://issues.apache.org/jira/browse/CAMEL-23322</a> refers to the various commits that resolved the issue, and have more details. This issue follows the same class of vulnerability previously addressed in CVE-2024-22369, CVE-2024-23114 and CVE-2026-25747.<br></p>

### References
* https://camel.apache.org/security/CVE-2026-40858.html


### Credits
* Feng Ning from Innora Pte. Ltd. (finder)


## Unsafe Deserialization in MinaConverter.toObjectInput() via TCP/UDP ## { #CVE-2026-40473 }

CVE-2026-40473 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40473) [\[CVE json\]](./CVE-2026-40473.cve.json) [\[OSV json\]](./CVE-2026-40473.osv.json)



_Last updated: 2026-04-27T07:51:56.460Z_

### Affected

* Apache Camel Mina from 3.0.0 before 4.14.6
* Apache Camel Mina from 4.15.0 before 4.18.2
* Apache Camel Mina from 4.19.0 before 4.20.0


### Description

<p>The camel-mina component's MinaConverter.toObjectInput(IoBuffer) type converter wraps an IoBuffer in a java.io.ObjectInputStream without applying any ObjectInputFilter or class-loading restrictions. When a Camel route uses camel-mina as a TCP or UDP consumer and requests conversion to ObjectInput (for example via getBody(ObjectInput.class) or @Body ObjectInput), an attacker sending a crafted serialized Java object over the network to the MINA consumer port can trigger arbitrary code execution in the context of the application during readObject().</p><p>This issue affects Apache Camel: from 3.0.0 before 4.14.6, from 4.15.0 before 4.18.2, from 4.19.0 before 4.20.0.</p><p>Users are recommended to upgrade to version 4.20.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.6. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.2.</p>

### References
* https://camel.apache.org/security/CVE-2026-40473.html


### Credits
* Venkatraman Kumar from Securin (finder)


## Incomplete fix for CVE-2025-27636 in non-HTTP HeaderFilterStrategies (camel-jms, camel-sjms, camel-coap, camel-google-pubsub) allows case-variant header injection ## { #CVE-2026-40453 }

CVE-2026-40453 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40453) [\[CVE json\]](./CVE-2026-40453.cve.json) [\[OSV json\]](./CVE-2026-40453.osv.json)



_Last updated: 2026-04-27T08:23:18.588Z_

### Affected

* Apache Camel JMS from 3.0.0 before 4.14.6
* Apache Camel JMS from 4.15.0 before 4.18.2
* Apache Camel JMS from 4.19.0 before 4.20.0
* Apache Camel CoAP from 3.0.0 before 4.14.6
* Apache Camel CoAP from 4.15.0 before 4.18.2
* Apache Camel CoAP from 4.19.0 before 4.20.0
* Apache Camel Google PubSub from 3.0.0 before 4.14.6
* Apache Camel Google PubSub from 4.15.0 before 4.18.2
* Apache Camel Google PubSub from 4.19.0 before 4.20.0


### Description

<p>The fix for CVE-2025-27636 added setLowerCase(true) to HttpHeaderFilterStrategy so that case-variant header names such as 'CAmelExecCommandExecutable' are filtered out alongside 'CamelExecCommandExecutable'. The same setLowerCase(true) call was not applied to five non-HTTP HeaderFilterStrategy implementations: JmsHeaderFilterStrategy and ClassicJmsHeaderFilterStrategy in camel-jms, SjmsHeaderFilterStrategy in camel-sjms, CoAPHeaderFilterStrategy in camel-coap, and GooglePubsubHeaderFilterStrategy in camel-google-pubsub. Because those strategies use case-sensitive String.startsWith('Camel'/'camel') filtering while the Camel Exchange stores headers in a case-insensitive map, an attacker with JMS (or equivalent) producer access to the broker consumed by a Camel route can inject case-variant Camel internal headers, which are then resolved by downstream components such as camel-exec and camel-file using their canonical casing. This enables remote code execution and arbitrary file write on routes that forward JMS messages to header-driven components.</p><p>This issue affects Apache Camel: from 3.0.0 before 4.14.6, from 4.15.0 before 4.18.2, from 4.19.0 before 4.20.0.</p><p>Users are recommended to upgrade to version 4.20.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.6. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.2.</p>

### References
* https://camel.apache.org/security/CVE-2026-40453.html


### Credits
* Saroj Khadka (finder)


## Unsafe Deserialization from FileBasedKeyLifecycleManager ## { #CVE-2026-40048 }

CVE-2026-40048 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40048) [\[CVE json\]](./CVE-2026-40048.cve.json) [\[OSV json\]](./CVE-2026-40048.osv.json)



_Last updated: 2026-04-27T07:53:48.505Z_

### Affected

* Apache Camel PQC from 4.19.0 before 4.20.0
* Apache Camel PQC from 4.18.0 before 4.18.2


### Description

<p>The Camel-PQC FileBasedKeyLifecycleManager class deserializes the contents of `&lt;keyId&gt;.key` files in the configured key directory using java.io.ObjectInputStream without applying any ObjectInputFilter or class-loading restrictions. The cast to `java.security.KeyPair` is evaluated only after `readObject()` has already returned, so any `readObject()` side effects in the deserialized object run before the type check. An attacker who can write to the key directory used by a Camel application — for example through a path traversal into the directory, misconfigured filesystem permissions on the volume where keys are stored, a compromised key provisioning pipeline, or a symlink attack — can place a crafted serialized Java object that, when deserialized during normal key lifecycle operations, results in arbitrary code execution in the context of the application.</p><p>This issue affects Apache Camel: from 4.19.0 before 4.20.0, from 4.18.0 before 4.18.2.</p><p>Users are recommended to upgrade to version 4.20.0, which fixes the issue by replacing java.io.ObjectInputStream-based key and metadata storage with standard PKCS#8 (private key) / X.509 SubjectPublicKeyInfo (public key) Base64 JSON encoding. For users on the 4.18.x LTS releases stream, upgrade to 4.18.2.</p>

### References
* https://camel.apache.org/security/CVE-2026-40048.html


### Credits
* Andrea Cosentino from ASF (finder)
* Venkatraman Kumar from Securin (finder)


## Authentication Bypass on Non-Root Context Paths in camel main runtime ## { #CVE-2026-40022 }

CVE-2026-40022 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40022) [\[CVE json\]](./CVE-2026-40022.cve.json) [\[OSV json\]](./CVE-2026-40022.osv.json)



_Last updated: 2026-04-27T09:40:26.613Z_

### Affected

* Apache Camel Platform HTTP Main from 4.14.1 before 4.14.6
* Apache Camel Platform HTTP Main from 4.18.0 before 4.18.2


### Description

<p>When authentication is enabled on the Apache Camel embedded HTTP server or embedded management server (camel-platform-http-main) and a non-root context path such as /api or /admin is configured via camel.server.path or camel.management.path, the BasicAuthenticationConfigurer and JWTAuthenticationConfigurer classes derive the authentication path from properties.getPath() when camel.server.authenticationPath / camel.management.authenticationPath is not explicitly set. Combined with the Vert.x sub-router mounting model - the sub-router is mounted at _path_* and the authentication handler is registered inside the sub-router at the resolved path - this causes the authentication handler to match only the exact configured context path, not its subpaths. Unauthenticated requests to subpaths such as /api/_route_ or /admin/observe/info therefore reach protected business routes and management endpoints without being challenged for credentials. The /observe/info endpoint can disclose runtime metadata such as the user, working directory, home directory, process ID, JVM and operating system information.</p><p>This issue affects Apache Camel: from 4.14.1 before 4.14.6, from 4.18.0 before 4.18.2.</p><p>Users are recommended to upgrade to version 4.20.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, they are suggested to upgrade to 4.14.6. If users are on the 4.18.x LTS releases stream, they are suggested to upgrade to 4.18.2.</p>

### References
* https://camel.apache.org/security/CVE-2026-40022.html


### Credits
* Jihang Yu (finder)


## Inbound Header Filter Missing in MailHeaderFilterStrategy Allows Remote Code Execution via MIME Header Injection (CVE-2025-30177 Variant) ## { #CVE-2026-33454 }

CVE-2026-33454 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33454) [\[CVE json\]](./CVE-2026-33454.cve.json) [\[OSV json\]](./CVE-2026-33454.osv.json)



_Last updated: 2026-04-27T09:42:29.897Z_

### Affected

* Apache Camel from 3.0.0 before 4.14.6
* Apache Camel from 4.15.0 before 4.18.1


### Description

<p>The Camel-Mail component is vulnerable to Camel message header injection. The custom header filter strategy used by the component (MailHeaderFilterStrategy) only filters the 'out' direction via setOutFilterStartsWith, while it does not configure the 'in' direction via setInFilterStartsWith. As a result, when a Camel application consumes mail through camel-mail (for example via from(\"imap://...\") or from(\"pop3://...\")) the inbound filter check is skipped and Camel-prefixed MIME headers are mapped unfiltered into the Exchange. An attacker who can deliver an email to a mailbox monitored by such a consumer can inject Camel-specific headers that, for some Camel components downstream of the mail consumer (such as camel-bean, camel-exec, or camel-sql), can alter the behaviour of the route. This is the same pattern that was previously addressed in camel-undertow (CVE-2025-30177) and the broader incoming-header filter (CVE-2025-27636 and CVE-2025-29891).</p><p>This issue affects Apache Camel: from 3.0.0 before 4.14.6, from 4.15.0 before 4.18.1.</p><p>Users are recommended to upgrade to version 4.19.0, which fixes the issue. If users are on the 4.18.x LTS releases stream, then they are suggested to upgrade to 4.18.1. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.6.</p>

### References
* https://camel.apache.org/security/CVE-2026-33454.html


### Credits
* Hyunwoo Kim (@v4bel) (finder)


## CoAP URI Query Parameter to Exchange Header Injection in camel-coap Allows Single-Packet Pre-Auth Remote Code Execution ## { #CVE-2026-33453 }

CVE-2026-33453 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33453) [\[CVE json\]](./CVE-2026-33453.cve.json) [\[OSV json\]](./CVE-2026-33453.osv.json)



_Last updated: 2026-04-27T09:58:44.714Z_

### Affected

* Apache Camel from 4.14.0 through 4.14.5
* Apache Camel from 4.18.0 before 4.18.1
* Apache Camel at 4.19.0


### Description

<p></p><p>Improperly Controlled Modification of Dynamically-Determined Object Attributes vulnerability in Apache Camel Camel-Coap component.</p><p>Apache Camel's camel-coap component is vulnerable to Camel message header injection, leading to remote code execution when routes forward CoAP requests to header-sensitive producers (e.g. camel-exec)</p>The camel-coap component maps incoming CoAP request URI query parameters directly into Camel Exchange In message headers without applying any HeaderFilterStrategy.  &nbsp; <br>Specifically, CamelCoapResource.handleRequest() iterates over OptionSet.getUriQuery() and calls camelExchange.getIn().setHeader(...) for every query parameter. CoAPEndpoint extends DefaultEndpoint rather than DefaultHeaderFilterStrategyEndpoint, and CoAPComponent does not implement HeaderFilterStrategyComponent; the component contains no references to HeaderFilterStrategy at all.<br><br>As a result, an unauthenticated attacker who can send a single CoAP UDP packet to a Camel route consuming from coap:// can inject arbitrary Camel internal headers (those prefixed with Camel*) into the Exchange. When the route delivers the message to a header-sensitive producer such as camel-exec, camel-sql, camel-bean, camel-file, or template components (camel-freemarker, camel-velocity), the injected headers can alter the producer's behavior. In the case of camel-exec, the CamelExecCommandExecutable and CamelExecCommandArgs headers override the executable and arguments configured on the endpoint, resulting in arbitrary OS command execution under the privileges of the Camel process.<br><br>The producer's output is written back to the Exchange body and returned in the CoAP response payload by CamelCoapResource, giving the attacker an interactive RCE channel without any need for out-of-band exfiltration.<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  <br>Exploitation prerequisites are minimal: a single unauthenticated UDP datagram to the CoAP port (default 5683). CoAP (RFC 7252) has no built-in authentication, and DTLS is optional and disabled by default. Because the protocol is UDP-based, HTTP-layer WAF/IDS controls do not apply.<br><p>This issue affects Apache Camel: from 4.14.0 through 4.14.5, from 4.18.0 before 4.18.1, 4.19.0.</p><p>Users are recommended to upgrade to version 4.18.1 or 4.19.0, fixing the issue.</p><p></p>

### References
* https://camel.apache.org/security/CVE-2026-33453.html


### Credits
* Hyunwoo Kim (@v4bel) (finder)


## Unsafe Java deserialization in camel-consul ConsulRegistry allows arbitrary code execution via malicious values read from the Consul KV store ## { #CVE-2026-27172 }

CVE-2026-27172 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-27172) [\[CVE json\]](./CVE-2026-27172.cve.json) [\[OSV json\]](./CVE-2026-27172.osv.json)



_Last updated: 2026-04-27T09:59:44.109Z_

### Affected

* Apache Camel from 3.0.0 before 4.14.6
* Apache Camel from 4.15.0 before 4.18.1


### Description

<p>The ConsulRegistry in the camel-consul component (class org.apache.camel.component.consul.ConsulRegistry and its inner ConsulRegistryUtils.deserialize method) read Java-serialized values from the Consul KV store and passed them to ObjectInputStream.readObject() without configuring an ObjectInputFilter. An attacker who can write to the Consul KV store backing a Camel ConsulRegistry instance could inject a malicious serialized Java object that is deserialized the next time Camel performs a lookup against that registry, leading to arbitrary code execution in the Camel process. The issue mirrors the class of vulnerability already addressed for other Camel components in CVE-2024-22369, CVE-2024-23114 and CVE-2026-25747, and was overlooked during the original remediation of those CVEs.</p><p>This issue affects Apache Camel: from 3.0.0 before 4.14.6, from 4.15.0 before 4.18.1.</p><p>Users are recommended to upgrade to version 4.19.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.6. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.1.</p>

### References
* https://camel.apache.org/security/CVE-2026-27172.html


### Credits
* Andrea Cosentino from Apache Software Foundation (finder)
* Andrea Cosentino from Apache Software Foundation (remediation developer)


## Deserialization of Untrusted Data in Camel LevelDB ## { #CVE-2026-25747 }

CVE-2026-25747 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-25747) [\[CVE json\]](./CVE-2026-25747.cve.json) [\[OSV json\]](./CVE-2026-25747.osv.json)



_Last updated: 2026-04-03T14:58:52.459Z_

### Affected

* Apache Camel LevelDB from 3.0.0 before 4.10.9
* Apache Camel LevelDB from 4.14.0 before 4.14.5
* Apache Camel LevelDB from 4.15.0 before 4.18.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Camel LevelDB component.</p><span style="background-color: rgb(255, 255, 255);">The Camel-LevelDB DefaultLevelDBSerializer class deserializes data read from the LevelDB aggregation repository using java.io.ObjectInputStream without applying any ObjectInputFilter or class-loading restrictions. An attacker who can write to the LevelDB database files used by a Camel application can inject a crafted serialized Java object that, when deserialized during normal aggregation repository operations, results in arbitrary code execution in the context of the application.</span><br><p>This issue affects Apache Camel: from 4.10.0 before 4.10.8, from 4.14.0 before 4.14.5, from 4.15.0 before 4.18.0.</p><p>Users are recommended to upgrade to version 4.18.0, which fixes the issue. For the 4.10.x LTS releases, users are recommended to upgrade to 4.10.9, while for 4.14.x LTS releases, users are recommended to upgrade to 4.14.5</p>

### References
* https://github.com/oscerd/CVE-2026-25747
* https://camel.apache.org/security/CVE-2026-25747.html


### Credits
* Andrea Cosentino (finder)
* Andrea Cosentino (remediation developer)


## Camel-Keycloak: Cross-Realm Token Acceptance Bypass in KeycloakSecurityPolicy ## { #CVE-2026-23552 }

CVE-2026-23552 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-23552) [\[CVE json\]](./CVE-2026-23552.cve.json) [\[OSV json\]](./CVE-2026-23552.osv.json)



_Last updated: 2026-02-22T15:55:13.482Z_

### Affected

* Apache Camel from 4.15.0 before 4.18.0


### Description

<p>Cross-Realm Token Acceptance Bypass in KeycloakSecurityPolicy Apache Camel Keycloak component.&nbsp;</p><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">The Camel-Keycloak KeycloakSecurityPolicy does not validate the iss (issuer) claim of JWT tokens against the configured realm. A token issued by one Keycloak realm is silently accepted by a policy configured for a completely different realm, breaking tenant isolation.</span></span><br><p>This issue affects Apache Camel: from 4.15.0 before 4.18.0.</p><p>Users are recommended to upgrade to version 4.18.0, which fixes the issue.</p>

### References
* https://camel.apache.org/security/CVE-2026-23552.html
* https://github.com/oscerd/CVE-2026-23552


### Credits
* Andrea Cosentino (finder)
* Andrea Cosentino (remediation developer)


## Cypher injection vulnerability in Camel-Neo4j component ## { #CVE-2025-66169 }

CVE-2025-66169 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-66169) [\[CVE json\]](./CVE-2025-66169.cve.json) [\[OSV json\]](./CVE-2025-66169.osv.json)



_Last updated: 2026-01-14T11:45:34.042Z_

### Affected

* Apache Camel Neo4j from 4.10.0 before 4.10.8
* Apache Camel Neo4j from 4.14.0 before 4.14.3
* Apache Camel Neo4j from 4.15.0 before 4.17.0


### Description

<p>Cypher Injection vulnerability in Apache Camel camel-neo4j component.</p><p>This issue affects Apache Camel: from 4.10.0 before 4.10.8, from 4.14.0 before 4.14.3, from 4.15.0 before 4.17.0</p><p><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 4.10.8 for 4.10.x LTS and 4.14.3 for 4.14.x LTS and 4.17.0.</span></p>

### References
* https://camel.apache.org/security/CVE-2025-66169.html


### Credits
* Ya0H4cker (finder)


## Camel-Undertow Message Header Injection via Improper Filtering ## { #CVE-2025-30177 }

CVE-2025-30177 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-30177) [\[CVE json\]](./CVE-2025-30177.cve.json) [\[OSV json\]](./CVE-2025-30177.osv.json)



_Last updated: 2025-04-01T16:32:28.939Z_

### Affected

* Apache Camel from 4.10.0 before 4.10.3
* Apache Camel from 4.8.0 before 4.8.6


### Description

<p>Bypass/Injection vulnerability in Apache Camel in Camel-Undertow component under particular conditions.</p><p>This issue affects Apache Camel: from 4.10.0 before 4.10.3, from 4.8.0 before 4.8.6.</p>Users are recommended to upgrade to version 4.10.3 for 4.10.x LTS and 4.8.6 for 4.8.x LTS.<br><br><div>Camel undertow component is vulnerable to Camel message header injection, in particular the custom header filter strategy used by the component only filter the "out" direction, while it doesn't filter the "in" direction.</div><br>This allows an attacker to include Camel specific headers that for some Camel components can alter the behaviour such as the camel-bean component, or the camel-exec component.<br><br>

### References
* https://camel.apache.org/security/CVE-2025-27636.html
* https://camel.apache.org/security/CVE-2025-29891.html
* https://lists.apache.org/thread/dj79zdgw01j337lr9gvyy4sv8xfyw8py
* https://camel.apache.org/security/CVE-2025-30177.html


### Credits
* Mark Thorson of AT&T (finder)
* Mark Thorson of AT&T (reporter)


## Camel Message Header Injection through request parameters ## { #CVE-2025-29891 }

CVE-2025-29891 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-29891) [\[CVE json\]](./CVE-2025-29891.cve.json) [\[OSV json\]](./CVE-2025-29891.osv.json)



_Last updated: 2025-03-13T08:19:35.754Z_

### Affected

* Apache Camel from 4.10.0 before 4.10.2
* Apache Camel from 4.8.0 before 4.8.5
* Apache Camel from 3.10.0 before 3.22.4


### Description

<p>Bypass/Injection vulnerability in Apache Camel.</p><p>This issue affects Apache Camel: from 4.10.0 before 4.10.2, from 4.8.0 before 4.8.5, from 3.10.0 before 3.22.4.</p><p>Users are recommended to upgrade to version 4.10.2 for 4.10.x LTS, 4.8.5 for 4.8.x LTS and 3.22.4 for 3.x releases.</p><p>This vulnerability is present in Camel's default incoming header filter, that allows an attacker to include Camel specific headers that for some Camel components can alter the behaviours such as the camel-bean component, or the camel-exec component.</p><p>If you have Camel applications that are directly connected to the internet via HTTP, then an attacker&nbsp;<span style="background-color: rgb(255, 255, 255);">could include parameters in the HTTP requests that are sent to the Camel application that get translated into headers.</span>&nbsp;</p><p>The headers could be both provided as request parameters for an HTTP methods invocation or as part of the payload of the HTTP methods invocation.</p><p><span style="background-color: var(--wht);">All the known Camel HTTP component such as camel-servlet, camel-jetty, camel-undertow, camel-platform-http, and camel-netty-http would be vulnerable out of the box.</span></p><span style="background-color: rgb(255, 255, 255);">This CVE is related to the CVE-2025-27636: while they have the same root cause and are fixed with the same fix, CVE-2025-27636 was assumed to only be exploitable if an attacker could add malicious HTTP headers, while we have now determined that it is also exploitable via HTTP parameters. Like in CVE-2025-27636, exploitation is only possible if the Camel route uses particular vulnerable components.</span><p></p>

### References
* https://camel.apache.org/security/CVE-2025-27636.html
* https://camel.apache.org/security/CVE-2025-29891.html


### Credits
* Citi Cyber Security Operations (finder)
* Akamai Security Intelligence Group (SIG) (reporter)
* Mark Thorson of AT&T (finder)
* Mark Thorson of AT&T (reporter)


## Camel Message Header Injection via Improper Filtering ## { #CVE-2025-27636 }

CVE-2025-27636 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27636) [\[CVE json\]](./CVE-2025-27636.cve.json) [\[OSV json\]](./CVE-2025-27636.osv.json)



_Last updated: 2025-03-17T14:20:17.925Z_

### Affected

* Apache Camel from 4.10.0 before 4.10.2
* Apache Camel from 4.8.0 before 4.8.5
* Apache Camel from 3.10.0 before 3.22.4


### Description

<p>Bypass/Injection vulnerability in Apache Camel components under particular conditions.</p><p>This issue affects Apache Camel: from 4.10.0 through &lt;= 4.10.1, from 4.8.0 through &lt;= 4.8.4, from 3.10.0 through &lt;= 3.22.3.</p><p>Users are recommended to upgrade to version 4.10.2 for 4.10.x LTS, 4.8.5 for 4.8.x LTS and 3.22.4 for 3.x releases.</p><div></div><div>This vulnerability is present in Camel's default incoming header filter, that allows an attacker to include Camel specific</div><div>headers that for some Camel components can alter the behaviours such as the camel-bean component, to call another method</div><div>on the bean, than was coded in the application. In the camel-jms component, then a malicious header can be used to send</div><div>the message to another queue (on the same broker) than was coded in the application. This could also be seen by using the camel-exec component</div><div><br></div><div>The attacker would need to inject custom headers, such as HTTP protocols. So if you have Camel applications that are</div><div>directly connected to the internet via HTTP, then an attacker could include malicious HTTP headers in the HTTP requests</div><div>that are send to the Camel application.</div><div><br></div>All the known Camel HTTP component such as camel-servlet, camel-jetty, camel-undertow, camel-platform-http, and camel-netty-http would be vulnerable out of the box.<br><br>In these conditions an attacker could be able to forge a Camel header name and make the bean component invoking other methods in the same bean.<br><br><div>In terms of usage of the default header filter strategy the list of components using that is: <br></div><div><div><ul><li>camel-activemq</li><li>camel-activemq6</li><li>camel-amqp</li><li>camel-aws2-sqs</li><li>camel-azure-servicebus</li><li>camel-cxf-rest</li><li>camel-cxf-soap</li><li>camel-http</li><li>camel-jetty</li><li>camel-jms</li><li>camel-kafka</li><li>camel-knative</li><li>camel-mail</li><li>camel-nats</li><li>camel-netty-http</li><li>camel-platform-http</li><li>camel-rest</li><li>camel-sjms</li><li>camel-spring-rabbitmq</li><li>camel-stomp</li><li>camel-tahu</li><li>camel-undertow</li><li>camel-xmpp</li></ul></div></div><div>The vulnerability arises due to a bug in the default filtering mechanism that only blocks headers starting with "Camel", "camel", or "org.apache.camel.".&nbsp;</div><br><div><span style="background-color: var(--wht);">Mitigation:&nbsp;</span>You can easily work around this in your Camel applications by removing the&nbsp;headers in your Camel routes. There are many ways of doing this, also&nbsp;globally or per route. This means you could use the removeHeaders EIP, to filter out anything like "cAmel, cAMEL" etc, or in general everything not starting with "Camel", "camel" or "org.apache.camel.".&nbsp;<br></div><br>

### References
* https://lists.apache.org/thread/l3zcg3vts88bmc7w8172wkgw610y693z
* https://issues.apache.org/jira/browse/CAMEL-21828
* https://camel.apache.org/security/CVE-2025-27636.html


### Credits
* Mark Thorson (finder)


## Camel-CassandraQL: Unsafe Deserialization from CassandraAggregationRepository ## { #CVE-2024-23114 }

CVE-2024-23114 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23114) [\[CVE json\]](./CVE-2024-23114.cve.json) [\[OSV json\]](./CVE-2024-23114.osv.json)



_Last updated: 2024-02-20T14:59:36.356Z_

### Affected

* Apache Camel from 3.0.0 before 3.21.4
* Apache Camel from 3.22.0 before 3.22.1
* Apache Camel from 4.0.0 before 4.0.4
* Apache Camel from 4.1.0 before 4.4.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Camel CassandraQL Component AggregationRepository which is vulnerable to unsafe deserialization. Under specific conditions it is possible to deserialize malicious payload.<p>This issue affects Apache Camel: from 3.0.0 before 3.21.4, from 3.22.0 before 3.22.1, from 4.0.0 before 4.0.4, from 4.1.0 before 4.4.0.</p><p>Users are recommended to upgrade to version 4.4.0, which fixes the issue.&nbsp;If users are on the 4.0.x LTS releases stream, then they are suggested to upgrade to 4.0.4. If users are on 3.x, they are suggested to move to 3.21.4 or 3.22.1</p>

### References
* https://camel.apache.org/security/CVE-2024-23114.html


### Credits
* Federico Mariani From Apache Software Foundation (finder)
* Andrea Cosentino from Apache Software Foundation (finder)


## Apache Camel issue on ExchangeCreatedEvent ## { #CVE-2024-22371 }

CVE-2024-22371 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-22371) [\[CVE json\]](./CVE-2024-22371.cve.json)

_Last updated: 2024-02-26T09:22:36.071Z_

### Affected

* Apache Camel from 1.x through 1.6.0 unaffected
* Apache Camel from 3.21.x through 3.21.3
* Apache Camel from 3.22.x through 3.22.0
* Apache Camel from 4.0.x through 4.0.3
* Apache Camel from 4.x through 4.3.0


### Description

Exposure of sensitive data by by crafting a malicious EventFactory and providing a custom ExchangeCreatedEvent that exposes sensitive data. Vulnerability in Apache Camel.<p>This issue affects Apache Camel: from 3.21.X through 3.21.3, from 3.22.X through 3.22.0, from 4.0.X through 4.0.3, from 4.X through 4.3.0.</p><p>Users are recommended to upgrade to version 3.21.4, 3.22.1, 4.0.4 or 4.4.0, which fixes the issue.</p>

### References
* https://camel.apache.org/security/CVE-2024-22371.html


### Credits
* Otavio Rodolfo Piske from the Apache Software Foundation (finder)


## Camel-SQL: Unsafe Deserialization from JDBCAggregationRepository ## { #CVE-2024-22369 }

CVE-2024-22369 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-22369) [\[CVE json\]](./CVE-2024-22369.cve.json) [\[OSV json\]](./CVE-2024-22369.osv.json)



_Last updated: 2024-02-20T15:01:05.582Z_

### Affected

* Apache Camel from 3.0.0 before 3.21.4
* Apache Camel from 3.22.0 before 3.22.1
* Apache Camel from 4.0.0 before 4.0.4
* Apache Camel from 4.1.0 before 4.4.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Camel SQL Component<p>This issue affects Apache Camel: from 3.0.0 before 3.21.4, from 3.22.0 before 3.22.1, from 4.0.0 before 4.0.4, from 4.1.0 before 4.4.0.</p><p>Users are recommended to upgrade to version 4.4.0, which fixes the issue. If users are on the 4.0.x LTS releases stream, then they are suggested to upgrade to 4.0.4. If users are on 3.x, they are suggested to move to 3.21.4 or 3.22.1</p>

### References
* https://lists.apache.org/thread/3dko781dy2gy5l3fs48p56fgp429yb0f
* https://camel.apache.org/security/CVE-2024-22369.html


### Credits
* Ziyang Chen from HuaWei Open Source Management Center (finder)
* Pingtao Wei from HuaWei Open Source Management Center (finder)
* Haoran Zhi from HuaWei Open Source Management Center (finder)


## Temporary file information disclosure in Camel-Jira ## { #CVE-2023-34442 }

CVE-2023-34442 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-34442) [\[CVE json\]](./CVE-2023-34442.cve.json) [\[OSV json\]](./CVE-2023-34442.osv.json)



_Last updated: 2023-07-10T09:31:01.757Z_

### Affected

* Apache Camel JIRA from 3.x through <=3.14.8
* Apache Camel JIRA from 3.18.x through <=3.18.7
* Apache Camel JIRA from 3.20.x through <= 3.20.5
* Apache Camel JIRA from 4.x through <= 4.0.0-M3


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Camel.<p>This issue affects Apache Camel: from 3.X through &lt;=3.14.8, from 3.18.X through &lt;=3.18.7, from 3.20.X through &lt;= 3.20.5, from 4.X through &lt;= 4.0.0-M3.</p><span style="background-color: rgb(255, 255, 255);">Users should upgrade to 3.14.9, 3.18.8, 3.20.6 or 3.21.0 and for users on Camel 4.x update to 4.0.0-M1</span><br>

### References
* https://lists.apache.org/thread/x4vy2hhbltb1xrvy1g6m8hpjgj2k7wgh


### Credits
* Jonathan Leitschuh of the Open Source Security Foundation: Project Alpha-Omega (reporter)
