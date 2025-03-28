---
title: Apache VCL security advisories
description: Security information for Apache VCL
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache VCL? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## SQL injection vulnerability in New Block Allocation form ## { #CVE-2024-53678 }

CVE-2024-53678 [\[CVE json\]](./CVE-2024-53678.cve.json) [\[OSV json\]](./CVE-2024-53678.osv.json)



_Last updated: 2025-03-25T09:33:34.457Z_

### Affected

* Apache VCL from 2.2 through 2.5.1


### Description

<p>Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache VCL. Users can modify form data submitted when requesting a new Block Allocation such that a SELECT SQL statement is modified. The data returned by the SELECT statement is not viewable by the attacker.</p><p>This issue affects all versions of Apache VCL from 2.2 through 2.5.1.</p><p>Users are recommended to upgrade to version 2.5.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/2bmjnzgjwwq59nv6xw44w0tnpz4k4pf4


### Credits
* Chiencp and Nothing from TeamTonTac (finder)


## XSS vulnerability in User Lookup impacting user privileges ## { #CVE-2024-53679 }

CVE-2024-53679 [\[CVE json\]](./CVE-2024-53679.cve.json) [\[OSV json\]](./CVE-2024-53679.osv.json)



_Last updated: 2025-03-25T09:33:43.087Z_

### Affected

* Apache VCL from 2.1 through 2.5.1


### Description

<p>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache VCL in the User Lookup form. A user with sufficient rights to be able to view this part of the site can craft a URL or be tricked in to clicking a URL that will give a specified user elevated rights.</p><p></p><p>This issue affects all versions of Apache VCL through 2.5.1.</p><p></p><p>Users are recommended to upgrade to version 2.5.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/bq5vs0hndt9cz9b6rpfr5on1nd4qrmyr


### Credits
* Chiencp and Nothing from TeamTonTac (finder)
