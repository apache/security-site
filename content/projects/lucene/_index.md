---
title: Apache Lucene security advisories
description: Security information for Apache Lucene
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Lucene? Send your report to the [Apache Lucene Security Team](mailto:security@lucene.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Security Vulnerability in Lucene Replicator - Deserialization Issue ## { #CVE-2024-45772 }

CVE-2024-45772 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45772) [\[CVE json\]](./CVE-2024-45772.cve.json) [\[OSV json\]](./CVE-2024-45772.osv.json)



_Last updated: 2024-12-10T17:34:29.725Z_

### Affected

* Apache Lucene Replicator from 4.4.0 before 9.12.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Lucene Replicator.</p><p>This issue affects Apache Lucene's replicator module: from 4.4.0 before 9.12.0.<br>The deprecated org.apache.lucene.replicator.http package is affected.<br>The org.apache.lucene.replicator.nrt package is not affected.</p><p><span style="background-color: var(--wht);">Users are recommended to upgrade to version 9.12.0, which fixes the issue.</span></p><p><span style="background-color: var(--wht);">Java serialization filters (such as&nbsp;<span style="background-color: rgb(255, 255, 255);">-Djdk.serialFilter='!*' on the commandline) can mitigate the issue on vulnerable versions without impacting functionality.</span></span></p>

### References
* https://lists.apache.org/thread/3f3oph7bqnqspb9q5p0gm5mgc1b6thjo


### Credits
* Summ3r from Vidar-Team (finder)
* Paul Irwin from Apache Lucene.NET (coordinator)
