---
title: Apache Kylin security advisories
description: Security information for Apache Kylin
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Kylin? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Kylin since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Command injection by Useless configuration ## { #CVE-2022-43396 }

[CVE-2022-43396](./CVE-2022-43396.cve.json)

### Affected

* Apache Kylin from Apache Kylin 4 through 4.0.2


### Description

In the fix for CVE-2022-24697, a blacklist is used to filter user input commands. But there is a risk of being bypassed. The user can control the command by controlling the&nbsp;kylin.engine.spark-cmd&nbsp;parameter of conf.

## Command injection by Diagnosis Controller ## { #CVE-2022-44621 }

[CVE-2022-44621](./CVE-2022-44621.cve.json)

### Affected

* Apache Kylin from Apache Kylin 4  through 4.0.2


### Description

Diagnosis Controller miss parameter validation, so user may attacked by command injection via HTTP Request.