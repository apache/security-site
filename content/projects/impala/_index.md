---
title: Apache Impala security advisories
description: Security information for Apache Impala
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Impala? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Impala).

You can read more about the security policy on:

- [Apache Impala security model](https://github.com/apache/impala/security/policy)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## RCE via External Data Source Class Loading ## { #CVE-2026-65181 }

CVE-2026-65181 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-65181) [\[CVE json\]](./CVE-2026-65181.cve.json) [\[OSV json\]](./CVE-2026-65181.osv.json)



_Last updated: 2026-09-09T10:40:47.268Z_

### Affected

* Apache Impala from 2.7.0 through 4.5.1


### Description

Insufficient authorization of Data Source tables in Impala 2.7-4.5 allows a client with privileges to upload a file to remote storage and create a table to execute arbitrary Java code.<br>Users are recommended to upgrade to version 4.5.2, which fixes this issue.

### References
* https://lists.apache.org/thread/2ty3srsh96j86xxg4g1hbo5rwvszwcnl


### Credits
* zhaokaifei ChinaTelecom (reporter)


## Secrets Exfiltration via SSRF ## { #CVE-2026-57866 }

CVE-2026-57866 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57866) [\[CVE json\]](./CVE-2026-57866.cve.json) [\[OSV json\]](./CVE-2026-57866.osv.json)



_Last updated: 2026-09-09T10:39:32.832Z_

### Affected

* Apache Impala from 4.4.0 through 4.5.1


### Description

Server side request forgery in Apache Impala versions 4.4.x and 4.5.x.&nbsp; Authenticated Impala users with permissions to execute the&nbsp;<span><span>ai_generate_text() function can exfiltrate secrets provided by the credential providers configured in the `<code>hadoop.security.credential.provider.path` property of `</code>core-site.xml`. The secret's key must be known to the user.</span></span><br>

### References
* https://lists.apache.org/thread/nnk4660cbs6dmmkch7ch7wwb3g9myw7j


### Credits
* Andrey Rukin (Arenadata) (reporter)


## SAML authentication bypass via forged bearer token ## { #CVE-2026-56207 }

CVE-2026-56207 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-56207) [\[CVE json\]](./CVE-2026-56207.cve.json) [\[OSV json\]](./CVE-2026-56207.osv.json)



_Last updated: 2026-09-09T10:36:50.910Z_

### Affected

* Apache Impala from 4.0.0 through 4.5.1


### Description

<p>Signature of Bearer token is not verified in last step of SAML2 authentication for Impala's hs2-http interface, allowing altering user name and acting as another user.</p><p>This issue affects Apache Impala: &gt;=4.0.0.</p><p>Users are recommended to upgrade to version 4.5.2, which fixes this issue.</p>

### References
* https://lists.apache.org/thread/20cov78py0zqzx7dyq39ktythkwn91zs


### Credits
* Andrew Rukin (Arenadata) (reporter)


## Avro Schema URL Server-Side Request Forgery ## { #CVE-2026-54048 }

CVE-2026-54048 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-54048) [\[CVE json\]](./CVE-2026-54048.cve.json) [\[OSV json\]](./CVE-2026-54048.osv.json)



_Last updated: 2026-09-09T10:33:43.525Z_

### Affected

* Apache Impala from 2.0.0 through 4.5.1


### Description

Specifying tblproperties('avro.schema.url'='<a target="_blank" rel="nofollow" href="http://...'">http://...'</a>) or with a 'file:///' URI on a table in Impala 2.0.0 to 4.5.1 on all platforms allows an attacker to trigger a GET request to internal endpoints they may not have access to but that Impala does and the response my be exposed via parsing error messages.<br>Users are recommended to upgrade to version 4.5.2, which fixes this issue.

### References
* https://lists.apache.org/thread/cn3q4s8yx924ndlm3gt04o6g4rfm980c


### Credits
* zhaokaifei ChinaTelecom (reporter)


## Impala logs contain secrets ## { #CVE-2021-28131 }

CVE-2021-28131 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-28131) [\[CVE json\]](./CVE-2021-28131.cve.json) [\[OSV json\]](./CVE-2021-28131.osv.json)



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
