---
title: Apache Knox security advisories
description: Security information for Apache Knox
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Knox? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## DOM based XSS Vulnerability in Apache Knox ## { #CVE-2021-42357 }

CVE-2021-42357 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-42357) [\[CVE json\]](./CVE-2021-42357.cve.json) [\[OSV json\]](./CVE-2021-42357.osv.json)



_Last updated: 2022-01-17T19:19:12.317Z_

### Affected

* Apache Knox from Apache Knox 1.x before 1.6.1
* Apache Knox from 0.12.0 before Apache Knox 0.x*


### Description

When using Apache Knox SSO prior to 1.6.1, a request could be crafted to redirect a user to a malicious page due to improper URL parsing.
A request that included a specially crafted request parameter could be used to redirect the user to a page controlled by an attacker. This URL would need to be presented to the user outside the normal request flow through a XSS or phishing campaign.

### References
* https://lists.apache.org/thread/b7v5dkpyqb51nw0lvz4cybhgrfhk1g7j


### Credits
* Apache Knox would like to thank Kajetan Rostojek for this report
