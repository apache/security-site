---
title: Apache Cassandra security advisories
description: Security information for Apache Cassandra
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Cassandra? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## User with MODIFY permission on ALL KEYSPACES can escalate privileges to superuser via unsafe actions (4.0.16 only) ## { #CVE-2025-26467 }

CVE-2025-26467 [\[CVE json\]](./CVE-2025-26467.cve.json) [\[OSV json\]](./CVE-2025-26467.osv.json)



_Last updated: 2025-08-25T13:14:47.609Z_

### Affected

* Apache Cassandra at 4.0.16


### Description

<p>

<span style="background-color: rgb(255, 255, 255);">Privilege Defined With Unsafe Actions vulnerability in Apache Cassandra. An user with MODIFY permission ON ALL KEYSPACES can escalate privileges to superuser within a targeted Cassandra cluster via unsafe actions to a system resource. Operators granting data MODIFY permission on all keyspaces on affected versions should review data access rules for potential breaches.</span>

<br><span style="background-color: var(--wht);"><br>This issue affects Apache Cassandra 3.0.30, 3.11.17, 4.0.16, 4.1.7, 5.0.2, but this advisory is only for 4.0.16 because the fix to CVE-2025-23015 was incorrectly applied to 4.0.16, so that version is still affected.<br></span><br>Users in the 4.0 series are recommended to upgrade to version 4.0.17 which fixes the issue. Users from 3.0, 3.11, 4.1 and 5.0 series should follow recommendation from CVE-2025-23015.<br></p>

### References
* https://lists.apache.org/thread/xxj36rr4d6mzyqpld05dn8b9951hfpz7


### Credits
* Adam Pond of Apple Services Engineering Security (finder)
* Ali Mirheidari of Apple Services Engineering Security (finder)
* Terry Thibault of Apple Services Engineering Security (finder)
* Will Brattain of Apple Services Engineering Security (finder)


## CassandraNetworkAuthorizer and CassandraCIDRAuthorizer can be bypassed allowing access to different network regions ## { #CVE-2025-24860 }

CVE-2025-24860 [\[CVE json\]](./CVE-2025-24860.cve.json) [\[OSV json\]](./CVE-2025-24860.osv.json)



_Last updated: 2025-02-04T10:17:53.494Z_

### Affected

* Apache Cassandra from 4.0.0 through 4.0.15
* Apache Cassandra from 4.1.0 through 4.1.7
* Apache Cassandra from 5.0.0 through 5.0.2


### Description

<p></p><p>Incorrect Authorization vulnerability in Apache Cassandra allowing users to access a datacenter or IP/CIDR groups they should not be able to when using CassandraNetworkAuthorizer or CassandraCIDRAuthorizer.<br><br>Users with restricted data center access can update their own permissions via data control language (DCL) statements on affected versions.<br></p><p></p><p>This issue affects Apache Cassandra: from 4.0.0 through 4.0.15 and from 4.1.0 through 4.1.7 for CassandraNetworkAuthorizer, and from 5.0.0 through 5.0.2 for both CassandraNetworkAuthorizer and CassandraCIDRAuthorizer.<br></p><p></p><p>Operators using&nbsp;CassandraNetworkAuthorizer or&nbsp;CassandraCIDRAuthorizer on affected versions should review data access rules for potential breaches. Users are recommended to upgrade to versions 4.0.16, 4.1.8, 5.0.3, which fixes the issue.<br></p><p></p>

### References
* https://lists.apache.org/thread/yjo5on4tf7s1r9qklc4byrz30b8vkm2d


### Credits
* Stefan Miklosovic (reporter)


## User with MODIFY permission on ALL KEYSPACES can escalate privileges to superuser via unsafe actions ## { #CVE-2025-23015 }

CVE-2025-23015 [\[CVE json\]](./CVE-2025-23015.cve.json) [\[OSV json\]](./CVE-2025-23015.osv.json)



_Last updated: 2025-02-11T15:47:20.883Z_

### Affected

* Apache Cassandra from 3.0.0 through 3.0.30
* Apache Cassandra from 3.1.0 through 3.11.17
* Apache Cassandra from 4.0.0 through 4.0.16
* Apache Cassandra from 4.1.0 through 4.1.7
* Apache Cassandra from 5.0.0 through 5.0.2


### Description

Privilege Defined With Unsafe Actions vulnerability in Apache Cassandra. An user with MODIFY permission ON ALL KEYSPACES can escalate privileges to superuser within a targeted Cassandra cluster via unsafe actions to a system resource. Operators granting data MODIFY permission on all keyspaces on affected versions should review data access rules for potential breaches.<br><br>This issue affects Apache Cassandra through 3.0.30, 3.11.17, 4.0.16, 4.1.7, 5.0.2.<br><br>Users are recommended to upgrade to versions 3.0.32, 3.11.19, 4.0.17, 4.1.8, 5.0.3, which fixes the issue.<br><br>Addendum:<br><br>



<span style="background-color: rgb(255, 255, 255);">A performance regression was detected in the security releases 3.0.30 [1] and 3.11.18 [2]. Affected users are recommended to upgrade to versions 3.0.32 and 3.11.19 instead.<br><br>The fix to this vulnerability was incorrectly applied to 4.0.16, and affected users in the 4.0 series are recommended to upgrade to 4.0.17 (see CVE-2025-26467 for more information).</span><br><br><span style="background-color: rgb(255, 255, 255);">Remaining versions are unaffected.</span><br><br><span style="background-color: rgb(255, 255, 255);">[1] - <a target="_blank" rel="nofollow" href="https://lists.apache.org/thread/yprngr9cmp9c43m1c56thv1v0v6y5ywq">https://lists.apache.org/thread/yprngr9cmp9c43m1c56thv1v0v6y5ywq</a></span><br><span style="background-color: rgb(255, 255, 255);">[2] - <a target="_blank" rel="nofollow" href="https://lists.apache.org/thread/hc9shwlm1kmxdxosbh3qo2xooqoo3sc6">https://lists.apache.org/thread/hc9shwlm1kmxdxosbh3qo2xooqoo3sc6</a></span>

<br>

### References
* https://lists.apache.org/thread/jmks4msbgkl65ssg69x728sv1m0hwz3s


### Credits
* Adam Pond of Apple Services Engineering Security (finder)
* Ali Mirheidari of Apple Services Engineering Security (finder)
* Terry Thibault of Apple Services Engineering Security (finder)
* Will Brattain of Apple Services Engineering Security (finder)


## unrestricted deserialization of JMX authentication credentials ## { #CVE-2024-27137 }

CVE-2024-27137 [\[CVE json\]](./CVE-2024-27137.cve.json) [\[OSV json\]](./CVE-2024-27137.osv.json)



_Last updated: 2025-02-04T10:19:42.511Z_

### Affected

* Apache Cassandra from 4.0.2 before 4.0.15
* Apache Cassandra from 4.1.0 before 4.1.8
* Apache Cassandra from 5.0-beta1 before 5.0.3


### Description

<p>In Apache Cassandra it is possible for a local attacker without access
 to the Apache Cassandra process or configuration files to manipulate 
the RMI registry to perform a man-in-the-middle attack and capture user 
names and passwords used to access the JMX interface. The attacker can 
then use these credentials to access the JMX interface and perform 
unauthorized operations.<br></p><p>This is same vulnerability that CVE-2020-13946 was issued for, but the Java option was changed in JDK10.<br></p><p>This issue affects Apache Cassandra from 4.0.2 through 5.0.2 running Java 11.<br></p><p>Operators are recommended to upgrade to a release equal to or later than 4.0.15, 4.1.8, or 5.0.3 which fixes the issue.<br></p>

### References
* https://lists.apache.org/thread/jsk87d9yv8r204mgqpz1qxtp5wcrpysm


## Privilege escalation when enabling FQL/Audit logs ## { #CVE-2023-30601 }

CVE-2023-30601 [\[CVE json\]](./CVE-2023-30601.cve.json) [\[OSV json\]](./CVE-2023-30601.osv.json)



_Last updated: 2023-05-30T07:25:46.970Z_

### Affected

* Apache Cassandra from 4.0.0 through 4.0.9
* Apache Cassandra from 4.1.0 through 4.1.1


### Description

Privilege escalation when enabling FQL/Audit logs allows user with JMX access to run arbitrary commands as the user running Apache Cassandra<br><p>This issue affects Apache Cassandra: from 4.0.0 through 4.0.9, from 4.1.0 through 4.1.1.</p>WORKAROUND<br>The vulnerability requires nodetool/JMX access to be exploitable, disable access for any non-trusted users.<br><br>MITIGATION<br>Upgrade to 4.0.10 or 4.1.2 and leave the new FQL/Auditlog configuration property&nbsp;allow_nodetool_archive_command as false.

### References
* https://lists.apache.org/thread/f74p9jdhmmp7vtrqd8lgm8bq3dhxl8vn


### Credits
* Gal Elbaz at Oligo (finder)


## Remote code execution for scripted UDFs ## { #CVE-2021-44521 }

CVE-2021-44521 [\[CVE json\]](./CVE-2021-44521.cve.json) [\[OSV json\]](./CVE-2021-44521.osv.json)



_Last updated: 2022-02-11T12:02:55.157Z_

### Affected

* Apache Cassandra from 3.0.0 before *


### Description

When running Apache Cassandra with the following configuration:

enable_user_defined_functions: true
enable_scripted_user_defined_functions: true
enable_user_defined_functions_threads: false 

it is possible for an attacker to execute arbitrary code on the host. The attacker would need to have enough permissions to create user defined functions in the cluster to be able to exploit this. Note that this configuration is documented as unsafe, and will continue to be considered unsafe after this CVE.

### References
* https://lists.apache.org/thread/y4nb9s4co34j8hdfmrshyl09lokm7356


### Credits
* This issue was discovered by Omer Kaspi of the JFrog Security vulnerability research team.
