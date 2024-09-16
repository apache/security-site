---
title: Apache Seata (Incubating) security advisories
description: Security information for Apache Seata (Incubating)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Seata (Incubating)? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Remote Code Execution vulnerability via Hessian Deserialization in Apache Seata Server ## { #CVE-2024-22399 }

CVE-2024-22399 [\[CVE json\]](./CVE-2024-22399.cve.json) [\[OSV json\]](./CVE-2024-22399.osv.json)



_Last updated: 2024-09-16T11:42:03.440Z_

### Affected

* Apache Seata at 2.0.0
* Apache Seata from 1.0.0 through 1.8.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Seata.&nbsp;<br><br><div><div><div><div><div><p>When developers disable authentication on the Seata-Server and do not use the Seata client SDK dependencies, they may construct uncontrolled serialized malicious requests by directly sending bytecode based on the Seata private protocol.<br><br></p></div></div></div></div></div><div></div><p>This issue affects Apache Seata: 2.0.0, from 1.0.0 through 1.8.0.</p><p>Users are recommended to upgrade to version 2.1.0/1.8.1, which fixes the issue.</p><br>

### References
* https://lists.apache.org/thread/91nzzlxyj4nmks85gbzwkkjtbmnmlkc4


### Credits
* X1r0z(exp10it666123@gmail.com) (finder)
