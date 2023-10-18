---
title: Apache Gobblin security advisories
description: Security information for Apache Gobblin
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Gobblin? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Local Credentials Disclosure Vulnerability ## { #CVE-2021-36151 }

CVE-2021-36151 [\[CVE json\]](./CVE-2021-36151.cve.json)

### Affected

* Apache Gobblin from Apache Gobblin through 0.15.0


### Description

In Apache Gobblin, the Hadoop token is written to a temp file that is visible to all local users on Unix-like systems. This affects versions <= 0.15.0. Users should update to version 0.16.0 which addresses this issue. 

### References
* https://lists.apache.org/thread/3cdkyxdd6xk05lsvr3l66dsnvhwyo1t0


### Credits
* Apache Gobblin would like to thank Jonathan Leitschuh for reporting this issue. 


## Insecure TrustManager used in LDAP connections ## { #CVE-2021-36152 }

CVE-2021-36152 [\[CVE json\]](./CVE-2021-36152.cve.json)

### Affected

* Apache Gobblin from Apache Gobblin through 0.15.0


### Description

Apache Gobblin trusts all certificates used for LDAP connections in Gobblin-as-a-Service. This affects versions <= 0.15.0. Users should update to version 0.16.0 which addresses this issue. 

### References
* https://lists.apache.org/thread/3bxf7rbf4zh95r78jtgth6gwhr5fyl2j


### Credits
* Apache Gobblin would like to thank Simon Gerst for reporting this issue. 
