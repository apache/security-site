---
title: Apache NiFi security advisories
description: Security information for Apache NiFi
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache NiFi? Send your report to the [Apache NiFi Security Team](mailto:security@nifi.apache.org?subject=NiFi).

You can read more about the security policy on:

- [Apache NiFi security model](https://nifi.apache.org/documentation/security/)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improper Limitation of Pathname in Persisted Extension Bundles ## { #CVE-2026-87976 }

CVE-2026-87976 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-87976) [\[CVE json\]](./CVE-2026-87976.cve.json) [\[OSV json\]](./CVE-2026-87976.osv.json)



_Last updated: 2026-09-16T19:32:43.274Z_

### Affected

* Apache NiFi Registry from 0.4.0 through 2.11.0


### Description

Apache NiFi Registry 0.4.0 through 2.11.0 are subject to path manipulation when storing extension bundle content using group, artifact, and version coordinates from uploaded NAR manifests. The default file persistence provider used coordinates as filesystem path components without rejected parent-directory names, and the path-containment check compared an unnormalized resolved path. An authenticated user authorized to write and delete bundles in a bucket can upload a NAR with a crafted manifest resulting in file system operations outside of the file persistence directory. Upgrading to Apache NiFi Registry 2.12.0 is the recommended mitigation, which rejects parent-directory coordinates and requires a normalized path to remain a strict child of the storage root location.

### References
* https://lists.apache.org/thread/kw89toml5zq20ry3279mx7y184vrlb8x


### Credits
* lichoin (finder)


## Missing Process Group Authorization for Connector Migration ## { #CVE-2026-86089 }

CVE-2026-86089 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86089) [\[CVE json\]](./CVE-2026-86089.cve.json) [\[OSV json\]](./CVE-2026-86089.osv.json)



_Last updated: 2026-09-16T19:34:58.987Z_

### Affected

* Apache NiFi at 2.11.0


### Description

Apache NiFi 2.11.0 supports migrating the contents of a version-controlled Process Group into a Connector using REST API methods that list eligible migration sources and submit migration requests. The framework authorized both methods against the target Connector alone, without evaluating access to the Process Groups involved. The absence of Process Group authorization allowed an authenticated user with read access to a Connector to enumerate the identifiers, names, and flow registry details of version-controlled Process Groups outside the scope of granted read policies. It also allowed a user with write access to a Connector to migrate a Process Group without write access to that Process Group, copying the flow definition, referenced assets, and component state into the Connector, and leaving the source Process Group disabled and renamed. Migration excludes sensitive property values and requires the source Process Group to be stopped with empty queues, which limits the scope of exposure. Apache NiFi installations that do not implement component-level authorization policies for Process Groups are not subject to this vulnerability, because the framework enforces Connector write permissions as the security boundary. Upgrading to Apache NiFi 2.12.0 is the recommended mitigation, which filters migration sources to Process Groups the requesting user is authorized to read, and requires write access to the source Process Group when submitting a migration request.

### References
* https://lists.apache.org/thread/lnpqnn61k62fkgxqd9cftf7sr77jhrk1


### Credits
* ZsZsec (finder)
* Alpesh Bhagwatkar (finder)


## Missing Authorization for Components Referenced in Flow Update Methods ## { #CVE-2026-82561 }

CVE-2026-82561 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82561) [\[CVE json\]](./CVE-2026-82561.cve.json) [\[OSV json\]](./CVE-2026-82561.osv.json)



_Last updated: 2026-09-16T19:37:17.700Z_

### Affected

* Apache NiFi from 1.5.0 through 2.11.0


### Description

Apache NiFi 1.5.0 through 2.11.0 provide REST API methods that replace the entire contents of a Process Group using a client-supplied flow definition, covering Process Group flow replacement together with versioned flow update and rebase operations. Framework authorization for these methods was limited to read and write privileges on the Process Group itself, unlike the corresponding asynchronous update request methods, which also authorize the components encapsulated in the Process Group along with referenced Controller Services, Parameter Contexts, and Parameter Providers. As a result of the missing authorization, an authenticated user with write access to a Process Group could supply a flow definition that modifies or removes components in descendant Process Groups protected by more restrictive access policies, and could bind components to Controller Services and Parameter Contexts without authorization for those referenced components. Existing verification checks limited the impact to stopped components, and the issue applies only to deployments that use component-level authorization policies, because the framework enforces write permissions as the security boundary. Upgrading to Apache NiFi 2.12.0 is the recommended mitigation, which applies consistent reference resolution and component authorization across Process Group replacement and versioned flow update methods

### References
* https://lists.apache.org/thread/opk7l8wqvnl85qxlzj3dnxp6qbk27lwm


### Credits
* n0mi1k (finder)


## Missing Authorization for Assets and Secrets Referenced by Connector Configuration ## { #CVE-2026-81866 }

CVE-2026-81866 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-81866) [\[CVE json\]](./CVE-2026-81866.cve.json) [\[OSV json\]](./CVE-2026-81866.osv.json)



_Last updated: 2026-09-16T19:38:01.279Z_

### Affected

* Apache NiFi from 2.9.0 through 2.11.0


### Description

Apache NiFi 2.9.0 through 2.11.0 provide Connector configuration update and verification REST API methods that do not enforce authorization checking on Assets and Secrets referenced in proposed configuration. Updating or verifying a Connector configuration step can apply Asset and Secret references, but framework authorization was limited to write privileges on the Connector itself. As a result of the missing authorization, an authenticated user authorized to modify a Connector, but not authorized to read a referenced Parameter Provider, could apply Secret values backed by that Parameter Provider. The same methods also accepted Asset identifiers without verifying that the Asset belonged to the Connector being configured. Apache NiFi installations that do not implement different levels of authorization across Connectors and Parameter Providers are not subject to this vulnerability, because the framework enforces write permissions on the Connector as the security boundary. Upgrading to Apache NiFi 2.12.0 is the recommended mitigation, which authorizes read access to referenced Parameter Providers and verifies Connector ownership of referenced Assets during configuration update and verification.

### References
* https://lists.apache.org/thread/rv49gwf4yb00ykv0zzfd509boxflolsf


### Credits
* h1ei1 (finder)
* Arpit Jain (finder)


## Improper Handling of Case Sensitivity for Content-Encoding in HTTP Requests ## { #CVE-2026-70469 }

CVE-2026-70469 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-70469) [\[CVE json\]](./CVE-2026-70469.cve.json) [\[OSV json\]](./CVE-2026-70469.osv.json)



_Last updated: 2026-09-16T19:38:38.299Z_

### Affected

* Apache NiFi at 2.11.0


### Description

Apache NiFi 2.11.0 disabled support for gzip-encoded HTTP requests for the application REST API and rejected requests that included the standard Content-Encoding header indicating gzip encoding. The framework enforcement filter did not check multiple instances of the Content-Encoding header and did not reject non-standard identifiers for gzip encoding, allowing a malicious client to send crafted requests that could consume excessive amounts of memory. Upgrading to Apache NiFi 2.12.0 is the recommended mitigation, which disables decompression of gzip-encoded HTTP requests regardless of header number or encoding identifiers.

### References
* https://lists.apache.org/thread/mjpv7r4djgn7fdvhnpjwgr2rcto47mx0


### Credits
* mak3bread (Minseong Kim) (finder)


## Uncontrolled Resource Consumption through Decompression of HTTP Requests ## { #CVE-2026-68981 }

CVE-2026-68981 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68981) [\[CVE json\]](./CVE-2026-68981.cve.json) [\[OSV json\]](./CVE-2026-68981.osv.json)



_Last updated: 2026-08-19T04:13:13.429Z_

### Affected

* Apache NiFi from 1.5.0 through 2.10.0


### Description

Apache NiFi 1.5.0 through 2.10.0 support gzip-encoded HTTP requests for the application REST API using a Jersey encoding filter. The framework enforced a configurable maximum request size on the compressed payload rather than the decompressed output, allowing a malicious client to send crafted requests that could consume excessive amounts of memory. Upgrading to Apache NiFi 2.11.0 is the recommended mitigation, which relocates response compression to Jetty Server and disables decompression of gzip-encoded HTTP requests.

### References
* https://lists.apache.org/thread/vxrqn7poyf1wx6gdy7c0dxqfqkctjngg


### Credits
* mak3bread (Minseong Kim) (finder)


## Authorization Bypass for Parameter Context Asset Deletion ## { #CVE-2026-68980 }

CVE-2026-68980 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68980) [\[CVE json\]](./CVE-2026-68980.cve.json) [\[OSV json\]](./CVE-2026-68980.osv.json)



_Last updated: 2026-08-03T19:58:50.048Z_

### Affected

* Apache NiFi from 2.0.0 through 2.10.0


### Description

Apache NiFi 2.0.0 through 2.10.0 support creating, reading, and deleting Assets associated with Parameter Contexts through the REST API. The framework authorizes asset deletion against the owning Parameter Context using the supplied Parameter Context Identifier and Asset Identifier. The framework performed authorized based on the supplied Parameter Context Identifier without verifying the requested Identifier against the stored Identifier. Apache NiFi installations that do not implement different levels of authorization across Parameter Contexts are not subject to this vulnerability, because the framework enforces write permissions as the security boundary. Upgrading to Apache NiFi 2.11.0 is the recommended mitigation, which verifies Parameter Context ownership of the requested Asset before deletion using the same strategy applied to Asset read operations.

### References
* https://lists.apache.org/thread/yo8k6tt3zxjm49zzhly3453v0xhwm3o1


### Credits
* mak3bread (Minseong Kim) (finder)


## Missing Authorization for Components Referenced by Parameter Context Updates ## { #CVE-2026-68979 }

CVE-2026-68979 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68979) [\[CVE json\]](./CVE-2026-68979.cve.json) [\[OSV json\]](./CVE-2026-68979.osv.json)



_Last updated: 2026-09-01T12:29:30.785Z_

### Affected

* Apache NiFi from 1.10.0 through 2.10.0


### Description

Apache NiFi 1.10.0 through 2.10.0 provide a Parameter Context update REST API method that does not enforce authorization checking on components referencing Parameter values. Updating a Parameter Context can change parameter values that affect referencing components, but framework authorization was limited to read and write privileges on the Parameter Context itself. As a result of the missing authorization, an authenticated user authorized to modify a Parameter Context, but not authorized on referencing components, could alter Parameter values affecting those components. In deployments where a Parameter value contains executable scripting content, updating a Parameter can result in code execution during automatic component validation, without starting the referencing component. The impact was limited to stopped components by existing verification checks, and the issue applies only to deployments that use component-level authorization policies. Upgrading to Apache NiFi 2.11.0 is the recommended mitigation, which aligns the Parameter Context update method authorization with other methods, adding authorization checking on affected components.

### References
* https://lists.apache.org/thread/xwz8wsss2ovx07tns96rkc3n7cm4xfrq


### Credits
* D0HY30N (finder)


## Incorrect Authorization for Parameter Context Validation Requests ## { #CVE-2026-62354 }

CVE-2026-62354 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-62354) [\[CVE json\]](./CVE-2026-62354.cve.json) [\[OSV json\]](./CVE-2026-62354.osv.json)



_Last updated: 2026-08-03T19:57:33.492Z_

### Affected

* Apache NiFi from 1.10.0 through 2.10.0


### Description

Authorization handling for Parameter Context validation requests in Apache NiFi 1.10.0 through 2.10.0 allows clients with read access to submit proposed Parameter values. The proposed values override current configuration, enabling users with read access to invoke predefined component validation methods with alternative settings. Apache NiFi installations that do not implement different levels of authorization for viewing and modifying Parameter Context configuration are not subject to this vulnerability. Upgrading to Apache NiFi 2.11.0 is the recommended mitigation, requiring write access to submit Parameter Context validation requests.

### References
* https://lists.apache.org/thread/l17xcnnf1rm7qljmypyjxmh62cx4o4wj


### Credits
* Nguyen Van Hiep from MBBank (finder)


## Missing Validation for Proxy Host Headers ## { #CVE-2026-54665 }

CVE-2026-54665 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-54665) [\[CVE json\]](./CVE-2026-54665.cve.json) [\[OSV json\]](./CVE-2026-54665.osv.json)



_Last updated: 2026-06-22T07:34:12.067Z_

### Affected

* Apache NiFi from 0.0.1 before 2.10.0


### Description

Apache NiFi 0.0.1 through 2.9.0 support building qualified URLs from one of several HTTP request headers that provide an alternative to the standard Host header without validating the values provided. Apache NiFi 1.6.0 introduced a configurable application property to restrict values provided in the HTTP Host header, but did not apply the validation to alternative Proxy and Forwarded headers. The absence of proxy host header validation allowed a client to instruct Apache NiFi web services to construct invalid qualified URLs for redirection or data references. Upgrading to Apache NiFi 2.10.0 is the recommended mitigation, which implements validation for the X-ProxyHost and X-Forwarded-Host HTTP request headers based on the nifi.web.proxy.host property. Enabling header validation requires configuring the application with HTTPS. Reverse proxy servers in front of Apache NiFi are responsible for filtering input request headers and providing allowed values to the application.

### References
* https://lists.apache.org/thread/y0yoblon8f6dp00qz5r90cxq5n6g4j6k


### Credits
* Jose Rivas (finder)


## Missing Authorization of Restricted Permissions when Replacing Flow Contents ## { #CVE-2026-44914 }

CVE-2026-44914 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44914) [\[CVE json\]](./CVE-2026-44914.cve.json) [\[OSV json\]](./CVE-2026-44914.osv.json)



_Last updated: 2026-06-22T07:38:00.013Z_

### Affected

* Apache NiFi from 1.12.0 through 2.9.0


### Description

Apache NiFi 1.12.0 through 2.9.0 are missing authorization when replacing Process Groups that include extension components with specific Required Permissions based on the Restricted annotation. The Restricted annotation indicates additional privileges required, but framework authorization did not check restricted status when handling requests to replace Process Groups. The missing authorization permits a user with general write access to add components with Restricted status. Apache NiFi installations that do not implement specific authorization for Restricted components are not subject to this vulnerability because the framework enforces write permissions as the security boundary. Upgrading to Apache NiFi 2.9.0 is the recommended mitigation, which removes the implementation of Restricted status authorization from the framework.<br>

### References
* https://lists.apache.org/thread/ydr34t03xd1n0t9oogpzogjrd5y93838


### Credits
* Roberto Suggi Liverani from NATO Cyber Security Centre (NCSC) (finder)


## Improper Escaping of Table Names in CaptureChangeMySQL ## { #CVE-2026-44913 }

CVE-2026-44913 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44913) [\[CVE json\]](./CVE-2026-44913.cve.json) [\[OSV json\]](./CVE-2026-44913.osv.json)



_Last updated: 2026-06-22T07:36:39.632Z_

### Affected

* Apache NiFi from 1.2.0 through 2.9.0


### Description

Improper escaping of database table names in the CaptureChangeMySQL Processor included with Apache NiFi 1.2.0 through 2.9.0 allows for injecting SQL commands using crafted naming. Manual quoted boundaries added in Apache NiFi 1.8.0 narrowed the scope of potential injection options, but did not cover additional strategies. Apache NiFi installations that do not use the CaptureChangeMySQL Processor are not subject to this vulnerability. Upgrading to Apache NiFi 2.10.0 is the recommended mitigation, which incorporates more robust identifier escaping.

### References
* https://lists.apache.org/thread/c8vkt5rz4dqql6sjxgrr3zdkbt1sfmsl


### Credits
* Roberto Suggi Liverani from NATO Cyber Security Centre (NCSC) (finder)


## Incorrect Authorization for Configuration Verification Requests ## { #CVE-2026-44911 }

CVE-2026-44911 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44911) [\[CVE json\]](./CVE-2026-44911.cve.json) [\[OSV json\]](./CVE-2026-44911.osv.json)



_Last updated: 2026-06-22T07:37:09.411Z_

### Affected

* Apache NiFi from 1.15.0 through 2.9.0


### Description

<div>Authorization handling for component configuration verification requests in Apache NiFi 1.15.0 through 2.9.0 allows clients with read access to submit proposed configuration properties. The proposed properties override current configuration, enabling users with read access to invoke predefined verification methods with alternative settings. Apache NiFi installations that do not implement different levels of authorization for viewing and modifying component configuration are not subject to this vulnerability. Upgrading to Apache NiFi 2.10.0 is the recommended mitigation, requiring write access to submit configuration verification requests.</div>

### References
* https://lists.apache.org/thread/wrj3t4k2bwd2cztyp078f5kj3722qfzy


### Credits
* Kaixuan Li from Nanyang Technological University (finder)


## Missing Execute Code Required Permission on TinkerpopClientService ## { #CVE-2026-39816 }

CVE-2026-39816 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-39816) [\[CVE json\]](./CVE-2026-39816.cve.json) [\[OSV json\]](./CVE-2026-39816.osv.json)



_Last updated: 2026-05-08T13:38:11.640Z_

### Affected

* Apache NiFi from 2.0.0-M1 through 2.8.0


### Description

The optional extension component TinkerpopClientService is missing the Restricted annotation with the Execute Code Required Permission in Apache NiFi 2.0.0-M1 through 2.8.0. The TinkerpopClientService supports configuration of ByteCode Submission for the Script Submission Type, enabling Groovy Script execution in the service prior to submitting the query. The missing Restricted annotation allows users without the Execute Code Permission to configure the Service in installations that use fine-grained authorization and have the optional TinkerpopClientService installed. Apache NiFi installations that do not have the nifi-other-graph-services-nar installed are not subject to this vulnerability. Upgrading to Apache NiFi 2.9.0 is the recommended mitigation.

### References
* https://lists.apache.org/thread/gh9g7xwvv4l20gzff6q3367snf35ctcb


### Credits
* John Walker from ZeroPath (finder)


## Missing Authorization of Restricted Permissions for Component Updates ## { #CVE-2026-25903 }

CVE-2026-25903 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-25903) [\[CVE json\]](./CVE-2026-25903.cve.json) [\[OSV json\]](./CVE-2026-25903.osv.json)



_Last updated: 2026-02-17T09:54:42.673Z_

### Affected

* Apache NiFi from 1.1.0 before 2.8.0


### Description

Apache NiFi 1.1.0 through 2.7.2 are missing authorization when updating configuration properties on extension components that have specific Required Permissions based on the Restricted annotation. The Restricted annotation indicates additional privileges required to add the annotated component to the flow configuration, but framework authorization did not check restricted status when updating a component previously added. The missing authorization requires a more privileged user to add a restricted component to the flow configuration, but permits a less privileged user to make property configuration changes. Apache NiFi installations that do not implement different levels of authorization for Restricted components are not subject to this vulnerability because the framework enforces write permissions as the security boundary. Upgrading to Apache NiFi 2.8.0 is the recommended mitigation.

### References
* https://lists.apache.org/thread/jf6bkt9sk6xvshy8xyxv3vtlxd340345


### Credits
* David Handermann (finder)


## Deserialization of Untrusted Data in GetAsanaObject Processor ## { #CVE-2025-66524 }

CVE-2025-66524 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-66524) [\[CVE json\]](./CVE-2025-66524.cve.json) [\[OSV json\]](./CVE-2025-66524.osv.json)



_Last updated: 2025-12-19T09:24:44.035Z_

### Affected

* Apache NiFi from 1.20.0 through 2.6.0


### Description

Apache NiFi 1.20.0 through 2.6.0 include the GetAsanaObject Processor, which requires integration with a configurable Distribute Map Cache Client Service for storing and retrieving state information. The GetAsanaObject Processor used generic Java Object serialization and deserialization without filtering. Unfiltered Java object deserialization does not provide protection against crafted state information stored in the cache server configured for GetAsanaObject. Exploitation requires an Apache NiFi system running with the GetAsanaObject Processor, and direct access to the configured cache server. Upgrading to Apache NiFi 2.7.0 is the recommended mitigation, which replaces Java Object serialization with JSON serialization. Removing the GetAsanaObject Processor located in the nifi-asana-processors-nar bundle also prevents exploitation.

### References
* https://lists.apache.org/thread/k9h004ydjg7opdvxr0nfywtzf33z60d7


### Credits
* Jaeyeong Lee (finder)


## Potential Insertion of MongoDB Password in Provenance Record ## { #CVE-2025-27017 }

CVE-2025-27017 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27017) [\[CVE json\]](./CVE-2025-27017.cve.json) [\[OSV json\]](./CVE-2025-27017.osv.json)



_Last updated: 2025-03-12T16:19:42.969Z_

### Affected

* Apache NiFi from 1.13.0 through 2.2.0


### Description

<p><span style="background-color: rgb(252, 252, 252);">Apache NiFi 1.13.0 through 2.2.0 includes the username and password used to authenticate with MongoDB in the NiFi provenance events that MongoDB components generate during processing. An authorized user with read access to the provenance events of those processors may see the credentials information. Upgrading to Apache NiFi 2.3.0 is the recommended mitigation, which removes the credentials from provenance event records.</span></p>

### References
* https://lists.apache.org/thread/d4n5474jkhp82dvnht13pjtlfx7bhn5q


### Credits
* Robert Creese (finder)


## Missing Complete Authorization for Parameter and Service References ## { #CVE-2024-56512 }

CVE-2024-56512 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-56512) [\[CVE json\]](./CVE-2024-56512.cve.json) [\[OSV json\]](./CVE-2024-56512.osv.json)



_Last updated: 2024-12-29T11:14:49.689Z_

### Affected

* Apache NiFi from 1.10.0 through 2.0.0


### Description

Apache NiFi 1.10.0 through 2.0.0 are missing fine-grained authorization checking for Parameter Contexts, referenced Controller Services, and referenced Parameter Providers, when creating new Process Groups.<br><br>Creating a new Process Group can include binding to a Parameter Context, but in cases where the Process Group did not reference any Parameter values, the framework did not check user authorization for the bound Parameter Context. Missing authorization for a bound Parameter Context enabled clients to download non-sensitive Parameter values after creating the Process Group.<br><br>Creating a new Process Group can also include referencing existing Controller Services or Parameter Providers. The framework did not check user authorization for referenced Controller Services or Parameter Providers, enabling clients to create Process Groups and use these components that were otherwise unauthorized.<br><br>This vulnerability is limited in scope to authenticated users authorized to create Process Groups. The scope is further limited to deployments with component-based authorization policies. Upgrading to Apache NiFi 2.1.0 is the recommended mitigation, which includes authorization checking for Parameter and Controller Service references on Process Group creation.<br>

### References
* https://lists.apache.org/thread/cjc8fns5kjsho0s7vonlnojokyfx47wn


### Credits
* Matt Gilman (finder)


## Potential Insertion of Sensitive Parameter Values in Debug Log ## { #CVE-2024-52067 }

CVE-2024-52067 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-52067) [\[CVE json\]](./CVE-2024-52067.cve.json) [\[OSV json\]](./CVE-2024-52067.osv.json)



_Last updated: 2024-11-21T09:28:41.996Z_

### Affected

* Apache NiFi from 1.16.0 through 1.28.0
* Apache NiFi from 2.0.0-M1 through 2.0.0-M4


### Description

Apache NiFi 1.16.0 through 1.28.0 and 2.0.0-M1 through 2.0.0-M4 include optional debug logging of Parameter Context values during the flow synchronization process. An authorized administrator with access to change logging levels could enable debug logging for framework flow synchronization, causing the application to write Parameter names and values to the application log. Parameter Context values may contain sensitive information depending on application flow configuration. Deployments of Apache NiFi with the default Logback configuration do not log Parameter Context values. Upgrading to Apache NiFi 2.0.0 or 1.28.1 is the recommendation mitigation, eliminating Parameter value logging from the flow synchronization process regardless of the Logback configuration.<br>

### References
* https://lists.apache.org/thread/9rz5rwn2zc7pfjq7ppqldqlc067tlcwd


### Credits
* David Handermann (finder)


## Improper Neutralization of Input in Parameter Description ## { #CVE-2024-45477 }

CVE-2024-45477 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45477) [\[CVE json\]](./CVE-2024-45477.cve.json) [\[OSV json\]](./CVE-2024-45477.osv.json)



_Last updated: 2024-10-29T09:00:05.602Z_

### Affected

* Apache NiFi from 1.10.0 through 1.27.0
* Apache NiFi from 2.0.0-M1 through 2.0.0-M3


### Description

Apache NiFi 1.10.0 through 1.27.0 and 2.0.0-M1 through 2.0.0-M3 support a description field for Parameters in a Parameter Context configuration that is vulnerable to cross-site scripting. An authenticated user, authorized to configure a Parameter Context, can enter arbitrary JavaScript code, which the client browser will execute within the session context of the authenticated user. Upgrading to Apache NiFi 1.28.0 or 2.0.0-M4 is the recommended mitigation.

### References
* https://lists.apache.org/thread/shdv0tw9hggj7tx9pl7g93mgok2lwbj9


### Credits
* Muhammad Hazim Bin Nor Aizi (finder)


## Improper Neutralization of Input in Parameter Context Description ## { #CVE-2024-37389 }

CVE-2024-37389 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-37389) [\[CVE json\]](./CVE-2024-37389.cve.json) [\[OSV json\]](./CVE-2024-37389.osv.json)



_Last updated: 2024-07-08T07:28:58.478Z_

### Affected

* Apache NiFi from 1.10.0 through 1.26.0
* Apache NiFi from 2.0.0-M1 through 2.0.0-M3


### Description

Apache NiFi 1.10.0 through 1.26.0 and 2.0.0-M1 through 2.0.0-M3 support a description field in the Parameter Context configuration that is vulnerable to cross-site scripting. An authenticated user, authorized to configure a Parameter Context, can enter arbitrary JavaScript code, which the client browser will execute within the session context of the authenticated user. Upgrading to Apache NiFi 1.27.0 or 2.0.0-M4 is the recommended mitigation.

### References
* https://lists.apache.org/thread/yso9fr0wtff53nk046h1o83hdyb1lrxh


### Credits
* Akbar Kustirama (finder)


## Improper Neutralization of Input in Advanced User Interface for Jolt ## { #CVE-2023-49145 }

CVE-2023-49145 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49145) [\[CVE json\]](./CVE-2023-49145.cve.json) [\[OSV json\]](./CVE-2023-49145.osv.json)



_Last updated: 2023-11-27T22:29:16.184Z_

### Affected

* Apache NiFi from 0.7.0 through 1.23.2


### Description

Apache NiFi 0.7.0 through 1.23.2 include the JoltTransformJSON Processor, which provides an advanced configuration user interface that is vulnerable to DOM-based cross-site scripting. If an authenticated user, who is authorized to configure a JoltTransformJSON Processor, visits a crafted URL, then arbitrary
JavaScript code can be executed within the session context of the authenticated user. Upgrading to Apache NiFi 1.24.0 or 2.0.0-M1 is the recommended mitigation.

### References
* https://nifi.apache.org/security.html#CVE-2023-49145
* https://lists.apache.org/thread/j8rd0qsvgoj0khqck5f49jfbp0fm8r1o


### Credits
* Dr. Oliver Matula, DB Systel GmbH (finder)


## Incorrect Certificate Validation in InvokeHTTP for MiNiFi C++ ## { #CVE-2023-41180 }

CVE-2023-41180 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-41180) [\[CVE json\]](./CVE-2023-41180.cve.json) [\[OSV json\]](./CVE-2023-41180.osv.json)



_Last updated: 2023-09-03T15:52:48.640Z_

### Affected

* Apache NiFi MiNiFi C++ from 0.13.0 through 0.14.0


### Description

<div>Incorrect certificate validation in InvokeHTTP on Apache NiFi MiNiFi C++ versions 0.13 to 0.14 allows an intermediary to present a forged certificate during TLS handshake negotation. The Disable Peer Verification property of InvokeHTTP was effectively flipped,  disabling verification by default, when using HTTPS.<br></div><div><br></div><div>Mitigation: Set the Disable Peer Verification property of InvokeHTTP to true when using MiNiFi C++ versions 0.13.0 or 0.14.0. Upgrading to MiNiFi C++ 0.15.0 corrects the default behavior.<br></div>

### References
* https://lists.apache.org/thread/b51f8csysg1pvgs6xjjrq5hrjrvfot1y


### Credits
* Ferenc Gerlits (finder)


## Incomplete Validation of JDBC and JNDI Connection URLs ## { #CVE-2023-40037 }

CVE-2023-40037 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-40037) [\[CVE json\]](./CVE-2023-40037.cve.json) [\[OSV json\]](./CVE-2023-40037.osv.json)



_Last updated: 2023-08-18T21:54:49.856Z_

### Affected

* Apache NiFi from 1.21.0 through 1.23.0


### Description

Apache NiFi 1.21.0 through 1.23.0 support JDBC and JNDI JMS access in several Processors and Controller Services with connection URL validation that does not provide sufficient protection against crafted inputs. An authenticated and authorized user can bypass connection URL validation using custom input formatting. The resolution enhances connection URL validation and introduces validation for additional related properties. Upgrading to Apache NiFi 1.23.1 is the recommended mitigation.<br>

### References
* https://nifi.apache.org/security.html#CVE-2023-40037
* https://lists.apache.org/thread/bqbjlrs2p5ghh8sbk5nsxb8xpf9l687q


### Credits
* Matei "Mal" Badanoiu (finder)


## Potential Code Injection with Properties Referencing Remote Resources ## { #CVE-2023-36542 }

CVE-2023-36542 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-36542) [\[CVE json\]](./CVE-2023-36542.cve.json) [\[OSV json\]](./CVE-2023-36542.osv.json)



_Last updated: 2023-07-29T07:12:37.941Z_

### Affected

* Apache NiFi from 0.0.2 through 1.22.0


### Description

Apache NiFi 0.0.2 through 1.22.0 include Processors and Controller Services that support HTTP URL references for retrieving drivers, which allows an authenticated and authorized user to configure a location that enables custom code execution. The resolution introduces a new Required Permission for referencing remote resources, restricting configuration of these components to privileged users. The permission prevents unprivileged users from configuring Processors and Controller Services annotated with the new Reference Remote Resources restriction. Upgrading to Apache NiFi 1.23.0 is the recommended mitigation.<br>

### References
* https://nifi.apache.org/security.html#CVE-2023-36542
* https://lists.apache.org/thread/swnly3dzhhq9zo3rofc8djq77stkhbof


### Credits
* nbxiglk (finder)


## Potential Code Injection with Database Services using H2 ## { #CVE-2023-34468 }

CVE-2023-34468 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-34468) [\[CVE json\]](./CVE-2023-34468.cve.json) [\[OSV json\]](./CVE-2023-34468.osv.json)



_Last updated: 2023-06-12T15:09:17.702Z_

### Affected

* Apache NiFi from 0.0.2 through 1.21.0


### Description

<div>The DBCPConnectionPool and HikariCPConnectionPool Controller Services in Apache NiFi 0.0.2 through 1.21.0 allow an authenticated and authorized user to configure a Database URL with the H2 driver that enables custom code execution.</div><div>The resolution validates the Database URL and rejects H2 JDBC locations.</div><div>You are recommended to upgrade to version 1.22.0 or later which fixes this issue.<br></div>

### References
* https://nifi.apache.org/security.html#CVE-2023-34468
* https://lists.apache.org/thread/7b82l4f5blmpkfcynf3y6z4x1vqo59h8


### Credits
* Matei "Mal" Badanoiu (finder)


## Potential Deserialization of Untrusted Data with JNDI in JMS Components ## { #CVE-2023-34212 }

CVE-2023-34212 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-34212) [\[CVE json\]](./CVE-2023-34212.cve.json) [\[OSV json\]](./CVE-2023-34212.osv.json)



_Last updated: 2023-06-12T15:10:30.889Z_

### Affected

* Apache NiFi from 1.8.0 through 1.21.0


### Description

<div>The JndiJmsConnectionFactoryProvider Controller Service, along with the ConsumeJMS and PublishJMS Processors, in Apache NiFi 1.8.0 through 1.21.0 allow an authenticated and authorized user to configure URL and library properties that enable deserialization of untrusted data from a remote location.</div><div>The resolution validates the JNDI URL and restricts locations to a set of allowed schemes.</div><div>You are recommended to upgrade to version 1.22.0 or later which fixes this issue.<br></div>

### References
* https://nifi.apache.org/security.html#CVE-2023-34212
* https://lists.apache.org/thread/w5rm46fxmvxy216tglf0dv83wo6gnzr5


### Credits
* Veraxy00 of Qianxin TI Center (finder)
* Matei "Mal" Badanoiu (reporter)


## Improper Restriction of XML External Entity References in ExtractCCDAAttributes ## { #CVE-2023-22832 }

CVE-2023-22832 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-22832) [\[CVE json\]](./CVE-2023-22832.cve.json) [\[OSV json\]](./CVE-2023-22832.osv.json)



_Last updated: 2023-02-10T07:45:29.071Z_

### Affected

* Apache NiFi from 1.2.0 through 1.19.1


### Description

<div>The ExtractCCDAAttributes Processor in Apache NiFi 1.2.0 through 1.19.1 does not restrict XML External Entity references.</div><div>Flow configurations that include the ExtractCCDAAttributes Processor are vulnerable to malicious XML documents that contain Document Type Declarations with XML External Entity references.</div><div>The resolution disables Document Type Declarations and disallows XML External Entity resolution in the ExtractCCDAAttributes Processor.</div>

### References
* https://nifi.apache.org/security.html#CVE-2023-22832
* https://lists.apache.org/thread/b51qs6y7b7r58vovddkv6wc16g2xbl3w


### Credits
* Yi Cai of Chaitin Tech (finder)


## Improper Neutralization of Command Elements in Shell User Group Provider ## { #CVE-2022-33140 }

CVE-2022-33140 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-33140) [\[CVE json\]](./CVE-2022-33140.cve.json) [\[OSV json\]](./CVE-2022-33140.osv.json)



_Last updated: 2022-06-15T14:21:09.085Z_

### Affected

* Apache NiFi from up to 1.16.2 through 1.16.2
* Apache NiFi from 1.10.0 before 1.10.0*
* Apache NiFi Registry from up to 1.16.2 through 1.16.2
* Apache NiFi Registry from 0.6.0 before 0.6.0*


### Description

The optional ShellUserGroupProvider in Apache NiFi 1.10.0 to 1.16.2 and Apache NiFi Registry 0.6.0 to 1.16.2 does not neutralize arguments for group resolution commands, allowing injection of operating system commands on Linux and macOS platforms.

The ShellUserGroupProvider is not included in the default configuration. Command injection requires ShellUserGroupProvider to be one of the enabled User Group Providers in the Authorizers configuration. Command injection also requires an authenticated user with elevated privileges.  Apache NiFi requires an authenticated user with authorization to modify access policies in order to execute the command. Apache NiFi Registry requires an authenticated user with authorization to read user groups in order to execute the command.

The resolution removes command formatting based on user-provided arguments.

### References
* https://lists.apache.org/thread/bzs2pcdjsdrh5039oslmfr9mbs9qqdhr
* https://nifi.apache.org/security.html#CVE-2022-33140


## Improper Restriction of XML External Entity References in Multiple Components ## { #CVE-2022-29265 }

CVE-2022-29265 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-29265) [\[CVE json\]](./CVE-2022-29265.cve.json) [\[OSV json\]](./CVE-2022-29265.osv.json)



_Last updated: 2022-04-30T08:01:30.969Z_

### Affected

* Apache NiFi from 0.0.1 to 1.16.0 through 0.0.1 to 1.16.0


### Description

Multiple components in Apache NiFi 0.0.1 to 1.16.0 do not restrict XML External Entity references in the default configuration.

The Standard Content Viewer service attempts to resolve XML External Entity references when viewing formatted XML files.

The following Processors attempt to resolve XML External Entity references when configured with default property values:

- EvaluateXPath
- EvaluateXQuery
- ValidateXml

Apache NiFi flow configurations that include these Processors are vulnerable to malicious XML documents that contain Document Type Declarations with XML External Entity references.

The resolution disables Document Type Declarations in the default configuration for these Processors, and disallows XML External Entity resolution in standard services.

### References
* https://nifi.apache.org/security.html#CVE-2022-29265
* https://lists.apache.org/thread/47od9kr9n4cyv0mv81jh3pkyx815kyjl


### Credits
* David Handermann at exceptionfactory.com reported this issue.


## Insufficiently protected credentials ## { #CVE-2022-26850 }

CVE-2022-26850 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-26850) [\[CVE json\]](./CVE-2022-26850.cve.json) [\[OSV json\]](./CVE-2022-26850.osv.json)



_Last updated: 2022-04-06T20:48:13.265Z_

### Affected

* Apache NiFi at NiFi 1.14.0 to 1.15.3


### Description

When creating or updating credentials for single-user access, Apache NiFi wrote a copy of the Login Identity Providers configuration to the operating system temporary directory. On most platforms, the operating system temporary directory has global read permissions. NiFi immediately moved the temporary file to the final configuration directory, which significantly limited the window of opportunity for access.

NiFi 1.16.0 includes updates to replace the Login Identity Providers configuration without writing a file to the operating system temporary directory.


### References
* https://nifi.apache.org/security.html#CVE-2022-26850


### Credits
* This issue was discovered by Jonathan Leitschuh (https://twitter.com/jlleitschuh)


## Apache NiFi information disclosure by XXE ## { #CVE-2021-44145 }

CVE-2021-44145 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-44145) [\[CVE json\]](./CVE-2021-44145.cve.json) [\[OSV json\]](./CVE-2021-44145.osv.json)



_Last updated: 2021-12-17T08:46:07.497Z_

### Affected

* Apache NiFi from Apache NiFi through 1.15.0


### Description

In the TransformXML processor of Apache NiFi before 1.15.1 an authenticated user could configure an XSLT file which, if it included malicious external entity calls, may reveal sensitive information.

### References
* https://nifi.apache.org/security.html#1.15.1-vulnerabilities


### Credits
* This issue was discovered by DangKhai at Viettel Cyber Security.


## MiNiFi CPP arbitrary script execution is possible on the agent's host machine through the c2 protocol ## { #CVE-2021-33191 }

CVE-2021-33191 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-33191) [\[CVE json\]](./CVE-2021-33191.cve.json) [\[OSV json\]](./CVE-2021-33191.osv.json)



_Last updated: 2021-08-24T11:14:05.278Z_

### Affected

* Apache NiFi - MiNiFi C++ from 0.5.0 before Apache NiFi - MiNiFi C++*


### Description

From Apache NiFi MiNiFi C++ version 0.5.0 the c2 protocol implements an "agent-update" command which was designed to patch the application binary. 
This "patching" command defaults to calling a trusted binary, but might be modified to an arbitrary value through a "c2-update"
command. Said command is then executed using the same privileges as the application binary.  This was addressed in version 0.10.0

### References
* https://www.openwall.com/lists/oss-security/2021/08/24/1
