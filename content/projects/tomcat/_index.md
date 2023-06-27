---
title: Apache Tomcat security advisories
description: Security information for Apache Tomcat
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Tomcat? You can read more about the projects' security policy on their [security page](https://tomcat.apache.org/security.html), and email your report to the  [Apache Tomcat Security Team](mailto:security@tomcat.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://tomcat.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## JsonErrorReportValve escaping ## { #CVE-2022-45143 }

CVE-2022-45143 [\[CVE json\]](./CVE-2022-45143.cve.json)

### Affected

* Apache Tomcat from 10.1.0-M1 through 10.1.1
* Apache Tomcat from 9.0.40 through 9.0.68
* Apache Tomcat at 8.5.83


### Description

The JsonErrorReportValve in Apache Tomcat 8.5.83, 9.0.40 to 9.0.68 and 10.1.0-M1 to 10.1.1 did not escape the type, message or description values. In some circumstances these are constructed from user provided data and it was therefore possible for users to supply values that invalidated or manipulated the JSON output.

### References
* https://lists.apache.org/thread/yqkd183xrw3wqvnpcg3osbcryq85fkzj


## JSESSIONID Cookie missing secure attribute in some configurations ## { #CVE-2023-28708 }

CVE-2023-28708 [\[CVE json\]](./CVE-2023-28708.cve.json)

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

CVE-2023-28709 [\[CVE json\]](./CVE-2023-28709.cve.json)

### Affected

* Apache Tomcat from 11.0.0-M2 through 11.0.0-M4
* Apache Tomcat from 10.1.5 through 10.1.7
* Apache Tomcat from 9.0.71 through 9.0.73
* Apache Tomcat from 8.5.85 through 8.5.87


### Description

<div><p>The fix for CVE-2023-24998 was incomplete for Apache Tomcat 11.0.0-M2 to 11.0.0-M4, 10.1.5 to 10.1.7, 9.0.71 to 9.0.73 and 8.5.85 to 8.5.87. If non-default HTTP       connector settings were used such that the maxParameterCount&nbsp;could be reached using query string parameters and a request was       submitted that supplied exactly maxParameterCount parameters&nbsp;<span style="background-color: var(--wht);">in the query string, the limit for uploaded request parts could be&nbsp;</span><span style="background-color: var(--wht);">bypassed with the potential for a denial of service to occur.</span></p></div><br>

### References
* https://lists.apache.org/thread/7wvxonzwb7k9hx9jt3q33cmy7j97jo3j


## AJP response header mix-up ## { #CVE-2023-34981 }

CVE-2023-34981 [\[CVE json\]](./CVE-2023-34981.cve.json)

### Affected

* Apache Tomcat at 11.0.0-M5
* Apache Tomcat at 10.1.8
* Apache Tomcat at 9.0.74
* Apache Tomcat at 8.5.88


### Description

A regression in the fix for bug 66512 in Apache Tomcat 11.0.0-M5, 10.1.8, 9.0.74 and 8.5.88 meant that, if a response did not include any HTTP headers no AJP SEND_HEADERS messare woudl be sent for the response which in turn meant that at least one AJP proxy (mod_proxy_ajp) would use the response headers from the previous request leading to an information leak.

### References
* https://lists.apache.org/thread/j1ksjh9m9gx1q60rtk1sbzmxhvj5h5qz
