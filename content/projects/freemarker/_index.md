---
title: Apache FreeMarker security advisories
description: Security information for Apache FreeMarker
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache FreeMarker? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=FreeMarker).

You can read more about the security policy on:

- [Apache FreeMarker security model](https://github.com/apache/freemarker/security/policy)
- [Apache FreeMarker Online Tester security model](https://github.com/apache/freemarker-online-tester/security/policy)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security pages linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## A malformed locale may be exploitable for path traversal attacks ## { #CVE-2026-84939 }

CVE-2026-84939 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-84939) [\[CVE json\]](./CVE-2026-84939.cve.json)

_Last updated: 2026-09-10T05:06:51.774Z_

### Affected

* Apache FreeMarker from 2.2.0 through 2.3.34
* Apache FreeMarker at 2.3.35 unaffected
* Apache FreeMarker from 2.2.0 through 2.3.34
* Apache FreeMarker at 2.3.35 unaffected


### Description

Path traversal vulnerability in Apache FreeMarker template loading mechanism, if the attacker can specify an arbitrary malformed locale identifier to FreeMarker, and the localized lookup configuration setting is enabled (it's by default enabled).<br><br>This issue affects Apache FreeMarker from 2.2.0 through 2.3.34.<br><br>Users are recommended to upgrade to version 2.3.35. Disabling localized lookup in previous versions also mitigates this.<br><br>Note that even in versions affected by this vulnerability, the files that can be loaded remain restricted by the <code>TemplateLoader</code> that FreeMarker is configured to use. In particular, <code>FileTemplateLoader</code> prevents attempts to traverse outside the <code>baseDir</code> specified in its constructor. Other <code>TemplateLoader</code> implementations may allow access outside their designated base directory, but they are still constrained by the underlying storage mechanism—for example, a loader wrapping a Java class loader can only access resources that the class loader can load, while one wrapping a web application context can only access resources available through that context.

### References
* https://lists.apache.org/thread/hrd7o2ylwkkswdyhyzllgqt0f80kyd5y
