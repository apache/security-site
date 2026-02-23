---
title: Apache Accumulo security advisories
description: Security information for Apache Accumulo
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Accumulo? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Accumulo 2.1.0 may incorrectly validate cached credentials ## { #CVE-2023-34340 }

CVE-2023-34340 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-34340) [\[CVE json\]](./CVE-2023-34340.cve.json) [\[OSV json\]](./CVE-2023-34340.osv.json)



_Last updated: 2023-06-21T07:01:43.546Z_

### Affected

* Apache Accumulo from 2.1.0 before 2.1.1


### Description

Improper Authentication vulnerability in Apache Software Foundation Apache Accumulo.<br><p>This issue affects Apache Accumulo: 2.1.0.<br><br><span style="background-color: rgb(255, 255, 255);">Accumulo 2.1.0 contains a defect in the user authentication process that </span><span style="background-color: rgb(255, 255, 255);">may succeed when invalid credentials are provided. Users are advised to </span><span style="background-color: rgb(255, 255, 255);">upgrade to 2.1.1.</span><br></p>

### References
* https://lists.apache.org/thread/syy6jftvy9l6tlhn33o0rzwhh4rd0z4t
* https://accumulo.apache.org/release/accumulo-2.1.1/


## Apache Accumulo Improper Handling of Insufficient Permissions ## { #CVE-2020-17533 }

CVE-2020-17533 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17533) [\[CVE json\]](./CVE-2020-17533.cve.json) [\[OSV json\]](./CVE-2020-17533.osv.json)



_Last updated: 2024-01-31T09:33:16.054Z_

### Affected

* Apache Accumulo at 2.0.0
* Apache Accumulo from 1.5.0 before Apache Accumulo*


### Description

Apache Accumulo versions 1.5.0 through 1.10.0 and version 2.0.0 do not properly check the return value of some policy enforcement functions before permitting an authenticated user to perform certain administrative operations. Specifically, the return values of the 'canFlush' and 'canPerformSystemActions' security functions are not checked in some instances, therefore allowing an authenticated user with insufficient permissions to perform the following actions: flushing a table, shutting down Accumulo or an individual tablet server, and setting or removing system-wide Accumulo configuration properties.

### References
* https://lists.apache.org/thread.html/rf8c1a787b6951d3dacb9ec58f0bf1633790c91f54ff10c6f8ff9d8ed%40%3Cuser.accumulo.apache.org%3E
