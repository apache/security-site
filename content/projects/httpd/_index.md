---
title: Apache HTTP Server security advisories
description: Security information for Apache HTTP Server
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache HTTP Server? You can read more about the projects' security policy on their [security page](https://httpd.apache.org/security_report.html), and email your report to the  [Apache HTTP Server Security Team](mailto:security@httpd.apache.org).

# Advisories

## mod_proxy prior to 2.4.55 allows a backend to trigger HTTP response splitting ## { #CVE-2022-37436 }

[CVE-2022-37436](./CVE-2022-37436.cve.json)

### Affected

* Apache HTTP Server versions  before 2.4.55


### Description

Prior to Apache HTTP Server 2.4.55, a malicious backend can cause the response headers to be truncated early, resulting in some headers being incorporated into the response body. If the later headers have any security purpose, they will not be interpreted by the client.

## mod_proxy_ajp Possible request smuggling ## { #CVE-2022-36760 }

[CVE-2022-36760](./CVE-2022-36760.cve.json)

### Affected

* Apache HTTP Server versions 2.4 including 2.4.54


### Description

Inconsistent Interpretation of HTTP Requests ('HTTP Request Smuggling') vulnerability in mod_proxy_ajp of Apache HTTP Server allows an attacker to smuggle requests to the AJP server it forwards requests to.  This issue affects Apache HTTP Server Apache HTTP Server 2.4 version 2.4.54 and prior versions.

## mod_dav out of  bounds read, or write of zero byte ## { #CVE-2006-20001 }

[CVE-2006-20001](./CVE-2006-20001.cve.json)

### Affected

* Apache HTTP Server versions 2.4 including 2.4.54


### Description

A carefully crafted If: request header can cause a memory read, or write of a single zero byte, in a pool (heap) memory location beyond the header value sent. This could cause the process to crash.<br><br>This issue affects Apache HTTP Server 2.4.54 and earlier.<br>

## HTTP request splitting with mod_rewrite and mod_proxy ## { #CVE-2023-25690 }

[CVE-2023-25690](./CVE-2023-25690.cve.json)

### Affected

* Apache HTTP Server versions 2.4.0 including 2.4.55


### Description

<div>Some mod_proxy configurations on Apache HTTP Server versions 2.4.0 through 2.4.55 allow a HTTP Request Smuggling attack.</div><div><br></div><div><div>Configurations are affected when mod_proxy is enabled along with some form of RewriteRule
 or ProxyPassMatch in which a non-specific pattern matches
 some portion of the user-supplied request-target (URL) data and is then
 re-inserted into the proxied request-target using variable 
substitution. For example, something like:</div><div><br></div><div>RewriteEngine on<br>RewriteRule "^/here/(.*)" "http://example.com:8080/elsewhere?$1"; [P]<br>ProxyPassReverse /here/ http://example.com:8080/</div><br>Request splitting/smuggling could result in bypass of access controls in the proxy server, proxying unintended URLs to existing origin servers, and cache poisoning. Users are recommended to update to at least version 2.4.56 of Apache HTTP Server.<br></div>

## mod_proxy_uwsgi HTTP response splitting ## { #CVE-2023-27522 }

[CVE-2023-27522](./CVE-2023-27522.cve.json)

### Affected

* Apache HTTP Server versions 2.4.30 including 2.4.55


### Description

<div>HTTP Response Smuggling vulnerability in Apache HTTP Server via mod_<code>proxy_uwsgi</code>. This issue affects Apache HTTP Server: from 2.4.30 through 2.4.55.</div><div>Special characters in the origin response header can truncate/split the response forwarded to the client.<br></div>