---
title: Apache Axis security advisories
description: Security information for Apache Axis
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Axis? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Axis 1.x (EOL) may allow RCE when untrusted input is passed to getService ## { #CVE-2023-40743 }

CVE-2023-40743 [\[CVE json\]](./CVE-2023-40743.cve.json)

### Affected

* Apache Axis through 1.3


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** When integrating Apache Axis 1.x in an application, it may not have been obvious that looking up a service through "ServiceFactory.getService" allows potentially dangerous lookup mechanisms such as LDAP. When passing untrusted input to this API method, this could expose the application to DoS, SSRF and even attacks leading to RCE.</div><div><br></div><div>As Axis 1 has been EOL we recommend you migrate to a different SOAP engine, such as Apache Axis 2/Java. As a workaround, you may review your code to verify no untrusted or unsanitized input is passed to "ServiceFactory.getService", or by applying the patch from <a target="_blank" rel="nofollow" href="https://github.com/apache/axis-axis1-java/commit/7e66753427466590d6def0125e448d2791723210">https://github.com/apache/axis-axis1-java/commit/7e66753427466590d6def0125e448d2791723210</a>. The Apache Axis project does not expect to create an Axis 1.x release fixing this problem, though contributors that would like to work towards this are welcome.<br></div>

### References
* https://github.com/apache/axis-axis1-java/commit/7e66753427466590d6def0125e448d2791723210
* https://lists.apache.org/thread/gs0qgk2mgss7zfhzdd6ftfjvm4kp7v82


### Credits
* Letian Yuan (finder)
