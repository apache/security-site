---
title: Apache ActiveMQ security advisories
description: Security information for Apache ActiveMQ
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ActiveMQ? You can read more about the projects' security policy on their [security page](https://activemq.apache.org/security-advisories), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://activemq.apache.org/security-advisories). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

##  ## { #CVE-2020-13947 }

CVE-2020-13947 [\[CVE json\]](./CVE-2020-13947.cve.json)

_Last updated: 2021-02-10T09:16:00.641Z_

### Affected

* Apache ActiveMQ from Apache ActiveMQ before 5.15.13


### Description

An instance of a cross-site scripting vulnerability was identified to be present in the web based administration console on the message.jsp page of Apache ActiveMQ versions 5.15.12 through 5.16.0.

### References
* http://activemq.apache.org/security-advisories.data/CVE-2020-13947-announcement.txt


## ActiveMQ: LDAP-Authentication does not verify passwords on servers with anonymous bind ## { #CVE-2021-26117 }

CVE-2021-26117 [\[CVE json\]](./CVE-2021-26117.cve.json)

_Last updated: 2021-01-27T18:47:20.605Z_

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

_Last updated: 2021-01-27T18:47:25.710Z_

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

_Last updated: 2022-02-04T08:26:48.236Z_

### Affected

* Apache ActiveMQ Artemis from 2.19.0 before 2.20.0


### Description

In Apache ActiveMQ Artemis prior to 2.20.0 or 2.19.1, an attacker could partially disrupt availability (DoS) through uncontrolled resource consumption of memory.

### References
* https://lists.apache.org/thread/fjynj57rd99s814rdn5hzvmx8lz403q2


## HTML Injection in ActiveMQ Artemis Web Console ## { #CVE-2022-35278 }

CVE-2022-35278 [\[CVE json\]](./CVE-2022-35278.cve.json)

_Last updated: 2022-08-18T07:52:49.472Z_

### Affected

* Apache ActiveMQ Artemis from unspecified through 2.23.1


### Description

In Apache ActiveMQ Artemis prior to 2.24.0, an attacker could show malicious content and/or redirect users to a malicious URL in the web console by using HTML in the name of an address or queue.

### References
* https://lists.apache.org/thread/bh6y81wtotg75337bpvxcjy436zfgf3n


### Credits
* Apache ActiveMQ would like to thank Yash Pandya (Digital14), Rajatkumar Karmarkar (Digital14), and Likhith Cheekatipalle (Digital14) for reporting this issue.


## Deserialization vulnerability on Jolokia that allows authenticated users to perform RCE ## { #CVE-2022-41678 }

CVE-2022-41678 [\[CVE json\]](./CVE-2022-41678.cve.json)

_Last updated: 2023-11-28T15:08:35.668Z_

### Affected

* Apache ActiveMQ before 5.16.6
* Apache ActiveMQ from 5.17.0 before 5.17.4
* Apache ActiveMQ at 5.18.0
* Apache ActiveMQ at 6.0.0


### Description

<span style="background-color: rgb(255, 255, 255);">Once an user is authenticated on Jolokia, he can potentially trigger arbitrary code execution.&nbsp;<br><br>In details, in ActiveMQ configurations, jetty allows
org.jolokia.http.AgentServlet to handler request to /api/jolokia<br><br>org.jolokia.http.HttpRequestHandler#handlePostRequest is able to
create JmxRequest through JSONObject. And calls to
org.jolokia.http.HttpRequestHandler#executeRequest.<br><br>Into deeper calling stacks,
org.jolokia.handler.ExecHandler#doHandleRequest is able to invoke
through refection.

And then, RCE is able to be achieved via
jdk.management.jfr.FlightRecorderMXBeanImpl which exists on Java version above 11.
<br><br>
1 Call newRecording.
<br>
2 Call setConfiguration. And a webshell data hides in it.
<br>
3 Call startRecording.
<br>
4 Call copyTo method. The webshell will be written to a .jsp file.<br><br></span>The mitigation is to restrict (by default) the actions authorized on Jolokia, or disable Jolokia.<br>A more restrictive Jolokia configuration has been defined in default ActiveMQ distribution. We encourage users to upgrade to ActiveMQ distributions version including updated Jolokia configuration: 5.16.6, 5.17.4, 5.18.0, 6.0.0.<br>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2022-41678-announcement.txt
* https://lists.apache.org/thread/7g17kwbtjl011mm4tr8bn1vnoq9wh4sl


### Credits
* wangxin@threatbook.cn (finder)
* wangzhendong@threatbook.cn (finder)
* honglonglong@threatbook.cn (finder)


## Unbounded deserialization causes ActiveMQ to be vulnerable to a remote code execution (RCE) attack ## { #CVE-2023-46604 }

CVE-2023-46604 [\[CVE json\]](./CVE-2023-46604.cve.json)

_Last updated: 2023-11-28T15:02:26.708Z_

### Affected

* Apache ActiveMQ from 5.18.0 before 5.18.3
* Apache ActiveMQ from 5.17.0 before 5.17.6
* Apache ActiveMQ from 5.16.0 before 5.16.7
* Apache ActiveMQ before 5.15.16
* Apache ActiveMQ Legacy OpenWire Module from 5.18.0 before 5.18.3
* Apache ActiveMQ Legacy OpenWire Module from 5.17.0 before 5.17.6
* Apache ActiveMQ Legacy OpenWire Module from 5.16.0 before 5.16.7
* Apache ActiveMQ Legacy OpenWire Module from 5.8.0 before 5.15.16


### Description

<div>The Java OpenWire protocol marshaller is vulnerable to Remote Code 
Execution. This vulnerability may allow a remote attacker with network 
access to either a Java-based OpenWire broker or client to run arbitrary
 shell commands by manipulating serialized class types in the OpenWire 
protocol to cause either the client or the broker (respectively) to 
instantiate any class on the classpath.</div><div><br></div><div>Users are recommended to upgrade
 both brokers and clients to version 5.15.16, 5.16.7, 5.17.6, or 5.18.3 
which fixes this issue.</div>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2023-46604-announcement.txt
* https://www.openwall.com/lists/oss-security/2023/10/27/5
* https://security.netapp.com/advisory/ntap-20231110-0010/
* https://packetstormsecurity.com/files/175676/Apache-ActiveMQ-Unauthenticated-Remote-Code-Execution.html
* https://lists.debian.org/debian-lts-announce/2023/11/msg00013.html


### Credits
* yejie@threatbook.cn (finder)
