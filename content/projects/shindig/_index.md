---
title: Apache Shindig security advisories
description: Security information for Apache Shindig
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Shindig? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Shindig).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Remote Code Execution via XStream deserialization (OpenSocial REST API) ## { #CVE-2026-66256 }

CVE-2026-66256 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66256) [\[CVE json\]](./CVE-2026-66256.cve.json) [\[OSV json\]](./CVE-2026-66256.osv.json)



_Last updated: 2026-08-13T13:53:33.194Z_

### Affected

* Apache Shindig Common through *
* Apache Shindig Social-Api through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Deserialization of Untrusted Data vulnerability in Apache Shindig.</p><p>This issue affects Apache Shindig: all versions.</p><p>Users with access to the Shindig REST API can send specially-crafted requests to trigger arbitrary code execution on the server.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/opgpnhk149614gx6vcy3lvyjnycw8mkh


### Credits
* Daryle Bourque, Horizon3.ai (finder)
* Noah King, Horizon3.ai (finder)
