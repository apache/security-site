---
title: Apache Kyuubi security advisories
description: Security information for Apache Kyuubi
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Kyuubi? Send your report to the [Apache Kyuubi Security Team](mailto:security@kyuubi.apache.org?subject=Kyuubi).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## kyuubi.session.local.dir.allow.list bypass via unprefixed Spark file-conf aliases ## { #CVE-2026-62391 }

CVE-2026-62391 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-62391) [\[CVE json\]](./CVE-2026-62391.cve.json) [\[OSV json\]](./CVE-2026-62391.osv.json)



_Last updated: 2026-07-31T09:20:26.636Z_

### Affected

* Apache Kyuubi from 1.6.0 before 1.12.0


### Description

<p><span style="background-color: rgb(255, 255, 255);">The security fix for CVE-2025-66518 is incomplete.&nbsp;</span><span style="background-color: rgb(255, 255, 255);">Any client who can access to Apache Kyuubi Server via Kyuubi frontend protocols can bypass server-side config&nbsp;</span>kyuubi.session.local.dir.allowlist via unprefixed Spark config aliases.</p><p>This issue affects Apache Kyuubi: from 1.6.0 before 1.12.0.</p><p>Users are recommended to upgrade to version 1.12.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/vo4k4nxz23kfzrpp120nsojb0vrkx4w1


### Credits
* Anand Nalya (finder)


## REST batch multipart upload path traversal allows controlled file write ## { #CVE-2026-52680 }

CVE-2026-52680 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-52680) [\[CVE json\]](./CVE-2026-52680.cve.json) [\[OSV json\]](./CVE-2026-52680.osv.json)



_Last updated: 2026-07-30T08:27:43.964Z_

### Affected

* Apache Kyuubi from 1.7.0 through 1.11.1


### Description

<p><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">Apache Kyuubi REST batch multipart upload handling uses the client-supplied multipart filename when creating a temporary uploaded resource. A remote attacker who can access the REST batch upload endpoint can provide path traversal sequences in the filename and cause the Kyuubi server process to write controlled content outside the intended upload directory, subject to filesystem permissions.</span><br></span></p><p>This issue affects Apache Kyuubi: from 1.7.0 through 1.11.1.</p><p>Users are recommended to upgrade to version 1.12.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/b0qx2v8k5v4rrqsh53pb146t7so0lmrk


### Credits
* LTSHFWJT (finder)


## Unrestricted access via Kyuubi engine-ui proxy ## { #CVE-2026-23904 }

CVE-2026-23904 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-23904) [\[CVE json\]](./CVE-2026-23904.cve.json) [\[OSV json\]](./CVE-2026-23904.osv.json)



_Last updated: 2026-07-29T04:15:21.816Z_

### Affected

* Apache Kyuubi from 1.8.0 before 1.12.0


### Description

<p><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">Kyuubi Engine UI proxy accepts a host and port from the request path and proxies HTTP requests to that destination.&nbsp;</span></span><span style="background-color: rgb(255, 255, 255);">A remote requester with network access to the proxy can cause the Kyuubi server to send HTTP requests to arbitrary reachable hosts, resulting in SSRF or open-proxy behavior.</span><br></p><p>This issue affects Apache Kyuubi: from 1.8.0 before 1.12.0.</p><p>Users are recommended to upgrade to version 1.12.0, which disables the proxy by default.&nbsp;To restore proxied Engine UI, set kyuubi.frontend.rest.engine.ui.proxy.enabled=true and configure allowed target hosts with kyuubi.frontend.rest.engine.ui.proxy.hosts.</p>

### References
* https://github.com/apache/kyuubi/pull/7483
* https://lists.apache.org/thread/ps79fcfx49ox9kwgztc5t5bw0tyhck9m


### Credits
* Ícaro Torres (reporter)


## Unauthorized directory access due to missing path normalization ## { #CVE-2025-66518 }

CVE-2025-66518 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-66518) [\[CVE json\]](./CVE-2025-66518.cve.json) [\[OSV json\]](./CVE-2025-66518.osv.json)



_Last updated: 2026-01-05T08:46:25.781Z_

### Affected

* Apache Kyuubi from 1.6.0 through 1.10.2


### Description

<p>Any client who can access to Apache Kyuubi Server via Kyuubi frontend protocols can bypass server-side config kyuubi.session.local.dir.allow.list and use local files which are not listed in the config.</p><p>This issue affects Apache Kyuubi: from 1.6.0 through 1.10.2.</p><p>Users are recommended to upgrade to version 1.10.3 or upper, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/xp460bwbyzdhho34ljd4nchyt2fmhodl


### Credits
* Hiroki Egawa (reporter)
* Hiroki Egawa (remediation developer)
