---
title: Apache Tomcat security advisories
description: Security information for Apache Tomcat
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Tomcat? You can read more about the projects' security policy on their [security page](https://tomcat.apache.org/security.html), and email your report to the  [Apache Tomcat Security Team](mailto:security@tomcat.apache.org).

# Advisories

## JsonErrorReportValve escaping ## { #CVE-2022-45143 }

[CVE-2022-45143](./CVE-2022-45143.cve.json)

### Affected

* Apache Tomcat versions 10.1.0-M1 including 10.1.19.0.40 including 9.0.688.5.83


### Description

The JsonErrorReportValve in Apache Tomcat 8.5.83, 9.0.40 to 9.0.68 and 10.1.0-M1 to 10.1.1 did not escape the type, message or description values. In some circumstances these are constructed from user provided data and it was therefore possible for users to supply values that invalidated or manipulated the JSON output.

## JSESSIONID Cookie missing secure attribute in some configurations ## { #CVE-2023-28708 }

[CVE-2023-28708](./CVE-2023-28708.cve.json)

### Affected

* Apache Tomcat versions 11.0.0-M1 including 11.0.0-M210.1.0-M1 including 10.1.59.0.0-M1 including 9.0.718.5.0 including 8.5.85


### Description

<div>
<div>
<p>When using the RemoteIpFilter with requests received from a    reverse proxy via HTTP that include the X-Forwarded-Proto    header set to https, session cookies created by Apache Tomcat 11.0.0-M1 to 11.0.0.-M2, 10.1.0-M1 to 10.1.5, 9.0.0-M1 to 9.0.71 and 8.5.0 to 8.5.85 did not&nbsp;include the secure attribute. This could result in the user agent&nbsp;<span style="background-color: var(--wht);">transmitting the session cookie over an insecure channel.</span></p></div>
</div>
