---
title: Apache Geode security advisories
description: Security information for Apache Geode
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Geode? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## CSRF attacks through GET requests to the Management and Monitoring REST API that can execute gfsh commands on the target system ## { #CVE-2025-47410 }

CVE-2025-47410 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-47410) [\[CVE json\]](./CVE-2025-47410.cve.json) [\[OSV json\]](./CVE-2025-47410.osv.json)



_Last updated: 2025-10-18T15:15:07.664Z_

### Affected

* Apache Geode from 1.10.0 before 1.15.2


### Description

Apache Geode is vulnerable to CSRF attacks through GET requests to the Management and Monitoring REST API that could allow an attacker who has tricked a user into giving up their Geode session credentials to submit malicious commands on the target system on behalf of the authenticated user.<br>

<p>This issue affects Apache Geode: versions 1.10 through 1.15.1</p><p>Users are recommended to upgrade to version 1.15.2, which fixes the issue.</p>

<br>

### References
* https://lists.apache.org/thread/k88tv3rhl4ymsvt4h6qsv7sq10q5prrt


### Credits
* S. M. Zuhair Zaki (finder)


## Reflected XSS ## { #CVE-2024-44088 }

CVE-2024-44088 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-44088) [\[CVE json\]](./CVE-2024-44088.cve.json) [\[OSV json\]](./CVE-2024-44088.osv.json)



_Last updated: 2025-10-14T14:36:50.748Z_

### Affected

* Apache Geode from 1.1.0 before 1.15.2


### Description

<p>

<span style="background-color: rgb(255, 255, 255);">Malicious script injection </span><span style="background-color: rgb(255, 255, 255);">('Cross-site Scripting') vulnerability in Apache Geode</span><span style="background-color: rgb(255, 255, 255);">&nbsp;web-api (REST). This vulnerability allows an attacker that tricks a logged-in user into clicking a specially-crafted link to execute code on the returned page, which could lead to theft of the user's session information and even account takeover.</span>

</p><p>This issue affects Apache Geode: all versions prior to 1.15.2</p><p>Users are recommended to upgrade to version 1.15.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/161r34nokmcc0w74mnf04lskgb8g1d3g


### Credits
* Nbxiglk (finder)


## Apache Geode deserialization of untrusted data flaw when using REST API on Java 8 or Java 11 ## { #CVE-2022-37023 }

CVE-2022-37023 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-37023) [\[CVE json\]](./CVE-2022-37023.cve.json) [\[OSV json\]](./CVE-2022-37023.osv.json)



_Last updated: 2022-08-31T06:58:07.415Z_

### Affected

* Apache Geode from Apache Geode before 1.15.0


### Description

Apache Geode versions prior to 1.15.0 are vulnerable to a deserialization of untrusted data flaw when using REST API on Java 8 or Java 11.

Any user wishing to protect against deserialization attacks involving REST APIs should upgrade to Apache Geode 1.15 and follow the documentation for details on enabling "validate-serializable-objects=true" and specifying any user classes that may be serialized/deserialized with "serializable-object-filter". Enabling "validate-serializable-objects" may impact performance.

### References
* https://lists.apache.org/thread/6js89pbqrp52zlpwgry5fsdn76gxbbfj


## Apache Geode deserialization of untrusted data flaw when using JMX over RMI on Java 11 ## { #CVE-2022-37022 }

CVE-2022-37022 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-37022) [\[CVE json\]](./CVE-2022-37022.cve.json) [\[OSV json\]](./CVE-2022-37022.osv.json)



_Last updated: 2022-08-31T06:56:24.123Z_

### Affected

* Apache Geode from Apache Geode through 1.12.2


### Description

Apache Geode versions up to 1.12.2 and 1.13.2 are vulnerable to a deserialization of untrusted data flaw when using JMX over RMI on Java 11.

Any user wishing to protect against deserialization attacks involving JMX or RMI should upgrade to Apache Geode 1.15. Use of 1.15 on Java 11 will automatically protect JMX over RMI against deserialization attacks. This should have no impact on performance since it only affects JMX/RMI which Gfsh uses to communicate with the JMX Manager which is hosted on a Locator.

### References
* https://lists.apache.org/thread/kr1y4l9752g1ww1shnmh8dbfjq785k4m


## Apache Geode deserialization of untrusted data flaw when using JMX over RMI on Java 8.  ## { #CVE-2022-37021 }

CVE-2022-37021 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-37021) [\[CVE json\]](./CVE-2022-37021.cve.json) [\[OSV json\]](./CVE-2022-37021.osv.json)



_Last updated: 2022-08-31T06:54:22.083Z_

### Affected

* Apache Geode from Apache Geode through 1.12.5


### Description

Apache Geode versions up to 1.12.5, 1.13.4 and 1.14.0 are vulnerable to a deserialization of untrusted data flaw when using JMX over RMI on Java 8. 

Any user still on Java 8 who wishes to protect against deserialization attacks involving JMX or RMI should upgrade to Apache Geode 1.15 and Java 11. 

If upgrading to Java 11 is not possible, then upgrade to Apache Geode 1.15 and specify "--J=-Dgeode.enableGlobalSerialFilter=true" when starting any Locators or Servers. Follow the documentation for details on specifying any user classes that may be serialized/deserialized with the "serializable-object-filter" configuration option. Using a global serial filter will impact performance.

### References
* https://lists.apache.org/thread/qrvhmytsshsk5xcb68pwccw3y6m8o8nr


## Apache Geode stored Cross-Site Scripting (XSS) via data injection vulnerability in Pulse web application ## { #CVE-2022-34870 }

CVE-2022-34870 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-34870) [\[CVE json\]](./CVE-2022-34870.cve.json) [\[OSV json\]](./CVE-2022-34870.osv.json)



_Last updated: 2022-10-24T18:09:52.450Z_

### Affected

* Apache Geode from Apache Geode through 1.15.0


### Description

Apache Geode versions up to 1.15.0 are vulnerable to a Cross-Site Scripting (XSS) via data injection when using Pulse web application to view Region entries.

### References
* https://lists.apache.org/thread/zltlr7f2ymr2m6jj54k4z0c4foos5fwx


## Apache Geode log file redaction of sensitive information vulnerability ## { #CVE-2021-34797 }

CVE-2021-34797 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-34797) [\[CVE json\]](./CVE-2021-34797.cve.json) [\[OSV json\]](./CVE-2021-34797.osv.json)



_Last updated: 2022-06-28T22:46:44.541Z_

### Affected

* Apache Geode from Apache Geode through 1.12.4


### Description

Apache Geode versions up to 1.12.4 and 1.13.4 are vulnerable to a log file redaction of sensitive information flaw when using values that begin with characters other than letters or numbers for passwords and security properties with the prefix "sysprop-", "javax.net.ssl", or "security-". This issue is fixed by overhauling the log file redaction in Apache Geode versions 1.12.5, 1.13.5, and 1.14.0.

### References
* https://lists.apache.org/thread/p4l0g49rzzzpn8yt9q9p0xp52h3zmsmk
* https://lists.apache.org/thread/nq2w9gjzm1cjx1rh6zw41ty39qw7qpx4


### Credits
* Apache Geode would like to thank Aaron Lindsey for reporting this issue.
