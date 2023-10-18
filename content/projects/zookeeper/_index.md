---
title: Apache ZooKeeper security advisories
description: Security information for Apache ZooKeeper
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ZooKeeper? You can read more about the projects' security policy on their [security page](https://zookeeper.apache.org/security.html), and email your report to the [Apache ZooKeeper Security Team](mailto:security@zookeeper.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://zookeeper.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Authorization bypass in SASL Quorum Peer Authentication ## { #CVE-2023-44981 }

CVE-2023-44981 [\[CVE json\]](./CVE-2023-44981.cve.json)

### Affected

* Apache ZooKeeper from 3.9.0 before 3.9.1
* Apache ZooKeeper from 3.8.0 through 3.8.2
* Apache ZooKeeper from 3.7.0 through 3.7.1
* Apache ZooKeeper before 3.7.0


### Description

Authorization Bypass Through User-Controlled Key vulnerability in Apache ZooKeeper. If SASL Quorum Peer authentication is enabled in ZooKeeper (<code>quorum.auth.enableSasl=</code><code>true)</code>, the authorization is done by verifying that the instance part in SASL authentication ID is listed in zoo.cfg server list. The instance part in SASL auth ID is optional and if it's missing, like 'eve@EXAMPLE.COM', the authorization check will be skipped.&nbsp;<span style="background-color: rgb(255, 255, 255);">As a result an arbitrary endpoint could join the cluster and begin propagating counterfeit changes to the leader, essentially giving it complete read-write access to the data tree.&nbsp;<span style="background-color: rgb(255, 255, 255);">Quorum Peer authentication is not enabled by default.</span><br><br></span><span style="background-color: var(--wht);">Users are recommended to upgrade to version 3.9.1, 3.8.3, 3.7.2, which fixes the issue.<br><br></span><span style="background-color: rgb(255, 255, 255);">Alternately ensure the ensemble election/quorum communication is protected by a firewall as this will mitigate the issue.<br><br><span style="background-color: rgb(255, 255, 255);">See the documentation for more details on correct cluster administration.</span></span><br>

### References
* https://lists.apache.org/thread/wf0yrk84dg1942z1o74kd8nycg6pgm5b


### Credits
* Damien Diederen <ddiederen@apache.org> (reporter)
