---
title: Apache Tomcat security advisories
description: Security information for Apache Tomcat
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Tomcat? You can read more about the projects' security policy on their [security page](https://tomcat.apache.org/security.html), and email your report to the  [Apache Tomcat Security Team](mailto:security@tomcat.apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Tomcat since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. It may also lack details found on the [project security page](https://tomcat.apache.org/security.html).

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

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


## Fix for CVE-2023-24998 is incomplete ## { #CVE-2023-28709 }

[CVE-2023-28709](./CVE-2023-28709.cve.json)

### Affected

* Apache Tomcat versions 11.0.0-M2 including 11.0.0-M410.1.5 including 10.1.79.0.71 including 9.0.738.5.85 including 8.5.87


### Description

<div><p>The fix for CVE-2023-24998 was incomplete for Apache Tomcat 11.0.0-M2 to 11.0.0-M4, 10.1.5 to 10.1.7, 9.0.71 to 9.0.73 and 8.5.85 to 8.5.87. If non-default HTTP       connector settings were used such that the maxParameterCount&nbsp;could be reached using query string parameters and a request was       submitted that supplied exactly maxParameterCount parameters&nbsp;<span style="background-color: var(--wht);">in the query string, the limit for uploaded request parts could be&nbsp;</span><span style="background-color: var(--wht);">bypassed with the potential for a denial of service to occur.</span></p></div><br>

## AJP response header mix-up ## { #CVE-2023-34981 }

[CVE-2023-34981](./CVE-2023-34981.cve.json)

### Affected

* Apache Tomcat versions 11.0.0-M510.1.89.0.748.5.88


### Description

A regression in the fix for bug 66512 in Apache Tomcat 11.0.0-M5, 10.1.8, 9.0.74 and 8.5.88 meant that, if a response did not include any HTTP headers no AJP SEND_HEADERS messare woudl be sent for the response which in turn meant that at least one AJP proxy (mod_proxy_ajp) would use the response headers from the previous request leading to an information leak.