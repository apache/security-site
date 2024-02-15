---
title: Apache MXNet security advisories
description: Security information for Apache MXNet
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache MXNet? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## ReDoS in Apache MXNet RTC Module ## { #CVE-2022-24294 }

CVE-2022-24294 [\[CVE json\]](./CVE-2022-24294.cve.json)

_Last updated: 2022-07-24T17:40:13.807Z_

### Affected

* Apache MXNet from unspecified before 1.9.1


### Description

A regular expression used in Apache MXNet (incubating) is vulnerable to a potential denial-of-service by excessive resource consumption. The bug could be exploited when loading a model in Apache MXNet that has a specially crafted operator name that would cause the regular expression evaluation to use excessive resources to attempt a match. This issue affects Apache MXNet versions prior to 1.9.1.

### References
* https://lists.apache.org/thread/b1fbfmvzlr2bbp95lqoh3mtovclfcl3o


### Credits
* Apache MXNet would like to thank Dwi Siswanto for reporting this issue.
