---
title: Apache Helix security advisories
description: Security information for Apache Helix
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Helix? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Helix since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Open redirect ## { #CVE-2022-47500 }

[CVE-2022-47500](./CVE-2022-47500.cve.json)

### Affected

* Apache Helix from 0.8.0 through 1.0.4


### Description

URL Redirection to Untrusted Site ('Open Redirect') vulnerability in Apache Software Foundation Apache Helix UI component.<p>This issue affects Apache Helix all releases from 0.8.0 to 1.0.4.</p><p></p><b>Solution</b>: removed the the forward component since it was improper designed for UI embedding.<br><br><span style="background-color: rgb(255, 255, 255);">&nbsp;User please upgrade to 1.1.0 to fix this issue.<br></span><br>

### References
* https://lists.apache.org/thread/lr74xtxxbb1t3dfn5qzzwl2xjr3qlbmh
