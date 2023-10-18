---
title: Apache ActiveMQ security advisories
description: Security information for Apache ActiveMQ
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ActiveMQ? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

##  ## { #CVE-2020-13947 }

CVE-2020-13947 [\[CVE json\]](./CVE-2020-13947.cve.json)

### Affected

* Apache ActiveMQ from Apache ActiveMQ before 5.15.13


### Description

An instance of a cross-site scripting vulnerability was identified to be present in the web based administration console on the message.jsp page of Apache ActiveMQ versions 5.15.12 through 5.16.0.

### References
* http://activemq.apache.org/security-advisories.data/CVE-2020-13947-announcement.txt


## ActiveMQ: LDAP-Authentication does not verify passwords on servers with anonymous bind ## { #CVE-2021-26117 }

CVE-2021-26117 [\[CVE json\]](./CVE-2021-26117.cve.json)

### Affected

* Apache ActiveMQ from Apache ActiveMQ Artemis before 2.16.0
* Apache ActiveMQ from Apache ActiveMQ before 5.16.1


### Description

The optional ActiveMQ LDAP login module can be configured to use anonymous access to the LDAP server. In this case, for Apache ActiveMQ Artemis prior to version 2.16.0 and Apache ActiveMQ prior to versions 5.16.1 and 5.15.14, the anonymous context is used to verify a valid users password in error, resulting in no check on the password.

### References
* https://mail-archives.apache.org/mod_mbox/activemq-users/202101.mbox/%3cCAH+vQmMeUEiKN4wYX9nLBbqmFZFPXqajNvBKmzb2V8QZANcSTA%40mail.gmail.com%3e


### Credits
* Apache ActiveMQ would like to thank Gregor Tudan <gregor.tudan@cofinpro.de> for reporting this issue.


## Flaw in ActiveMQ Artemis OpenWire support ## { #CVE-2021-26118 }

CVE-2021-26118 [\[CVE json\]](./CVE-2021-26118.cve.json)

### Affected

* Apache ActiveMQ Artemis from unspecified before 2.16.0


### Description

While investigating ARTEMIS-2964 it was found that the creation of advisory messages in the OpenWire protocol head of Apache ActiveMQ Artemis 2.15.0 bypassed policy based access control for the entire session. Production of advisory messages was not subject to access control in error.

### References
* https://mail-archives.apache.org/mod_mbox/activemq-users/202101.mbox/%3CCAH%2BvQmMUNnkiXv2-d3ucdErWOsdnLi6CgnK%2BVfixyJvTgTuYig%40mail.gmail.com%3E


### Credits
* Apache ActiveMQ  would like to thank Francesco Marchioni (Red Hat) for reporting this issue.


## Apache ActiveMQ Artemis DoS ## { #CVE-2022-23913 }

CVE-2022-23913 [\[CVE json\]](./CVE-2022-23913.cve.json)

### Affected

* Apache ActiveMQ Artemis from 2.19.0 before 2.20.0


### Description

In Apache ActiveMQ Artemis prior to 2.20.0 or 2.19.1, an attacker could partially disrupt availability (DoS) through uncontrolled resource consumption of memory.

### References
* https://lists.apache.org/thread/fjynj57rd99s814rdn5hzvmx8lz403q2


## HTML Injection in ActiveMQ Artemis Web Console ## { #CVE-2022-35278 }

CVE-2022-35278 [\[CVE json\]](./CVE-2022-35278.cve.json)

### Affected

* Apache ActiveMQ Artemis from unspecified through 2.23.1


### Description

In Apache ActiveMQ Artemis prior to 2.24.0, an attacker could show malicious content and/or redirect users to a malicious URL in the web console by using HTML in the name of an address or queue.

### References
* https://lists.apache.org/thread/bh6y81wtotg75337bpvxcjy436zfgf3n


### Credits
* Apache ActiveMQ would like to thank Yash Pandya (Digital14), Rajatkumar Karmarkar (Digital14), and Likhith Cheekatipalle (Digital14) for reporting this issue.
