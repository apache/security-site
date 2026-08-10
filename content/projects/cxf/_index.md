---
title: Apache CXF security advisories
description: Security information for Apache CXF
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache CXF? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=CXF).

You can read more about the security policy on:

- [Apache CXF security model](https://github.com/apache/cxf/blob/main/THREAT_MODEL.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Revocation bypass in DefaultEncryptingOAuthDataProvider ## { #CVE-2026-68481 }

CVE-2026-68481 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68481) [\[CVE json\]](./CVE-2026-68481.cve.json) [\[OSV json\]](./CVE-2026-68481.osv.json)



_Last updated: 2026-08-06T11:22:36.450Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

In Apache CXF's DefaultEncryptingOAuthDataProvider, revoked access tokens still decrypt successfully, and TokenIntrospectionService reports active:true. The same applies to refresh tokens. This violates the RFC stipulations that 'The authorization server MUST invalidate the token.' and 'introspection of a revoked token MUST return {"active":false}'. Users are recommended to upgrade to versions 4.2.3 or 4.1.8 or 3.6.12, which fix this issue.

### References
* https://lists.apache.org/thread/88c0h10yjb2b8201o1km3st71fs2zw2b


### Credits
* Guanping Zhang reported this vulnerability (finder)


## DefaultEncryptingCodeDataProvider allows unlimited authorization code replay ## { #CVE-2026-68079 }

CVE-2026-68079 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68079) [\[CVE json\]](./CVE-2026-68079.cve.json) [\[OSV json\]](./CVE-2026-68079.osv.json)



_Last updated: 2026-08-06T11:22:56.675Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

In Apache CXF's DefaultEncryptingCodeDataProvider,&nbsp;a captured authorization code can be redeemed an unlimited number of times due to a flaw in the implementation of the&nbsp;removeCodeGrant functionality. This violates the RFC requirement that&nbsp;"The authorization code MUST NOT be used more than once." Users are recommended to upgrade to versions 4.2.3 or 4.1.8 or 3.6.12, which fix this issue.

### References
* https://lists.apache.org/thread/6m06gdqz4rxhy9g90qz9lyqx2gqmf13o


### Credits
* Guanping Zhang reported this vulnerability (finder)


## Unsafe deserialization of inbound JMS ObjectMessage ## { #CVE-2026-66909 }

CVE-2026-66909 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66909) [\[CVE json\]](./CVE-2026-66909.cve.json) [\[OSV json\]](./CVE-2026-66909.osv.json)



_Last updated: 2026-08-06T10:23:22.148Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

<span style="background-color: rgb(252, 252, 251);">Apache CXF's JMS transport deserializes the body of any inbound </span><code>JMS ObjectMessage</code><span style="background-color: rgb(252, 252, 251);">&nbsp;using native Java deserialization, with no type restrictions in place. An</span><span style="background-color: rgb(252, 252, 251);">y attacker able to place a message on the service's JMS destination can submit a malicious serialized object, leading to denial of service or, if a suitable gadget class is on </span><span style="background-color: rgb(252, 252, 251);">the </span><span style="background-color: rgb(252, 252, 251);">classpath, </span><span style="background-color: rgb(252, 252, 251);">remote </span><span style="background-color: rgb(252, 252, 251);">code </span><span style="background-color: rgb(252, 252, 251);">execution. </span><span style="background-color: rgb(252, 252, 251);">The </span><span style="background-color: rgb(252, 252, 251);">fix </span><span style="background-color: rgb(252, 252, 251);">disables </span><span style="background-color: rgb(252, 252, 251);"><code>ObjectMessage</code></span><span style="background-color: rgb(252, 252, 251);">&nbsp;deserialization </span><span style="background-color: rgb(252, 252, 251);">by </span><span style="background-color: rgb(252, 252, 251);">default, </span><span style="background-color: rgb(252, 252, 251);">with </span><span style="background-color: rgb(252, 252, 251);">a </span><span style="background-color: rgb(252, 252, 251);">configuration </span><span style="background-color: rgb(252, 252, 251);">switch </span><span style="background-color: rgb(252, 252, 251);">to </span><span style="background-color: rgb(252, 252, 251);">re-enable </span><span style="background-color: rgb(252, 252, 251);">it </span><span style="background-color: rgb(252, 252, 251);">if </span><span style="background-color: rgb(252, 252, 251);">needed.&nbsp;</span>Users are recommended to upgrade to versions 4.2.3 or 4.1.8 or 3.6.12, which fix this issue.

### References
* https://lists.apache.org/thread/lr5d4tg6tf7j29jmw8wt242oowonjqpx


### Credits
* Reported by n0mi1k (finder)


## Self-issued ID token claims validation skipped ## { #CVE-2026-65583 }

CVE-2026-65583 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-65583) [\[CVE json\]](./CVE-2026-65583.cve.json) [\[OSV json\]](./CVE-2026-65583.osv.json)



_Last updated: 2026-08-06T11:23:16.168Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

Apache CXF’s OIDC relying-party token validation could accept self-issued ID tokens without enforcing required claim checks (issuer/subject/audience/time and sub_jwk binding), enabling authentication bypass with crafted tokens. However, note that self-issued ID tokens are not accepted by default in the validator. Users are recommended to upgrade to versions 4.2.3 or 4.1.8 or 3.6.12, which fixes this issue.

### References
* https://lists.apache.org/thread/fzj8yzgfl53gclxrcdrnrx3grcpkq51j


### Credits
* Guanping Zhang reported this vulnerability. (finder)


## XXE via WSDL/XSD import parsing ## { #CVE-2026-65432 }

CVE-2026-65432 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-65432) [\[CVE json\]](./CVE-2026-65432.cve.json) [\[OSV json\]](./CVE-2026-65432.osv.json)



_Last updated: 2026-08-06T10:26:07.597Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

<span style="background-color: rgb(253, 253, 252);">Apache CXF reads a top-level WSDL through its hardened </span><code>StaxUtils</code><span style="background-color: rgb(253, 253, 252);">&nbsp;path, which disables XML DTDs and external entities. However, any </span><code>&lt;wsdl:import&gt;</code><span style="background-color: rgb(253, 253, 252);">&nbsp;or </span><code>&lt;xsd:import&gt;</code><span style="background-color: rgb(253, 253, 252);">&nbsp;referenced from that top-level WSDL is handed off to WSDL4J, which does </span><strong>not</strong><span style="background-color: rgb(253, 253, 252);">&nbsp;disable </span><span style="background-color: rgb(253, 253, 252);">DOCTYPE </span><span style="background-color: rgb(253, 253, 252);">declarations </span><span style="background-color: rgb(253, 253, 252);">or </span><span style="background-color: rgb(253, 253, 252);">external </span><span style="background-color: rgb(253, 253, 252);">entities. </span><span style="background-color: rgb(253, 253, 252);">As </span><span style="background-color: rgb(253, 253, 252);">a </span><span style="background-color: rgb(253, 253, 252);">result, </span><span style="background-color: rgb(253, 253, 252);">the </span><span style="background-color: rgb(253, 253, 252);">protections </span><span style="background-color: rgb(253, 253, 252);">applied </span><span style="background-color: rgb(253, 253, 252);">to </span><span style="background-color: rgb(253, 253, 252);">the </span><span style="background-color: rgb(253, 253, 252);">top-level </span><span style="background-color: rgb(253, 253, 252);">document </span><span style="background-color: rgb(253, 253, 252);">do </span><span style="background-color: rgb(253, 253, 252);">not </span><span style="background-color: rgb(253, 253, 252);">extend </span><span style="background-color: rgb(253, 253, 252);">to </span><span style="background-color: rgb(253, 253, 252);">imported </span><span style="background-color: rgb(253, 253, 252);">documents, </span><span style="background-color: rgb(253, 253, 252);">leaving </span><span style="background-color: rgb(253, 253, 252);">imported </span><span style="background-color: rgb(253, 253, 252);">WSDL/XSD </span><span style="background-color: rgb(253, 253, 252);">content </span><span style="background-color: rgb(253, 253, 252);">vulnerable </span><span style="background-color: rgb(253, 253, 252);">to </span><span style="background-color: rgb(253, 253, 252);">XML </span><span style="background-color: rgb(253, 253, 252);">External </span><span style="background-color: rgb(253, 253, 252);">Entity </span><span style="background-color: rgb(253, 253, 252);">(XXE) </span><span style="background-color: rgb(253, 253, 252);">attacks.&nbsp;</span>Users are recommended to upgrade to versions 4.2.3 or 4.1.8 or 3.6.12, which fix this issue.

### References
* https://lists.apache.org/thread/5qs207krzg51jl3zs3cvnl5lt9njp8c3


### Credits
* Reported by n0mi1k (finder)


## Denial of service via message header attachments ## { #CVE-2026-64958 }

CVE-2026-64958 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-64958) [\[CVE json\]](./CVE-2026-64958.cve.json) [\[OSV json\]](./CVE-2026-64958.osv.json)



_Last updated: 2026-08-06T10:13:02.649Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

An incomplete fix for&nbsp;CVE-2026-50645 means that it is still possible to perform a denial of service attack on Apache CXF by sending a message with many attachment headers. Users are recommended to upgrade to versions 4.2.3 or 4.1.8 or 3.6.12, which fix this issue.

### References
* https://lists.apache.org/thread/trsnkxc2f21585zlt819blvchgl6oykb


### Credits
* Markus Vogl, RISE GmbH (finder)


## JwtRequestCodeFilter silently overrides outer PKCE and nonce parameters ## { #CVE-2026-63687 }

CVE-2026-63687 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-63687) [\[CVE json\]](./CVE-2026-63687.cve.json) [\[OSV json\]](./CVE-2026-63687.osv.json)



_Last updated: 2026-08-06T11:23:42.840Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

Apache CXF's JwtRequestCodeFilter copies all claims from a signed request JWT into the authorization parameter map without excluding security-sensitive parameters. A client that can produce a validly-signed request JWT (e.g., one whose client_secret is known or compromised) can thereby substitute the code_challenge, code_challenge_method, nonce, and state values that were set in the outer HTTP request, undermining PKCE integrity and OpenID Connect replay protection. Users are recommended to upgrade to versions 4.2.3 or 4.1.8 or 3.6.12, which fix this issue.

### References
* https://lists.apache.org/thread/drcq4chmt0btx86f17o47j17r378hzpw


### Credits
* Guanping Zhang reported this vulnerability. (finder)


## OAuth2 Dynamic Client Registration Scope Self-Escalation ## { #CVE-2026-61466 }

CVE-2026-61466 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-61466) [\[CVE json\]](./CVE-2026-61466.cve.json) [\[OSV json\]](./CVE-2026-61466.osv.json)



_Last updated: 2026-08-06T11:24:26.209Z_

### Affected

* Apache CXF before 3.6.12
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF from 4.2.0 before 4.2.3


### Description

<p>In Apache CXF's OAuth2 Dynamic Client Registration endpoint, the authorization server accepts and stores the `scope` value supplied in the client registration request verbatim, without validating it against an AS-defined allowlist. This could lead to a client self-assigning privileged scopes at registration time. Users are recommended to upgrade to versions 4.2.3 or 4.1.8 or 3.6.12, which fix this issue.</p>

### References
* https://lists.apache.org/thread/2l1r16g79tpxd7fzrzr2q9oscwrjgljs


### Credits
* Guanping Zhang reported this vulnerability. (finder)


## No default restriction on the amount of form parameters per message ## { #CVE-2026-57819 }

CVE-2026-57819 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57819) [\[CVE json\]](./CVE-2026-57819.cve.json) [\[OSV json\]](./CVE-2026-57819.osv.json)



_Last updated: 2026-08-06T10:12:25.051Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

Apache CXF allows to set a limit on the number of form parameters in a JAX-RS message via the "maxFormParameterCount" configuration option. However, no default limit is set which may lead to denial of service attacks when processing&nbsp; requests with very large numbers of form parameters. Users are recommended to upgrade to versions 4.2.3 or 4.1.8 or 3.6.12, which fix this issue by using a default limit of 500 parameters.

### References
* https://lists.apache.org/thread/2n14mk01bjc3lrsyhzrkwy8h86289mov


## OAuth2 Authorization Code Replay via TOCTOU in JCacheCodeDataProvider ## { #CVE-2026-57818 }

CVE-2026-57818 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57818) [\[CVE json\]](./CVE-2026-57818.cve.json) [\[OSV json\]](./CVE-2026-57818.osv.json)



_Last updated: 2026-08-06T11:24:52.308Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

A race condition in JCacheCodeDataProvider allows an attacker to redeem a single authorization code multiple times via concurrent requests, resulting in the issuance of multiple distinct, valid access tokens. Users are recommended to upgrade to versions 4.2.3, 4.1.8 or 3.6.12, which fix this issue.<br>

### References
* https://lists.apache.org/thread/7q08mz8bcbosp25wok7gr537zlp15mfz


### Credits
* Guanping Zhang reported this vulnerability (finder)


## The authorization code hash (c_hash) is not enforced for the hybrid OIDC flow ## { #CVE-2026-57817 }

CVE-2026-57817 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57817) [\[CVE json\]](./CVE-2026-57817.cve.json) [\[OSV json\]](./CVE-2026-57817.osv.json)



_Last updated: 2026-08-06T10:24:04.605Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

The OpenID Connect Core 1.0 specification mandates that the RP MUST validate the `c_hash` parameter when operating in the Hybrid Flow.&nbsp;If an Apache CXF RP is integrated with a non-compliant or misconfigured Identity Provider (IdP) that omits the `c_hash`, the RP becomes vulnerable to Authorization Code Substitution/Injection attacks.&nbsp;Users are recommended to upgrade to versions 4.2.3 or 4.1.8 or 3.6.12, which fix this issue.

### References
* https://lists.apache.org/thread/pj63c3pf7kkp1xhr53do704fwj3t3htn


### Credits
* Guanping Zhang reported this vulnerability. (finder)


## Denial of Service attack via large attachments ## { #CVE-2026-54225 }

CVE-2026-54225 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-54225) [\[CVE json\]](./CVE-2026-54225.cve.json) [\[OSV json\]](./CVE-2026-54225.osv.json)



_Last updated: 2026-08-06T10:11:39.713Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.3
* Apache CXF from 4.0.0 before 4.1.8
* Apache CXF before 3.6.12


### Description

Apache CXF allows to control the maximum attachment size via the&nbsp;"attachment-max-size". Prior to Apache CXF 4.2.3 and 4.1.8 and 3.6.12, there was no default placed on this size, meaning that a denial of service attack is possible if the user doesn't explicitly set the limit. Users should update to Apache CXF 4.2.3 or 4.1.8 or 3.6.12 which fixes this problem by imposing a default attachment size limit of 50mb.

### References
* https://lists.apache.org/thread/h2bjqm6g58z0j6893qzh728kdtk1byfy


## No restriction on attachment headers per message ## { #CVE-2026-50645 }

CVE-2026-50645 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50645) [\[CVE json\]](./CVE-2026-50645.cve.json) [\[OSV json\]](./CVE-2026-50645.osv.json)



_Last updated: 2026-08-07T11:18:25.630Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF before 4.1.7


### Description

There is no restriction on the amount of attachment headers that a message can contain when being deserialized by Apache CXF, which can lead to uncontrolled resource consumption or a denial of service attack.&nbsp;Users are recommended to upgrade to versions 4.2.2 or 4.1.7, which fix this issue by imposing a maximum default of 500 attachments per message.<br><br>

### References
* https://lists.apache.org/thread/24zb7cqcvykhwm0j797dmdq25s61mj93


## WS JSON request filter trusts metadata from an unvalidated first signature entry ## { #CVE-2026-50634 }

CVE-2026-50634 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50634) [\[CVE json\]](./CVE-2026-50634.cve.json) [\[OSV json\]](./CVE-2026-50634.osv.json)



_Last updated: 2026-06-25T06:51:16.599Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF from 4.0.0 before 4.1.7
* Apache CXF before 3.6.12


### Description

A vulnerability in Apache CXF's&nbsp;JwsJsonContainerRequestFilter can be exploited to cause&nbsp;CXF to process metadata that was not authenticated by the accepted signature.&nbsp;This can bypass the application's assumption<br>
that accepted `Content-Type` or protected HTTP-header metadata came from a verified signature entry, and may steer downstream JAX-RS entity parsing or signed-header consistency checks. Users are recommended to upgrade to versions 4.2.2 or 4.1.7 or 3.6.12, which fix this issue.<br><br>

### References
* https://lists.apache.org/thread/9nfwh9d3m4kznxrk1mz98hl0jml18k0p


### Credits
* Mitchell Benjamin / Revamp Studio. (finder)


## JNDI Injection vulnerability in DispatchMDBMessageListenerImpl ## { #CVE-2026-50633 }

CVE-2026-50633 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50633) [\[CVE json\]](./CVE-2026-50633.cve.json) [\[OSV json\]](./CVE-2026-50633.osv.json)



_Last updated: 2026-06-25T06:49:37.691Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF from 4.0.0 before 4.1.7
* Apache CXF before 3.6.12


### Description

A JNDI Injection vulnerability has been discovered in Apache CXF's JCA integration module, which can allow for code execution, if an attacker is able to manipulate the JCA deployment descriptor (ra.xml) or runtime activation parameters.&nbsp;Users are recommended to upgrade to versions 4.2.2 or 4.1.7 or 3.6.12, which fixes this issue.

### References
* https://lists.apache.org/thread/1czhgovkgzdkyp3t61wthn0foogh2grf


### Credits
* Venkatraman Kumar (r3dw0lfsec), Securin (finder)


## JNDI Injection Vulnerability in JMSConfigFactory ## { #CVE-2026-50632 }

CVE-2026-50632 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50632) [\[CVE json\]](./CVE-2026-50632.cve.json) [\[OSV json\]](./CVE-2026-50632.osv.json)



_Last updated: 2026-06-25T06:47:58.029Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF from 4.0.0 before 4.1.7
* Apache CXF before 3.6.12


### Description

A further incomplete fix for&nbsp;a previous advisory CVE-2026-44417&nbsp;(Untrusted JMS configuration can lead to RCE) for Apache CXF has been identified, which can allow code execution capabilities, if untrusted users are allowed to configure JMS for Apache CXF. Users are recommended to upgrade to versions 4.2.2 or 4.1.7 or 3.6.12, which fixes this issue. <br>

### References
* https://lists.apache.org/thread/740ghch5z5y675cn2kzgtyo5k37n6qcw


### Credits
* Venkatraman Kumar (r3dw0lfsec), Securin (finder)


## OAuth2: TOCTOU Race Condition in Refresh Token Processing ## { #CVE-2026-50631 }

CVE-2026-50631 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50631) [\[CVE json\]](./CVE-2026-50631.cve.json) [\[OSV json\]](./CVE-2026-50631.osv.json)



_Last updated: 2026-06-25T06:40:52.934Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF from 4.0.0 before 4.1.7
* Apache CXF before 3.6.12


### Description

A race condition in AbstractOAuthDataProvider allows concurrent requests using the same Refresh Token to bypass single-use semantics and generate multiple valid Access Tokens, when 'recycleRefreshTokens' is set to false. A leaked refresh token can be replayed concurrently by multiple attackers or threads.&nbsp;Users are recommended to upgrade to versions 4.2.2 or 4.1.7 or 3.6.12, which fixes this issue.<br>

### References
* https://lists.apache.org/thread/s83t3x4r626o9h8rt0ryr1w7w53l1vv8


### Credits
* Guanping Zhang reported this vulnerability. (finder)


## OAuth2: HTTP Response Splitting via WWW-Authenticate Realm Injection ## { #CVE-2026-50630 }

CVE-2026-50630 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50630) [\[CVE json\]](./CVE-2026-50630.cve.json) [\[OSV json\]](./CVE-2026-50630.osv.json)



_Last updated: 2026-06-25T06:42:38.758Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF from 4.0.0 before 4.1.7
* Apache CXF before 3.6.12


### Description

A CRLF injection vulnerability exists in the OAuth2 AuthorizationUtils class. When constructing the WWW-Authenticate response header, the 'realm' parameter is concatenated without sanitizing Carriage Return (CR) and Line Feed (LF) characters. If an attacker can control the realm value, they can inject arbitrary HTTP headers or split the HTTP response entirely.&nbsp;Users are recommended to upgrade to versions 4.2.2 or 4.1.7 or 3.6.12, which fixes this issue.<br>

### References
* https://lists.apache.org/thread/bt7vnjzzkpd6vdhkxv103poor1jy5trm


### Credits
* Guanping Zhang reported this vulnerability. (finder)


## OAuth2: Log Injection via Unsanitized Client Identifier ## { #CVE-2026-50629 }

CVE-2026-50629 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50629) [\[CVE json\]](./CVE-2026-50629.cve.json) [\[OSV json\]](./CVE-2026-50629.osv.json)



_Last updated: 2026-06-25T06:43:46.623Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF from 4.0.0 before 4.1.7
* Apache CXF before 3.6.12


### Description

The 'clientId' parameter from incoming HTTP requests is directly concatenated into OAuth2 server log warning messages without sanitizing control characters. This allows an attacker to inject arbitrary content, including fake log entries, into the server's log files.&nbsp;Users are recommended to upgrade to versions 4.2.2 or 4.1.7 or 3.6.12, which fixes this issue.<br>

### References
* https://lists.apache.org/thread/xw95po30p8th58ms1no6b0f2375cql00


### Credits
* Guanping Zhang reported this vulnerability. (finder)


## OAuth2: Inverted IP Binding Check Defeats Security Control ## { #CVE-2026-50628 }

CVE-2026-50628 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50628) [\[CVE json\]](./CVE-2026-50628.cve.json) [\[OSV json\]](./CVE-2026-50628.osv.json)



_Last updated: 2026-06-25T06:38:43.915Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF from 4.0.0 before 4.1.7
* Apache CXF before 3.6.12


### Description

A logic error in OAuthRequestFilter rejects legitimate requests originating from the bound IP address, while blindly allowing requests from any other IP address. Enabling this<br>
security feature inadvertently creates an inverse security check.&nbsp;Users are recommended to upgrade to versions 4.2.2 or 4.1.7 or 3.6.12, which fixes this issue.<br>

### References
* https://lists.apache.org/thread/vb3ho8lf228gh90m1fpnohf2008xrdxk


### Credits
* Guanping Zhang reported this vulnerability (finder)


## OAuth2: Missing JWT Audience and Issuer Validation in Access Token Validator ## { #CVE-2026-50627 }

CVE-2026-50627 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50627) [\[CVE json\]](./CVE-2026-50627.cve.json) [\[OSV json\]](./CVE-2026-50627.osv.json)



_Last updated: 2026-06-25T06:36:34.767Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF from 4.0.0 before 4.1.7
* Apache CXF before 3.6.12


### Description

The JwtAccessTokenValidator class in Apache CXF fails to validate the 'aud' (Audience) claims of incoming JWT access tokens. This allows a JWT issued for one Resource Server to be successfully replayed against a completely different Resource Server, leading to Token Confusion/Routing attacks.&nbsp;Users are recommended to upgrade to versions 4.2.2 or 4.1.7 or 3.6.12, which fixes this issue.<br>

### References
* https://lists.apache.org/thread/0jfzz9q992957b99tw7hodcqjfyxwb1m


### Credits
* Guanping Zhang reported this vulnerability. (finder)


## Authentication Bypass in OAuth2 TokenIntrospectionService ## { #CVE-2026-50623 }

CVE-2026-50623 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50623) [\[CVE json\]](./CVE-2026-50623.cve.json) [\[OSV json\]](./CVE-2026-50623.osv.json)



_Last updated: 2026-06-25T06:34:24.353Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF from 4.0.0 before 4.1.7
* Apache CXF before 3.6.12


### Description

An authentication bypass vulnerability exists in the OAuth2 TokenIntrospectionService in Apache CXF.&nbsp;Due to a missing 'throw' keyword in the security context check, the introspection endpoint (/services/oauth2/introspect) can be accessed by any unauthenticated network attacker. However note that this is a safeguard only in the case that someone forgot to enable authentication on the service.&nbsp;Users are recommended to upgrade to version 4.2.2 or 4.1.7 or 3.6.12, which fixes this issue.<br><br>

### References
* https://lists.apache.org/thread/ydzj8m5mqmjy13xgyj9mkk9hfff63qq7


### Credits
* Guanping Zhang reported this vulnerability. (finder)


## XML External Entity (XXE) Injection in W3CMultiSchemaFactory and EndpointReferenceUtils ## { #CVE-2026-49875 }

CVE-2026-49875 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49875) [\[CVE json\]](./CVE-2026-49875.cve.json) [\[OSV json\]](./CVE-2026-49875.osv.json)



_Last updated: 2026-06-25T06:58:56.041Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.2
* Apache CXF from 4.0.0 before 4.1.7
* Apache CXF before 3.6.12


### Description

Apache CXF's EndpointReferenceUtils and W3CMultiSchemaFactory classes construct a SAXParserFactory without the necessary JAXP hardening configurations, enabling out-of-band (OOB) 
external entity resolution.&nbsp;Users are recommended to upgrade to versions 4.2.2 or 4.1.7 or 3.6.12, which fix this issue.<br><br>

### References
* https://lists.apache.org/thread/3kb9w5bg90xcp06fccoz9k3gpsvyy79o


### Credits
* Venkatraman Kumar (r3dw0lfsec), Securin (finder)


## LDAP Injection vulnerability in XKMS LDAP Repository ## { #CVE-2026-44930 }

CVE-2026-44930 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44930) [\[CVE json\]](./CVE-2026-44930.cve.json) [\[OSV json\]](./CVE-2026-44930.osv.json)



_Last updated: 2026-05-22T12:16:45.335Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.1
* Apache CXF from 4.0.0 before 4.1.6
* Apache CXF before 3.6.11


### Description

An LDAP injection vulnerability in the LDAP Certificate repository of the XKMS server in Apache CXF may allow an attacker to retrieve arbitrary certificates from the repository.&nbsp;<br>Users are recommended to upgrade to versions 4.2.1, 4.1.6 or 3.6.11, which fix this issue.

### References
* https://lists.apache.org/thread/c1zqxppo1m5z3kbdhjn5p991zk09ynkh


## XXE vulnerability in WS-Transfer functionality ## { #CVE-2026-44618 }

CVE-2026-44618 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44618) [\[CVE json\]](./CVE-2026-44618.cve.json) [\[OSV json\]](./CVE-2026-44618.osv.json)



_Last updated: 2026-05-22T12:17:12.799Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.1
* Apache CXF from 4.0.0 before 4.1.6
* Apache CXF before 3.6.11


### Description

Insecure XML parser configuration in Apache CXF's WS-Transfer module may allow attackers to perform XXE attacks.<br>Users are recommended to upgrade to versions 4.2.1, 4.1.6 or 3.6.11, which fix this issue.

### References
* https://lists.apache.org/thread/c7vb015f8ljmjl44030mn0yfq71f7sd7


### Credits
* Credit to IcySun (icysun@qq.com), 广东东方思维科技有限公司 (finder)


## Incomplete fix for CVE-2025-48913 (Untrusted JMS configuration can lead to RCE) ## { #CVE-2026-44417 }

CVE-2026-44417 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44417) [\[CVE json\]](./CVE-2026-44417.cve.json) [\[OSV json\]](./CVE-2026-44417.osv.json)



_Last updated: 2026-05-22T12:17:23.985Z_

### Affected

* Apache CXF from 4.2.0 before 4.2.1
* Apache CXF from 4.0.0 before 4.1.6
* Apache CXF before 3.6.11


### Description

The fix for&nbsp;CVE-2025-48913: Apache CXF: Untrusted JMS configuration can lead to RCE was not complete, meaning that another path in the code might lead to code execution capabilities, if untrusted users are allowed to configure JMS for Apache CXF. <br>Users are recommended to upgrade to versions 4.2.1, 4.1.6 or 3.6.11, which fix this issue.

### References
* https://lists.apache.org/thread/bqg6gjy2cx7rfyqjxcpv3jwjvmclvz4o


### Credits
* Github / twitter - https://github.com/exploitintel / @exploit_intel (finder)


## Untrusted JMS configuration can lead to RCE ## { #CVE-2025-48913 }

CVE-2025-48913 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-48913) [\[CVE json\]](./CVE-2025-48913.cve.json) [\[OSV json\]](./CVE-2025-48913.osv.json)



_Last updated: 2025-08-08T09:21:18.803Z_

### Affected

* Apache CXF from 4.1.0 before 4.1.3
* Apache CXF from 4.0.0 before 4.0.9
* Apache CXF before 3.6.8


### Description

If untrusted users are allowed to configure JMS for Apache CXF, previously they could use RMI or LDAP URLs, potentially leading to code execution capabilities.  This interface is now restricted to reject those protocols, removing this possibility.<br><br>Users are recommended to upgrade to versions 3.6.8, 4.0.9 or 4.1.3, which fix this issue.

### References
* https://lists.apache.org/thread/f1nv488ztc0js4g5ml2v88mzkzslyh83


### Credits
* M Bhatt (r34p3r) OWASP GenAI Security Project & Blake Gatto (b1oo) Shrewd Research (finder)


## Denial of Service and sensitive data exposure in logs ## { #CVE-2025-48795 }

CVE-2025-48795 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-48795) [\[CVE json\]](./CVE-2025-48795.cve.json) [\[OSV json\]](./CVE-2025-48795.osv.json)



_Last updated: 2025-07-15T14:26:43.340Z_

### Affected

* Apache CXF from 3.5.10 before 3.5.11
* Apache CXF from 3.6.5 before 3.6.6
* Apache CXF from 4.0.6 before 4.0.7
* Apache CXF from 4.1.0 before 4.1.1


### Description

Apache CXF stores large stream based messages as temporary files on the local filesystem. A bug was introduced which means that the entire temporary file is read into memory and then logged. An attacker might be able to exploit this to cause a denial of service attack by causing an out of memory exception. In addition, it is possible to configure CXF to encrypt temporary files to prevent sensitive credentials from being cached unencrypted on the local filesystem, however this bug means that the cached files are written out to logs unencrypted.<br><br>Users are recommended to upgrade to versions 3.5.11, 3.6.6, 4.0.7 or 4.1.1, which fixes this issue.

### References
* https://lists.apache.org/thread/vo5qv02mvv5plmb6z2xf1ktjmrpv3jmn


### Credits
* MAUGIN Thomas https://github.com/Thom-x, Qlik (finder)


## Denial of Service vulnerability with temporary files ## { #CVE-2025-23184 }

CVE-2025-23184 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-23184) [\[CVE json\]](./CVE-2025-23184.cve.json) [\[OSV json\]](./CVE-2025-23184.osv.json)



_Last updated: 2025-01-21T09:35:35.654Z_

### Affected

* Apache CXF before 3.5.10
* Apache CXF from 3.6.0 before 3.6.5
* Apache CXF from 4.0.0 before 4.0.6


### Description

A potential denial of service vulnerability is present in versions of Apache CXF before&nbsp;3.5.10, 3.6.5 and 4.0.6.&nbsp;In some edge cases, the CachedOutputStream instances may not be closed and, if backed by temporary files, may fill up the file system (it applies to servers and clients).<br><br>

### References
* https://lists.apache.org/thread/lfs8l63rnctnj2skfrxyys7v8fgnt122


## Unrestricted memory consumption in CXF HTTP clients ## { #CVE-2024-41172 }

CVE-2024-41172 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-41172) [\[CVE json\]](./CVE-2024-41172.cve.json) [\[OSV json\]](./CVE-2024-41172.osv.json)



_Last updated: 2024-07-19T08:50:42.522Z_

### Affected

* Apache CXF from 3.6.0, 4.0.0 before 3.6.4, 4.0.5


### Description

In versions of Apache CXF before 3.6.4 and 4.0.5 (3.5.x and lower versions are not impacted), a CXF HTTP client conduit may prevent HTTPClient instances from being garbage collected and it is possible that memory consumption will continue to increase, eventually causing the application to run  out of memory<br>

### References
* https://lists.apache.org/thread/n2hvbrgwpdtcqdccod8by28ynnolybl6


## Apache CXF Denial of Service vulnerability in JOSE ## { #CVE-2024-32007 }

CVE-2024-32007 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-32007) [\[CVE json\]](./CVE-2024-32007.cve.json) [\[OSV json\]](./CVE-2024-32007.osv.json)



_Last updated: 2024-07-19T08:50:30.464Z_

### Affected

* Apache CXF before 4.0.5, 3.6.4, 3.5.9


### Description

An improper input validation of the&nbsp;p2c parameter in the Apache CXF JOSE code before 4.0.5, 3.6.4 and 3.5.9&nbsp;allows an attacker to perform a denial of service attack by specifying a large value for this parameter in a token.&nbsp;<br>

### References
* https://lists.apache.org/thread/stwrgsr1llb73nkl16klv9vjqgmmx633


### Credits
* Jingcheng Yang and Jianjun Chen from Sichuan University and Zhongguancun Lab. (finder)


## SSRF vulnerability via WADL stylesheet parameter ## { #CVE-2024-29736 }

CVE-2024-29736 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-29736) [\[CVE json\]](./CVE-2024-29736.cve.json) [\[OSV json\]](./CVE-2024-29736.osv.json)



_Last updated: 2024-07-19T08:50:06.520Z_

### Affected

* Apache CXF before 3.5.9, 3.6.4, 4.0.5


### Description

A SSRF vulnerability in WADL service description in versions of Apache CXF before 4.0.5, 3.6.4 and 3.5.9 allows an attacker to perform SSRF style attacks on REST webservices. The attack only applies if a custom stylesheet parameter is configured.

### References
* https://lists.apache.org/thread/4jtpsswn2r6xommol54p5mg263ysgdw2


### Credits
* Tobias S. Fink (finder)


## Apache CXF SSRF Vulnerability using the Aegis databinding ## { #CVE-2024-28752 }

CVE-2024-28752 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-28752) [\[CVE json\]](./CVE-2024-28752.cve.json) [\[OSV json\]](./CVE-2024-28752.osv.json)



_Last updated: 2024-03-15T10:28:02.596Z_

### Affected

* Apache CXF before 4.0.4, 3.6.3, 3.5.8


### Description

A SSRF vulnerability using the Aegis DataBinding in versions of Apache CXF before 4.0.4, 3.6.3 and 3.5.8 allows an attacker to perform SSRF style attacks on webservices that take at least one parameter of any type. Users of other data bindings (including the default databinding) are not impacted.<br><br>

### References
* https://cxf.apache.org/security-advisories.data/CVE-2024-28752.txt


### Credits
* Tobias S. Fink (finder)


## Apache CXF SSRF Vulnerability ## { #CVE-2022-46364 }

CVE-2022-46364 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-46364) [\[CVE json\]](./CVE-2022-46364.cve.json) [\[OSV json\]](./CVE-2022-46364.osv.json)



_Last updated: 2022-12-13T15:44:20.951Z_

### Affected

* Apache CXF before 3.5.5
* Apache CXF before 3.4.10


### Description

A SSRF vulnerability in parsing the&nbsp;href attribute of XOP:Include in MTOM requests in versions of Apache CXF before 3.5.5 and 3.4.10 allows an attacker to perform SSRF style attacks on webservices that take at least one parameter of any type.&nbsp;

### References
* https://cxf.apache.org/security-advisories.data/CVE-2022-46364.txt?version=1&modificationDate=1670944472739&api=v2


### Credits
* thanat0s from Beijin Qihoo 360 adlab (finder)


## Apache CXF directory listing / code exfiltration ## { #CVE-2022-46363 }

CVE-2022-46363 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-46363) [\[CVE json\]](./CVE-2022-46363.cve.json) [\[OSV json\]](./CVE-2022-46363.osv.json)



_Last updated: 2022-12-13T14:47:26.050Z_

### Affected

* Apache CXF from 3.5 before 3.5.5
* Apache CXF from 3.4 before 3.4.10


### Description

A vulnerability in Apache CXF before versions 3.5.5 and 3.4.10 allows an attacker to perform a remote directory listing or code exfiltration. The vulnerability only applies when the&nbsp;CXFServlet is configured with both the&nbsp;static-resources-list and&nbsp;redirect-query-check attributes. These attributes are not supposed to be used together, and so the vulnerability can only arise if the CXF service is misconfigured.<br><br>

### References
* https://lists.apache.org/thread/pdzo1qgyplf4y523tnnzrcm7hoco3l8c


### Credits
* thanat0s from Beijin Qihoo 360 adlab (finder)


## Apache CXF Denial of service vulnerability in parsing JSON via JsonMapObjectReaderWriter ## { #CVE-2021-30468 }

CVE-2021-30468 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-30468) [\[CVE json\]](./CVE-2021-30468.cve.json) [\[OSV json\]](./CVE-2021-30468.osv.json)



_Last updated: 2021-06-16T11:56:32.302Z_

### Affected

* Apache CXF from Apache CXF before 3.4.4


### Description

A vulnerability in the JsonMapObjectReaderWriter of Apache CXF allows an attacker to submit malformed JSON to a web service, which results in the thread getting stuck in an infinite loop, consuming CPU indefinitely.  

This issue affects Apache CXF versions prior to 3.4.4; Apache CXF versions prior to 3.3.11.

### References
* http://cxf.apache.org/security-advisories.data/CVE-2021-30468.txt.asc


## OAuth 2 authorization service vulnerable to DDos attacks ## { #CVE-2021-22696 }

CVE-2021-22696 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-22696) [\[CVE json\]](./CVE-2021-22696.cve.json) [\[OSV json\]](./CVE-2021-22696.osv.json)



_Last updated: 2021-04-02T09:58:49.120Z_

### Affected

* Apache CXF from unspecified before 3.4.3


### Description

CXF supports (via JwtRequestCodeFilter) passing OAuth 2 parameters via a JWT token as opposed to query parameters (see: The OAuth 2.0 Authorization Framework: JWT Secured Authorization Request (JAR)). Instead of sending a JWT token as a "request" parameter, the spec also supports specifying a URI from which to retrieve a JWT token from via the "request_uri" parameter.

CXF was not validating the "request_uri" parameter (apart from ensuring it uses "https) and was making a REST request to the parameter in the request to retrieve a token.

This means that CXF was vulnerable to DDos attacks on the authorization server, as specified in section 10.4.1 of the spec. 

This issue affects Apache CXF versions prior to 3.4.3; Apache CXF versions prior to 3.3.10.

### References
* https://cxf.apache.org/security-advisories.data/CVE-2021-22696.txt.asc


## Apache CXF Reflected XSS in the services listing page via the styleSheetPath ## { #CVE-2020-13954 }

CVE-2020-13954 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-13954) [\[CVE json\]](./CVE-2020-13954.cve.json) [\[OSV json\]](./CVE-2020-13954.osv.json)



_Last updated: 2020-11-12T12:45:31.751Z_

### Affected

* Apache CXF from unspecified before 3.4.1


### Description

By default, Apache CXF creates a /services page containing a listing of the available endpoint names and addresses. This webpage is vulnerable to a reflected Cross-Site Scripting (XSS) attack via the styleSheetPath, which allows a malicious actor to inject javascript into the web page.

This vulnerability affects all versions of Apache CXF prior to 3.4.1 and 3.3.8.

Please note that this is a separate issue to CVE-2019-17573.


### References
* http://cxf.apache.org/security-advisories.data/CVE-2020-13954.txt.asc?version=1&modificationDate=1605183670659&api=v2


### Credits
* Thanks to Ryan Lambeth for reporting this issue.
