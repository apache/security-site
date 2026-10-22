---
title: Apache Cocoon security advisories
description: Security information for Apache Cocoon
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache Cocoon? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Cocoon).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unauthenticated access to diagnostic interfaces ## { #CVE-2026-108089 }

CVE-2026-108089 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108089) [\[CVE json\]](./CVE-2026-108089.cve.json) [\[OSV json\]](./CVE-2026-108089.osv.json)



_Last updated: 2026-10-20T10:25:52.945Z_

### Affected

* Apache Cocoon through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Exposure of sensitive system information to an unauthorized control sphere vulnerability in Apache Cocoon. An unauthenticated user could gain access to diagnostic interfaces, including triggering of cache, exposure of (verbose) debug logging and profile information.</p><p>This issue affects Apache Cocoon: all versions.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/fo6wh59zg4zmsnt3ohpc8pblyotn4zw7


### Credits
* Tiago Abreu (finder)


## Cross-user cache poisoning ## { #CVE-2026-108088 }

CVE-2026-108088 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108088) [\[CVE json\]](./CVE-2026-108088.cve.json) [\[OSV json\]](./CVE-2026-108088.osv.json)



_Last updated: 2026-10-20T10:25:32.068Z_

### Affected

* Apache Cocoon through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Use of cache containing sensitive information vulnerability in Apache Cocoon. When using the cache on a multi-user application, cached values for one user could be used when serving content for other users.</p><p>This issue affects Apache Cocoon: all versions.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/30vg3mht5vsm9vsmrdnx80zp5fw536st


### Credits
* Tiago Abreu (finder)


## SQL Injection ## { #CVE-2026-108087 }

CVE-2026-108087 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108087) [\[CVE json\]](./CVE-2026-108087.cve.json) [\[OSV json\]](./CVE-2026-108087.osv.json)



_Last updated: 2026-10-20T10:25:11.609Z_

### Affected

* Apache Cocoon through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Apache Cocoon.</p><p>This issue affects Apache Cocoon: all versions.</p><p>Missing input sanitation would allow arbitrary SQL injection through&nbsp;the SQL processor or sql:/esql: logicsheets.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/ty85v7t2vgrtvdj6btvoxm5jj2xv48kt


### Credits
* Tiago Abreu (finder)


## XEE could lead to SSRF and information disclosure ## { #CVE-2026-108086 }

CVE-2026-108086 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-108086) [\[CVE json\]](./CVE-2026-108086.cve.json) [\[OSV json\]](./CVE-2026-108086.osv.json)



_Last updated: 2026-10-20T10:24:52.101Z_

### Affected

* Apache Cocoon through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Improper restriction of recursive entity references in DTDs ('XML entity expansion') vulnerability in Apache Cocoon.</p><p>This issue affects Apache Cocoon: all versions. XEE in the&nbsp;fp: form processor could lead to SSRF, including exposing files from the server to an untrusted external system</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/mt0h1cpjzps76nq6op7714rmnq6pbtht


### Credits
* Tiago Abreu (finder)


## continuations may not be private ## { #CVE-2025-24783 }

CVE-2025-24783 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-24783) [\[CVE json\]](./CVE-2025-24783.cve.json) [\[OSV json\]](./CVE-2025-24783.osv.json)



_Last updated: 2025-01-27T14:47:41.250Z_

### Affected

* Apache Cocoon through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Incorrect Usage of Seeds in Pseudo-Random Number Generator (PRNG) vulnerability in Apache Cocoon.</p><p>This issue affects Apache Cocoon: all versions.</p><p>When a continuation is created, it gets a random identifier. Because the random number generator used to generate these identifiers was seeded with the startup time, it may not have been sufficiently unpredictable, and an attacker could use this to guess continuation ids and look up continuations they should not have had access to.</p><p>As a mitigation, you may enable the "session-bound-continuations" option to make sure continuations are not shared across sessions.<br></p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/pk86jp5cvn41432op8wv1k8p14mp27nz


### Credits
* Xiangfan Wu from the StarMap Team of Legendsec at Qi-Anxin Group (finder)


## Apache Cocoon's StreamGenerator is vulnerable to XXE injection ## { #CVE-2023-49733 }

CVE-2023-49733 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49733) [\[CVE json\]](./CVE-2023-49733.cve.json) [\[OSV json\]](./CVE-2023-49733.osv.json)



_Last updated: 2023-11-30T11:29:43.636Z_

### Affected

* Apache Cocoon from 2.2.0 before 2.3.0


### Description

Improper Restriction of XML External Entity Reference vulnerability in Apache Cocoon.<p>This issue affects Apache Cocoon: from 2.2.0 before 2.3.0.</p><p>Users are recommended to upgrade to version 2.3.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/t87nntzt6dxw354zbqr9k7l7o1x8gq11


## SQL injection in DatabaseCookieAuthenticatorAction ## { #CVE-2022-45135 }

CVE-2022-45135 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-45135) [\[CVE json\]](./CVE-2022-45135.cve.json) [\[OSV json\]](./CVE-2022-45135.osv.json)



_Last updated: 2023-11-30T08:05:43.177Z_

### Affected

* Apache Cocoon from 2.2.0 before 2.3.0


### Description

Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Cocoon.<p>This issue affects Apache Cocoon: from 2.2.0 before 2.3.0.</p><p>Users are recommended to upgrade to version 2.3.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lsvd1hmr2t2q823x21d5ygzgbj9jpvjp


### Credits
* QSec-Team (finder)
