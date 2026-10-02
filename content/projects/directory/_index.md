---
title: Apache Directory security advisories
description: Security information for Apache Directory
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Directory? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Directory).

You can read more about the security policy on:

- [Apache Directory security model](https://github.com/apache/directory-server/blob/master/THREAT_MODEL.md)
- [Apache Directory SCIMple security model](https://github.com/apache/directory-scimple/blob/develop/THREAT_MODEL.md)
- [Apache Fortress Web security model](https://github.com/apache/directory-fortress-commander/blob/master/README-SECURITY-MODEL.md)
- [Apache Fortress Rest security model](https://github.com/apache/directory-fortress-enmasse/blob/master/README-SECURITY-MODEL.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security pages linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Kerberos Pre-Authentication Bypass ## { #CVE-2026-57915 }

CVE-2026-57915 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57915) [\[CVE json\]](./CVE-2026-57915.cve.json) [\[OSV json\]](./CVE-2026-57915.osv.json)



_Last updated: 2026-06-26T12:09:53.178Z_

### Affected

* Apache Kerby before 2.1.2


### Description

It is possible to bypass the Kerberos pre-authentication check in Apache Kerby by sending a PA-DATA with an unrecognized or unsupported type. Users are recommended to upgrade to version 2.1.2, which fixes this issue.

### References
* https://lists.apache.org/thread/1y3glgh3kzwoxo5m2lq504cjlh1dsrfh


## StackOverflow on parsing deeply nested ASN1 structures ## { #CVE-2026-57914 }

CVE-2026-57914 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57914) [\[CVE json\]](./CVE-2026-57914.cve.json) [\[OSV json\]](./CVE-2026-57914.osv.json)



_Last updated: 2026-06-26T11:28:25.784Z_

### Affected

* Apache Kerby before 2.1.2


### Description

By sending a deeply nested ASN1 structure to a Apache Kerby client or service, it's possible to trigger a StackOverFlow Exception which can lead to denial of service issues. Users are recommended to upgrade to version 2.1.2, which fixes this issue.

### References
* https://lists.apache.org/thread/w98h2q8wz0bq97vhz4vf55hqomcb2j1m


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


## Denial of service via crafted telephone number values ## { #CVE-2026-103885 }

CVE-2026-103885 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-103885) [\[CVE json\]](./CVE-2026-103885.cve.json) [\[OSV json\]](./CVE-2026-103885.osv.json)



_Last updated: 2026-10-02T10:09:46.664Z_

### Affected

* Apache Directory LDAP API from 2.1.0 before 2.1.9


### Description

<p><span><span>Asymmetric Resource Consumption&nbsp;</span></span>vulnerability in Apache Directory LDAP API.</p><p>A LDAP server using the LDAP API (like Apache DS)&nbsp;may consume 100% of a CPU core indefinitely&nbsp;when processing some badly crafted Telephone Numbers.</p><p>This issue affects Apache Directory LDAP API: from 2.1.0 before 2.1.9.</p><p>Users are recommended to upgrade to version 2.1.9, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/wjt9p1l123v6b3zd5dg41f8lfrgy5vg9


### Credits
* Claude Security (tool)
* The Apache Software Foundation (finder)


## Denial of service via excessive bcrypt cost factor in stored passwords ## { #CVE-2026-103880 }

CVE-2026-103880 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-103880) [\[CVE json\]](./CVE-2026-103880.cve.json) [\[OSV json\]](./CVE-2026-103880.osv.json)



_Last updated: 2026-10-02T10:03:42.918Z_

### Affected

* Apache Directory LDAP API from 2.1.0 before 2.1.9


### Description

<p>Asymmetric Resource Consumption&nbsp;vulnerability in Apache Directory LDAP API.</p><p>Storing a password using the bcrypt algorithm with a high force like 30 in a LDAP server that supports this algorithm will cause the server CPU to&nbsp; run for hours checking the credentials. A bounded cost should be enforced to avoid a server DOS.</p><p>This issue affects Apache Directory LDAP API: from 2.1.0 before 2.1.9.</p><p>Users are recommended to upgrade to version 2.1.9, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/39q63m54v9go6xj7pqj7q18c3szn9go4


### Credits
* Claude Security (tool)
* The Apache Software Foundation (finder)


## Injection of plaintext responses during StartTLS ## { #CVE-2026-103878 }

CVE-2026-103878 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-103878) [\[CVE json\]](./CVE-2026-103878.cve.json) [\[OSV json\]](./CVE-2026-103878.osv.json)



_Last updated: 2026-10-02T10:02:31.520Z_

### Affected

* Apache Directory LDAP API from 2.1.0 before 2.1.9


### Description

<p>Cleartext transmission of sensitive information&nbsp;vulnerability in Apache Directory LDAP API.</p><p>A StartTLS extended operation started after a Search request has been sent can lead to receive data in plain text before the TLS Handshake has been completed.</p><p>This issue affects Apache Directory LDAP API: from 2.1.0 before 2.1.9.</p><p>Users are recommended to upgrade to version 2.1.9, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/d98f9w01nd3zmkwrr21y0l9kdr9jpty9


### Credits
* Claude Security (tool)
* The Apache Software Foundation (finder)


## Unsafe loading of Java code from LDAP schema elements ## { #CVE-2026-103877 }

CVE-2026-103877 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-103877) [\[CVE json\]](./CVE-2026-103877.cve.json) [\[OSV json\]](./CVE-2026-103877.osv.json)



_Last updated: 2026-10-02T10:08:30.840Z_

### Affected

* Apache Directory LDAP API from 2.1.0 before 2.1.9


### Description

<pre>Deserialization of Untrusted Data <span>vulnerability in Apache Directory LDAP API.</span></pre><p>A rogue/compromised LDAP server (or pre-TLS MITM) can answer a client's loadSchema() subschema search with a schema object that contains a serialized Java class, allowing some potential RCE.&nbsp;</p><p>This issue affects Apache Directory LDAP API: from 2.1.0 before 2.1.9.</p><p>Users are recommended to upgrade to version 2.1.9, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/sys8l881blqfgoc3o724jl32bmjl8pvw


### Credits
* Claude Security (tool)
* The Apache Software Foundation (finder)


## A unbound client can send a deeply nested search filter that overflows the stack in the server's decoder ## { #CVE-2026-103552 }

CVE-2026-103552 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-103552) [\[CVE json\]](./CVE-2026-103552.cve.json) [\[OSV json\]](./CVE-2026-103552.osv.json)



_Last updated: 2026-10-02T09:47:58.183Z_

### Affected

* Apache Directory LDAP API from 1.2.0 before 1.2.9


### Description

<p>Stack Overflow vulnerability in Apache Directory LDAP API.</p><p><span>Before binding, a client can send a deeply nested search filter </span><span>that overflows the stack in the server's decoder.</span></p><p>This issue affects Apache Directory LDAP API: from 1.2.0 before 1.2.9.</p><p>Users are recommended to upgrade to version 1.2.9, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/fn3bwknn57266hx66w9vv6b4k8rfwcx7


### Credits
* Claude Security (tool)
* The Apache Software Foundation (finder)


## Denial of service via excessive memory allocation in BER decode ## { #CVE-2026-102731 }

CVE-2026-102731 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-102731) [\[CVE json\]](./CVE-2026-102731.cve.json) [\[OSV json\]](./CVE-2026-102731.osv.json)



_Last updated: 2026-10-02T09:21:56.550Z_

### Affected

* Apache Directory LDAP API from 1.2.0 before 1.2.9


### Description

<p>Memory allocation with excessive size value vulnerability in Apache Directory LDAP API.</p><p>A malicious peer (or a MITM) can send a small BER-encoded response causing a large memory allocation before any data is received. This can lead to an OutOfMemoryError and denial of service.</p><p>The client JVM OOMs (OutOfMemoryError bypasses the DecoderException handlers) or pins the large allocation per connection while the attacker stalls.</p><p>A handful of connections exhausts any heap. The same bytes from an unauthenticated pre-bind client hit any embedding server that did not set MAX_PDU_SIZE_ATTR.</p><p>This issue affects Apache Directory LDAP API: from 1.2.0 before 1.2.9.</p><p>Users are recommended to upgrade to version 1.2.9, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/b8kg8881pc0v8lp59w0fcfrs69wjbqvd


### Credits
* Claude Security (tool)
* The Apache Software Foundation (finder)


## LDAP Injection Vulnerability in Apache Kerby ## { #CVE-2023-25613 }

CVE-2023-25613 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25613) [\[CVE json\]](./CVE-2023-25613.cve.json) [\[OSV json\]](./CVE-2023-25613.osv.json)



_Last updated: 2024-01-18T09:14:01.669Z_

### Affected

* Apache Kerby LDAP Backend before 2.0.3


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
