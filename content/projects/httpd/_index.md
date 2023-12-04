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

## mod_proxy_http NULL pointer dereference ## { #CVE-2020-13950 }

CVE-2020-13950 [\[CVE json\]](./CVE-2020-13950.cve.json)

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


## mod_auth_digest possible stack overflow by one nul byte ## { #CVE-2020-35452 }

CVE-2020-35452 [\[CVE json\]](./CVE-2020-35452.cve.json)

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


## mod_proxy_wstunnel tunneling of non Upgraded connections ## { #CVE-2019-17567 }

CVE-2019-17567 [\[CVE json\]](./CVE-2019-17567.cve.json)

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


## Improper Handling of Insufficient Privileges ## { #CVE-2020-13938 }

CVE-2020-13938 [\[CVE json\]](./CVE-2020-13938.cve.json)

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


## mod_session NULL pointer dereference ## { #CVE-2021-26690 }

CVE-2021-26690 [\[CVE json\]](./CVE-2021-26690.cve.json)

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


## Apache HTTP Server mod_session response handling heap overflow ## { #CVE-2021-26691 }

CVE-2021-26691 [\[CVE json\]](./CVE-2021-26691.cve.json)

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


## Unexpected URL matching with 'MergeSlashes OFF' ## { #CVE-2021-30641 }

CVE-2021-30641 [\[CVE json\]](./CVE-2021-30641.cve.json)

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


## NULL pointer dereference on specially crafted HTTP/2 request ## { #CVE-2021-31618 }

CVE-2021-31618 [\[CVE json\]](./CVE-2021-31618.cve.json)

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


## Request splitting via HTTP/2 method injection and mod_proxy ## { #CVE-2021-33193 }

CVE-2021-33193 [\[CVE json\]](./CVE-2021-33193.cve.json)

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


## NULL pointer dereference in httpd core ## { #CVE-2021-34798 }

CVE-2021-34798 [\[CVE json\]](./CVE-2021-34798.cve.json)

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.48


### Description

Malformed requests may cause the server to dereference a NULL pointer.


This issue affects Apache HTTP Server 2.4.48 and earlier.

### References
* http://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The issue was discovered by the Apache HTTP security team


## mod_proxy_uwsgi out of bound read ## { #CVE-2021-36160 }

CVE-2021-36160 [\[CVE json\]](./CVE-2021-36160.cve.json)

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.48


### Description

A carefully crafted request uri-path can cause mod_proxy_uwsgi to read above the allocated memory and crash (DoS).

This issue affects Apache HTTP Server versions 2.4.30 to 2.4.48 (inclusive).

### References
* http://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* LI ZHI XIN from NSFocus Security Team


## ap_escape_quotes buffer overflow ## { #CVE-2021-39275 }

CVE-2021-39275 [\[CVE json\]](./CVE-2021-39275.cve.json)

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


## mod_proxy SSRF ## { #CVE-2021-40438 }

CVE-2021-40438 [\[CVE json\]](./CVE-2021-40438.cve.json)

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.48


### Description

A crafted request uri-path can cause mod_proxy to forward the request to an origin server choosen by the remote user.

This issue affects Apache HTTP Server 2.4.48 and earlier.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The issue was discovered by the Apache HTTP security team while analysing CVE-2021-36160


## null pointer dereference in h2 fuzzing ## { #CVE-2021-41524 }

CVE-2021-41524 [\[CVE json\]](./CVE-2021-41524.cve.json)

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


## Path traversal and file disclosure vulnerability in Apache HTTP Server 2.4.49 ## { #CVE-2021-41773 }

CVE-2021-41773 [\[CVE json\]](./CVE-2021-41773.cve.json)

### Affected

* Apache HTTP Server at Apache HTTP Server 2.4 2.4.49


### Description

A flaw was found in a change made to path normalization in Apache HTTP Server 2.4.49. An attacker could use a path traversal attack to map URLs to files outside the directories configured by Alias-like directives.

If files outside of these directories are not protected by the usual default configuration "require all denied", these requests can succeed. If CGI scripts are also enabled for these aliased pathes, this could allow for remote code execution.

This issue is known to be exploited in the wild.

This issue only affects Apache 2.4.49 and not earlier versions.

### Credits
* This issue was reported by Ash Daulton along with the cPanel Security Team


## Path Traversal and Remote Code Execution in Apache HTTP Server 2.4.49 and 2.4.50 (incomplete fix of CVE-2021-41773) ## { #CVE-2021-42013 }

CVE-2021-42013 [\[CVE json\]](./CVE-2021-42013.cve.json)

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


## Possible NULL dereference or SSRF in forward proxy configurations in Apache HTTP Server 2.4.51 and earlier ## { #CVE-2021-44224 }

CVE-2021-44224 [\[CVE json\]](./CVE-2021-44224.cve.json)

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


## Possible buffer overflow when parsing multipart content in mod_lua of Apache HTTP Server 2.4.51 and earlier ## { #CVE-2021-44790 }

CVE-2021-44790 [\[CVE json\]](./CVE-2021-44790.cve.json)

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


## mod_lua Use of uninitialized value of in r:parsebody ## { #CVE-2022-22719 }

CVE-2022-22719 [\[CVE json\]](./CVE-2022-22719.cve.json)

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.52


### Description

A carefully crafted request body can cause a read to a random memory area which could cause the process to crash.

This issue affects Apache HTTP Server 2.4.52 and earlier.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Chamal De Silva


## HTTP request smuggling vulnerability in Apache HTTP Server 2.4.52 and earlier ## { #CVE-2022-22720 }

CVE-2022-22720 [\[CVE json\]](./CVE-2022-22720.cve.json)

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.52


### Description

Apache HTTP Server 2.4.52 and earlier fails to close inbound connection when errors are encountered discarding the request body, exposing the server to HTTP Request Smuggling

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* James Kettle <james.kettle portswigger.net>


## core: Possible buffer overflow with very large or unlimited LimitXMLRequestBody ## { #CVE-2022-22721 }

CVE-2022-22721 [\[CVE json\]](./CVE-2022-22721.cve.json)

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.52


### Description

If LimitXMLRequestBody is set to allow request bodies larger than 350MB (defaults to 1M) on 32 bit systems an integer overflow happens which later causes out of bounds writes.

This issue affects Apache HTTP Server 2.4.52 and earlier.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Anonymous working with Trend Micro Zero Day Initiative


## libapreq2 multipart form parse memory corruption ## { #CVE-2022-22728 }

CVE-2022-22728 [\[CVE json\]](./CVE-2022-22728.cve.json)

### Affected

* libapreq2 from unspecified through 2.16


### Description

A flaw in Apache libapreq2 versions 2.16 and earlier could cause a buffer overflow while processing multipart form uploads.  A remote attacker could send a request causing a process crash which could lead to a denial of service attack.

### References
* https://lists.apache.org/thread/2fsjoor96d47vtkpf76x4yo06nccvy1y


## mod_sed: Read/write beyond bounds ## { #CVE-2022-23943 }

CVE-2022-23943 [\[CVE json\]](./CVE-2022-23943.cve.json)

### Affected

* Apache HTTP Server from 2.4 through 2.4.52


### Description

Out-of-bounds Write vulnerability in mod_sed of Apache HTTP Server allows an attacker to overwrite heap memory with possibly attacker provided data.

This issue affects Apache HTTP Server 2.4 version 2.4.52 and prior versions.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Ronald Crane (Zippenhop LLC)


## mod_proxy_ajp: Possible request smuggling ## { #CVE-2022-26377 }

CVE-2022-26377 [\[CVE json\]](./CVE-2022-26377.cve.json)

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.53


### Description

Inconsistent Interpretation of HTTP Requests ('HTTP Request Smuggling') vulnerability in mod_proxy_ajp of Apache HTTP Server allows an attacker to smuggle requests to the AJP server it forwards requests to.  This issue affects Apache HTTP Server Apache HTTP Server 2.4 version 2.4.53 and prior versions.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Ricter Z @ 360 Noah Lab


## read beyond bounds in mod_isapi ## { #CVE-2022-28330 }

CVE-2022-28330 [\[CVE json\]](./CVE-2022-28330.cve.json)

### Affected

* Apache HTTP Server from Apache HTTP Server through 2.4.53


### Description

Apache HTTP Server 2.4.53 and earlier on Windows may read beyond bounds when configured to process requests with the mod_isapi module. 

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Ronald Crane (Zippenhop LLC) for reporting this issue


## read beyond bounds via ap_rwrite()  ## { #CVE-2022-28614 }

CVE-2022-28614 [\[CVE json\]](./CVE-2022-28614.cve.json)

### Affected

* Apache HTTP Server from unspecified through 2.4.53


### Description

The ap_rwrite() function in Apache HTTP Server 2.4.53 and earlier may read unintended memory if an attacker can cause the server to reflect very large input using ap_rwrite() or ap_rputs(), such as with mod_luas r:puts() function.

Modules compiled and distributed separately from Apache HTTP Server that use the "ap_rputs" function and may pass it a very large (INT_MAX or larger) string must be compiled against current headers to resolve the issue.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Ronald Crane (Zippenhop LLC) for reporting this issue


## Read beyond bounds in ap_strcmp_match() ## { #CVE-2022-28615 }

CVE-2022-28615 [\[CVE json\]](./CVE-2022-28615.cve.json)

### Affected

* Apache HTTP Server from Apache HTTP Server through 2.4.53


### Description

Apache HTTP Server 2.4.53 and earlier may crash or disclose information due to a read beyond bounds in ap_strcmp_match() when provided with an extremely large input buffer.  While no code distributed with the server can be coerced into such a call, third-party modules or lua scripts that use ap_strcmp_match() may hypothetically be affected.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Ronald Crane (Zippenhop LLC) for reporting this issue


## Denial of service in mod_lua r:parsebody ## { #CVE-2022-29404 }

CVE-2022-29404 [\[CVE json\]](./CVE-2022-29404.cve.json)

### Affected

* Apache HTTP Server from unspecified through 2.4.53


### Description

In Apache HTTP Server 2.4.53 and earlier, a malicious request to a lua script that calls r:parsebody(0) may cause a denial of service due to no default limit on possible input size.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Ronald Crane (Zippenhop LLC) for reporting this issue


## mod_sed denial of service ## { #CVE-2022-30522 }

CVE-2022-30522 [\[CVE json\]](./CVE-2022-30522.cve.json)

### Affected

* Apache HTTP Server at 2.4.53


### Description

If Apache HTTP Server 2.4.53 is configured to do transformations with mod_sed in contexts where the input to mod_sed may be very large, mod_sed may make excessively large memory allocations and trigger an abort.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* This issue was found by Brian Moussalli from the JFrog Security Research team


## Information Disclosure in mod_lua with websockets ## { #CVE-2022-30556 }

CVE-2022-30556 [\[CVE json\]](./CVE-2022-30556.cve.json)

### Affected

* Apache HTTP Server from unspecified through 2.4.53


### Description

Apache HTTP Server 2.4.53 and earlier may return lengths to applications calling r:wsread() that point past the end of the storage allocated for the buffer.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Ronald Crane (Zippenhop LLC) for reporting this issue


## mod_proxy X-Forwarded-For dropped by hop-by-hop mechanism ## { #CVE-2022-31813 }

CVE-2022-31813 [\[CVE json\]](./CVE-2022-31813.cve.json)

### Affected

* Apache HTTP Server from Apache HTTP Server 2.4 through 2.4.53


### Description

Apache HTTP Server 2.4.53 and earlier may not send the X-Forwarded-* headers to the origin server based on client side Connection header hop-by-hop mechanism.
This may be used to bypass IP based authentication on the origin server/application.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* The Apache HTTP Server project would like to thank Gaetan Ferry (Synacktiv) for reporting this issue


## mod_proxy prior to 2.4.55 allows a backend to trigger HTTP response splitting ## { #CVE-2022-37436 }

CVE-2022-37436 [\[CVE json\]](./CVE-2022-37436.cve.json)

### Affected

* Apache HTTP Server before 2.4.55


### Description

Prior to Apache HTTP Server 2.4.55, a malicious backend can cause the response headers to be truncated early, resulting in some headers being incorporated into the response body. If the later headers have any security purpose, they will not be interpreted by the client.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Dimas Fariski Setyawan Putra (@nyxsorcerer) (finder)


## mod_proxy_ajp Possible request smuggling ## { #CVE-2022-36760 }

CVE-2022-36760 [\[CVE json\]](./CVE-2022-36760.cve.json)

### Affected

* Apache HTTP Server from 2.4 through 2.4.54


### Description

Inconsistent Interpretation of HTTP Requests ('HTTP Request Smuggling') vulnerability in mod_proxy_ajp of Apache HTTP Server allows an attacker to smuggle requests to the AJP server it forwards requests to.  This issue affects Apache HTTP Server Apache HTTP Server 2.4 version 2.4.54 and prior versions.

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* ZeddYu_Lu from Qi'anxin Research Institute of Legendsec at Qi'anxin Group (finder)


## mod_dav out of  bounds read, or write of zero byte ## { #CVE-2006-20001 }

CVE-2006-20001 [\[CVE json\]](./CVE-2006-20001.cve.json)

### Affected

* Apache HTTP Server from 2.4 through 2.4.54


### Description

A carefully crafted If: request header can cause a memory read, or write of a single zero byte, in a pool (heap) memory location beyond the header value sent. This could cause the process to crash.<br><br>This issue affects Apache HTTP Server 2.4.54 and earlier.<br>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


## HTTP request splitting with mod_rewrite and mod_proxy ## { #CVE-2023-25690 }

CVE-2023-25690 [\[CVE json\]](./CVE-2023-25690.cve.json)

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


## mod_proxy_uwsgi HTTP response splitting ## { #CVE-2023-27522 }

CVE-2023-27522 [\[CVE json\]](./CVE-2023-27522.cve.json)

### Affected

* Apache HTTP Server from 2.4.30 through 2.4.55


### Description

<div>HTTP Response Smuggling vulnerability in Apache HTTP Server via mod_<code>proxy_uwsgi</code>. This issue affects Apache HTTP Server: from 2.4.30 through 2.4.55.</div><div>Special characters in the origin response header can truncate/split the response forwarded to the client.<br></div>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Dimas Fariski Setyawan Putra (nyxsorcerer) (finder)


## mod_macro buffer over-read ## { #CVE-2023-31122 }

CVE-2023-31122 [\[CVE json\]](./CVE-2023-31122.cve.json)

### Affected

* Apache HTTP Server through 2.4.57


### Description

Out-of-bounds Read vulnerability in mod_macro of Apache HTTP Server.<p>This issue affects Apache HTTP Server: through 2.4.57.</p>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* David Shoon (github/davidshoon) (finder)


## DoS in HTTP/2 with initial windows size 0 ## { #CVE-2023-43622 }

CVE-2023-43622 [\[CVE json\]](./CVE-2023-43622.cve.json)

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


## HTTP/2 stream memory not reclaimed right away on RST ## { #CVE-2023-45802 }

CVE-2023-45802 [\[CVE json\]](./CVE-2023-45802.cve.json)

### Affected

* Apache HTTP Server from 2.4.17 through 2.4.57


### Description

When a HTTP/2 stream was reset (RST frame) by a client, there was a time window were the request's memory resources were not reclaimed immediately. Instead, de-allocation was deferred to connection close. A client could send new requests and resets, keeping the connection busy and open and causing the memory footprint to keep on growing. On connection close, all resources were reclaimed, but the process might run out of memory before that.<br><br>This was found by the reporter during testing of&nbsp;CVE-2023-44487 (HTTP/2 Rapid Reset Exploit) with their own test client. During "normal" HTTP/2 use, the probability to hit this bug is very low. The kept memory would not become noticeable before the connection closes or times out.<br><br>Users are recommended to upgrade to version 2.4.58, which fixes the issue.<br>

### References
* https://httpd.apache.org/security/vulnerabilities_24.html


### Credits
* Will Dormann of Vul Labs (finder)
* David Warren of Vul Labs (finder)
