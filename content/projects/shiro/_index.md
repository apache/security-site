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

## Apache Shiro before 1.8.0, when using Apache Shiro with Spring Boot, a specially crafted HTTP request may cause an authentication bypass ## { #CVE-2021-41303 }

CVE-2021-41303 [\[CVE json\]](./CVE-2021-41303.cve.json)

### Affected

* Apache Shiro from Apache Shiro before 1.8.0


### Description

Apache Shiro before 1.8.0, when using Apache Shiro with Spring Boot, a specially crafted HTTP request may cause an authentication bypass.

Users should update to Apache Shiro 1.8.0.

### References
* https://lists.apache.org/thread.html/re470be1ffea44bca28ccb0e67a4cf5d744e2d2b981d00fdbbf5abc13%40%3Cannounce.shiro.apache.org%3E


### Credits
* Apache Shiro would like to thank tsug0d for reporting this issue.


## Authentication Bypass Vulnerability ## { #CVE-2022-32532 }

CVE-2022-32532 [\[CVE json\]](./CVE-2022-32532.cve.json)

### Affected

* Apache Shiro at Before 1.9.1


### Description

Apache Shiro before 1.9.1, A RegexRequestMatcher can be misconfigured to be bypassed on some servlet containers. Applications using RegExPatternMatcher with `.` in the regular expression are possibly vulnerable to an authorization bypass.

### References
* https://lists.apache.org/thread/y8260dw8vbm99oq7zv6y3mzn5ovk90xh


### Credits
* Apache Shiro would like the thank 4ra1n for reporting this issue.


## Authentication Bypass Vulnerability in Shiro when forwarding or including via RequestDispatcher ## { #CVE-2022-40664 }

CVE-2022-40664 [\[CVE json\]](./CVE-2022-40664.cve.json)

### Affected

* Apache Shiro from Apache Shiro before 1.10.0


### Description

Apache Shiro before 1.10.0, Authentication Bypass Vulnerability in Shiro when forwarding or including via RequestDispatcher.

### References
* https://lists.apache.org/thread/loc2ktxng32xpy7lfwxto13k4lvnhjwg


### Credits
* Apache Shiro would like to thank Y4tacker for reporting this issue


## Apache Shiro before 1.11.0, when used with Spring Boot 2.6+, may allow authentication bypass through a specially crafted HTTP request ## { #CVE-2023-22602 }

CVE-2023-22602 [\[CVE json\]](./CVE-2023-22602.cve.json)

### Affected

* Apache Shiro before 1.11.0


### Description

<span style="background-color: rgb(255, 255, 255);">When using Apache Shiro before 1.11.0 together with Spring Boot 2.6+, a specially crafted HTTP request may cause an authentication bypass.<br><br></span>The authentication bypass occurs when Shiro and Spring Boot are using different pattern-matching techniques. Both Shiro and Spring Boot &lt; 2.6 default to Ant style pattern matching.<br><p>Mitigation: Update to Apache Shiro 1.11.0, or set the following Spring Boot configuration value:  `spring.mvc.pathmatch.matching-strategy = ant_path_matcher`<br></p>

### References
* https://lists.apache.org/thread/dzj0k2smpzzgj6g666hrbrgsrlf9yhkl


### Credits
* v3ged0ge and Adamytd (finder)


## Apache Shiro before 1.12.0, or 2.0.0-alpha-3, may be susceptible to a path traversal attack when used together with APIs or other web frameworks that route requests based on non-normalized requests. ## { #CVE-2023-34478 }

CVE-2023-34478 [\[CVE json\]](./CVE-2023-34478.cve.json)

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
