---
title: Apache SpamAssassin security advisories
description: Security information for Apache SpamAssassin
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache SpamAssassin? You can read more about the projects' security policy on their [security page](https://cwiki.apache.org/confluence/display/SPAMASSASSIN/SecurityPolicy), and email your report to the [Apache SpamAssassin Security Team](mailto:security@spamassassin.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://cwiki.apache.org/confluence/display/SPAMASSASSIN/SecurityPolicy). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache SpamAssassin has an OS Command Injection vulnerability ## { #CVE-2020-1946 }

CVE-2020-1946 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-1946) [\[CVE json\]](./CVE-2020-1946.cve.json) [\[OSV json\]](./CVE-2020-1946.osv.json)



_Last updated: 2021-03-25T09:15:51.926Z_

### Affected

* Apache SpamAssassin from Apache SpamAssassin before 3.4.5


### Description

In Apache SpamAssassin before 3.4.5, malicious rule configuration (.cf) files can be configured to run system commands without any output or errors. With this, exploits can be injected in a number of scenarios.  In addition to upgrading to SA version 3.4.5, users should only use update channels or 3rd party .cf files from trusted places. 

### References
* https://s.apache.org/3r1wh


### Credits
* Apache SpamAssassin would like to thank Damian Lukowski at credativ for ethically reporting this issue.
