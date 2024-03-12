---
title: Apache Aurora security advisories
description: Security information for Apache Aurora
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Aurora? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## padding oracle can allow construction an authentication cookie ## { #CVE-2024-27905 }

CVE-2024-27905 [\[CVE json\]](./CVE-2024-27905.cve.json)

_Last updated: 2024-02-27T14:29:18.380Z_

### Affected

* Apache Aurora from 0.5.0 through *


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Aurora.</div><p>An endpoint exposing internals to unauthenticated users can be used as a "padding oracle" allowing an anonymous attacker to construct a valid authentication cookie. Potentially this could be combined with vulnerabilities in other components to achieve remote code execution.<br></p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.<br></p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p><p><br></p>

### References
* https://lists.apache.org/thread/564kbv3wqdzkscmdn2bg4vlk48qymryp


### Credits
* Quang Luong (reporter)
* Duc Nguyen (reporter)
