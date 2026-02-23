---
title: Apache Helix security advisories
description: Security information for Apache Helix
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Helix? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Helix front hard-coded secret in the express-session ## { #CVE-2024-22281 }

CVE-2024-22281 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-22281) [\[CVE json\]](./CVE-2024-22281.cve.json) [\[OSV json\]](./CVE-2024-22281.osv.json)



_Last updated: 2024-08-20T22:11:36.792Z_

### Affected

* Apache Helix Front (UI) through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** The Apache Helix Front (UI) component contained a hard-coded secret, allowing an attacker to spoof sessions by generating their own fake cookies.<br></p><p>This issue affects Apache Helix Front (UI): all versions.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/zt26fpmrqx3fzcy8nv3b43kb3xllo5ny


### Credits
* Jonathan Leitschuh (finder)


## Deserialization vulnerability in Helix workflow and REST ## { #CVE-2023-38647 }

CVE-2023-38647 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-38647) [\[CVE json\]](./CVE-2023-38647.cve.json) [\[OSV json\]](./CVE-2023-38647.osv.json)



_Last updated: 2023-07-26T07:52:23.420Z_

### Affected

* Apache Helix through 1.2.0


### Description

<p><span style="background-color: rgb(255, 255, 255);">An attacker can use SnakeYAML to deserialize java.net.URLClassLoader and make it load a JAR from a specified URL, and then deserialize javax.script.</span><span style="background-color: rgb(255, 255, 255);">ScriptEngineManager to load code using that ClassLoader. <span style="background-color: rgb(255, 255, 255);">This unbounded deserialization can likely lead to remote code execution.&nbsp;</span>The code can be run in Helix REST start and Workflow creation.</span><br><span style="background-color: var(--wht);"><br></span></p><p><span style="background-color: var(--wht);">Affect all the versions lower and include 1.2.0.</span></p><p><span style="background-color: var(--wht);">Affected products: helix-core, helix-rest</span></p><p><span style="background-color: var(--wht);">Mitigation: Short term, stop using any YAML based configuration and workflow creation.</span><br><span style="background-color: var(--wht);">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Long term, all Helix version bumping up to 1.3.0&nbsp;</span><br></p>

### References
* https://lists.apache.org/thread/zyqxhv0lc2z9w3tgr8ttrdy2zfh5jvc4


### Credits
* Qing Xu (reporter)


## Open redirect ## { #CVE-2022-47500 }

CVE-2022-47500 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-47500) [\[CVE json\]](./CVE-2022-47500.cve.json) [\[OSV json\]](./CVE-2022-47500.osv.json)



_Last updated: 2022-12-19T09:23:48.197Z_

### Affected

* Apache Helix from 0.8.0 through 1.0.4


### Description

URL Redirection to Untrusted Site ('Open Redirect') vulnerability in Apache Software Foundation Apache Helix UI component.<p>This issue affects Apache Helix all releases from 0.8.0 to 1.0.4.</p><p></p><b>Solution</b>: removed the the forward component since it was improper designed for UI embedding.<br><br><span style="background-color: rgb(255, 255, 255);">&nbsp;User please upgrade to 1.1.0 to fix this issue.<br></span><br>

### References
* https://lists.apache.org/thread/lr74xtxxbb1t3dfn5qzzwl2xjr3qlbmh


### Credits
* This issue was discovered by Everardo Padilla Saca (reporter)
