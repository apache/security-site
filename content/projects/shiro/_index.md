---
title: Apache Shiro security advisories
description: Security information for Apache Shiro
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Shiro? You can read more about the projects' security policy on their [security page](https://shiro.apache.org/security-reports.html), and email your report to the [Apache Shiro Security Team](mailto:security@shiro.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://shiro.apache.org/security-reports.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Auth bypass when accessing static files only on case-insensitive filesystems ## { #CVE-2026-23903 }

CVE-2026-23903 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-23903) [\[CVE json\]](./CVE-2026-23903.cve.json) [\[OSV json\]](./CVE-2026-23903.osv.json)



_Last updated: 2026-02-09T09:26:19.996Z_

### Affected

* Apache Shiro before 2.0.7


### Description

<p>Authentication Bypass by Alternate Name vulnerability in Apache Shiro.</p><p>This issue affects Apache Shiro: before 2.0.7.</p><p>Users are recommended to upgrade to version 2.0.7, which fixes the issue.</p>The issue only effects static files. If static files are served from a case-insensitive filesystem,<br>such as default macOS setup, static files may be accessed by varying the case of the filename in the request.<br>If only lower-case (common default) filters are present in Shiro, they may be bypassed this way.<br><br>Shiro 2.0.7 and later has a new parameters to remediate this issue<br>shiro.ini: <span style="background-color: rgba(129, 139, 152, 0.12);">filterChainResolver.caseInsensitive = true<br></span>application.propertie: shiro<span style="background-color: rgba(129, 139, 152, 0.12);">.caseInsensitive=true<br></span><br>Shiro 3.0.0 and later (upcoming) makes this the default.

### References
* https://lists.apache.org/thread/5jjf0hnjcol58z2m5y255c7scz1lnp8k


### Credits
* Jesse Yang (finder)
* Lenny Pimak (remediation developer)


## Brute force attack possible to determine valid user names ## { #CVE-2026-23901 }

CVE-2026-23901 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-23901) [\[CVE json\]](./CVE-2026-23901.cve.json) [\[OSV json\]](./CVE-2026-23901.osv.json)



_Last updated: 2026-02-10T09:25:49.952Z_

### Affected

* Apache Shiro before 2.0.7


### Description

<p>Observable Timing Discrepancy vulnerability in Apache Shiro.</p><p>This issue affects Apache Shiro: from 1.*, 2.* before 2.0.7.</p><p>Users are recommended to upgrade to version 2.0.7 or later, which fixes the issue.</p>Prior to Shiro 2.0.7, code paths for non-existent vs. existing users are different enough,<br>that a brute-force attack may be able to tell, by timing the requests only, determine if<br>the request failed because of a non-existent user vs. wrong password.<br><br>The most likely attack vector is a local attack only.<br>Shiro security model&nbsp;<a target="_blank" rel="nofollow" href="https://shiro.apache.org/security-model.html#username_enumeration">https://shiro.apache.org/security-model.html#username_enumeration</a>&nbsp;discusses this as well.<br><br>Typically, brute force attack can be mitigated at the infrastructure level.

### References
* https://lists.apache.org/thread/mm1jct9b86jvnh3y44tj22xvjtx3xhhh


### Credits
* 4ra1n (finder)
* Y4tacker (finder)
* lprimak (remediation developer)


## URL Redirection to Untrusted Site ('Open Redirect') vulnerability in FORM authentication feature Apache Shiro. ## { #CVE-2023-46750 }

CVE-2023-46750 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-46750) [\[CVE json\]](./CVE-2023-46750.cve.json) [\[OSV json\]](./CVE-2023-46750.osv.json)



_Last updated: 2023-12-14T08:15:56.341Z_

### Affected

* Apache Shiro before 1.13.0
* Apache Shiro from 2.0.0-alpha-1 before 2.0.0-alpha-4


### Description

<span style="background-color: rgb(255, 255, 255);">URL Redirection to Untrusted Site ('Open Redirect') vulnerability when "form" authentication is used in Apache Shiro.<br><span style="background-color: rgb(255, 255, 255);">Mitigation: Update to Apache Shiro 1.13.0+ or 2.0.0-alpha-4+.</span></span><br>

### References
* https://lists.apache.org/thread/hoc9zdyzmmrfj1zhctsvvtx844tcq6w9


### Credits
* Claudio Villella (finder)


## Apache Shiro before 1.13.0 or 2.0.0-alpha-4, may be susceptible to a path traversal attack that results in an authentication bypass when used together with path rewriting  ## { #CVE-2023-46749 }

CVE-2023-46749 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-46749) [\[CVE json\]](./CVE-2023-46749.cve.json) [\[OSV json\]](./CVE-2023-46749.osv.json)



_Last updated: 2024-01-19T18:12:43.905Z_

### Affected

* Apache Shiro before 1.13.0
* Apache Shiro from 2.0.0-alpha-1 before 2.0.0-alpha-4


### Description

Apache Shiro before 1.13.0 or 2.0.0-alpha-4, may be susceptible to a path traversal attack that results in an authentication bypass when used together with path rewriting <br><br><span style="background-color: rgb(255, 255, 255);">Mitigation: Update to Apache Shiro 1.13.0+ or 2.0.0-alpha-4+, or ensure `blockSemicolon` is enabled (this is the default).<br></span><br>

### References
* https://lists.apache.org/thread/mdv7ftz7k4488rzloxo2fb0p9shnp9wm


## Apache Shiro before 1.12.0, or 2.0.0-alpha-3, may be susceptible to a path traversal attack when used together with APIs or other web frameworks that route requests based on non-normalized requests. ## { #CVE-2023-34478 }

CVE-2023-34478 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-34478) [\[CVE json\]](./CVE-2023-34478.cve.json) [\[OSV json\]](./CVE-2023-34478.osv.json)



_Last updated: 2023-07-24T18:24:43.013Z_

### Affected

* Apache Shiro before 1.12.0
* Apache Shiro before 2.0.0-alpha-3


### Description

Apache Shiro, before 1.12.0 or 2.0.0-alpha-3, <span style="background-color: rgb(255, 255, 255);">may be susceptible to a path traversal attack that results in an authentication bypass when used together with APIs or other web frameworks that route requests based on non-normalized requests.<br><br><strong>Mitigation:</strong><span style="background-color: rgb(255, 255, 255);">&nbsp;Update to Apache Shiro 1.12.0+ or 2.0.0-alpha-3+</span></span><br>

### References
* https://lists.apache.org/thread/mbv26onkgw9o35rldh7vmq11wpv2t2qk


### Credits
* tkswifty (finder)
* Ha1c9on (finder)


## Apache Shiro before 1.11.0, when used with Spring Boot 2.6+, may allow authentication bypass through a specially crafted HTTP request ## { #CVE-2023-22602 }

CVE-2023-22602 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-22602) [\[CVE json\]](./CVE-2023-22602.cve.json)

_Last updated: 2023-01-14T09:33:37.695Z_

### Affected

* Apache Shiro before 1.11.0


### Description

<span style="background-color: rgb(255, 255, 255);">When using Apache Shiro before 1.11.0 together with Spring Boot 2.6+, a specially crafted HTTP request may cause an authentication bypass.<br><br></span>The authentication bypass occurs when Shiro and Spring Boot are using different pattern-matching techniques. Both Shiro and Spring Boot &lt; 2.6 default to Ant style pattern matching.<br><p>Mitigation: Update to Apache Shiro 1.11.0, or set the following Spring Boot configuration value:  `spring.mvc.pathmatch.matching-strategy = ant_path_matcher`<br></p>

### References
* https://lists.apache.org/thread/dzj0k2smpzzgj6g666hrbrgsrlf9yhkl


### Credits
* v3ged0ge and Adamytd (finder)


## Authentication Bypass Vulnerability in Shiro when forwarding or including via RequestDispatcher ## { #CVE-2022-40664 }

CVE-2022-40664 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-40664) [\[CVE json\]](./CVE-2022-40664.cve.json) [\[OSV json\]](./CVE-2022-40664.osv.json)



_Last updated: 2022-10-12T07:07:53.344Z_

### Affected

* Apache Shiro from Apache Shiro before 1.10.0


### Description

Apache Shiro before 1.10.0, Authentication Bypass Vulnerability in Shiro when forwarding or including via RequestDispatcher.

### References
* https://lists.apache.org/thread/loc2ktxng32xpy7lfwxto13k4lvnhjwg


### Credits
* Apache Shiro would like to thank Y4tacker for reporting this issue


## Authentication Bypass Vulnerability ## { #CVE-2022-32532 }

CVE-2022-32532 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-32532) [\[CVE json\]](./CVE-2022-32532.cve.json) [\[OSV json\]](./CVE-2022-32532.osv.json)



_Last updated: 2022-06-28T23:13:16.050Z_

### Affected

* Apache Shiro at Before 1.9.1


### Description

Apache Shiro before 1.9.1, A RegexRequestMatcher can be misconfigured to be bypassed on some servlet containers. Applications using RegExPatternMatcher with `.` in the regular expression are possibly vulnerable to an authorization bypass.

### References
* https://lists.apache.org/thread/y8260dw8vbm99oq7zv6y3mzn5ovk90xh


### Credits
* Apache Shiro would like the thank 4ra1n for reporting this issue.


## Apache Shiro before 1.8.0, when using Apache Shiro with Spring Boot, a specially crafted HTTP request may cause an authentication bypass ## { #CVE-2021-41303 }

CVE-2021-41303 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-41303) [\[CVE json\]](./CVE-2021-41303.cve.json) [\[OSV json\]](./CVE-2021-41303.osv.json)



_Last updated: 2021-09-17T08:17:09.454Z_

### Affected

* Apache Shiro from Apache Shiro before 1.8.0


### Description

Apache Shiro before 1.8.0, when using Apache Shiro with Spring Boot, a specially crafted HTTP request may cause an authentication bypass.

Users should update to Apache Shiro 1.8.0.

### References
* https://lists.apache.org/thread.html/re470be1ffea44bca28ccb0e67a4cf5d744e2d2b981d00fdbbf5abc13%40%3Cannounce.shiro.apache.org%3E


### Credits
* Apache Shiro would like to thank tsug0d for reporting this issue.
