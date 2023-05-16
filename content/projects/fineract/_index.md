---
title: Apache Fineract security advisories
description: Security information for Apache Fineract
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Fineract? You can read more about the projects' security policy on their [security page](https://cwiki.apache.org/confluence/display/FINERACT/Apache+Fineract+Security+Report), and email your report to the  [Apache Fineract Security Team](mailto:security@fineract.apache.org).

# Advisories

## SSRF template type vulnerability in certain authenticated users ## { #CVE-2023-25195 }

[CVE-2023-25195](./CVE-2023-25195.cve.json)

### Affected

* Apache Fineract versions 1.4 including 1.8.3


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache Software Foundation Apache Fineract.<br><p>Authorized users with limited permissions can gain access to server and may be able to use server for any outbound traffic.&nbsp;</p><p>This issue affects Apache Fineract: from 1.4 through 1.8.3.</p>

## SQL injection vulnerability  ## { #CVE-2023-25196 }

[CVE-2023-25196](./CVE-2023-25196.cve.json)

### Affected

* Apache Fineract versions 1.4 including 1.8.2


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Software Foundation Apache Fineract.<br><p>Authorized users may be able to change or add data in certain components. &nbsp;</p><p>This issue affects Apache Fineract: from 1.4 through 1.8.2.</p>

## SQL injection vulnerability in certain procedure calls  ## { #CVE-2023-25197 }

[CVE-2023-25197](./CVE-2023-25197.cve.json)

### Affected

* apache fineract versions 1.4 including 1.8.2


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Software Foundation apache fineract.<br><p>Authorized users may be able to exploit this for limited impact on components. &nbsp;</p><p>This issue affects apache fineract: from 1.4 through 1.8.2.</p>