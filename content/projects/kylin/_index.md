---
title: Apache Kylin security advisories
description: Security information for Apache Kylin
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Kylin? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Command injection by Useless configuration ## { #CVE-2022-43396 }

[CVE-2022-43396](./CVE-2022-43396.cve.json)

### Affected

* Apache Kylin from Apache Kylin 4 through 4.0.2


### Description

In the fix for CVE-2022-24697, a blacklist is used to filter user input commands. But there is a risk of being bypassed. The user can control the command by controlling the&nbsp;kylin.engine.spark-cmd&nbsp;parameter of conf.

### References
* https://lists.apache.org/thread/ob2ks04zl5ms0r44cd74y1xdl1rzfd1r


## Command injection by Diagnosis Controller ## { #CVE-2022-44621 }

[CVE-2022-44621](./CVE-2022-44621.cve.json)

### Affected

* Apache Kylin from Apache Kylin 4  through 4.0.2


### Description

Diagnosis Controller miss parameter validation, so user may attacked by command injection via HTTP Request.

### References
* https://lists.apache.org/thread/7ctchj24dofgsj9g1rg1245cms9myb34
