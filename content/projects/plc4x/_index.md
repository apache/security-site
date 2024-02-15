---
title: Apache PLC4X security advisories
description: Security information for Apache PLC4X
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache PLC4X? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache PLC4X 0.9.0 Buffer overflow in PLC4C via crafted server response ## { #CVE-2021-43083 }

CVE-2021-43083 [\[CVE json\]](./CVE-2021-43083.cve.json)

_Last updated: 2022-02-04T08:46:33.224Z_

### Affected

* Apache PLC4X from PLC4C through 0.9.0


### Description

Apache PLC4X - PLC4C (Only the C language implementation was effected) was vulnerable to an unsigned integer underflow flaw inside the tcp transport. Users should update to 0.9.1, which addresses this issue.

However, in order to exploit this vulnerability, a user would have to actively connect to a mallicious device which could send a response with invalid content. Currently we consider the probability of this being exploited as quite minimal, however this could change in the future, especially with the industrial networks growing more and more together.

### References
* https://lists.apache.org/thread/jxx6qc84z60xbbhn6vp2s5qf09psrtc7


### Credits
* Apache PLC4X would like to thank Eugene Lim for reporting this issue.
