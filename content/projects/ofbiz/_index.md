---
title: Apache OFBiz security advisories
description: Security information for Apache OFBiz
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache OFBiz? You can read more about the projects' security policy on their [security page](https://ofbiz.apache.org/download.html#security), and email your report to the  [Apache OFBiz Security Team](mailto:security@ofbiz.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://ofbiz.apache.org/download.html#security). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Arbitrary file reading vulnerability ## { #CVE-2022-47501 }

CVE-2022-47501 [\[CVE json\]](./CVE-2022-47501.cve.json)

### Affected

* Apache OFBiz from 18.12.06 before 18.12.07


### Description

Arbitrary file reading vulnerability in Apache Software Foundation Apache OFBiz when using the Solr plugin. This is a&nbsp;
pre-authentication attack.<br><p>This issue affects Apache OFBiz: before 18.12.07.</p>

### References
* https://lists.apache.org/thread/k8s76l0whydy45bfm4b69vq0mf94p3wc
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html


### Credits
* Skay <lhcaomail@gmail.com> (finder)
