---
title: Apache Portals security advisories
description: Security information for Apache Portals
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Portals? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Portals Jetspeed XSS, CSRF, SSRF, and XXE issues ## { #CVE-2022-32533 }

CVE-2022-32533 [\[CVE json\]](./CVE-2022-32533.cve.json) [\[OSV json\]](./CVE-2022-32533.osv.json)



_Last updated: 2022-07-06T09:38:32.582Z_

### Affected

* Apache Portals at Jetspeed 2.3.1


### Description

Apache Jetspeed-2 does not sufficiently filter untrusted user input by default leading to a number of issues including XSS, CSRF, XXE, and SSRF.  Setting the configuration option "xss.filter.post = true" may mitigate these issues.

NOTE: Apache Jetspeed is a dormant project of Apache Portals and no updates will be provided for this issue.

### References
* https://lists.apache.org/thread/d3g248pr03x8rvmh8p2t3xdlw0wn5dz2
* https://www.openwall.com/lists/oss-security/2022/07/06/1


### Credits
* Thanks to RunningSnail for reporting.


## XSS vulnerability in the MVCBean JSP portlet maven archetype ## { #CVE-2021-36739 }

CVE-2021-36739 [\[CVE json\]](./CVE-2021-36739.cve.json) [\[OSV json\]](./CVE-2021-36739.osv.json)



_Last updated: 2022-01-06T08:48:42.463Z_

### Affected

* Apache Portals at org.apache.portals.pluto.archetype:mvcbean-jsp-portlet-archetype 3.1.0


### Description

The "first name" and "last name" fields of the Apache Pluto 3.1.0 MVCBean JSP portlet maven archetype are vulnerable to Cross-Site Scripting (XSS) attacks.

### References
* https://lists.apache.org/thread/m5j87nn1lmvzp8b9lmh7gqq68g5lnb7p


## XSS vulnerability in the JSP version of the Apache Pluto Applicant MVCBean CDI portlet ## { #CVE-2021-36738 }

CVE-2021-36738 [\[CVE json\]](./CVE-2021-36738.cve.json) [\[OSV json\]](./CVE-2021-36738.osv.json)



_Last updated: 2022-01-06T08:48:04.239Z_

### Affected

* Apache Portals at org.apache.portals.pluto.demo:applicant-mvcbean-cdi-jsp-portlet 3.1.0


### Description

The input fields in the JSP version of the Apache Pluto Applicant MVCBean CDI portlet are vulnerable to Cross-Site Scripting (XSS) attacks. Users should migrate to version 3.1.1 of the applicant-mvcbean-cdi-jsp-portlet.war artifact

### References
* https://lists.apache.org/thread/11j19v1gjsk7o6o8nch1xrydow9b8lll


## XSS in V3 Demo Portlet ## { #CVE-2021-36737 }

CVE-2021-36737 [\[CVE json\]](./CVE-2021-36737.cve.json) [\[OSV json\]](./CVE-2021-36737.osv.json)



_Last updated: 2022-01-06T08:47:29.193Z_

### Affected

* Apache Portals at org.apache.portals.pluto:PortletV3Demo 3.0.0
* Apache Portals at org.apache.portals.pluto:PortletV3Demo 3.0.1
* Apache Portals at org.apache.portals.pluto.demo:v3-demo-portlet 3.1.0


### Description

The input fields of the Apache Pluto UrlTestPortlet are vulnerable to Cross-Site Scripting (XSS) attacks.  Users should migrate to version 3.1.1 of the v3-demo-portlet.war artifact

### References
* https://lists.apache.org/thread/x7kt47bf358x8sg9qg02zt0dmdrtow25


### Credits
* Thanks to Dhiraj Mishra for reporting.
