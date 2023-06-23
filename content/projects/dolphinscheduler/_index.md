---
title: Apache DolphinScheduler security advisories
description: Security information for Apache DolphinScheduler
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache DolphinScheduler? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache DolphinScheduler since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Remote command execution Vulnerability in script alert plugin ## { #CVE-2022-45875 }

[CVE-2022-45875](./CVE-2022-45875.cve.json)

### Affected

* Apache DolphinScheduler from 3.0 through 3.0.1
* Apache DolphinScheduler from 3.1 through 3.1.0


### Description

Improper validation of script alert plugin parameters in Apache DolphinScheduler to avoid remote command execution vulnerability.  This issue affects Apache DolphinScheduler version 3.0.1 and prior versions; version 3.1.0 and prior versions.

## Apache DolphinScheduler 3.0.0 to 3.1.1 python gateway has improper authentication ## { #CVE-2023-25601 }

[CVE-2023-25601](./CVE-2023-25601.cve.json)

### Affected

* Apache DolphinScheduler from 3.0.0 before 3.1.2


### Description

On version 3.0.0 through 3.1.1, Apache DolphinScheduler's python gateway suffered from improper authentication: an attacker could use a socket bytes attack without authentication. This issue has been fixed from version 3.1.2 onwards. For users who use version 3.0.0 to 3.1.1, you can turn off the python-gateway function by changing the value `python-gateway.enabled=false` in configuration file `application.yaml`. If you are using the python gateway, please upgrade to version 3.1.2 or above.<br>