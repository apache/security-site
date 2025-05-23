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

CVE-2021-27905 [\[CVE json\]](./CVE-2021-27905.cve.json) [\[OSV json\]](./CVE-2021-27905.osv.json)



_Last updated: 2021-04-13T06:30:52.402Z_

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

CVE-2021-29262 [\[CVE json\]](./CVE-2021-29262.cve.json) [\[OSV json\]](./CVE-2021-29262.osv.json)



_Last updated: 2021-04-13T06:28:50.304Z_

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

CVE-2021-29943 [\[CVE json\]](./CVE-2021-29943.cve.json) [\[OSV json\]](./CVE-2021-29943.osv.json)



_Last updated: 2021-04-13T06:29:18.585Z_

### Affected

* Apache Solr from Apache Solr before 8.8.2


### Description

When using ConfigurableInternodeAuthHadoopPlugin for authentication, Apache Solr versions prior to 8.8.2 would forward/proxy distributed requests using server credentials instead of original client credentials. This would result in incorrect authorization resolution on the receiving hosts.

### References
* https://lists.apache.org/thread.html/r91dd0ff556e0c9aab4c92852e0e540c59d4633718ce12881558cf44d%40%3Cusers.solr.apache.org%3E


### Credits
* Geza Nagy


## Apache Solr information disclosure vulnerability through DataImportHandler ## { #CVE-2021-44548 }

CVE-2021-44548 [\[CVE json\]](./CVE-2021-44548.cve.json) [\[OSV json\]](./CVE-2021-44548.osv.json)



_Last updated: 2021-12-23T08:51:22.228Z_

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


## Host environment variables are published via the Metrics API ## { #CVE-2023-50290 }

CVE-2023-50290 [\[CVE json\]](./CVE-2023-50290.cve.json) [\[OSV json\]](./CVE-2023-50290.osv.json)



_Last updated: 2024-01-15T09:32:41.749Z_

### Affected

* Apache Solr from 9.0.0 before 9.3.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Solr.<br><p>The Solr Metrics API publishes all unprotected environment variables available to each Apache Solr instance. Users are able to specify which environment variables to hide, however, the default list is designed to work for known secret Java system properties. Environment variables cannot be strictly defined in Solr, like Java system properties can be, and may be set for the entire host,&nbsp;unlike Java system properties which are set per-Java-proccess.</p>The Solr Metrics API is protected by the "metrics-read" permission.<br>Therefore, Solr Clouds with Authorization setup will only be vulnerable via users with the "metrics-read" permission.<br><p>This issue affects Apache Solr: from 9.0.0 before 9.3.0.</p><p>Users are recommended to upgrade to version 9.3.0 or later, in which environment variables are not published via the Metrics API.</p>

### References
* https://solr.apache.org/security.html#cve-2023-50290-apache-solr-allows-read-access-to-host-environment-variables


## System Property redaction logic inconsistency can lead to leaked passwords ## { #CVE-2023-50291 }

CVE-2023-50291 [\[CVE json\]](./CVE-2023-50291.cve.json) [\[OSV json\]](./CVE-2023-50291.osv.json)



_Last updated: 2024-02-09T17:29:31.072Z_

### Affected

* Apache Solr from 6.0.0 through 8.11.2
* Apache Solr from 9.0.0 before 9.3.0


### Description

Insufficiently Protected Credentials vulnerability in Apache Solr.<p></p><p>This issue affects Apache Solr: from 6.0.0 through 8.11.2, from 9.0.0 before 9.3.0.<span style="background-color: rgb(255, 255, 255);"><br></span>One of the two endpoints that publishes the Solr process' Java system properties, /admin/info/properties, was only setup to hide system properties that had "password" contained in the name.<br>There are a number of sensitive system properties, such as "basicauth" and "aws.secretKey" do not contain "password", thus their values were published via the "/admin/info/properties" endpoint.<br><span style="background-color: rgb(255, 255, 255);">This endpoint populates the list of System Properties on the home screen of the Solr Admin page, making the exposed credentials visible in the UI.</span><br></p>This /admin/info/properties endpoint is protected under the "config-read" permission.<br>Therefore, Solr Clouds with Authorization enabled will only be vulnerable through logged-in users that have the "config-read" permission.<br><p>Users are recommended to upgrade to version 9.3.0 or 8.11.3, which fixes the issue.<br>A single option now controls hiding Java system property for all endpoints, "-Dsolr.hiddenSysProps".<br>By default all known sensitive properties are hidden (including "-Dbasicauth"), as well as any property with a name containing "secret" or "password".</p><p>Users who cannot upgrade can also use the following Java system property to fix the issue:<br>&nbsp; '-D<span style="background-color: rgb(255, 255, 255);">solr.redaction.system.pattern</span>=.*(password|secret|basicauth).*'</p><p></p>

### References
* https://solr.apache.org/security.html#cve-2023-50291-apache-solr-can-leak-certain-passwords-due-to-system-property-redaction-logic-inconsistencies


### Credits
* Michael Taggart (reporter)


## Solr Schema Designer blindly "trusts" all configsets, possibly leading to RCE by unauthenticated users ## { #CVE-2023-50292 }

CVE-2023-50292 [\[CVE json\]](./CVE-2023-50292.cve.json) [\[OSV json\]](./CVE-2023-50292.osv.json)



_Last updated: 2024-02-09T17:29:19.451Z_

### Affected

* Apache Solr from 8.10.0 through 8.11.2
* Apache Solr from 9.0.0 before 9.3.0


### Description

Incorrect Permission Assignment for Critical Resource, Improper Control of Dynamically-Managed Code Resources vulnerability in Apache Solr.<p></p><p>This issue affects Apache Solr: from 8.10.0 through 8.11.2, from 9.0.0 before 9.3.0.<br><br>The Schema Designer was introduced to allow users to more easily configure and test new Schemas and configSets.<br>However, when the feature was created, the "trust" (authentication) of these configSets was not considered.<br>External library loading is only available to configSets that are "trusted" (created by authenticated users), thus non-authenticated users are unable to perform Remote Code Execution.<br>Since the Schema Designer loaded configSets without taking their "trust" into account, configSets that were created by unauthenticated users were allowed to load external libraries when used in the Schema Designer.<br></p><p>Users are recommended to upgrade to version 9.3.0, which fixes the issue.</p><p></p>

### References
* https://solr.apache.org/security.html#cve-2023-50298-apache-solr-can-expose-zookeeper-credentials-via-streaming-expressions


### Credits
* Skay (reporter)


## Solr can expose ZooKeeper credentials via Streaming Expressions ## { #CVE-2023-50298 }

CVE-2023-50298 [\[CVE json\]](./CVE-2023-50298.cve.json) [\[OSV json\]](./CVE-2023-50298.osv.json)



_Last updated: 2024-02-09T17:29:05.785Z_

### Affected

* Apache Solr from 6.0.0 through 8.11.2
* Apache Solr from 9.0.0 before 9.4.1


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Solr.<p>This issue affects Apache Solr: from 6.0.0 through 8.11.2, from 9.0.0 before 9.4.1.</p>Solr Streaming Expressions allows users to extract data from other Solr Clouds, using a "zkHost" parameter.<br>When original SolrCloud is setup to use ZooKeeper credentials and ACLs, they will be sent to whatever "zkHost" the user provides.<br>An attacker could setup a server to mock ZooKeeper, that accepts ZooKeeper requests with credentials and ACLs and extracts the sensitive information,<br>then send a streaming expression using the mock server's address in "zkHost".<br><p>Streaming Expressions are exposed via the "/streaming" handler, with "read" permissions.</p><p>Users are recommended to upgrade to version 8.11.3 or 9.4.1, which fix the issue.<br>From these versions on, only zkHost values that have the same server address (regardless of chroot), will use the given ZooKeeper credentials and ACLs when connecting.</p>

### References
* https://solr.apache.org/security.html#cve-2023-50298-apache-solr-can-expose-zookeeper-credentials-via-streaming-expressions


### Credits
* Qing Xu (reporter)


## Backup/Restore APIs allow for deployment of executables in malicious ConfigSets ## { #CVE-2023-50386 }

CVE-2023-50386 [\[CVE json\]](./CVE-2023-50386.cve.json) [\[OSV json\]](./CVE-2023-50386.osv.json)



_Last updated: 2024-02-09T17:28:49.163Z_

### Affected

* Apache Solr from 6.0.0 through 8.11.2
* Apache Solr from 9.0.0 before 9.4.1


### Description

Improper Control of Dynamically-Managed Code Resources, Unrestricted Upload of File with Dangerous Type, Inclusion of Functionality from Untrusted Control Sphere vulnerability in Apache Solr.<p>This issue affects Apache Solr: from 6.0.0 through 8.11.2, from 9.0.0 before 9.4.1.</p>In the affected versions, Solr ConfigSets accepted Java jar and class files to be uploaded through the ConfigSets API.<br>When backing up Solr Collections, these configSet files would be saved to disk when using the LocalFileSystemRepository (the default for backups).<br>If the backup was saved to a directory that Solr uses in its ClassPath/ClassLoaders, then the jar and class files would be available to use with any ConfigSet, trusted or untrusted.<br><br>When Solr is run in a secure way (Authorization enabled), as is strongly suggested, this vulnerability is limited to extending the Backup permissions with the ability to add libraries.<br><p>Users are recommended to upgrade to version 8.11.3 or 9.4.1, which fix the issue.<br>In these versions, the following protections have been added:</p><ul><li>Users are no longer able to upload files to a configSet that could be executed via a Java ClassLoader.</li><li>The Backup API restricts saving backups to directories that are used in the ClassLoader.</li></ul>

### References
* https://solr.apache.org/security.html#cve-2023-50386-apache-solr-backuprestore-apis-allow-for-deployment-of-executables-in-malicious-configsets


### Credits
* L3yx (reporter)


## Solr-Operator liveness and readiness probes may leak basic auth credentials ## { #CVE-2024-31391 }

CVE-2024-31391 [\[CVE json\]](./CVE-2024-31391.cve.json) [\[OSV json\]](./CVE-2024-31391.osv.json)



_Last updated: 2024-04-12T15:00:22.627Z_

### Affected

* Apache Solr Operator from 0.3.0 through 0.8.0


### Description

Insertion of Sensitive Information into Log File vulnerability in the Apache Solr Operator.<br><br>This issue affects all versions of the Apache Solr Operator from 0.3.0 through 0.8.0.<br><br>When asked to bootstrap Solr security, the operator will enable basic authentication and create several accounts for accessing Solr: including the "solr" and "admin" accounts for use by end-users, and a "k8s-oper" account which the operator uses for its own requests to Solr.<br>One common source of these operator requests is healthchecks: liveness, readiness, and startup probes are all used to determine Solr's health and ability to receive traffic.<br>By default, the operator configures the Solr APIs used for these probes to be exempt from authentication, but&nbsp;users may specifically request that authentication be required on probe endpoints as well.<br>Whenever one of these probes would fail, if authentication was in use, the Solr Operator would create a Kubernetes "event" containing the username and password of the "k8s-oper" account.<br><br>Within the affected version range, this vulnerability affects any solrcloud resource which (1) bootstrapped security through use of the `.solrOptions.security.authenticationType=basic` option, and (2) required authentication be used on probes by setting `.solrOptions.security.probesRequireAuth=true`.<br><br>Users are recommended to upgrade to Solr Operator version 0.8.1, which fixes this issue by ensuring that probes no longer print the credentials used for Solr requests.&nbsp; Users may also mitigate the vulnerability by disabling authentication on their healthcheck probes using the setting `.solrOptions.security.probesRequireAuth=false`.<br>

### References
* https://lists.apache.org/thread/w7011s78lzywzwyszvy4d8zm99ybt8c7


### Credits
* Flip Hess (finder)


## Authentication bypass possible using a fake URL Path ending ## { #CVE-2024-45216 }

CVE-2024-45216 [\[CVE json\]](./CVE-2024-45216.cve.json) [\[OSV json\]](./CVE-2024-45216.osv.json)



_Last updated: 2024-12-03T17:55:26.574Z_

### Affected

* Apache Solr from 5.3.0 before 8.11.4
* Apache Solr from 9.0.0 before 9.7.0


### Description

<p>Improper Authentication vulnerability in Apache Solr.</p>Solr instances using the PKIAuthenticationPlugin, which is enabled by default when Solr Authentication is used, are vulnerable to Authentication bypass.<br>A fake ending at the end of any Solr API URL path, will allow requests to skip Authentication while maintaining the API contract with the original URL Path.<br>This fake ending looks like an unprotected API path, however it is stripped off internally after authentication but before API routing.<br><p></p><p>This issue affects Apache Solr: from 5.3.0 before 8.11.4, from 9.0.0 before 9.7.0.</p><p>Users are recommended to upgrade to version 9.7.0, or 8.11.4, which fix the issue.</p>

### References
* https://solr.apache.org/security.html#cve-2024-45216-apache-solr-authentication-bypass-possible-using-a-fake-url-path-ending


### Credits
* Liu Huajin (reporter)


## ConfigSets created during a backup restore command are trusted implicitly ## { #CVE-2024-45217 }

CVE-2024-45217 [\[CVE json\]](./CVE-2024-45217.cve.json) [\[OSV json\]](./CVE-2024-45217.osv.json)



_Last updated: 2024-10-16T07:51:15.128Z_

### Affected

* Apache Solr from 6.6.0 before 8.11.4
* Apache Solr from 9.0.0 before 9.7.0


### Description

<p>Insecure Default Initialization of Resource vulnerability in Apache Solr.</p><p><span style="background-color: rgb(255, 255, 255);">New ConfigSets that are created via a Restore command, which copy a configSet from the backup and give it a new name, are created without setting the "trusted" metadata.<br>ConfigSets that do not contain the flag are trusted implicitly if the metadata is missing, therefore this leads to "trusted" ConfigSets that may not have been created with an Authenticated request.</span><br><span style="background-color: rgb(255, 255, 255);">"trusted" ConfigSets are able to load custom code into classloaders, therefore the flag is supposed to only be set when the request that uploads the ConfigSet is Authenticated &amp; Authorized.</span></p><p>This issue affects Apache Solr: from 6.6.0 before 8.11.4, from 9.0.0 before 9.7.0. This issue does not affect Solr instances that are secured via Authentication/Authorization.</p><p>Users are primarily recommended to use Authentication and Authorization when running Solr. However, upgrading to version 9.7.0, or 8.11.4 will mitigate this issue otherwise.</p><p></p>

### References
* https://solr.apache.org/security.html#cve-2024-45217-apache-solr-configsets-created-during-a-backup-restore-command-are-trusted-implicitly


### Credits
* Liu Huajin (reporter)


## Configset upload on Windows allows arbitrary path write-access ## { #CVE-2024-52012 }

CVE-2024-52012 [\[CVE json\]](./CVE-2024-52012.cve.json) [\[OSV json\]](./CVE-2024-52012.osv.json)



_Last updated: 2025-01-27T08:54:39.844Z_

### Affected

* Apache Solr from 6.6 through 9.7.0


### Description

<p>Relative Path Traversal vulnerability in Apache Solr.</p>Solr instances running on Windows are vulnerable to arbitrary filepath write-access, due to a lack of input-sanitation in the "configset upload" API.&nbsp; Commonly known as a "zipslip", maliciously constructed ZIP files can use relative filepaths to write data to unanticipated parts of the filesystem.&nbsp;&nbsp;<br><p>This issue affects Apache Solr: from 6.6 through 9.7.0.</p><p>Users are recommended to upgrade to version 9.8.0, which fixes the issue.&nbsp; Users unable to upgrade may also safely prevent the issue by using Solr's "Rule-Based Authentication Plugin" to restrict access to the configset upload API, so that it can only be accessed by a trusted set of administrators/users.</p>

### References
* https://lists.apache.org/thread/yp39pgbv4vf1746pf5yblz84lv30vfxd


### Credits
* rry (finder)


## Core-creation with "trusted" configset can use arbitrary untrusted files ## { #CVE-2025-24814 }

CVE-2025-24814 [\[CVE json\]](./CVE-2025-24814.cve.json) [\[OSV json\]](./CVE-2025-24814.osv.json)



_Last updated: 2025-01-27T08:58:06.761Z_

### Affected

* Apache Solr through 9.7


### Description

<p>Core creation allows users to replace "trusted" configset files with arbitrary configuration</p>Solr instances that (1) use the "FileSystemConfigSetService" component (the default in "standalone" or "user-managed" mode), and (2) are running without authentication and authorization are vulnerable to a sort of privilege escalation wherein individual "trusted" configset files can be ignored in favor of potentially-untrusted replacements available elsewhere on the filesystem.&nbsp; These replacement config files are treated as "trusted" and can use "&lt;lib&gt;" tags to add to Solr's classpath, which an attacker might use to load malicious code as a searchComponent or other plugin.<br><br>This issue affects all Apache Solr versions up through Solr 9.7.&nbsp; Users can protect against the vulnerability by enabling authentication and authorization on their Solr clusters or switching to SolrCloud (and away from "FileSystemConfigSetService").&nbsp; Users are also recommended to upgrade to Solr 9.8.0, which mitigates this issue by disabling use of "&lt;lib&gt;" tags by default.<br>

### References
* https://lists.apache.org/thread/gl291pn8x9f9n52ys5l0pc0b6qtf0qw1


### Credits
* pwn null (finder)
