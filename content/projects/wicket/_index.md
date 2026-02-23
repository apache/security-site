---
title: Apache Wicket security advisories
description: Security information for Apache Wicket
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Wicket? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## An attacker can intentionally trigger a memory leak ## { #CVE-2024-53299 }

CVE-2024-53299 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-53299) [\[CVE json\]](./CVE-2024-53299.cve.json) [\[OSV json\]](./CVE-2024-53299.osv.json)



_Last updated: 2025-01-23T08:37:04.162Z_

### Affected

* Apache Wicket from 7.0.0 through 7.18.*
* Apache Wicket from 8.0.0-M1 through 8.16.*
* Apache Wicket from 9.0.0-M1 through 9.18.*
* Apache Wicket from 10.0.0-M1 through 10.2.*


### Description

The request handling in the core in Apache Wicket 7.0.0 on any platform allows an attacker to create a DOS via multiple requests to server resources.<br>Users are recommended to upgrade to versions 9.19.0 or 10.3.0, which fixes this issue.

### References
* https://lists.apache.org/thread/gyp2ht00c62827y0379lxh5dbx3hhho5


### Credits
* Pedro Santos (finder)


## Remote code execution via XSLT injection ## { #CVE-2024-36522 }

CVE-2024-36522 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-36522) [\[CVE json\]](./CVE-2024-36522.cve.json) [\[OSV json\]](./CVE-2024-36522.osv.json)



_Last updated: 2024-07-12T12:13:50.122Z_

### Affected

* Apache Wicket from 10.0.0-M1 through 10.0.0
* Apache Wicket from 9.0.0 through 9.17.0
* Apache Wicket from 8.0.0 through 8.15.0


### Description

The default configuration of XSLTResourceStream.java is vulnerable to remote code execution via XSLT injection when <span style="background-color: rgb(255, 255, 255);">processing input from an untrusted source without validation</span>.<br>Users are recommended to upgrade to versions 10.1.0, 9.18.0 or 8.16.0, which fix this issue.

### References
* https://lists.apache.org/thread/w613qh7yors840pbx00l1pq6wkl9jzkc


### Credits
* cigar (finder)


## Possible bypass of CSRF protection ## { #CVE-2024-27439 }

CVE-2024-27439 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-27439) [\[CVE json\]](./CVE-2024-27439.cve.json) [\[OSV json\]](./CVE-2024-27439.osv.json)



_Last updated: 2024-03-19T11:07:46.188Z_

### Affected

* Apache Wicket from 9.1.0 through 9.16.0
* Apache Wicket from 10.0.0-M1 before 10.0.0


### Description

An error in the evaluation of the fetch metadata headers could allow a bypass of the CSRF protection in Apache Wicket.<br><p>This issue affects Apache Wicket: from 9.1.0 through 9.16.0, and the milestone releases for the 10.0 series.<br>Apache Wicket 8.x does not support CSRF protection via the fetch metadata headers and as such is not affected.</p><p>Users are recommended to upgrade to version 9.17.0 or 10.0.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/o825rvjjtmz3qv21ps5k7m2w9193g1lo


### Credits
* Jo Theunis (finder)


## DNS proxy and possible amplification attack ## { #CVE-2021-23937 }

CVE-2021-23937 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-23937) [\[CVE json\]](./CVE-2021-23937.cve.json) [\[OSV json\]](./CVE-2021-23937.osv.json)



_Last updated: 2021-05-25T08:01:09.799Z_

### Affected

* Apache Wicket from Apache Wicket 9.x through 9.2.0
* Apache Wicket from Apache Wicket 8.x through 8.11.0
* Apache Wicket from Apache Wicket 7.x through 7.17.0
* Apache Wicket from 6.2.0 before Apache Wicket 6.x*


### Description

A DNS proxy and possible amplification attack vulnerability in WebClientInfo of Apache Wicket allows an attacker to trigger arbitrary DNS lookups from the server when the X-Forwarded-For header is not properly sanitized. This DNS lookup can be engineered to overload an internal DNS server or to slow down request processing of the Apache Wicket application causing a possible denial of service on either the internal infrastructure or the web application itself.

This issue affects Apache Wicket Apache Wicket 9.x version 9.2.0 and prior versions; Apache Wicket 8.x version 8.11.0 and prior versions; Apache Wicket 7.x version 7.17.0 and prior versions and Apache Wicket 6.x version 6.2.0 and later versions.

### References
* https://lists.apache.org/thread.html/rc2ef22f90793e158cef65a7e370cdbca023c499d1403d65feeca870d%40%3Cusers.wicket.apache.org%3E


### Credits
* Apache Wicket would like to thank Jonathan Juursema from Topicus.Healthcare for reporting this issue.
