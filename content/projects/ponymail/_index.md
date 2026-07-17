---
title: Apache Pony Mail security advisories
description: Security information for Apache Pony Mail
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Pony Mail? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Admin account takeover via request smuggling ## { #CVE-2026-41873 }

CVE-2026-41873 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41873) [\[CVE json\]](./CVE-2026-41873.cve.json) [\[OSV json\]](./CVE-2026-41873.osv.json)



_Last updated: 2026-04-28T15:18:49.753Z_

### Affected

* Pony Mail through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling') vulnerability in Pony Mail leading to admin account takeover.</p><p>This issue affects all versions of the Lua implementation of Pony Mail. There is a Python implementation under development under the name "Pony Mail Foal" that is not affected by this issue, but hasn't been released yet.</p><p>As the Lua implementation of this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/1c7jtxjobh280kqc13fzw1cg57xrz951


### Credits
* Li Jiantao (@CurseRed) of STAR Labs SG Pte. Ltd. (@starlabs_sg) (finder)
* Tevel Sho of STAR Labs SG Pte. Ltd (finder)
