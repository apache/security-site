---
title: Apache Zeppelin security advisories
description: Security information for Apache Zeppelin
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Zeppelin? You can read more about the projects' security policy on their [security page](https://zeppelin.apache.org/security.html), and email your report to the  [Apache Zeppelin Security Team](mailto:security@zeppelin.apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Zeppelin since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. It may also lack details found on the [project security page](https://zeppelin.apache.org/security.html).

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Arbitrary file deletion vulnerability ## { #CVE-2021-28655 }

[CVE-2021-28655](./CVE-2021-28655.cve.json)

### Affected

* Apache Zeppelin through 0.9.0


### Description

The improper Input Validation vulnerability in "”Move folder to Trash” feature of Apache Zeppelin allows an attacker to delete the arbitrary files.  This issue affects Apache Zeppelin Apache Zeppelin version 0.9.0 and prior versions.

### References
* https://lists.apache.org/thread/bxs056g3xlsofz0jb3wny9dw4llwptd2


## Stored XSS in note permissions ## { #CVE-2022-46870 }

[CVE-2022-46870](./CVE-2022-46870.cve.json)

### Affected

* Apache Zeppelin before 0.8.2


### Description

An Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Zeppelin allows logged-in users to execute arbitrary javascript in other users' browsers.<br><p>This issue affects Apache Zeppelin before 0.8.2. Users are recommended to upgrade to a supported version of Zeppelin.<br></p>

### References
* https://lists.apache.org/thread/gb1wdnrm1095xw6qznpsycfrht4lwbwc
