---
title: Apache Accumulo security advisories
description: Security information for Apache Accumulo
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Accumulo? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Accumulo since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Accumulo 2.1.0 may incorrectly validate cached credentials ## { #CVE-2023-34340 }

[CVE-2023-34340](./CVE-2023-34340.cve.json)

### Affected

* Apache Accumulo versions 2.1.0 before 2.1.1


### Description

Improper Authentication vulnerability in Apache Software Foundation Apache Accumulo.<br><p>This issue affects Apache Accumulo: 2.1.0.<br><br><span style="background-color: rgb(255, 255, 255);">Accumulo 2.1.0 contains a defect in the user authentication process that </span><span style="background-color: rgb(255, 255, 255);">may succeed when invalid credentials are provided. Users are advised to </span><span style="background-color: rgb(255, 255, 255);">upgrade to 2.1.1.</span><br></p>