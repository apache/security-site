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

## DNS proxy and possible amplification attack ## { #CVE-2021-23937 }

CVE-2021-23937 [\[CVE json\]](./CVE-2021-23937.cve.json)

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
