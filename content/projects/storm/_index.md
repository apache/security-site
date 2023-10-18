---
title: Apache Storm security advisories
description: Security information for Apache Storm
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Storm? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Shell Command Injection Vulnerability in Nimbus Thrift Server ## { #CVE-2021-38294 }

CVE-2021-38294 [\[CVE json\]](./CVE-2021-38294.cve.json)

### Affected

* Apache Storm from v1.0.0 before Apache Storm*
* Apache Storm from Apache Storm before v1.2.4


### Description

A Command Injection vulnerability exists in the getTopologyHistory service of the Apache Storm 2.x prior to 2.2.1 and Apache Storm 1.x prior to 1.2.4. A specially crafted thrift request to the Nimbus server allows Remote Code Execution (RCE) prior to authentication. 

### References
* https://lists.apache.org/thread.html/r5fe881f6ca883908b7a0f005d35115af49f43beea7a8b0915e377859%40%3Cuser.storm.apache.org%3E
* https://seclists.org/oss-sec/2021/q4/44


### Credits
* Apache Storm would like to thank @pwntester Alvaro Muñoz of the GitHub Security Lab team for reporting this issue.


## Unsafe Pre-Authentication Deserialization In Workers ## { #CVE-2021-40865 }

CVE-2021-40865 [\[CVE json\]](./CVE-2021-40865.cve.json)

### Affected

* Apache Storm from v1.0.0 before Apache Storm *
* Apache Storm from Apache Storm before v1.2.4


### Description

An Unsafe Deserialization vulnerability exists in the worker services of the Apache Storm supervisor server allowing pre-auth Remote Code Execution (RCE).  Apache Storm 2.2.x users should upgrade to version 2.2.1 or 2.3.0. Apache Storm 2.1.x users should upgrade to version 2.1.1. Apache Storm 1.x users should upgrade to version 1.2.4

### References
* https://lists.apache.org/thread.html/r8d45e74299897b6734dd0f788c46a631009ce2eeb731523386f7a253%40%3Cuser.storm.apache.org%3E
* https://seclists.org/oss-sec/2021/q4/45


### Credits
* Apache Storm would like to thank @pwntester Alvaro Muñoz of the GitHub Security Lab team for reporting this issue.
