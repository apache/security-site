---
title: Apache ManifoldCF security advisories
description: Security information for Apache ManifoldCF
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ManifoldCF? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache ManifoldCF since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## LDAP Injection Vulnerability - ActiveDirectory Authorities ## { #CVE-2022-45910 }

[CVE-2022-45910](./CVE-2022-45910.cve.json)

### Affected

* Apache ManifoldCF through 2.23


### Description

Improper neutralization of special elements used in an LDAP query ('LDAP Injection') vulnerability in ActiveDirectory and Sharepoint ActiveDirectory authority connectors of Apache ManifoldCF allows an attacker to manipulate the LDAP search queries (DoS, additional queries, filter manipulation) during user lookup, if the username or the domain string are passed to the UserACLs servlet without validation.<br><br>This issue affects Apache ManifoldCF version 2.23 and prior versions.