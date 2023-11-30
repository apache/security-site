---
title: Apache Livy (Incubating) security advisories
description: Security information for Apache Livy (Incubating)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Livy (Incubating)? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Livy (Incubating) is vulnerable to cross site scripting ## { #CVE-2021-26544 }

CVE-2021-26544 [\[CVE json\]](./CVE-2021-26544.cve.json)

### Affected

* Apache Livy (Incubating) at 0.7.0-incubating


### Description

Livy server version 0.7.0-incubating (only) is vulnerable to a cross site scripting issue in the session name.  A malicious user could use this flaw to access logs and results of other users' sessions and run jobs with their privileges.  This issue is fixed in Livy 0.7.1-incubating.

### References
* https://github.com/apache/incubator-livy/commit/4d8a912699683b973eee76d4e91447d769a0cb0d
* https://lists.apache.org/thread.html/r2db14e7fd1e5ec2519e8828d43529bad623d75698cc7918af3a3f3ed%40%3Cuser.livy.apache.org%3E


### Credits
* We would like to thank Andras Beni for reporting this issue
