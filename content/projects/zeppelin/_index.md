---
title: Apache Zeppelin security advisories
description: Security information for Apache Zeppelin
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Zeppelin? You can read more about the projects' security policy on their [security page](https://zeppelin.apache.org/security.html), and email your report to the [Apache Zeppelin Security Team](mailto:security@zeppelin.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://zeppelin.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## bash command injection in spark interpreter ## { #CVE-2019-10095 }

CVE-2019-10095 [\[CVE json\]](./CVE-2019-10095.cve.json)

_Last updated: 2022-12-08T11:51:05.587Z_

### Affected

* Apache Zeppelin from Apache Zeppelin through 0.9.0


### Description

bash command injection vulnerability in Apache Zeppelin allows an attacker to inject system commands into Spark interpreter settings.  This issue affects Apache Zeppelin Apache Zeppelin version 0.9.0 and prior versions.

### References
* https://lists.apache.org/thread.html/rdf06e8423833b3daadc30c56a2ff47c48920864d5199476daa897208%40%3Cusers.zeppelin.apache.org%3E


### Credits
* Apache Zeppelin would like to thank HERE Security team for reporting this issue 


## Notebook permissions bypass ## { #CVE-2020-13929 }

CVE-2020-13929 [\[CVE json\]](./CVE-2020-13929.cve.json)

_Last updated: 2021-09-02T16:10:15.351Z_

### Affected

* Apache Zeppelin from Apache Zeppelin through 0.9.0


### Description

Authentication bypass vulnerability in Apache Zeppelin allows an attacker to bypass Zeppelin authentication mechanism to act as another user.  This issue affects Apache Zeppelin Apache Zeppelin version 0.9.0 and prior versions.

### References
* https://lists.apache.org/thread.html/r768800925d6407a6a87ccae0ec98776b7bda50c0e3ed3d0130dad028%40%3Cusers.zeppelin.apache.org%3E


### Credits
* Apache Zeppelin would like to thank David Woodhouse for reporting this issue 


## Cross Site Scripting in markdown interpreter ## { #CVE-2021-27578 }

CVE-2021-27578 [\[CVE json\]](./CVE-2021-27578.cve.json)

_Last updated: 2021-09-02T16:11:07.660Z_

### Affected

* Apache Zeppelin from Apache Zeppelin before 0.9.0


### Description

Cross Site Scripting vulnerability in markdown interpreter of Apache Zeppelin allows an attacker to inject malicious scripts.  This issue affects Apache Zeppelin Apache Zeppelin versions prior to 0.9.0.

### References
* https://lists.apache.org/thread.html/r90590aa5ea788128ecc2e822e1e64d5200b4cb92b06707b38da4cb3d%40%3Cusers.zeppelin.apache.org%3E


### Credits
* Apache Zeppelin would like to thank Paulo Pacheco for reporting this issue 


## Arbitrary file deletion vulnerability ## { #CVE-2021-28655 }

CVE-2021-28655 [\[CVE json\]](./CVE-2021-28655.cve.json)

_Last updated: 2022-12-20T09:49:02.814Z_

### Affected

* Apache Zeppelin through 0.9.0


### Description

The improper Input Validation vulnerability in "”Move folder to Trash” feature of Apache Zeppelin allows an attacker to delete the arbitrary files.  This issue affects Apache Zeppelin Apache Zeppelin version 0.9.0 and prior versions.

### References
* https://lists.apache.org/thread/bxs056g3xlsofz0jb3wny9dw4llwptd2


### Credits
* Kai Zhao (finder)


## Stored XSS in note permissions ## { #CVE-2022-46870 }

CVE-2022-46870 [\[CVE json\]](./CVE-2022-46870.cve.json)

_Last updated: 2022-12-16T12:54:56.815Z_

### Affected

* Apache Zeppelin before 0.8.2


### Description

An Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Zeppelin allows logged-in users to execute arbitrary javascript in other users' browsers.<br><p>This issue affects Apache Zeppelin before 0.8.2. Users are recommended to upgrade to a supported version of Zeppelin.<br></p>

### References
* https://lists.apache.org/thread/gb1wdnrm1095xw6qznpsycfrht4lwbwc
