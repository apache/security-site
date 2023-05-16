---
title: Apache Commons security advisories
description: Security information for Apache Commons
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Commons? You can read more about the projects' security policy on their [security page](https://commons.apache.org/security.html), and email your report to the  [Apache Commons Security Team](mailto:security@commons.apache.org).

# Advisories

## FileUpload DoS with excessive parts ## { #CVE-2023-24998 }

[CVE-2023-24998](./CVE-2023-24998.cve.json)

### Affected

* Apache Commons FileUpload versions  before 1.5
* Apache Tomcat versions 11.0.0-M110.0.0-M1 including 10.1.49.0.0-M1 including 9.0.708.5.0 including 8.5.84


### Description

<div>Apache Commons FileUpload before 1.5 does not limit the number of request parts to be processed resulting in the possibility of an attacker triggering a DoS with a malicious upload or series of uploads.</div><div><br></div><div>Note that, like all of the file upload limits, the
          new configuration option (FileUploadBase#setFileCountMax) is not
          enabled by default and must be explicitly configured.<br></div>