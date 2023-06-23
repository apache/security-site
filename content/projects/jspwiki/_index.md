---
title: Apache JSPWiki security advisories
description: Security information for Apache JSPWiki
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache JSPWiki? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache JSPWiki since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## XSS Injection points in several plugins ## { #CVE-2022-46907 }

[CVE-2022-46907](./CVE-2022-46907.cve.json)

### Affected

* Apache JSPWiki versions  before Apache JSPWiki up to 2.12.0 


### Description

A carefully crafted request on several JSPWiki plugins could trigger an XSS vulnerability on Apache JSPWiki, which could allow the attacker to execute javascript in the victim's browser and get some sensitive information about the victim.  Apache JSPWiki users should upgrade to 2.12.0 or later.<br>