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

CVE-2020-13947 [\[CVE json\]](./CVE-2020-13947.cve.json) [\[OSV json\]](./CVE-2020-13947.osv.json)



_Last updated: 2021-02-10T09:16:00.641Z_

### Affected

* Apache ActiveMQ from Apache ActiveMQ before 5.15.13


### Description

An instance of a cross-site scripting vulnerability was identified to be present in the web based administration console on the message.jsp page of Apache ActiveMQ versions 5.15.12 through 5.16.0.

### References
* http://activemq.apache.org/security-advisories.data/CVE-2020-13947-announcement.txt


## ActiveMQ: LDAP-Authentication does not verify passwords on servers with anonymous bind ## { #CVE-2021-26117 }

CVE-2021-26117 [\[CVE json\]](./CVE-2021-26117.cve.json) [\[OSV json\]](./CVE-2021-26117.osv.json)



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

CVE-2021-26118 [\[CVE json\]](./CVE-2021-26118.cve.json) [\[OSV json\]](./CVE-2021-26118.osv.json)



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

CVE-2022-23913 [\[CVE json\]](./CVE-2022-23913.cve.json) [\[OSV json\]](./CVE-2022-23913.osv.json)



_Last updated: 2022-02-04T08:26:48.236Z_

### Affected

* Apache ActiveMQ Artemis from 2.19.0 before 2.20.0


### Description

In Apache ActiveMQ Artemis prior to 2.20.0 or 2.19.1, an attacker could partially disrupt availability (DoS) through uncontrolled resource consumption of memory.

### References
* https://lists.apache.org/thread/fjynj57rd99s814rdn5hzvmx8lz403q2


## HTML Injection in ActiveMQ Artemis Web Console ## { #CVE-2022-35278 }

CVE-2022-35278 [\[CVE json\]](./CVE-2022-35278.cve.json) [\[OSV json\]](./CVE-2022-35278.osv.json)



_Last updated: 2022-08-18T07:52:49.472Z_

### Affected

* Apache ActiveMQ Artemis from unspecified through 2.23.1


### Description

In Apache ActiveMQ Artemis prior to 2.24.0, an attacker could show malicious content and/or redirect users to a malicious URL in the web console by using HTML in the name of an address or queue.

### References
* https://lists.apache.org/thread/bh6y81wtotg75337bpvxcjy436zfgf3n


### Credits
* Apache ActiveMQ would like to thank Yash Pandya (Digital14), Rajatkumar Karmarkar (Digital14), and Likhith Cheekatipalle (Digital14) for reporting this issue.


## Insufficient API restrictions on Jolokia allow authenticated users to perform RCE ## { #CVE-2022-41678 }

CVE-2022-41678 [\[CVE json\]](./CVE-2022-41678.cve.json)

_Last updated: 2024-05-31T08:42:39.786Z_

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


## Authenticated users could perform RCE via Jolokia MBeans ## { #CVE-2023-50780 }

CVE-2023-50780 [\[CVE json\]](./CVE-2023-50780.cve.json) [\[OSV json\]](./CVE-2023-50780.osv.json)



_Last updated: 2024-10-14T16:03:33.323Z_

### Affected

* Apache ActiveMQ Artemis before 2.29.0


### Description

<p>Apache ActiveMQ Artemis allows access to diagnostic information and controls through MBeans, which are also exposed through the authenticated Jolokia endpoint. Before version 2.29.0, this also included the Log4J2 MBean. This MBean is not meant for exposure to non-administrative users. This could eventually allow an authenticated attacker to write arbitrary files to the filesystem and indirectly achieve RCE.<br></p><p>Users are recommended to upgrade to version 2.29.0 or later, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/63b78shqz312phsx7v1ryr7jv7bprg58


### Credits
* Matei "Mal" Badanoiu (finder)


## Jolokia and REST API were not secured with default configuration ## { #CVE-2024-32114 }

CVE-2024-32114 [\[CVE json\]](./CVE-2024-32114.cve.json) [\[OSV json\]](./CVE-2024-32114.osv.json)



_Last updated: 2024-05-01T16:07:22.140Z_

### Affected

* Apache ActiveMQ from 6.0.0 through 6.1.1


### Description

In Apache ActiveMQ 6.x, the default configuration doesn't secure the API web context (where the Jolokia JMX REST API and the Message REST API are located).<br>It means that anyone can use these layers without any required authentication. Potentially, anyone can interact with the broker (using Jolokia JMX REST API) and/or produce/consume messages or purge/delete destinations (using the Message REST API).<br><br>To mitigate, users can update the default conf/jetty.xml configuration file to add authentication requirement:<br><blockquote><pre>&lt;bean id="securityConstraintMapping" class="org.eclipse.jetty.security.ConstraintMapping"&gt;
&nbsp; &lt;property name="constraint" ref="securityConstraint" /&gt;
&nbsp; &lt;property name="pathSpec" value="/" /&gt;
&lt;/bean&gt;</pre></blockquote>Or we encourage users to upgrade to Apache ActiveMQ 6.1.2 where the default configuration has been updated with authentication by default.<br>

### References
* https://activemq.apache.org/security-advisories.data/CVE-2024-32114-announcement.txt


### Credits
* Martin Zeissig (finder)


## Passwords leaking from broker properties in the debug log ## { #CVE-2025-27391 }

CVE-2025-27391 [\[CVE json\]](./CVE-2025-27391.cve.json) [\[OSV json\]](./CVE-2025-27391.osv.json)



_Last updated: 2025-04-09T14:42:30.509Z_

### Affected

* Apache ActiveMQ Artemis from 1.5.1 before 2.40.0


### Description

<p>Insertion of Sensitive Information into Log File vulnerability in Apache ActiveMQ Artemis. All the values of the broker properties are&nbsp;logged when the org.apache.activemq.artemis.core.config.impl.ConfigurationImpl <span style="background-color: rgb(255, 255, 255);">logger has the&nbsp;</span>debug level enabled.</p><p>This issue affects Apache ActiveMQ Artemis: from 1.5.1 before 2.40.0. It can be mitigated by restricting log access to only trusted users.</p><p>Users are recommended to upgrade to version 2.40.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/25p96cvzl1mkt29lwm2d8knklkoqolps


### Credits
* Rafael Yanez Illescas <ryanezil@redhat.com> (finder)


## Address routing-type can be updated by user without the createAddress permission ## { #CVE-2025-27427 }

CVE-2025-27427 [\[CVE json\]](./CVE-2025-27427.cve.json) [\[OSV json\]](./CVE-2025-27427.osv.json)



_Last updated: 2025-04-01T07:26:53.803Z_

### Affected

* Apache ActiveMQ Artemis from 2.0.0 through 2.39.0


### Description

<p>A vulnerability exists in Apache ActiveMQ Artemis whereby a user with the createDurableQueue or createNonDurableQueue permission on an address can augment the routing-type supported by that address even if said user doesn't have the createAddress permission for that particular address. When combined with the send permission and automatic queue creation a user could successfully send a message with a routing-type not supported by the address when that message should actually be rejected on the basis that the user doesn't have permission to change the routing-type of the address.</p><p>This issue affects Apache ActiveMQ Artemis from 2.0.0 through 2.39.0.</p><p>Users are recommended to upgrade to version 2.40.0 which fixes the issue.</p>

### References
* https://lists.apache.org/thread/8dzlm2vkqphyrnkrby8r8kzndsm5o6x8


### Credits
* Eojin Lee <djwls7179@gmail.com> (reporter)
* Dain Lee <ledain5094@gmail.com> (finder)
* WooJin Park <1203kids@gmail.com> (finder)
* MinJung Lee <whitney2319@gmail.com> (finder)
* SeChang Oh <osc010524@gmail.com> (finder)


## Unchecked buffer length can cause excessive memory allocation ## { #CVE-2025-27533 }

CVE-2025-27533 [\[CVE json\]](./CVE-2025-27533.cve.json) [\[OSV json\]](./CVE-2025-27533.osv.json)



_Last updated: 2025-05-07T08:58:58.430Z_

### Affected

* Apache ActiveMQ from 6.0.0 before 6.1.6
* Apache ActiveMQ from 5.18.0 before 5.18.7
* Apache ActiveMQ from 5.17.0 before 5.17.7
* Apache ActiveMQ from 5.16.0 before 5.16.8


### Description

<p>Memory Allocation with Excessive Size Value vulnerability in Apache ActiveMQ.</p><span style="background-color: rgb(255, 255, 255);">During unmarshalling of OpenWire commands the size value of buffers was not properly validated which could lead to excessive memory allocation and be exploited to cause a denial of service (DoS) by depleting process memory, thereby affecting applications and services that rely on the availability of the ActiveMQ broker when not using mutual TLS connections.</span><br><p>This issue affects Apache ActiveMQ: from 6.0.0 before 6.1.6, from 5.18.0 before 5.18.7, from 5.17.0 before 5.17.7, before 5.16.8. ActiveMQ 5.19.0 is not affected.</p><p>Users are recommended to upgrade to version 6.1.6+, 5.19.0+,  5.18.7+, 5.17.7, or 5.16.8 or which fixes the issue.</p><p>Existing users may implement mutual TLS to mitigate the risk on affected brokers.</p>

### References
* https://lists.apache.org/thread/8hcm25vf7mchg4zbbhnlx2lc5bs705hg


## deserialization allowlist bypass ## { #CVE-2025-29953 }

CVE-2025-29953 [\[CVE json\]](./CVE-2025-29953.cve.json) [\[OSV json\]](./CVE-2025-29953.osv.json)



_Last updated: 2025-04-18T15:23:28.244Z_

### Affected

* Apache ActiveMQ NMS OpenWire Client before 2.1.1


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache ActiveMQ NMS OpenWire Client.</p><p>This issue affects Apache ActiveMQ NMS OpenWire Client before 2.1.1 when performing connections to untrusted servers. Such servers could abuse the unbounded deserialization in the client to provide malicious responses that may eventually cause arbitrary code execution on the client. Version 2.1.0 introduced a allow/denylist feature to restrict deserialization, but this feature could be bypassed.</p><p>The .NET team has deprecated the built-in .NET binary serialization feature starting with .NET 9 and suggests migrating away from binary serialization. The project is considering to follow suit and drop this part of the NMS API altogether.</p><p>Users are recommended to upgrade to version 2.1.1, which fixes the issue. We also recommend to migrate away from relying on .NET binary serialization as a hardening method for the future.</p>

### References
* https://lists.apache.org/thread/vc1sj9y3056d3kkhcvrs9fyw5w8kpmlx


### Credits
* g7shot working with Trend Zero Day Initiative (finder)


## Deserialization of Untrusted Data ## { #CVE-2025-54539 }

CVE-2025-54539 [\[CVE json\]](./CVE-2025-54539.cve.json) [\[OSV json\]](./CVE-2025-54539.osv.json)



_Last updated: 2025-10-16T08:26:04.874Z_

### Affected

* Apache ActiveMQ NMS AMQP Client through 2.3.0


### Description

A Deserialization of Untrusted Data vulnerability exists in the Apache ActiveMQ NMS AMQP Client.<br><br>This issue affects all versions of Apache ActiveMQ NMS AMQP up to and including 2.3.0, when establishing connections to untrusted AMQP servers. Malicious servers could exploit unbounded deserialization logic present in the client to craft responses that may lead to arbitrary code execution on the client side.<br><br>Although version 2.1.0 introduced a mechanism to restrict deserialization via allow/deny lists, the protection was found to be bypassable under certain conditions.<br><br>In line with Microsoft’s deprecation of binary serialization in .NET 9, the project is evaluating the removal of .NET binary serialization support from the NMS API entirely in future releases.<br><br>Mitigation and Recommendations:<br>Users are strongly encouraged to upgrade to version 2.4.0 or later, which resolves the issue. Additionally, projects depending on NMS-AMQP should migrate away from .NET binary serialization as part of a long-term hardening strategy.

### References
* https://lists.apache.org/thread/9k684j07ljrshy3hxwhj5m0xjmkz1g2n


### Credits
* Security Research Team @ Endor Labs (finder)
