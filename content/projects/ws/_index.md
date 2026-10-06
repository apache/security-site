---
title: Apache Web Services security advisories
description: Security information for Apache Web Services
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache Web Services? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Web%20Services).

You can read more about the security policy on:

- [Apache Axiom security model](https://github.com/apache/ws-axiom/blob/master/THREAT-MODEL.md)
- [Apache XmlSchema security model](https://github.com/apache/ws-xmlschema/blob/master/THREAT-MODEL.md)
- [Apache Neethi security model](https://github.com/apache/ws-neethi/blob/master/THREAT-MODEL.md)
- [Apache WSS4J security model](https://github.com/apache/ws-wss4j/blob/master/THREAT-MODEL.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security pages linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unauthenticated denial of service via integer overflow in DER parsing of X.509 certificate extensions ## { #CVE-2026-95616 }

CVE-2026-95616 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-95616) [\[CVE json\]](./CVE-2026-95616.cve.json) [\[OSV json\]](./CVE-2026-95616.osv.json)



_Last updated: 2026-09-30T12:25:24.410Z_

### Affected

* Apache WSS4J from 4.0.0 before 4.0.2
* Apache WSS4J from 3.0.0 before 3.0.6
* Apache WSS4J before 2.4.4


### Description

An integer overflow in WSS4J's DER bounds check lets an oversized allocation pass validation. An unauthenticated attacker can send a SOAP message carrying an X.509 certificate whose SubjectKeyIdentifier extension declares a length of <code>0x7FFFFFFF</code>; WSS4J decodes this while resolving the signature's key reference, before the message is authenticated, so an eleven-byte extension triggers a 2 GB allocation. Repeated requests exhaust server memory.<br>Users are recommended to upgrade to versions 4.0.2 or 3.0.6 or 2.4.4, which fix this issue.

### References
* https://lists.apache.org/thread.html/sdf0fsphkg4qbj7nh2brjgwvcmd67hct


## UsernameToken replay protection bypassed by re-encoding the Nonce ## { #CVE-2026-92899 }

CVE-2026-92899 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-92899) [\[CVE json\]](./CVE-2026-92899.cve.json) [\[OSV json\]](./CVE-2026-92899.osv.json)



_Last updated: 2026-09-30T12:02:37.412Z_

### Affected

* Apache WSS4J from 4.0.0 before 4.0.2
* Apache WSS4J from 3.0.0 before 3.0.6
* Apache WSS4J before 2.4.4


### Description

<p>Apache WSS4J remembers the Nonce of each UsernameToken it accepts, so a captured token cannot be reused. It stored the Nonce as raw base64 text, but authentication decodes that text and uses the bytes.<span>The same bytes can be written as base64 in several ways. An attacker who captured an authenticated request could re-send it with a space added to the Nonce: the password digest still verified, but the token no longer matched the remembered one, so the replay was accepted. Since a UsernameToken does not cover the message body, the captured token could then be reused on requests of the attacker's choosing until it expired. Affects deployments with a nonce replay cache configured, as Apache CXF has by default, and only tokens using a password digest. The cache is now keyed on the decoded Nonce.&nbsp;</span><span>Users are recommended to upgrade to versions 4.0.2 or 3.0.6 or 2.4.4, which fix this issue.</span></p>

### References
* https://lists.apache.org/thread.html/nrzngsz1xm2lztq3t873663xx9wnrwm7


### Credits
* Reported by n0mi1k (finder)


## WS-SecurityPolicy signature checks skipped in the streaming code after an STR-Transform reference ## { #CVE-2026-92121 }

CVE-2026-92121 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-92121) [\[CVE json\]](./CVE-2026-92121.cve.json) [\[OSV json\]](./CVE-2026-92121.osv.json)



_Last updated: 2026-09-30T12:01:51.419Z_

### Affected

* Apache WSS4J from 4.0.0 before 4.0.2
* Apache WSS4J from 3.0.0 before 3.0.6
* Apache WSS4J before 2.4.4


### Description

In the WSS4J streaming (StAX) code, a signature reference using the WS-Security STR-Transform leaves an internal "inside signed content" flag permanently set. The WS-SecurityPolicy enforcer uses that flag to decide whether an element needs checking, so it stops evaluating <code>SignedParts</code> and <code>SignedElements</code> for the rest of the message. A policy requiring the SOAP Body to be signed is then satisfied even when the Body carries no signature, removing the protection against XML Signature Wrapping. Signature verification itself is unaffected. The DOM code is not affected.&nbsp;<br>Users are recommended to upgrade to versions 4.0.2 or 3.0.6 or 2.4.4 which fix this issue.

### References
* https://lists.apache.org/thread.html/oop9p4hpl5o9byosb1qg3z7q1sgnn4pc


### Credits
* Reported by n0mi1k (finder)


## Remote policy fetch lacks a total timeout, allowing a slow server to hang the request indefinitely ## { #CVE-2026-91867 }

CVE-2026-91867 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91867) [\[CVE json\]](./CVE-2026-91867.cve.json) [\[OSV json\]](./CVE-2026-91867.osv.json)



_Last updated: 2026-09-21T11:27:43.899Z_

### Affected

* Apache Neethi before 3.2.4


### Description

When Neethi fetches a remote policy reference, it only limits the time per read, not the whole transfer, so a server that trickles bytes slowly can keep the fetch alive indefinitely and tie up the calling thread (denial of service).<br>Users are recommended to upgrade to version 3.2.4, which fixes this issue.

### References
* https://lists.apache.org/thread/dsr2ktf199mqhw2jtlbklyz7tzd86ycd


### Credits
* This issue was found using Claude agents to study the security of open-source projects (finder)


## Crafted policies cause unbounded work during intersection leading to denial of service ## { #CVE-2026-91866 }

CVE-2026-91866 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91866) [\[CVE json\]](./CVE-2026-91866.cve.json) [\[OSV json\]](./CVE-2026-91866.osv.json)



_Last updated: 2026-09-21T11:27:14.661Z_

### Affected

* Apache Neethi before 3.2.4


### Description

A specially crafted pair of WS-Policy documents can force Neethi's policy-intersection to do exponential amounts of work, pinning the CPU for a long time (denial of service).<br>Users are recommended to upgrade to version 3.2.4, which fixes this issue.

### References
* https://lists.apache.org/thread/zbfxnomgvbmqchqjgc6lk5h0z76k3gh4


### Credits
* This issue was found using Claude agents to study the security of open-source projects (finder)


## Crafted policy references cause exponential expansion during normalization leading to denial of service ## { #CVE-2026-91865 }

CVE-2026-91865 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91865) [\[CVE json\]](./CVE-2026-91865.cve.json) [\[OSV json\]](./CVE-2026-91865.osv.json)



_Last updated: 2026-09-21T11:26:51.403Z_

### Affected

* Apache Neethi before 3.2.4


### Description

A small WS-Policy document using repeated policy references can force Neethi to re-expand the same references exponentially during normalization, consuming huge amounts of CPU and memory (denial of service).<br>Users are recommended to upgrade to version 3.2.4, which fixes this issue.

### References
* https://lists.apache.org/thread/l48btqh02rlpsgf5p6r5ltqk1cb69dtc


### Credits
* This issue was found using Claude agents to study the security of open-source projects (finder)


## Crafted WS-Policy documents bypass element/attribute limits causing memory exhaustion ## { #CVE-2026-91864 }

CVE-2026-91864 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91864) [\[CVE json\]](./CVE-2026-91864.cve.json) [\[OSV json\]](./CVE-2026-91864.osv.json)



_Last updated: 2026-09-21T11:26:18.944Z_

### Affected

* Apache Neethi before 3.2.4


### Description

A specially crafted WS-Policy document can pack unlimited content inside a policy assertion, which Neethi copies into memory without counting it against its size limits, exhausting the heap (denial of service).<br>Users are recommended to upgrade to version 3.2.4, which fixes this issue.

### References
* https://lists.apache.org/thread/400kbynbyhqhsjkv1yz251jm9wdz8z69


### Credits
* This issue was found using Claude agents to study the security of open-source projects (finder)


## Uncontrolled recursion while parsing crafted WS-Policy documents allows denial of service ## { #CVE-2026-91863 }

CVE-2026-91863 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91863) [\[CVE json\]](./CVE-2026-91863.cve.json) [\[OSV json\]](./CVE-2026-91863.osv.json)



_Last updated: 2026-09-21T11:25:25.043Z_

### Affected

* Apache Neethi before 3.2.4


### Description

A specially crafted WS-Policy document with deeply nested policy elements can bypass Neethi's nesting-depth limit and exhaust the thread stack, crashing the parser (denial of service).<br>Users are recommended to upgrade to version 3.2.4, which fixes this issue.

### References
* https://lists.apache.org/thread/72kxj71lvrqqx90xxqqctvpbw0t8mpxw


### Credits
* This issue was found using Claude agents to study the security of open-source projects (finder)


## WSS4J EncryptedHeader child confusion causing wrong protected-header selection ## { #CVE-2026-89238 }

CVE-2026-89238 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-89238) [\[CVE json\]](./CVE-2026-89238.cve.json) [\[OSV json\]](./CVE-2026-89238.osv.json)



_Last updated: 2026-09-30T11:59:03.446Z_

### Affected

* Apache WSS4J from 4.0.0 before 4.0.2
* Apache WSS4J from 3.0.0 before 3.0.6
* Apache WSS4J before 2.4.4


### Description

WSS4J EncryptedHeader child confusion could promote an attacker-controlled plaintext element as the decrypted header, leading to incorrect confidentiality coverage and possible policy bypass.<br>Users are recommended to upgrade to versions 4.0.2 or 3.0.6 or 2.4.4, which fix this issue.

### References
* https://lists.apache.org/thread.html/1lv4hpl8kon1ns5txjnhn2m2sh9rl22w


### Credits
* Reported by n0mi1k (finder)


## SAML Sender-Vouches Authentication Bypass ## { #CVE-2026-88920 }

CVE-2026-88920 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-88920) [\[CVE json\]](./CVE-2026-88920.cve.json) [\[OSV json\]](./CVE-2026-88920.osv.json)



_Last updated: 2026-09-30T11:57:51.366Z_

### Affected

* Apache WSS4J from 4.0.0 before 4.0.2
* Apache WSS4J from 3.0.0 before 3.0.6
* Apache WSS4J before 2.4.4


### Description

An authentication bypass in the DOM security processor in Apache WSS4J allows unauthenticated remote attackers to forge authenticated SOAP messages via a crafted unsigned SAML sender-vouches assertion containing an attacker-controlled key.<br><br>Users are recommended to upgrade to versions 4.0.2 or 3.0.6 or 2.4.4, which fix this issue.

### References
* https://lists.apache.org/thread.html/grt43m3bgbzz0mk0cnho3rcybb1j01z9


### Credits
* Reported by n0mi1k (finder)


## Streaming WS-SecurityPolicy validation may skip element-protection checks. ## { #CVE-2026-87830 }

CVE-2026-87830 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-87830) [\[CVE json\]](./CVE-2026-87830.cve.json) [\[OSV json\]](./CVE-2026-87830.osv.json)



_Last updated: 2026-09-30T11:56:54.179Z_

### Affected

* Apache WSS4J from 4.0.0 before 4.0.2
* Apache WSS4J from 3.0.0 before 3.0.6
* Apache WSS4J before 2.4.4


### Description

In the StAX streaming WS-SecurityPolicy validator, certain relative or unsupported XPath expressions can be converted into paths that never match the actual XML element path. A remote SOAP peer may therefore send a required element without the expected signature or encryption.<div><br>Users are recommended to upgrade to versions 4.0.2 or 3.0.6 or 2.4.4, which fix this issue.</div>

### References
* https://lists.apache.org/thread.html/lwlozb1x20d16f9dnyvoygc9rrhzq2vn


### Credits
* Reported by n0mi1k (finder)


## Insufficient Validation of Derived-Key Parameters ## { #CVE-2026-85532 }

CVE-2026-85532 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-85532) [\[CVE json\]](./CVE-2026-85532.cve.json) [\[OSV json\]](./CVE-2026-85532.osv.json)



_Last updated: 2026-09-30T11:55:32.052Z_

### Affected

* Apache WSS4J from 4.0.0 before 4.0.2
* Apache WSS4J from 3.0.0 before 3.0.6
* Apache WSS4J before 2.4.4


### Description

Apache WSS4J accepted attacker-controlled derived-key lengths and offsets without adequate bounds. This could permit cryptographically weak keys or excessive CPU and memory consumption when processing crafted WS-Security messages. The fixes enforce a minimum key length of 16 bytes, a maximum length of 512 bytes, and a maximum offset of 4096 bytes.<div><br>Users are recommended to upgrade to versions 4.0.2 or 3.0.6 or 2.4.4, which fix this issue.</div>

### References
* https://lists.apache.org/thread.html/7jllcpbf4nbzhdp2vchz5yplnl5w6vd6


### Credits
* This issue was independently reported by Ho1aAs (GitHub: @HolaAsuka) and also found using Claude agents to study the security of open-source projects (finder)


## Remote PolicyReference fetch lacks resource bounds ## { #CVE-2026-66144 }

CVE-2026-66144 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66144) [\[CVE json\]](./CVE-2026-66144.cve.json) [\[OSV json\]](./CVE-2026-66144.osv.json)



_Last updated: 2026-07-24T12:08:26.736Z_

### Affected

* Apache Neethi before 3.2.3


### Description

Although remote policy references are not retrieved during policy normalization, if they are manually retrieved via the API it can cause a denial of service attack if a huge policy is retrieved. Users are recommended to upgrade to version 3.2.3, which fixes this issue by imposing a default maximum size on data read from remote policy references.

### References
* https://lists.apache.org/thread/80xwwbhkqvbwkkmco6yl6fr5xkpdysjf


### Credits
* Reported by LTSHFWJT (finder)


## Missing global alternative-output budget across policy computation paths ## { #CVE-2026-66143 }

CVE-2026-66143 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66143) [\[CVE json\]](./CVE-2026-66143.cve.json) [\[OSV json\]](./CVE-2026-66143.osv.json)



_Last updated: 2026-07-24T12:07:51.381Z_

### Affected

* Apache Neethi before 3.2.3


### Description

It is possible to bypass the&nbsp;<span style="background-color: rgb(255, 255, 255);">maximum number of normalized policy alternatives that was introduced in Apache Neethi 3.2.2 via certain crafted policies, which may lead to a denial of service attack via resource consumption.&nbsp;</span>Users are recommended to upgrade to version 3.2.3, which fixes this issue.

### References
* https://lists.apache.org/thread/s6o6p5pvcbcsk54dlg6j699t5gxol28w


### Credits
* Reported by LTSHFWJT (finder)


## Uncontrolled recursion in policy processing ## { #CVE-2026-66142 }

CVE-2026-66142 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66142) [\[CVE json\]](./CVE-2026-66142.cve.json) [\[OSV json\]](./CVE-2026-66142.osv.json)



_Last updated: 2026-07-24T12:07:24.609Z_

### Affected

* Apache Neethi before 3.2.3


### Description

Apache Neethi is vulnerable to uncontrolled recursion when parsing policies that lack policy Ids or with deeply nested structures, which may lead to a denial of service attack when parsing policies due to runtime memory exhaustion. Users are recommended to upgrade to version 3.2.3, which fixes this issue.

### References
* https://lists.apache.org/thread/fomwtwt4pzzhxn4fyn3skykto913vfzt


### Credits
* Reported by LTSHFWJT (finder)


## Unrestricted HTTP Redirect Following in Policy References ## { #CVE-2026-42404 }

CVE-2026-42404 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42404) [\[CVE json\]](./CVE-2026-42404.cve.json) [\[OSV json\]](./CVE-2026-42404.osv.json)



_Last updated: 2026-05-01T09:46:48.474Z_

### Affected

* Apache Neethi before 3.2.2


### Description

Apache Neethi does not impose any restrictions on URIs when manually fetching remote policy references through the PolicyReference API. When an application explicitly calls the API to retrieve a policy from a remote URI, an outbound request is made for arbitrary protocols and internal IP adddresses. From 3.2.2, only http or https URIs are allowed, and link-local/multicast/any-local addresses are forbidden.<br><br>Users are recommended to upgrade to version 3.2.2, which fixes this issue.

### References
* https://lists.apache.org/thread/zdspnt64zznyjyn648553kptx69w23oq


## Circular Policy Reference Infinite Loop ## { #CVE-2026-42403 }

CVE-2026-42403 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42403) [\[CVE json\]](./CVE-2026-42403.cve.json) [\[OSV json\]](./CVE-2026-42403.osv.json)



_Last updated: 2026-05-01T09:36:06.796Z_

### Affected

* Apache Neethi before 3.2.2


### Description

Apache Neethi does not properly detect circular references in policy definitions. When a WS-Policy document contains circular policy references (where Policy A references Policy B which references Policy A), the policy normalization process can enter an infinite loop or cause excessive recursion, leading to a stack overflow or application hang. An attacker can craft malicious policy documents with circular references to cause a Denial of Service condition<br><br>Users are recommended to upgrade to version 3.2.2, which fixes this issue.

### References
* https://lists.apache.org/thread/zm6t8skkkskjwk1881l4m4n0l7dqclzo


## Policy Normalization Unbounded Resource Allocation DoS ## { #CVE-2026-42402 }

CVE-2026-42402 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42402) [\[CVE json\]](./CVE-2026-42402.cve.json) [\[OSV json\]](./CVE-2026-42402.osv.json)



_Last updated: 2026-05-01T09:35:22.670Z_

### Affected

* Apache Neethi before 3.2.2


### Description

Apache Neethi is vulnerable to a Denial of Service attack through algorithmic complexity in policy normalization. Specially crafted WS-Policy documents can trigger an exponential Cartesian cross-product expansion during the normalization process, causing unbounded memory allocation that exhausts the JVM heap. This occurs when the normalization process generates an excessive number of policy alternatives without bounds, leading to runtime memory exhaustion.<br><br>Users should upgrade to 3.2.2 which limits the maximum number of normalized policy alternatives.

### References
* https://lists.apache.org/thread/p826j0phhmr9f83wzpmys1y0bdfrr2q4


## Denial of service through cyclic schema definitions in the schema walker ## { #CVE-2026-102497 }

CVE-2026-102497 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-102497) [\[CVE json\]](./CVE-2026-102497.cve.json) [\[OSV json\]](./CVE-2026-102497.osv.json)



_Last updated: 2026-09-29T11:34:15.228Z_

### Affected

* Apache XMLSchema before 2.3.3


### Description

<p>The Apache XmlSchema walker (xmlschema-walker) doesn't detect cycles in type derivation, substitution groups, model groups or attribute groups. A malicious schema with such a cycle can make the walker recurse until the stack overflows, causing a denial of service.<br><br>Users are recommended to upgrade to version 2.3.3, which fixes this issue.</p>

### References
* https://lists.apache.org/thread/1cj02tobjyhjqq723bvg78yxkqt1lk7k


### Credits
* This issue was found using Claude agents to study the security of open-source projects (finder)


## Denial of service through deeply nested schema structures ## { #CVE-2026-102496 }

CVE-2026-102496 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-102496) [\[CVE json\]](./CVE-2026-102496.cve.json) [\[OSV json\]](./CVE-2026-102496.osv.json)



_Last updated: 2026-09-29T11:34:02.943Z_

### Affected

* Apache XMLSchema before 2.3.3


### Description

Apache XmlSchema doesn't limit how deeply schema structures can be nested when it builds its schema model, so a malicious schema can make parsing recurse until the stack overflows. This causes a denial of service.<br>Users are recommended to upgrade to version 2.3.3, which fixes this issue.

### References
* https://lists.apache.org/thread/9z1vg8wmvwpfw748fb2nb55w4hgbnxol


### Credits
* This issue was found using Claude agents to study the security of open-source projects (finder)


## Denial of service through unbounded recursion when resolving schema imports and includes ## { #CVE-2026-102495 }

CVE-2026-102495 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-102495) [\[CVE json\]](./CVE-2026-102495.cve.json) [\[OSV json\]](./CVE-2026-102495.osv.json)



_Last updated: 2026-09-29T11:33:50.143Z_

### Affected

* Apache XMLSchema before 2.3.3


### Description

Apache XmlSchema doesn't limit how deeply schema imports and includes can be nested, so a malicious schema can make parsing recurse until the stack overflows. This causes a denial of service.<br>Users are recommended to upgrade to version 2.3.3, which fixes this issue.

### References
* https://lists.apache.org/thread/l339q3oldm0cd2lph4b6f93fd07x9g6s


### Credits
* This issue was found using Claude agents to study the security of open-source projects (finder)


## Apache SOAP allows unauthenticated users to potentially invoke arbitrary code ## { #CVE-2022-45378 }

CVE-2022-45378 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-45378) [\[CVE json\]](./CVE-2022-45378.cve.json)

_Last updated: 2022-11-14T14:06:51.577Z_

### Affected

* Apache SOAP at 2.3
* Apache SOAP from Apache SOAP before 2.3 unknown


### Description

In the default configuration of Apache SOAP, an RPCRouterServlet is available without authentication. This gives an attacker the possibility to invoke methods on the classpath that meet certain criteria. Depending on what classes are available on the classpath this might even lead to arbitrary remote code execution. NOTE: This vulnerability only affects products that are no longer supported by the maintainer

### References
* https://lists.apache.org/thread/g4l64s283njhnph2otx7q4gs2j952d31


### Credits
*   Apache would like to thank TsungShu Chiu (CHT Security) for reporting this issue


## Apache SOAP: XML External Entity Injection (XXE) allows unauthenticated users to read arbitrary files via HTTP ## { #CVE-2022-40705 }

CVE-2022-40705 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-40705) [\[CVE json\]](./CVE-2022-40705.cve.json) [\[OSV json\]](./CVE-2022-40705.osv.json)



_Last updated: 2022-09-22T08:11:36.490Z_

### Affected

* Apache SOAP from 2.2 before Apache SOAP*


### Description

An Improper Restriction of XML External Entity Reference vulnerability in RPCRouterServlet of Apache SOAP allows an attacker to read arbitrary files over HTTP. This issue affects Apache SOAP version 2.2 and later versions. It is unknown whether previous versions are also affected.  NOTE: This vulnerability only affects products that are no longer supported by the maintainer

### References
* https://lists.apache.org/thread/02yo04w93rdjmllz4454lvodn5xzhwhl


### Credits
* Apache would like to thank TsungShu Chiu (CHT Security) for reporting this issue
