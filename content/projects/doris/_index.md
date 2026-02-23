---
title: Apache Doris security advisories
description: Security information for Apache Doris
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Doris? You can read more about the projects' security policy on their [security page](https://doris.apache.org/docs/dev/admin-manual/auth/security-overview), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://doris.apache.org/docs/dev/admin-manual/auth/security-overview). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improper Access Control results in bypassing a "read-only" mode for doris-mcp-server MCP Server ## { #CVE-2025-58337 }

CVE-2025-58337 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-58337) [\[CVE json\]](./CVE-2025-58337.cve.json) [\[OSV json\]](./CVE-2025-58337.osv.json)



_Last updated: 2025-11-05T09:26:34.887Z_

### Affected

* Apache Doris-MCP-Server from 0.1.0 before 0.6.0


### Description

<p>An attacker with a valid read-only account can bypass Doris MCP Server’s read-only mode due to improper access control, allowing modifications that should have been prevented by read-only restrictions.<br></p><p>Impact:<br>
Bypasses read-only mode; attackers with read-only access may perform unauthorized modifications.</p>
<p></p><p>Recommended action for operators: Upgrade to version 0.6.0 as soon as possible (this release contains the fix).</p><p></p>
<p></p><br>

### References
* https://lists.apache.org/thread/6tswlphj0pqn9zf25594r3c1vzvfj40h


### Credits
* Liran Tal, (liran@lirantal.com) (finder)


## allows admin users to read arbitrary files through the REST API ## { #CVE-2024-48019 }

CVE-2024-48019 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-48019) [\[CVE json\]](./CVE-2024-48019.cve.json) [\[OSV json\]](./CVE-2024-48019.osv.json)



_Last updated: 2025-02-04T18:19:49.957Z_

### Affected

* Apache Doris from 2.1.0 before 2.1.8
* Apache Doris from 3.0.0 before 3.0.3


### Description

<p>Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'), Files or Directories Accessible to External Parties vulnerability in Apache Doris.<br></p><p><span style="background-color: rgb(255, 255, 255);">Application administrators can read arbitrary
files from the server filesystem through path traversal.</span><br></p><p>Users are recommended to upgrade to version 2.1.8, 3.0.3 or later, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/p70klgmyrgknhn0t195261wvwv5jw6hr


### Credits
* Man Yue Mo of the GitHub Security Lab team (finder)


## Downloading arbitrary remote jar files resulting in remote command execution ## { #CVE-2024-27438 }

CVE-2024-27438 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-27438) [\[CVE json\]](./CVE-2024-27438.cve.json) [\[OSV json\]](./CVE-2024-27438.osv.json)



_Last updated: 2024-03-21T09:39:20.599Z_

### Affected

* Apache Doris from 1.2.0 through 2.0.4


### Description

Download of Code Without Integrity Check vulnerability in Apache Doris.<br>The jdbc driver files used for JDBC catalog is not checked and may&nbsp;resulting in remote command execution.<br>Once the attacker is authorized to create a JDBC catalog, he/she can use arbitrary driver jar file with unchecked code snippet. This&nbsp;code snippet will be run when catalog is initializing without any check.<br><p>This issue affects Apache Doris: from 1.2.0 through 2.0.4.</p><p>Users are recommended to upgrade to version 2.0.5 or 2.1.x, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/h95h82b0svlnwcg6c2xq4b08j6gwgczh


## Possible race condition ## { #CVE-2024-26307 }

CVE-2024-26307 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-26307) [\[CVE json\]](./CVE-2024-26307.cve.json) [\[OSV json\]](./CVE-2024-26307.osv.json)



_Last updated: 2024-03-21T09:38:16.580Z_

### Affected

* Apache Doris before 1.2.8
* Apache Doris before 2.0.4


### Description

Possible race condition vulnerability in Apache Doris.<br>Some of code using `chmod()` method. This method <span style="background-color: rgb(255, 255, 255);">run the risk of someone renaming the file out from under user and chmodding the wrong file.<br>This could theoretically happen, but the impact would be minimal.</span><br><p>This issue affects Apache Doris: before 1.2.8, before 2.0.4.</p><p>Users are recommended to upgrade to version 2.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/5shhw8x8m271hd2wfwzqzwgf36pmc4pl


## Missing API authentication allowed DoS ## { #CVE-2023-41314 }

CVE-2023-41314 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-41314) [\[CVE json\]](./CVE-2023-41314.cve.json) [\[OSV json\]](./CVE-2023-41314.osv.json)



_Last updated: 2023-12-18T08:27:49.193Z_

### Affected

* Apache Doris from 1.2.0 through 2.0.3


### Description

The api /api/snapshot and /api/get_log_file would allow unauthenticated access.<br>It could allow a&nbsp;DoS attack or get arbitrary files from FE node.<br>Please&nbsp;upgrade to 2.0.3 to fix these issues.

### References
* https://lists.apache.org/thread/tgvpvz3yw7zgodl1sb3sv3jbbz8t5zb4


## Timing Attack weakness ## { #CVE-2023-41313 }

CVE-2023-41313 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-41313) [\[CVE json\]](./CVE-2023-41313.cve.json) [\[OSV json\]](./CVE-2023-41313.osv.json)



_Last updated: 2024-03-12T10:16:14.512Z_

### Affected

* Apache Doris before 1.2.8


### Description

<span style="background-color: rgb(255, 255, 255);">The authentication method in Apache Doris versions before 2.0.0 was vulnerable to timing attacks.</span><br><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 2.0.0 + or 1.2.8, which fixes this issue.</span><br><p></p>

### References
* https://lists.apache.org/thread/jqczy3vxzs6q6rz9o0626j5nks9fnv95


### Credits
* Andrea Cosentino from  Apache Software Foundation  (reporter)


## Apache Doris hardcoded cryptography initialization ## { #CVE-2022-23942 }

CVE-2022-23942 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-23942) [\[CVE json\]](./CVE-2022-23942.cve.json) [\[OSV json\]](./CVE-2022-23942.osv.json)



_Last updated: 2022-04-26T14:49:46.143Z_

### Affected

* Apache Doris(Incubating) at 0.15.0


### Description

Apache Doris, prior to 1.0.0, used a hardcoded key and IV to initialize the cipher used for ldap password, which may lead to information disclosure.

### References
* https://lists.apache.org/thread/com2dyzp3bn2rdrotry90q2zzord4tvt


### Credits
* We would like to thanks to Dwi Siswanto<me@dw1.io> for the report of this issue
