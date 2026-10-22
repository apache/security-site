---
title: Apache YuniKorn security advisories
description: Security information for Apache YuniKorn
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache YuniKorn? Send your report to the [Apache YuniKorn Security Team](mailto:security@yunikorn.apache.org?subject=YuniKorn).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Admission control bypass via system label forgery ## { #CVE-2026-97146 }

CVE-2026-97146 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97146) [\[CVE json\]](./CVE-2026-97146.cve.json) [\[OSV json\]](./CVE-2026-97146.osv.json)



_Last updated: 2026-10-07T09:16:08.899Z_

### Affected

* Apache YuniKorn before 1.10.0


### Description

Apache YuniKorn 1.9.0 and earlier allows bypassing the check for the user annotation by setting a secondary label on the pod.&nbsp;<span>If the pod has the label 'app=yunikorn' the checks </span><span>limiting the user annotation content are not run. The label is used to identify the YuniKorn application itself in the deployments.</span><div><br></div><div>The bypass allows any user to specify an arbitrary user info annotation. The arbitrary user information&nbsp;<span>could allow access to a queue that the user normally would not have access to.&nbsp;</span><span>Quota usage for the queue might be impacted if the application runs in the incorrect queue.&nbsp;</span><span>User based quota enforcement is also based on the user annotation. User quota tracking could be side stepped even if the application runs in the correct queue.</span></div><div><div><div><div><br></div><div>Users are recommended to upgrade to version 1.10.0, which fixes this issue.</div></div></div></div>

### References
* https://lists.apache.org/thread.html/nds5ct9xzlo4fp0jfr1rx6jxm03g0jro


### Credits
* mopmonk-ai@tophant.com (finder)


## Admission control bypass via workload UPDATE operation ## { #CVE-2026-92393 }

CVE-2026-92393 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-92393) [\[CVE json\]](./CVE-2026-92393.cve.json) [\[OSV json\]](./CVE-2026-92393.osv.json)



_Last updated: 2026-10-07T09:15:30.217Z_

### Affected

* Apache YuniKorn before 1.10.0


### Description

Apache YuniKorn 1.9.0 and earlier does not implement label and user annotation checks for workload UPDATE action bypassing all checks.&nbsp;<span>Workloads in YuniKorn are defined as the following Kubernetes objects: "deployments",&nbsp;</span><span>"replicasets", "statefulsets", "daemonsets", "jobs", "cronjobs".</span><span>&nbsp;</span><span>The CREATE action correctly enforces the checks for all object types.</span><div><br></div><div><div>The bypass allows any user to specify an arbitrary user info annotation. The same bypass also allows changing the application ID for the workload. The combination of the two applied in one UPDATE&nbsp;<span>could allow access to a queue that the user normally would not have access to.&nbsp;</span><span>Quota usage for the queue might be impacted if the application runs in the incorrect queue.&nbsp;</span><span>User based quota enforcement is also based on the user annotation. User quota tracking could be side stepped even if the application runs in the correct queue.</span></div><div><br></div><div>Users are recommended to upgrade to version 1.10.0, which fixes this issue.</div></div>

### References
* https://lists.apache.org/thread.html/sfo83zlrrx9ftbox9oxcp03qox2co449


### Credits
* diana.wang.turing@gmail.com (finder)


## LDAP Group provider panics on lowercase attribute name ## { #CVE-2026-78243 }

CVE-2026-78243 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-78243) [\[CVE json\]](./CVE-2026-78243.cve.json) [\[OSV json\]](./CVE-2026-78243.osv.json)



_Last updated: 2026-10-07T09:15:40.706Z_

### Affected

* Apache YuniKorn from 1.8.0 before 1.10.0


### Description

Apache YuniKorn 1.8.0 and later, if configured with the LDAP group resolver, crashes due to an out of bounds read processing group membership entries.<div>If the LDAP server returns a group membership entry, memberOf attribute, for a user specified in the pod the server crashes&nbsp;<span>if a membership record does not start with "CN=".</span></div><div><div><div><br></div><div>This only affects install that have the non default LDAP group provider configured.&nbsp;</div><div><br>Users are recommended to upgrade to version 1.10.0, which fixes this issue.</div></div></div>

### References
* https://lists.apache.org/thread.html/yz51lpj6k8q2hz7x2gjdpcrk44hdn25v


### Credits
* gjoko@zeroscience.mk (finder)
