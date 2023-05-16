---
title: Apache Logging security advisories
description: Security information for Apache Logging
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Logging? You can read more about the projects' security policy on their [security page](None), and email your report to the  [Apache Logging Security Team](mailto:security@logging.apache.org).

# Advisories

## Apache Log4j 1.x (EOL) allows DoS in Chainsaw and SocketAppender ## { #CVE-2023-26464 }

[CVE-2023-26464](./CVE-2023-26464.cve.json)

### Affected

* Apache Log4j versions 1.0.4 before 22 including *


### Description

<div>** UNSUPPORTED WHEN ASSIGNED **</div><div>When using the Chainsaw or SocketAppender components with Log4j 1.x on JRE less than 1.7, an attacker that manages to cause a logging entry involving a specially-crafted (ie, deeply nested) 
hashmap or hashtable (depending on which logging component is in use) to be processed could exhaust the available memory in the virtual machine and achieve Denial of Service when the object is deserialized.</div><div>This issue affects Apache Log4j before 2. Affected users are recommended to update to Log4j 2.x.</div><div>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.<br></div><p></p>