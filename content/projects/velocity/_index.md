---
title: Apache Velocity security advisories
description: Security information for Apache Velocity
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Velocity? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Velocity Tools XSS Vulnerability ## { #CVE-2020-13959 }

CVE-2020-13959 [\[CVE json\]](./CVE-2020-13959.cve.json) [\[OSV json\]](./CVE-2020-13959.osv.json)



_Last updated: 2021-03-10T07:52:04.870Z_

### Affected

* Apache Velocity Tools from Apache Velocity Tools before 3.1


### Description

The default error page for VelocityView in Apache Velocity Tools prior to 3.1 reflects back the vm file that was entered as part of the URL.  An attacker can set an XSS payload file as this vm file in the URL which results in this payload being executed.   
XSS vulnerabilities allow attackers to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim or for phishing attacks.

### References
* https://lists.apache.org/thread.html/r6802a38c3041059e763a1aadd7b37fe95de75408144b5805e29b84e3%40%3Cuser.velocity.apache.org%3E


### Credits
* This issue was reported and a patch was submitted by Jackson Henry, member of Sakura Samurai.


## Velocity Sandbox Bypass ## { #CVE-2020-13936 }

CVE-2020-13936 [\[CVE json\]](./CVE-2020-13936.cve.json) [\[OSV json\]](./CVE-2020-13936.osv.json)



_Last updated: 2021-03-10T07:51:18.089Z_

### Affected

* Apache Velocity Engine from Apache Velocity Engine through 2.2


### Description

An attacker that is able to modify Velocity templates may execute arbitrary Java code or run arbitrary system commands with the same privileges as the account running the Servlet container.  This applies to applications that allow untrusted users to upload/modify velocity templates running Apache Velocity Engine versions up to 2.2.

### References
* https://lists.apache.org/thread.html/r01043f584cbd47959fabe18fff64de940f81a65024bb8dddbda31d9a%40%3Cuser.velocity.apache.org%3E


### Credits
* This issue was discovered by Alvaro Munoz pwntester@github.com of Github Security Labs and was originally reported as GHSL-2020-048.
