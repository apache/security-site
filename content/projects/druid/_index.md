---
title: Apache Druid security advisories
description: Security information for Apache Druid
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Druid? You can read more about the projects' security policy on their [security page](https://druid.apache.org/docs/latest/operations/security-overview.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://druid.apache.org/docs/latest/operations/security-overview.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Authenticated users can override system configurations in their requests which allows them to execute arbitrary code. ## { #CVE-2021-25646 }

CVE-2021-25646 [\[CVE json\]](./CVE-2021-25646.cve.json) [\[OSV json\]](./CVE-2021-25646.osv.json)



_Last updated: 2021-01-29T19:09:31.597Z_

### Affected

* Apache Druid from 0.20.0 and earlier through 0.20.0


### Description

Apache Druid includes the ability to execute user-provided JavaScript code embedded in various types of requests. This functionality is intended for use in high-trust environments, and is disabled by default. However, in Druid 0.20.0 and earlier, it is possible for an authenticated user to send a specially-crafted request that forces Druid to run user-provided JavaScript code for that request, regardless of server configuration. This can be leveraged to execute code on the target machine with the privileges of the Druid server process.


### References
* https://lists.apache.org/thread.html/rfda8a3aa6ac06a80c5cbfdeae0fc85f88a5984e32ea05e6dda46f866%40%3Cdev.druid.apache.org%3E


### Credits
* This issue was discovered by Litch1 from the Security Team of Alibaba Cloud.


## Apache Druid Authenticated users can execute arbitrary code from malicious MySQL database systems. ## { #CVE-2021-26919 }

CVE-2021-26919 [\[CVE json\]](./CVE-2021-26919.cve.json) [\[OSV json\]](./CVE-2021-26919.osv.json)



_Last updated: 2021-03-30T07:47:52.941Z_

### Affected

* Apache Druid from Apache Druid through 0.20.1


### Description

Apache Druid allows users to read data from other database systems using JDBC. This functionality is to allow trusted users with the proper permissions to set up lookups or submit ingestion tasks. The MySQL JDBC driver supports certain properties, which, if left unmitigated, can allow an attacker to execute arbitrary code from a hacker-controlled malicious MySQL server within Druid server processes.  This issue was addressed in Apache Druid 0.20.2

### References
* https://lists.apache.org/thread.html/rd87451fce34df54796e66321c40d743a68fb4553d72e7f6f0bc62ebd%40%3Cdev.druid.apache.org%3E


### Credits
* This issue was discovered by fantasyC4t from the Ant FG Security Lab.


## Apache Druid: The HTTP inputSource allows authenticated users to read data from other sources than intended ## { #CVE-2021-26920 }

CVE-2021-26920 [\[CVE json\]](./CVE-2021-26920.cve.json) [\[OSV json\]](./CVE-2021-26920.osv.json)



_Last updated: 2021-07-02T07:14:27.176Z_

### Affected

* Apache Druid from Apache Druid through 0.20.2


### Description

In the Druid ingestion system, the InputSource is used for reading data from a certain data source. However, the HTTP InputSource allows authenticated users to read data from other sources than intended, such as the local file system, with the privileges of the Druid server process. This is not an elevation of privilege when users access Druid directly, since Druid also provides the Local InputSource, which allows the same level of access. But it is problematic when users interact with Druid indirectly through an application that allows users to specify the HTTP InputSource, but not the Local InputSource. In this case, users could bypass the application-level restriction by passing a file URL to the HTTP InputSource.

### References
* https://lists.apache.org/thread.html/r29e45561343cc5cf7d3290ee0b0e94e565faab19c20d022df9b5e29c%40%3Cdev.druid.apache.org%3E


### Credits
* This issue was discovered by chybeta from the Security Team of Alibaba Cloud.


## Apache Druid: The HTTP inputSource allows authenticated users to read data from other sources than intended (incomplete fix of CVE-2021-26920) ## { #CVE-2021-36749 }

CVE-2021-36749 [\[CVE json\]](./CVE-2021-36749.cve.json) [\[OSV json\]](./CVE-2021-36749.osv.json)



_Last updated: 2021-09-23T23:08:21.915Z_

### Affected

* Apache Druid from 0.21.1 and earlier through 0.21.1


### Description

In the Druid ingestion system, the InputSource is used for reading data from a certain data source. However, the HTTP InputSource allows authenticated users to read data from other sources than intended, such as the local file system, with the privileges of the Druid server process. This is not an elevation of privilege when users access Druid directly, since Druid also provides the Local InputSource, which allows the same level of access. But it is problematic when users interact with Druid indirectly through an application that allows users to specify the HTTP InputSource, but not the Local InputSource. In this case, users could bypass the application-level restriction by passing a file URL to the HTTP InputSource.

This issue was previously mentioned as being fixed in 0.21.0 as per CVE-2021-26920 but was not fixed in 0.21.0 or 0.21.1.

### References
* https://lists.apache.org/thread.html/rc9400a70d0ec5cdb8a3486fc5ddb0b5282961c0b63e764abfbcb9f5d%40%3Cdev.druid.apache.org%3E


### Credits
* This issue was originally discovered by chybeta from the Security Team of Alibaba Cloud.
* ABKing and g0udan from the Security Team of Xiaomi discovered that it was still an issue after CVE-2021-26920.


## Reflected XSS on certain HTTP endpoints ## { #CVE-2021-44791 }

CVE-2021-44791 [\[CVE json\]](./CVE-2021-44791.cve.json) [\[OSV json\]](./CVE-2021-44791.osv.json)



_Last updated: 2022-07-07T18:29:34.319Z_

### Affected

* Apache Druid from Apache Druid through 0.22.1


### Description

In Apache Druid 0.22.1 and earlier, certain specially-crafted links result in unescaped URL parameters being sent back in HTML responses. This makes it possible to execute reflected XSS attacks.

### References
* https://lists.apache.org/thread/lh2kcl4j45q7xj4w6rqf6kwf0mvyp2o6


### Credits
* This issue was discovered by DangKhai from Viettel Cyber Security


## Clickjacking in the web console ## { #CVE-2022-28889 }

CVE-2022-28889 [\[CVE json\]](./CVE-2022-28889.cve.json) [\[OSV json\]](./CVE-2022-28889.osv.json)



_Last updated: 2022-07-07T18:30:27.570Z_

### Affected

* Apache Druid from unspecified through 0.22.1


### Description

In Apache Druid 0.22.1 and earlier, the server did not set appropriate headers to prevent clickjacking. Druid 0.23.0 and later prevent clickjacking using the Content-Security-Policy header.

### References
* https://lists.apache.org/thread/t3nsq4crdr8wqgmj721d2wg6pf26s5cw


## Padding oracle in druid-pac4j extension that allows an attacker to manipulate a pac4j session cookie via Padding Oracle Attack ## { #CVE-2024-45384 }

CVE-2024-45384 [\[CVE json\]](./CVE-2024-45384.cve.json) [\[OSV json\]](./CVE-2024-45384.osv.json)



_Last updated: 2024-09-17T17:58:14.680Z_

### Affected

* Apache Druid from 0.18.0 through 30.0.0


### Description

<p>Padding Oracle vulnerability in Apache Druid extension, druid-pac4j.<br>This could allow an attacker to manipulate a pac4j session cookie.<br><br></p><p>This issue affects Apache Druid versions 0.18.0 through 30.0.0.<br>Since the druid-pac4j extension is optional and disabled by default, Druid installations not using the druid-pac4j extension are not affected by this vulnerability.<br></p><p></p><br>While we are not aware of a way to meaningfully exploit this flaw, we 
nevertheless recommend upgrading to version 30.0.1 or higher which fixes the issue<br>and ensuring you have a strong 
druid.auth.pac4j.cookiePassphrase as a precaution.<br><p></p>

### References
* https://lists.apache.org/thread/gr94fnp574plb50lsp8jw4smvgv1lbz1


### Credits
* mr-n30 (reporter)


## Users can provide MySQL JDBC properties not on allow list ## { #CVE-2024-45537 }

CVE-2024-45537 [\[CVE json\]](./CVE-2024-45537.cve.json) [\[OSV json\]](./CVE-2024-45537.osv.json)



_Last updated: 2024-09-19T09:29:22.203Z_

### Affected

* Apache Druid through 30.0.0


### Description

<div>Apache Druid allows users with certain permissions to read data from other database systems using JDBC. This functionality allows trusted users to set up Druid lookups or run ingestion tasks. Druid also allows administrators to configure a list of allowed properties that users are able to provide for their JDBC connections. By default, this allowed properties list restricts users to TLS-related properties only. However, when configuration a MySQL JDBC connection, users can use a particularly-crafted JDBC connection string to provide properties that are not on this allow list.</div><div><br></div>Users without the permission to configure JDBC connections are not able to exploit this vulnerability.<br>CVE-2021-26919 describes a similar vulnerability which was partially addressed in Apache Druid 0.20.2.<br><div><br></div><div><br></div><div>This issue is fixed in Apache Druid 30.0.1.</div><br>

### References
* https://lists.apache.org/thread/2ovx1t77y6tlkhk5b42clp4vwo4c8cjv


### Credits
* L0ne1y (finder)


## Server-Side Request Forgery and Cross-Site Scripting ## { #CVE-2025-27888 }

CVE-2025-27888 [\[CVE json\]](./CVE-2025-27888.cve.json) [\[OSV json\]](./CVE-2025-27888.osv.json)



_Last updated: 2025-03-24T07:41:49.543Z_

### Affected

* Apache Druid before 31.0.2
* Apache Druid at 32.0.0


### Description

<p>Severity: medium (5.8) / important</p><p>Server-Side Request Forgery (SSRF), Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'),&nbsp;URL Redirection to Untrusted Site ('Open Redirect') vulnerability in Apache Druid.</p><p>This issue affects all previous Druid versions.<br></p><p><span style="background-color: rgba(232, 232, 232, 0.04);">When using the Druid management proxy, a request that has a specially crafted URL could be used to redirect the request to an arbitrary server instead. This has the potential for XSS or XSRF. The user is required to be authenticated for this exploit. The management proxy is enabled in Druid's out-of-box configuration. It may be disabled to mitigate this vulnerability. If the management proxy is disabled, some web console features will not work properly, but core functionality is unaffected.<br></span></p><p>Users are recommended to upgrade to Druid 31.0.2 or Druid 32.0.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/c0qo989pwtrqkjv6xfr0c30dnjq8vf39


### Credits
* XBOW (reporter)


## Kerberos authenticaton chooses a cryptographically unsecure secret if not configured explicitly. ## { #CVE-2025-59390 }

CVE-2025-59390 [\[CVE json\]](./CVE-2025-59390.cve.json) [\[OSV json\]](./CVE-2025-59390.osv.json)



_Last updated: 2025-12-11T12:56:31.790Z_

### Affected

* Apache Druid through 34.0.0


### Description

<p>Apache Druid’s Kerberos authenticator uses a weak fallback secret when the `druid.auth.authenticator.kerberos.cookieSignatureSecret<code></code>` configuration is not explicitly set. In this case, the secret is generated using <code>`ThreadLocalRandom`</code>,
 which is not a crypto-graphically secure random number generator. This 
may allow an attacker to predict or brute force the secret used to sign 
authentication cookies, potentially enabling token forgery or 
authentication bypass. Additionally, each process generates its own 
fallback secret, resulting in inconsistent secrets across nodes. This 
causes authentication failures in distributed or multi-broker 
deployments, effectively leading to a incorrectly configured clusters. Users are 
advised to configure a strong&nbsp;<code>`druid.auth.authenticator.kerberos.cookieSignatureSecret`</code><br><br></p><p>This issue affects Apache Druid: through 34.0.0.</p><p>Users are recommended to upgrade to version 35.0.0, which fixes the issue making it mandatory to set `druid.auth.authenticator.kerberos.cookieSignatureSecret` when using the&nbsp;Kerberos authenticator. Services will fail to come up if the secret is not set.&nbsp;</p>

### References
* https://lists.apache.org/thread/jwjltllnntgj1sb9wzsjmvwm9f8rlhg8


### Credits
* Luke Smith (smithluke1966@gmail.com) (finder)
* 1nfocalypse (analyst)
