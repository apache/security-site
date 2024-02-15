---
title: Apache Flume security advisories
description: Security information for Apache Flume
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Flume? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Flume vulnerable to a JNDI RCE in JMSSource  ## { #CVE-2022-25167 }

CVE-2022-25167 [\[CVE json\]](./CVE-2022-25167.cve.json)

_Last updated: 2022-06-14T07:51:07.443Z_

### Affected

* Apache Flume from flume-jms-source before 1.10.0


### Description

Apache Flume versions 1.4.0 through 1.9.0 are vulnerable to a remote code execution (RCE) attack when a configuration uses a JMS Source with a JNDI LDAP data source URI when an attacker has control of the target LDAP server. This issue is fixed by limiting JNDI to allow only the use of the java protocol or no protocol. 

### References
* https://lists.apache.org/thread/16nf6b81zjpdc4y93ho99oxo83ddbsvg
* https://issues.apache.org/jira/browse/FLUME-3416


## Improper Input Validation (JNDI Injection) in JMSMessageConsumer ## { #CVE-2022-34916 }

CVE-2022-34916 [\[CVE json\]](./CVE-2022-34916.cve.json)

_Last updated: 2022-08-21T08:11:17.200Z_

### Affected

* Apache Flume from flume-jms-source before 1.11.0


### Description

Apache Flume versions 1.4.0 through 1.10.0 are vulnerable to a remote code execution (RCE) attack when a configuration uses a JMS Source with a JNDI LDAP data source URI when an attacker has control of the target LDAP server. This issue is fixed by limiting JNDI to allow only the use of the java protocol or no protocol. 

### References
* https://issues.apache.org/jira/browse/FLUME-3428
* https://lists.apache.org/thread/qkmt4r2t9tbrxrdbjg1m2oczbvczd9zn


### Credits
* Apache Flume would like to thank Frentzen Amaral for reporting this issue.


## Apache Flume prior to 1.11.0 has an Improper Input Validation (JNDI Injection) in JMSSource ## { #CVE-2022-42468 }

CVE-2022-42468 [\[CVE json\]](./CVE-2022-42468.cve.json)

_Last updated: 2022-10-26T13:08:08.448Z_

### Affected

* Apache Flume from Flume JMSSource before 1.11.0


### Description

Apache Flume versions 1.4.0 through 1.10.1 are vulnerable to a remote code execution (RCE) attack when a configuration uses a JMS Source with an unsafe providerURL. This issue is fixed by limiting JNDI to allow only the use of the java protocol or no protocol. 

### References
* https://issues.apache.org/jira/browse/FLUME-3437
* https://lists.apache.org/thread/939wkx8o90bp6m2ht3t1sdyo1ncypl78
* https://lists.apache.org/thread/1ckhmp539zr2nd2rs45pocpywk2d9zvz
