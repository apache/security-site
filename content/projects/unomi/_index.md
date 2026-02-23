---
title: Apache Unomi security advisories
description: Security information for Apache Unomi
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Unomi? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Unomi log injection ## { #CVE-2021-31164 }

CVE-2021-31164 [\[CVE json\]](./CVE-2021-31164.cve.json) [\[OSV json\]](./CVE-2021-31164.osv.json)



_Last updated: 2021-05-04T06:40:34.093Z_

### Affected

* Apache Unomi from Apache Unomi before 1.5.5


### Description

Apache Unomi prior to version 1.5.5 allows CRLF log injection because of the lack of escaping in the log statements.


### References
* http://unomi.apache.org/security/cve-2021-31164


## Remote Code Execution in Apache Unomi ## { #CVE-2020-13942 }

CVE-2020-13942 [\[CVE json\]](./CVE-2020-13942.cve.json) [\[OSV json\]](./CVE-2020-13942.osv.json)



_Last updated: 2020-11-24T17:55:44.282Z_

### Affected

* Apache Unomi from unspecified before 1.5.2


### Description

It is possible to inject malicious OGNL or MVEL scripts into the /context.json public endpoint. This was partially fixed in 1.5.1 but a new attack vector was found. In Apache Unomi version 1.5.2 scripts are now completely filtered from the input. It is highly recommended to upgrade to the latest available version of the 1.5.x release to fix this problem.

### References
* http://unomi.apache.org./security/cve-2020-13942.txt
