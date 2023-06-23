---
title: Apache Shiro security advisories
description: Security information for Apache Shiro
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Shiro? You can read more about the projects' security policy on their [security page](https://shiro.apache.org/security-reports.html), and email your report to the  [Apache Shiro Security Team](mailto:security@shiro.apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Shiro since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. It may also lack details found on the [project security page](https://shiro.apache.org/security-reports.html).

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Apache Shiro before 1.11.0, when used with Spring Boot 2.6+, may allow authentication bypass through a specially crafted HTTP request ## { #CVE-2023-22602 }

[CVE-2023-22602](./CVE-2023-22602.cve.json)

### Affected

* Apache Shiro before 1.11.0


### Description

<span style="background-color: rgb(255, 255, 255);">When using Apache Shiro before 1.11.0 together with Spring Boot 2.6+, a specially crafted HTTP request may cause an authentication bypass.<br><br></span>The authentication bypass occurs when Shiro and Spring Boot are using different pattern-matching techniques. Both Shiro and Spring Boot &lt; 2.6 default to Ant style pattern matching.<br><p>Mitigation: Update to Apache Shiro 1.11.0, or set the following Spring Boot configuration value:  `spring.mvc.pathmatch.matching-strategy = ant_path_matcher`<br></p>