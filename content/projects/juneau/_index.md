---
title: Apache Juneau security advisories
description: Security information for Apache Juneau
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache Juneau? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Juneau).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Cross-site scripting via unescaped request variables in HTML-doc chrome ## { #CVE-2026-96677 }

CVE-2026-96677 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-96677) [\[CVE json\]](./CVE-2026-96677.cve.json) [\[OSV json\]](./CVE-2026-96677.osv.json)



_Last updated: 2026-11-05T11:54:34.525Z_

### Affected

* Apache Juneau before 9.2.1


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Juneau.<br><br>HTML document serialization does not HTML-encode variable substitutions in the page chrome (header, nav, aside, footer and similar fields). Applications whose chrome includes request-derived variables, such as request headers, form data or path values, reflect those values unencoded, allowing cross-site scripting. The default chrome does not use request variables, so only applications that add them are affected.<br><br>This issue affects Apache Juneau: through 9.2.0.<br><br>Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### References
* https://lists.apache.org/thread.html/j05q7vw08j48o96tdlzcsd4sozx1lyl6


### Credits
* 姬珏 (Diana Wang) (finder)


## Response header CRLF injection and open redirect when applications set headers or redirect targets from request data ## { #CVE-2026-73117 }

CVE-2026-73117 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73117) [\[CVE json\]](./CVE-2026-73117.cve.json) [\[OSV json\]](./CVE-2026-73117.osv.json)



_Last updated: 2026-11-05T11:54:07.631Z_

### Affected

* Apache Juneau before 9.2.1


### Description

Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Response Splitting') vulnerability in Apache Juneau.<br><br>The Apache Juneau REST server passed response header values and redirect targets to the servlet container unchecked. An application that sets a response header or redirect target from request data could let a remote client inject header lines (where the servlet container does not itself reject CR/LF) or redirect users to an arbitrary external site. The framework itself does not build headers or redirects from request data; exposure depends on application code.<br><br>This issue affects Apache Juneau: through 9.2.0.<br><br>Users are recommended to upgrade to version 9.2.1, which fixes the issue. Header values are now sanitized by default; applications that build redirect targets from request data must also switch from sendRedirect() to the new sendSafeRedirect().

### References
* https://lists.apache.org/thread.html/j05q7vw08j48o96tdlzcsd4sozx1lyl6


## REST client forwards credentials to a different origin when following HTTP redirects ## { #CVE-2026-73116 }

CVE-2026-73116 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73116) [\[CVE json\]](./CVE-2026-73116.cve.json) [\[OSV json\]](./CVE-2026-73116.osv.json)



_Last updated: 2026-11-05T11:53:48.491Z_

### Affected

* Apache Juneau before 9.2.1
* Apache Juneau before 9.2.1


### Description

Insufficiently Protected Credentials vulnerability in Apache Juneau.<br><br>The Apache Juneau RestClient followed HTTP redirects while keeping credential headers from the original request, so a server that redirected the client to a different host or port, or from HTTPS to HTTP, could receive headers such as Authorization, Cookie, Proxy-Authorization and X-API-Key.<br><br>This issue affects Apache Juneau: through 9.2.0.<br><br>Users are recommended to upgrade to version 9.2.1, which fixes the issue. The fix applies to HTTP clients created by the RestClient builder; applications that supply their own HttpClient must disable automatic redirects or strip credential headers on cross-origin redirects themselves.

### References
* https://lists.apache.org/thread.html/j05q7vw08j48o96tdlzcsd4sozx1lyl6


## Internal exception class and message disclosed via error response header and body regardless of secure defaults ## { #CVE-2026-73101 }

CVE-2026-73101 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73101) [\[CVE json\]](./CVE-2026-73101.cve.json) [\[OSV json\]](./CVE-2026-73101.osv.json)



_Last updated: 2026-11-05T11:52:22.021Z_

### Affected

* Apache Juneau before 9.2.1


### Description

Generation of Error Message Containing Sensitive Information vulnerability in Apache Juneau.<br><br>The REST server sends the internal exception class and message to clients in a "Thrown" response header on every error response, and can include internal exception messages in the error body, even when stack-trace rendering is disabled. This reveals implementation details to remote clients.<br><br>This issue affects Apache Juneau: through 9.2.0.<br><br>Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### References
* https://lists.apache.org/thread.html/j05q7vw08j48o96tdlzcsd4sozx1lyl6


## Sensitive request headers logged in cleartext by the default request logger on server errors ## { #CVE-2026-73100 }

CVE-2026-73100 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73100) [\[CVE json\]](./CVE-2026-73100.cve.json) [\[OSV json\]](./CVE-2026-73100.osv.json)



_Last updated: 2026-11-05T11:50:47.595Z_

### Affected

* Apache Juneau before 9.2.1
* Apache Juneau before 9.2.1


### Description

Insertion of Sensitive Information into Log File vulnerability in Apache Juneau.<br><br>The default REST server call logger records request headers for requests that end in a server error, without redacting them. Any client able to cause a server error gets headers such as Authorization, Cookie, Proxy-Authorization and X-API-Key written in cleartext to the application log, exposing them to anyone who can read the logs.<br><br>This issue affects Apache Juneau: through 9.2.0.<br><br>Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### References
* https://lists.apache.org/thread.html/j05q7vw08j48o96tdlzcsd4sozx1lyl6


## Cross-site request forgery via default-enabled content query-parameter body override ## { #CVE-2026-73099 }

CVE-2026-73099 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73099) [\[CVE json\]](./CVE-2026-73099.cve.json) [\[OSV json\]](./CVE-2026-73099.osv.json)



_Last updated: 2026-11-05T11:49:58.205Z_

### Affected

* Apache Juneau before 9.2.1


### Description

Cross-Site Request Forgery (CSRF) vulnerability in Apache Juneau.<br><br>The REST server accepts a "content" query parameter that replaces the request body, and this is enabled by default on every HTTP method, including GET. A cross-site link can therefore deliver an attacker-chosen request body to an endpoint without a CORS preflight, defeating protections that rely on the HTTP method or content type instead of an anti-CSRF token.<br><br>This issue affects Apache Juneau: through 9.2.0.<br><br>Users are recommended to upgrade to version 9.2.1, which fixes the issue. Applications that do not use the content parameter can also set disableContentParam to true.

### References
* https://lists.apache.org/thread.html/j05q7vw08j48o96tdlzcsd4sozx1lyl6


## Unsafe reflection allows attacker-controlled class initialization during parsing ## { #CVE-2026-73098 }

CVE-2026-73098 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73098) [\[CVE json\]](./CVE-2026-73098.cve.json) [\[OSV json\]](./CVE-2026-73098.osv.json)



_Last updated: 2026-11-05T11:49:14.698Z_

### Affected

* Apache Juneau before 9.2.1


### Description

Improper control of dynamically-loaded code vulnerability in Apache Juneau.<br><br>When Apache Juneau parses a value into a property of type java.lang.Class (including parameterized forms), the default class swap loaded the named class with initialization enabled, so input naming a class on the application classpath ran that class's static initializer. The impact depends on the classes present in the deployment.<br><br>This issue affects Apache Juneau: through 9.2.0.<br><br>Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### References
* https://lists.apache.org/thread.html/j05q7vw08j48o96tdlzcsd4sozx1lyl6


## Denial of service via unbounded memory allocation in parsers and REST request handling ## { #CVE-2026-73095 }

CVE-2026-73095 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73095) [\[CVE json\]](./CVE-2026-73095.cve.json) [\[OSV json\]](./CVE-2026-73095.osv.json)



_Last updated: 2026-11-05T11:48:21.694Z_

### Affected

* Apache Juneau before 9.2.1
* Apache Juneau before 9.2.1


### Description

Allocation of Resources Without Limits or Throttling vulnerability in Apache Juneau.<br><br>The MessagePack parser, which the REST server enables by default, sizes buffers from length values in the input. An unauthenticated client can send a few bytes that force a multi-gigabyte allocation and an OutOfMemoryError, causing denial of service. Related unbounded allocations in REST request handling (multipart uploads and request reader buffers) are fixed at the same time.<br><br>This issue affects Apache Juneau: through 9.2.0.<br><br>Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### References
* https://lists.apache.org/thread.html/j05q7vw08j48o96tdlzcsd4sozx1lyl6


### Credits
* n0mi1k (finder)


## Path traversal in DirectoryResource allows reading files outside the configured root directory ## { #CVE-2026-121489 }

CVE-2026-121489 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-121489) [\[CVE json\]](./CVE-2026-121489.cve.json) [\[OSV json\]](./CVE-2026-121489.osv.json)



_Last updated: 2026-11-05T11:55:20.166Z_

### Affected

* Apache Juneau before 9.2.1
* Apache Juneau before 9.2.1


### Description

Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Juneau.<br><br>The microservice DirectoryResource does not keep request paths inside its configured root directory. When an application enables the resource's view, upload or delete settings (all off by default), a client can read, write or delete files outside the root, anywhere the server process has access.<br><br>This issue affects Apache Juneau: through 9.2.0.<br><br>Users are recommended to upgrade to version 9.2.1, which fixes the issue.

### References
* https://lists.apache.org/thread.html/j05q7vw08j48o96tdlzcsd4sozx1lyl6


### Credits
* LTSHFWJT (finder)
