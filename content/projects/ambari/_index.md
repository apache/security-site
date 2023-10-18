---
title: Apache Ambari security advisories
description: Security information for Apache Ambari
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Ambari? Send your report to the [Apache Ambari Security Team](mailto:security@ambari.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Stored XSS in Apache Ambari ## { #CVE-2020-1936 }

CVE-2020-1936 [\[CVE json\]](./CVE-2020-1936.cve.json)

### Affected

* Apache Ambari from Apache Ambari before 2.7.4


### Description

A cross-site scripting issue was found in Apache Ambari Views.  This was addressed in Apache Ambari 2.7.4.

### References
* https://lists.apache.org/thread.html/946a9d72e664ad8bc592168d9a2fed88100c6e9f1bdfea08e91a3184%40%3Cuser.ambari.apache.org%3E


### Credits
* Apache Ambari would like to thank Krzysztof Przybylski from STM Solutions


##  ## { #CVE-2020-13924 }

CVE-2020-13924 [\[CVE json\]](./CVE-2020-13924.cve.json)

### Affected

* Apache Ambari from Apache Ambari through 2.6.2.2


### Description

In Apache Ambari versions 2.6.2.2 and earlier, malicious users can construct file names for directory traversal and traverse to other directories to download files.

### References
* https://mail-archives.apache.org/mod_mbox/ambari-user/202102.mbox/%3CCAEJYuxEQZ_aPwJdAaSxPu-Dva%3Dhc7zZUx3-pzBORbd23g%2BGH1A%40mail.gmail.com%3E


### Credits
* threedr3am


## A malicious authenticated user can remotely execute arbitrary code in the context of the application. ## { #CVE-2022-42009 }

CVE-2022-42009 [\[CVE json\]](./CVE-2022-42009.cve.json)

### Affected

* Apache Ambari from 2.7.0 through 2.7.6


### Description

SpringEL injection in the server agent in Apache Ambari version 2.7.0 to 2.7.6 allows a malicious authenticated user to execute arbitrary code remotely. U<span style="background-color: rgb(255, 255, 255);">sers are recommended to upgrade to 2.7.7.</span><br>

### References
* https://lists.apache.org/thread/6xf477ttz1oxmg0bx0tpdoz2mlqd7sbc


### Credits
* Jecki Go (jecgo@visa.com) (finder)


## Allows authenticated metrics consumers to perform RCE ## { #CVE-2022-45855 }

CVE-2022-45855 [\[CVE json\]](./CVE-2022-45855.cve.json)

### Affected

* Apache Ambari from 2.7.0 through 2.7.6


### Description

SpringEL injection in the metrics source in Apache Ambari version 2.7.0 to 2.7.6 allows a malicious authenticated user to execute arbitrary code remotely.&nbsp;U<span style="background-color: rgb(255, 255, 255);">sers are recommended to upgrade to 2.7.7.</span><br>

### References
* https://lists.apache.org/thread/302c4hwfjy9lx63jrbhcdx948pxc54l1


### Credits
* rg <18993610179@163.com> (finder)
