---
title: Apache Camel security advisories
description: Security information for Apache Camel
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Camel? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=%5BFINDING%5D%20Apache%20Camel).

You can read more about the security policy on:

- [Apache Camel security model](https://camel.apache.org/manual/security-model.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## An inbound Camel-namespace filter was added to Sns2HeaderFilterStrategy to align it with sibling components ## { #CVE-2026-56140 }

CVE-2026-56140 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-56140) [\[CVE json\]](./CVE-2026-56140.cve.json) [\[OSV json\]](./CVE-2026-56140.osv.json)



_Last updated: 2026-07-06T08:15:59.205Z_

### Affected

* Apache Camel AWS2 SNS from 4.0.0 before 4.14.8
* Apache Camel AWS2 SNS from 4.15.0 before 4.18.3
* Apache Camel AWS2 SNS from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation vulnerability in Apache Camel AWS SNS component.<br></p><p>The camel-aws2-sns component filters Camel headers through a component-specific HeaderFilterStrategy, Sns2HeaderFilterStrategy. Like the sibling Sqs2HeaderFilterStrategy, it originally configured only an outbound filter (setOutFilterPattern, which blocks Camel*, breadcrumbId and org.apache.camel.* headers from being written out) and did not configure an inbound filter rule. For the related camel-aws2-sqs component this inbound gap was exploitable, because the Sqs2Consumer maps inbound SQS message attributes into the Camel Exchange via HeaderFilterStrategy.applyFilterToExternalHeaders, allowing a message sender to inject Camel control headers (tracked as CVE-2026-46456). camel-aws2-sns, by contrast, is producer-only: Sns2Endpoint does not support consumers (createConsumer throws UnsupportedOperationException, 'You cannot receive messages from this endpoint'), so no externally-supplied message attributes are ever mapped inbound into a Camel Exchange through SNS, and the missing inbound filter rule on Sns2HeaderFilterStrategy was therefore not reachable by an attacker. As part of the same fix (CAMEL-23506), an inbound filter rule (setInFilterStartsWith for the Camel namespace) was added to Sns2HeaderFilterStrategy so that its configuration matches the corrected Sqs2HeaderFilterStrategy and the other sibling strategies. This is a defense-in-depth alignment with no known exploit path in camel-aws2-sns.<br></p><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>This is a defense-in-depth hardening change with no known exploit path in camel-aws2-sns, which is producer-only, so no urgent action or workaround is required. Users who want the aligned behaviour can upgrade to version 4.21.0, or to 4.14.8 on the 4.14.x LTS releases stream, or to 4.18.3 on the 4.18.x releases stream, which contain the change. As a general best practice, operators should continue to apply least-privilege IAM permissions on their SNS topics.</p>

### References
* https://camel.apache.org/security/CVE-2026-56140.html


### Credits
* Yu Bao from PayPal (finder)
* Andrea Cosentino (remediation developer)


## The muteException consumer option defaulted to false, so a processing error returned the full Java stack trace in the HTTP response body, disclosing sensitive internal information to unauthenticated clients ## { #CVE-2026-56139 }

CVE-2026-56139 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-56139) [\[CVE json\]](./CVE-2026-56139.cve.json) [\[OSV json\]](./CVE-2026-56139.osv.json)



_Last updated: 2026-07-06T08:15:07.275Z_

### Affected

* Apache Camel Undertow from 4.0.0 before 4.14.8
* Apache Camel Undertow from 4.15.0 before 4.18.3
* Apache Camel Undertow from 4.19.0 before 4.21.0


### Description

<p>Generation of Error Message Containing Sensitive Information vulnerability in Apache Camel Undertow Component.</p>The camel-undertow HTTP server consumer exposes a muteException option that controls what is returned to the client when a route processing error occurs. This option defaulted to false, whereas the other Camel HTTP server components (camel-http / camel-jetty / camel-servlet and camel-platform-http) default it to true. With muteException=false, when a request triggers an exception during route processing the consumer writes the full Throwable stack trace into the HTTP response body as text/plain instead of returning an empty body. Any unauthenticated client that can reach the endpoint and cause a processing error - for example by sending a malformed request body, an invalid parameter, or otherwise triggering a route-internal failure - therefore receives a complete Java stack trace. Such a stack trace can disclose sensitive internal information, including credentials embedded in exception messages, internal host names and IP addresses, filesystem paths, dependency and version details, database and class names, and the application's internal structure, which an attacker can use to plan further attacks. In addition, for Rest DSL consumers the muteException option was not honoured at all: the RestUndertowHttpBinding was created with a hard-coded false, so the stack trace was returned even when muteException=true had been configured.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. For deployments that cannot upgrade immediately, set muteException=true explicitly on the camel-undertow consumer (for example undertow:<a target="_blank" rel="nofollow" href="http://0.0.0.0:8080/api?muteException=true">http://0.0.0.0:8080/api?muteException=true</a>, or globally via the camel.component.undertow.mute-exception=true property), so that processing errors no longer return the stack trace to the client; note that on affected releases this workaround does not cover Rest DSL consumers, whose binding ignores the option until the fix is applied.</p>

### References
* https://camel.apache.org/security/CVE-2026-56139.html


### Credits
* Yu Bao from PayPal (finder)
* Andrea Cosentino (remediation developer)


## The inbound consumer maps externally-supplied Iggy message user-headers into the Exchange without a HeaderFilterStrategy, allowing injection of Camel control headers - enabling control over internal behaviour ## { #CVE-2026-55994 }

CVE-2026-55994 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-55994) [\[CVE json\]](./CVE-2026-55994.cve.json) [\[OSV json\]](./CVE-2026-55994.osv.json)



_Last updated: 2026-07-06T08:13:58.182Z_

### Affected

* Apache Camel Iggy from 4.17.0 before 4.18.3
* Apache Camel Iggy from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Exposure of Sensitive Information to an Unauthorized Actor, Server-Side Request Forgery (SSRF) vulnerability in Apache Camel in Iggy component.</p>The camel-iggy consumer mapped the user-headers of inbound Iggy messages into the Camel Exchange header map without applying any HeaderFilterStrategy (IggyFetchRecords copied the message user-headers straight into the Exchange). Because nothing blocked the Camel header namespace, an actor able to publish to the consumed Iggy stream/topic could set Camel-internal control headers - including CamelHttpUri (Exchange.HTTP_URI) - simply by supplying them as message user-headers. In a route where the Iggy consumer feeds a downstream HTTP producer, the injected CamelHttpUri redirects the server-side HTTP request to an attacker-chosen destination (server-side request forgery - for example to an internal service or a cloud metadata endpoint). In addition, the HTTP producer resolves Camel property placeholders on the resulting (attacker-controlled) URI, so placeholders embedded in the injected value - such as an environment-variable reference, an application property, or a vault reference - are resolved to their real values and sent to the attacker, disclosing environment variables, application properties and vault secrets.<br><p>This issue affects Apache Camel: from 4.17.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. The fix adds a dedicated IggyHeaderFilterStrategy (and a headerFilterStrategy endpoint option) that filters the Camel header namespace case-insensitively on inbound mapping, so externally-supplied Camel* / camel* headers are no longer copied into the Exchange. For deployments that cannot upgrade immediately, strip the Camel control headers from the inbound message before they reach any downstream producer (for example removeHeaders('Camel*') and removeHeaders('camel*') at the start of the route), restrict who can publish to the consumed Iggy stream/topic, and avoid bridging an untrusted consumer directly into an HTTP producer whose target URI can be driven from message headers.</p>

### References
* https://camel.apache.org/security/CVE-2026-55994.html


### Credits
* Kamalpreet Singh (finder)
* Andrea Cosentino (remediation reviewer)


## The inbound consumer maps externally-supplied WebSocket query parameters into the Exchange without a HeaderFilterStrategy, allowing injection of Camel control headers - enabling influencing internal behaviour ## { #CVE-2026-55993 }

CVE-2026-55993 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-55993) [\[CVE json\]](./CVE-2026-55993.cve.json) [\[OSV json\]](./CVE-2026-55993.osv.json)



_Last updated: 2026-07-06T08:13:23.425Z_

### Affected

* Apache Camel Atmosphere Websocket from 4.0.0 before 4.14.8
* Apache Camel Atmosphere Websocket from 4.15.0 before 4.18.3
* Apache Camel Atmosphere Websocket from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Exposure of Sensitive Information to an Unauthorized Actor, Server-Side Request Forgery (SSRF) vulnerability in Apache Camel in Atmosphere Websocket Component.</p>The camel-atmosphere-websocket consumer mapped inbound WebSocket query parameters into the Camel Exchange header map without applying any HeaderFilterStrategy (WebsocketConsumer.sendEventNotification() iterates the query-string map collected in WebsocketConsumer.service() and copies each entry into the Exchange). Because nothing blocked the Camel header namespace, a client connecting to the WebSocket endpoint could set Camel-internal control headers - including CamelHttpUri (Exchange.HTTP_URI) - simply by supplying them as query parameters. In a route where the WebSocket consumer feeds a downstream HTTP producer, the injected CamelHttpUri redirects the server-side HTTP request to an attacker-chosen destination (server-side request forgery - for example to an internal service or a cloud metadata endpoint). In addition, the HTTP producer resolves Camel property placeholders on the resulting (attacker-controlled) URI, so placeholders embedded in the injected value - such as an environment-variable reference, an application property, or a vault reference - are resolved to their real values and sent to the attacker, disclosing environment variables, application properties and vault secrets. When the WebSocket endpoint is exposed without authentication, this is reachable by an unauthenticated remote attacker.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. The fix makes the consumer apply the HeaderFilterStrategy it already inherits from the HTTP/servlet stack, filtering the Camel header namespace case-insensitively on inbound mapping, so externally-supplied Camel* / camel* headers are no longer copied into the Exchange. For deployments that cannot upgrade immediately, strip the Camel control headers from the inbound message before they reach any downstream producer (for example removeHeaders('Camel*') and removeHeaders('camel*') at the start of the route), require authentication on the WebSocket endpoint, and avoid bridging an untrusted consumer directly into an HTTP producer whose target URI can be driven from message headers.</p>

### References
* https://camel.apache.org/security/CVE-2026-55993.html


### Credits
* Kamalpreet Singh (finder)
* Andrea Cosentino (remediation developer)


## KeycloakSecurityPolicy verifies the bearer access token only inside its role and permission checks, so in the default configuration the token is never verified and any non-null bearer value is accepted ## { #CVE-2026-53913 }

CVE-2026-53913 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-53913) [\[CVE json\]](./CVE-2026-53913.cve.json) [\[OSV json\]](./CVE-2026-53913.osv.json)



_Last updated: 2026-07-06T08:12:31.281Z_

### Affected

* Apache Camel Keycloak from 4.15.0 before 4.18.3
* Apache Camel Keycloak from 4.19.0 before 4.21.0


### Description

<p>Improper Authentication, Missing Authentication for Critical Function, Not Failing Securely ('Failing Open') vulnerability in Apache Camel Keycloak Component.</p>The KeycloakSecurityPolicy of camel-keycloak guards a route by running KeycloakSecurityProcessor.beforeProcess(), which performs three checks in sequence: it rejects a request that carries no access token, then - only if requiredRoles is non-empty - validates the roles, and - only if requiredPermissions is non-empty - validates the permissions. The actual cryptographic verification of the bearer access token (signature, issuer and expiry for a local JWT, or active-state and issuer for token introspection) is performed exclusively inside those role and permission checks. KeycloakSecurityPolicy defaults requiredRoles and requiredPermissions to empty - which is the documented 'Basic Setup' - so on a route configured that way the role and permission checks are skipped and the access token is therefore never verified. The token-presence check still rejects a missing token, but an invalid token is accepted: any non-null value in the Authorization: Bearer header - including an arbitrary string or a forged, unsigned JWT - passes the policy and the request reaches the protected route, with no signature, issuer or expiry check and no request to Keycloak. The token is read from the inbound request header because allowTokenFromHeader defaults to true. Because the normal reason to place a route behind this policy is that the route performs server-side work, the bypass results in unauthenticated access to that work; where the protected route forwards to a code-execution-capable producer, it can result in unauthenticated remote code execution. This defect is independent of CVE-2026-23552: that issue concerned the issuer claim and was fixed by adding a check inside the verification routine, but here the verification routine is not reached at all in the default configuration, so the defect remains.<br><p>This issue affects Apache Camel: from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. For deployments that cannot upgrade immediately, configure a non-empty requiredRoles or requiredPermissions on every KeycloakSecurityPolicy so that the token-verification path is exercised, set allowTokenFromHeader to false where the token is not expected from the request header, or perform token verification at the framework layer ahead of the policy.</p>

### References
* https://camel.apache.org/security/CVE-2026-53913.html


### Credits
* Lidor Ben Shitrit from Novee Security (finder)
* Andrea Cosentino (remediation developer)


## Camel-Netty-HTTP: The muteException consumer option defaulted to false, so a processing error returned the full Java stack trace in the HTTP response body, disclosing sensitive internal information to unauthenticated clients ## { #CVE-2026-49365 }

CVE-2026-49365 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49365) [\[CVE json\]](./CVE-2026-49365.cve.json) [\[OSV json\]](./CVE-2026-49365.osv.json)



_Last updated: 2026-07-05T11:49:54.080Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Generation of Error Message Containing Sensitive Information vulnerability in Apache Camel Netty HTTP component.</p>The camel-netty-http HTTP server consumer exposes a muteException option that controls what is returned to the client when a route processing error occurs. This option defaulted to false because the backing field was an uninitialised primitive boolean (Java's default of false), whereas the other Camel HTTP server components (camel-http / camel-jetty / camel-servlet and camel-platform-http) default it to true. With muteException=false, when a request triggers an exception during route processing the consumer writes the full Throwable stack trace into the HTTP response body as text/plain (via DefaultNettyHttpBinding) instead of returning an empty body. Any unauthenticated client that can reach the endpoint and cause a processing error - for example by sending a malformed request body, an invalid parameter, or otherwise triggering a route-internal failure - therefore receives a complete Java stack trace. Such a stack trace can disclose sensitive internal information, including credentials embedded in exception messages, internal host names and IP addresses, filesystem paths, dependency and version details, database and class names, and the application's internal structure, which an attacker can use to plan further attacks.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. For deployments that cannot upgrade immediately, set muteException=true explicitly on the camel-netty-http consumer (for example netty-http:<a target="_blank" rel="nofollow" href="http://0.0.0.0:8080/api?muteException=true">http://0.0.0.0:8080/api?muteException=true</a>, or globally via the camel.component.netty-http.configuration.mute-exception=true property), so that processing errors no longer return the stack trace to the client.</p>

### References
* https://camel.apache.org/security/CVE-2026-49365.html


### Credits
* Yu Bao from PayPal (finder)
* Andrea Cosentino (remediation developer)


## Non-Camel-prefixed Exchange header constants bypass the HTTP header filter, allowing an HTTP client to influence internal behaviour ## { #CVE-2026-49099 }

CVE-2026-49099 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49099) [\[CVE json\]](./CVE-2026-49099.cve.json) [\[OSV json\]](./CVE-2026-49099.osv.json)



_Last updated: 2026-07-06T08:11:29.239Z_

### Affected

* Apache Camel Salesforce from 4.0.0 before 4.14.8
* Apache Camel Salesforce from 4.15.0 before 4.18.3
* Apache Camel Salesforce from 4.19.0 before 4.21.0


### Description

<p>Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection'), Authorization Bypass Through User-Controlled Key vulnerability in Apache Camel Salesforce Component.</p>The camel-salesforce producer resolves its operation parameters - the SOQL query, the SOSL search, the target SObject name and id, the Apex REST URL and method, and the Apex query parameters - from Exchange message headers, reading the header in preference to the value configured on the endpoint (AbstractSalesforceProcessor.getParameter() reads the header first and uses the endpoint configuration only as a fallback). The control-header constants in SalesforceEndpointConfig (for example SOBJECT_QUERY = sObjectQuery, SOBJECT_SEARCH = sObjectSearch, SOBJECT_NAME = sObjectName, SOBJECT_ID = sObjectId, APEX_URL = apexUrl, APEX_METHOD = apexMethod, and the apexQueryParam. prefix) used plain, non-Camel-prefixed values. Because these names do not start with the Camel / camel prefix, HttpHeaderFilterStrategy - which blocks only the Camel header namespace on the HTTP boundary - let them pass from an inbound HTTP request straight into the Exchange. In a route that bridges an HTTP consumer (for example platform-http) into a salesforce: producer, any HTTP client could therefore set these headers and override what the route intended - supplying its own SOQL query or SOSL search to read data from any SObject the connected Salesforce user can access, overriding the target SObject name and id for CRUD operations, or redirecting an Apex REST call to a different endpoint and HTTP method (including destructive methods) with injected query parameters. All such operations run with the full permissions of the Salesforce connected (integration) user, which is typically broad. No credentials are required from the attacker when the bridging consumer is unauthenticated.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, routes that set Salesforce operation parameters via the raw header names must use the CamelSalesforce* names (for example CamelSalesforceSObjectQuery and CamelSalesforceApexUrl) instead of the old sObject* / apex* values; the endpoint-option spelling is unchanged. For deployments that cannot upgrade immediately, strip the Salesforce control headers from any untrusted ingress before the salesforce: producer (for example removeHeaders('sObject*') and removeHeaders('apex*') at the start of the route), and set the query, SObject and Apex parameters from a trusted source.</p>

### References
* https://camel.apache.org/security/CVE-2026-49099.html


### Credits
* Yu Bao from PayPal (finder)
* Andrea Cosentino (remediation developer)


## Camel-Kafka: The kafka.OVERRIDE_TOPIC (and other kafka.*) Exchange header constants used non-Camel-prefixed names that bypass the upstream HTTP header filter, allowing an HTTP client to redirect Kafka messages to an arbitrary topic ## { #CVE-2026-49098 }

CVE-2026-49098 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49098) [\[CVE json\]](./CVE-2026-49098.cve.json) [\[OSV json\]](./CVE-2026-49098.osv.json)



_Last updated: 2026-07-05T11:51:10.500Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection') vulnerability in Apache Camel Kafka Component.</p>The camel-kafka producer can override its configured target topic at runtime from the kafka.OVERRIDE_TOPIC Exchange header: KafkaProducer.evaluateTopic() returns the header value in preference to the topic configured on the endpoint. The control-header constants in KafkaConstants (for example OVERRIDE_TOPIC = kafka.OVERRIDE_TOPIC, OVERRIDE_TIMESTAMP = kafka.OVERRIDE_TIMESTAMP, PARTITION_KEY = kafka.PARTITION_KEY) used plain, non-Camel-prefixed values. camel-kafka's own KafkaHeaderFilterStrategy does filter the kafka.* namespace, but only on the Kafka-to-Exchange serialization boundary (reading Kafka record headers into the Exchange, and writing Exchange headers into a Kafka record); it does not apply to headers that arrive from an upstream consumer in a multi-component route. The upstream HTTP consumer uses HttpHeaderFilterStrategy, which blocks only the Camel / camel namespace, so a kafka.* header passes through unfiltered. As a result, in a route that bridges an HTTP consumer (for example platform-http) into a kafka: producer, any HTTP client could set the kafka.OVERRIDE_TOPIC header and cause the message to be published to an arbitrary Kafka topic instead of the configured one - redirecting it to a sensitive internal topic, or injecting attacker-crafted messages into a topic consumed by a critical downstream service. The related kafka.OVERRIDE_TIMESTAMP and kafka.PARTITION_KEY headers could likewise be injected to backdate messages or target specific partitions. No credentials are required when the bridging consumer is unauthenticated.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, routes that set or read Kafka headers via the raw header names must use the CamelKafka* names (for example CamelKafkaOverrideTopic and CamelKafkaTopic) instead of the old kafka.* values. For deployments that cannot upgrade immediately, strip the kafka.* headers from any untrusted ingress before the kafka: producer (for example removeHeaders('kafka.*') at the start of the route), and set the target topic from a trusted source.</p>

### References
* https://camel.apache.org/security/CVE-2026-49098.html


### Credits
* Yu Bao from PayPal (finder)
* Andrea Cosentino (remediation developer)


## Camel-IRC: The irc.sendTo (and other irc.*) Exchange header constants used non-Camel-prefixed names that bypass the HTTP header filter, allowing an HTTP client to redirect outgoing IRC messages to arbitrary channels or users ## { #CVE-2026-49097 }

CVE-2026-49097 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49097) [\[CVE json\]](./CVE-2026-49097.cve.json) [\[OSV json\]](./CVE-2026-49097.osv.json)



_Last updated: 2026-07-05T11:51:47.659Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection') vulnerability in Apache Camel IRC component.</p>The camel-irc producer chooses the destination of an outgoing IRC message from the irc.sendTo Exchange header (the constant IrcConstants.IRC_SEND_TO, value irc.sendTo); when that header is present it overrides the channel list configured on the endpoint, and the message is sent only to the specified destination. This and the component's other control headers (irc.target, irc.messageType, irc.user.*, irc.num, irc.value) used plain, non-Camel-prefixed values. Because these names do not start with the Camel / camel prefix, HttpHeaderFilterStrategy - which blocks only the Camel header namespace on the HTTP boundary - let them pass from an inbound HTTP request straight into the Exchange. In a route that bridges an HTTP consumer (for example platform-http) into an irc: producer, any HTTP client could therefore set the irc.sendTo header and redirect a message that the route intended for a configured channel to an arbitrary IRC channel or user - exfiltrating the message content to an attacker-chosen nickname, leaking it into a public channel, or delivering messages that appear to come from the bot. No credentials are required when the bridging consumer is unauthenticated.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, routes that set IRC headers via the raw header names must use the CamelIrc* names (for example CamelIrcSendTo) instead of the old irc.* values. For deployments that cannot upgrade immediately, strip the irc.* headers from any untrusted ingress before the irc: producer (for example removeHeaders('irc.*') at the start of the route), and set the IRC destination from a trusted source.</p>

### References
* https://camel.apache.org/security/CVE-2026-49097.html


### Credits
* Yu Bao from PayPal (finder)
* Andrea Cosentino (remediation developer)


## Pub/Sub consumer copied the inbound CloudEvent's pub/sub-name and topic into producer-direction routing headers, allowing an actor who can publish to the subscribed topic to influence internal behaviour ## { #CVE-2026-49086 }

CVE-2026-49086 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49086) [\[CVE json\]](./CVE-2026-49086.cve.json) [\[OSV json\]](./CVE-2026-49086.osv.json)



_Last updated: 2026-07-06T08:10:05.908Z_

### Affected

* Apache Camel Dapr from 4.12.0 before 4.14.8
* Apache Camel Dapr from 4.15.0 before 4.18.3
* Apache Camel Dapr from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Unintended Proxy or Intermediary ('Confused Deputy') vulnerability in Apache Camel DAPR component.</p>The camel-dapr Dapr Pub/Sub consumer (DaprPubSubConsumer) copied two fields from each inbound CloudEvent - its Pub/Sub component name and its topic - into the CamelDaprPubSubName and CamelDaprTopic Exchange headers. These two headers are producer-direction routing headers: when the route republishes through a Dapr producer, DaprConfigurationOptionsProxy reads them back and prefers them over the destination configured on the endpoint. As a result, in a route that consumes from one Dapr Pub/Sub topic and republishes to another (for example from('dapr-pubsub:p:t').to('dapr-pubsub:p:other')), an actor able to publish a message to the subscribed topic could set the CloudEvent's pub/sub-name and topic to values of their choosing and cause the re-published message to be delivered to an arbitrary Dapr Pub/Sub component and topic instead of the configured destination - redirecting or exfiltrating the message and bypassing the route's intended routing and any topic-level access controls in the underlying broker. Exploitation requires the ability to publish to the topic the route subscribes to; no other authentication or user interaction is needed.<br><p>This issue affects Apache Camel: from 4.12.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. For deployments that cannot upgrade immediately, remove the CamelDaprPubSubName and CamelDaprTopic headers from the Exchange between the Dapr consumer and any Dapr producer in the route (for example removeHeaders('CamelDaprPubSubName', 'CamelDaprTopic')), and restrict who can publish to the subscribed Dapr Pub/Sub topic so that only trusted producers can send to it.</p>

### References
* https://camel.apache.org/security/CVE-2026-49086.html


### Credits
* Leon Zlobecki (finder)
* Andrea Cosentino (remediation developer)


## langchain4j-tools: filter tool argument headers against declared parameters ## { #CVE-2026-49042 }

CVE-2026-49042 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49042) [\[CVE json\]](./CVE-2026-49042.cve.json) [\[OSV json\]](./CVE-2026-49042.osv.json)



_Last updated: 2026-07-06T09:25:44.186Z_

### Affected

* Apache Camel from 4.8.0 through 4.18.2
* Apache Camel from 4.19.0 through 4.20.0


### Description

<p>Improper Input Validation vulnerability in Apache Camel.</p><p>This issue affects Apache Camel: from 4.8.0 through 4.18.2, from 4.19.0 through 4.20.0.</p><p>Users are recommended to upgrade to version 4.18.3, 4.21.0, which fixes the issue.</p><br>

### References
* https://camel.apache.org/security/CVE-2026-49042.html


### Credits
* Yu Bao - yubao@paypal.com, who works for paypal.com. (reporter)


## A set of non-Camel-prefixed Exchange header constants bypass the HTTP header filter, allowing an HTTP client to drive arbitrary JIRA issue operations using the endpoint's configured credentials ## { #CVE-2026-48206 }

CVE-2026-48206 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48206) [\[CVE json\]](./CVE-2026-48206.cve.json) [\[OSV json\]](./CVE-2026-48206.osv.json)



_Last updated: 2026-07-06T08:09:07.730Z_

### Affected

* Apache Camel JIRA from 4.0.0 before 4.14.8
* Apache Camel JIRA from 4.15.0 before 4.18.3
* Apache Camel JIRA from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Authorization Bypass Through User-Controlled Key vulnerability in Apache Camel JIRA component.</p>The camel-jira producers read their operation parameters - the issue key, project key, transition id, summary, type, assignee, components, watchers, link type, work-log minutes and others - from Exchange message headers. The header constants defined in JiraConstants (for example ISSUE_KEY = IssueKey, ISSUE_PROJECT_KEY = ProjectKey, ISSUE_TRANSITION_ID = IssueTransitionId, LINK_TYPE = linkType) used plain, non-Camel-prefixed values. Because these names do not start with the Camel / camel prefix, HttpHeaderFilterStrategy - which blocks only the Camel header namespace on the HTTP boundary - let them pass from an inbound HTTP request straight into the Exchange. In a route that bridges an HTTP consumer (for example platform-http) into a jira: producer, any HTTP client could therefore supply these headers and override the values the route intended, driving JIRA operations against the configured JIRA instance with the endpoint's configured service-account credentials - for example deleting or transitioning an arbitrary issue (via IssueKey / IssueTransitionId), creating an issue in a different project (via ProjectKey), modifying issue fields, adding or removing watchers, or logging work. The operations are bounded by what the configured service account is permitted to do. No credentials are required from the attacker when the bridging consumer is unauthenticated.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, routes that drive JIRA operations via the raw header names must use the CamelJira* names (for example CamelJiraIssueKey) instead of the old values. For deployments that cannot upgrade immediately, strip the camel-jira control headers from any untrusted ingress before the jira: producer (for example removing the IssueKey, ProjectKey, IssueTransitionId and related headers at the start of the route), and set the required JIRA operation parameters from a trusted source.</p>

### References
* https://camel.apache.org/security/CVE-2026-48206.html


### Credits
* Yu Bao from PayPal (finder)
* Andrea Cosentino (remediation developer)


## The dns.* and term Exchange header constants used non-Camel-prefixed names that bypass the HTTP header filter, allowing an HTTP client to influence internal behaviour ## { #CVE-2026-48205 }

CVE-2026-48205 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48205) [\[CVE json\]](./CVE-2026-48205.cve.json) [\[OSV json\]](./CVE-2026-48205.osv.json)



_Last updated: 2026-07-06T08:08:18.509Z_

### Affected

* Apache Camel DNS from 4.0.0 before 4.14.8
* Apache Camel DNS from 4.15.0 before 4.18.3
* Apache Camel DNS from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Server-Side Request Forgery (SSRF) vulnerability in Apache Camel DNS component.</p>The camel-dns producers read DNS operation parameters - the resolver to query, the name or domain to look up, the record type and class, and the search term - from Exchange message headers whose constant values (DnsConstants.DNS_SERVER, DNS_NAME, DNS_DOMAIN, DNS_TYPE, DNS_CLASS, TERM) were the plain strings dns.server, dns.name, dns.domain, dns.type, dns.class and term. Because these names do not start with the Camel / camel prefix, HttpHeaderFilterStrategy - which blocks only the Camel header namespace on the HTTP boundary - let them pass from an inbound HTTP request straight into the Exchange. In a route that bridges an HTTP consumer (for example platform-http) into a dns: producer, any HTTP client could therefore set the dns.server header to make the dig producer build a SimpleResolver pointing at an attacker-controlled DNS server - a server-side request forgery via DNS, through which the attacker observes the queried name and can return poisoned responses - and set the dns.name / dns.domain headers to resolve arbitrary internal hostnames, disclosing whether they exist (internal network reconnaissance). No credentials are required when the bridging consumer is unauthenticated.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, routes that drive DNS operations via the raw header names must use CamelDnsServer / CamelDnsName / CamelDnsDomain / CamelDnsType / CamelDnsClass / CamelDnsTerm instead of the dns.* / term names. For deployments that cannot upgrade immediately, strip the dns.* and term headers from any untrusted ingress before the dns: producer, and set the DNS server and lookup parameters from a trusted source in the route.</p>

### References
* https://camel.apache.org/security/CVE-2026-48205.html


### Credits
* Yu Bao from PayPal (finder)
* Andrea Cosentino (remediation developer)


## Camel-MongoDB-GridFS: The gridfs.* control headers used non-Camel-prefixed names that bypass the HTTP header filter, allowing an HTTP client to switch the GridFS operation - including destructive file deletion - in the default configuration ## { #CVE-2026-48204 }

CVE-2026-48204 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48204) [\[CVE json\]](./CVE-2026-48204.cve.json) [\[OSV json\]](./CVE-2026-48204.osv.json)



_Last updated: 2026-07-05T11:54:33.844Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Improper Access Control vulnerability in Apache Camel in Camel Mongodb Gridfs component.</p>The camel-mongodb-gridfs producer selects the GridFS operation to perform from the gridfs.operation Exchange header when the endpoint's operation parameter is not set - which is the default. The control-header constants (GridFsConstants.GRIDFS_OPERATION, GRIDFS_OBJECT_ID, GRIDFS_METADATA, GRIDFS_CHUNKSIZE, GRIDFS_FILE_ID_PRODUCED) were the plain strings gridfs.operation, gridfs.objectid, gridfs.metadata, gridfs.chunksize and gridfs.fileid. Because these names do not start with the Camel / camel prefix, HttpHeaderFilterStrategy - which blocks only the Camel header namespace on the HTTP boundary - let them pass from an inbound HTTP request straight into the Exchange. In a route that bridges an HTTP consumer (for example platform-http) into a mongodb-gridfs: producer with no explicit operation, any HTTP client could therefore set the gridfs.operation header to override the route's intended operation - switching, for example, a file upload to remove (deleting a file identified by the attacker-supplied gridfs.objectid), listAll (enumerating every file in the bucket) or findOne (reading a file) - and supply a gridfs.metadata value that is parsed as a MongoDB document, enabling NoSQL operator injection. No credentials are required when the bridging consumer is unauthenticated.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, routes that drive GridFS operations or metadata via the raw header names must use CamelGridFsOperation / CamelGridFsObjectId / CamelGridFsMetadata / CamelGridFsChunkSize / CamelGridFsFileId instead of the gridfs.* names. For deployments that cannot upgrade immediately, set an explicit operation on the mongodb-gridfs: endpoint so the operation is not taken from a header, and strip the gridfs.* headers from any untrusted ingress before the producer.</p>

### References
* https://camel.apache.org/security/CVE-2026-48204.html


### Credits
* Yu Bao from PayPal (finder)
* Andrea Cosentino (remediation developer)


## Camel-Solr: The SolrParam. and SolrField. Exchange header prefixes used non-Camel-prefixed names that bypass the HTTP header filter, allowing an HTTP client to inject Solr query parameters (server-side request forgery) and document fields ## { #CVE-2026-48203 }

CVE-2026-48203 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48203) [\[CVE json\]](./CVE-2026-48203.cve.json) [\[OSV json\]](./CVE-2026-48203.osv.json)



_Last updated: 2026-07-05T11:55:11.904Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection'), Improper Input Validation, Server-Side Request Forgery (SSRF) vulnerability in Apache Camel Solr component.</p>The camel-solr producer copies Exchange message headers whose names begin with the SolrParam. prefix into the parameters of the Solr request, and headers whose names begin with the SolrField. prefix into the fields of the indexed Solr document. The prefix constants (SolrConstants.HEADER_PARAM_PREFIX / HEADER_FIELD_PREFIX) were the plain strings SolrParam. / SolrField.. Because these names do not start with the Camel / camel prefix, HttpHeaderFilterStrategy - which blocks only the Camel header namespace on the HTTP boundary - let them pass from an inbound HTTP request straight into the Exchange. In a route that bridges an HTTP consumer (for example platform-http) into a solr: producer, any HTTP client could therefore set SolrParam.* headers to inject arbitrary Solr request parameters - including shards or stream.url, which cause the Solr server to issue server-side requests to an attacker-chosen URL (server-side request forgery, for example to an internal service or a cloud metadata endpoint), or qt to reach administrative request handlers - and set SolrField.* headers to inject arbitrary fields into indexed documents. No credentials are required when the bridging consumer is unauthenticated.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, routes that set Solr parameters or fields via the raw header prefixes must use CamelSolrParam. / CamelSolrField. instead of SolrParam. / SolrField.. For deployments that cannot upgrade immediately, strip the SolrParam.* and SolrField.* headers from any untrusted ingress before the solr: producer, and set the required Solr parameters and fields from a trusted source in the route.</p>

### References
* http://camel.apache.org/security/CVE-2026-48203.html


### Credits
* Yu Bao from Paypal (finder)
* Andrea Cosentino (remediation developer)


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


## The inbound consumer maps externally-supplied WebSocket query and path parameters into the Exchange without a HeaderFilterStrategy, allowing injection of Camel control headers ## { #CVE-2026-46726 }

CVE-2026-46726 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46726) [\[CVE json\]](./CVE-2026-46726.cve.json) [\[OSV json\]](./CVE-2026-46726.osv.json)



_Last updated: 2026-07-06T08:05:38.812Z_

### Affected

* Apache Camel Vertx Websocket from 4.0.0 before 4.14.8
* Apache Camel Vertx Websocket from 4.15.0 before 4.18.3
* Apache Camel Vertx Websocket from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Exposure of Sensitive Information to an Unauthorized Actor, Server-Side Request Forgery (SSRF) vulnerability in Apache Camel in Vertx Websocket component.</p>The camel-vertx-websocket consumer mapped inbound WebSocket query and path parameters into the Camel Exchange header map without applying any HeaderFilterStrategy (VertxWebsocketConsumer.populateExchangeHeaders()). Because nothing blocked the Camel header namespace, a client connecting to the WebSocket endpoint could set Camel-internal control headers - including CamelHttpUri (Exchange.HTTP_URI) - simply by supplying them as query parameters. In a route where the WebSocket consumer feeds a downstream HTTP producer, the injected CamelHttpUri redirects the server-side HTTP request to an attacker-chosen destination (server-side request forgery - for example to an internal service or a cloud metadata endpoint). In addition, the HTTP producer resolves Camel property placeholders on the resulting (attacker-controlled) URI, so placeholders embedded in the injected value - such as an environment-variable reference, an application property, or a vault reference - are resolved to their real values and sent to the attacker, disclosing environment variables, application properties and vault secrets. When the WebSocket endpoint is exposed without authentication, this is reachable by an unauthenticated remote attacker.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. The fix makes the affected consumers apply a HeaderFilterStrategy that filters the Camel header namespace case-insensitively on inbound mapping, so externally-supplied Camel* / camel* headers are no longer copied into the Exchange. For deployments that cannot upgrade immediately, strip the Camel control headers from the inbound message before they reach any downstream producer (for example removeHeaders('Camel*') and removeHeaders('camel*') at the start of the route), require authentication on the WebSocket endpoint, and avoid bridging an untrusted consumer directly into an HTTP producer whose target URI can be driven from message headers.</p>

### References
* https://camel.apache.org/security/CVE-2026-46726.html


### Credits
* Kamalpreet Singh (finder)
* Andrea Cosentino (remediation developer)


## Camel-CXF: The SOAP operation-selection headers used non-Camel-prefixed names (operationName, operationNamespace) that bypass the HTTP header filter, allowing an HTTP client to redirect the invoked SOAP operation ## { #CVE-2026-46592 }

CVE-2026-46592 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46592) [\[CVE json\]](./CVE-2026-46592.cve.json) [\[OSV json\]](./CVE-2026-46592.osv.json)



_Last updated: 2026-07-05T11:56:44.036Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Unintended Proxy or Intermediary ('Confused Deputy') vulnerability in Apache Camel CXF SOAP component.</p>The camel-cxf producer selects which SOAP operation to invoke on the backend service from the operationName (and operationNamespace) Exchange header, whose constant values (CxfConstants.OPERATION_NAME / OPERATION_NAMESPACE) were the plain strings operationName / operationNamespace. Because these names do not start with the Camel / camel prefix, HttpHeaderFilterStrategy - which blocks only the Camel header namespace on the HTTP boundary - let them pass from an inbound HTTP request straight into the Exchange. In a route that bridges an HTTP consumer (for example platform-http) into a cxf: producer, any HTTP client could therefore set the operationName header and have CxfProducer resolve and invoke a different WSDL operation than the route intended - for example replacing a read operation with a destructive one - against the backend SOAP service (a confused-deputy redirection). The constant is defined in the shared camel-cxf-common module, so the same non-prefixed names also applied to camel-cxfrs. No credentials are required when the bridging consumer is unauthenticated.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, the operation-selection headers are named CamelCxfOperationName / CamelCxfOperationNamespace and are filtered at transport boundaries; see the 4.21 upgrade guide for the cross-transport carrier-header pattern. For deployments that cannot upgrade immediately, do not select the CXF operation from untrusted input: strip the operationName and operationNamespace headers from any untrusted ingress before the cxf: producer and set the operation from a trusted source in the route.<br></p>

### References
* https://camel.apache.org/security/CVE-2026-46592.html


### Credits
* Yu Bao from Paypal (finder)
* Andrea Cosentino (remediation developer)


## Camel-Neo4j: JSON property names from the CamelNeo4jMatchProperties header are interpolated into the Cypher WHERE clause without validation, allowing Cypher injection (incomplete remediation of CVE-2025-66169) ## { #CVE-2026-46591 }

CVE-2026-46591 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46591) [\[CVE json\]](./CVE-2026-46591.cve.json) [\[OSV json\]](./CVE-2026-46591.osv.json)



_Last updated: 2026-07-05T11:57:19.664Z_

### Affected

* Apache Camel from 4.10.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Improper Neutralization of Special Elements in Data Query Logic vulnerability in Apache Camel Neo4J component.</p>The camel-neo4j producer builds the Cypher WHERE clause for its match/retrieve and delete operations from the CamelNeo4jMatchProperties map. CVE-2025-66169 addressed Cypher injection through the property values by binding them as query parameters ($paramN), but the property names (the JSON keys of that map) were still concatenated into the query string verbatim in Neo4jProducer.retrieveNodes() and deleteNode(). A property name containing Cypher syntax therefore alters the structure of the executed query. Where a route maps untrusted input into the CamelNeo4jMatchProperties map - for example by passing a request body as the match map, or from a consumer that does not filter inbound Camel* headers - an attacker who controls the JSON key names can inject arbitrary Cypher and read, modify or delete any node or relationship in the Neo4j database. The CamelNeo4jMatchProperties header is itself Camel-prefixed and is filtered by the HTTP header-filter strategy, so a plain HTTP client cannot set it directly; the issue is reachable through routes that deliberately or inadvertently carry untrusted data into that header.<br><p>This issue affects Apache Camel: from 4.10.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. For deployments that cannot upgrade immediately, do not populate the CamelNeo4jMatchProperties map from untrusted input: validate or allow-list the property names (for example against ^[A-Za-z_][A-Za-z0-9_]*$) before the Neo4j producer, and ensure that any consumer feeding such a route filters inbound Camel* / camel* headers so the match header cannot be supplied by an external sender.</p>

### References
* https://camel.apache.org/security/CVE-2026-46591.html


### Credits
* Yu Bao from Paypal (finder)
* Andrea Cosentino (remediation developer)


## Camel-PQC: The HashiCorp Vault and AWS Secrets Manager key-lifecycle managers deserialize persisted key metadata with java.io.ObjectInputStream and no ObjectInputFilter (incomplete remediation of CVE-2026-40048) ## { #CVE-2026-46590 }

CVE-2026-46590 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46590) [\[CVE json\]](./CVE-2026-46590.cve.json) [\[OSV json\]](./CVE-2026-46590.osv.json)



_Last updated: 2026-07-05T11:58:05.374Z_

### Affected

* Apache Camel from 4.18.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Camel PQC component.</p>The camel-pqc component persists post-quantum key metadata (KeyMetadata) through pluggable KeyLifecycleManager implementations. HashicorpVaultKeyLifecycleManager and AwsSecretsManagerKeyLifecycleManager read that metadata back from the configured secret backend by deserializing a Base64-wrapped value with a raw java.io.ObjectInputStream.readObject() and no ObjectInputFilter or class allow-list; the cast to KeyMetadata happens only after readObject() returns, so any readObject() side effects in a crafted object run before the type check. The same unfiltered legacy-migration read also remained in FileBasedKeyLifecycleManager (for the stored KeyPair and KeyMetadata). A principal who can write to the operator-controlled backend that holds these values - the HashiCorp Vault KV path, or the AWS Secrets Manager secret (requiring a Vault token or secretsmanager:PutSecretValue) - could store a crafted serialized object that is deserialized during normal key-lifecycle operations, potentially leading to code execution in the context of the application that manages the keys. This is an incomplete-remediation follow-on to CVE-2026-40048 (CAMEL-23200), which changed FileBasedKeyLifecycleManager to store metadata as JSON / PKCS#8 / X.509 but did not add an ObjectInputFilter, did not cover the Vault and AWS sibling managers, and left FileBasedKeyLifecycleManager's own legacy-migration deserialization unfiltered.<br><p>This issue affects Apache Camel: from 4.18.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.18.x LTS releases stream, then they are suggested to upgrade to 4.18.3. For deployments that cannot upgrade immediately, restrict write access to the key backend so that only the application's own identity can write the camel-pqc secrets (least-privilege HashiCorp Vault policies and secretsmanager:PutSecretValue IAM), and keep the PQC key material in a backend separate from any data that less-trusted principals can write.</p>

### References
* https://camel.apache.org/security/CVE-2026-46590.html


### Credits
* Yu Bao from Paypal (finder)
* Andrea Cosentino (remediation developer)


## CouchDB: Non-Camel-prefixed Exchange headers bypass HeaderFilterStrategy allowing operation override from untrusted input ## { #CVE-2026-46588 }

CVE-2026-46588 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46588) [\[CVE json\]](./CVE-2026-46588.cve.json) [\[OSV json\]](./CVE-2026-46588.osv.json)



_Last updated: 2026-07-06T09:25:34.812Z_

### Affected

* Apache Camel through 4.14.7
* Apache Camel from 4.15.0 through 4.18.2
* Apache Camel from 4.19.0 through 4.20.0


### Description

<p>Improper Input Validation vulnerability in Apache Camel.</p><p>This issue affects Apache Camel: through 4.14.7, from 4.15.0 through 4.18.2, from 4.19.0 through 4.20.0.</p><p>Users are recommended to upgrade to version 4.14.8, 4.18.3, 4.21.0, which fixes the issue.</p>

### References
* https://camel.apache.org/security/CVE-2026-46588.html


### Credits
* Yu Bao - yubao@paypal.com, who works for paypal.com. (reporter)


## Couchbase: Non-Camel-prefixed Exchange headers bypass HeaderFilterStrategy allowing operation override from untrusted input ## { #CVE-2026-46587 }

CVE-2026-46587 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46587) [\[CVE json\]](./CVE-2026-46587.cve.json) [\[OSV json\]](./CVE-2026-46587.osv.json)



_Last updated: 2026-07-06T09:25:19.132Z_

### Affected

* Apache Camel through 4.14.7
* Apache Camel from 4.15.0 through 4.18.2
* Apache Camel from 4.19.0 through 4.20.0


### Description

<p>Improper Input Validation vulnerability in Apache Camel.</p><p>This issue affects Apache Camel: through 4.14.7, from 4.15.0 through 4.18.2, from 4.19.0 through 4.20.0.</p><p>Users are recommended to upgrade to version 4.14.8, 4.18.3, 4.21.0, which fixes the issue.</p>

### References
* https://camel.apache.org/security/CVE-2026-46587.html


### Credits
* Yu Bao - yubao@paypal.com, who works for paypal.com. (reporter)


## The query control headers used non-Camel-prefixed names (QUERY, RETURN_LUCENE_DOCS) that bypass the HTTP header filter, allowing an HTTP client to inject the full-text search query ## { #CVE-2026-46585 }

CVE-2026-46585 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46585) [\[CVE json\]](./CVE-2026-46585.cve.json) [\[OSV json\]](./CVE-2026-46585.osv.json)



_Last updated: 2026-07-06T08:03:14.855Z_

### Affected

* Apache Camel Lucene from 4.0.0 before 4.14.8
* Apache Camel Lucene from 4.15.0 before 4.18.3
* Apache Camel Lucene from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Authorization Bypass Through User-Controlled Key vulnerability in Apache Camel Lucene Component.</p>The camel-lucene producer reads the search phrase from an Exchange header (LuceneConstants.HEADER_QUERY) whose value was the plain string QUERY (and RETURN_LUCENE_DOCS for HEADER_RETURN_LUCENE_DOCS). Because these names do not start with the Camel / camel prefix, HttpHeaderFilterStrategy - which blocks only the Camel header namespace on the HTTP boundary - let them pass from an inbound HTTP request straight into the Exchange. In a route that exposes a Lucene query operation behind an HTTP consumer (for example platform-http), any HTTP client could therefore set the QUERY header and have its value executed against the full-text index, overriding the query the route intended to run. Depending on what is indexed, this allows reading documents the request should not have access to (for example a match-all query returns the entire index, or the route's intended per-user filter can be replaced), and expensive regular-expression queries can consume significant CPU. No credentials are required when the HTTP consumer is unauthenticated.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, routes that set the query via the raw header name must use CamelLuceneQuery (and CamelLuceneReturnLuceneDocs) instead of QUERY / RETURN_LUCENE_DOCS. For deployments that cannot upgrade immediately, strip the attacker-controllable headers before the Lucene producer and set the query from a trusted source (for example removeHeader('QUERY') and removeHeader('RETURN_LUCENE_DOCS'), then setHeader('QUERY', constant(...)) at the start of the route).</p>

### References
* https://camel.apache.org/security/CVE-2026-46585.html


### Credits
* Yu Bao from Paypal (finder)
* Andrea Cosentino (remediation developer)


## The mail producer applied attacker-supplied message headers as JavaMail session properties, allowing an attacker to influence SMTP parameters ## { #CVE-2026-46584 }

CVE-2026-46584 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46584) [\[CVE json\]](./CVE-2026-46584.cve.json) [\[OSV json\]](./CVE-2026-46584.osv.json)



_Last updated: 2026-07-06T08:02:36.402Z_

### Affected

* Apache Camel Mail from 4.0.0 before 4.14.8
* Apache Camel Mail from 4.15.0 before 4.18.3
* Apache Camel Mail from 4.19.0 before r


### Description

<p>Improper Input Validation, Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Camel Mail Component.</p>The camel-mail producer (MailProducer.getSender) scanned the outgoing Exchange for message headers in the mail.smtp. / mail.smtps. namespace and, when any were present, built a per-message JavaMail sender with those values applied as JavaMail session properties, overriding the endpoint configuration. This namespace is Camel-internal - only MailProducer interprets it - and was not blocked by any HeaderFilterStrategy, so the values could originate from any inbound protocol (for example platform-http query parameters or request headers, or JMS / Kafka messages from untrusted producers) that feeds a route ending in an smtp / smtps producer without an intervening removeHeaders. The maximal impact is version-dependent: on releases before 4.19.0, setting mail.smtp.host redirects the SMTP connection to a server under the attacker's control, and because the producer then authenticates with the endpoint's configured username and password those credentials are transmitted to the attacker; on 4.19.0 and later the producer connects to the endpoint's configured host explicitly, so the reachable impact is limited to weakening transport security (for example mail.smtp.ssl.trust, mail.smtp.starttls.enable or mail.smtp.socks.host) and interception of the outgoing message rather than host redirect. Exploitation requires a route that channels untrusted input into the mail producer without stripping the namespace.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, the per-message override is disabled by default; enable it only on trusted endpoints with useJavaMailSessionPropertiesFromHeaders=true. For deployments that cannot upgrade immediately, strip the namespace before the mail producer with removeHeaders('mail.smtp.*') and removeHeaders('mail.smtps.*') between any untrusted ingress and the smtp / smtps producer. Even with the opt-in enabled, route authors should still strip the namespace on any path that carries untrusted input.</p>

### References
* https://camel.apache.org/security/CVE-2026-46584.html


### Credits
* Yu Bao from PayPal (finder)


## Camel-NATS: Inbound NATS message headers are mapped into the Exchange without a configured HeaderFilterStrategy, allowing a client that can publish to the subject to inject Camel control headers ## { #CVE-2026-46457 }

CVE-2026-46457 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46457) [\[CVE json\]](./CVE-2026-46457.cve.json) [\[OSV json\]](./CVE-2026-46457.osv.json)



_Last updated: 2026-07-05T12:00:52.558Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation vulnerability in Apache Camel NATS component.</p>The camel-nats component maps inbound NATS message headers into the Camel Exchange but defaulted its headerFilterStrategy to a bare new DefaultHeaderFilterStrategy() with no inbound rules configured (NatsConfiguration). With no inFilter, inFilterPattern or inFilterStartsWith set, DefaultHeaderFilterStrategy.applyFilterToExternalHeaders returns not filtered for every header name, so NatsConsumer copies every NATS message header - including Camel-internal control headers such as CamelHttpUri, CamelFileName or CamelSqlQuery - unmodified onto the Camel message. A client able to publish to the consumed NATS subject can therefore inject arbitrary Camel control headers that influence the behaviour of downstream producers in the route (for example redirecting an HTTP producer, changing a file name, or overriding a query); the injected headers also persist across internal direct, seda and vm hops. The concrete downstream impact depends on which producers the route uses. NATS message headers require NATS 2.2 or later, and the issue is reachable without credentials when the NATS server is configured without authentication (the NATS server default).<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. The fix makes camel-nats default to a dedicated NatsHeaderFilterStrategy that filters the Camel header namespace case-insensitively on inbound mapping, so client-supplied Camel* / camel* headers are no longer copied into the Exchange. For deployments that cannot upgrade immediately, strip the Camel control headers from inbound NATS messages before they reach any downstream producer (for example removeHeaders('Camel*') and removeHeaders('camel*') at the start of the route), and enable authentication on the NATS server so that only trusted clients can publish to the consumed subject.</p>

### References
* https://camel.apache.org/security/CVE-2026-46457.html


### Credits
* Yu Bao from PayPal (finder)


## Camel-AWS2-SQS: Inbound message attributes are mapped into the Exchange without an inbound HeaderFilterStrategy, allowing a message sender to inject Camel control headers ## { #CVE-2026-46456 }

CVE-2026-46456 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46456) [\[CVE json\]](./CVE-2026-46456.cve.json) [\[OSV json\]](./CVE-2026-46456.osv.json)



_Last updated: 2026-07-05T12:01:36.500Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation vulnerability in Apache Camel AWS2-SQS Component.<br></p><p>The camel-aws2-sqs component map inbound message attributes into the Camel Exchange through a component-specific HeaderFilterStrategy. Sqs2HeaderFilterStrategy configured only an outbound filter (setOutFilterPattern, which blocks Camel*, breadcrumbId and org.apache.camel.* headers being written to the broker) but did not configure an inbound filter. As a result, when Sqs2Consumer copies each SQS MessageAttribute into the Exchange via HeaderFilterStrategy.applyFilterToExternalHeaders, DefaultHeaderFilterStrategy applied no inbound rule and treated every header name as not filtered - including Camel-internal control headers such as CamelHttpUri, CamelFileName or CamelSqlQuery - copying them unmodified onto the Camel message. Any principal able to send messages to the consumed SQS queue (for example a cross-account sender or a lower-privileged in-account component holding sqs:SendMessage) could therefore set arbitrary Camel control headers that influence the behaviour of downstream producers in the route (for example redirecting an HTTP producer, changing a file name, or overriding a query); the injected headers also persist across internal direct, seda and vm hops. The concrete downstream impact depends on which producers the route uses.<br></p><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. The fix adds an inbound HeaderFilterStrategy rule to Sqs2HeaderFilterStrategy that filters the Camel header namespace case-insensitively on inbound mapping, so sender-supplied Camel* / camel* headers are no longer copied into the Exchange. For deployments that cannot upgrade immediately, strip the Camel control headers from inbound messages before they reach any downstream producer (for example removeHeaders('Camel*') and removeHeaders('camel*') at the start of the route), and restrict who may send to the consumed SQS queue by applying least-privilege sqs:SendMessage permissions on the queue resource policy.</p>

### References
* https://camel.apache.org/security/CVE-2026-46456.html


### Credits
* Yu Bao from Paypal (finder)


## Camel-Keycloak: The access-token validity window is not verified because the IS_ACTIVE check is missing from the TokenVerifier, allowing expired tokens to be accepted ## { #CVE-2026-46455 }

CVE-2026-46455 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46455) [\[CVE json\]](./CVE-2026-46455.cve.json) [\[OSV json\]](./CVE-2026-46455.osv.json)



_Last updated: 2026-07-05T12:02:14.819Z_

### Affected

* Apache Camel from 4.18.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Insufficient Session Expiration vulnerability in Apache Camel Keycloak Component.</p>The camel-keycloak security helper KeycloakSecurityHelper.parseAndVerifyAccessToken builds a Keycloak TokenVerifier using withChecks(...) with only the subject-exists check and the realm-URL (issuer) check. Keycloak's TokenVerifier.withChecks(...) appends to an initially empty check list - the upstream default checks are installed only when withDefaultChecks() is called - so the built-in IS_ACTIVE predicate, which validates the token's exp (expiration) and nbf (not-before) claims, is never applied. As a result the helper verifies the token signature, subject and issuer but does not enforce the token's validity window: an access token that is expired, or not yet valid, is accepted as valid. Routes that rely on this helper to authenticate inbound requests therefore accept access tokens that are outside their intended lifetime.<br><p>This issue affects Apache Camel: from 4.18.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. The fix makes KeycloakSecurityHelper.parseAndVerifyAccessToken include the TokenVerifier.IS_ACTIVE check so that expired or not-yet-valid access tokens are rejected, aligning the helper with Keycloak's default check set. For deployments that cannot upgrade immediately, enforce token expiration outside the helper - for example validate the access token's exp/nbf claims in the route before trusting it, keep Keycloak access-token lifetimes short, and ensure any upstream gateway or resource server also validates the token validity window.</p>

### References
* https://camel.apache.org/security/CVE-2026-46455.html


### Credits
* Yu Bao from Paypal (finder)
* Andrea Cosentino from Apache Software Foundation (finder)


## Camel-Cometd: Inbound Bayeux message headers are mapped into the Exchange without a HeaderFilterStrategy, allowing unauthenticated clients to inject Camel control headers ## { #CVE-2026-46454 }

CVE-2026-46454 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46454) [\[CVE json\]](./CVE-2026-46454.cve.json) [\[OSV json\]](./CVE-2026-46454.osv.json)



_Last updated: 2026-07-05T12:02:45.108Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation vulnerability in Apache Camel Cometd Component.</p>The camel-cometd component maps inbound Bayeux (CometD) message headers into the Camel Exchange without applying a HeaderFilterStrategy. CometdBinding.populateExchangeFromMessage copies the entire ext.CamelHeaders map supplied by the CometD client directly onto the Camel message (message.setHeaders), so any header name - including Camel-internal control headers such as CamelHttpUri, CamelFileName or CamelJmsDestinationName - is accepted unmodified. Because a CometdComponent installs no Bayeux SecurityPolicy by default, any client that can complete the Bayeux handshake against the CometD endpoint can publish such a message without authentication. An attacker can therefore inject arbitrary Camel control headers that influence the behaviour of downstream producers in the route (for example redirecting an HTTP producer, changing a file name, or overriding a JMS destination); the injected headers also persist across internal direct, seda and vm hops. The concrete downstream impact depends on which producers the route uses.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. The fix implements a HeaderFilterStrategy in the camel-cometd binding (a long-standing TODO in the code) that filters the Camel header namespace case-insensitively on inbound mapping, so client-supplied Camel* / camel* headers are no longer copied into the Exchange. For deployments that cannot upgrade immediately, strip the Camel control headers from inbound CometD messages before they reach any downstream producer (for example removeHeaders('Camel*') and removeHeaders('camel*') at the start of the route), and install an explicit Bayeux SecurityPolicy on the CometdComponent so that only authenticated clients can publish.</p>

### References
* https://camel.apache.org/security/CVE-2026-46454.html


### Credits
* Yu Bao from Paypal (finder)


## Camel-Elasticsearch-Rest-Client: Exchange header constants without the Camel prefix bypass inbound HTTP header filtering, allowing untrusted clients to override the Elasticsearch query and operation ## { #CVE-2026-46453 }

CVE-2026-46453 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46453) [\[CVE json\]](./CVE-2026-46453.cve.json) [\[OSV json\]](./CVE-2026-46453.osv.json)



_Last updated: 2026-07-05T12:03:20.579Z_

### Affected

* Apache Camel from 4.3.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Improper Input Validation, Authorization Bypass Through User-Controlled Key vulnerability in Apache Camel ElasticSearch Rest Client.</p>The camel-elasticsearch-rest-client component reads several Exchange headers to control its behaviour - SEARCH_QUERY (an advanced query body), OPERATION (which Elasticsearch operation to run), INDEX_NAME, INDEX_SETTINGS and ID. The string values of these header constants, defined in ElasticSearchRestClientConstant, are plain unprefixed names ('SEARCH_QUERY', 'OPERATION', 'INDEX_NAME', 'INDEX_SETTINGS', 'ID') rather than the 'Camel'-prefixed names used by every other Camel component (for example CamelSqlQuery, CamelMongoDbCriteria, CamelCqlQuery). Camel's inbound HTTP header filter, HttpHeaderFilterStrategy, blocks only header names that begin with 'Camel' or 'camel'. Because the Elasticsearch header names do not carry that prefix, they pass through the inbound filter unchanged. When a Camel route exposes an HTTP entry point (for example platform-http) in front of an elasticsearch-rest-client producer, an untrusted HTTP client can set these headers directly on its request and override the query and operation that the route author configured: reading every document in the index (SEARCH_QUERY with a match_all query), deleting documents (OPERATION set to Delete together with ID), or exfiltrating selected fields. No credentials are required and the producer reads the headers unconditionally.<br><p>This issue affects Apache Camel: from 4.3.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. The fix renames the camel-elasticsearch-rest-client Exchange header constant string values (ID, SEARCH_QUERY, INDEX_SETTINGS, INDEX_NAME, OPERATION) to carry the Camel prefix (CamelElasticsearchId, CamelElasticsearchSearchQuery, CamelElasticsearchIndexSettings, CamelElasticsearchIndexName, CamelElasticsearchOperation) so that they are blocked by the inbound HttpHeaderFilterStrategy; the Java field names are unchanged. For deployments that cannot upgrade immediately, strip the affected headers from untrusted inbound messages before they reach the producer (for example removeHeader('SEARCH_QUERY'), removeHeader('OPERATION'), removeHeader('INDEX_NAME'), removeHeader('INDEX_SETTINGS') and removeHeader('ID') in front of the elasticsearch-rest-client endpoint), or apply a custom HeaderFilterStrategy that blocks these names.</p>

### References
* https://camel.apache.org/security/CVE-2026-46453.html


### Credits
* Yu Bao from Paypal (finder)


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


## Camel-PQC: The AWS Secrets Manager key-lifecycle manager deserializes persisted key metadata with java.io.ObjectInputStream and no ObjectInputFilter ## { #CVE-2026-43867 }

CVE-2026-43867 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43867) [\[CVE json\]](./CVE-2026-43867.cve.json) [\[OSV json\]](./CVE-2026-43867.osv.json)



_Last updated: 2026-07-06T08:15:07.227Z_

### Affected

* Apache Camel from 4.18.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Camel PQC Component.</p><span style="background-color: rgb(255, 255, 255);">The camel-pqc component persists post-quantum key metadata (KeyMetadata) through pluggable KeyLifecycleManager implementations. AwsSecretsManagerKeyLifecycleManager.deserializeMetadata() reads that metadata back from the configured AWS Secrets Manager secret by Base64-decoding the stored value and deserializing it with a raw java.io.ObjectInputStream.readObject() and no ObjectInputFilter or class allow-list; the cast to KeyMetadata happens only after readObject() returns, so any readObject() side effects in a crafted object run before the type check. A principal who can write to the AWS Secrets Manager secret that holds this metadata (requiring secretsmanager:PutSecretValue on that secret) could store a crafted serialized object that is deserialized during normal key-lifecycle operations, potentially leading to code execution in the context of the application that manages the keys. This is the same underlying defect, in the same code path and remediated by the same fix, as CVE-2026-46590, which was reported independently and additionally covers the HashiCorp Vault and file-based sibling managers; both are incomplete-remediation follow-ons to CVE-2026-40048 (CAMEL-23200).</span><br><p>This issue affects Apache Camel: from 4.18.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.18.x LTS releases stream, then they are suggested to upgrade to 4.18.3. For deployments that cannot upgrade immediately, restrict write access to the AWS Secrets Manager secret that holds the camel-pqc key metadata so that only the application’s own identity holds secretsmanager:PutSecretValue on it (least-privilege IAM), and keep the PQC key material in a secret separate from any data that less-trusted principals can write.</span></p>

### References
* https://camel.apache.org/security/CVE-2026-43867.html


### Credits
* Venkatraman Kumar from Securin (finder)
* Andrea Cosentino (remediation developer)


## Camel JMS - CVE-2026-40860 fix bypass via DefaultExchangeHolder ## { #CVE-2026-43866 }

CVE-2026-43866 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43866) [\[CVE json\]](./CVE-2026-43866.cve.json) [\[OSV json\]](./CVE-2026-43866.osv.json)



_Last updated: 2026-07-06T07:24:17.611Z_

### Affected

* Apache Camel from 3.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0
* Apache Camel from 3.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Camel, Apache Camel JMS component.</p><span style="background-color: rgb(255, 255, 255);">JmsBinding.extractBodyFromJms() in camel-jms - and the equivalent JmsBinding in camel-sjms - deserializes the payload of an incoming JMS ObjectMessage via jakarta.jms.ObjectMessage.getObject() whenever the mapJmsMessage option is enabled (the default) and Camel acts as a JMS consumer. The CVE-2026-40860 hardening added a post-deserialization class check that rejects classes outside the default allow-list java.**;javax.**;org.apache.camel.**;!*. However org.apache.camel.support.DefaultExchangeHolder itself lives in the allow-listed org.apache.camel.** namespace, so an ObjectMessage whose top-level object is a DefaultExchangeHolder passes the check. The receiving side then calls DefaultExchangeHolder.unmarshal() on it without requiring the transferExchange option to be enabled - an asymmetric trust boundary, since the sending side gates ObjectMessage and transferExchange handling but the receiving side did not - writing every non-null field of the holder into the Exchange: the message body, the IN and OUT headers, the exchange properties, the variables, the exchange id and the exception. An attacker who can publish an ObjectMessage to a queue or topic consumed by an affected Camel application can therefore inject arbitrary Exchange state using only universally-trusted java.lang and java.util types, with no deserialization gadget chain required, to manipulate routing and headers, exchange properties and error handling. The same handling applies to camel-sjms and camel-sjms2, and to the JMS-family components built on JmsComponent and JmsBinding: camel-amqp, camel-activemq and camel-activemq6. This is a bypass of the CVE-2026-40860 fix rather than a flaw in it.</span><br><p>This issue affects Apache Camel: from 3.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0; Apache Camel: from 3.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, JMS ObjectMessage handling is disabled by default in camel-jms, camel-sjms and the JMS-family components (a new objectMessageEnabled option defaults to false at the component and endpoint level), so an incoming ObjectMessage - including a DefaultExchangeHolder payload - is no longer deserialized unless the option is explicitly enabled; only set objectMessageEnabled=true when the consumed JMS destination is fed exclusively by trusted producers. For deployments that cannot upgrade immediately, restrict publish access to the queues and topics consumed by Camel to trusted producers via JMS broker authorization, and do not expose JMS consumers that map ObjectMessage bodies to untrusted networks; a JMS-provider deserialization allow-list does not mitigate this specific bypass because the crafted payload uses only universally-trusted classes.</span><br>

### References
* https://camel.apache.org/security/CVE-2026-43866.html


### Credits
* gaorenyusi (finder)
* Andrea Cosentino (remediation developer)


## Camel-Hazelcast: Unsafe Java deserialization in default-configured managed Hazelcast instances enables remote code execution ## { #CVE-2026-43865 }

CVE-2026-43865 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43865) [\[CVE json\]](./CVE-2026-43865.cve.json) [\[OSV json\]](./CVE-2026-43865.osv.json)



_Last updated: 2026-07-05T12:04:39.086Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Camel Hazelcast component.</p>The camel-hazelcast component creates and manages Hazelcast instances using a default configuration that applies no Java deserialization filter. When Camel builds the Hazelcast Config itself - that is, when no user-supplied HazelcastInstance, hazelcastConfigUri, or referenced Config bean is provided - neither Hazelcast's JavaSerializationFilterConfig nor a Camel-side ObjectInputFilter is configured, so objects received over the Hazelcast cluster protocol are deserialized inside Hazelcast's own serialization layer (ObjectInputStream.readObject) before Camel ever processes them. An attacker who can join or otherwise reach the Hazelcast cluster can publish a crafted serialized Java object that is then deserialized on every Camel node, resulting in remote code execution. The exposure is present by default and requires no opt-in endpoint configuration: any route using a hazelcast consumer (hazelcast-topic, hazelcast-queue, hazelcast-seda, hazelcast-map, hazelcast-multimap, hazelcast-replicatedmap, hazelcast-list, hazelcast-set), as well as the HazelcastAggregationRepository and HazelcastIdempotentRepository, is affected whenever the managed instance is created from Camel's default configuration.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to version 4.21.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. The fix makes Camel apply a default Hazelcast JavaSerializationFilterConfig (whitelisting the java., javax. and org.apache.camel. class-name prefixes and blacklisting java.net.) to instances it creates from its own default configuration, while leaving any user-supplied Config or HazelcastInstance untouched. For deployments that cannot upgrade immediately, configure a deserialization filter on the Hazelcast instance (Hazelcast JavaSerializationFilterConfig, or the JVM-wide system property -Djdk.serialFilter=!java.net.**;java.**;javax.**;org.apache.camel.**;!*) and enable Hazelcast cluster authentication and TLS to restrict who can reach the cluster.</p>

### References
* https://camel.apache.org/security/CVE-2026-43865.html


### Credits
* gaorenyusi (finder)


## Permissive default ObjectInputFilter pattern admits java.net.** and enables DNS-based information disclosure ## { #CVE-2026-42527 }

CVE-2026-42527 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42527) [\[CVE json\]](./CVE-2026-42527.cve.json) [\[OSV json\]](./CVE-2026-42527.osv.json)



_Last updated: 2026-07-05T12:05:31.946Z_

### Affected

* Apache Camel from 4.14.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.21.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Camel.</p>The default ObjectInputFilter pattern shipped with several Apache Camel components for defense-in-depth deserialization filtering ('java.**;javax.**;org.apache.camel.**;!*', or the no-'javax.**' variant in the aggregation-repository components) uses a recursive 'java.**' glob that admits classes whose hashCode/equals/readObject methods perform network I/O, notably java.net.URL and java.net.InetAddress. When an attacker can deliver a Java-serialized payload to an affected Camel consumer, deserialization of a HashMap (or any collection that calls hashCode on its elements) containing java.net.URL keys causes the JVM to issue DNS queries to the attacker-supplied host during the deserialization side-effect. The class-level filter check passes because the resulting object's class (HashMap) is allow-listed; the DNS query is observable on an attacker-controlled DNS server, providing an out-of-band side channel. The exposure is highest on the camel-jms family because JmsBinding.extractBodyFromJms invokes ObjectMessage.getObject() unconditionally when mapJmsMessage=true (default). Affected components: camel-jms, camel-sjms, camel-amqp, camel-mina, camel-netty, camel-netty-http, camel-vertx-http, camel-infinispan, and the aggregation repository components camel-leveldb, camel-cassandraql, camel-consul, camel-sql (JDBC aggregation repository).<br><p>This issue affects Apache Camel: from 4.14.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.21.0.</p><p>Users are recommended to upgrade to a version that contains the CAMEL-23372 fix once available: 4.21.0 for the 4.21.x line, 4.18.3 for the 4.18.x line, and 4.14.8 for the 4.14.x line. For deployments that cannot upgrade immediately, configure a JMS-provider-side allow-list (Apache ActiveMQ Artemis 'deserializationAllowList' / 'deserializationDenyList', Apache ActiveMQ Classic 'org.apache.activemq.SERIALIZABLE_PACKAGES') as the primary mitigation, and/or override the in-code default via the endpoint-level 'deserializationFilter' option or the JVM-wide '-Djdk.serialFilter' system property with an explicit deny: '!java.net.**;java.**;javax.**;org.apache.camel.**;!*' (or '!java.net.**;java.**;org.apache.camel.**;!*' for the aggregation-repository components, which do not include javax.**).</p>

### References
* https://camel.apache.org/security/CVE-2026-42527.html


### Credits
* Venkatraman Kumar from Securin (finder)
* Yu Bao from Paypal (finder)


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


## Camel-Vertx-Http: Unsafe Java deserialization of HTTP response bodies via a raw ObjectInputStream when transferException is enabled ## { #CVE-2026-40859 }

CVE-2026-40859 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40859) [\[CVE json\]](./CVE-2026-40859.cve.json) [\[OSV json\]](./CVE-2026-40859.osv.json)



_Last updated: 2026-07-05T12:06:34.457Z_

### Affected

* Apache Camel from 4.0.0 before 4.14.8
* Apache Camel from 4.15.0 before 4.18.3
* Apache Camel from 4.19.0 before 4.20.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Camel.</p>The camel-vertx-http component deserializes HTTP response bodies carrying the Content-Type application/x-java-serialized-object using a raw java.io.ObjectInputStream, without applying any ObjectInputFilter (VertxHttpHelper.deserializeJavaObjectFromStream) This deserialization path is reached only when the producer endpoint is configured with transferException=true (or the component-level allowJavaSerializedObject=true) and throwExceptionOnFailure is left at its default value of true; in that case a backend HTTP response with a 5xx status and the application/x-java-serialized-object content type has its body deserialized with no class restrictions. An attacker who controls the backend the Camel producer talks to - through a man-in-the-middle position on an unencrypted (plain HTTP) connection, or by compromising the backend service - can return a crafted serialized Java object and, if a suitable gadget chain is present on the classpath, achieve remote code execution on the Camel application host. The path is not reachable in the default configuration, where transferException is false.<br><p>This issue affects Apache Camel: from 4.0.0 before 4.14.8, from 4.15.0 before 4.18.3, from 4.19.0 before 4.20.0.</p><p>Users are recommended to upgrade to version 4.20.0, which fixes the issue. If users are on the 4.14.x LTS releases stream, then they are suggested to upgrade to 4.14.8. If users are on the 4.18.x releases stream, then they are suggested to upgrade to 4.18.3. After upgrading, the deserialization performed by both helper utilities is constrained by a default ObjectInputFilter (allow-list java.**;javax.**;org.apache.camel.**;!*), which can be customised through the new deserializationFilter endpoint option or the JVM-wide -Djdk.serialFilter system property. For deployments that cannot upgrade immediately: do not enable transferException=true (or allowJavaSerializedObject=true) on producers that talk to untrusted or network-reachable backends; ensure producer connections use TLS (https) so that a response cannot be substituted by a man-in-the-middle; and, where the option is required, set an explicit -Djdk.serialFilter allow-list (for example java.**;org.apache.camel.**;!*) to constrain deserialization.</p>

### References
* https://camel.apache.org/security/CVE-2026-40859.html


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


## Camel-Docling: Insufficient validation of custom CLI arguments enables argument injection and path traversal in DoclingProducer ## { #CVE-2026-40047 }

CVE-2026-40047 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40047) [\[CVE json\]](./CVE-2026-40047.cve.json) [\[OSV json\]](./CVE-2026-40047.osv.json)



_Last updated: 2026-07-05T12:07:12.860Z_

### Affected

* Apache Camel from 4.15.0 before 4.18.3


### Description

<p>Improper Neutralization of Argument Delimiters in a Command ('Argument Injection') vulnerability in Apache Camel Docling component.</p>The camel-docling component invokes the external `docling` command-line tool by assembling an argument list in DoclingProducer and executing it through java.lang.ProcessBuilder. Custom CLI arguments supplied through the `CamelDoclingCustomArguments` exchange header (a List&lt;String&gt;) were appended to that argument list with insufficient validation: the original implementation relied on a denylist of disallowed flags and only rejected path values that contained a literal `../` sequence. As a result, a Camel route that forwards externally-influenced data into the `CamelDoclingCustomArguments` header (or into the path-bearing headers used to build the invocation) could cause the producer to pass unrecognized or unintended `docling` CLI flags to the subprocess, and could supply path-like argument values that resolved outside the intended directory through traversal sequences not caught by the literal `../` check. Because Camel itself builds the `docling` invocation from these values, the component is responsible for constraining them, and the weak validation allowed CLI-argument injection and directory traversal in the arguments passed to the external tool. The invocation uses the list-based form of ProcessBuilder, so a shell does not interpret the argument values; OS command injection through shell metacharacters was not possible, and the metacharacter rejection added by the fix is defense-in-depth.<br><p>This issue affects Apache Camel: from 4.15.0 before 4.18.3.</p><p>Users are recommended to upgrade to a release that contains the CAMEL-23212 fix. On the mainline the fix is included from Apache Camel 4.19.0 (and later releases such as 4.20.0). For users on the 4.18.x LTS releases stream, upgrade to 4.18.3. The fix replaces the denylist with a strict allowlist of recognized `docling` CLI flags (rejecting any unrecognized flag, and rejecting producer-managed flags such as the output-directory flags), defensively rejects shell metacharacters in argument values, and normalizes path-like values with Path.normalize() before validating them so that traversal sequences which bypass a literal `../` check are detected. As defence in depth, route authors should avoid mapping untrusted message content into the `CamelDoclingCustomArguments` header and the path-bearing headers, and should strip Camel-internal headers from messages that arrive from untrusted producers.</p>

### References
* https://camel.apache.org/security/CVE-2026-40047.html


### Credits
* Andrea Cosentino from Apache Software Foundation (finder)
* Andrea Cosentino from Apache Software Foundation (remediation developer)


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
