---
title: Apache Allura security advisories
description: Security information for Apache Allura
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Allura? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## sensitive information exposure via import ## { #CVE-2023-46851 }

CVE-2023-46851 [\[CVE json\]](./CVE-2023-46851.cve.json)

### Affected

* Apache Allura from 1.0.1 through 1.15.0


### Description

<div>Allura Discussion and Allura Forum importing does not restrict URL values specified in attachments. Project administrators can run these imports, which could cause Allura to read local files and expose them.&nbsp; Exposing internal files then can lead to other exploits, like session hijacking, or remote code execution.<br></div><div><br></div><div>This issue affects Apache Allura from 1.0.1 through 1.15.0.</div><p></p><p>Users are recommended to upgrade to version 1.16.0, which fixes the issue.&nbsp; If you are unable to upgrade, set "disable_entry_points.allura.importers = forge-tracker, forge-discussion" in your .ini config file.<br></p>

### References
* https://allura.apache.org/posts/2023-allura-1.16.0.html
* https://lists.apache.org/thread/hqk0vltl7qgrq215zgwjfoj0khbov0gx


### Credits
* Stefan Schiller (Sonar) (finder)
