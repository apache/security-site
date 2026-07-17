---
title: Apache Seata security advisories
description: Security information for Apache Seata
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Seata? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=%5BFINDING%5D%20Apache%20Seata).

You can read more about the security policy on:

- [Apache Seata security model](https://seata.apache.org/docs/next/security/secret-key)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Deserialization of untrusted Data in Apache Seata Server ## { #CVE-2025-53606 }

CVE-2025-53606 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-53606) [\[CVE json\]](./CVE-2025-53606.cve.json) [\[OSV json\]](./CVE-2025-53606.osv.json)



_Last updated: 2025-08-08T09:22:52.076Z_

### Affected

* Apache Seata (incubating) at 2.4.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Seata (incubating).</p><p>This issue affects Apache Seata (incubating): 2.4.0.</p><p>Users are recommended to upgrade to version 2.5.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ggfd72vvvxjozs81zbcls45zxg64pphx


### Credits
* A.R. (finder)


## Deserialization of untrusted Data in Apache Seata Server ## { #CVE-2025-32897 }

CVE-2025-32897 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-32897) [\[CVE json\]](./CVE-2025-32897.cve.json) [\[OSV json\]](./CVE-2025-32897.osv.json)



_Last updated: 2026-03-30T02:05:32.515Z_

### Affected

* Apache Seata (incubating) from 2.0.0 before 2.3.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Seata (incubating).</p><span style="background-color: rgb(255, 255, 255);">This security vulnerability is the same as CVE-2024-47552, but the version range described in the CVE-2024-47552 definition is too narrow.</span><br><p>This issue affects Apache Seata (incubating): from 2.0.0 before 2.3.0.</p><b>Severity Justification:</b><br>The Apache Seata security team assesses the severity of this vulnerability as "Low" due to stringent real-world mitigating factors. First, the vulnerability is strictly isolated to the Raft cluster mode, an optional and non-default feature introduced in v2.0.0, while most users rely on the unaffected traditional architecture. Second, Seata is an internal middleware; communication between TC and RM/TM occurs entirely within trusted internal networks. An attacker would require prior, unauthorized access to the Intranet to exploit this, making external exploitation highly improbable.<br><p>Users are recommended to upgrade to version 2.3.0, which fixes the issue.</p>

### References
* https://www.cve.org/CVERecord?id=CVE-2024-47552
* https://lists.apache.org/thread/9fhtf7yvpjpzlwd1m0wfgg6tp2btxpy1
* https://github.com/apache/incubator-seata/commit/20cd9625d23f99b71fefc83b8db96c14092a9950


## compression bomb attack in Apache Seata Server ## { #CVE-2024-54016 }

CVE-2024-54016 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-54016) [\[CVE json\]](./CVE-2024-54016.cve.json) [\[OSV json\]](./CVE-2024-54016.osv.json)



_Last updated: 2025-03-20T08:59:24.157Z_

### Affected

* Apache Seata (incubating) through <=2.2.0


### Description

<p>Improper Handling of Highly Compressed Data (Data Amplification) vulnerability in Apache Seata (incubating).</p><p>This issue affects Apache Seata (incubating): through &lt;=2.2.0.</p><p>Users are recommended to upgrade to version 2.3.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/grn0x8tmssx07qc9z50lwgmrkwzrrhzg


### Credits
* yyjLF@proton.me (finder)


## Deserialization of untrusted Data in jraft mode in Apache Seata Server ## { #CVE-2024-47552 }

CVE-2024-47552 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-47552) [\[CVE json\]](./CVE-2024-47552.cve.json) [\[OSV json\]](./CVE-2024-47552.osv.json)



_Last updated: 2026-03-30T02:08:11.034Z_

### Affected

* Apache Seata (incubating) from 2.0.0 before 2.2.0


### Description

<div>Deserialization of Untrusted Data vulnerability in Apache Seata (incubating).</div><div>
</div><div><br>This issue affects Apache Seata (incubating): from 2.0.0 before 2.2.0.</div><div>
</div><div><br><b>Severity Justification:</b></div><div>The Apache Seata security team assesses the severity of this vulnerability as "Low" due to stringent real-world mitigating factors. First, the vulnerability is strictly isolated to the Raft cluster mode, an optional and non-default feature introduced in v2.0.0, while most users rely on the unaffected traditional architecture. Second, Seata is an internal middleware; communication between TC and RM/TM occurs entirely within trusted internal networks. An attacker would require prior, unauthorized access to the Intranet to exploit this, making external exploitation highly improbable.</div><div>
</div><div><br>Users are recommended to upgrade to version 2.2.0, which fixes the issue.</div><br>

### References
* https://lists.apache.org/thread/652o82vzk9qrtgksk55cfgpbvdgtkch0
* https://github.com/apache/incubator-seata/commit/20cd9625d23f99b71fefc83b8db96c14092a9950


### Credits
* liuhuajin<liuhuajin1@huawei.com> (finder)
* llqxc369@gmail.com (finder)


## Remote Code Execution vulnerability via Hessian Deserialization in Apache Seata Server ## { #CVE-2024-22399 }

CVE-2024-22399 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-22399) [\[CVE json\]](./CVE-2024-22399.cve.json) [\[OSV json\]](./CVE-2024-22399.osv.json)



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
