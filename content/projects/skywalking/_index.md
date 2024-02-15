---
title: Apache SkyWalking security advisories
description: Security information for Apache SkyWalking
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache SkyWalking? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Service unavailability impact in NodeJS agent(version <= 0.5.0) ## { #CVE-2022-36127 }

CVE-2022-36127 [\[CVE json\]](./CVE-2022-36127.cve.json)

_Last updated: 2022-07-18T11:24:38.575Z_

### Affected

* Apache SkyWalking NodeJS Agent from Apache SkyWalking NodeJS Agent through 0.5.0


### Description

A vulnerability in Apache SkyWalking NodeJS Agent prior to 0.5.1. The vulnerability will cause NodeJS services that has this agent installed to be unavailable if the OAP is unhealthy and NodeJS agent can't establish the connection.

### References
* https://lists.apache.org/thread/x238wo4r5goy39dxdjcmlofp6gcdnqr3
