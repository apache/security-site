---
title: Apache Shiro security advisories
description: Security information for Apache Shiro
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Shiro? Send your report to the [Apache Shiro Security Team](mailto:security@shiro.apache.org?subject=Shiro).

You can read more about the security policy on:

- [Apache Shiro security model](https://shiro.apache.org/security-reports.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Remember-me cookie isn't checked for expiry on the server ## { #CVE-2026-56130 }

CVE-2026-56130 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-56130) [\[CVE json\]](./CVE-2026-56130.cve.json) [\[OSV json\]](./CVE-2026-56130.osv.json)



_Last updated: 2026-06-25T08:44:28.652Z_

### Affected

* Apache Shiro from 1.2.4 through 2.99.99
* Apache Shiro from 3.0.0-alpha-0 through 3.0.0-alpha-1


### Description

<p>"Remember me" cookie age is not verified on the server. This potentially allows an attacker to intercept a valid cookie and reuse it indefinitely, even after the configured expiration time has passed.<br>This issue affects all Apache Shiro versions from 1.2.4 through 2.x, and 3.0.0-alpha-1, only when RememberMe functionality is enabled.<br></p><p>Upgrade to version 3.0.0 or later, which fixes the issue.<br></p>

### References
* https://lists.apache.org/thread/9k9b3bmlq516ylvf7cdp3dlrtdtmxbmo


### Credits
* Richard Bradley (finder)
* Lenny Primak <lenny@flowlogix.com> (remediation developer)


## Authentication bypass in Guice-Web integration ## { #CVE-2026-56091 }

CVE-2026-56091 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-56091) [\[CVE json\]](./CVE-2026-56091.cve.json) [\[OSV json\]](./CVE-2026-56091.osv.json)



_Last updated: 2026-06-25T08:45:18.079Z_

### Affected

* Apache Shiro through 2.99.99
* Apache Shiro from 3.0.0-alpha-0 through 3.0.0-alpha-1


### Description

When using Apache Shiro with the shiro-guice module in a web servlet context, a specially crafted HTTP request may cause an authentication bypass.<br>This vulnerability is similar to <a target="_blank" rel="nofollow" href="https://www.cve.org/CVERecord?id=CVE-2020-1957[CVE-2020-1957">https://www.cve.org/CVERecord?id=CVE-2020-1957</a>, except that it affects the `shiro-guice` module instead of the `shiro-spring` module.<br><br>This issue affects all Apache Shiro versions through 2.x, and 3.0.0-alpha-1 only when using `shiro-guice` module in a web servlet context.<br><br>Upgrade to version 3.0.0 or later, which fixes the issue.<br>

### References
* https://lists.apache.org/thread/onmtxmy2qonbpx7xlw3o34x8sctv47r7


### Credits
* LocalHost <localhost.detect@gmail.com> (finder)
* Lenny Primak <lenny@flowlogix.com> (remediation developer)


## LDAP DN Injection in DefaultLdapRealm ## { #CVE-2026-49268 }

CVE-2026-49268 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49268) [\[CVE json\]](./CVE-2026-49268.cve.json) [\[OSV json\]](./CVE-2026-49268.osv.json)



_Last updated: 2026-06-17T13:07:43.325Z_

### Affected

* Apache Shiro through 2.2.0
* Apache Shiro from 3.0.0-alpha-0 through 3.0.0-alpha-1


### Description

A remote attacker can inject LDAP special characters into the Distinguished Name (DN) construction in DefaultLdapRealm class. User-supplied username input is directly concatenated into the LDAP DN template without any escaping of RFC 2253 special characters. This allows an attacker to manipulate the DN structure used for LDAP bind authentication, potentially bypassing authentication or impersonating other users.<br><br>This issue affects all Apache Shiro versions through 2.2.0, and 3.0.0-alpha-1 when using&nbsp;<span style="background-color: rgb(239, 239, 239);">DefaultLdapRealm</span><br>Upgrade to Apache Shiro 2.2.1 or 3.0.0-alpha-2 or later, which fixes the issue.

### References
* https://lists.apache.org/thread/svszql3od8td7hn6conyj2oq70v53b5s


### Credits
* zhaokaifei (reporter) - ChinaTelecom (finder)
* Lenny Primak <lenny@flowlogix.com> (remediation developer)


## Jakarta EE open redirect via untrusted Referer in post-login redirect flow ## { #CVE-2026-48589 }

CVE-2026-48589 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48589) [\[CVE json\]](./CVE-2026-48589.cve.json) [\[OSV json\]](./CVE-2026-48589.osv.json)



_Last updated: 2026-05-25T20:20:09.531Z_

### Affected

* Apache Shiro from 2.0.0-alpha-0 through 2.2.0
* Apache Shiro from 3.0.0-alpha-0 through 3.0.0-alpha-1


### Description

<span style="background-color: rgb(255, 255, 255);">Apache Shiro’s Jakarta EE module used the HTTP Referer header in certain cases to issue redirect after a user login.<br>In affected versions, insufficient validation of this client-controlled value could allow an attacker to influence the redirect target in applications using the Jakarta EE module.<br>This issue affects Apache Shiro from 2.0-alpha to 2.2.0, and 3.0.0-alpha-1, only when using shiro-jakarta-ee integration module.</span><br>

### References
* https://shiro.apache.org/security-reports.html#cve_2026_48589


### Credits
* Bartlomiej Dmitruk <bartek@striga.ai> (finder)
* Lenny Primak <lenny@flowlogix.com> (remediation developer)


## Open redirect and SSRF (requires valid credentials) ## { #CVE-2026-44598 }

CVE-2026-44598 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44598) [\[CVE json\]](./CVE-2026-44598.cve.json) [\[OSV json\]](./CVE-2026-44598.osv.json)



_Last updated: 2026-05-25T20:19:50.656Z_

### Affected

* Apache Shiro Jakarta EE module from 2.0.0-alpha-0 through 2.1.0
* Apache Shiro Jakarta EE module from 3.0.0-alpha-0 through 3.0.0-alpha-1


### Description

<p>With valid login credentials, URL Redirection to Untrusted Site ('Open Redirect'), Server-Side Request Forgery (SSRF) vulnerability in Apache Shiro.<br></p><p></p><p>This issue affects Apache Shiro from 2.0-alpha to 2.1.0, and 3.0.0-alpha-1,&nbsp;<span style="background-color: rgb(255, 255, 255);">only w</span><span style="background-color: rgb(255, 255, 255);">hen using shiro-jakarta-ee integration module.</span></p><p>Users are recommended to upgrade to version 2.1.1, or 3.0.0-alpha-2 or later, which fixes the issue by encrypting the cookie.</p><p>After successful login, Jakarta EE integration module uses shiroSavedRequest cookie to redirect to a particular web page after login.<br>This cookie was not validated, and can be forged to send a HTTP GET request from the server itself to an arbitrary URL from the cookie.</p>

### References
* https://shiro.apache.org/security-reports.html#cve_2026_44598


### Credits
* James Love <jameslove2k22@gmail.com> (finder)
* Lenny Primak <lenny@flowlogix.com> (remediation developer)


## Shiro's native session and rememberMe cookies do not have secure flag set by default ## { #CVE-2026-43828 }

CVE-2026-43828 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43828) [\[CVE json\]](./CVE-2026-43828.cve.json) [\[OSV json\]](./CVE-2026-43828.osv.json)



_Last updated: 2026-05-25T20:19:30.172Z_

### Affected

* Apache Shiro from 1.0 through 2.1.0
* Apache Shiro from 3.0.0-alpha-0 through 3.0.0-alpha-1


### Description

<p>Default configurations of Apache Shiro send sensitive cookies in HTTPS session without 'Secure' attribute.</p><p></p><p>This issue affects Apache Shiro from 1.0 to 2.1.0, and 3.0.0-alpha-1.</p><p>Users are recommended to upgrade to version 2.1.1, or 3.0.0-alpha-2 or later, which fixes the issue.</p>In the affected versions, Shiro-native session manager, as well as Remember-Me manager sends JSESSIONID and rememberMe cookies without 'secure' attribute by default.<p></p>

### References
* https://shiro.apache.org/security-reports.html#cve_2026_43828


### Credits
* Meteor_Kai <1318723916@qq.com> (finder)
* Lenny Primak <lenny@flowlogix.com> (remediation developer)


## Session fixation: new session is not created after login by default ## { #CVE-2026-43827 }

CVE-2026-43827 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43827) [\[CVE json\]](./CVE-2026-43827.cve.json) [\[OSV json\]](./CVE-2026-43827.osv.json)



_Last updated: 2026-05-25T20:19:09.384Z_

### Affected

* Apache Shiro from 1.0 through 2.1.0
* Apache Shiro from 3.0.0-alpha-0 through 3.0.0-alpha-1


### Description

<p><span style="background-color: rgb(255, 255, 255);">Default configurations of Apache Shiro have a s</span>ession fixation vulnerability.</p><p>This issue affects Apache Shiro from 1.0 to 2.1.0, and 3.0.0-alpha-1.</p><p>Users are recommended to upgrade to version 2.1.1, or 3.0.0-alpha-2 or later, which fixes the issue.</p>In the affected versions, when a session already exists, it is not invalidated upon successful login, nor is a new session being generated with a new ID.<br><br>

### References
* https://shiro.apache.org/security-reports.html#cve_2026_43827


### Credits
* Rasmus Moorats <xx@nns.ee> (finder)
* Lenny Primak <lenny@flowlogix.com> (remediation developer)


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

* Apache Shiro before 1.11.0 unaffected


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
