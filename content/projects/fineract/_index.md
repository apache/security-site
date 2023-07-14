---
title: Apache Fineract security advisories
description: Security information for Apache Fineract
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Fineract? You can read more about the projects' security policy on their [security page](https://cwiki.apache.org/confluence/display/FINERACT/Apache+Fineract+Security+Report), and email your report to the  [Apache Fineract Security Team](mailto:security@fineract.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://cwiki.apache.org/confluence/display/FINERACT/Apache+Fineract+Security+Report). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## SSRF template type vulnerability in certain authenticated users ## { #CVE-2023-25195 }

CVE-2023-25195 [\[CVE json\]](./CVE-2023-25195.cve.json)

### Affected

* Apache Fineract from 1.4 through 1.8.3


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache Software Foundation Apache Fineract.<br><p>Authorized users with limited permissions can gain access to server and may be able to use server for any outbound traffic.&nbsp;</p><p>This issue affects Apache Fineract: from 1.4 through 1.8.3.</p>

### References
* https://lists.apache.org/thread/m58fdjmtkfp9h4c0r4l48rv995w3qhb6


### Credits
* Huydoppa from GHTK  (reporter)
* Aleksander (remediation developer)


## SQL injection vulnerability  ## { #CVE-2023-25196 }

CVE-2023-25196 [\[CVE json\]](./CVE-2023-25196.cve.json)

### Affected

* Apache Fineract from 1.4 through 1.8.2


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Software Foundation Apache Fineract.<br><p>Authorized users may be able to change or add data in certain components. &nbsp;</p><p>This issue affects Apache Fineract: from 1.4 through 1.8.2.</p>

### References
* https://lists.apache.org/thread/m9x3vpn3bry4fympkzxnnz4qx0oc0w8m


### Credits
*  Zhang Baocheng at Leng Jing Qi Cai Security Lab (reporter)
* Aleks@apache.org (remediation developer)


## SQL injection vulnerability in certain procedure calls  ## { #CVE-2023-25197 }

CVE-2023-25197 [\[CVE json\]](./CVE-2023-25197.cve.json)

### Affected

* apache fineract from 1.4 through 1.8.2


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Software Foundation apache fineract.<br><p>Authorized users may be able to exploit this for limited impact on components. &nbsp;</p><p>This issue affects apache fineract: from 1.4 through 1.8.2.</p>

### References
* https://lists.apache.org/thread/v0q9x86sx6f6l2nzr1z0nwm3y9qlng04


### Credits
* Eugene Lim at Cyber Security Group (CSG) Government Technology Agency GOVTECH.sg (reporter)
* aleks@apache.org (remediation developer)
