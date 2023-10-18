---
title: Apache Felix security advisories
description: Security information for Apache Felix
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Felix? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## XSS in healthcheck webconsole plugin ## { #CVE-2023-38435 }

CVE-2023-38435 [\[CVE json\]](./CVE-2023-38435.cve.json)

### Affected

* Apache Felix Healthcheck Webconsole Plugin through 2.0.2


### Description



An improper neutralization of input during web page generation ('Cross-site Scripting') [CWE-79] vulnerability in Apache Felix Healthcheck Webconsole Plugin version 2.0.2 and prior may allow an attacker to perform a reflected cross-site scripting (XSS) attack.<br><br><span style="background-color: rgb(255, 255, 255);">Upgrade to Apache Felix Healthcheck Webconsole Plugin 2.1.0 or higher.</span>

### References
* https://lists.apache.org/thread/r3blhp3onr4rdbkgdyglqnccg0v79pfv


### Credits
*  This vulnerability was found by xray web vulnerability scanner (github.com/chaitin/xray) (finder)
