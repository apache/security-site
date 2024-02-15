---
title: Apache Answer (Incubating) security advisories
description: Security information for Apache Answer (Incubating)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Answer (Incubating)? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Repeated submissions using scripts resulted in an abnormal number of collections for questions. ## { #CVE-2023-49619 }

CVE-2023-49619 [\[CVE json\]](./CVE-2023-49619.cve.json)

_Last updated: 2024-01-10T08:24:57.576Z_

### Affected

* Apache Answer through 1.2.0


### Description

Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition') vulnerability in Apache Answer.<br><br><span style="background-color: var(--wht);">This issue affects Apache Answer: through 1.2.0.<br><br></span><span style="background-color: rgb(255, 255, 255);">Under normal circumstances, a user can only bookmark a question once, and will only increase the number of questions bookmarked once. However, repeat submissions through the script can increase the number of collection of the question many times.<br><br></span><span style="background-color: var(--wht);">Users are recommended to upgrade to version [</span><span style="background-color: var(--wht);">1.2.1</span><span style="background-color: var(--wht);">], which fixes the issue.</span>

### References
* https://lists.apache.org/thread/nscrl3c7pn68q4j73y3ottql6n5x3hd4


### Credits
* ek1ng (reporter)
