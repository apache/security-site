---
title: Apache Axis security advisories
description: Security information for Apache Axis
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Axis? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Axis).

You can read more about the security policy on:

- [Apache Axis2 Java Core security model](https://github.com/apache/axis-axis2-java-core/security/policy)
- [Apache Axis2 Java Rampart security model](https://github.com/apache/axis-axis2-java-rampart/security/policy)
- [Apache Axis2 C Core security model](https://github.com/apache/axis-axis2-c-core/security/policy)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security pages linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## deserialization of untrusted Data ## { #CVE-2026-66713 }

CVE-2026-66713 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66713) [\[CVE json\]](./CVE-2026-66713.cve.json) [\[OSV json\]](./CVE-2026-66713.osv.json)



_Last updated: 2026-07-28T13:44:22.395Z_

### Affected

* Apache Axis2/Java through 2.0.0


### Description

<span style="background-color: rgb(255, 255, 255);">Deserialization</span> <span style="background-color: rgb(255, 255, 255);">of</span> <span style="background-color: rgb(255, 255, 255);">Untrusted</span> <span style="background-color: rgb(255, 255, 255);">Data</span> <span style="background-color: rgb(255, 255, 255);">(CWE-502)</span> <span style="background-color: rgb(255, 255, 255);">in</span> <span style="background-color: rgb(255, 255, 255);">the</span> <span style="background-color: rgb(255, 255, 255);">Tribes-based</span> <span style="background-color: rgb(255, 255, 255);">clustering</span> <span style="background-color: rgb(255, 255, 255);">component</span>
<br><span style="background-color: rgb(255, 255, 255);"> &nbsp;in Apache Software Foundation Apache Axis2/Java through 2.0.0 on Apache Tomcat</span>
<br><span style="background-color: rgb(255, 255, 255);"> &nbsp;</span><span style="background-color: rgb(255, 255, 255);">(only</span> <span style="background-color: rgb(255, 255, 255);">when</span> <span style="background-color: rgb(255, 255, 255);">Tribes</span> <span style="background-color: rgb(255, 255, 255);">clustering</span> <span style="background-color: rgb(255, 255, 255);">is</span> <span style="background-color: rgb(255, 255, 255);">enabled,</span> <span style="background-color: rgb(255, 255, 255);">which</span> <span style="background-color: rgb(255, 255, 255);">is</span> <span style="background-color: rgb(255, 255, 255);">off</span> <span style="background-color: rgb(255, 255, 255);">by</span> <span style="background-color: rgb(255, 255, 255);">default)</span> <span style="background-color: rgb(255, 255, 255);">allows</span> <span style="background-color: rgb(255, 255, 255);">an</span>
<br><span style="background-color: rgb(255, 255, 255);"> &nbsp;unauthenticated remote attacker with network access to the clustering port to</span>
<br><span style="background-color: rgb(255, 255, 255);"> &nbsp;execute</span> <span style="background-color: rgb(255, 255, 255);">arbitrary</span> <span style="background-color: rgb(255, 255, 255);">code</span> <span style="background-color: rgb(255, 255, 255);">via</span> <span style="background-color: rgb(255, 255, 255);">a</span> <span style="background-color: rgb(255, 255, 255);">crafted</span> <span style="background-color: rgb(255, 255, 255);">serialized</span> <span style="background-color: rgb(255, 255, 255);">Java</span> <span style="background-color: rgb(255, 255, 255);">object</span> <span style="background-color: rgb(255, 255, 255);">delivered</span> <span style="background-color: rgb(255, 255, 255);">to</span> <span style="background-color: rgb(255, 255, 255);">the</span> <span style="background-color: rgb(255, 255, 255);">cluster</span>
<br><span style="background-color: rgb(255, 255, 255);"> &nbsp;</span><span style="background-color: rgb(255, 255, 255);">channel</span> <span style="background-color: rgb(255, 255, 255);">and</span> <span style="background-color: rgb(255, 255, 255);">deserialized</span> <span style="background-color: rgb(255, 255, 255);">in</span>
<br><span style="background-color: rgb(255, 255, 255);"> &nbsp;org.apache.axis2.clustering.tribes.Axis2ChannelListener#messageReceived. Users are</span>
<br><span style="background-color: rgb(255, 255, 255);"> &nbsp;recommended</span> <span style="background-color: rgb(255, 255, 255);">to</span> <span style="background-color: rgb(255, 255, 255);">upgrade</span> <span style="background-color: rgb(255, 255, 255);">to</span> <span style="background-color: rgb(255, 255, 255);">version</span> <span style="background-color: rgb(255, 255, 255);">2.0.1,</span> <span style="background-color: rgb(255, 255, 255);">which</span> <span style="background-color: rgb(255, 255, 255);">fixes</span> <span style="background-color: rgb(255, 255, 255);">this</span> <span style="background-color: rgb(255, 255, 255);">issue</span> <span style="background-color: rgb(255, 255, 255);">by</span> <span style="background-color: rgb(255, 255, 255);">removing</span> <span style="background-color: rgb(255, 255, 255);">the</span>
<br><span style="background-color: rgb(255, 255, 255);"> &nbsp;clustering feature entirely.</span><br>
<br>

<br>

### References
* https://github.com/apache/axis-axis2-java-core/commit/e6f53b230bddcb40577c84ff290ba51e7265fa15
* https://lists.apache.org/thread/fgggbv3sjjqw7p6q0j88gspt9b2rb728


### Credits
* liuhuajin of Huawei (finder)


## Apache Axis 1.x (EOL) may allow SSRF when untrusted input is passed to the service admin HTTP API ## { #CVE-2023-51441 }

CVE-2023-51441 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-51441) [\[CVE json\]](./CVE-2023-51441.cve.json) [\[OSV json\]](./CVE-2023-51441.osv.json)



_Last updated: 2024-01-31T09:07:08.922Z_

### Affected

* Apache Axis through 1.3


### Description

** UNSUPPORTED WHEN ASSIGNED ** Improper Input Validation vulnerability in Apache Axis allowed users with access to the admin service to perform possible SSRF<br><p>This issue affects Apache Axis: through 1.3.</p><p>As Axis 1 has been EOL we recommend you migrate to a different SOAP engine, such as Apache Axis 2/Java. Alternatively you could use a build of Axis with the patch from <a target="_blank" rel="nofollow" href="https://github.com/apache/axis-axis1-java/commit/685c309febc64aa393b2d64a05f90e7eb9f73e06">https://github.com/apache/axis-axis1-java/commit/685c309febc64aa393b2d64a05f90e7eb9f73e06</a> applied. The Apache Axis project does not expect to create an Axis 1.x release 
fixing this problem, though contributors that would like to work towards
 this are welcome.
</p>

### References
* https://github.com/apache/axis-axis1-java/commit/685c309febc64aa393b2d64a05f90e7eb9f73e06
* https://lists.apache.org/thread/8nrm5thop8f82pglx4o0jg8wmvy6d9yd


### Credits
* thiscodecc of MoyunSec Vlab and Bing (finder)


## Apache Axis 1.x (EOL) may allow RCE when untrusted input is passed to getService ## { #CVE-2023-40743 }

CVE-2023-40743 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-40743) [\[CVE json\]](./CVE-2023-40743.cve.json) [\[OSV json\]](./CVE-2023-40743.osv.json)



_Last updated: 2023-09-05T14:42:08.579Z_

### Affected

* Apache Axis through 1.3


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** When integrating Apache Axis 1.x in an application, it may not have been obvious that looking up a service through "ServiceFactory.getService" allows potentially dangerous lookup mechanisms such as LDAP. When passing untrusted input to this API method, this could expose the application to DoS, SSRF and even attacks leading to RCE.</div><div><br></div><div>As Axis 1 has been EOL we recommend you migrate to a different SOAP engine, such as Apache Axis 2/Java. As a workaround, you may review your code to verify no untrusted or unsanitized input is passed to "ServiceFactory.getService", or by applying the patch from <a target="_blank" rel="nofollow" href="https://github.com/apache/axis-axis1-java/commit/7e66753427466590d6def0125e448d2791723210">https://github.com/apache/axis-axis1-java/commit/7e66753427466590d6def0125e448d2791723210</a>. The Apache Axis project does not expect to create an Axis 1.x release fixing this problem, though contributors that would like to work towards this are welcome.<br></div>

### References
* https://github.com/apache/axis-axis1-java/commit/7e66753427466590d6def0125e448d2791723210
* https://lists.apache.org/thread/gs0qgk2mgss7zfhzdd6ftfjvm4kp7v82


### Credits
* Letian Yuan (finder)
