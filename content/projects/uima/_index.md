---
title: Apache UIMA security advisories
description: Security information for Apache UIMA
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache UIMA? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## DUCC (EOL) allows RCE ## { #CVE-2023-28935 }

CVE-2023-28935 [\[CVE json\]](./CVE-2023-28935.cve.json)

### Affected

* Apache UIMA DUCC through *


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache UIMA DUCC.<br></div><div>When using the "Distributed UIMA Cluster Computing" (DUCC) module of Apache UIMA, an authenticated user that has the permissions to modify core entities can cause command execution as the system user that runs the web process.<br></div><div>As the "Distributed UIMA Cluster Computing" module for UIMA is retired, we do not plan to release a fix for this issue.<br>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</div>

### References
* https://lists.apache.org/thread/r19z14b9rrfxv72r93q5trq5tyffo75g


### Credits
* Crilwa (finder)
