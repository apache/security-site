---
title: Apache Traffic Server security advisories
description: Security information for Apache Traffic Server
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Traffic Server? You can read more about the projects' security policy on their [security page](None), and email your report to the  [Apache Traffic Server Security Team](mailto:security@trafficserver.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](None). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improperly handled requests can cause crashes in specific plugins ## { #CVE-2022-32749 }

CVE-2022-32749 [\[CVE json\]](./CVE-2022-32749.cve.json)

### Affected

* Apache Traffic Server from 8.0.0 through 9.1.3


### Description



Improper Check for Unusual or Exceptional Conditions vulnerability handling requests in Apache Traffic Server allows an attacker to crash the server under certain conditions.

<p>This issue affects Apache Traffic Server: from 8.0.0 through 9.1.3.</p>

### References
* https://lists.apache.org/thread/mrj2lg4s0hf027rk7gz8t7hbn9xpfg02


## Improperly reading the client requests ## { #CVE-2022-37392 }

CVE-2022-37392 [\[CVE json\]](./CVE-2022-37392.cve.json)

### Affected

* Apache Traffic Server from 8.0.0 through 9.1.3


### Description

Improper Check for Unusual or Exceptional Conditions vulnerability in handling the requests to Apache Traffic Server.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/mrj2lg4s0hf027rk7gz8t7hbn9xpfg02


## Security issues with the xdebug plugin ## { #CVE-2022-40743 }

CVE-2022-40743 [\[CVE json\]](./CVE-2022-40743.cve.json)

### Affected

* Apache Traffic Server from 9.0.0 through 9.1.3


### Description

Improper Input Validation vulnerability for the xdebug plugin in Apache Software Foundation Apache Traffic Server can lead to cross site scripting and cache poisoning attacks.<p>This issue affects Apache Traffic Server: 9.0.0 to 9.1.3. Users should upgrade to 9.1.4 or later versions.<br></p>

### References
* https://lists.apache.org/thread/mrj2lg4s0hf027rk7gz8t7hbn9xpfg02


## The TRACE method can be use to disclose network information ## { #CVE-2022-47184 }

CVE-2022-47184 [\[CVE json\]](./CVE-2022-47184.cve.json)

### Affected

* Apache Traffic Server from 8.0.0 through 9.2.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Traffic Server.<p>This issue affects Apache Traffic Server: 8.0.0 to 9.2.0.</p>

### References
* https://lists.apache.org/thread/tns2b4khyyncgs5v5p9y35pobg9z2bvs


## Configuration option to block the PUSH method in ATS didn't work ## { #CVE-2023-30631 }

CVE-2023-30631 [\[CVE json\]](./CVE-2023-30631.cve.json)

### Affected

* Apache Traffic Server from 8.0.0 through 9.2.0


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Traffic Server.&nbsp; The configuration option&nbsp;proxy.config.http.push_method_enabled didn't function.&nbsp; However, by default the PUSH method is blocked in the ip_allow configuration file.<p>This issue affects Apache Traffic Server: from 8.0.0 through 9.2.0.</p><p>8.x users should upgrade to 8.1.7 or later versions<br>9.x users should upgrade to 9.2.1 or later versions<br></p>

### References
* https://lists.apache.org/thread/tns2b4khyyncgs5v5p9y35pobg9z2bvs


## s3_auth plugin problem with hash calculation ## { #CVE-2023-33933 }

CVE-2023-33933 [\[CVE json\]](./CVE-2023-33933.cve.json)

### Affected

* Apache Traffic Server from 8.0.0 through 9.2.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Traffic Server.<p>This issue affects Apache Traffic Server: from 8.0.0 through 9.2.0.</p><p>8.x users should upgrade to 8.1.7 or later versions<br>9.x users should upgrade to 9.2.1 or later versions<br></p>

### References
* https://lists.apache.org/thread/tns2b4khyyncgs5v5p9y35pobg9z2bvs
