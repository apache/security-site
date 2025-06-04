---
title: Apache Pekko security advisories
description: Security information for Apache Pekko
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Pekko? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## management API basic authentication is not effective ## { #CVE-2025-46548 }

CVE-2025-46548 [\[CVE json\]](./CVE-2025-46548.cve.json) [\[OSV json\]](./CVE-2025-46548.osv.json)



_Last updated: 2025-06-03T14:45:30.963Z_

### Affected

* Apache Pekko Management from 1.0.0 before 1.1.1
* Apache Pekko Management from 1.0.0 before 1.1.1
* Apache Pekko Management from 1.0.0 before 1.1.1


### Description

<div>If you enable Basic Authentication in Pekko Management using the Java DSL, the authenticator may not be properly applied.<br></div><div>Users that rely on authentication instead of making sure the Management API ports are only available to trusted users are recommended to upgrade to version 1.1.1, which fixes this issue.</div>

### References
* https://github.com/apache/pekko-management/pull/418
* https://github.com/akka/akka-management/pull/1385
* https://lists.apache.org/thread/tnd84hj9w0ggjcft6cp12q67d5jzhp66


### Credits
* Per-Ivar Bakke of GE Vernova (finder)
