---
title: Apache Web Services security advisories
description: Security information for Apache Web Services
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Web Services? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache SOAP: XML External Entity Injection (XXE) allows unauthenticated users to read arbitrary files via HTTP ## { #CVE-2022-40705 }

CVE-2022-40705 [\[CVE json\]](./CVE-2022-40705.cve.json)

_Last updated: 2022-09-22T08:11:36.490Z_

### Affected

* Apache SOAP from 2.2 before Apache SOAP*


### Description

An Improper Restriction of XML External Entity Reference vulnerability in RPCRouterServlet of Apache SOAP allows an attacker to read arbitrary files over HTTP. This issue affects Apache SOAP version 2.2 and later versions. It is unknown whether previous versions are also affected.  NOTE: This vulnerability only affects products that are no longer supported by the maintainer

### References
* https://lists.apache.org/thread/02yo04w93rdjmllz4454lvodn5xzhwhl


### Credits
* Apache would like to thank TsungShu Chiu (CHT Security) for reporting this issue


## Apache SOAP allows unauthenticated users to potentially invoke arbitrary code ## { #CVE-2022-45378 }

CVE-2022-45378 [\[CVE json\]](./CVE-2022-45378.cve.json)

_Last updated: 2022-11-14T14:06:51.577Z_

### Affected

* Apache SOAP at 2.3
* Apache SOAP from Apache SOAP before 2.3


### Description

In the default configuration of Apache SOAP, an RPCRouterServlet is available without authentication. This gives an attacker the possibility to invoke methods on the classpath that meet certain criteria. Depending on what classes are available on the classpath this might even lead to arbitrary remote code execution. NOTE: This vulnerability only affects products that are no longer supported by the maintainer

### References
* https://lists.apache.org/thread/g4l64s283njhnph2otx7q4gs2j952d31


### Credits
*   Apache would like to thank TsungShu Chiu (CHT Security) for reporting this issue
