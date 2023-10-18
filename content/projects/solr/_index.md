---
title: Apache Solr security advisories
description: Security information for Apache Solr
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Solr? You can read more about the projects' security policy on their [security page](https://cwiki.apache.org/confluence/display/SOLR/SolrSecurity), and email your report to the [Apache Solr Security Team](mailto:security@solr.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://cwiki.apache.org/confluence/display/SOLR/SolrSecurity). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## SSRF vulnerability with the Replication handler ## { #CVE-2021-27905 }

CVE-2021-27905 [\[CVE json\]](./CVE-2021-27905.cve.json)

### Affected

* Apache Solr from Apache Solr before 8.8.2


### Description

The ReplicationHandler (normally registered at "/replication" under a Solr core) in Apache Solr has a "masterUrl" (also "leaderUrl" alias) parameter that is used to designate another ReplicationHandler on another Solr core to replicate index data into the local core.  To prevent a SSRF vulnerability, Solr ought to check these parameters against a similar configuration it uses for the "shards" parameter.  Prior to this bug getting fixed, it did not.
This problem affects essentially all Solr versions prior to it getting fixed in 8.8.2.

### References
* https://lists.apache.org/thread.html/r0ddc3a82bd7523b1453cb7a5e09eb5559517145425074a42eb326b10%40%3Cannounce.apache.org%3E


### Credits
* Reported by Caolinhong(Skay) from QI-ANXIN Cert (QI-ANXIN Technology Group Inc.)


## Misapplied Zookeeper ACLs can result in leakage of configured authentication and authorization settings ## { #CVE-2021-29262 }

CVE-2021-29262 [\[CVE json\]](./CVE-2021-29262.cve.json)

### Affected

* Apache Solr from Apache Solr before 8.8.2


### Description

When starting Apache Solr versions prior to 8.8.2, configured with the SaslZkACLProvider or VMParamsAllAndReadonlyDigestZkACLProvider and no existing security.json znode, if the optional read-only user is configured then Solr would not treat that node as a sensitive path and would allow it to be readable.
Additionally, with any ZkACLProvider, if the security.json is already present, Solr will not automatically update the ACLs.

### References
* https://lists.apache.org/thread.html/r536da4c4e4e406f7843461cc754a3d0a3fe575aa576e2b71a9cd57d0%40%3Cannounce.apache.org%3E


### Credits
* Timothy Potter and Mike Drob, Apple Cloud Services


## Apache Solr Unprivileged users may be able to perform unauthorized read/write to collections ## { #CVE-2021-29943 }

CVE-2021-29943 [\[CVE json\]](./CVE-2021-29943.cve.json)

### Affected

* Apache Solr from Apache Solr before 8.8.2


### Description

When using ConfigurableInternodeAuthHadoopPlugin for authentication, Apache Solr versions prior to 8.8.2 would forward/proxy distributed requests using server credentials instead of original client credentials. This would result in incorrect authorization resolution on the receiving hosts.

### References
* https://lists.apache.org/thread.html/r91dd0ff556e0c9aab4c92852e0e540c59d4633718ce12881558cf44d%40%3Cusers.solr.apache.org%3E


### Credits
* Geza Nagy


## Apache Solr information disclosure vulnerability through DataImportHandler ## { #CVE-2021-44548 }

CVE-2021-44548 [\[CVE json\]](./CVE-2021-44548.cve.json)

### Affected

* Apache Solr from unspecified before 8.11.1


### Description

An Improper Input Validation vulnerability in DataImportHandler of Apache Solr allows an attacker to provide a Windows UNC path resulting in an SMB network call being made from the Solr host to another host on the network. If the attacker has wider access to the network, this may lead to SMB attacks, which may result in:

* The exfiltration of sensitive data such as OS user hashes (NTLM/LM hashes),
* In case of misconfigured systems, SMB Relay Attacks which can lead to user impersonation on SMB Shares or, in a worse-case scenario, Remote Code Execution

This issue affects all Apache Solr versions prior to 8.11.1. This issue only affects Windows.

### References
* https://solr.apache.org/security.html#cve-2021-44548-apache-solr-information-disclosure-vulnerability-through-dataimporthandler


### Credits
* Apache Solr would like to thank LaiHan of Nsfocus security team for reporting the issue
