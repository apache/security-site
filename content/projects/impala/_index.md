---
title: Apache Impala security advisories
description: Security information for Apache Impala
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Impala? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Impala logs contain secrets ## { #CVE-2021-28131 }

CVE-2021-28131 [\[CVE json\]](./CVE-2021-28131.cve.json)

_Last updated: 2021-07-22T09:44:57.855Z_

### Affected

* Apache Impala from Apache Impala through 3.4.0


### Description

Impala sessions use a 16 byte secret to verify that the session is not being hijacked by another user. However, these secrets appear in the Impala logs, therefore Impala users with access to the logs can use another authenticated user's sessions with specially constructed requests. This means the attacker is able to execute statements for which they don't have the necessary privileges otherwise.

Impala deployments with Apache Sentry or Apache Ranger authorization enabled may be vulnerable to privilege escalation if an authenticated attacker is able to hijack a session or query from another authenticated user with privileges not assigned to the attacker.

Impala deployments with audit logging enabled may be vulnerable to incorrect audit logging as a user could undertake actions that were logged under the name of a different authenticated user.

Constructing an attack requires a high degree of technical sophistication and access to the Impala system as an authenticated user.

Mitigation: If an Impala deployment uses Apache Sentry, Apache Ranger or audit logging, then users should upgrade to a version of Impala with the fix for IMPALA-10600. The Impala 4.0 release includes this fix. This hides session secrets from the logs to eliminate the risk of any attack using this mechanism.

In lieu of an upgrade, restricting access to logs that expose secrets will reduce the risk of an attack. Restricting access to the Impala deployment to trusted users will also reduce the risk of an attack. Log redaction techniques can be used to redact secrets from the logs.

### References
* https://lists.apache.org/thread.html/rb54f54a91b7abaf1ed772f3a9cec290153c24881b25567b06f1b4a8c%40%3Cuser.impala.apache.org%3E
