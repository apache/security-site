---
title: Apache Commons security advisories
description: Security information for Apache Commons
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Commons? You can read more about the projects' security policy on their [security page](https://commons.apache.org/security.html), and email your report to the  [Apache Commons Security Team](mailto:security@commons.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://commons.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## FileUpload DoS with excessive parts ## { #CVE-2023-24998 }

CVE-2023-24998 [\[CVE json\]](./CVE-2023-24998.cve.json)

### Affected

* Apache Commons FileUpload before 1.5
* Apache Tomcat at 11.0.0-M1
* Apache Tomcat from 10.0.0-M1 through 10.1.4
* Apache Tomcat from 9.0.0-M1 through 9.0.70
* Apache Tomcat from 8.5.0 through 8.5.84


### Description

<div>Apache Commons FileUpload before 1.5 does not limit the number of request parts to be processed resulting in the possibility of an attacker triggering a DoS with a malicious upload or series of uploads.</div><div><br></div><div>Note that, like all of the file upload limits, the
          new configuration option (FileUploadBase#setFileCountMax) is not
          enabled by default and must be explicitly configured.<br></div>

### References
* https://lists.apache.org/thread/4xl4l09mhwg4vgsk7dxqogcjrobrrdoy


### Credits
* Jakob Ackermann (finder)
