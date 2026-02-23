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

## XSS in HTTP Webconsole Plugin ## { #CVE-2025-27867 }

CVE-2025-27867 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27867) [\[CVE json\]](./CVE-2025-27867.cve.json) [\[OSV json\]](./CVE-2025-27867.osv.json)



_Last updated: 2025-03-12T15:51:23.297Z_

### Affected

* Apache Felix HTTP Webconsole Plugin from 1.x through 1.2.0


### Description

<p>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Felix HTTP Webconsole Plugin.</p><p>This issue affects Apache Felix HTTP Webconsole Plugin: from Version 1.X through 1.2.0.</p><p>Users are recommended to upgrade to version 1.2.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/y83f2rvm8bccr5ctgv7mzxd69p6f77dp


### Credits
* Viktor Mares (me@viktormares.com) (finder)


## XSS in services console ## { #CVE-2025-25247 }

CVE-2025-25247 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-25247) [\[CVE json\]](./CVE-2025-25247.cve.json) [\[OSV json\]](./CVE-2025-25247.osv.json)



_Last updated: 2025-02-10T11:16:58.175Z_

### Affected

* Apache Felix Webconsole from Version 4.x through 4.9.8
* Apache Felix Webconsole from Version 5.x through 5.0.8


### Description

<p>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Felix Webconsole.</p><p>This issue affects Apache Felix Webconsole 4.x up to 4.9.8 and 5.x up to 5.0.8.</p><p>Users are recommended to upgrade to version 4.9.10 or 5.0.10 or higher, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/z47jbf0rbylzd0ktfzdw9c8b5fpyl24m


### Credits
* Viktor Mares (me@viktormares.com) (finder)


## XSS in healthcheck webconsole plugin ## { #CVE-2023-38435 }

CVE-2023-38435 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-38435) [\[CVE json\]](./CVE-2023-38435.cve.json) [\[OSV json\]](./CVE-2023-38435.osv.json)



_Last updated: 2023-07-31T08:08:18.396Z_

### Affected

* Apache Felix Healthcheck Webconsole Plugin through 2.0.2


### Description



An improper neutralization of input during web page generation ('Cross-site Scripting') [CWE-79] vulnerability in Apache Felix Healthcheck Webconsole Plugin version 2.0.2 and prior may allow an attacker to perform a reflected cross-site scripting (XSS) attack.<br><br><span style="background-color: rgb(255, 255, 255);">Upgrade to Apache Felix Healthcheck Webconsole Plugin 2.1.0 or higher.</span>

### References
* https://lists.apache.org/thread/r3blhp3onr4rdbkgdyglqnccg0v79pfv


### Credits
*  This vulnerability was found by xray web vulnerability scanner (github.com/chaitin/xray) (finder)
