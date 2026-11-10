---
title: Apache Axis security advisories
description: Security information for Apache Axis
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache Axis? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Axis).

You can read more about the security policy on:

- [Apache Axis2 Java Core security model](https://github.com/apache/axis-axis2-java-core/security/policy)
- [Apache Axis2 Java Rampart security model](https://github.com/apache/axis-axis2-java-rampart/security/policy)
- [Apache Axis2 C Core security model](https://github.com/apache/axis-axis2-c-core/security/policy)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security pages linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## unauthenticated remote class instantiation via SOAP fault exceptionName ## { #CVE-2026-90436 }

CVE-2026-90436 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90436) [\[CVE json\]](./CVE-2026-90436.cve.json) [\[OSV json\]](./CVE-2026-90436.osv.json)



_Last updated: 2026-11-06T15:52:59.387Z_

### Affected

* Apache Axis 1.x (EOL) through 1.4
* Apache Axis 1.x (EOL) through 1.4
* Apache Axis 1.x (EOL) from aac718c6035435d96b39d6aebb9c078a13af7cc8 before 41f3b4e8d04e310ca81f86b92630ab2c11d608bd


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Deserialization of an inbound SOAP fault in Apache Axis 1.x allows unauthenticated remote class instantiation. When a SOAP &lt;Fault&gt; carries a &lt;detail&gt;&lt;exceptionName&gt; element, Axis loads the named class and, if a String &lt;data&gt; element is also present, instantiates it through its String constructor before checking that it is an AxisFault. Loading alone runs the class's static initializer. With a suitable class on the application's classpath this leads to remote code execution. The fault is parsed while the engine resolves the target service, before any per-service handler chain runs, so authentication handlers configured on a service do not protect against it. This affects all Apache Axis 1.x versions through 1.4.</p><p>As Axis 1 has been EOL we recommend you migrate to a different SOAP engine, such as Apache Axis 2/Java. Alternatively you could use a build of Axis with the patch from https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd applied. The Apache Axis project does not expect to create an Axis 1.x release fixing this problem.</p>

### References
* https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd
* https://lists.apache.org/thread.html/8slf0j9gz35z56t0glt5h0ncwlbn4bdz


### Credits
* José Apari-Pantigozo from OKIOK (finder)


## deserialization of untrusted Data ## { #CVE-2026-66713 }

CVE-2026-66713 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66713) [\[CVE json\]](./CVE-2026-66713.cve.json) [\[OSV json\]](./CVE-2026-66713.osv.json)



_Last updated: 2026-09-04T13:57:12.851Z_

### Affected

* Apache Axis2/Java through 2.0.0


### Description

Deserialization of Untrusted Data (CWE-502) in the Tribes-based clustering component in Apache Software Foundation Apache Axis2/Java through 2.0.0 on Apache Tomcat (only when Tribes clustering is enabled, which is off by default) allows an unauthenticated remote attacker with network access to the clustering port to execute arbitrary code via a crafted serialized Java object delivered to the cluster channel and deserialized in org.apache.axis2.clustering.tribes.Axis2ChannelListener#messageReceived. Users are recommended to upgrade to version 2.0.1, which fixes this issue by removing the clustering feature entirely.

### References
* https://github.com/apache/axis-axis2-java-core/commit/e6f53b230bddcb40577c84ff290ba51e7265fa15
* https://lists.apache.org/thread/fgggbv3sjjqw7p6q0j88gspt9b2rb728


### Credits
* liuhuajin of Huawei (finder)


## exposeServiceMetadata not enforced on all metadata routes ## { #CVE-2026-123779 }

CVE-2026-123779 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-123779) [\[CVE json\]](./CVE-2026-123779.cve.json) [\[OSV json\]](./CVE-2026-123779.osv.json)



_Last updated: 2026-11-09T10:29:28.370Z_

### Affected

* Apache Axis2/Java before 2.0.2
* Apache Axis2/Java before 2.0.2


### Description

Direct Request ('Forced Browsing') vulnerability in Apache Axis2/Java. The exposeServiceMetadata service parameter was enforced only on the ?wsdl, ?wsdl2 and ?xsd queries. For a service that had disabled it, the packaged .wsdl and .xsd file routes, the named-WSDL ?wsdl=NAME route of the standalone HTTP server, the OpenAPI, Swagger UI and MCP catalog endpoints, the services listing, WS-MetadataExchange GetMetadata and the ping module still disclosed its metadata to anonymous callers, including operation names and request and response schemas. This issue affects Apache Axis2/Java: through 2.0.1. Users are recommended to upgrade to version 2.0.2, which fixes the issue.

### References
* https://axis.apache.org/axis2/java/core/release-notes/2.0.2.html
* https://github.com/apache/axis-axis2-java-core/commit/1671a68660df39459bf22f7b00309e2a8e782117
* https://github.com/apache/axis-axis2-java-core/commit/8a81216b1b723e98a3c801de939201ad68f59b23
* https://lists.apache.org/thread.html/qqn6c4fb8tj0ldmb97c75zzxdjrh5dl3


### Credits
* n0mi1k (finder)


## Unbounded multipart and form-encoded request bodies ## { #CVE-2026-123770 }

CVE-2026-123770 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-123770) [\[CVE json\]](./CVE-2026-123770.cve.json) [\[OSV json\]](./CVE-2026-123770.osv.json)



_Last updated: 2026-11-09T10:26:13.899Z_

### Affected

* Apache Axis2/Java before 2.0.2


### Description

Allocation of Resources Without Limits or Throttling vulnerability in Apache Axis2/Java. The multipart/form-data and application/x-www-form-urlencoded message builders read the request body directly from the transport stream with no size limit, so the servlet container's post-size limit did not apply, and multipart temporary files were not deleted. An unauthenticated caller could exhaust memory or disk. Version 2.0.2 bounds these bodies with configurable limits and deletes temporary files. This issue affects Apache Axis2/Java: through 2.0.1. Users are recommended to upgrade to version 2.0.2, which fixes the issue.

### References
* https://axis.apache.org/axis2/java/core/release-notes/2.0.2.html
* https://github.com/apache/axis-axis2-java-core/commit/1671a68660df39459bf22f7b00309e2a8e782117
* https://github.com/apache/axis-axis2-java-core/commit/2b98e5a31c793589915711f5e29fb4ffb697de70
* https://github.com/apache/axis-axis2-java-core/commit/94c935d1406bc0875daebd36994595efa2f48ae0
* https://lists.apache.org/thread.html/78poyrrggq8tjoos5tgw508m7oylqjlg


### Credits
* n0mi1k (finder)


## Cross-site scripting in the OpenAPI module's Swagger UI page ## { #CVE-2026-123766 }

CVE-2026-123766 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-123766) [\[CVE json\]](./CVE-2026-123766.cve.json) [\[OSV json\]](./CVE-2026-123766.osv.json)



_Last updated: 2026-11-09T10:27:45.558Z_

### Affected

* Apache Axis2/Java from 2.0.1 before 2.0.2


### Description

Improper Neutralization of Input During Web Page Generation (Cross-site Scripting) vulnerability in the OpenAPI module of Apache Axis2/Java. The Swagger UI page served by the OpenAPI module wrote a value derived from the request's Host header into the page without encoding, allowing script injection in the context of the Axis2 origin. This issue affects Apache Axis2/Java: 2.0.1. Users are recommended to upgrade to version 2.0.2, which fixes the issue.

### References
* https://axis.apache.org/axis2/java/core/release-notes/2.0.2.html
* https://github.com/apache/axis-axis2-java-core/commit/1671a68660df39459bf22f7b00309e2a8e782117
* https://lists.apache.org/thread.html/gzxdd4gobm1kb0jdonmn4n8xhjkwlrbg


### Credits
* n0mi1k (finder)


## SSRF via WS-Addressing ReplyTo and FaultTo endpoints ## { #CVE-2026-123753 }

CVE-2026-123753 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-123753) [\[CVE json\]](./CVE-2026-123753.cve.json) [\[OSV json\]](./CVE-2026-123753.osv.json)



_Last updated: 2026-11-09T10:28:45.244Z_

### Affected

* Apache Axis2/Java before 2.0.2


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache Axis2/Java. An unauthenticated caller could supply a non-anonymous WS-Addressing wsa:ReplyTo or wsa:FaultTo address, and Axis2 would open a connection to that address to deliver the response or fault, allowing requests to internal hosts and delivery of response content to a host of the caller's choosing. From 2.0.2, decoupled responses are refused unless allowNonAnonymousResponseEndpoints is enabled, and enabled endpoints are restricted by scheme and screened at both the header-parsing and transport-selection layers. This issue affects Apache Axis2/Java: through 2.0.1. Users are recommended to upgrade to version 2.0.2, which fixes the issue.

### References
* https://axis.apache.org/axis2/java/core/release-notes/2.0.2.html
* https://github.com/apache/axis-axis2-java-core/commit/1671a68660df39459bf22f7b00309e2a8e782117
* https://github.com/apache/axis-axis2-java-core/commit/1b6856b4d7903780786c79327bed1b53ea051a15
* https://lists.apache.org/thread.html/rddzl5jfmlr09yr9qj33by7kzprwwvnc


### Credits
* n0mi1k (finder)


## SSRF via WSDL/XSD schema import resolution ## { #CVE-2026-120832 }

CVE-2026-120832 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-120832) [\[CVE json\]](./CVE-2026-120832.cve.json) [\[OSV json\]](./CVE-2026-120832.osv.json)



_Last updated: 2026-11-09T10:21:58.700Z_

### Affected

* Apache Axis2/Java before 2.0.2


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache Axis2/Java. When Axis2 built a service description from a WSDL, through ServiceClient, AxisService.createClientSideAxisService or WSDLToAxisServiceBuilder, it fetched the absolute URLs in wsdl:import locations and in xsd:import and xsd:include schemaLocations with no scheme or host restriction; the AAR and WAR deployment resolvers also passed absolute schema locations on to the network. An attacker who controls a WSDL or schema processed by an Axis2 application could therefore make the JVM send requests to arbitrary internal or external hosts. This issue affects Apache Axis2/Java: through 2.0.1. Users are recommended to upgrade to version 2.0.2, which fixes the issue.

### References
* https://axis.apache.org/axis2/java/core/release-notes/2.0.2.html
* https://github.com/apache/axis-axis2-java-core/commit/7ac84d8339ad80f8f7f7977cf0caaa28fc3b7b98
* https://lists.apache.org/thread.html/bdf689rhvgg6rtlgqvvq8728f8pkj6zb


### Credits
* Chinmohan Nayak (finder)


## XML External Entity (XXE) injection via imported WSDL/XSD documents ## { #CVE-2026-120761 }

CVE-2026-120761 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-120761) [\[CVE json\]](./CVE-2026-120761.cve.json) [\[OSV json\]](./CVE-2026-120761.osv.json)



_Last updated: 2026-11-09T10:23:17.004Z_

### Affected

* Apache Axis2/Java before 2.0.2


### Description

Improper Restriction of XML External Entity Reference vulnerability in Apache Axis2/Java. When a client built an AxisService from a WSDL URL, through ServiceClient or AxisService.createClientSideAxisService, wsdl4j import resolution was enabled and the documents named by wsdl:import and xsd:import were parsed by wsdl4j's own XML parser, which processes DOCTYPE declarations and external entities. An attacker who controls a WSDL, or a document it imports, could therefore read local files or make the JVM issue network requests. This issue affects Apache Axis2/Java: through 2.0.1. Users are recommended to upgrade to version 2.0.2, which fixes the issue.

### References
* https://github.com/apache/axis-axis2-java-core/commit/1d3457d12399c7721ed3f52e7031d1d24d169460
* https://axis.apache.org/axis2/java/core/release-notes/2.0.2.html
* https://lists.apache.org/thread.html/7jw9v3qz0cdpon7fc6vsvkqp0jdt5kt0


### Credits
* Chinmohan Nayak (finder)


## unbounded JSON request body buffering ## { #CVE-2026-120367 }

CVE-2026-120367 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-120367) [\[CVE json\]](./CVE-2026-120367.cve.json) [\[OSV json\]](./CVE-2026-120367.osv.json)



_Last updated: 2026-11-09T10:31:25.220Z_

### Affected

* Apache Axis2/Java before 2.0.2


### Description

Allocation of Resources Without Limits or Throttling vulnerability in Apache Axis2/Java. The JSON message builders, including the Gson, Moshi and HTTP/2 variants, buffered the entire request body with no size limit, so an unauthenticated caller could exhaust server memory with a large JSON request. Version 2.0.2 bounds JSON request bodies with the configurable jsonMaxRequestSize parameter. This issue affects Apache Axis2/Java: through 2.0.1. Users are recommended to upgrade to version 2.0.2, which fixes the issue.

### References
* https://axis.apache.org/axis2/java/core/release-notes/2.0.2.html
* https://github.com/apache/axis-axis2-java-core/commit/aea2671e3c5ebd8638d37db30d69639223366d5d
* https://lists.apache.org/thread.html/kf6goprhhtvfzb6lwnbvnors7xnq0w0r


### Credits
* MopMonk-AI (finder)


## Apache Axis 1.x (EOL) may allow SSRF when untrusted input is passed to the service admin HTTP API ## { #CVE-2023-51441 }

CVE-2023-51441 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-51441) [\[CVE json\]](./CVE-2023-51441.cve.json) [\[OSV json\]](./CVE-2023-51441.osv.json)



_Last updated: 2024-01-31T09:07:08.922Z_

### Affected

* Apache Axis through 1.3


### Description

** UNSUPPORTED WHEN ASSIGNED ** Improper Input Validation vulnerability in Apache Axis allowed users with access to the admin service to perform possible SSRF<br><p>This issue affects Apache Axis: through 1.3.</p><p>As Axis 1 has been EOL we recommend you migrate to a different SOAP engine, such as Apache Axis 2/Java. Alternatively you could use a build of Axis with the patch from <a target="_blank" rel="nofollow" href="https://github.com/apache/axis-axis1-java/commit/685c309febc64aa393b2d64a05f90e7eb9f73e06">https://github.com/apache/axis-axis1-java/commit/685c309febc64aa393b2d64a05f90e7eb9f73e06</a> applied. The Apache Axis project does not expect to create an Axis 1.x release 
fixing this problem, though contributors that would like to work towards
 this are welcome.
</p>

### References
* https://github.com/apache/axis-axis1-java/commit/685c309febc64aa393b2d64a05f90e7eb9f73e06
* https://lists.apache.org/thread/8nrm5thop8f82pglx4o0jg8wmvy6d9yd


### Credits
* thiscodecc of MoyunSec Vlab and Bing (finder)


## Apache Axis 1.x (EOL) may allow RCE when untrusted input is passed to getService ## { #CVE-2023-40743 }

CVE-2023-40743 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-40743) [\[CVE json\]](./CVE-2023-40743.cve.json) [\[OSV json\]](./CVE-2023-40743.osv.json)



_Last updated: 2023-09-05T14:42:08.579Z_

### Affected

* Apache Axis through 1.3


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** When integrating Apache Axis 1.x in an application, it may not have been obvious that looking up a service through "ServiceFactory.getService" allows potentially dangerous lookup mechanisms such as LDAP. When passing untrusted input to this API method, this could expose the application to DoS, SSRF and even attacks leading to RCE.</div><div><br></div><div>As Axis 1 has been EOL we recommend you migrate to a different SOAP engine, such as Apache Axis 2/Java. As a workaround, you may review your code to verify no untrusted or unsanitized input is passed to "ServiceFactory.getService", or by applying the patch from <a target="_blank" rel="nofollow" href="https://github.com/apache/axis-axis1-java/commit/7e66753427466590d6def0125e448d2791723210">https://github.com/apache/axis-axis1-java/commit/7e66753427466590d6def0125e448d2791723210</a>. The Apache Axis project does not expect to create an Axis 1.x release fixing this problem, though contributors that would like to work towards this are welcome.<br></div>

### References
* https://github.com/apache/axis-axis1-java/commit/7e66753427466590d6def0125e448d2791723210
* https://lists.apache.org/thread/gs0qgk2mgss7zfhzdd6ftfjvm4kp7v82


### Credits
* Letian Yuan (finder)
