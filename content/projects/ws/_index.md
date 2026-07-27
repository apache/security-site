---
title: Apache Web Services security advisories
description: Security information for Apache Web Services
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Web Services? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Web%20Services).

You can read more about the security policy on:

- [Apache Axiom security model](https://github.com/apache/ws-axiom/blob/master/THREAT-MODEL.md)
- [Apache XmlSchema security model](https://github.com/apache/ws-xmlschema/blob/master/THREAT-MODEL.md)
- [Apache Neethi security model](https://github.com/apache/ws-neethi/blob/master/THREAT-MODEL.md)
- [Apache WSS4J security model](https://github.com/apache/ws-wss4j/blob/master/THREAT-MODEL.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security pages linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

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
