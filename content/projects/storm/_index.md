---
title: Apache Storm security advisories
description: Security information for Apache Storm
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Storm? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Storm).

You can read more about the security policy on:

- [Apache Storm security model](https://storm.apache.org/security-model.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Disclosure of Unredacted Merged Daemon Configuration via the Topology Page ## { #CVE-2026-84179 }

CVE-2026-84179 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-84179) [\[CVE json\]](./CVE-2026-84179.cve.json) [\[OSV json\]](./CVE-2026-84179.osv.json)



_Last updated: 2026-09-14T13:57:57.741Z_

### Affected

* Apache Storm Nimbus from 3.0.0 before 3.1.0
* Apache Storm UI from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>  getTopologyPageInfo merged the Nimbus daemon configuration with the topology's own configuration and returned the result without redaction in the topology_conf field of TopologyPageInfo. The Storm UI copied that value verbatim into the configuration field of GET /api/v1/topology/{id} and of the corresponding metrics endpoint.<br><br>  Where the cluster is configured with them, the merged map includes storm.zookeeper.auth.payload, which Storm's own documentation directs operators to keep in storm-cluster-auth.yaml under permissions that deny access from workers, together with the keystore and truststore passwords for the Thrift, Netty and ZooKeeper TLS configuration, and any plugin key whose name denotes a secret.<br><br>  getTopologyPageInfo is a topology read-only operation. Under SimpleACLAuthorizer a principal listed in topology.readonly.users or topology.readonly.groups could therefore read daemon credentials that the dedicated cluster configuration API, getNimbusConf, redacts and that is gated on nimbus.users instead. The sibling operations that exist to serve configuration were masked; the topology page, which merges in strictly more daemon state, was not.<br><br><b>  Mitigation</b><br><br>  Upgrade to 3.1.0, where credential-bearing values are masked before any configuration is served over the Nimbus API.<br><br>  Users who cannot upgrade immediately should remove any principal that is not trusted with cluster credentials from topology.readonly.users, topology.readonly.groups, topology.users and topology.groups, and should rotate the ZooKeeper authentication payload and any TLS keystore or truststore passwords that were reachable through the topology page.<br><br><b>  Credit</b><div><b><br></b><div><span>Wanxin Yin (yaklang.io)&nbsp;</span><span>reported this issue to the Apache Security Team.</span></div></div>

### References
* https://lists.apache.org/thread/3pj6tf6xq8l6f661k3c20tqjnx6w5k55


### Credits
* Wanxin Yin (yaklang.io) (finder)


## Cross-Tenant Blob Deletion and Cluster Denial of Service via Unvalidated Topology Dependency Keys ## { #CVE-2026-82441 }

CVE-2026-82441 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82441) [\[CVE json\]](./CVE-2026-82441.cve.json) [\[OSV json\]](./CVE-2026-82441.osv.json)



_Last updated: 2026-09-14T13:58:55.224Z_

### Affected

* Apache Storm Nimbus from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>A submitted topology carries two lists of blobstore keys, `dependency_jars` and `dependency_artifacts`,<br>which the client fills in after uploading the corresponding blobs. Nimbus performed no validation of their<br>contents on the submission path, yet acts on them in two places.<br><br>During cleanup of a finished topology, Nimbus deletes the keys named in those lists, and the deletion is<br>performed as the Nimbus subject, for which the blobstore short-circuits its ACL check. A submitter who<br>listed a key belonging to another topology, such as its `-stormjar.jar`, could therefore cause<br>that blob to be deleted when their own topology was cleaned up.<br><br>Separately, on acquiring leadership a Nimbus compares the dependency keys of all active topologies against<br>the blobstore contents and surrenders leadership if any is missing. A single key that does not exist, on a<br>single active topology, therefore causes every Nimbus to acquire leadership, surrender it and requeue<br>indefinitely, leaving the cluster without a leader and unable to schedule, clean up or accept submissions.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where a submission is refused unless every entry in both lists is a dependency blob key<br>and exists in the blobstore.<br><br>Note that this validates new submissions only; a topology stored by an affected version with an invalid list<br>is unaffected by the upgrade. An operator whose cluster is failing to retain a leader should inspect the<br>Nimbus log for the dependency keys reported as missing and remove or resubmit the topology naming them.<br><br>Users who cannot upgrade immediately should restrict topology submission to trusted principals.<br><br><b>Credit</b><br><br>This issue was discovered by rzo1 while investigating an unrelated blobstore defect.<br>

### References
* https://lists.apache.org/thread/qzh245bczoxw4mfnyvrj3dj2crtzdso8


### Credits
* rzo1 (finder)


## Unauthenticated Unbounded Memory Growth in DRPC ## { #CVE-2026-82439 }

CVE-2026-82439 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82439) [\[CVE json\]](./CVE-2026-82439.cve.json) [\[OSV json\]](./CVE-2026-82439.osv.json)



_Last updated: 2026-09-14T14:00:08.012Z_

### Affected

* Apache Storm DRPC from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>The DRPC server kept a map from function name to request queue and created an entry the first time a<br>function name was seen. No code path ever removed an entry: request cleanup removed the request from its<br>queue, and the shutdown path drained queues, but the queue object and its map entry remained for the life of<br>the process.<br><br>Function names come from the client and are not constrained to functions any topology has registered, so the<br>number of retained entries is bounded only by the number of distinct names an attacker chooses to send, and<br>each retained entry holds the name itself. `drpc.authorizer` is unset by default, so no credentials are<br>required to reach the endpoint.<br><br>The retained state is permanent rather than a transient load spike, so the effect accumulates until the DRPC<br>server exhausts its heap.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where a function's queue is removed once nothing is waiting in it.<br><br>Users who cannot upgrade immediately should configure `drpc.authorizer` so that only trusted principals can<br>reach the DRPC endpoints, and should ensure the DRPC ports are not reachable from untrusted networks.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.<br>

### References
* https://lists.apache.org/thread/7sgzvv5lzz93jn6vy74qfk105bhmkrzs


### Credits
* The ASF using Claude Agents (finder)


## Authenticated API Responses Exposed to Arbitrary Web Origins ## { #CVE-2026-82438 }

CVE-2026-82438 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82438) [\[CVE json\]](./CVE-2026-82438.cve.json) [\[OSV json\]](./CVE-2026-82438.osv.json)



_Last updated: 2026-09-14T14:02:06.144Z_

### Affected

* Apache Storm Webapp from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>Three separate mechanisms allowed a web page on an unrelated origin to read responses that Storm's HTTP<br>components served to an authenticated user.<br><br>The Logviewer reflected the request's `Origin` header back in `Access-Control-Allow-Origin` while also<br>sending `Access-Control-Allow-Credentials: true`. The published security model documents a permissive<br>`Access-Control-Allow-Origin: *` posture as accepted, which is safe precisely because browsers refuse to<br>honour `*` together with credentials; reflecting the concrete origin removes that protection.<br><br>The shared CORS filter used by the UI, the Logviewer and DRPC was configured with a response header name<br>where an initialisation parameter name was expected. The container ignored the setting and applied its own<br>defaults, which allow credentials.<br><br>Finally, the UI and Logviewer wrapped API responses in a caller-supplied JSONP callback for every GET<br>request. A script element on any origin can load such a response, which bypasses the same-origin policy<br>entirely rather than negotiating it, and there was no way to turn the behaviour off.<br><br>In each case the effect is that a page visited by an authenticated operator can read cluster, topology and<br>log data on their behalf.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where the Logviewer no longer reflects the request origin in a credentialed response, the<br>CORS filter is configured explicitly, and JSONP wrapping is governed by `ui.enable.jsonp`, which defaults to<br>false.<br><br>Note that disabling JSONP is a behaviour change for tooling that passes a `callback` query parameter; such<br>tooling should be moved to ordinary JSON requests.<br><br>Users who cannot upgrade immediately should place the UI, Logviewer and DRPC HTTP endpoints behind a reverse<br>proxy that strips `Access-Control-Allow-Origin` and `Access-Control-Allow-Credentials` from responses and<br>rejects requests carrying a `callback` parameter.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.<br>

### References
* https://lists.apache.org/thread/2o7tl3hcdd865njxsn4d9cxp1frkctz3


### Credits
* The ASF using Claude Agents (finder)


## Log Access Controls Not Enforced by Logviewer ## { #CVE-2026-82437 }

CVE-2026-82437 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82437) [\[CVE json\]](./CVE-2026-82437.cve.json) [\[OSV json\]](./CVE-2026-82437.osv.json)



_Last updated: 2026-09-14T14:05:07.291Z_

### Affected

* Apache Storm Logviewer from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>The Logviewer offers `logs.users` and `logs.groups` so operators can control who may read log content. For<br>daemon logs those settings were not applied: the access decision combined the "this is a daemon log" flag<br>with the authorizer result in a way that discarded the authorizer's answer whenever the flag was set, and<br>the daemon log page and download endpoints reached the handler without consulting an authorizer at all. Any<br>user able to pass the configured servlet filter could therefore read `nimbus.log`, `supervisor.log` and the<br>other daemon logs on every reachable node, which contain other tenants' topology names, owners and<br>configuration fragments.<br><br>The same advisory covers the log listing endpoints, which accepted a user argument and never applied it, so<br>`/listLogs` and `/searchLogs` returned every tenant's topology and worker log file names regardless of the<br>caller. That part is metadata only.<br><br>There was no configuration that closed either behaviour.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where the daemon log paths evaluate the same configured user and group lists that the<br>worker log paths already used, and the listing endpoints filter by the requesting user.<br><br>Users who cannot upgrade immediately should place the Logviewer behind a reverse proxy that restricts the<br>daemon log endpoints, and should treat daemon log content as readable by any filter-authenticated user.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.<br>

### References
* https://lists.apache.org/thread/hqyj3spllmbj6vg9vmx29b1tjhzysdkl


### Credits
* The ASF using Claude Agents (finder)


## Unauthenticated Remote Memory Exhaustion in the Worker Messaging Decoder ## { #CVE-2026-82435 }

CVE-2026-82435 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82435) [\[CVE json\]](./CVE-2026-82435.cve.json) [\[OSV json\]](./CVE-2026-82435.osv.json)



_Last updated: 2026-09-14T14:09:19.187Z_

### Affected

* Apache Storm Worker from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>The worker's Netty message decoder is installed ahead of the SASL authentication handlers in the pipeline<br>and acts on frames before any authentication has taken place. It allocated buffers sized from a<br>length field carried in the frame, so a single frame from an unauthenticated peer able to reach a worker<br>slot port could drive a large allocation.<br><br>`storm.messaging.netty.authentication` defaults to false, and the decoder runs before the handler that<br>enforces it in any case, so no credentials are required. The attacker needs only TCP reachability to a<br>worker port.<br><br>The effect of a single frame at the default 768 MB worker heap has not been measured to distinguish<br>sustained worker loss from transient garbage-collection pressure. The severity assigned to this advisory<br>reflects the more conservative reading; consumers who require a precise figure should test against their own<br>worker heap configuration.<br><br><div><b>Mitigation</b><br><br>Upgrade to 3.1.0, where frames are decoded only after the handshake completes.<br><br>Users who cannot upgrade immediately should ensure that worker slot ports are reachable only from within the<br>cluster, as the security model already recommends, and should enable<br>`storm.messaging.netty.authentication` where the deployment permits it.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.<br></div>

### References
* https://lists.apache.org/thread/wqfy7qb8c76f4c3wr2w6bhoz62vcnpb7


### Credits
* The ASF using Claude Agents (finder)


## Disclosure of the Topology ZooKeeper Credential to Read-Only Users and to Logs ## { #CVE-2026-82434 }

CVE-2026-82434 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82434) [\[CVE json\]](./CVE-2026-82434.cve.json) [\[OSV json\]](./CVE-2026-82434.osv.json)



_Last updated: 2026-09-14T14:10:14.214Z_

### Affected

* Apache Storm Nimbus from 3.0.0 before 3.1.0
* Apache Storm Client from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>When ZooKeeper authentication is configured, Storm deliberately retains<br>`storm.zookeeper.topology.auth.payload` in the topology configuration, because workers need it. Nimbus then<br>served that configuration verbatim to any caller holding read-only topology permissions, so a user whose<br>only grant was the ability to view a topology received its ZooKeeper credential.<br><br>That credential is not read-only. The cluster state implementation uses write-capable ACLs for worker<br>heartbeats, backpressure and error state, so a recipient can forge or remove that state for the topology<br>concerned. It is not a write credential on assignments.<br><br>The same advisory covers the submission client, which logged the generated payload at INFO on every<br>submission that generated one, and the SASL handlers, which logged it at DEBUG. The credential therefore<br>also reached any log aggregation or support bundle collected from the cluster.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where the payload is removed from the configuration served to read-only callers and is no<br>longer written to logs.<br><br>Users who cannot upgrade immediately should rotate `storm.zookeeper.topology.auth.payload` for existing<br>topologies, review retained logs and support bundles for the value, and restrict read-only topology<br>permissions to trusted principals.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.

### References
* https://lists.apache.org/thread/1t7hggrz59rdq792qm1pnkqj0ogm2szq


### Credits
* The ASF using Claude Agents (finder)


## Disclosure of Unredacted Daemon Configuration via Nimbus and the UI ## { #CVE-2026-82433 }

CVE-2026-82433 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82433) [\[CVE json\]](./CVE-2026-82433.cve.json) [\[OSV json\]](./CVE-2026-82433.osv.json)



_Last updated: 2026-09-14T14:12:22.650Z_

### Affected

* Apache Storm Nimbus from 3.0.0 before 3.1.0
* Apache Storm UI from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>`getNimbusConf` returned the complete daemon configuration without redaction after only a user-level<br>authorization check. Where the cluster is configured with them, that response includes<br>`storm.zookeeper.auth.payload` and the keystore and truststore passwords for the Thrift, Netty and<br>ZooKeeper TLS configuration. The project masks passwords elsewhere before display, so the omission here is<br>inconsistent rather than intended.<br><br>The UI endpoint `/api/v1/cluster/configuration` compounded this. It carried no `@AuthNimbusOp` annotation,<br>and the authorization filter treated a missing annotation as "no gate required" and returned immediately, so<br>the endpoint applied no per-user check at all and proxied the request under the UI daemon's own principal.<br>Any user able to pass `ui.filter` therefore received the full configuration, including principals that<br>Nimbus itself would have refused.&nbsp;<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where credential-bearing values are masked before the configuration is served and where<br>every UI API endpoint must declare its authorization explicitly.<br><br>Users who cannot upgrade immediately should place the UI behind an authenticating reverse proxy that<br>restricts `/api/v1/cluster/configuration`, and should rotate the ZooKeeper authentication payload and any<br>TLS keystore or truststore passwords that were reachable through it.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.<br>

### References
* https://lists.apache.org/thread/ohw4s30rhm2r20498c0zbqxyy7xd5hxl


### Credits
* The ASF using Claude Agents (finder)


## Blobstore Authorization Bypass via Rebalance Configuration Overrides ## { #CVE-2026-82432 }

CVE-2026-82432 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82432) [\[CVE json\]](./CVE-2026-82432.cve.json) [\[OSV json\]](./CVE-2026-82432.osv.json)



_Last updated: 2026-09-14T14:11:26.098Z_

### Affected

* Apache Storm Nimbus from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>Nimbus validated `topology.blobstore.map` against the calling subject at submission time only. The rebalance<br>operation accepts configuration overrides and stripped a small set of keys from them, but never re-ran that<br>validation, so a caller authorised to rebalance a topology could introduce a blobstore map entry naming a<br>blob whose ACL does not grant them access. Supervisors localise whatever key the map names, placing the<br>blob's contents into the topology's working directory.<br><br>The same advisory covers `listBlobs`, which performed no authorization check and passed no subject, unlike<br>the neighbouring `getBlobMeta` and `beginBlobDownload` operations. It therefore returned every key in the<br>blobstore to any caller able to reach the Nimbus Thrift port, which provides the key names that make the<br>above practical. On its own the disclosure is metadata only.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where rebalance configuration overrides are validated exactly as submission-time<br>configuration is, against the rebalancing caller, and where `listBlobs` applies the configured<br>authorization.<br><br>Users who cannot upgrade immediately should restrict rebalance rights to trusted principals, keeping in mind<br>that membership of a topology's `topology.users` or `topology.groups` confers them.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.<br>

### References
* https://lists.apache.org/thread/psy1gj77jhf9y3lhph9yz4f5fovmkz7b


### Credits
* The ASF using Claude Agents (finder)


## Authorization Bypass When nimbus.groups Is Configured Without nimbus.users ## { #CVE-2026-82431 }

CVE-2026-82431 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82431) [\[CVE json\]](./CVE-2026-82431.cve.json) [\[OSV json\]](./CVE-2026-82431.osv.json)



_Last updated: 2026-09-14T14:14:47.150Z_

### Affected

* Apache Storm Client from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>`SimpleACLAuthorizer` evaluated the user-level command set by returning early when `nimbus.users` was empty,<br>before `nimbus.groups` was considered. An operator who restricted cluster access by group alone, leaving<br>`nimbus.users` unset, therefore received no restriction at all: every authenticated principal was permitted<br>every user-level operation, including `submitTopology`, `beginFileUpload` and `getNimbusConf`.<br><br>`docs/SECURITY.md` presents `nimbus.groups` as a supported way to lock down a cluster, so a deployment<br>following the documentation could believe it was restricted while it was not. The failure is silent; nothing<br>in the logs or the configuration indicates that the group list is being ignored.<br><br>Both lists left empty continues to mean that no restriction is configured, which is the shipped default and<br>is unchanged.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where `nimbus.groups` is evaluated whether or not `nimbus.users` is set.<br><br>Users who cannot upgrade immediately should additionally populate `nimbus.users` with the intended<br>principals, since a non-empty user list causes the group list to be evaluated on affected versions.<br>Operators should review Nimbus access logs for operations by principals outside the intended groups.<br><br>Note that after upgrading, a cluster configured with `nimbus.groups` alone becomes restrictive for the first<br>time. This includes `NimbusClient`, which calls `getLeader` on every connection, so clients outside the<br>configured groups will begin to be refused.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.<br>

### References
* https://lists.apache.org/thread/s335qxb6woqb35ho3fpq7toytsz1gpts


### Credits
* The ASF using Claude Agents (finder)


## Local Privilege Escalation to Root via Container Command Files Chowned to the Tenant ## { #CVE-2026-82430 }

CVE-2026-82430 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82430) [\[CVE json\]](./CVE-2026-82430.cve.json) [\[OSV json\]](./CVE-2026-82430.osv.json)



_Last updated: 2026-09-14T14:15:57.534Z_

### Affected

* Apache Storm Worker Launcher from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>When launching a Docker or OCI worker, the setuid-root `worker-launcher` first changes ownership of the<br>entire worker directory to the untrusted topology user, and only afterwards reads and acts on the command<br>file that the supervisor wrote into that same directory. The file is opened without `O_NOFOLLOW` and without<br>re-verifying its owner, so between the ownership change and the read the tenant can replace its contents.<br><br>For the Docker path the parsed command is executed with real uid 0, and the command sanitiser is not a<br>privilege boundary: it admits `-v` with an arbitrary source, `--device`, `--cap-add`, `--security-opt`,<br>`--user` and `--net`, and copies positional arguments through verbatim. A rewritten file therefore yields an<br>attacker-authored, root-equivalent container invocation with the host filesystem available.<br><br>For the OCI path the same rewrite window applies, and mount validation is structural only, with no<br>source or destination allow-list, so arbitrary host paths can be bind-mounted read-write into the<br>container. The `username` field of the command file is likewise attacker-settable and is checked only<br>against non-root and minimum-uid rules, permitting execution as another tenant's uid.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where the command file is validated before the ownership change and re-verified on open,<br>and where mount sources and destinations are constrained by configuration.<br><br>Users who cannot upgrade immediately should disable Docker and OCI worker isolation, or restrict topology<br>submission on affected supervisors to trusted principals. Note that the launcher must be rebuilt and<br>reinstalled after upgrading.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.

### References
* https://lists.apache.org/thread/8d5pkn486p8vrz5klg6onk5r8k9sd9lv


### Credits
* The ASF using Claude Agents (finder)


## Local Privilege Escalation to Root via a Time-of-Check Race in the Worker Launcher ## { #CVE-2026-82429 }

CVE-2026-82429 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82429) [\[CVE json\]](./CVE-2026-82429.cve.json) [\[OSV json\]](./CVE-2026-82429.osv.json)



_Last updated: 2026-09-14T14:16:44.051Z_

### Affected

* Apache Storm Worker Launcher from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>The setuid-root `worker-launcher` binary adjusts ownership and permissions of worker directories by walking<br>the tree with FTS and calling `lchown` and `chmod` on each entry's full pathname while running with an<br>effective uid of 0. Both syscalls re-resolve the path at the time of the call, after FTS has classified the<br>entry, and the trees being walked are owned and writable by the untrusted topology user.<br><br>A tenant running code on a supervisor node could therefore replace an intermediate directory component with<br>a symbolic link between classification and the privileged operation, redirecting the root-owned `lchown` or<br>`chmod` at an arbitrary file on the host. The operation is repeatable at will, since crashing a worker<br>forces a relaunch and blob updates re-run the walk, so a failed attempt costs the attacker nothing.<br><br>This crosses the boundary that `supervisor.run.worker.as.user` and container isolation are intended to<br>enforce. It is the same defect class as the Hadoop container-executor issues from which this code derives.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where the privileged walk operates on file descriptors it has already stat'd rather than<br>on pathnames re-resolved at call time.<br><br>Users who cannot upgrade immediately should not run untrusted topology code on supervisors configured with<br>`supervisor.run.worker.as.user`, since the launcher is the boundary being crossed. Note that the launcher<br>must be rebuilt and reinstalled after upgrading; replacing the Java artifacts alone is not sufficient.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.<br>

### References
* https://lists.apache.org/thread/9vjqrt28g0mxg304vw6pw46cx72v4rvq


### Credits
* The ASF using Claude Agents (finder)


## Cross-Tenant Dependency Jar Substitution via Predictable Blob Keys ## { #CVE-2026-82428 }

CVE-2026-82428 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82428) [\[CVE json\]](./CVE-2026-82428.cve.json) [\[OSV json\]](./CVE-2026-82428.osv.json)



_Last updated: 2026-09-14T14:18:08.670Z_

### Affected

* Apache Storm Client from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>Dependency artifacts uploaded with `storm jar --artifacts` were stored under a blob key derived only from<br>the Maven coordinate, for example `dep---.jar`. The key was therefore identical<br>for every user of the cluster and predictable in advance. When the blob already existed, the uploader<br>caught `KeyAlreadyExistsException` and silently reused it, with no check that the existing blob's content<br>or owner matched the artifact the submitter had resolved.<br><br>A user who uploaded a blob under such a key first therefore controlled the bytes that every later submitter<br>of the same coordinate would receive on the worker classpath, resulting in code execution inside another<br>tenant's topology.<br><br>This affects deployments where more than one principal may create blobs and where the `--artifacts`<br>dependency feature is used.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where each uploaded artifact receives a key carrying a freshly generated UUID and a<br>pre-existing blob is no longer silently reused.<br><br>Note that the corrected key generation is on the SUBMITTING CLIENT, so upgrading the cluster alone does not<br>close this; every client that runs `storm jar --artifacts` must also be upgraded. Operators should audit<br>existing `dep-` blobs for unexpected owners before upgrading. Users who cannot upgrade immediately should<br>avoid the `--artifacts` mechanism in multi-tenant clusters and distribute dependencies inside the topology<br>jar instead.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.<br>

### References
* https://lists.apache.org/thread/pj3fspp4l10fgk2jkvrnqsmxycmjv622


### Credits
* The ASF using Claude Agents (finder)


## Path Traversal as the Supervisor User via Unsanitised Blobstore Map Local Name ## { #CVE-2026-82427 }

CVE-2026-82427 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82427) [\[CVE json\]](./CVE-2026-82427.cve.json) [\[OSV json\]](./CVE-2026-82427.osv.json)



_Last updated: 2026-09-14T14:19:14.743Z_

### Affected

* Apache Storm Nimbus from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>A topology's `topology.blobstore.map` lets the submitter choose a local name for each blob that the<br>supervisor localises. That name was used to build a path under the topology's working directory without<br>normalisation, in both `AsyncLocalizer` and `Container.createBlobstoreLinks`, and the symlink helper<br>force-deletes whatever already exists at the target before creating the link.<br><br>A submitter could therefore use `../` segments to direct that delete-and-symlink operation at an arbitrary<br>path, as the supervisor user, on every node the topology is scheduled onto. The consequences include<br>recursive deletion of supervisor-owned content and planting a symlink that causes a subsequent worker<br>launch to execute attacker-chosen code as another tenant's operating-system user, which defeats the<br>isolation that `supervisor.run.worker.as.user` is intended to provide.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where the resolved target must lie inside the expected root at both call sites.<br><br>Users who cannot upgrade immediately should restrict topology submission to trusted principals, and may<br>reject submissions whose `topology.blobstore.map` entries contain path separators or `..` segments before<br>they reach Nimbus.<br><br><b>Credit</b><br><br>The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.<br>

### References
* https://lists.apache.org/thread/o0j51w6m0qdmwypvzfnd8w97s7ysnmyj


### Credits
* The ASF using Claude Agents (finder)


## Arbitrary File Read on Nimbus via Unvalidated Uploaded Jar Location ## { #CVE-2026-82426 }

CVE-2026-82426 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82426) [\[CVE json\]](./CVE-2026-82426.cve.json) [\[OSV json\]](./CVE-2026-82426.osv.json)



_Last updated: 2026-09-14T14:04:15.864Z_

### Affected

* Apache Storm Nimbus from 3.0.0 before 3.1.0


### Description

<b>Description</b><br><br>Nimbus accepted the `uploadedJarLocation` argument of `submitTopology` / `submitTopologyWithOpts` as a<br>server-side path and opened it directly, without checking that it referred to a file the caller had<br>actually uploaded. The intended flow is that a client first calls `beginFileUpload`, which returns a path<br>inside the Nimbus inbox, and uploads the jar in chunks to that location; nothing bound submission to that<br>flow, and the `uploaders` map populated by `beginFileUpload` was never consulted at submit time.<br><br>An authenticated user with topology submission rights could therefore submit any path readable by the<br>Nimbus daemon user as their topology jar. Nimbus copied the file into the topology's jar blob, and the<br>blob ACL grants the submitting subject read access, so the contents could then be retrieved with the<br>ordinary blob download RPCs. Candidate targets include the Nimbus Kerberos keytab, Thrift and UI TLS<br>private keys, and `storm.yaml` with the ZooKeeper authentication payload. Possession of the Nimbus keytab<br>turns an ordinary tenant into a cluster administrator.<br><br>In a deployment configured as the documentation recommends, submission is available to every<br>authenticated principal when `nimbus.users` is unset, so no elevated privilege is required.<br><br><b>Mitigation</b><br><br>Upgrade to 3.1.0, where the submitted location is canonicalised and must resolve inside the Nimbus inbox.<br><br>Users who cannot upgrade immediately should restrict topology submission to trusted principals via<br>`nimbus.users` or `nimbus.groups`, and should treat any file readable by the Nimbus daemon user as<br>potentially exposed to submitters: rotate the Nimbus keytab and any TLS private keys or ZooKeeper<br>credentials reachable from that account. Local mode is unaffected.<div><br></div><div><b>Credit</b><br><br>Independently reported to the Apache Storm PMC by n0mi1k, with a proof of concept.<br><br>Also found by the ASF using Claude agents to study the security of open-source projects, validated and reported by Apache Storm.</div>

### References
* https://lists.apache.org/thread/cq3xzxvvhtb6brbp9nl9p8kobnvtmnwc


### Credits
* n0mi1k (finder)
* The ASF using Claude Agents (finder)


## Anonymous principal assigned on TLS client certificate verification failure ## { #CVE-2026-41081 }

CVE-2026-41081 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41081) [\[CVE json\]](./CVE-2026-41081.cve.json) [\[OSV json\]](./CVE-2026-41081.osv.json)



_Last updated: 2026-04-27T13:10:44.288Z_

### Affected

* Apache Storm Client before 2.8.7


### Description

<b>Improper Handling of TLS Client Authentication Failure Leading to Anonymous Principal Assignment in Apache Storm</b><br><br><b>Versions Affected:</b> up to 2.8.7<br><br><b>Description: </b>When TLS transport is enabled in Apache Storm without requiring client certificate authentication (the default configuration), the TlsTransportPlugin assigns a fallback principal (CN=ANONYMOUS) if no client certificate is presented or if certificate verification fails. The underlying SSLPeerUnverifiedException is caught and suppressed rather than rejecting the connection.<br><br>This fail-open behavior means an unauthenticated client can establish a TLS connection and receive a valid principal identity. If the configured authorizer (e.g., SimpleACLAuthorizer) does not explicitly deny access to CN=ANONYMOUS, this may result in unauthorized access to Storm services. The condition is logged at debug level only, reducing visibility in production.<br><br><b>Impact:</b> Unauthenticated clients may be assigned a principal identity, potentially bypassing authorization in permissive or misconfigured environments.<br><br><b>Mitigation:</b> Users should upgrade to 2.8.7 in which TLS authentication failures are handled in a fail-closed manner.<br><br><b>Users who cannot upgrade immediately should:</b><br>- Enable mandatory client certificate authentication (nimbus.thrift.tls.client.auth.required: true)<br>- Ensure authorization rules explicitly deny access to CN=ANONYMOUS<br>- Review all ACL configurations for implicit default-allow behavior<br>

### References
* https://lists.apache.org/thread/plxx5l29dvplk5rwzdcq53rdfl6v4gs8


### Credits
* K (finder)


## Disabling TLS verification for Prometheus Reporter also disables it for all other connections ## { #CVE-2026-40557 }

CVE-2026-40557 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40557) [\[CVE json\]](./CVE-2026-40557.cve.json) [\[OSV json\]](./CVE-2026-40557.osv.json)



_Last updated: 2026-04-27T13:12:09.640Z_

### Affected

* Apache Storm Prometheus Reporter from 2.6.3 before 2.8.7


### Description

<p><strong>Improper Certificate Validation via Global SSL Context Downgrade in Apache Storm Prometheus Reporter</strong></p>
<p><b>Versions Affected: </b>from 2.6.3 to 2.8.6</p>
<p><b>Description:&nbsp;</b></p><p><span style="background-color: rgb(255, 255, 255);">In production deployments where an administrator enables </span><code>storm.daemon.metrics.reporter.plugin.prometheus.skip_tls_validation&nbsp;</code>(by default it is disabled)&nbsp;<span style="background-color: rgb(255, 255, 255);">intending to affect only the Prometheus reporter, the undocumented global side effect creates an attack surface across every TLS-protected communication channel in the Storm daemon.</span><b><br></b></p><p>The <code>PrometheusPreparableReporter</code> class implements an <code>INSECURE_TRUST_MANAGER</code> that accepts all SSL certificates without validation, with empty <code>checkClientTrusted</code> and <code>checkServerTrusted</code> methods. Most critically, when the <code>storm.daemon.metrics.reporter.plugin.prometheus.skip_tls_validation</code> configuration option is enabled (default = disabled) for HTTPS Prometheus PushGateway connections, the <code>INSECURE_CONNECTION_FACTORY</code> calls <code>SSLContext.setDefault(sslContext)</code>, which globally replaces the JVM's default SSL context rather than applying the insecure context only to the Prometheus connection. This payload flows through storm.yaml configuration → <code>PrometheusPreparableReporter.prepare()</code> → <code>INSECURE_CONNECTION_FACTORY</code> → <code>SSLContext.setDefault()</code>, resulting in a JVM-wide TLS security downgrade. All subsequent HTTPS connections in the process - including ZooKeeper, Thrift, Netty, and UI connections - silently trust all certificates, including self-signed, expired, and attacker-generated ones, enabling man-in-the-middle interception of cluster state, topology submissions, tuple data, and administrative credentials.<br></p>

<p><b>Mitigation:</b> 2.x users should upgrade to 2.8.7 if the Prometheus Metrics Reporter is used. Prometheus Metrics Reporter Users who cannot upgrade immediately should remove the <code>storm.daemon.metrics.reporter.plugin.prometheus.skip_tls_validation: true</code> setting from their storm.yaml configuration and instead configure a proper truststore containing the PushGateway's certificate.<br></p>
<br>

### References
* https://lists.apache.org/thread/f5bv68z1y5xstz22psjk05p3wn86knjq


### Credits
* K (finder)


## Stored Cross-Site Scripting (XSS) via Unsanitized Topology Metadata in Storm UI ## { #CVE-2026-35565 }

CVE-2026-35565 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-35565) [\[CVE json\]](./CVE-2026-35565.cve.json) [\[OSV json\]](./CVE-2026-35565.osv.json)



_Last updated: 2026-04-13T09:10:15.976Z_

### Affected

* Apache Storm UI before 2.8.6


### Description

<p><strong>Stored Cross-Site Scripting (XSS) via Unsanitized Topology Metadata in Apache Storm UI</strong></p>
<p><strong>Versions Affected:</strong> before 2.8.6</p>
<p><strong>Description:</strong> The Storm UI visualization component interpolates topology metadata including component IDs, stream names, and grouping values directly into HTML via <code>innerHTML</code> in <code>parseNode()</code> and <code>parseEdge()</code> without sanitization at any layer. An authenticated user with topology submission rights could craft a topology containing malicious HTML/JavaScript in component identifiers (e.g., a bolt ID containing an <code>onerror</code> event handler). This payload flows through Nimbus → Thrift → the Visualization API → vis.js tooltip rendering, resulting in stored cross-site scripting.&nbsp;</p><p>In multi-tenant deployments where topology submission is available to less-trusted users but the UI is accessed by operators or administrators, this enables privilege escalation through script execution in an admin's browser session.</p>
<p><strong>Mitigation:</strong>&nbsp;2.x users should upgrade to 2.8.6. Users who cannot upgrade immediately should monkey-patch the <code>parseNode()</code> and <code>parseEdge()</code> functions in the visualization JavaScript file to HTML-escape all API-supplied values including <code>nodeId</code>, <code>:capacity</code>, <code>:latency</code>, <code>:component</code>, <code>:stream</code>, and <code>:grouping</code>&nbsp;before interpolation into tooltip HTML strings, and should additionally restrict topology submission to trusted users via Nimbus ACLs as a defense-in-depth measure.&nbsp;A guide on how to do this is available in the release notes of 2.8.6.</p><b>Credit:</b> This issue was discovered while investigating another report by K.<br>

### References
* https://storm.apache.org/2026/04/12/storm286-released.html


## RCE through Unsafe Deserialization via Kerberos TGT Credential Handling ## { #CVE-2026-35337 }

CVE-2026-35337 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-35337) [\[CVE json\]](./CVE-2026-35337.cve.json) [\[OSV json\]](./CVE-2026-35337.osv.json)



_Last updated: 2026-04-13T09:11:04.526Z_

### Affected

* Apache Storm Client before 2.8.6


### Description

<p><b>Deserialization of Untrusted Data vulnerability in Apache Storm.</b></p><p><strong>Versions Affected:</strong>
before 2.8.6.</p>
<p><strong>Description:</strong>
When processing topology credentials submitted via the Nimbus Thrift API, Storm deserializes the base64-encoded TGT blob using <code>ObjectInputStream.readObject()</code> without any class filtering or validation.&nbsp;An authenticated user with topology submission rights could supply a crafted serialized object in the <code>"TGT"</code> credential field, leading to remote code execution in both the Nimbus and Worker JVMs.</p>
<p><strong>Mitigation:</strong>
2.x users should upgrade to 2.8.6.</p>
<p>Users who cannot upgrade immediately should monkey-patch an <code>ObjectInputFilter</code> allow-list to <code>ClientAuthUtils.deserializeKerberosTicket()</code> restricting deserialized classes to <code>javax.security.auth.kerberos.KerberosTicket</code> and its known dependencies. A guide on how to do this is available in the release notes of 2.8.6.</p><p><span style="background-color: rgb(255, 255, 255);"><b>Credit:</b> This issue was discovered by K.</span><br></p>

### References
* https://storm.apache.org/2026/04/12/storm286-released.html


### Credits
* K (finder)


## Local Information Disclosure Vulnerability in Storm-core on Unix-Like systems due temporary files ## { #CVE-2023-43123 }

CVE-2023-43123 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-43123) [\[CVE json\]](./CVE-2023-43123.cve.json) [\[OSV json\]](./CVE-2023-43123.osv.json)



_Last updated: 2023-11-23T09:16:32.695Z_

### Affected

* Apache Storm from 2.0.0 before 2.6.0


### Description

<div>On unix-like systems, the temporary directory is shared between all user. As such, writing to this directory using APIs that do not explicitly set the file/directory permissions can lead to information disclosure. Of note, this does not impact modern MacOS Operating Systems.<br><br>The method File.createTempFile on unix-like systems creates a file with predefined name (so easily identifiable) and by default will create this file with the permissions -rw-r--r--. Thus, if sensitive information is written to this file, other local users can read this information.<br></div><div><br></div><div>File.createTempFile(String, String) will create a temporary file in the system temporary directory if the 'java.io.tmpdir' system property is not explicitly set. <br><br>This affects the class&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/storm/blob/master/storm-core/src/jvm/org/apache/storm/utils/TopologySpoutLag.java#L99">https://github.com/apache/storm/blob/master/storm-core/src/jvm/org/apache/storm/utils/TopologySpoutLag.java#L99</a>&nbsp;and was introduced by&nbsp;<a target="_blank" rel="nofollow" href="https://issues.apache.org/jira/browse/STORM-3123">https://issues.apache.org/jira/browse/STORM-3123</a><br></div><div><br>In practice, this has a very limited impact as this class is used only if&nbsp;<span style="background-color: rgb(206, 204, 247);">ui.disable.spout.lag.monitoring</span></div> <div><span style="background-color: var(--wht);">is set to false, but its value is true by default.<br>Moreover, the temporary file gets deleted soon after its creation.<br><br>The solution is to use&nbsp;</span><span style="background-color: var(--hig);"><a target="_blank" rel="nofollow" href="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/nio/file/Files.html#createTempFile(java.lang.String,java.lang.String,java.nio.file.attribute.FileAttribute...)">Files.createTempFile</a></span><span style="background-color: var(--wht);">&nbsp;instead.<br><br>We recommend that all users upgrade to the latest version of Apache Storm.</span></div><div><span style="background-color: var(--wht);"><br></span></div><br>

### References
* https://lists.apache.org/thread/88oc1vqfjtr29cz5xts0v2wm5pmhbm0l


### Credits
* Andrea Cosentino from Apache Software Foundation (finder)


## Unsafe Pre-Authentication Deserialization In Workers ## { #CVE-2021-40865 }

CVE-2021-40865 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-40865) [\[CVE json\]](./CVE-2021-40865.cve.json) [\[OSV json\]](./CVE-2021-40865.osv.json)



_Last updated: 2021-10-21T21:27:58.697Z_

### Affected

* Apache Storm from v1.0.0 before Apache Storm *
* Apache Storm from Apache Storm before v1.2.4


### Description

An Unsafe Deserialization vulnerability exists in the worker services of the Apache Storm supervisor server allowing pre-auth Remote Code Execution (RCE).  Apache Storm 2.2.x users should upgrade to version 2.2.1 or 2.3.0. Apache Storm 2.1.x users should upgrade to version 2.1.1. Apache Storm 1.x users should upgrade to version 1.2.4

### References
* https://lists.apache.org/thread.html/r8d45e74299897b6734dd0f788c46a631009ce2eeb731523386f7a253%40%3Cuser.storm.apache.org%3E
* https://seclists.org/oss-sec/2021/q4/45


### Credits
* Apache Storm would like to thank @pwntester Alvaro Muñoz of the GitHub Security Lab team for reporting this issue.


## Shell Command Injection Vulnerability in Nimbus Thrift Server ## { #CVE-2021-38294 }

CVE-2021-38294 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-38294) [\[CVE json\]](./CVE-2021-38294.cve.json) [\[OSV json\]](./CVE-2021-38294.osv.json)



_Last updated: 2021-10-21T22:16:43.838Z_

### Affected

* Apache Storm from v1.0.0 before Apache Storm*
* Apache Storm from Apache Storm before v1.2.4


### Description

A Command Injection vulnerability exists in the getTopologyHistory service of the Apache Storm 2.x prior to 2.2.1 and Apache Storm 1.x prior to 1.2.4. A specially crafted thrift request to the Nimbus server allows Remote Code Execution (RCE) prior to authentication. 

### References
* https://lists.apache.org/thread.html/r5fe881f6ca883908b7a0f005d35115af49f43beea7a8b0915e377859%40%3Cuser.storm.apache.org%3E
* https://seclists.org/oss-sec/2021/q4/44


### Credits
* Apache Storm would like to thank @pwntester Alvaro Muñoz of the GitHub Security Lab team for reporting this issue.
