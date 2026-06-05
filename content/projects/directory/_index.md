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

## LDAP client implementation does not verify if the server certificate matches the intended LDAP hostname ## { #CVE-2026-35563 }

CVE-2026-35563 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-35563) [\[CVE json\]](./CVE-2026-35563.cve.json) [\[OSV json\]](./CVE-2026-35563.osv.json)



_Last updated: 2026-06-01T07:38:34.650Z_

### Affected

* Apache Directory LDAP API from 2.0.0 through 2.1.7


### Description

It was identified that the LDAP client implementation in version 2.1.7 does not verify if the server certificate matches the intended LDAP 
hostname. While the underlying code validates the certificate chain 
against a trusted authority, the absence of endpoint identification 
allows a valid certificate issued for an entirely unrelated host to be 
improperly accepted. This oversight leaves the connection highly 
vulnerable to server impersonation and complete connection compromise.<div><br></div><div>The
 root cause of this vulnerability lies in the incomplete TLS server 
identity verification within the LDAP client implementation.</div><div><br></div><div>The attacker requires MITM capability on the network to exploit this vulnerability. This attacker must be able to present a certificate trusted by the client's configured trust store.</div><div><br></div><div>The hostname verification has been enforced in the new version of the LDAP API</div>

### References
* https://lists.apache.org/thread/5rc2nzqxp1m9wknyf93r8dnp46fhc1nn


### Credits
* Rafał Łykowski and Łukasz Kollbek of Qualtrics (finder)


## LDAP Injection Vulnerability in Apache Kerby ## { #CVE-2023-25613 }

CVE-2023-25613 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25613) [\[CVE json\]](./CVE-2023-25613.cve.json) [\[OSV json\]](./CVE-2023-25613.osv.json)



_Last updated: 2024-01-18T09:14:01.669Z_

### Affected

* Apache Kerby before 2.0.3


### Description

An LDAP Injection vulnerability exists in the&nbsp;LdapIdentityBackend of Apache Kerby before 2.0.3.&nbsp;

### References
* https://lists.apache.org/thread/ynz3hhbbq6d980fzpncwbh5jd8mkyt5y


### Credits
* 4ra1n of Chaitin Tech (finder)


## StartTLS and SASL confidentiality protection bypass ## { #CVE-2021-33900 }

CVE-2021-33900 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-33900) [\[CVE json\]](./CVE-2021-33900.cve.json) [\[OSV json\]](./CVE-2021-33900.osv.json)



_Last updated: 2021-07-26T07:00:11.196Z_

### Affected

* Apache Directory Studio from unspecified through 2.0.0.v20210213-M16


### Description

While investigating DIRSTUDIO-1219 it was noticed that configured StartTLS encryption was not applied when any SASL authentication mechanism (DIGEST-MD5, GSSAPI) was used. While investigating DIRSTUDIO-1220 it was noticed that any configured SASL confidentiality layer was not applied. This issue affects Apache Directory Studio version 2.0.0.v20210213-M16 and prior versions.

### References
* https://lists.apache.org/thread.html/rb1dbcc43a5b406e45d335343a1704f4233de613140a01929d102fdc9%40%3Cusers.directory.apache.org%3E


### Credits
* Apache Directory would like to thank Hugh Cole-Baker for reporting this issue.
