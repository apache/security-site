---
title: Apache Jackrabbit security advisories
description: Security information for Apache Jackrabbit
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Jackrabbit? You can read more about the projects' security policy on their [security page](https://jackrabbit.apache.org/jcr/security-reports.html), and email your report to the [Apache Jackrabbit Security Team](mailto:security@jackrabbit.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://jackrabbit.apache.org/jcr/security-reports.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## XXE vulnerability in jackrabbit-spi-commons ## { #CVE-2025-53689 }

CVE-2025-53689 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-53689) [\[CVE json\]](./CVE-2025-53689.cve.json) [\[OSV json\]](./CVE-2025-53689.osv.json)



_Last updated: 2025-07-14T09:15:35.583Z_

### Affected

* Apache Jackrabbit from 2.20.0 before 2.20.17
* Apache Jackrabbit from 2.22.0 before 2.22.1
* Apache Jackrabbit from 2.23.0-beta before 2.23.2-beta


### Description

Blind XXE Vulnerabilities in jackrabbit-spi-commons and jackrabbit-core in Apache Jackrabbit &lt; 2.23.2 due to usage of an unsecured document build to load privileges.<br><br>Users are recommended to upgrade to versions 2.20.17 (Java 8), 2.22.1 (Java 11) or 2.23.2 (Java 11, beta versions), which fix this issue. Earlier versions (up to 2.20.16) are not supported anymore, thus users should update to the respective supported version.

### References
* https://lists.apache.org/thread/5pf9n76ny13pzzk765og2h3gxdxw7p24


### Credits
* Lars Krapf - Adobe (reporter)
* Dylan Pindur - Assetnote (finder)
* Adam Kues - Assetnote (finder)


## Apache Jackrabbit RMI access can lead to RCE ## { #CVE-2023-37895 }

CVE-2023-37895 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-37895) [\[CVE json\]](./CVE-2023-37895.cve.json)

_Last updated: 2023-07-25T14:02:07.695Z_

### Affected

* Apache Jackrabbit Webapp (jackrabbit-webapp) from 2.21.0 before 2.21.18
* Apache Jackrabbit Webapp (jackrabbit-webapp) from 1.0.0 before 2.20.11
* Apache Jackrabbit Standalone (jackrabbit-standalone and jackrabbit-standalone-components) from 2.21.0 before 2.21.18
* Apache Jackrabbit Standalone (jackrabbit-standalone and jackrabbit-standalone-components) from 1.0.0 before 2.20.11


### Description

<h1>Java object deserialization issue in Jackrabbit webapp/standalone on all platforms allows attacker to remotely execute code via RMI</h1><div>Versions up to (including) 2.20.10 (stable branch) and 2.21.17 (unstable branch) use the component "commons-beanutils", which contains a class that can be used for remote code execution over RMI.</div><div><br></div><div>Users are advised to immediately update to versions 2.20.11 or 2.21.18. Note that earlier stable branches (1.0.x .. 2.18.x) have been EOLd already and do not receive updates anymore.<br><br>In general, RMI support can expose vulnerabilities by the mere presence of an exploitable class on the classpath. Even if Jackrabbit itself does not contain any code known to be exploitable anymore, adding other components to your server can expose the same type of problem. We therefore recommend to disable RMI access altogether (see further below), and will discuss deprecating RMI support in future Jackrabbit releases.<br></div><h2>How to check whether RMI support is enabled</h2><div>RMI support can be over an RMI-specific TCP port, and over an HTTP binding. Both are by default enabled in Jackrabbit webapp/standalone.<br></div><div><br></div><div>The native RMI protocol by default uses port 1099. To check whether it is enabled, tools like "netstat" can be used to check.</div><div><br></div><div>RMI-over-HTTP in Jackrabbit by default uses the path "/rmi". So when running standalone on port 8080, check whether an HTTP GET request on localhost:8080/rmi returns 404 (not enabled) or 200 (enabled). Note that the HTTP path may be different when the webapp is deployed in a container as non-root context, in which case the prefix is under the user's control.<br></div><div><br></div><h2>Turning off RMI</h2><div>Find web.xml (either in JAR/WAR file or in unpacked web application folder), and remove the declaration and the mapping definition for the RemoteBindingServlet:</div><div><br></div><div>&nbsp; &nbsp; &nbsp; &nbsp; &lt;servlet&gt;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;servlet-name&gt;RMI&lt;/servlet-name&gt;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;servlet-class&gt;org.apache.jackrabbit.servlet.remote.RemoteBindingServlet&lt;/servlet-class&gt;<br>&nbsp; &nbsp; &nbsp; &nbsp; &lt;/servlet&gt;</div><div><br>&nbsp; &nbsp; &nbsp; &nbsp; &lt;servlet-mapping&gt;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;servlet-name&gt;RMI&lt;/servlet-name&gt;<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;url-pattern&gt;/rmi&lt;/url-pattern&gt;<br>&nbsp; &nbsp; &nbsp; &nbsp; &lt;/servlet-mapping&gt;</div><div><br></div><div>Find the bootstrap.properties file (in $REPOSITORY_HOME), and set<br></div><div><br></div><div>&nbsp; &nbsp; &nbsp; &nbsp;  rmi.enabled=false<br><br>&nbsp; &nbsp; and also remove<br><br>&nbsp; &nbsp; &nbsp; &nbsp;  rmi.host<br>&nbsp; &nbsp; &nbsp; &nbsp;  rmi.port<br>&nbsp; &nbsp; &nbsp; &nbsp;  rmi.url-pattern<br><br>&nbsp;If there is no file named bootstrap.properties in $REPOSITORY_HOME, it is located somewhere in the classpath. In this case, place a copy in $REPOSITORY_HOME and modify it as explained.<br><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div>&nbsp;<br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div>

### References
* https://lists.apache.org/list.html?users@jackrabbit.apache.org
* https://lists.apache.org/thread/j03b3qdhborc2jrhdc4d765d3jkh8bfw


### Credits
* Siebene@ (reporter)
* Michael Dürig (other)
* Manfred Baedke (other)
