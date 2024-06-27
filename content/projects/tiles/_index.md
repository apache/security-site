---
title: Apache Tiles security advisories
description: Security information for Apache Tiles
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Tiles? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unvalidated input may lead to path traversal and XXE ## { #CVE-2023-49735 }

CVE-2023-49735 [\[CVE json\]](./CVE-2023-49735.cve.json) [\[OSV json\]](./CVE-2023-49735.osv.json)



_Last updated: 2023-12-12T08:40:25.303Z_

### Affected

* Apache Tiles from 2.0.0 before *


### Description

<div>** UNSUPPORTED WHEN ASSIGNED **<br></div><div><br></div><div>The value set as the DefaultLocaleResolver.LOCALE_KEY attribute on the session was not validated while resolving XML definition files, leading to possible path traversal and eventually SSRF/XXE when passing user-controlled data to this key. Passing user-controlled data to this key may be relatively common, as it was also used like that to set the language in the 'tiles-test' application shipped with Tiles.<br></div><p>This issue affects Apache Tiles from version 2 onwards.<br></p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.<br></p>

### References
* https://lists.apache.org/thread/8ktm4vxr6vvc1qsxh6ft8jzmom1zl65p


### Credits
* Joseph Beeton of Contrast Security (finder)
