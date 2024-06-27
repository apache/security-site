---
title: Apache Maven security advisories
description: Security information for Apache Maven
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Maven? You can read more about the projects' security policy on their [security page](https://maven.apache.org/security.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://maven.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## block repositories using http by default ## { #CVE-2021-26291 }

CVE-2021-26291 [\[CVE json\]](./CVE-2021-26291.cve.json) [\[OSV json\]](./CVE-2021-26291.osv.json)



_Last updated: 2021-04-23T14:14:28.607Z_

### Affected

* Apache Maven from Apache Maven through 3.8.1


### Description

Apache Maven will follow repositories that are defined in a dependency’s Project Object Model (pom) which may be surprising to some users, resulting in potential risk if a malicious actor takes over that repository or is able to insert themselves into a position to pretend to be that repository. Maven is changing the default behavior in 3.8.1+ to no longer follow http (non-SSL) repository references by default. More details available in the referenced urls.

If you are currently using a repository manager to govern the repositories used by your builds, you are unaffected by the risks present in the legacy behavior, and are unaffected by this vulnerability and change to default behavior. See this link for more information about repository management: https://maven.apache.org/repository-management.html

### References
* https://lists.apache.org/thread.html/r9a027668558264c4897633e66bcb7784099fdec9f9b22c38c2442f00%40%3Cusers.maven.apache.org%3E


### Credits
* Apache Maven would like to thank Jonathan Leitschuh for highlighting the need for this change.


## Commandline class shell injection vulnerabilities ## { #CVE-2022-29599 }

CVE-2022-29599 [\[CVE json\]](./CVE-2022-29599.cve.json) [\[OSV json\]](./CVE-2022-29599.osv.json)



_Last updated: 2022-05-23T10:22:16.632Z_

### Affected

* Apache Maven from maven-shared-utils before 3.3.3


### Description

In Apache Maven maven-shared-utils prior to version 3.3.3, the Commandline class can emit double-quoted strings without proper escaping, allowing shell injection attacks.

### References
* https://issues.apache.org/jira/browse/MSHARED-297
* https://github.com/apache/maven-shared-utils/pull/40
