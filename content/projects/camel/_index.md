---
title: Apache Camel security advisories
description: Security information for Apache Camel
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Camel? You can read more about the projects' security policy on their [security page](https://camel.apache.org/security/), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://camel.apache.org/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Temporary file information disclosure in Camel-Jira ## { #CVE-2023-34442 }

CVE-2023-34442 [\[CVE json\]](./CVE-2023-34442.cve.json) [\[OSV json\]](./CVE-2023-34442.osv.json)



_Last updated: 2023-07-10T09:31:01.757Z_

### Affected

* Apache Camel JIRA from 3.x through <=3.14.8
* Apache Camel JIRA from 3.18.x through <=3.18.7
* Apache Camel JIRA from 3.20.x through <= 3.20.5
* Apache Camel JIRA from 4.x through <= 4.0.0-M3


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Camel.<p>This issue affects Apache Camel: from 3.X through &lt;=3.14.8, from 3.18.X through &lt;=3.18.7, from 3.20.X through &lt;= 3.20.5, from 4.X through &lt;= 4.0.0-M3.</p><span style="background-color: rgb(255, 255, 255);">Users should upgrade to 3.14.9, 3.18.8, 3.20.6 or 3.21.0 and for users on Camel 4.x update to 4.0.0-M1</span><br>

### References
* https://lists.apache.org/thread/x4vy2hhbltb1xrvy1g6m8hpjgj2k7wgh


### Credits
* Jonathan Leitschuh of the Open Source Security Foundation: Project Alpha-Omega (reporter)


## Camel-SQL: Unsafe Deserialization from JDBCAggregationRepository ## { #CVE-2024-22369 }

CVE-2024-22369 [\[CVE json\]](./CVE-2024-22369.cve.json) [\[OSV json\]](./CVE-2024-22369.osv.json)



_Last updated: 2024-02-20T15:01:05.582Z_

### Affected

* Apache Camel from 3.0.0 before 3.21.4
* Apache Camel from 3.22.0 before 3.22.1
* Apache Camel from 4.0.0 before 4.0.4
* Apache Camel from 4.1.0 before 4.4.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Camel SQL Component<p>This issue affects Apache Camel: from 3.0.0 before 3.21.4, from 3.22.0 before 3.22.1, from 4.0.0 before 4.0.4, from 4.1.0 before 4.4.0.</p><p>Users are recommended to upgrade to version 4.4.0, which fixes the issue. If users are on the 4.0.x LTS releases stream, then they are suggested to upgrade to 4.0.4. If users are on 3.x, they are suggested to move to 3.21.4 or 3.22.1</p>

### References
* https://lists.apache.org/thread/3dko781dy2gy5l3fs48p56fgp429yb0f
* https://camel.apache.org/security/CVE-2024-22369.html


### Credits
* Ziyang Chen from HuaWei Open Source Management Center (finder)
* Pingtao Wei from HuaWei Open Source Management Center (finder)
* Haoran Zhi from HuaWei Open Source Management Center (finder)


## Apache Camel issue on ExchangeCreatedEvent ## { #CVE-2024-22371 }

CVE-2024-22371 [\[CVE json\]](./CVE-2024-22371.cve.json)

_Last updated: 2024-02-26T09:22:36.071Z_

### Affected

* Apache Camel from 1.x through 1.6.0
* Apache Camel from 3.21.x through 3.21.3
* Apache Camel from 3.22.x through 3.22.0
* Apache Camel from 4.0.x through 4.0.3
* Apache Camel from 4.x through 4.3.0


### Description

Exposure of sensitive data by by crafting a malicious EventFactory and providing a custom ExchangeCreatedEvent that exposes sensitive data. Vulnerability in Apache Camel.<p>This issue affects Apache Camel: from 3.21.X through 3.21.3, from 3.22.X through 3.22.0, from 4.0.X through 4.0.3, from 4.X through 4.3.0.</p><p>Users are recommended to upgrade to version 3.21.4, 3.22.1, 4.0.4 or 4.4.0, which fixes the issue.</p>

### References
* https://camel.apache.org/security/CVE-2024-22371.html


### Credits
* Otavio Rodolfo Piske from the Apache Software Foundation (finder)


## Camel-CassandraQL: Unsafe Deserialization from CassandraAggregationRepository ## { #CVE-2024-23114 }

CVE-2024-23114 [\[CVE json\]](./CVE-2024-23114.cve.json) [\[OSV json\]](./CVE-2024-23114.osv.json)



_Last updated: 2024-02-20T14:59:36.356Z_

### Affected

* Apache Camel from 3.0.0 before 3.21.4
* Apache Camel from 3.22.0 before 3.22.1
* Apache Camel from 4.0.0 before 4.0.4
* Apache Camel from 4.1.0 before 4.4.0


### Description

Deserialization of Untrusted Data vulnerability in Apache Camel CassandraQL Component AggregationRepository which is vulnerable to unsafe deserialization. Under specific conditions it is possible to deserialize malicious payload.<p>This issue affects Apache Camel: from 3.0.0 before 3.21.4, from 3.22.0 before 3.22.1, from 4.0.0 before 4.0.4, from 4.1.0 before 4.4.0.</p><p>Users are recommended to upgrade to version 4.4.0, which fixes the issue.&nbsp;If users are on the 4.0.x LTS releases stream, then they are suggested to upgrade to 4.0.4. If users are on 3.x, they are suggested to move to 3.21.4 or 3.22.1</p>

### References
* https://camel.apache.org/security/CVE-2024-23114.html


### Credits
* Federico Mariani From Apache Software Foundation (finder)
* Andrea Cosentino from Apache Software Foundation (finder)


## Camel Message Header Injection via Improper Filtering ## { #CVE-2025-27636 }

CVE-2025-27636 [\[CVE json\]](./CVE-2025-27636.cve.json) [\[OSV json\]](./CVE-2025-27636.osv.json)



_Last updated: 2025-03-17T14:20:17.925Z_

### Affected

* Apache Camel from 4.10.0 before 4.10.2
* Apache Camel from 4.8.0 before 4.8.5
* Apache Camel from 3.10.0 before 3.22.4


### Description

<p>Bypass/Injection vulnerability in Apache Camel components under particular conditions.</p><p>This issue affects Apache Camel: from 4.10.0 through &lt;= 4.10.1, from 4.8.0 through &lt;= 4.8.4, from 3.10.0 through &lt;= 3.22.3.</p><p>Users are recommended to upgrade to version 4.10.2 for 4.10.x LTS, 4.8.5 for 4.8.x LTS and 3.22.4 for 3.x releases.</p><div></div><div>This vulnerability is present in Camel's default incoming header filter, that allows an attacker to include Camel specific</div><div>headers that for some Camel components can alter the behaviours such as the camel-bean component, to call another method</div><div>on the bean, than was coded in the application. In the camel-jms component, then a malicious header can be used to send</div><div>the message to another queue (on the same broker) than was coded in the application. This could also be seen by using the camel-exec component</div><div><br></div><div>The attacker would need to inject custom headers, such as HTTP protocols. So if you have Camel applications that are</div><div>directly connected to the internet via HTTP, then an attacker could include malicious HTTP headers in the HTTP requests</div><div>that are send to the Camel application.</div><div><br></div>All the known Camel HTTP component such as camel-servlet, camel-jetty, camel-undertow, camel-platform-http, and camel-netty-http would be vulnerable out of the box.<br><br>In these conditions an attacker could be able to forge a Camel header name and make the bean component invoking other methods in the same bean.<br><br><div>In terms of usage of the default header filter strategy the list of components using that is: <br></div><div><div><ul><li>camel-activemq</li><li>camel-activemq6</li><li>camel-amqp</li><li>camel-aws2-sqs</li><li>camel-azure-servicebus</li><li>camel-cxf-rest</li><li>camel-cxf-soap</li><li>camel-http</li><li>camel-jetty</li><li>camel-jms</li><li>camel-kafka</li><li>camel-knative</li><li>camel-mail</li><li>camel-nats</li><li>camel-netty-http</li><li>camel-platform-http</li><li>camel-rest</li><li>camel-sjms</li><li>camel-spring-rabbitmq</li><li>camel-stomp</li><li>camel-tahu</li><li>camel-undertow</li><li>camel-xmpp</li></ul></div></div><div>The vulnerability arises due to a bug in the default filtering mechanism that only blocks headers starting with "Camel", "camel", or "org.apache.camel.".&nbsp;</div><br><div><span style="background-color: var(--wht);">Mitigation:&nbsp;</span>You can easily work around this in your Camel applications by removing the&nbsp;headers in your Camel routes. There are many ways of doing this, also&nbsp;globally or per route. This means you could use the removeHeaders EIP, to filter out anything like "cAmel, cAMEL" etc, or in general everything not starting with "Camel", "camel" or "org.apache.camel.".&nbsp;<br></div><br>

### References
* https://lists.apache.org/thread/l3zcg3vts88bmc7w8172wkgw610y693z
* https://issues.apache.org/jira/browse/CAMEL-21828
* https://camel.apache.org/security/CVE-2025-27636.html


### Credits
* Mark Thorson (finder)


## Camel Message Header Injection through request parameters ## { #CVE-2025-29891 }

CVE-2025-29891 [\[CVE json\]](./CVE-2025-29891.cve.json) [\[OSV json\]](./CVE-2025-29891.osv.json)



_Last updated: 2025-03-13T08:19:35.754Z_

### Affected

* Apache Camel from 4.10.0 before 4.10.2
* Apache Camel from 4.8.0 before 4.8.5
* Apache Camel from 3.10.0 before 3.22.4


### Description

<p>Bypass/Injection vulnerability in Apache Camel.</p><p>This issue affects Apache Camel: from 4.10.0 before 4.10.2, from 4.8.0 before 4.8.5, from 3.10.0 before 3.22.4.</p><p>Users are recommended to upgrade to version 4.10.2 for 4.10.x LTS, 4.8.5 for 4.8.x LTS and 3.22.4 for 3.x releases.</p><p>This vulnerability is present in Camel's default incoming header filter, that allows an attacker to include Camel specific headers that for some Camel components can alter the behaviours such as the camel-bean component, or the camel-exec component.</p><p>If you have Camel applications that are directly connected to the internet via HTTP, then an attacker&nbsp;<span style="background-color: rgb(255, 255, 255);">could include parameters in the HTTP requests that are sent to the Camel application that get translated into headers.</span>&nbsp;</p><p>The headers could be both provided as request parameters for an HTTP methods invocation or as part of the payload of the HTTP methods invocation.</p><p><span style="background-color: var(--wht);">All the known Camel HTTP component such as camel-servlet, camel-jetty, camel-undertow, camel-platform-http, and camel-netty-http would be vulnerable out of the box.</span></p><span style="background-color: rgb(255, 255, 255);">This CVE is related to the CVE-2025-27636: while they have the same root cause and are fixed with the same fix, CVE-2025-27636 was assumed to only be exploitable if an attacker could add malicious HTTP headers, while we have now determined that it is also exploitable via HTTP parameters. Like in CVE-2025-27636, exploitation is only possible if the Camel route uses particular vulnerable components.</span><p></p>

### References
* https://camel.apache.org/security/CVE-2025-27636.html
* https://camel.apache.org/security/CVE-2025-29891.html


### Credits
* Citi Cyber Security Operations (finder)
* Akamai Security Intelligence Group (SIG) (reporter)
* Mark Thorson of AT&T (finder)
* Mark Thorson of AT&T (reporter)
