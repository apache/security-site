---
title: Apache HTTP Server security advisories
description: Security information for Apache HTTP Server
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache HTTP Server? You can read more about the projects' security policy on their [security page](https://httpd.apache.org/security_report.html), and email your report to the [Apache HTTP Server Security Team](mailto:security@httpd.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://httpd.apache.org/security_report.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## mod_userdir+suexec bypass via AllowOverride FileInfo ## { #CVE-2025-66200 }

CVE-2025-66200 [\[CVE json\]](./CVE-2025-66200.cve.json) [\[OSV json\]](./CVE-2025-66200.osv.json)



_Last updated: 2025-12-05T11:02:46.192Z_

### Affected

* Apache HTTP Server from 2.4.7 through 2.4.65


### Description

<p>mod_userdir+suexec bypass via AllowOverride FileInfo vulnerability in Apache HTTP Server. Users with access to use the RequestHeader directive in htaccess can cause some CGI scripts to run under an unexpected userid.</p><p>This issue affects Apache HTTP Server: from 2.4.7 through 2.4.65.</p><p>Users are recommended to upgrade to version 2.4.66, which fixes the issue.</p>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Mattias Åsander (Umeå University) (finder)


## CGI environment variable override ## { #CVE-2025-65082 }

CVE-2025-65082 [\[CVE json\]](./CVE-2025-65082.cve.json) [\[OSV json\]](./CVE-2025-65082.osv.json)



_Last updated: 2025-12-05T10:46:23.466Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.65


### Description

<p>Improper Neutralization of Escape, Meta, or Control Sequences vulnerability in Apache HTTP Server through environment variables set via the Apache configuration unexpectedly superseding variables calculated by the server for CGI programs.</p><p>This issue affects Apache HTTP Server from 2.4.0 through 2.4.65.</p><p>Users are recommended to upgrade to version 2.4.66 which fixes the issue.</p>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Mattias Åsander (Umeå University) (finder)


## NTLM Leakage on Windows through UNC SSRF ## { #CVE-2025-59775 }

CVE-2025-59775 [\[CVE json\]](./CVE-2025-59775.cve.json) [\[OSV json\]](./CVE-2025-59775.osv.json)



_Last updated: 2025-12-05T10:17:02.236Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.65


### Description

<p>

Server-Side Request Forgery (SSRF) vulnerability 

&nbsp;in Apache HTTP Server on Windows 

with <span style="background-color: rgb(247, 247, 247);">AllowEncodedSlashes</span> <span style="background-color: rgb(247, 247, 247);">On</span>&nbsp;and <span style="background-color: rgb(247, 247, 247);">MergeSlashes</span> <span style="background-color: rgb(247, 247, 247);">Off</span>&nbsp; allows to potentially leak NTLM 
hashes to a malicious server via SSRF and malicious requests or content</p><p>Users are recommended to upgrade to version 2.4.66, which fixes the issue.</p>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Orange Tsai (@orange_8361) from DEVCORE (finder)


## Server Side Includes adds query string to #exec cmd=... ## { #CVE-2025-58098 }

CVE-2025-58098 [\[CVE json\]](./CVE-2025-58098.cve.json) [\[OSV json\]](./CVE-2025-58098.osv.json)



_Last updated: 2025-12-05T13:40:37.496Z_

### Affected

* Apache HTTP Server before 2.4.66


### Description

<p>Apache HTTP Server 2.4.65 and earlier with Server Side Includes (SSI) enabled and mod_cgid (but not mod_cgi) passes the shell-escaped query string to #exec cmd="..." directives.</p><p>This issue affects Apache HTTP Server before 2.4.66.</p><p>Users are recommended to upgrade to version 2.4.66, which fixes the issue.</p>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Anthony Parfenov (United Rentals, Inc.) (finder)


## mod_md (ACME), unintended retry intervals ## { #CVE-2025-55753 }

CVE-2025-55753 [\[CVE json\]](./CVE-2025-55753.cve.json) [\[OSV json\]](./CVE-2025-55753.osv.json)



_Last updated: 2025-12-05T10:17:13.634Z_

### Affected

* Apache HTTP Server from 2.4.30 before 2.4.66


### Description

<p><span style="background-color: rgb(255, 255, 255);">An integer overflow in the case of failed ACME certificate renewal leads, after a number of failures (~30 days in default configurations), to the backoff timer becoming 0. Attempts to renew the certificate then are repeated without delays until it succeeds.</span></p><p>This issue affects Apache HTTP Server: from 2.4.30 before 2.4.66.<br></p><p>Users are recommended to upgrade to version 2.4.66, which fixes the issue.</p>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Aisle Research (finder)


## 'RewriteCond expr' always evaluates to true in 2.4.64 ## { #CVE-2025-54090 }

CVE-2025-54090 [\[CVE json\]](./CVE-2025-54090.cve.json) [\[OSV json\]](./CVE-2025-54090.osv.json)



_Last updated: 2025-07-23T13:19:23.112Z_

### Affected

* Apache HTTP Server at 2.4.64


### Description

<p>A bug in Apache HTTP Server 2.4.64 results in all "RewriteCond expr ..." tests evaluating as "true".<br><br></p><p>Users are recommended to upgrade to version 2.4.65, which fixes the issue.</p>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


## HTTP/2 DoS by Memory Increase ## { #CVE-2025-53020 }

CVE-2025-53020 [\[CVE json\]](./CVE-2025-53020.cve.json) [\[OSV json\]](./CVE-2025-53020.osv.json)



_Last updated: 2025-07-11T10:30:11.990Z_

### Affected

* Apache HTTP Server from 2.4.17 through 2.4.63


### Description

<p>Late Release of Memory after Effective Lifetime vulnerability in Apache HTTP Server.</p><p>This issue affects Apache HTTP Server: from 2.4.17 up to 2.4.63.</p><p>Users are recommended to upgrade to version 2.4.64, which fixes the issue.</p>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Gal Bar Nahum (finder)


## mod_ssl TLS upgrade attack ## { #CVE-2025-49812 }

CVE-2025-49812 [\[CVE json\]](./CVE-2025-49812.cve.json) [\[OSV json\]](./CVE-2025-49812.osv.json)



_Last updated: 2025-07-11T10:29:53.093Z_

### Affected

* Apache HTTP Server through 2.4.63


### Description

In some mod_ssl configurations on Apache HTTP Server versions through to 2.4.63, an HTTP desynchronisation attack allows a man-in-the-middle attacker to hijack an HTTP session via a TLS upgrade.<br><br>Only configurations using "SSLEngine optional" to enable TLS upgrades are affected. Users are recommended to upgrade to version 2.4.64, which removes support for TLS upgrade.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Robert Merget (Technology Innovation Institute) (finder)
* Nurullah Erinola (Ruhr University Bochum) (finder)
* Marcel Maehren (Ruhr University Bochum) (finder)
* Lukas Knittel (Ruhr University Bochum) (finder)
* Sven Hebrok (Paderborn University) (finder)
* Marcus Brinkmann (Ruhr University Bochum) (finder)
* Juraj Somorovsky (Paderborn University) (finder)
* Jörg Schwenk (Ruhr University Bochum) (finder)


## mod_proxy_http2 denial of service ## { #CVE-2025-49630 }

CVE-2025-49630 [\[CVE json\]](./CVE-2025-49630.cve.json) [\[OSV json\]](./CVE-2025-49630.osv.json)



_Last updated: 2025-08-13T15:38:59.198Z_

### Affected

* Apache HTTP Server from 2.4.26 through 2.4.63


### Description

In certain proxy configurations, a denial of service attack against&nbsp;Apache HTTP Server versions 2.4.26 through to 2.4.63 can be triggered by untrusted clients causing an assertion in mod_proxy_http2.<br><br>Configurations affected are a reverse proxy is configured for an HTTP/2 backend, with ProxyPreserveHost set to "on".<br>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Anthony CORSIEZ (finder)


## mod_ssl access control bypass with session resumption ## { #CVE-2025-23048 }

CVE-2025-23048 [\[CVE json\]](./CVE-2025-23048.cve.json) [\[OSV json\]](./CVE-2025-23048.osv.json)



_Last updated: 2025-07-11T10:30:23.007Z_

### Affected

* Apache HTTP Server from 2.4.35 through 2.4.63


### Description

In some mod_ssl configurations on Apache HTTP Server 2.4.35 through to 2.4.63, an access control bypass by trusted clients is possible using TLS 1.3 session resumption.<br><br>Configurations are affected when mod_ssl is configured for multiple virtual hosts, with each restricted to a different set of trusted client certificates (for example with a different SSLCACertificateFile/Path setting). In such a case, a client trusted to access one virtual host may be able to access another virtual host, if SSLStrictSNIVHostCheck is not enabled in either virtual host.<br><br>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Sven Hebrok, Felix Cramer, Tim Storm, Maximilian Radoy, and Juraj Somorovsky at Paderborn University (finder)


## mod_ssl error log variable escaping ## { #CVE-2024-47252 }

CVE-2024-47252 [\[CVE json\]](./CVE-2024-47252.cve.json) [\[OSV json\]](./CVE-2024-47252.osv.json)



_Last updated: 2025-07-11T10:29:12.847Z_

### Affected

* Apache HTTP Server from 2.4 through 2.4.63


### Description

Insufficient escaping of user-supplied data in mod_ssl in Apache HTTP Server 2.4.63 and earlier allows an untrusted SSL/TLS client to insert escape characters into log files in some configurations.<br><br>In a logging configuration where CustomLog is used with "%{varname}x" or "%{varname}c" to log variables provided by mod_ssl such as SSL_TLS_SNI, no escaping is performed by either mod_log_config or mod_ssl and unsanitized data provided by the client may appear in log files.<br><br>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* John Runyon (finder)


## SSRF on Windows due to UNC paths ## { #CVE-2024-43394 }

CVE-2024-43394 [\[CVE json\]](./CVE-2024-43394.cve.json) [\[OSV json\]](./CVE-2024-43394.osv.json)



_Last updated: 2025-07-11T10:29:24.674Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.63


### Description

<p></p><p>Server-Side Request Forgery (SSRF)&nbsp;in Apache HTTP Server on Windows allows to potentially leak NTLM hashes to a malicious server via&nbsp;<br>mod_rewrite or apache expressions that pass unvalidated request input.</p><p>This issue affects Apache HTTP Server: from 2.4.0 through 2.4.63.</p>Note: <span style="background-color: rgb(255, 255, 255);">&nbsp;The Apache HTTP Server Project will be setting a higher bar for accepting vulnerability reports regarding SSRF via UNC paths. <br><br>The server offers limited protection against administrators directing the server to open UNC paths.<br></span>Windows servers should limit the hosts they will connect over via SMB based on the nature of NTLM authentication.<br>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Kainan Zhang (@4xpl0r3r) from Fortinet (finder)


## SSRF with mod_headers setting Content-Type header ## { #CVE-2024-43204 }

CVE-2024-43204 [\[CVE json\]](./CVE-2024-43204.cve.json) [\[OSV json\]](./CVE-2024-43204.osv.json)



_Last updated: 2025-07-11T10:33:09.127Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.63


### Description

SSRF in Apache HTTP Server with mod_proxy loaded allows an attacker to send outbound proxy requests to a URL controlled by the attacker.&nbsp; Requires an unlikely configuration where mod_headers is configured to modify the Content-Type request or response header with a value provided in the HTTP request.<br><br>Users are recommended to upgrade to version 2.4.64 which fixes this issue.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* xiaojunjie@安恒信息杭州市滨江区技能大师工作室 (finder)


## HTTP response splitting ## { #CVE-2024-42516 }

CVE-2024-42516 [\[CVE json\]](./CVE-2024-42516.cve.json) [\[OSV json\]](./CVE-2024-42516.osv.json)



_Last updated: 2025-07-11T10:29:33.054Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.63


### Description

HTTP response splitting in the core of Apache HTTP Server allows an attacker who can manipulate the Content-Type response headers of applications hosted or proxied by the server can split the HTTP response.<br><br>This vulnerability was described as CVE-2023-38709 but the patch included in Apache HTTP Server 2.4.59 did not address the issue.<br><br>Users are recommended to upgrade to version 2.4.64, which fixes this issue.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


## SSRF with mod_rewrite in server/vhost context on Windows ## { #CVE-2024-40898 }

CVE-2024-40898 [\[CVE json\]](./CVE-2024-40898.cve.json) [\[OSV json\]](./CVE-2024-40898.osv.json)



_Last updated: 2024-07-18T09:55:11.215Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.61


### Description

SSRF in Apache HTTP Server on Windows with mod_rewrite in server/vhost context, allows to potentially leak NTLM hashes to a malicious server via SSRF and <span style="background-color: rgb(255, 255, 255);">malicious requests.<br></span><br>Users are recommended to upgrade to version 2.4.62 which fixes this issue.&nbsp;

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Smi1e (DBAPPSecurity Ltd.) (finder)
* xiaojunjie (DBAPPSecurity Ltd.) (finder)


## source code disclosure with handlers configured via AddType ## { #CVE-2024-40725 }

CVE-2024-40725 [\[CVE json\]](./CVE-2024-40725.cve.json) [\[OSV json\]](./CVE-2024-40725.osv.json)



_Last updated: 2024-07-18T09:32:42.028Z_

### Affected

* Apache HTTP Server from 2.4.60 through 2.4.61


### Description

<p>A partial fix for&nbsp; CVE-2024-39884 in the core of Apache HTTP Server 2.4.61 ignores some use of the legacy content-type based configuration of handlers. "AddType" and similar configuration, under some circumstances where files are requested indirectly, result in source code disclosure of local content. For example, PHP scripts may be served instead of interpreted.</p><p></p><p>Users are recommended to upgrade to version 2.4.62, which fixes this issue.</p><br><br>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


## source code disclosure with handlers configured via AddType ## { #CVE-2024-39884 }

CVE-2024-39884 [\[CVE json\]](./CVE-2024-39884.cve.json) [\[OSV json\]](./CVE-2024-39884.osv.json)



_Last updated: 2024-07-04T08:41:17.573Z_

### Affected

* Apache HTTP Server at 2.4.60


### Description

A regression in the core of Apache HTTP Server 2.4.60 ignores some use of the legacy content-type based configuration of handlers.&nbsp; &nbsp;"AddType" and similar configuration, under some circumstances where files are requested indirectly, result in source code disclosure of local content. For example, PHP scripts may be served instead of interpreted.<br><br>Users are recommended to upgrade to version 2.4.61, which fixes this issue.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


## mod_rewrite proxy handler substitution ## { #CVE-2024-39573 }

CVE-2024-39573 [\[CVE json\]](./CVE-2024-39573.cve.json) [\[OSV json\]](./CVE-2024-39573.osv.json)



_Last updated: 2024-07-01T18:16:42.254Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.59


### Description

Potential SSRF in mod_rewrite in Apache HTTP Server 2.4.59 and earlier allows an attacker to cause unsafe RewriteRules to unexpectedly setup URL's to be handled by mod_proxy.<br>Users are recommended to upgrade to version 2.4.60, which fixes this issue.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Orange Tsai (@orange_8361) from DEVCORE (finder)


## Crash resulting in Denial of Service in mod_proxy via a malicious request ## { #CVE-2024-38477 }

CVE-2024-38477 [\[CVE json\]](./CVE-2024-38477.cve.json) [\[OSV json\]](./CVE-2024-38477.osv.json)



_Last updated: 2024-07-01T18:16:10.377Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.59


### Description

null pointer dereference in mod_proxy in Apache HTTP Server 2.4.59 and earlier allows an attacker to crash the server via a malicious request.<br>Users are recommended to upgrade to version 2.4.60, which fixes this issue.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Orange Tsai (@orange_8361) from DEVCORE (finder)


## Apache HTTP Server may use exploitable/malicious backend application output to run local handlers via internal redirect ## { #CVE-2024-38476 }

CVE-2024-38476 [\[CVE json\]](./CVE-2024-38476.cve.json) [\[OSV json\]](./CVE-2024-38476.osv.json)



_Last updated: 2024-07-01T19:20:41.405Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.59


### Description

Vulnerability in core of Apache HTTP Server 2.4.59 and earlier are vulnerably to information disclosure, SSRF or local script execution via&nbsp;<span style="background-color: rgb(255, 255, 255);">backend applications whose response headers are malicious or exploitable.</span><br><br>Note: Some legacy uses of the 'AddType' directive to connect a&nbsp;request to a handler must be ported to 'AddHandler' after this fix.<br><br>Users are recommended to upgrade to version 2.4.60, which fixes this issue.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Orange Tsai (@orange_8361) from DEVCORE (finder)


## Apache HTTP Server weakness in mod_rewrite when first segment of substitution matches filesystem path. ## { #CVE-2024-38475 }

CVE-2024-38475 [\[CVE json\]](./CVE-2024-38475.cve.json) [\[OSV json\]](./CVE-2024-38475.osv.json)



_Last updated: 2024-07-01T18:15:10.846Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.59


### Description

Improper escaping of output in mod_rewrite in Apache HTTP Server 2.4.59 and earlier allows an attacker to map URLs to filesystem locations that are&nbsp;permitted to be served by the server but are not intentionally/directly reachable by any URL, resulting in code execution or source code disclosure. <br><br>Substitutions in&nbsp;server context that use a backreferences or variables as the first segment of the substitution are affected.&nbsp; Some unsafe RewiteRules will be broken by this change and the rewrite flag "UnsafePrefixStat" can be used to opt back in once ensuring the substitution is appropriately constrained.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Orange Tsai (@orange_8361) from DEVCORE (finder)


## Apache HTTP Server weakness with encoded question marks in backreferences ## { #CVE-2024-38474 }

CVE-2024-38474 [\[CVE json\]](./CVE-2024-38474.cve.json) [\[OSV json\]](./CVE-2024-38474.osv.json)



_Last updated: 2024-07-01T18:14:45.297Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.59


### Description

Substitution encoding issue in mod_rewrite in Apache HTTP Server 2.4.59 and earlier allows attacker to execute scripts in<br>directories permitted by the configuration but not directly reachable by any&nbsp;URL or source disclosure of scripts meant to only to be executed as CGI.<br><br>Users are recommended to upgrade to version 2.4.60, which fixes this issue.<br><br>Some RewriteRules that capture and substitute unsafely will now fail unless rewrite flag "UnsafeAllow3F" is specified.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Orange Tsai (@orange_8361) from DEVCORE (finder)


## Apache HTTP Server proxy encoding problem ## { #CVE-2024-38473 }

CVE-2024-38473 [\[CVE json\]](./CVE-2024-38473.cve.json) [\[OSV json\]](./CVE-2024-38473.osv.json)



_Last updated: 2024-07-03T12:05:25.367Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.59


### Description

Encoding problem in mod_proxy in Apache HTTP Server 2.4.59 and earlier allows request URLs with incorrect encoding to be sent to backend services, potentially bypassing authentication via crafted requests. This affects configurations where mechanisms other than ProxyPass/ProxyPassMatch or RewriteRule with the 'P' flag are used to configure a request to be proxied, such as SetHandler or inadvertent proxying via&nbsp;CVE-2024-39573.&nbsp; Note that these alternate mechanisms may be used within .htaccess.<br><br>Users are recommended to upgrade to version 2.4.60, which fixes this issue.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Orange Tsai (@orange_8361) from DEVCORE (finder)


## Apache HTTP Server on WIndows UNC SSRF ## { #CVE-2024-38472 }

CVE-2024-38472 [\[CVE json\]](./CVE-2024-38472.cve.json) [\[OSV json\]](./CVE-2024-38472.osv.json)



_Last updated: 2024-11-18T08:50:42.606Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.59


### Description

SSRF in Apache HTTP Server on Windows allows to potentially leak NTML hashes to a malicious server via SSRF and&nbsp;<span style="background-color: rgb(255, 255, 255);">malicious requests or content </span><br>Users are recommended to upgrade to version 2.4.60 which fixes this issue.&nbsp; Note: Existing configurations that access UNC paths will have to configure new directive "UNCList" to allow access during request processing.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Orange Tsai (@orange_8361) from DEVCORE (finder)


## DoS by Null pointer in websocket over HTTP/2 ## { #CVE-2024-36387 }

CVE-2024-36387 [\[CVE json\]](./CVE-2024-36387.cve.json) [\[OSV json\]](./CVE-2024-36387.osv.json)



_Last updated: 2024-07-02T10:05:08.772Z_

### Affected

* Apache HTTP Server from 2.4.55 through 2.4.59


### Description

Serving WebSocket protocol upgrades over a HTTP/2 connection could result in a Null Pointer dereference, leading to a crash of the server process, degrading performance.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Marc Stern (<marc.stern@approach-cyber.com>) (finder)


## HTTP/2 DoS by memory exhaustion on endless continuation frames ## { #CVE-2024-27316 }

CVE-2024-27316 [\[CVE json\]](./CVE-2024-27316.cve.json) [\[OSV json\]](./CVE-2024-27316.osv.json)



_Last updated: 2024-07-22T08:42:12.197Z_

### Affected

* Apache HTTP Server from 2.4.17 through 2.4.58


### Description

HTTP/2 incoming headers exceeding the limit are temporarily buffered in nghttp2 in order to generate an informative HTTP 413 response. If a client does not stop sending headers, this leads to memory exhaustion.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Bartek Nowotarski (https://nowotarski.info/)  (finder)


## HTTP Response Splitting in multiple modules ## { #CVE-2024-24795 }

CVE-2024-24795 [\[CVE json\]](./CVE-2024-24795.cve.json) [\[OSV json\]](./CVE-2024-24795.osv.json)



_Last updated: 2024-10-03T12:15:08.331Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.58


### Description

HTTP Response splitting in multiple modules in Apache HTTP Server allows an attacker that can inject malicious response headers into backend applications to cause an HTTP desynchronization attack.<br><br>Users are recommended to upgrade to version 2.4.59, which fixes this issue.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Keran Mu, Tsinghua University and Zhongguancun Laboratory. (finder)
* Jianjun Chen, Tsinghua University and Zhongguancun Laboratory. (finder)


## HTTP/2 stream memory not reclaimed right away on RST ## { #CVE-2023-45802 }

CVE-2023-45802 [\[CVE json\]](./CVE-2023-45802.cve.json) [\[OSV json\]](./CVE-2023-45802.osv.json)



_Last updated: 2024-10-14T09:01:43.211Z_

### Affected

* Apache HTTP Server from 2.4.17 through 2.4.57


### Description

When a HTTP/2 stream was reset (RST frame) by a client, there was a time window were the request's memory resources were not reclaimed immediately. Instead, de-allocation was deferred to connection close. A client could send new requests and resets, keeping the connection busy and open and causing the memory footprint to keep on growing. On connection close, all resources were reclaimed, but the process might run out of memory before that.<br><br>This was found by the reporter during testing of&nbsp;CVE-2023-44487 (HTTP/2 Rapid Reset Exploit) with their own test client. During "normal" HTTP/2 use, the probability to hit this bug is very low. The kept memory would not become noticeable before the connection closes or times out.<br><br>Users are recommended to upgrade to version 2.4.58, which fixes the issue.<br>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Will Dormann of Vul Labs (finder)
* David Warren of Vul Labs (finder)


## DoS in HTTP/2 with initial windows size 0 ## { #CVE-2023-43622 }

CVE-2023-43622 [\[CVE json\]](./CVE-2023-43622.cve.json) [\[OSV json\]](./CVE-2023-43622.osv.json)



_Last updated: 2023-10-23T06:50:49.104Z_

### Affected

* Apache HTTP Server from 2.4.55 through 2.4.57


### Description

An attacker, opening a HTTP/2 connection with an initial window size of 0, was able to block handling of that connection indefinitely in Apache HTTP Server. This could be used to exhaust worker resources in the server, similar to the well known "slow loris" attack pattern.<br><p>This has been fixed in version 2.4.58, so that such connection are terminated properly after the configured connection timeout.</p><p>This issue affects Apache HTTP Server: from 2.4.55 through 2.4.57.</p><p>Users are recommended to upgrade to version 2.4.58, which fixes the issue.</p>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Prof. Sven Dietrich (City University of New York) (finder)
* Isa Jafarov (City University of New York) (finder)
* Prof. Heejo Lee (Korea University) (finder)
* Choongin Lee (Korea University) (finder)


## HTTP response splitting ## { #CVE-2023-38709 }

CVE-2023-38709 [\[CVE json\]](./CVE-2023-38709.cve.json) [\[OSV json\]](./CVE-2023-38709.osv.json)



_Last updated: 2025-01-17T11:15:18.205Z_

### Affected

* Apache HTTP Server through 2.4.58


### Description

Faulty input validation in the core of Apache allows malicious or exploitable backend/content generators to split HTTP responses.<br><br>This issue affects Apache HTTP Server: through 2.4.58.<br>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Orange Tsai (@orange_8361) from DEVCORE (finder)


## mod_macro buffer over-read ## { #CVE-2023-31122 }

CVE-2023-31122 [\[CVE json\]](./CVE-2023-31122.cve.json) [\[OSV json\]](./CVE-2023-31122.osv.json)



_Last updated: 2023-10-23T06:51:56.755Z_

### Affected

* Apache HTTP Server through 2.4.57


### Description

Out-of-bounds Read vulnerability in mod_macro of Apache HTTP Server.<p>This issue affects Apache HTTP Server: through 2.4.57.</p>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* David Shoon (github/davidshoon) (finder)


## mod_proxy_uwsgi HTTP response splitting ## { #CVE-2023-27522 }

CVE-2023-27522 [\[CVE json\]](./CVE-2023-27522.cve.json) [\[OSV json\]](./CVE-2023-27522.osv.json)



_Last updated: 2023-03-07T15:09:26.534Z_

### Affected

* Apache HTTP Server from 2.4.30 through 2.4.55


### Description

<div>HTTP Response Smuggling vulnerability in Apache HTTP Server via mod_<code>proxy_uwsgi</code>. This issue affects Apache HTTP Server: from 2.4.30 through 2.4.55.</div><div>Special characters in the origin response header can truncate/split the response forwarded to the client.<br></div>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Dimas Fariski Setyawan Putra (nyxsorcerer) (finder)


## HTTP request splitting with mod_rewrite and mod_proxy ## { #CVE-2023-25690 }

CVE-2023-25690 [\[CVE json\]](./CVE-2023-25690.cve.json) [\[OSV json\]](./CVE-2023-25690.osv.json)



_Last updated: 2023-03-07T15:08:45.400Z_

### Affected

* Apache HTTP Server from 2.4.0 through 2.4.55


### Description

<div>Some mod_proxy configurations on Apache HTTP Server versions 2.4.0 through 2.4.55 allow a HTTP Request Smuggling attack.</div><div><br></div><div><div>Configurations are affected when mod_proxy is enabled along with some form of RewriteRule
 or ProxyPassMatch in which a non-specific pattern matches
 some portion of the user-supplied request-target (URL) data and is then
 re-inserted into the proxied request-target using variable 
substitution. For example, something like:</div><div><br></div><div>RewriteEngine on<br>RewriteRule "^/here/(.*)" "http://example.com:8080/elsewhere?$1"; [P]<br>ProxyPassReverse /here/ http://example.com:8080/</div><br>Request splitting/smuggling could result in bypass of access controls in the proxy server, proxying unintended URLs to existing origin servers, and cache poisoning. Users are recommended to update to at least version 2.4.56 of Apache HTTP Server.<br></div>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Lars Krapf of Adobe (finder)


## mod_proxy prior to 2.4.55 allows a backend to trigger HTTP response splitting ## { #CVE-2022-37436 }

CVE-2022-37436 [\[CVE json\]](./CVE-2022-37436.cve.json) [\[OSV json\]](./CVE-2022-37436.osv.json)



_Last updated: 2023-01-17T19:13:19.999Z_

### Affected

* Apache HTTP Server before 2.4.55


### Description

Prior to Apache HTTP Server 2.4.55, a malicious backend can cause the response headers to be truncated early, resulting in some headers being incorporated into the response body. If the later headers have any security purpose, they will not be interpreted by the client.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Dimas Fariski Setyawan Putra (@nyxsorcerer) (finder)


## mod_proxy_ajp Possible request smuggling ## { #CVE-2022-36760 }

CVE-2022-36760 [\[CVE json\]](./CVE-2022-36760.cve.json) [\[OSV json\]](./CVE-2022-36760.osv.json)



_Last updated: 2023-01-17T19:12:02.488Z_

### Affected

* Apache HTTP Server from 2.4 through 2.4.54


### Description

Inconsistent Interpretation of HTTP Requests ('HTTP Request Smuggling') vulnerability in mod_proxy_ajp of Apache HTTP Server allows an attacker to smuggle requests to the AJP server it forwards requests to.  This issue affects Apache HTTP Server Apache HTTP Server 2.4 version 2.4.54 and prior versions.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* ZeddYu_Lu from Qi'anxin Research Institute of Legendsec at Qi'anxin Group (finder)


## mod_proxy X-Forwarded-For dropped by hop-by-hop mechanism ## { #CVE-2022-31813 }

CVE-2022-31813 [\[CVE json\]](./CVE-2022-31813.cve.json) [\[OSV json\]](./CVE-2022-31813.osv.json)



_Last updated: 2022-06-08T09:46:07.679Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.53


### Description

Apache HTTP Server 2.4.53 and earlier may not send the X-Forwarded-* headers to the origin server based on client side Connection header hop-by-hop mechanism.
This may be used to bypass IP based authentication on the origin server/application.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Gaetan Ferry (Synacktiv) for reporting this issue


## Information Disclosure in mod_lua with websockets ## { #CVE-2022-30556 }

CVE-2022-30556 [\[CVE json\]](./CVE-2022-30556.cve.json) [\[OSV json\]](./CVE-2022-30556.osv.json)



_Last updated: 2022-06-08T09:45:55.863Z_

### Affected

* Apache HTTP Server from unspecified through 2.4.53


### Description

Apache HTTP Server 2.4.53 and earlier may return lengths to applications calling r:wsread() that point past the end of the storage allocated for the buffer.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Ronald Crane (Zippenhop LLC) for reporting this issue


## mod_sed denial of service ## { #CVE-2022-30522 }

CVE-2022-30522 [\[CVE json\]](./CVE-2022-30522.cve.json) [\[OSV json\]](./CVE-2022-30522.osv.json)



_Last updated: 2022-06-08T09:45:43.331Z_

### Affected

* Apache HTTP Server at 2.4.53


### Description

If Apache HTTP Server 2.4.53 is configured to do transformations with mod_sed in contexts where the input to mod_sed may be very large, mod_sed may make excessively large memory allocations and trigger an abort.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* This issue was found by Brian Moussalli from the JFrog Security Research team


## Denial of service in mod_lua r:parsebody ## { #CVE-2022-29404 }

CVE-2022-29404 [\[CVE json\]](./CVE-2022-29404.cve.json) [\[OSV json\]](./CVE-2022-29404.osv.json)



_Last updated: 2022-06-08T09:45:33.924Z_

### Affected

* Apache HTTP Server from unspecified through 2.4.53


### Description

In Apache HTTP Server 2.4.53 and earlier, a malicious request to a lua script that calls r:parsebody(0) may cause a denial of service due to no default limit on possible input size.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Ronald Crane (Zippenhop LLC) for reporting this issue


## Read beyond bounds in ap_strcmp_match() ## { #CVE-2022-28615 }

CVE-2022-28615 [\[CVE json\]](./CVE-2022-28615.cve.json) [\[OSV json\]](./CVE-2022-28615.osv.json)



_Last updated: 2022-06-08T09:45:23.244Z_

### Affected

* Apache HTTP Server from Apache HTTP Server through 2.4.53


### Description

Apache HTTP Server 2.4.53 and earlier may crash or disclose information due to a read beyond bounds in ap_strcmp_match() when provided with an extremely large input buffer.  While no code distributed with the server can be coerced into such a call, third-party modules or lua scripts that use ap_strcmp_match() may hypothetically be affected.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Ronald Crane (Zippenhop LLC) for reporting this issue


## read beyond bounds via ap_rwrite()  ## { #CVE-2022-28614 }

CVE-2022-28614 [\[CVE json\]](./CVE-2022-28614.cve.json) [\[OSV json\]](./CVE-2022-28614.osv.json)



_Last updated: 2022-06-10T17:43:34.235Z_

### Affected

* Apache HTTP Server from unspecified through 2.4.53


### Description

The ap_rwrite() function in Apache HTTP Server 2.4.53 and earlier may read unintended memory if an attacker can cause the server to reflect very large input using ap_rwrite() or ap_rputs(), such as with mod_luas r:puts() function.

Modules compiled and distributed separately from Apache HTTP Server that use the "ap_rputs" function and may pass it a very large (INT_MAX or larger) string must be compiled against current headers to resolve the issue.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Ronald Crane (Zippenhop LLC) for reporting this issue


## read beyond bounds in mod_isapi ## { #CVE-2022-28330 }

CVE-2022-28330 [\[CVE json\]](./CVE-2022-28330.cve.json) [\[OSV json\]](./CVE-2022-28330.osv.json)



_Last updated: 2022-06-08T09:44:43.156Z_

### Affected

* Apache HTTP Server from Apache HTTP Server through 2.4.53


### Description

Apache HTTP Server 2.4.53 and earlier on Windows may read beyond bounds when configured to process requests with the mod_isapi module. 

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Ronald Crane (Zippenhop LLC) for reporting this issue


## mod_proxy_ajp: Possible request smuggling ## { #CVE-2022-26377 }

CVE-2022-26377 [\[CVE json\]](./CVE-2022-26377.cve.json) [\[OSV json\]](./CVE-2022-26377.osv.json)



_Last updated: 2022-06-08T09:44:32.521Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.53


### Description

Inconsistent Interpretation of HTTP Requests ('HTTP Request Smuggling') vulnerability in mod_proxy_ajp of Apache HTTP Server allows an attacker to smuggle requests to the AJP server it forwards requests to.  This issue affects Apache HTTP Server Apache HTTP Server 2.4 version 2.4.53 and prior versions.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Ricter Z @ 360 Noah Lab


## mod_sed: Read/write beyond bounds ## { #CVE-2022-23943 }

CVE-2022-23943 [\[CVE json\]](./CVE-2022-23943.cve.json) [\[OSV json\]](./CVE-2022-23943.osv.json)



_Last updated: 2022-03-14T10:07:36.342Z_

### Affected

* Apache HTTP Server from 2.4 through 2.4.52


### Description

Out-of-bounds Write vulnerability in mod_sed of Apache HTTP Server allows an attacker to overwrite heap memory with possibly attacker provided data.

This issue affects Apache HTTP Server 2.4 version 2.4.52 and prior versions.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Ronald Crane (Zippenhop LLC)


## libapreq2 multipart form parse memory corruption ## { #CVE-2022-22728 }

CVE-2022-22728 [\[CVE json\]](./CVE-2022-22728.cve.json) [\[OSV json\]](./CVE-2022-22728.osv.json)



_Last updated: 2022-08-25T14:13:38.823Z_

### Affected

* libapreq2 from unspecified through 2.16


### Description

A flaw in Apache libapreq2 versions 2.16 and earlier could cause a buffer overflow while processing multipart form uploads.  A remote attacker could send a request causing a process crash which could lead to a denial of service attack.

### References
* https://lists.apache.org/thread/2fsjoor96d47vtkpf76x4yo06nccvy1y


## core: Possible buffer overflow with very large or unlimited LimitXMLRequestBody ## { #CVE-2022-22721 }

CVE-2022-22721 [\[CVE json\]](./CVE-2022-22721.cve.json) [\[OSV json\]](./CVE-2022-22721.osv.json)



_Last updated: 2022-03-14T10:08:56.550Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.52


### Description

If LimitXMLRequestBody is set to allow request bodies larger than 350MB (defaults to 1M) on 32 bit systems an integer overflow happens which later causes out of bounds writes.

This issue affects Apache HTTP Server 2.4.52 and earlier.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Anonymous working with Trend Micro Zero Day Initiative


## HTTP request smuggling vulnerability in Apache HTTP Server 2.4.52 and earlier ## { #CVE-2022-22720 }

CVE-2022-22720 [\[CVE json\]](./CVE-2022-22720.cve.json) [\[OSV json\]](./CVE-2022-22720.osv.json)



_Last updated: 2022-03-14T10:09:48.647Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.52


### Description

Apache HTTP Server 2.4.52 and earlier fails to close inbound connection when errors are encountered discarding the request body, exposing the server to HTTP Request Smuggling

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* James Kettle <james.kettle portswigger.net>


## mod_lua Use of uninitialized value of in r:parsebody ## { #CVE-2022-22719 }

CVE-2022-22719 [\[CVE json\]](./CVE-2022-22719.cve.json) [\[OSV json\]](./CVE-2022-22719.osv.json)



_Last updated: 2022-03-14T10:10:30.113Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.52


### Description

A carefully crafted request body can cause a read to a random memory area which could cause the process to crash.

This issue affects Apache HTTP Server 2.4.52 and earlier.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Chamal De Silva


## Possible buffer overflow when parsing multipart content in mod_lua of Apache HTTP Server 2.4.51 and earlier ## { #CVE-2021-44790 }

CVE-2021-44790 [\[CVE json\]](./CVE-2021-44790.cve.json) [\[OSV json\]](./CVE-2021-44790.osv.json)



_Last updated: 2021-12-20T11:07:20.265Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.51


### Description

A carefully crafted request body can cause a buffer overflow in the mod_lua multipart parser (r:parsebody() called from Lua scripts).
The Apache httpd team is not aware of an exploit for the vulnerabilty though it might be possible to craft one.

This issue affects Apache HTTP Server 2.4.51 and earlier.

### References
* http://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Chamal
* Anonymous working with Trend Micro Zero Day Initiative


## Possible NULL dereference or SSRF in forward proxy configurations in Apache HTTP Server 2.4.51 and earlier ## { #CVE-2021-44224 }

CVE-2021-44224 [\[CVE json\]](./CVE-2021-44224.cve.json) [\[OSV json\]](./CVE-2021-44224.osv.json)



_Last updated: 2021-12-20T11:06:17.917Z_

### Affected

* Apache HTTP Server from 2.4.7 before Apache HTTP Server 2.4*


### Description

A crafted URI sent to httpd configured as a forward proxy (ProxyRequests on) can cause a crash (NULL pointer dereference) or, for configurations mixing forward and reverse proxy declarations, can allow for requests to be directed to a declared Unix Domain Socket endpoint (Server Side Request Forgery).

This issue affects Apache HTTP Server 2.4.7 up to 2.4.51 (included).

### References
* http://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* 漂亮鼠
* TengMA(@Te3t123)


## Path Traversal and Remote Code Execution in Apache HTTP Server 2.4.49 and 2.4.50 (incomplete fix of CVE-2021-41773) ## { #CVE-2021-42013 }

CVE-2021-42013 [\[CVE json\]](./CVE-2021-42013.cve.json) [\[OSV json\]](./CVE-2021-42013.osv.json)



_Last updated: 2021-10-11T17:31:43.275Z_

### Affected

* Apache HTTP Server at 2.4.49
* Apache HTTP Server at 2.4.50


### Description

It was found that the fix for CVE-2021-41773 in Apache HTTP Server 2.4.50 was insufficient.  An attacker could use a path traversal attack to map URLs to files outside the directories configured by Alias-like directives.  

If files outside of these directories are not protected by the usual default configuration "require all denied", these requests can succeed. If CGI scripts are also enabled for these aliased pathes, this could allow for remote code execution.

This issue only affects Apache 2.4.49 and Apache 2.4.50 and not earlier versions.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Reported by Juan Escobar from Dreamlab Technologies
* Reported by Fernando Muñoz from NULL Life CTF Team
* Reported by Shungo Kumasaka
* Reported by Nattapon Jongcharoen


## Path traversal and file disclosure vulnerability in Apache HTTP Server 2.4.49 ## { #CVE-2021-41773 }

CVE-2021-41773 [\[CVE json\]](./CVE-2021-41773.cve.json)

_Last updated: 2021-10-11T14:15:40.313Z_

### Affected

* Apache HTTP Server at Apache HTTP Server 2.4 2.4.49


### Description

A flaw was found in a change made to path normalization in Apache HTTP Server 2.4.49. An attacker could use a path traversal attack to map URLs to files outside the directories configured by Alias-like directives.

If files outside of these directories are not protected by the usual default configuration "require all denied", these requests can succeed. If CGI scripts are also enabled for these aliased pathes, this could allow for remote code execution.

This issue is known to be exploited in the wild.

This issue only affects Apache 2.4.49 and not earlier versions.

### Credits
* This issue was reported by Ash Daulton along with the cPanel Security Team


## null pointer dereference in h2 fuzzing ## { #CVE-2021-41524 }

CVE-2021-41524 [\[CVE json\]](./CVE-2021-41524.cve.json) [\[OSV json\]](./CVE-2021-41524.osv.json)



_Last updated: 2021-10-05T11:31:17.600Z_

### Affected

* Apache HTTP Server at 2.4.49


### Description

While fuzzing the 2.4.49 httpd, a new null pointer dereference was detected during HTTP/2 request processing,
allowing an external source to DoS the server. This requires a specially crafted request. 

The vulnerability was recently introduced in version 2.4.49. No exploit is known to the project.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Apache httpd team would like to thank LI ZHI XIN from NSFocus Security Team for reporting this issue.


## mod_proxy SSRF ## { #CVE-2021-40438 }

CVE-2021-40438 [\[CVE json\]](./CVE-2021-40438.cve.json) [\[OSV json\]](./CVE-2021-40438.osv.json)



_Last updated: 2021-09-16T14:37:10.201Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.48


### Description

A crafted request uri-path can cause mod_proxy to forward the request to an origin server choosen by the remote user.

This issue affects Apache HTTP Server 2.4.48 and earlier.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The issue was discovered by the Apache HTTP security team while analysing CVE-2021-36160


## ap_escape_quotes buffer overflow ## { #CVE-2021-39275 }

CVE-2021-39275 [\[CVE json\]](./CVE-2021-39275.cve.json) [\[OSV json\]](./CVE-2021-39275.osv.json)



_Last updated: 2021-09-16T14:35:11.663Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.48


### Description

ap_escape_quotes() may write beyond the end of a buffer when given malicious input.  
No included modules pass untrusted data to these functions, but third-party / external modules may.

This issue affects Apache HTTP Server 2.4.48 and earlier.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* ClusterFuzz


## mod_proxy_uwsgi out of bound read ## { #CVE-2021-36160 }

CVE-2021-36160 [\[CVE json\]](./CVE-2021-36160.cve.json) [\[OSV json\]](./CVE-2021-36160.osv.json)



_Last updated: 2021-09-16T14:33:49.077Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.48


### Description

A carefully crafted request uri-path can cause mod_proxy_uwsgi to read above the allocated memory and crash (DoS).

This issue affects Apache HTTP Server versions 2.4.30 to 2.4.48 (inclusive).

### References
* http://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* LI ZHI XIN from NSFocus Security Team


## NULL pointer dereference in httpd core ## { #CVE-2021-34798 }

CVE-2021-34798 [\[CVE json\]](./CVE-2021-34798.cve.json) [\[OSV json\]](./CVE-2021-34798.osv.json)



_Last updated: 2021-09-16T14:31:21.975Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.48


### Description

Malformed requests may cause the server to dereference a NULL pointer.


This issue affects Apache HTTP Server 2.4.48 and earlier.

### References
* http://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The issue was discovered by the Apache HTTP security team


## Request splitting via HTTP/2 method injection and mod_proxy ## { #CVE-2021-33193 }

CVE-2021-33193 [\[CVE json\]](./CVE-2021-33193.cve.json) [\[OSV json\]](./CVE-2021-33193.osv.json)



_Last updated: 2021-09-16T12:49:38.115Z_

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.48


### Description

A crafted method sent through HTTP/2 will bypass validation and be forwarded by mod_proxy, which can lead to request splitting or cache poisoning.

This issue affects Apache HTTP Server 2.4.17 to 2.4.48.

### References
* https://portswigger.net/research/http2
* https://github.com/apache/httpd/commit/ecebcc035ccd8d0e2984fe41420d9e944f456b3c.patch


### Credits
* Reported by James Kettle of PortSwigger


## NULL pointer dereference on specially crafted HTTP/2 request ## { #CVE-2021-31618 }

CVE-2021-31618 [\[CVE json\]](./CVE-2021-31618.cve.json) [\[OSV json\]](./CVE-2021-31618.osv.json)



_Last updated: 2021-06-15T08:48:10.111Z_

### Affected

* Apache HTTP Server at 2.4.47


### Description

Apache HTTP Server protocol handler for the HTTP/2 protocol checks received request headers against the size limitations as configured for the server and used for the HTTP/1 protocol as well. On violation of these restrictions and HTTP response is sent to the client with a status code indicating why the request was rejected.

This rejection response was not fully initialised in the HTTP/2 protocol handler if the offending header was the very first one received or appeared in a a footer. This led to a NULL pointer dereference on initialised memory, crashing reliably the child process. Since such a triggering HTTP/2 request is easy to craft and submit, this can be exploited to DoS the server.

This issue affected  mod_http2 1.15.17 and Apache HTTP Server version 2.4.47 only. Apache HTTP Server 2.4.47 was never released.

### References
* http://httpd.apache.org/security/vulnerabilities_24.html
* https://seclists.org/oss-sec/2021/q2/206


### Credits
* Apache HTTP server would like to thank  LI ZHI XIN from NSFocus for reporting this.


## Unexpected URL matching with 'MergeSlashes OFF' ## { #CVE-2021-30641 }

CVE-2021-30641 [\[CVE json\]](./CVE-2021-30641.cve.json) [\[OSV json\]](./CVE-2021-30641.osv.json)



_Last updated: 2021-06-10T07:02:16.829Z_

### Affected

* Apache HTTP Server at 2.4.46
* Apache HTTP Server at 2.4.43
* Apache HTTP Server at 2.4.41
* Apache HTTP Server at 2.4.39


### Description

Apache HTTP Server versions 2.4.39 to 2.4.46 Unexpected matching behavior with 'MergeSlashes OFF'

### References
* http://httpd.apache.org/security/vulnerabilities_24.html
* https://lists.apache.org/thread.html/re026d3da9d7824bd93b9f871c0fdda978d960c7e62d8c43cba8d0bf3%40%3Ccvs.httpd.apache.org%3E


### Credits
* Discovered by Christoph Anton Mitterer


## Apache HTTP Server mod_session response handling heap overflow ## { #CVE-2021-26691 }

CVE-2021-26691 [\[CVE json\]](./CVE-2021-26691.cve.json) [\[OSV json\]](./CVE-2021-26691.osv.json)



_Last updated: 2021-06-10T07:01:56.009Z_

### Affected

* Apache HTTP Server at 2.4.46
* Apache HTTP Server at 2.4.43
* Apache HTTP Server at 2.4.41
* Apache HTTP Server at 2.4.39
* Apache HTTP Server at 2.4.38
* Apache HTTP Server at 2.4.37
* Apache HTTP Server at 2.4.35
* Apache HTTP Server at 2.4.34
* Apache HTTP Server at 2.4.33
* Apache HTTP Server at 2.4.29
* Apache HTTP Server at 2.4.28
* Apache HTTP Server at 2.4.27
* Apache HTTP Server at 2.4.26
* Apache HTTP Server at 2.4.25
* Apache HTTP Server at 2.4.23
* Apache HTTP Server at 2.4.20
* Apache HTTP Server at 2.4.18
* Apache HTTP Server at 2.4.17
* Apache HTTP Server at 2.4.16
* Apache HTTP Server at 2.4.12
* Apache HTTP Server at 2.4.10
* Apache HTTP Server at 2.4.9
* Apache HTTP Server at 2.4.7
* Apache HTTP Server at 2.4.6
* Apache HTTP Server at 2.4.4
* Apache HTTP Server at 2.4.3
* Apache HTTP Server at 2.4.2
* Apache HTTP Server at 2.4.1
* Apache HTTP Server at 2.4.0


### Description

In Apache HTTP Server versions 2.4.0 to 2.4.46 a specially crafted SessionHeader sent by an origin server could cause a heap overflow

### References
* http://httpd.apache.org/security/vulnerabilities_24.html
* https://lists.apache.org/thread.html/re026d3da9d7824bd93b9f871c0fdda978d960c7e62d8c43cba8d0bf3%40%3Ccvs.httpd.apache.org%3E


### Credits
* Discovered internally Christophe Jaillet


## mod_session NULL pointer dereference ## { #CVE-2021-26690 }

CVE-2021-26690 [\[CVE json\]](./CVE-2021-26690.cve.json) [\[OSV json\]](./CVE-2021-26690.osv.json)



_Last updated: 2021-06-10T07:01:40.445Z_

### Affected

* Apache HTTP Server at 2.4.46
* Apache HTTP Server at 2.4.43
* Apache HTTP Server at 2.4.41
* Apache HTTP Server at 2.4.39
* Apache HTTP Server at 2.4.38
* Apache HTTP Server at 2.4.37
* Apache HTTP Server at 2.4.35
* Apache HTTP Server at 2.4.34
* Apache HTTP Server at 2.4.33
* Apache HTTP Server at 2.4.29
* Apache HTTP Server at 2.4.28
* Apache HTTP Server at 2.4.27
* Apache HTTP Server at 2.4.26
* Apache HTTP Server at 2.4.25
* Apache HTTP Server at 2.4.23
* Apache HTTP Server at 2.4.20
* Apache HTTP Server at 2.4.18
* Apache HTTP Server at 2.4.17
* Apache HTTP Server at 2.4.16
* Apache HTTP Server at 2.4.12
* Apache HTTP Server at 2.4.10
* Apache HTTP Server at 2.4.9
* Apache HTTP Server at 2.4.7
* Apache HTTP Server at 2.4.6
* Apache HTTP Server at 2.4.4
* Apache HTTP Server at 2.4.3
* Apache HTTP Server at 2.4.2
* Apache HTTP Server at 2.4.1
* Apache HTTP Server at 2.4.0


### Description

Apache HTTP Server versions 2.4.0 to 2.4.46 A specially crafted Cookie header handled by mod_session can cause a NULL pointer dereference and crash, leading to a possible Denial Of Service

### References
* http://httpd.apache.org/security/vulnerabilities_24.html
* https://lists.apache.org/thread.html/re026d3da9d7824bd93b9f871c0fdda978d960c7e62d8c43cba8d0bf3%40%3Ccvs.httpd.apache.org%3E


### Credits
* This issue was discovered and reported by GHSL team member @antonio-morales (Antonio Morales)


## mod_auth_digest possible stack overflow by one nul byte ## { #CVE-2020-35452 }

CVE-2020-35452 [\[CVE json\]](./CVE-2020-35452.cve.json) [\[OSV json\]](./CVE-2020-35452.osv.json)



_Last updated: 2021-06-10T07:01:23.279Z_

### Affected

* Apache HTTP Server at 2.4.46
* Apache HTTP Server at 2.4.43
* Apache HTTP Server at 2.4.41
* Apache HTTP Server at 2.4.39
* Apache HTTP Server at 2.4.38
* Apache HTTP Server at 2.4.37
* Apache HTTP Server at 2.4.35
* Apache HTTP Server at 2.4.34
* Apache HTTP Server at 2.4.33
* Apache HTTP Server at 2.4.29
* Apache HTTP Server at 2.4.28
* Apache HTTP Server at 2.4.27
* Apache HTTP Server at 2.4.26
* Apache HTTP Server at 2.4.25
* Apache HTTP Server at 2.4.23
* Apache HTTP Server at 2.4.20
* Apache HTTP Server at 2.4.18
* Apache HTTP Server at 2.4.17
* Apache HTTP Server at 2.4.16
* Apache HTTP Server at 2.4.12
* Apache HTTP Server at 2.4.10
* Apache HTTP Server at 2.4.9
* Apache HTTP Server at 2.4.7
* Apache HTTP Server at 2.4.6
* Apache HTTP Server at 2.4.4
* Apache HTTP Server at 2.4.3
* Apache HTTP Server at 2.4.2
* Apache HTTP Server at 2.4.1
* Apache HTTP Server at 2.4.0


### Description

Apache HTTP Server versions 2.4.0 to 2.4.46 A specially crafted Digest nonce can cause a stack overflow in mod_auth_digest. There is no report of this overflow being exploitable, nor the Apache HTTP Server team could create one, though some particular compiler and/or compilation option might make it possible, with limited consequences anyway due to the size (a single byte) and the value (zero byte) of the overflow

### References
* http://httpd.apache.org/security/vulnerabilities_24.html
* https://lists.apache.org/thread.html/re026d3da9d7824bd93b9f871c0fdda978d960c7e62d8c43cba8d0bf3%40%3Ccvs.httpd.apache.org%3E


### Credits
* This issue was discovered and reported by GHSL team member @antonio-morales (Antonio Morales)


## mod_proxy_http NULL pointer dereference ## { #CVE-2020-13950 }

CVE-2020-13950 [\[CVE json\]](./CVE-2020-13950.cve.json) [\[OSV json\]](./CVE-2020-13950.osv.json)



_Last updated: 2021-06-10T07:00:03.831Z_

### Affected

* Apache HTTP Server at 2.4.46
* Apache HTTP Server at 2.4.43
* Apache HTTP Server at 2.4.41


### Description

Apache HTTP Server versions 2.4.41 to 2.4.46 mod_proxy_http can be made to crash (NULL pointer dereference) with specially crafted requests using both Content-Length and Transfer-Encoding headers, leading to a Denial of Service

### References
* http://httpd.apache.org/security/vulnerabilities_24.html
* https://lists.apache.org/thread.html/re026d3da9d7824bd93b9f871c0fdda978d960c7e62d8c43cba8d0bf3%40%3Ccvs.httpd.apache.org%3E


### Credits
* Reported by Marc Stern (<marc.stern approach.be>)


## Improper Handling of Insufficient Privileges ## { #CVE-2020-13938 }

CVE-2020-13938 [\[CVE json\]](./CVE-2020-13938.cve.json) [\[OSV json\]](./CVE-2020-13938.osv.json)



_Last updated: 2021-06-10T06:59:41.634Z_

### Affected

* Apache HTTP Server at 2.4.46
* Apache HTTP Server at 2.4.43
* Apache HTTP Server at 2.4.41
* Apache HTTP Server at 2.4.39
* Apache HTTP Server at 2.4.38
* Apache HTTP Server at 2.4.37
* Apache HTTP Server at 2.4.35
* Apache HTTP Server at 2.4.34
* Apache HTTP Server at 2.4.33
* Apache HTTP Server at 2.4.29
* Apache HTTP Server at 2.4.28
* Apache HTTP Server at 2.4.27
* Apache HTTP Server at 2.4.26
* Apache HTTP Server at 2.4.25
* Apache HTTP Server at 2.4.23
* Apache HTTP Server at 2.4.20
* Apache HTTP Server at 2.4.18
* Apache HTTP Server at 2.4.17
* Apache HTTP Server at 2.4.16
* Apache HTTP Server at 2.4.12
* Apache HTTP Server at 2.4.10
* Apache HTTP Server at 2.4.9
* Apache HTTP Server at 2.4.7
* Apache HTTP Server at 2.4.6
* Apache HTTP Server at 2.4.4
* Apache HTTP Server at 2.4.3
* Apache HTTP Server at 2.4.2
* Apache HTTP Server at 2.4.1
* Apache HTTP Server at 2.4.0


### Description

Apache HTTP Server versions 2.4.0 to 2.4.46 Unprivileged local users can stop httpd on Windows

### References
* http://httpd.apache.org/security/vulnerabilities_24.html
* https://lists.apache.org/thread.html/re026d3da9d7824bd93b9f871c0fdda978d960c7e62d8c43cba8d0bf3%40%3Ccvs.httpd.apache.org%3E


### Credits
* Discovered by Ivan Zhakov


## mod_proxy_wstunnel tunneling of non Upgraded connections ## { #CVE-2019-17567 }

CVE-2019-17567 [\[CVE json\]](./CVE-2019-17567.cve.json) [\[OSV json\]](./CVE-2019-17567.osv.json)



_Last updated: 2021-06-16T13:33:49.334Z_

### Affected

* Apache HTTP Server at 2.4.46
* Apache HTTP Server at 2.4.43
* Apache HTTP Server at 2.4.41
* Apache HTTP Server at 2.4.39
* Apache HTTP Server at 2.4.38
* Apache HTTP Server at 2.4.37
* Apache HTTP Server at 2.4.35
* Apache HTTP Server at 2.4.34
* Apache HTTP Server at 2.4.33
* Apache HTTP Server at 2.4.29
* Apache HTTP Server at 2.4.28
* Apache HTTP Server at 2.4.27
* Apache HTTP Server at 2.4.26
* Apache HTTP Server at 2.4.25
* Apache HTTP Server at 2.4.23
* Apache HTTP Server at 2.4.20
* Apache HTTP Server at 2.4.18
* Apache HTTP Server at 2.4.17
* Apache HTTP Server at 2.4.16
* Apache HTTP Server at 2.4.12
* Apache HTTP Server at 2.4.10
* Apache HTTP Server at 2.4.9
* Apache HTTP Server at 2.4.7
* Apache HTTP Server at 2.4.6


### Description

Apache HTTP Server versions 2.4.6 to 2.4.46 mod_proxy_wstunnel configured on an URL that is not necessarily Upgraded by the origin server was tunneling the whole connection regardless, thus allowing for subsequent requests on the same connection to pass through with no HTTP validation, authentication or authorization possibly configured.

### References
* http://httpd.apache.org/security/vulnerabilities_24.html
* https://lists.apache.org/thread.html/re026d3da9d7824bd93b9f871c0fdda978d960c7e62d8c43cba8d0bf3%40%3Ccvs.httpd.apache.org%3E


### Credits
* Reported by Mikhail Egorov (<0ang3el gmail.com>)


## mod_dav out of  bounds read, or write of zero byte ## { #CVE-2006-20001 }

CVE-2006-20001 [\[CVE json\]](./CVE-2006-20001.cve.json) [\[OSV json\]](./CVE-2006-20001.osv.json)



_Last updated: 2023-01-17T19:07:17.134Z_

### Affected

* Apache HTTP Server from 2.4 through 2.4.54


### Description

A carefully crafted If: request header can cause a memory read, or write of a single zero byte, in a pool (heap) memory location beyond the header value sent. This could cause the process to crash.<br><br>This issue affects Apache HTTP Server 2.4.54 and earlier.<br>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html
