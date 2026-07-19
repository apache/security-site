---
title: Apache Livy security advisories
description: Security information for Apache Livy
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Livy? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Livy).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unauthorized directory access ## { #CVE-2025-66249 }

CVE-2025-66249 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-66249) [\[CVE json\]](./CVE-2025-66249.cve.json) [\[OSV json\]](./CVE-2025-66249.osv.json)



_Last updated: 2026-04-10T15:57:26.189Z_

### Affected

* Apache Livy from 0.3.0-incubating before 0.9.0-incubating


### Description

<p>Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Livy.</p><p>This issue affects Apache Livy: from 0.3.0 before 0.9.0.</p><p>The vulnerability can only be exploited with non-default Apache Livy Server settings. If&nbsp;the configuration value "livy.file.local-dir-whitelist" is set to a non-default value, the directory checking can be bypassed.</p><p>Users are recommended to upgrade to version 0.9.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/1xwphsfn4jbtym4k4o0zlvwfogwqwwc3


### Credits
* Hiroki Egawa (finder)


## Restrict file access ## { #CVE-2025-60012 }

CVE-2025-60012 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-60012) [\[CVE json\]](./CVE-2025-60012.cve.json) [\[OSV json\]](./CVE-2025-60012.osv.json)



_Last updated: 2026-03-13T15:23:05.927Z_

### Affected

* Apache Livy from 0.7.0-incubating before 0.9.0-incubating


### Description

<p>Malicious configuration can lead to unauthorized file access in Apache Livy.</p><p>This issue affects Apache Livy 0.7.0 and 0.8.0 when connecting to Apache&nbsp;Spark 3.1 or later.</p><p>A request that includes a Spark configuration value supported from Apache&nbsp;Spark version 3.1 can lead to users gaining access to files they do not have permissions to.</p><p>For the vulnerability to be exploitable, the user needs to have access to Apache Livy's REST or JDBC interface and be able to send requests with arbitrary Spark configuration values.</p><p>Users are recommended to upgrade to version 0.9.0 or later, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/gpc85fwrgrbglpk9gm8tmcjzqnctx64w


### Credits
* Furue Hideyuki (finder)


## Apache Livy (Incubating) is vulnerable to cross site scripting ## { #CVE-2021-26544 }

CVE-2021-26544 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-26544) [\[CVE json\]](./CVE-2021-26544.cve.json) [\[OSV json\]](./CVE-2021-26544.osv.json)



_Last updated: 2021-02-20T08:56:02.977Z_

### Affected

* Apache Livy (Incubating) at 0.7.0-incubating


### Description

Livy server version 0.7.0-incubating (only) is vulnerable to a cross site scripting issue in the session name.  A malicious user could use this flaw to access logs and results of other users' sessions and run jobs with their privileges.  This issue is fixed in Livy 0.7.1-incubating.

### References
* https://github.com/apache/incubator-livy/commit/4d8a912699683b973eee76d4e91447d769a0cb0d
* https://lists.apache.org/thread.html/r2db14e7fd1e5ec2519e8828d43529bad623d75698cc7918af3a3f3ed%40%3Cuser.livy.apache.org%3E


### Credits
* We would like to thank Andras Beni for reporting this issue
