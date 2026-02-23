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

## Maven Archetype integration-test may package local settings into the published artifact, possibly containing credentials ## { #CVE-2024-47197 }

CVE-2024-47197 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-47197) [\[CVE json\]](./CVE-2024-47197.cve.json) [\[OSV json\]](./CVE-2024-47197.osv.json)



_Last updated: 2024-09-26T08:01:19.076Z_

### Affected

* Maven Archetype Plugin from 3.2.1 before 3.3.0


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor, Insecure Storage of Sensitive Information vulnerability in Maven Archetype Plugin.</p><p>This issue affects Maven Archetype Plugin: from 3.2.1 before 3.3.0.</p><p>Users are recommended to upgrade to version 3.3.0, which fixes the issue.</p><span style="background-color: rgb(255, 255, 255);">Archetype integration testing creates a file
called ./target/classes/archetype-it/archetype-settings.xml
This file contains all the content from the users ~/.m2/settings.xml file,
which often contains information they do not want to publish. We expect that on many developer machines, this also contains
credentials.<br><br><span style="background-color: rgb(255, 255, 255);">When the user runs </span></span><tt><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">mvn verify</span></span></tt><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);"> again (without a </span></span><tt><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">mvn clean</span></span></tt><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">), this file becomes part of
the final artifact.<br><br><span style="background-color: rgb(255, 255, 255);">If a developer were to publish this into Maven Central or any other remote repository (whether as a release
or a snapshot) their credentials would be published without them knowing.</span></span></span><br>

### References
* https://lists.apache.org/thread/ftg81np183wnyk0kg4ks95dvgxdrof96


### Credits
* Niels Basjes (reporter)


## Commandline class shell injection vulnerabilities ## { #CVE-2022-29599 }

CVE-2022-29599 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-29599) [\[CVE json\]](./CVE-2022-29599.cve.json) [\[OSV json\]](./CVE-2022-29599.osv.json)



_Last updated: 2022-05-23T10:22:16.632Z_

### Affected

* Apache Maven from maven-shared-utils before 3.3.3


### Description

In Apache Maven maven-shared-utils prior to version 3.3.3, the Commandline class can emit double-quoted strings without proper escaping, allowing shell injection attacks.

### References
* https://issues.apache.org/jira/browse/MSHARED-297
* https://github.com/apache/maven-shared-utils/pull/40


## block repositories using http by default ## { #CVE-2021-26291 }

CVE-2021-26291 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-26291) [\[CVE json\]](./CVE-2021-26291.cve.json) [\[OSV json\]](./CVE-2021-26291.osv.json)



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
