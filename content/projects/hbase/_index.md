---
title: Apache HBase security advisories
description: Security information for Apache HBase
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache HBase? Send your report to the [Apache HBase Security Team](mailto:security@hbase.apache.org?subject=HBase).

You can read more about the security policy on:

- [Apache HBase security model](https://hbase.apache.org/security-model/)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Missing scanner instance owner check in thrift delegation service ## { #CVE-2026-49326 }

CVE-2026-49326 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49326) [\[CVE json\]](./CVE-2026-49326.cve.json) [\[OSV json\]](./CVE-2026-49326.osv.json)



_Last updated: 2026-07-24T14:56:20.732Z_

### Affected

* Apache HBase through 2.5.14
* Apache HBase from 2.6-alpha through 2.6.5
* Apache HBase from 3-alpha through 3.0.0-beta-1


### Description

<p></p><p>Missing Authorization vulnerability in Apache HBase thrift and rest delegation service.</p><span style="background-color: rgb(255, 255, 255);">A scan operation in thrift/rest service has 3 steps, open, fetch(possible multiple times), close.</span><br><span style="background-color: rgb(255, 255, 255);">The open step will return an id which will be passed back to server for identifying the scanner instances stored at server side.</span><br><span style="background-color: rgb(255, 255, 255);">We missed the owner check in fetch and close steps which means a user can fetch rows from the scanner which is opened by other users, and close scanners which belongs to other users.</span><p></p><p>This issue affects Apache HBase:from 3.0.0-alpha-1 through 3.0.0-beta-1, from 2.6.0 through 2.6.5, from 2.5.0 through 2.5.14, through 2.4.*.</p><p>Users are recommended to upgrade to version 3.0.0-beta-2, 2.6.6 and 2.5.15, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/f4l4sjgwb9tb04cqnkpgl6gy3slgvcsj


### Credits
* Andrew Rukin (Arenadata) <a.rukin@arenadata.io> (reporter)
