---
title: Apache Tomcat security advisories
description: Security information for Apache Tomcat
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Tomcat? You can read more about the projects' security policy on their [security page](https://tomcat.apache.org/security.html), and email your report to the [Apache Tomcat Security Team](mailto:security@tomcat.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://tomcat.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Tomcat: Request header mix-up between HTTP/2 streams ## { #CVE-2020-17527 }

CVE-2020-17527 [\[CVE json\]](./CVE-2020-17527.cve.json) [\[OSV json\]](./CVE-2020-17527.osv.json)



_Last updated: 2020-12-03T18:25:33.380Z_

### Affected

* Apache Tomcat at Apache Tomcat 10 10.0.0-M1 to 10.0.0-M9
* Apache Tomcat at Apache Tomcat 9 9.0.0-M1 to 9.0.39
* Apache Tomcat at Apache Tomcat 8.5 8.5.0 to 8.5.59


### Description

While investigating bug 64830 it was discovered that Apache Tomcat 10.0.0-M1 to 10.0.0-M9, 9.0.0-M1 to 9.0.39 and 8.5.0 to 8.5.59 could re-use an HTTP request header value from the previous stream received on an HTTP/2 connection for the request associated with the subsequent stream. While this would most likely lead to an error and the closure of the HTTP/2 connection, it is possible that information could leak between requests.

### References
* https://lists.apache.org/thread.html/rce5ac9a40173651d540babce59f6f3825f12c6d4e886ba00823b11e5%40%3Cannounce.tomcat.apache.org%3E


## Apache Tomcat information disclosure ## { #CVE-2021-24122 }

CVE-2021-24122 [\[CVE json\]](./CVE-2021-24122.cve.json) [\[OSV json\]](./CVE-2021-24122.osv.json)



_Last updated: 2021-01-14T14:26:04.037Z_

### Affected

* Apache Tomcat from Apache Tomcat 10 before 10.0.0-M10
* Apache Tomcat from Apache Tomcat 9 before 9.0.40
* Apache Tomcat from Apache Tomcat 8.5 before 8.5.60
* Apache Tomcat from Apache Tomcat 7 before 7.0.106


### Description

When serving resources from a network location using the NTFS file system, Apache Tomcat versions 10.0.0-M1 to 10.0.0-M9, 9.0.0.M1 to 9.0.39, 8.5.0 to 8.5.59 and 7.0.0 to 7.0.106 were susceptible to JSP source code disclosure in some configurations. The root cause was the unexpected behaviour of the JRE API File.getCanonicalPath() which in turn was caused by the inconsistent behaviour of the Windows API (FindFirstFileW) in some circumstances.

### References
* https://lists.apache.org/thread.html/r1595889b083e05986f42b944dc43060d6b083022260b6ea64d2cec52%40%3Cannounce.tomcat.apache.org%3E


### Credits
* This issue was identified by Ilja Brander.


## Apache Tomcat h2c request mix-up ## { #CVE-2021-25122 }

CVE-2021-25122 [\[CVE json\]](./CVE-2021-25122.cve.json) [\[OSV json\]](./CVE-2021-25122.osv.json)



_Last updated: 2021-03-01T11:12:28.219Z_

### Affected

* Apache Tomcat from Apache Tomcat 10 before 10.0.2
* Apache Tomcat from Apache Tomcat 9 before 9.0.42
* Apache Tomcat from Apache Tomcat 8.5 before 8.5.62


### Description

When responding to new h2c connection requests, Apache Tomcat versions 10.0.0-M1 to 10.0.0, 9.0.0.M1 to 9.0.41 and 8.5.0 to 8.5.61 could duplicate request headers and a limited amount of request body from one request to another meaning user A and user B could both see the results of user A's request.

### References
* https://lists.apache.org/thread.html/r7b95bc248603360501f18c8eb03bb6001ec0ee3296205b34b07105b7%40%3Cannounce.tomcat.apache.org%3E


## Incomplete fix for CVE-2020-9484 ## { #CVE-2021-25329 }

CVE-2021-25329 [\[CVE json\]](./CVE-2021-25329.cve.json) [\[OSV json\]](./CVE-2021-25329.osv.json)



_Last updated: 2021-03-01T12:01:51.094Z_

### Affected

* Apache Tomcat from Apache Tomcat 10 before 10.0.0
* Apache Tomcat from Apache Tomcat 9 before 9.0.41
* Apache Tomcat from Apache Tomcat 8.5 before 8.5.61
* Apache Tomcat from Apache Tomcat 7 before 7.0.107


### Description

The fix for CVE-2020-9484 was incomplete. When using Apache Tomcat 10.0.0-M1 to 10.0.0, 9.0.0.M1 to 9.0.41, 8.5.0 to 8.5.61 or 7.0.0. to 7.0.107 with a configuration edge case that was highly unlikely to be used, the Tomcat instance was still vulnerable to CVE-2020-9494. Note that both the previously published prerequisites for CVE-2020-9484 and the previously published mitigations for CVE-2020-9484 also apply to this issue.

### References
* https://lists.apache.org/thread.html/rfe62fbf9d4c314f166fe8c668e50e5d9dd882a99447f26f0367474bf%40%3Cannounce.tomcat.apache.org%3E


### Credits
* This issue was identified by Trung Pham of Viettel Cyber Security.


## DoS after non-blocking IO error ## { #CVE-2021-30639 }

CVE-2021-30639 [\[CVE json\]](./CVE-2021-30639.cve.json) [\[OSV json\]](./CVE-2021-30639.osv.json)



_Last updated: 2021-07-12T13:20:34.738Z_

### Affected

* Apache Tomcat at Apache Tomcat 10 10.0.3 to 10.0.4
* Apache Tomcat at Apache Tomcat 9 9.0.44
* Apache Tomcat at Apache Tomcat 8.5 8.5.64


### Description

A vulnerability in Apache Tomcat allows an attacker to remotely trigger a denial of service. An error introduced as part of a change to improve error handling during non-blocking I/O meant that the error flag associated with the Request object was not reset between requests. This meant that once a non-blocking I/O error occurred, all future requests handled by that request object would fail. Users were able to trigger non-blocking I/O errors, e.g. by dropping a connection, thereby creating the possibility of triggering a DoS.
Applications that do not use non-blocking I/O are not exposed to this vulnerability. This issue affects Apache Tomcat 10.0.3 to 10.0.4; 9.0.44; 8.5.64.

### References
* https://lists.apache.org/thread.html/rd84fae1f474597bdf358f5bdc0a5c453c507bd527b83e8be6b5ea3f4%40%3Cannounce.tomcat.apache.org%3E


## Auth weakness in JNDIRealm ## { #CVE-2021-30640 }

CVE-2021-30640 [\[CVE json\]](./CVE-2021-30640.cve.json) [\[OSV json\]](./CVE-2021-30640.osv.json)



_Last updated: 2021-07-12T13:14:16.116Z_

### Affected

* Apache Tomcat at Apache Tomcat 10 10.0.0-M1 to 10.0.5
* Apache Tomcat at Apache Tomcat 9 9.0.0.M1 to 9.0.45
* Apache Tomcat at Apache Tomcat 8.5 8.5.0 to 8.5.65
* Apache Tomcat at Apache Tomcat 7 7.0.0 to 7.0.108


### Description

A vulnerability in the JNDI Realm of Apache Tomcat allows an attacker to authenticate using variations of a valid user name and/or to bypass some of the protection provided by the LockOut Realm.  This issue affects Apache Tomcat 10.0.0-M1 to 10.0.5; 9.0.0.M1 to 9.0.45; 8.5.0 to 8.5.65.

### References
* https://lists.apache.org/thread.html/r59f9ef03929d32120f91f4ea7e6e79edd5688d75d0a9b65fd26d1fe8%40%3Cannounce.tomcat.apache.org%3E


## Incorrect Transfer-Encoding handling with HTTP/1.0 ## { #CVE-2021-33037 }

CVE-2021-33037 [\[CVE json\]](./CVE-2021-33037.cve.json) [\[OSV json\]](./CVE-2021-33037.osv.json)



_Last updated: 2021-07-12T13:31:58.821Z_

### Affected

* Apache Tomcat at Apache Tomcat 10 10.0.0-M1 to 10.0.6
* Apache Tomcat at Apache Tomcat 9 9.0.0.M1 to 9.0.46
* Apache Tomcat at Apache Tomcat 8 8.5.0 to 8.5.66


### Description

Apache Tomcat 10.0.0-M1 to 10.0.6, 9.0.0.M1 to 9.0.46 and 8.5.0 to 8.5.66 did not correctly parse the HTTP transfer-encoding request header in some circumstances leading to the possibility to request smuggling when used with a reverse proxy. Specifically:
- Tomcat incorrectly ignored the transfer encoding header if the client declared it would only accept an HTTP/1.0 response;
- Tomcat honoured the identify encoding; and
- Tomcat did not ensure that, if present, the chunked encoding was the final encoding.

### References
* https://lists.apache.org/thread.html/r612a79269b0d5e5780c62dfd34286a8037232fec0bc6f1a7e60c9381%40%3Cannounce.tomcat.apache.org%3E


### Credits
* The Apache Tomcat Security Team would like to thank Bahruz Jabiyev, Steven Sprecher and Kaan Onarlioglu of NEU seclab for identifying and reporting this issue.


## Apache Tomcat DoS with unexpected TLS packet ## { #CVE-2021-41079 }

CVE-2021-41079 [\[CVE json\]](./CVE-2021-41079.cve.json) [\[OSV json\]](./CVE-2021-41079.osv.json)



_Last updated: 2021-09-15T17:56:16.883Z_

### Affected

* Apache Tomcat at Apache Tomcat 8.5 8.5.0 to 8.5.63
* Apache Tomcat at Apache Tomcat 9 9.0.0-M1 to 9.0.43
* Apache Tomcat at Apache Tomcat 10 10.0.0-M1 to 10.0.2


### Description

Apache Tomcat 8.5.0 to 8.5.63, 9.0.0-M1 to 9.0.43 and 10.0.0-M1 to 10.0.2 did not properly validate incoming TLS packets. When Tomcat was configured to use NIO+OpenSSL or NIO2+OpenSSL for TLS, a specially crafted packet could be used to trigger an infinite loop resulting in a denial of service.

### References
* https://lists.apache.org/thread.html/rccdef0349fdf4fb73a4e4403095446d7fe6264e0a58e2df5c6799434%40%3Cannounce.tomcat.apache.org%3E


### Credits
* The Apache Tomcat security team would like to thank Thomas Wozenilek for originally reporting this issue and David Frankson of Infinite Campus for also providing a test case that reproduced the issue.


## DoS via memory leak with WebSocket connections ## { #CVE-2021-42340 }

CVE-2021-42340 [\[CVE json\]](./CVE-2021-42340.cve.json) [\[OSV json\]](./CVE-2021-42340.osv.json)



_Last updated: 2021-10-14T14:26:25.345Z_

### Affected

* Apache Tomcat at Apache Tomcat 10 10.0.0-M10 to 10.0.11
* Apache Tomcat at Apache Tomcat 10 10.1.0-M1 to 10.1.0-M5
* Apache Tomcat at Apache Tomcat 9 9.0.40 to 9.0.53
* Apache Tomcat at Apache Tomcat 8 8.5.60 to 8.5.71


### Description

The fix for bug 63362 present in Apache Tomcat 10.1.0-M1 to 10.1.0-M5, 10.0.0-M1 to 10.0.11, 9.0.40 to 9.0.53 and 8.5.60 to 8.5.71 introduced a memory leak. The object introduced to collect metrics for HTTP upgrade connections was not released for WebSocket connections once the connection was closed. This created a memory leak that, over time, could lead to a denial of service via an OutOfMemoryError.

### References
* https://lists.apache.org/thread.html/r83a35be60f06aca2065f188ee542b9099695d57ced2e70e0885f905c%40%3Cannounce.tomcat.apache.org%3E


## Apache Tomcat: Information disclosure ## { #CVE-2021-43980 }

CVE-2021-43980 [\[CVE json\]](./CVE-2021-43980.cve.json) [\[OSV json\]](./CVE-2021-43980.osv.json)



_Last updated: 2022-09-28T13:18:54.072Z_

### Affected

* Apache Tomcat at 10.1.0-M1 to 10.1.0-M12
* Apache Tomcat at 10.0.0-M1 to 10.0.18
* Apache Tomcat at 9.0.0-M1 to 9.0.60
* Apache Tomcat at 8.5.0 to 8.5.77


### Description

The simplified implementation of blocking reads and writes introduced in Tomcat 10 and back-ported to Tomcat 9.0.47 onwards exposed a long standing (but extremely hard to trigger) concurrency bug in Apache Tomcat 10.1.0 to 10.1.0-M12, 10.0.0-M1 to 10.0.18, 9.0.0-M1 to 9.0.60 and 8.5.0 to 8.5.77 that could cause client connections to share an Http11Processor instance resulting in responses, or part responses, to be received by the wrong client. 

### References
* https://lists.apache.org/thread/3jjqbsp6j88b198x5rmg99b1qr8ht3g3


### Credits
* Thanks to Adam Thomas, Richard Hernandez and Ryan Schmitt for discovering the issue and working with the Tomcat security team to identify the root cause and appropriate fix.


## Local privilege escalation with FileStore ## { #CVE-2022-23181 }

CVE-2022-23181 [\[CVE json\]](./CVE-2022-23181.cve.json) [\[OSV json\]](./CVE-2022-23181.osv.json)



_Last updated: 2022-01-26T11:25:59.878Z_

### Affected

* Apache Tomcat at Apache Tomcat 10.1 10.1.0-M1 to 10.1.0-M8
* Apache Tomcat at Apache Tomcat 10.0 10.0.0-M5 to 10.0.14
* Apache Tomcat at Apache Tomcat 9 9.0.35 to 9.0.56
* Apache Tomcat at Apache Tomcat 8 8.5.55 to 8.5.73


### Description

The fix for bug CVE-2020-9484 introduced a time of check, time of use vulnerability into Apache Tomcat 10.1.0-M1 to 10.1.0-M8, 10.0.0-M5 to 10.0.14, 9.0.35 to 9.0.56 and 8.5.55 to 8.5.73 that allowed a local attacker to perform actions with the privileges of the user that the Tomcat process is using. This issue is only exploitable when Tomcat is configured to persist sessions using the FileStore. 

### References
* https://lists.apache.org/thread/l8x62p3k19yfcb208jo4zrb83k5mfwg9


## Response mix-up with WebSocket concurrent send and close ## { #CVE-2022-25762 }

CVE-2022-25762 [\[CVE json\]](./CVE-2022-25762.cve.json) [\[OSV json\]](./CVE-2022-25762.osv.json)



_Last updated: 2022-05-12T20:00:18.925Z_

### Affected

* Apache Tomcat at Apache Tomcat 9 9.0.0.M1 to 9.0.20
* Apache Tomcat at Apache Tomcat 8.5 8.5.0 to 8.5.75


### Description

If a web application sends a WebSocket message concurrently with the WebSocket connection closing when running on Apache Tomcat 8.5.0 to 8.5.75 or Apache Tomcat 9.0.0.M1 to 9.0.20, it is possible that the application will continue to use the socket after it has been closed. The error handling triggered in this case could cause the a pooled object to be placed in the pool twice. This could result in subsequent connections using the same object concurrently which could result in data being returned to the wrong use and/or other errors.

### References
* https://lists.apache.org/thread/6ckmjfb1k61dyzkto9vm2k5jvt4o7w7c


## EncryptInterceptor does not provide complete protection on insecure networks ## { #CVE-2022-29885 }

CVE-2022-29885 [\[CVE json\]](./CVE-2022-29885.cve.json) [\[OSV json\]](./CVE-2022-29885.osv.json)



_Last updated: 2022-05-11T16:28:52.897Z_

### Affected

* Apache Tomcat at Apache Tomcat 10.1 10.1.0-M1 to 10.1.0-M14
* Apache Tomcat at Apache Tomcat 10 10.0.0-M1 to 10.0.20
* Apache Tomcat at Apache Tomcat 9 9.0.13 to 9.0.62
* Apache Tomcat at Apache Tomcat 8.5 8.5.38 to 8.5.78 


### Description

The documentation of Apache Tomcat 10.1.0-M1 to 10.1.0-M14, 10.0.0-M1 to 10.0.20, 9.0.13 to 9.0.62 and 8.5.38 to 8.5.78 for the EncryptInterceptor incorrectly stated it enabled Tomcat clustering to run over an untrusted network. This was not correct. While the EncryptInterceptor does provide confidentiality and integrity protection, it does not protect against all risks associated with running over any untrusted network, particularly DoS risks. 

### References
* https://lists.apache.org/thread/2b4qmhbcyqvc7dyfpjyx54c03x65vhcv


### Credits
* This issue was reported to the Apache Tomcat Security team by 4ra1n.


## XSS in examples web application ## { #CVE-2022-34305 }

CVE-2022-34305 [\[CVE json\]](./CVE-2022-34305.cve.json) [\[OSV json\]](./CVE-2022-34305.osv.json)



_Last updated: 2022-06-23T10:22:24.067Z_

### Affected

* Apache Tomcat at Apache Tomcat 8.5 8.5.50 to 8.5.81
* Apache Tomcat at Apache Tomcat 9 9.0.30 to 9.0.64
* Apache Tomcat at Apache Tomcat 10.0 10.0.0-M1 to 10.0.22
* Apache Tomcat at Apache Tomcat 10.1 10.1.0-M1 to 10.1.0-M16


### Description

In Apache Tomcat 10.1.0-M1 to 10.1.0-M16, 10.0.0-M1 to 10.0.22, 9.0.30 to 9.0.64 and 8.5.50 to 8.5.81 the Form authentication example in the examples web application displayed user provided data without filtering, exposing a XSS vulnerability. 

### References
* https://lists.apache.org/thread/k04zk0nq6w57m72w5gb0r6z9ryhmvr4k


## Apache Tomcat request smuggling via malformed content-length ## { #CVE-2022-42252 }

CVE-2022-42252 [\[CVE json\]](./CVE-2022-42252.cve.json) [\[OSV json\]](./CVE-2022-42252.osv.json)



_Last updated: 2022-11-18T12:36:02.907Z_

### Affected

* Apache Tomcat at Apache Tomcat 10.1.x 10.1.0-M1 to 10.1.0
* Apache Tomcat at Apache Tomcat 10.0.x 10.0.0-M1 to 10.0.26
* Apache Tomcat at Apache Tomcat 9.0.x 9.0.0-M1 to 9.0.67
* Apache Tomcat at Apache Tomcat 8.5.x 8.5.0 to 8.5.82


### Description

If Apache Tomcat 8.5.0 to 8.5.82, 9.0.0-M1 to 9.0.67, 10.0.0-M1 to 10.0.26 or 10.1.0-M1 to 10.1.0 was configured to ignore invalid HTTP headers via setting rejectIllegalHeader to false (the default for 8.5.x only), Tomcat did not reject a request containing an invalid Content-Length header making a request smuggling attack possible if Tomcat was located behind a reverse proxy that also failed to reject the request with the invalid header. 

### References
* https://lists.apache.org/thread/zzcxzvqfdqn515zfs3dxb7n8gty589sq


### Credits
* Thanks to Sam Shahsavar who discovered this issue and reported it to the Apache Tomcat security team.


## JsonErrorReportValve escaping ## { #CVE-2022-45143 }

CVE-2022-45143 [\[CVE json\]](./CVE-2022-45143.cve.json) [\[OSV json\]](./CVE-2022-45143.osv.json)



_Last updated: 2023-03-21T17:23:52.275Z_

### Affected

* Apache Tomcat from 10.1.0-M1 through 10.1.1
* Apache Tomcat from 9.0.40 through 9.0.68
* Apache Tomcat at 8.5.83


### Description

The JsonErrorReportValve in Apache Tomcat 8.5.83, 9.0.40 to 9.0.68 and 10.1.0-M1 to 10.1.1 did not escape the type, message or description values. In some circumstances these are constructed from user provided data and it was therefore possible for users to supply values that invalidated or manipulated the JSON output.

### References
* https://lists.apache.org/thread/yqkd183xrw3wqvnpcg3osbcryq85fkzj


## JSESSIONID Cookie missing secure attribute in some configurations ## { #CVE-2023-28708 }

CVE-2023-28708 [\[CVE json\]](./CVE-2023-28708.cve.json) [\[OSV json\]](./CVE-2023-28708.osv.json)



_Last updated: 2023-03-22T10:11:10.614Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.0-M2
* Apache Tomcat from 10.1.0-M1 through 10.1.5
* Apache Tomcat from 9.0.0-M1 through 9.0.71
* Apache Tomcat from 8.5.0 through 8.5.85


### Description

<div>
<div>
<p>When using the RemoteIpFilter with requests received from a    reverse proxy via HTTP that include the X-Forwarded-Proto    header set to https, session cookies created by Apache Tomcat 11.0.0-M1 to 11.0.0.-M2, 10.1.0-M1 to 10.1.5, 9.0.0-M1 to 9.0.71 and 8.5.0 to 8.5.85 did not&nbsp;include the secure attribute. This could result in the user agent&nbsp;<span style="background-color: var(--wht);">transmitting the session cookie over an insecure channel.</span></p></div>
</div>


### References
* https://lists.apache.org/thread/hdksc59z3s7tm39x0pp33mtwdrt8qr67


## Fix for CVE-2023-24998 is incomplete ## { #CVE-2023-28709 }

CVE-2023-28709 [\[CVE json\]](./CVE-2023-28709.cve.json) [\[OSV json\]](./CVE-2023-28709.osv.json)



_Last updated: 2023-05-22T10:09:00.405Z_

### Affected

* Apache Tomcat from 11.0.0-M2 through 11.0.0-M4
* Apache Tomcat from 10.1.5 through 10.1.7
* Apache Tomcat from 9.0.71 through 9.0.73
* Apache Tomcat from 8.5.85 through 8.5.87


### Description

<div><p>The fix for CVE-2023-24998 was incomplete for Apache Tomcat 11.0.0-M2 to 11.0.0-M4, 10.1.5 to 10.1.7, 9.0.71 to 9.0.73 and 8.5.85 to 8.5.87. If non-default HTTP       connector settings were used such that the maxParameterCount&nbsp;could be reached using query string parameters and a request was       submitted that supplied exactly maxParameterCount parameters&nbsp;<span style="background-color: var(--wht);">in the query string, the limit for uploaded request parts could be&nbsp;</span><span style="background-color: var(--wht);">bypassed with the potential for a denial of service to occur.</span></p></div><br>

### References
* https://lists.apache.org/thread/7wvxonzwb7k9hx9jt3q33cmy7j97jo3j


### Credits
* Chenwei Jiang, Chenfeng Nie and Yue Yang from the Huawei Nebula Security Lab (finder)


## AJP response header mix-up ## { #CVE-2023-34981 }

CVE-2023-34981 [\[CVE json\]](./CVE-2023-34981.cve.json) [\[OSV json\]](./CVE-2023-34981.osv.json)



_Last updated: 2023-06-21T10:26:13.887Z_

### Affected

* Apache Tomcat at 11.0.0-M5
* Apache Tomcat at 10.1.8
* Apache Tomcat at 9.0.74
* Apache Tomcat at 8.5.88


### Description

A regression in the fix for bug 66512 in Apache Tomcat 11.0.0-M5, 10.1.8, 9.0.74 and 8.5.88 meant that, if a response did not include any HTTP headers no AJP SEND_HEADERS messare woudl be sent for the response which in turn meant that at least one AJP proxy (mod_proxy_ajp) would use the response headers from the previous request leading to an information leak.

### References
* https://lists.apache.org/thread/j1ksjh9m9gx1q60rtk1sbzmxhvj5h5qz


### Credits
* Hidenobu Hayashi and Yuichiro Fukubayashi of M3, Inc. (finder)


## Open redirect with FORM authentication ## { #CVE-2023-41080 }

CVE-2023-41080 [\[CVE json\]](./CVE-2023-41080.cve.json) [\[OSV json\]](./CVE-2023-41080.osv.json)



_Last updated: 2023-08-25T20:39:30.851Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.0-M10
* Apache Tomcat from 10.1.0-M1 through 10.0.12
* Apache Tomcat from 9.0.0-M1 through 9.0.79
* Apache Tomcat from 8.5.0 through 8.5.92


### Description

URL Redirection to Untrusted Site ('Open Redirect') vulnerability in FORM authentication feature Apache Tomcat.<p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.0-M10, from 10.1.0-M1 through 10.0.12, from 9.0.0-M1 through 9.0.79 and from 8.5.0 through 8.5.92.</p>The vulnerability is limited to the ROOT (default) web application.

### References
* https://lists.apache.org/thread/71wvwprtx2j2m54fovq9zr7gbm2wow2f


### Credits
* This vulnerability was reported responsibly to the Tomcat security team by Yiheng Cao. (finder)


## Unexpected use of first declared worker in mod_jk for unmapped request ## { #CVE-2023-41081 }

CVE-2023-41081 [\[CVE json\]](./CVE-2023-41081.cve.json)

_Last updated: 2023-09-28T21:30:55.612Z_

### Affected

* Apache Tomcat Connectors from 1.2.0 through 1.2.48


### Description

<div><p>Important: Authentication Bypass CVE-2023-41081
<br>
</p><p>The mod_jk component of <span style="background-color: rgb(255, 255, 255);">Apache Tomcat Connectors&nbsp;</span>in some circumstances, such as when a configuration included&nbsp;"JkOptions +ForwardDirectories" but the configuration did not       provide explicit mounts for all possible proxied requests, mod_jk would       use an implicit mapping and map the request to the first defined worker.&nbsp;<span style="background-color: var(--wht);">Such an implicit mapping could result in the unintended exposure of the&nbsp;</span><span style="background-color: var(--wht);">status worker and/or bypass security constraints configured in httpd. As&nbsp;</span><span style="background-color: var(--wht);">of JK 1.2.49, the implicit mapping functionality has been removed and all&nbsp;</span><span style="background-color: var(--wht);">mappings must now be via explicit configuration.&nbsp;</span><span style="background-color: var(--wht);">Only mod_jk is affected&nbsp;</span><span style="background-color: var(--wht);">by this issue. The ISAPI redirector is not affected.</span></p></div><p>This issue affects Apache Tomcat Connectors <span style="background-color: rgb(255, 255, 255);">(mod_jk only)</span>: from 1.2.0 through 1.2.48.</p><p>Users are recommended to upgrade to version 1.2.49, which fixes the issue.</p><h2>History<br></h2><h2></h2><p>2023-09-13 Original advisory
<br>2023-09-28 Updated summary<br></p>

### References
* https://lists.apache.org/thread/rd1r26w7271jyqgzr4492tooyt583d8b
* https://www.openwall.com/lists/oss-security/2023/09/13/2
* https://lists.debian.org/debian-lts-announce/2023/09/msg00027.html


### Credits
* Karl von Randow (finder)


## FileUpload: DoS due to accumulation of temporary files on Windows ## { #CVE-2023-42794 }

CVE-2023-42794 [\[CVE json\]](./CVE-2023-42794.cve.json) [\[OSV json\]](./CVE-2023-42794.osv.json)



_Last updated: 2023-10-10T17:17:04.806Z_

### Affected

* Apache Tomcat from 9.0.70 through 9.0.80
* Apache Tomcat from 8.5.85 through 8.5.93


### Description

Incomplete Cleanup vulnerability in Apache Tomcat.<br><br>The internal fork of Commons FileUpload packaged with Apache Tomcat 9.0.70 through 9.0.80 and 8.5.85 through 8.5.93 included an unreleased, 
in progress refactoring that exposed a potential denial of service on 
Windows if a web application opened a stream for an uploaded file but 
failed to close the stream. The file would never be deleted from disk 
creating the possibility of an eventual denial of service due to the 
disk being full.
<br><p><span style="background-color: var(--wht);">Users are recommended to upgrade to version 9.0.81 onwards or 8.5.94 onwards, which fixes the issue.</span><br></p>

### References
* https://lists.apache.org/thread/vvbr2ms7lockj1hlhz5q3wmxb2mwcw82


### Credits
* Mohammad Khedmatgozar (cellbox) (finder)


## Failure during request clean-up leads to sensitive data leaking to subsequent requests ## { #CVE-2023-42795 }

CVE-2023-42795 [\[CVE json\]](./CVE-2023-42795.cve.json) [\[OSV json\]](./CVE-2023-42795.osv.json)



_Last updated: 2023-10-10T17:42:21.672Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.0-M11
* Apache Tomcat from 10.1.0-M1 through 10.1.13
* Apache Tomcat from 9.0.0-M1 through 9.0.80
* Apache Tomcat from 8.5.0 through 8.5.93


### Description

Incomplete Cleanup vulnerability in Apache Tomcat.<p>When recycling various internal objects in Apache Tomcat from 11.0.0-M1 through 11.0.0-M11, from 10.1.0-M1 through 10.1.13, from 9.0.0-M1 through 9.0.80 and from 8.5.0 through 8.5.93, an error could 
cause Tomcat to skip some parts of the recycling process leading to 
information leaking from the current request/response to the next.<br></p><p>Users are recommended to upgrade to version 11.0.0-M12 onwards, 10.1.14 onwards, 9.0.81 onwards or 8.5.94 onwards, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/065jfyo583490r9j2v73nhpyxdob56lw


## Trailer header parsing too lenient ## { #CVE-2023-45648 }

CVE-2023-45648 [\[CVE json\]](./CVE-2023-45648.cve.json) [\[OSV json\]](./CVE-2023-45648.osv.json)



_Last updated: 2023-10-10T18:38:37.767Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.0-M11
* Apache Tomcat from 10.1.0-M1 through 10.1.13
* Apache Tomcat from 9.0.0-M1 through 9.0.81
* Apache Tomcat from 8.5.0 through 8.5.93


### Description

Improper Input Validation vulnerability in Apache Tomcat.<p>Tomcat&nbsp;<span style="background-color: rgb(255, 255, 255);">from 11.0.0-M1 through 11.0.0-M11, from 10.1.0-M1 through 10.1.13, from 9.0.0-M1 through 9.0.81 and from 8.5.0 through 8.5.93</span> did not correctly parse HTTP trailer headers. A specially 
crafted, invalid trailer header could cause Tomcat to treat a single 
request as multiple requests leading to the possibility of request 
smuggling when behind a reverse proxy.<br></p><p><span style="background-color: var(--wht);">Users are recommended to upgrade to version 11.0.0-M12 onwards, 10.1.14 onwards, 9.0.81 onwards or 8.5.94 onwards, which fix the issue.</span><br></p>

### References
* https://lists.apache.org/thread/2pv8yz1pyp088tsxfb7ogltk9msk0jdp


### Credits
* Keran Mu and Jianjun Chen from Tsinghua University and Zhongguancun Laboratory (finder)


## HTTP request smuggling via malformed trailer headers ## { #CVE-2023-46589 }

CVE-2023-46589 [\[CVE json\]](./CVE-2023-46589.cve.json) [\[OSV json\]](./CVE-2023-46589.osv.json)



_Last updated: 2023-12-05T09:49:53.674Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.0-M10
* Apache Tomcat from 10.1.0-M1 through 10.1.15
* Apache Tomcat from 9.0.0-M1 through 9.0.82
* Apache Tomcat from 8.5.0 through 8.5.95


### Description

Improper Input Validation vulnerability in Apache Tomcat.<p>Tomcat <span style="background-color: rgb(255, 255, 255);">from 11.0.0-M1 through 11.0.0-M10, from 10.1.0-M1 through 10.1.15, from 9.0.0-M1 through 9.0.82 and from 8.5.0 through 8.5.95</span> did not correctly parse HTTP trailer headers. A trailer header that exceeded the header size limit could cause Tomcat to treat a single 
request as multiple requests leading to the possibility of request 
smuggling when behind a reverse proxy.<br></p><p><span style="background-color: var(--wht);">Users are recommended to upgrade to version 11.0.0-M11&nbsp;onwards, 10.1.16 onwards, 9.0.83 onwards or 8.5.96 onwards, which fix the issue.</span></p><br>

### References
* https://lists.apache.org/thread/0rqq6ktozqc42ro8hhxdmmdjm1k1tpxr


### Credits
* Norihito Aimoto (OSSTech Corporation)  (finder)


## Leaking of unrelated request bodies in default error page ## { #CVE-2024-21733 }

CVE-2024-21733 [\[CVE json\]](./CVE-2024-21733.cve.json) [\[OSV json\]](./CVE-2024-21733.osv.json)



_Last updated: 2024-01-19T10:29:13.588Z_

### Affected

* Apache Tomcat from 8.5.7 through 8.5.63
* Apache Tomcat from 9.0.0-M11 through 9.0.43


### Description

Generation of Error Message Containing Sensitive Information vulnerability in Apache Tomcat.<p>This issue affects Apache Tomcat: from 8.5.7 through 8.5.63, from 9.0.0-M11 through 9.0.43.</p><p>Users are recommended to upgrade to version 8.5.64 onwards or 9.0.44 onwards, which contain a fix for the issue.</p>

### References
* https://lists.apache.org/thread/h9bjqdd0odj6lhs2o96qgowcc6hb0cfz


### Credits
* xer0dayz from company Sn1perSecurity LLC (finder)


## WebSocket DoS with incomplete closing handshake ## { #CVE-2024-23672 }

CVE-2024-23672 [\[CVE json\]](./CVE-2024-23672.cve.json) [\[OSV json\]](./CVE-2024-23672.osv.json)



_Last updated: 2024-07-03T18:12:25.589Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.0-M16
* Apache Tomcat from 10.1.0-M1 through 10.1.18
* Apache Tomcat from 9.0.0-M1 through 9.0.85
* Apache Tomcat from 8.5.0 through 8.5.98


### Description

Denial of Service via incomplete cleanup vulnerability in Apache Tomcat. It was possible for WebSocket clients to keep WebSocket connections open leading to increased resource consumption.<p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.0-M16, from 10.1.0-M1 through 10.1.18, from 9.0.0-M1 through 9.0.85, from 8.5.0 through 8.5.98.</p><p>Users are recommended to upgrade to version 11.0.0-M17, 10.1.19, 9.0.86 or 8.5.99 which fix the issue.</p>

### References
* https://lists.apache.org/thread/cmpswfx6tj4s7x0nxxosvfqs11lvdx2f


## HTTP/2 header handling DoS ## { #CVE-2024-24549 }

CVE-2024-24549 [\[CVE json\]](./CVE-2024-24549.cve.json) [\[OSV json\]](./CVE-2024-24549.osv.json)



_Last updated: 2024-03-13T15:47:06.777Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.0-M16
* Apache Tomcat from 10.1.0-M1 through 10.1.18
* Apache Tomcat from 9.0.0-M1 through 9.0.85
* Apache Tomcat from 8.5.0 through 8.5.98


### Description

Denial of Service due to improper input validation vulnerability for HTTP/2 requests in Apache Tomcat. When processing an HTTP/2 request, if the request exceeded any of the configured limits for headers, the associated HTTP/2 stream was not reset until after all of the headers had been processed.<p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.0-M16, from 10.1.0-M1 through 10.1.18, from 9.0.0-M1 through 9.0.85, from 8.5.0 through 8.5.98.</p><p>Users are recommended to upgrade to version 11.0.0-M17, 10.1.19, 9.0.86 or 8.5.99 which fix the issue.</p>

### References
* https://lists.apache.org/thread/4c50rmomhbbsdgfjsgwlb51xdwfjdcvg


### Credits
* Bartek Nowotarski (finder)


## HTTP/2 excess header handling DoS ## { #CVE-2024-34750 }

CVE-2024-34750 [\[CVE json\]](./CVE-2024-34750.cve.json) [\[OSV json\]](./CVE-2024-34750.osv.json)



_Last updated: 2024-07-03T19:38:21.788Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.0-M20
* Apache Tomcat from 10.1.0-M1 through 10.1.24
* Apache Tomcat from 9.0.0-M1 through 9.0.89


### Description

<p>Improper Handling of Exceptional Conditions, Uncontrolled Resource Consumption vulnerability in Apache Tomcat. When processing an HTTP/2 stream, Tomcat did not handle some cases of excessive HTTP headers correctly. This led to a miscounting of active HTTP/2 streams which in turn led to the use of an incorrect infinite timeout which allowed connections to remain open which should have been closed.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.0-M20, from 10.1.0-M1 through 10.1.24, from 9.0.0-M1 through 9.0.89.</p><p>Users are recommended to upgrade to version 11.0.0-M21, 10.1.25 or 9.0.90, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/4kqf0bc9gxymjc2x7v3p7dvplnl77y8l


### Credits
* devme4f from VNPT-VCI (finder)


## Denial of Service ## { #CVE-2024-38286 }

CVE-2024-38286 [\[CVE json\]](./CVE-2024-38286.cve.json) [\[OSV json\]](./CVE-2024-38286.osv.json)



_Last updated: 2024-11-07T07:37:40.443Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.0-M20
* Apache Tomcat from 10.1.0-M1 through 10.1.24
* Apache Tomcat from 9.0.13 through 9.0.89


### Description

<p>Allocation of Resources Without Limits or Throttling vulnerability in Apache Tomcat.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.0-M20, from 10.1.0-M1 through 10.1.24, from 9.0.13 through 9.0.89. Older, unsupported versions may also be affected.<br></p><p>Users are recommended to upgrade to version 11.0.0-M21, 10.1.25, or 9.0.90, which fixes the issue.</p><p></p><div>Apache Tomcat, under certain configurations on any platform, allows an attacker to cause an OutOfMemoryError by abusing the TLS handshake process.<br></div><br><p></p>

### References
* https://lists.apache.org/thread/wms60cvbsz3fpbz9psxtfx8r41jl6d4s


### Credits
* Ozaki, North Grid Corporation (reporter)


## mod_jk: local users can view and modify configuration ## { #CVE-2024-46544 }

CVE-2024-46544 [\[CVE json\]](./CVE-2024-46544.cve.json) [\[OSV json\]](./CVE-2024-46544.osv.json)



_Last updated: 2024-09-23T10:51:17.287Z_

### Affected

* Apache Tomcat Connectors from 1.2.9-beta through 1.2.49


### Description

<p>Incorrect Default Permissions vulnerability in Apache Tomcat Connectors allows local users to view and modify shared memory containing mod_jk configuration which may lead to information disclosure and/or denial of service.</p><p>This issue affects Apache Tomcat Connectors: from 1.2.9-beta through 1.2.49. Only mod_jk on Unix like systems is affected. Neither the ISAPI redirector nor mod_jk on Windows is affected.<br></p><p>Users are recommended to upgrade to version 1.2.50, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/q1gp7cc38hs1r8gj8gfnopwznd5fpr4d


## RCE due to TOCTOU issue in JSP compilation ## { #CVE-2024-50379 }

CVE-2024-50379 [\[CVE json\]](./CVE-2024-50379.cve.json) [\[OSV json\]](./CVE-2024-50379.osv.json)



_Last updated: 2024-12-19T17:34:02.440Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.1
* Apache Tomcat from 10.1.0-M1 through 10.1.33
* Apache Tomcat from 9.0.0.M1 through 9.0.97


### Description

<p>Time-of-check Time-of-use (TOCTOU) Race Condition vulnerability during JSP compilation in Apache Tomcat permits an RCE on case insensitive file systems when the default servlet is enabled for write (non-default configuration).</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.1, from 10.1.0-M1 through 10.1.33, from 9.0.0.M1 through 9.0.97.</p><p>Users are recommended to upgrade to version 11.0.2, 10.1.34 or 9.0.98, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/y6lj6q1xnp822g6ro70tn19sgtjmr80r


### Credits
* Nacl, WHOAMI, Yemoli and Ruozhi (finder)


## Authentication bypass when using Jakarta Authentication API ## { #CVE-2024-52316 }

CVE-2024-52316 [\[CVE json\]](./CVE-2024-52316.cve.json) [\[OSV json\]](./CVE-2024-52316.osv.json)



_Last updated: 2024-11-18T11:32:31.150Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.0-M26
* Apache Tomcat from 10.1.0-M1 through 10.1.30
* Apache Tomcat from 9.0.0-M1 through 9.0.95


### Description

<p>Unchecked Error Condition vulnerability in Apache Tomcat. If Tomcat is configured to use a custom Jakarta Authentication (formerly JASPIC)&nbsp;ServerAuthContext component which may throw an exception during the authentication process without explicitly setting an HTTP status to indicate failure, the authentication may not fail, allowing the user to bypass the authentication process. There are no known Jakarta&nbsp;Authentication components that behave in this way.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.0-M26, from 10.1.0-M1 through 10.1.30, from 9.0.0-M1 through 9.0.95.</p><p>Users are recommended to upgrade to version 11.0.0, 10.1.31 or 9.0.96, which fix the issue.</p>

### References
* https://lists.apache.org/thread/lopzlqh91jj9n334g02om08sbysdb928


## Request/response mix-up with HTTP/2 ## { #CVE-2024-52317 }

CVE-2024-52317 [\[CVE json\]](./CVE-2024-52317.cve.json) [\[OSV json\]](./CVE-2024-52317.osv.json)



_Last updated: 2024-11-18T11:37:01.194Z_

### Affected

* Apache Tomcat from 11.0.0-M23 through 11.0.0-M26
* Apache Tomcat from 10.1.27 through 10.1.30
* Apache Tomcat from 9.0.92 through 9.0.95


### Description

<p>Incorrect object re-cycling and re-use vulnerability in Apache Tomcat.&nbsp;Incorrect recycling of the request and response used by HTTP/2 requests 
could lead to request and/or response mix-up between users.</p><p>This issue affects Apache Tomcat: from 11.0.0-M23 through 11.0.0-M26, from 10.1.27 through 10.1.30, from 9.0.92 through 9.0.95.</p><p>Users are recommended to upgrade to version 11.0.0, 10.1.31 or 9.0.96, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ty376mrxy1mmxtw3ogo53nc9l3co3dfs


## Incorrect JSP tag recycling leads to XSS ## { #CVE-2024-52318 }

CVE-2024-52318 [\[CVE json\]](./CVE-2024-52318.cve.json) [\[OSV json\]](./CVE-2024-52318.osv.json)



_Last updated: 2024-11-18T12:21:44.105Z_

### Affected

* Apache Tomcat at 11.0.0
* Apache Tomcat at 10.1.31
* Apache Tomcat at 9.0.96


### Description

<p>Incorrect object recycling and reuse vulnerability in Apache Tomcat.</p><p>This issue affects Apache Tomcat: 11.0.0, 10.1.31, 9.0.96.</p><p>Users are recommended to upgrade to version 11.0.1, 10.1.32 or 9.0.97, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/co243cw1nlh6p521c5265cm839wkqdp9


## DoS in examples web application ## { #CVE-2024-54677 }

CVE-2024-54677 [\[CVE json\]](./CVE-2024-54677.cve.json) [\[OSV json\]](./CVE-2024-54677.osv.json)



_Last updated: 2024-12-18T07:08:27.136Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.1
* Apache Tomcat from 10.1.0-M1 through 10.1.33
* Apache Tomcat from 9.0.0.M1 through 9.0.97


### Description

<p>Uncontrolled Resource Consumption vulnerability in the examples web application provided with Apache Tomcat leads to denial of service.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.1, from 10.1.0-M1 through 10.1.33, from 9.0.0.M1 through 9.9.97.</p><p>Users are recommended to upgrade to version 11.0.2, 10.1.34 or 9.0.98, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/tdtbbxpg5trdwc2wnopcth9ccvdftq2n


## RCE due to TOCTOU issue in JSP compilation - CVE-2024-50379 mitigation was incomplete ## { #CVE-2024-56337 }

CVE-2024-56337 [\[CVE json\]](./CVE-2024-56337.cve.json) [\[OSV json\]](./CVE-2024-56337.osv.json)



_Last updated: 2024-12-20T15:29:02.063Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.1
* Apache Tomcat from 10.1.0-M1 through 10.1.33
* Apache Tomcat from 9.0.0.M1 through 9.0.97


### Description

<p>Time-of-check Time-of-use (TOCTOU) Race Condition vulnerability in Apache Tomcat.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.1, from 10.1.0-M1 through 10.1.33, from 9.0.0.M1 through 9.0.97.</p><p>The mitigation for CVE-2024-50379 was incomplete.</p><p>Users running Tomcat on a case insensitive file system with the default servlet write enabled (readonly initialisation 
parameter set to the non-default value of false) may need additional configuration to fully mitigate CVE-2024-50379 depending on which version of Java they are using with Tomcat:<br>- running on Java 8 or Java 11: the system property&nbsp;sun.io.useCanonCaches must be explicitly set to false (it defaults to true)<br>- running on Java 17: the&nbsp;system property sun.io.useCanonCaches, if set, must be set to false&nbsp;(it defaults to false)<br>- running on Java 21 onwards: no further configuration is required&nbsp;(the system property and the problematic cache have been removed)</p><p><span style="background-color: var(--wht);">Tomcat 11.0.3, 10.1.35 and 9.0.99 onwards will include checks that&nbsp;sun.io.useCanonCaches is set appropriately before allowing the default servlet to be write enabled on a case insensitive file system. Tomcat will also set&nbsp;sun.io.useCanonCaches to false by default where it can.</span></p>

### References
* https://www.cve.org/CVERecord?id=CVE-2024-50379
* https://lists.apache.org/thread/b2b9qrgjrz1kvo4ym8y2wkfdvwoq6qbp


### Credits
* This vulnerability was first reported by Nacl, WHOAMI, Yemoli and Ruozhi. (finder)
* This vulnerability was independently reported with a very helpful PoC by dawu@knownsec 404 team and Sunflower@knownsec 404 team (finder)


## Potential RCE and/or information disclosure and/or information corruption with partial PUT ## { #CVE-2025-24813 }

CVE-2025-24813 [\[CVE json\]](./CVE-2025-24813.cve.json) [\[OSV json\]](./CVE-2025-24813.osv.json)



_Last updated: 2025-03-18T16:09:43.998Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.2
* Apache Tomcat from 10.1.0-M1 through 10.1.34
* Apache Tomcat from 9.0.0.M1 through 9.0.98


### Description

<p>Path Equivalence: 'file.Name' (Internal Dot) leading to&nbsp;<span style="background-color: var(--wht);">Remote Code Execution and/or Information disclosure&nbsp;</span><span style="background-color: var(--wht);">and/or malicious content added to uploaded files via write enabled&nbsp;</span><span style="background-color: var(--wht);">Default Servlet</span>&nbsp;in Apache Tomcat.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.2, from 10.1.0-M1 through 10.1.34, from 9.0.0.M1 through 9.0.98.</p><div><p>If all of the following were true, a malicious user was able to view       security sensitive files and/or inject content into those files:<br>-&nbsp;<span style="background-color: var(--wht);">writes enabled for the default servlet (disabled by default)<br></span><span style="background-color: var(--wht);">- support for partial PUT (enabled by default)<br></span><span style="background-color: var(--wht);">- a target URL for security sensitive uploads that was a sub-directory of&nbsp;</span><span style="background-color: var(--wht);">a target URL for public uploads<br>-&nbsp;</span><span style="background-color: var(--wht);">attacker knowledge of the names of security sensitive files being&nbsp;</span><span style="background-color: var(--wht);">uploaded<br>-&nbsp;</span><span style="background-color: var(--wht);">the security sensitive files also being uploaded via partial PUT</span></p><p><span style="background-color: var(--wht);">If all of the following were true, a malicious user was able to</span>       perform remote code execution:<br><span style="background-color: var(--wht);">- writes enabled for the default servlet (disabled by default)<br>-&nbsp;</span><span style="background-color: var(--wht);">support for partial PUT (enabled by default)<br>-&nbsp;</span><span style="background-color: var(--wht);">application was using Tomcat's file based session persistence with the&nbsp;</span><span style="background-color: var(--wht);">default storage location<br>-&nbsp;</span><span style="background-color: var(--wht);">application included a library that may be leveraged in a&nbsp;</span><span style="background-color: var(--wht);">deserialization attack</span></p><p><span style="background-color: var(--wht);">Users are recommended to upgrade to version 11.0.3, 10.1.35 or 9.0.98, which fixes the issue.</span></p></div>

### References
* https://lists.apache.org/thread/j5fkjv2k477os90nczf2v9l61fb0kkgq


### Credits
* COSCO Shipping Lines DIC (finder)
* sw0rd1ight (https://github.com/sw0rd1ight) (finder)


## DoS via malformed HTTP/2 PRIORITY_UPDATE frame ## { #CVE-2025-31650 }

CVE-2025-31650 [\[CVE json\]](./CVE-2025-31650.cve.json) [\[OSV json\]](./CVE-2025-31650.osv.json)



_Last updated: 2025-05-06T13:12:48.728Z_

### Affected

* Apache Tomcat from 9.0.76 through 9.0.102
* Apache Tomcat from 10.1.10 through 10.1.39
* Apache Tomcat from 11.0.0-M2 through 11.0.5


### Description

<p>Improper Input Validation vulnerability in Apache Tomcat. Incorrect error handling for some invalid HTTP priority headers resulted in incomplete clean-up of the failed request which created a memory leak. A large number of such requests could trigger an OutOfMemoryException resulting in a denial of service.</p><p>This issue affects Apache Tomcat: from 9.0.76 through 9.0.102, from 10.1.10 through 10.1.39, from 11.0.0-M2 through 11.0.5.</p><p>Users are recommended to upgrade to version 9.0.104, 10.1.40 or 11.0.6 which fix the issue.</p>

### References
* https://lists.apache.org/thread/j6zzk0y3yym9pzfzkq5vcyxzz0yzh826


## Bypass of rules in Rewrite Valve ## { #CVE-2025-31651 }

CVE-2025-31651 [\[CVE json\]](./CVE-2025-31651.cve.json) [\[OSV json\]](./CVE-2025-31651.osv.json)



_Last updated: 2025-05-06T13:13:07.142Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.5
* Apache Tomcat from 10.1.0-M1 through 10.1.39
* Apache Tomcat from 9.0.0.M1 through 9.0.102


### Description

<p>Improper Neutralization of Escape, Meta, or Control Sequences vulnerability in Apache Tomcat.&nbsp;For a subset of unlikely rewrite rule configurations, it was possible 
for a specially crafted request to bypass some rewrite rules. If those 
rewrite rules effectively enforced security constraints, those 
constraints could be bypassed.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.5, from 10.1.0-M1 through 10.1.39, from 9.0.0.M1 through 9.0.102.</p><p>Users are recommended to upgrade to version [FIXED_VERSION], which fixes the issue.</p>

### References
* https://lists.apache.org/list.html?announce@tomcat.apache.org


### Credits
* COSCO Shipping Lines DIC (finder)


## Security constraint bypass for CGI scripts ## { #CVE-2025-46701 }

CVE-2025-46701 [\[CVE json\]](./CVE-2025-46701.cve.json) [\[OSV json\]](./CVE-2025-46701.osv.json)



_Last updated: 2025-05-29T19:06:20.436Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.6
* Apache Tomcat from 10.1.0-M1 through 10.1.40
* Apache Tomcat from 9.0.0.M1 through 9.0.104


### Description

<p>Improper Handling of Case Sensitivity vulnerability in Apache Tomcat's GCI servlet allows security constraint bypass of security constraints that apply to the pathInfo component of a URI mapped to the CGI servlet.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.6, from 10.1.0-M1 through 10.1.40, from 9.0.0.M1 through 9.0.104.</p><p>Users are recommended to upgrade to version 11.0.7, 10.1.41 or 9.0.105, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/xhqqk9w5q45srcdqhogdk04lhdscv30j


### Credits
* Greg K (https://github.com/gregk4sec) (finder)


## FileUpload large number of parts with headers DoS ## { #CVE-2025-48988 }

CVE-2025-48988 [\[CVE json\]](./CVE-2025-48988.cve.json) [\[OSV json\]](./CVE-2025-48988.osv.json)



_Last updated: 2025-06-16T14:17:28.072Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.7
* Apache Tomcat from 10.1.0-M1 through 10.1.41
* Apache Tomcat from 9.0.0.M1 through 9.0.105


### Description

<p>Allocation of Resources Without Limits or Throttling vulnerability in Apache Tomcat.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.7, from 10.1.0-M1 through 10.1.41, from 9.0.0.M1 through 9.0.105.</p><p>Users are recommended to upgrade to version 11.0.8, 10.1.42 or 9.0.106, which fix the issue.</p>

### References
* https://lists.apache.org/thread/nzkqsok8t42qofgqfmck536mtyzygp18


### Credits
* TERASOLUNA Framework Security Team of NTT DATA Group Corporation (finder)


## exe side-loading via icalcs.exe in Tomcat installer for Windows ## { #CVE-2025-49124 }

CVE-2025-49124 [\[CVE json\]](./CVE-2025-49124.cve.json) [\[OSV json\]](./CVE-2025-49124.osv.json)



_Last updated: 2025-06-16T14:22:26.411Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.7
* Apache Tomcat from 10.1.0 through 10.1.41
* Apache Tomcat from 9.0.23 through 9.0.105


### Description

<p>Untrusted Search Path vulnerability in Apache Tomcat installer for Windows. During installation, the Tomcat installer for Windows used icacls.exe without specifying a full path.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.7, from 10.1.0 through 10.1.41, from 9.0.23 through 9.0.105.</p><p>Users are recommended to upgrade to version 11.0.8, 10.1.42 or 9.0.106, which fix the issue.</p>

### References
* https://lists.apache.org/thread/lnow7tt2j6hb9kcpkggx32ht6o90vqzv


### Credits
* T. Doğa Gelişli https://linkedin.com/in/tdogagelisli/ (finder)


## Security constraint bypass for pre/post-resources ## { #CVE-2025-49125 }

CVE-2025-49125 [\[CVE json\]](./CVE-2025-49125.cve.json) [\[OSV json\]](./CVE-2025-49125.osv.json)



_Last updated: 2025-06-16T14:20:04.248Z_

### Affected

* Apache Tomcat from 11.0.0-M1 through 11.0.7
* Apache Tomcat from 10.1.0-M1 through 10.1.41
* Apache Tomcat from 9.0.0.M1 through 9.0.105


### Description

<p>Authentication Bypass Using an Alternate Path or Channel vulnerability in Apache Tomcat.&nbsp; When using PreResources or PostResources mounted other than at the root of the web application, it was possible to access those resources via an unexpected path. That path was likely not to be protected by the same security constraints as the expected path, allowing those security constraints to be bypassed.</p><p>This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.7, from 10.1.0-M1 through 10.1.41, from 9.0.0.M1 through 9.0.105.</p><p>Users are recommended to upgrade to version 11.0.8, 10.1.42 or 9.0.106, which fix the issue.</p>

### References
* https://lists.apache.org/thread/m66cytbfrty9k7dc4cg6tl1czhsnbywk


### Credits
* Greg K (https://github.com/gregk4sec) (finder)
