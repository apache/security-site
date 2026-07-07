---
title: Apache Lucene.NET security advisories
description: Security information for Apache Lucene.NET
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Lucene.NET? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## XXE vulnerability in Lucene.Net.Analysis.Common PatternParser ## { #CVE-2026-47898 }

CVE-2026-47898 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-47898) [\[CVE json\]](./CVE-2026-47898.cve.json) [\[OSV json\]](./CVE-2026-47898.osv.json)



_Last updated: 2026-07-03T07:47:36.852Z_

### Affected

* Apache Lucene.Net from 4.8.0-beta00005 before 4.8.0-beta00018


### Description

<p>Improper Restriction of XML External Entity Reference vulnerability in Apache Lucene.Net (Lucene.Net.Analysis.Common library).</p><p>This issue affects Apache Lucene.Net.Analysis.Common: from 4.8.0-beta00005 before 4.8.0-beta00018.</p><p>Users are recommended to upgrade to version 4.8.0-beta00018, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7yn9k6sbbsk18yco5y2hszpcf8dst489


### Credits
* Daniel Cervera (reporter)
* Paul Irwin (coordinator)
* Shad Storhaug (remediation reviewer)


## Arbitrary file write from malicious server to Lucene.Net.Replicator client ## { #CVE-2026-47897 }

CVE-2026-47897 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-47897) [\[CVE json\]](./CVE-2026-47897.cve.json) [\[OSV json\]](./CVE-2026-47897.osv.json)



_Last updated: 2026-07-03T07:48:10.017Z_

### Affected

* Apache Lucene.Net from 4.8.0-beta00005 before 4.8.0-beta00018


### Description

<p>Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Lucene.Net (Lucene.Net.Replicator library).</p><p>This issue affects Apache Lucene.Net.Replicator: from 4.8.0-beta00005 before 4.8.0-beta00018.</p><p>Users are recommended to upgrade to version 4.8.0-beta00018, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/on1j3zmvgtf8n9fw78z3lyf6dn94p5zc


### Credits
* Daniel Cervera (reporter)
* Paul Irwin (coordinator)
* Shad Storhaug (remediation reviewer)


## Unauthenticated arbitrary file read on the Lucene.Net.Replicator replication server ## { #CVE-2026-47896 }

CVE-2026-47896 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-47896) [\[CVE json\]](./CVE-2026-47896.cve.json) [\[OSV json\]](./CVE-2026-47896.osv.json)



_Last updated: 2026-07-03T07:48:34.009Z_

### Affected

* Apache Lucene.Net from 4.8.0-beta00005 before 4.8.0-beta00018


### Description

<p>Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Lucene.Net (Lucene.Net.Replicator library).</p><p>This issue affects Apache Lucene.Net.Replicator: from 4.8.0-beta00005 through 4.8.0-beta00017.</p><p>Users are recommended to upgrade to version 4.8.0-beta00018, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7y9gbt17p55fh1zltks4pnh719wq9sqt


### Credits
* Daniel Cervera (reporter)
* Paul Irwin (coordinator)
* Shad Storhaug (remediation reviewer)


## Remote Code Execution in Lucene.Net.Replicator ## { #CVE-2024-43383 }

CVE-2024-43383 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-43383) [\[CVE json\]](./CVE-2024-43383.cve.json) [\[OSV json\]](./CVE-2024-43383.osv.json)



_Last updated: 2024-10-31T09:57:26.362Z_

### Affected

* Apache Lucene.Net.Replicator from 4.8.0-beta00005 through 4.8.0-beta00016


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Lucene.Net.Replicator.</p><p>This issue affects Apache Lucene.NET's Replicator library: from 4.8.0-beta00005 through 4.8.0-beta00016.</p><p>An attacker that can intercept traffic between a replication client and server, or control the target replication node URL, can provide a specially-crafted JSON response that is deserialized as an attacker-provided exception type. This can result in remote code execution or other potential unauthorized access.<br></p><p>Users are recommended to upgrade to version 4.8.0-beta00017, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/wlz1p76dxpt4rl9o29voxjd5zl7717nh


### Credits
* Summ3r, Vidar-Team (reporter)
* Apache Lucene (remediation developer)
