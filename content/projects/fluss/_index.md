---
title: Apache Fluss (Incubating) security advisories
description: Security information for Apache Fluss (Incubating)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Fluss (Incubating)? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Fluss Netty Frame Decoder Memory Exhaustion Vulnerability ## { #CVE-2026-49361 }

CVE-2026-49361 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49361) [\[CVE json\]](./CVE-2026-49361.cve.json) [\[OSV json\]](./CVE-2026-49361.osv.json)



_Last updated: 2026-06-01T07:57:25.667Z_

### Affected

* Apache Fluss (incubating) at 0.8.0
* Apache Fluss (incubating) at 0.9.0


### Description

Apache Fluss versions prior to 0.9.1 configure the Netty LengthFieldBasedFrameDecoder with Integer.MAX_VALUE as the maximum frame length, allowing unauthenticated remote attackers to exhaust JVM heap memory on TabletServer and CoordinatorServer by sending specially crafted frame headers, resulting in denial of service.<br><br>This issue affects Apache Fluss (incubating): 0.8.0 and 0.9.0.<br><br>Users are recommended to upgrade to version 0.9.1, which fixes the issue.

### References
* https://lists.apache.org/thread/dccw6tj0njwtmvbftq13mw7fdhsok373


### Credits
* Andrea Cosentino (reporter)
