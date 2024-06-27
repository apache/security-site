---
title: Apache Pinot security advisories
description: Security information for Apache Pinot
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Pinot? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Pinot segment push endpoint has a vulnerability in unprotected environments ## { #CVE-2022-23974 }

CVE-2022-23974 [\[CVE json\]](./CVE-2022-23974.cve.json) [\[OSV json\]](./CVE-2022-23974.osv.json)



_Last updated: 2022-04-05T19:51:49.065Z_

### Affected

* Apache Pinot from Apache Pinot through 0.9.3


### Description

In 0.9.3 or older versions of Apache Pinot segment upload path allowed segment directories to be imported into pinot tables. In pinot installations that allow open access to the controller a specially crafted request can potentially be exploited to cause disruption in pinot service.

Pinot release 0.10.0 fixes this. See https://docs.pinot.apache.org/basics/releases/0.10.0

### References
* https://lists.apache.org/thread/3dk8pf1n02p8oj2j3czbtchyjsf8khwr


### Credits
* Apache Pinot would like to thank bubblegumkk@qq.com, Kuiplatain@knownsec and FA1C0N@RPO_OFFICIAL for reporting the issue


## Pinot query endpoint and the realtime ingestion layer has a vulnerability in unprotected environments due to a groovy function support ## { #CVE-2022-26112 }

CVE-2022-26112 [\[CVE json\]](./CVE-2022-26112.cve.json) [\[OSV json\]](./CVE-2022-26112.osv.json)



_Last updated: 2022-09-23T03:13:43.429Z_

### Affected

* Apache Pinot from Apache Pinot through 0.10.0


### Description

In 0.10.0 or older versions of Apache Pinot, Pinot query endpoint and realtime ingestion layer has a vulnerability in unprotected environments due to a groovy function support. In order to avoid this, we disabled the groovy function support by default from Pinot release 0.11.0. See https://docs.pinot.apache.org/basics/releases/0.11.0

### References
* https://lists.apache.org/thread/4pb0r12s2b68d78llk04yd8rh3qk5t9h


### Credits
* Apache Pinot would like to thank Haoruo Chen(chenhaoruo0128@gmail.com) for reporting the issue
