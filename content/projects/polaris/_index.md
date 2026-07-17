---
title: Apache Polaris security advisories
description: Security information for Apache Polaris
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Polaris? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=%5BFINDING%5D%20Apache%20Polaris).

You can read more about the security policy on:

- [Apache Polaris security model](https://github.com/apache/polaris/blob/main/SECURITY-THREAT-MODEL.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## write.metadata.path changes could bypass location validation and broaden delegated storage access ## { #CVE-2026-42812 }

CVE-2026-42812 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42812) [\[CVE json\]](./CVE-2026-42812.cve.json) [\[OSV json\]](./CVE-2026-42812.osv.json)



_Last updated: 2026-05-04T16:28:09.922Z_

### Affected

* Apache Polaris before 1.4.1


### Description

<span style="background-color: rgb(255, 255, 255);">In Apache Iceberg, the table's metadata files are control files: they tell readers
which data files belong to the table and which table version to read.
<br><br>
`write.metadata.path` is an optional table property that tells Polaris
where to
write those metadata files. <br>For a table already registered in a
Polaris-managed
catalog, changing only that property through an `ALTER TABLE`-style settings
change (not a row-level `INSERT`, `SELECT`, `UPDATE`, or `DELETE`) bypasses
the commit-time branch that is supposed to revalidate storage locations.

The full persisted / credential-vending variant requires the affected
catalog
to have `polaris.config.allow.unstructured.table.location=true`, with
`allowedLocations` broad enough to include the attacker-chosen target.
<br><br>`allowedLocations` is the admin-configured allowlist of storage paths that
the
catalog is allowed to use. Public project materials suggest that this flag
is a
real supported compatibility / layout mode, not just a contrived lab-only
prerequisite.
<br>
In that configuration, a user who can change table settings can cause Apache Polaris
itself to write new table metadata to an attacker-chosen reachable storage
location before the intended location-validation branch runs.

If the later concrete-path validation also accepts that location, Polaris
persists the resulting metadata path into stored table state. Later
table-load
and credential APIs can then return temporary cloud-storage credentials for
the
same location without revalidating it. In plain terms, Polaris can later
hand
out temporary storage access for the same attacker-chosen area.

That attacker-chosen area does not need to be limited to the poisoned
table's
own files. If it is a broader storage prefix, another table's prefix, or,
depending on configuration or provider behavior, even a bucket/container
root,
the resulting disclosure or corruption scope can extend to any data and
metadata Polaris can reach there.
<br><br>
The practical consequences are therefore similar to the staged-create
credential-vending issue already discussed: data and metadata reachable in
that
storage scope can be exposed and, if write-capable credentials are later
issued, modified, corrupted, or removed. Even before that later credential
step, Polaris itself performs the metadata write to the unchecked location.

So the core issue is not only later credential vending. <br><br>The primary defect
is
that Polaris skips its intended location checks before performing a
security-
sensitive metadata write when only `write.metadata.path` changes.
<br><br>
When `polaris.config.allow.unstructured.table.location=false`, current code
review suggests the later `updateTableLike(...)` validation usually rejects
out-of-tree metadata locations before the unsafe path is persisted. That may
reduce the persisted / credential-vending variant, but it does not prevent
the
underlying defect: Polaris still skips the intended pre-write location check
when only `write.metadata.path` changes.</span><br>

### References
* https://lists.apache.org/thread/wxd2wj3p0smvrk84msv317wg5tp3jtw9


## could broaden vended GCS credentials through unescaped identifier content in access-boundary CEL conditions ## { #CVE-2026-42811 }

CVE-2026-42811 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42811) [\[CVE json\]](./CVE-2026-42811.cve.json) [\[OSV json\]](./CVE-2026-42811.osv.json)



_Last updated: 2026-05-04T16:26:53.369Z_

### Affected

* Apache Polaris before 1.4.1


### Description

<span style="background-color: rgb(255, 255, 255);">In plain terms, Apache Polaris is supposed to issue short-lived GCS credentials
that
only work for one table's files, but a crafted namespace or table name can
cause those credentials to work across the configured bucket instead.
<br><br>Apache Polaris builds Google Cloud Storage downscoped credentials by creating a
Credential Access Boundary (CAB) with CEL conditions that are intended to
restrict access to the requested table's storage path.
<br><br>
The relevant CEL string is built from the bucket name and the table path.
That
table path is derived from namespace and table identifiers. In current code,
that path appears to be inserted into the CEL expression without escaping.
<br><br>
As a result, a namespace or table identifier containing a single quote and
other URI-safe CEL fragments can break out of the intended quoted string and
change the meaning of the CEL condition.
<br><br>
In private testing against Polaris 1.4.0 on real Google Cloud Storage, it was confirmed that Polaris accepted a crafted identifier and returned delegated
GCS
credentials whose CEL path restriction had effectively collapsed.
<br>
Those delegated credentials could then:
<br>
- list another table's object prefix;
<br>- read another table's metadata control file (Iceberg metadata JSON);
<br>- create and delete an object under another table's object prefix;
<br>- and also list, read, create, and delete objects under an unrelated
external
prefix in the same bucket that was not part of any table path.
<br><br>
That last point is important. The issue is not limited to "another table".
In
the confirmed setup, once Apache Polaris returned credentials for the crafted
table,
the path restriction inside the configured bucket was effectively gone.

The practical effect is that temporary credentials for one crafted table
can be
broader than the table Polaris was asked to authorize, and can become
effectively bucket-wide within the configured bucket.
<br><br>
<span style="background-color: rgb(255, 255, 255);">The current GCS testing used a Polaris principal with broad catalog
privileges for setup. A separate least-privilege Polaris RBAC variant
has not yet been tested on GCS. However, the storage-credential
broadening behavior itself has been confirmed on GCS.</span></span><br>

### References
* https://lists.apache.org/thread/hovn5hmkj9wj7v9cd8sn67svg03klgvg


## could broaden vended S3 credentials through wildcard-bearing namespace or table names ## { #CVE-2026-42810 }

CVE-2026-42810 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42810) [\[CVE json\]](./CVE-2026-42810.cve.json) [\[OSV json\]](./CVE-2026-42810.osv.json)



_Last updated: 2026-05-04T16:48:47.000Z_

### Affected

* Apache Polaris before 1.4.1


### Description

<span style="background-color: rgb(255, 255, 255);">Apache Polaris accepts literal `*` characters in namespace and table names. When it
later builds temporary S3 access policies for delegated table access, those
same characters appear to be reused unescaped in S3 IAM resource patterns
and
`s3:prefix` conditions.
<br><br>
In S3 IAM policy matching, `*` is treated as a wildcard rather than as
ordinary text. That means temporary credentials issued for one crafted table
can match the storage path of a different table.
<br><br>
In private testing against Polaris 1.4.0 using Polaris' AWS S3 temporary-
credential path on both MinIO and real AWS S3, credentials returned for
crafted tables such as `f*.t1`, `f*.*`, `*.*`, and `foo.*` could reach other
tables' S3 locations.
<br>
The confirmed behavior includes:
<br>
- reading another table's metadata control file ([Iceberg metadata JSON]);
<br>- listing another table's exact S3 table prefix ([table prefix]);
<br>- and, when write delegation was returned for the crafted table, creating
and
deleting an object under another table's exact S3 table prefix.
<br><br>
A control case using ordinary different names did not allow the same
cross-table access.
<br><br>
<span style="background-color: rgb(255, 255, 255);">A least-privilege AWS S3 variant was also confirmed in which the attacker
principal had no Polaris permissions on the victim table and only the
minimal permissions required to create and use a crafted wildcard table
(namespace-scoped `TABLE_CREATE` and `TABLE_WRITE_DATA` on `*`).</span> In that
setup, direct Polaris access to `foo.t1` remained forbidden, but the
attacker
could still create and load `*.*`, receive delegated S3 credentials, and use
those credentials to list, read, create, and delete objects under `foo.t1`.
<br><br>
In Iceberg, the metadata JSON file is a control file: it tells readers which
data files belong to the table, which snapshots exist, and which table
version
to read. So unauthorized access to it is already a meaningful
confidentiality
problem. The confirmed write-capable variant means the issue is not limited
to
disclosure.</span><br>

### References
* https://lists.apache.org/thread/gg3qq9sqg4hdjmprqy46p40xmln61dm9


## staged table creation could vend storage credentials for unvalidated locations ## { #CVE-2026-42809 }

CVE-2026-42809 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42809) [\[CVE json\]](./CVE-2026-42809.cve.json) [\[OSV json\]](./CVE-2026-42809.osv.json)



_Last updated: 2026-05-04T16:36:14.167Z_

### Affected

* Apache Polaris before 1.4.1


### Description

<span style="background-color: rgb(255, 255, 255);">Apache Polaris can issue broad temporary ("vended") storage credentials during
staged
table creation before the effective table location has been validated or
durably reserved. <br>Those temporary credentials are meant to limit the scope
of
accessible table data and metadata, but this scope limitation becomes
attacker-
directed because the attacker can choose a reachable target location.
<br><br>
In the confirmed variant, if the caller supplies a custom `location` during
stage create and requests credential vending, Apache Polaris uses that location to
construct delegated storage credentials immediately. The stage-create path
itself neither runs the normal location validation nor the overlap checks
before those credentials are issued.
<br><br>
Closely related to that, the staged-create flow also accepts
`write.data.path` / `write.metadata.path` in the request properties and
feeds
those location overrides into the same effective table location set used for
credential vending. Those fields are secondary to the main custom-`location`
exploit, but they are still attacker-influenced location inputs that should
be
validated before any credentials are issued.</span><br>

### References
* https://lists.apache.org/thread/8tfsr8y7pgq6rdcvjx95hkcr47td671r
