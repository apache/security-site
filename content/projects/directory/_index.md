---
title: Apache Directory security advisories
description: Security information for Apache Directory
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Directory? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## StartTLS and SASL confidentiality protection bypass ## { #CVE-2021-33900 }

CVE-2021-33900 [\[CVE json\]](./CVE-2021-33900.cve.json)

### Affected

* Apache Directory Studio from unspecified through 2.0.0.v20210213-M16


### Description

While investigating DIRSTUDIO-1219 it was noticed that configured StartTLS encryption was not applied when any SASL authentication mechanism (DIGEST-MD5, GSSAPI) was used. While investigating DIRSTUDIO-1220 it was noticed that any configured SASL confidentiality layer was not applied. This issue affects Apache Directory Studio version 2.0.0.v20210213-M16 and prior versions.

### References
* https://lists.apache.org/thread.html/rb1dbcc43a5b406e45d335343a1704f4233de613140a01929d102fdc9%40%3Cusers.directory.apache.org%3E


### Credits
* Apache Directory would like to thank Hugh Cole-Baker for reporting this issue.


## LDAP Injection Vulnerability in Apache Kerby ## { #CVE-2023-25613 }

CVE-2023-25613 [\[CVE json\]](./CVE-2023-25613.cve.json)

### Affected

* Apache Kerby before 2.0.3


### Description

An LDAP Injection vulnerability exists in the&nbsp;LdapIdentityBackend of Apache Kerby before 2.0.3.&nbsp;

### References
* https://lists.apache.org/thread/ynz3hhbbq6d980fzpncwbh5jd8mkyt5y


### Credits
* 4ra1n of Chaitin Tech (finder)
