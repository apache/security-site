---
title: Apache TomEE security advisories
description: Security information for Apache TomEE
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache TomEE? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=TomEE).

You can read more about the security policy on:

- [Apache TomEE security model](https://github.com/apache/tomee/security/policy)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Session fixation in embedded HTTP server ## { #CVE-2026-97890 }

CVE-2026-97890 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97890) [\[CVE json\]](./CVE-2026-97890.cve.json) [\[OSV json\]](./CVE-2026-97890.osv.json)



_Last updated: 2026-11-10T15:31:21.904Z_

### Affected

* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

The embedded HTTP server does not invalidate the previous session identifier when an application changes the session id, e.g. after login. An attacker who can plant a session identifier in a victim's browser can hijack the victim's authenticated session. Users are recommended to block network access to the embedded HTTP server from untrusted clients, or to migrate to the Tomcat based TomEE distributions.

### References
* https://lists.apache.org/thread/2wx7lvso54j2xp6m7omq12hkcb9tfzjx


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Caller identity leaks across requests in embedded HTTP server ## { #CVE-2026-97888 }

CVE-2026-97888 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97888) [\[CVE json\]](./CVE-2026-97888.cve.json) [\[OSV json\]](./CVE-2026-97888.osv.json)



_Last updated: 2026-11-10T15:32:07.999Z_

### Affected

* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

The embedded HTTP server does not clear the security identity established during a request before its worker thread handles the next request. A remote unauthenticated attacker can have their request processed with the identity of a previously authenticated user, gaining that user's privileges. Only applications served by the embedded HTTP server that authenticate programmatically or via basic authentication are affected. Users are recommended to block network access to the embedded HTTP server from untrusted clients, or to migrate to the Tomcat based TomEE distributions.

### References
* https://lists.apache.org/thread/7snc0d5bd2hvk1416v5b34pjgn0mmdvn


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Path traversal in embedded HTTP server static resource handling ## { #CVE-2026-97881 }

CVE-2026-97881 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97881) [\[CVE json\]](./CVE-2026-97881.cve.json) [\[OSV json\]](./CVE-2026-97881.osv.json)



_Last updated: 2026-11-10T15:32:33.362Z_

### Affected

* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

The embedded OpenEJB HTTP server does not restrict static resource paths to the configured resource directories. A remote unauthenticated attacker can read arbitrary files accessible to the server process. Users are recommended to block network access to the embedded HTTP server from untrusted clients, or to migrate to the Tomcat based TomEE distributions.

### References
* https://lists.apache.org/thread/pptsyzp963c01nmss9hn7p68pthzdnp9


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Authentication bypass in the embedded HTTP server for endpoints protected by HTTP Basic authentication ## { #CVE-2026-97880 }

CVE-2026-97880 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97880) [\[CVE json\]](./CVE-2026-97880.cve.json) [\[OSV json\]](./CVE-2026-97880.osv.json)



_Last updated: 2026-11-10T15:33:20.499Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

The embedded OpenEJB HTTP server dispatches some requests to REST endpoints configured for HTTP Basic authentication without verifying credentials. A remote unauthenticated attacker can invoke protected resources, bypassing authentication. Only deployments that use the embedded HTTP server with Basic authentication are affected. Users are recommended to block network access to the embedded HTTP server from untrusted clients, or to migrate to the Tomcat based TomEE distributions.

### References
* https://lists.apache.org/thread/fm51rhyqmjv2b9hphro608thj4yr4ngx


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Authentication bypass for Hessian endpoints in non-root web applications ## { #CVE-2026-97874 }

CVE-2026-97874 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97874) [\[CVE json\]](./CVE-2026-97874.cve.json) [\[OSV json\]](./CVE-2026-97874.osv.json)



_Last updated: 2026-11-10T15:33:56.619Z_

### Affected

* Apache TomEE from 4.6.0 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

When Hessian remoting is configured with BASIC authentication, the authentication check is not applied to Hessian endpoints of applications deployed under a non-root context path. A remote unauthenticated attacker can invoke the exposed EJB methods without credentials. Users are recommended to block network access to Hessian endpoints from untrusted clients, or to migrate to another remoting protocol.

### References
* https://lists.apache.org/thread/jl8dn3bdz52n8126gvc85nddprkwjhmq


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Authentication bypass of Hessian EJB endpoints due to ignored security settings ## { #CVE-2026-97872 }

CVE-2026-97872 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97872) [\[CVE json\]](./CVE-2026-97872.cve.json) [\[OSV json\]](./CVE-2026-97872.osv.json)



_Last updated: 2026-11-10T15:34:19.551Z_

### Affected

* Apache TomEE from 4.6.0 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

When an EJB is exposed over the optional Hessian protocol inside an existing web application, some configured authentication and transport security settings are silently not enforced. A remote unauthenticated attacker can invoke the exposed EJB methods. Only deployments using the Hessian module with such settings are affected. Users are recommended to block network access to Hessian endpoints from untrusted clients, or to migrate to another remoting protocol.

### References
* https://lists.apache.org/thread/hythwhxfnmghgv21y2pw73s41qt99z72


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Missing authentication for Hessian endpoints in embedded HTTP server ## { #CVE-2026-97870 }

CVE-2026-97870 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97870) [\[CVE json\]](./CVE-2026-97870.cve.json) [\[OSV json\]](./CVE-2026-97870.osv.json)



_Last updated: 2026-11-10T15:34:48.122Z_

### Affected

* Apache TomEE from 4.6.0 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

When Hessian remoting endpoints are served by the embedded HTTP server, configured authentication and transport security requirements are silently ignored. A remote unauthenticated attacker can invoke the exposed EJB methods without credentials or over an unencrypted connection. Only deployments that use the embedded HTTP server rather than Tomcat and rely on these settings are affected. Users are recommended to block network access to Hessian endpoints from untrusted clients, or to migrate to another remoting protocol.

### References
* https://lists.apache.org/thread/hvggn9r4nod9yrww9qrz5vttcrcvomhz


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Database credential disclosure via remote JNDI lookup ## { #CVE-2026-97867 }

CVE-2026-97867 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97867) [\[CVE json\]](./CVE-2026-97867.cve.json) [\[OSV json\]](./CVE-2026-97867.osv.json)



_Last updated: 2026-11-10T15:35:59.249Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The EJBd remote protocol returns datasource connection details, including database credentials, to remote clients that look up a datasource. A remote client able to reach the EJBd endpoint can obtain the database credentials and connect to the database directly. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/f6nqckc3wgqnnsrkb1hd640o3k4omfvr


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Derby network service listens on all interfaces ## { #CVE-2026-97849 }

CVE-2026-97849 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97849) [\[CVE json\]](./CVE-2026-97849.cve.json) [\[OSV json\]](./CVE-2026-97849.osv.json)



_Last updated: 2026-11-10T15:36:29.896Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The embedded Derby network service ignores its configured bind address and listens on all network interfaces. When the service is enabled, a remote attacker with network access can connect to the database server and read or modify data. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/20fl5wnn3slxs0tq0ktmrc9xv9glffhq


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Missing TLS hostname verification in ejbds client connections ## { #CVE-2026-87758 }

CVE-2026-87758 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-87758) [\[CVE json\]](./CVE-2026-87758.cve.json) [\[OSV json\]](./CVE-2026-87758.osv.json)



_Last updated: 2026-11-10T15:37:06.712Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The remote EJB client does not verify that the hostname of the server it connects to matches the server's TLS certificate. An attacker able to intercept network traffic between an EJB client and server can impersonate the server and read or modify the traffic, including credentials and invocation data. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/nzy4n8rmv4zl5wzdz0v0kwrj62tjrd7z


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Missing authorization on internal deployer EJBs in default profile ## { #CVE-2026-87756 }

CVE-2026-87756 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-87756) [\[CVE json\]](./CVE-2026-87756.cve.json) [\[OSV json\]](./CVE-2026-87756.osv.json)



_Last updated: 2026-11-10T14:57:18.443Z_

### Affected

* Apache TomEE from 4.5.1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The internal system EJBs used for remote deployment and configuration did not enforce their administrative role check when the server ran with the default profile. A remote unauthenticated attacker able to reach the remote EJB endpoint could deploy arbitrary applications and execute code. Only installations that enabled the system applications and a remote EJB endpoint are exposed. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread.html/4748mnztpzyfcy840z143ttgj92yl84r


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Stateful session bean hijacking via predictable session identifiers ## { #CVE-2026-87755 }

CVE-2026-87755 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-87755) [\[CVE json\]](./CVE-2026-87755.cve.json) [\[OSV json\]](./CVE-2026-87755.osv.json)



_Last updated: 2026-11-10T14:56:28.554Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

Stateful session bean identifiers are not generated from a cryptographically secure random source. A remote attacker with access to the EJB remote endpoint who holds one valid identifier can derive those of other clients' sessions and invoke methods on their beans, exposing or modifying other users' session state. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread.html/srzp26oyjtb3bwgxwsyhpphv778s17m8


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Path traversal via stateful EJB passivation ## { #CVE-2026-86811 }

CVE-2026-86811 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86811) [\[CVE json\]](./CVE-2026-86811.cve.json) [\[OSV json\]](./CVE-2026-86811.osv.json)



_Last updated: 2026-11-10T14:55:49.535Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The stateful session bean passivation mechanism derives the on-disk file name from a client-supplied identifier without validating it. A remote attacker with access to the remote EJB service can cause session state to be read from or written to files outside the passivation directory. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread.html/f2x7r654o1nt2z98m39kk0m6x24mz69f


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Username enumeration and timing side channel in JAAS login modules ## { #CVE-2026-86532 }

CVE-2026-86532 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86532) [\[CVE json\]](./CVE-2026-86532.cve.json) [\[OSV json\]](./CVE-2026-86532.osv.json)



_Last updated: 2026-11-10T14:54:32.864Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The bundled JAAS login modules leak whether a username exists and compare credentials in a non-constant-time manner. A remote unauthenticated attacker can enumerate valid accounts and may infer credential material through timing analysis. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread.html/oohwxbp6xx8dgl18xy1p1y6qjg59dgoh


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## DoS via unbounded request body and multipart handling in embedded HTTP server ## { #CVE-2026-86531 }

CVE-2026-86531 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86531) [\[CVE json\]](./CVE-2026-86531.cve.json) [\[OSV json\]](./CVE-2026-86531.osv.json)



_Last updated: 2026-11-10T15:37:38.210Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

The embedded OpenEJB HTTP server does not limit the size of incoming request bodies or of multipart requests, and does not remove the temporary files it creates for multipart parts. A remote unauthenticated attacker can cause excessive memory or disk usage, leading to denial of service. Deployments using the Tomcat connectors are not affected. Users are recommended to block network access to the embedded HTTP server from untrusted clients, or to migrate to the Tomcat based TomEE distributions.

### References
* https://lists.apache.org/thread/cm1vdbx03ctl607nrrkdqyshwjscpd2y


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## EJB method authorization is silently skipped on JDK 21+ ## { #CVE-2026-86336 }

CVE-2026-86336 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86336) [\[CVE json\]](./CVE-2026-86336.cve.json) [\[OSV json\]](./CVE-2026-86336.osv.json)



_Last updated: 2026-11-10T15:38:23.784Z_

### Affected

* Apache TomEE from 10.1.1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

Apache TomEE running on JDK 21 or later skips EJB method authorization checks, allowing callers to invoke EJB methods without the configured access restrictions being enforced. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/tv0407xmnpy4qctqm9nzx56lgjln2t4j


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Authentication bypass on EJB web service endpoints via HTTP method ## { #CVE-2026-111264 }

CVE-2026-111264 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111264) [\[CVE json\]](./CVE-2026-111264.cve.json) [\[OSV json\]](./CVE-2026-111264.osv.json)



_Last updated: 2026-11-10T15:04:29.387Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.0.0
* Apache TomEE from 1.5.0 through 1.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The security constraint generated for EJB JAX-WS endpoints with configured authentication protects only some HTTP methods. A remote unauthenticated attacker can bypass authentication by sending requests with another HTTP method. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread.html/tldxh492p71z2rlw7g4l1vplrxo5n116


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Jonathan Gallimore (remediation developer)


## Missing authentication on EJB web service endpoints deployed in a web application ## { #CVE-2026-111263 }

CVE-2026-111263 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111263) [\[CVE json\]](./CVE-2026-111263.cve.json) [\[OSV json\]](./CVE-2026-111263.osv.json)



_Last updated: 2026-11-10T15:05:07.056Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.0.0
* Apache TomEE from 1.5.0 through 1.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

Authentication configured for an EJB JAX-WS endpoint in the TomEE deployment descriptor is not enforced when the endpoint is published within an existing web application. A remote unauthenticated attacker can invoke the web service operations, unless the application protects the endpoint with its own web.xml security constraints or EJB method permissions. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread.html/bgk825mdkyxfrlnbfszmlmbwmlk1qlhl


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Jonathan Gallimore (remediation developer)


## LDAP injection in LDAP identity store ## { #CVE-2026-111262 }

CVE-2026-111262 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111262) [\[CVE json\]](./CVE-2026-111262.cve.json) [\[OSV json\]](./CVE-2026-111262.osv.json)



_Last updated: 2026-11-10T15:05:54.914Z_

### Affected

* Apache TomEE from 8.0.4 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The Jakarta Security LDAP identity store does not neutralize special characters in the caller name before using it in directory queries. A remote unauthenticated attacker can alter the queries to enumerate accounts, infer directory attribute values, or influence which directory entry the login is validated against. Only applications using the LDAP identity store are affected. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread.html/qrfq68g2znq773z7g960qsckldvtkqzd


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Authentication bypass with empty password in LDAP identity store ## { #CVE-2026-111261 }

CVE-2026-111261 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111261) [\[CVE json\]](./CVE-2026-111261.cve.json) [\[OSV json\]](./CVE-2026-111261.osv.json)



_Last updated: 2026-11-10T15:14:29.692Z_

### Affected

* Apache TomEE from 8.0.4 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The Jakarta Security LDAP identity store accepts an empty password as valid if the directory server allows unauthenticated binds, which some directory servers do by default. A remote attacker can then authenticate as any existing user without knowing the password. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread.html/8dfmrhg064j5btmfs3mwclnw88bdqrt7


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Predictable OpenID Connect state and nonce values ## { #CVE-2026-111260 }

CVE-2026-111260 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111260) [\[CVE json\]](./CVE-2026-111260.cve.json) [\[OSV json\]](./CVE-2026-111260.osv.json)



_Last updated: 2026-11-10T15:15:31.716Z_

### Affected

* Apache TomEE from 10.0.0-M2 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The Jakarta Security OpenID Connect authentication mechanism generates the state and nonce values with a non-cryptographic random number generator and insufficient entropy. A remote attacker who predicts these values can forge an authentication callback that logs a victim into the attacker's account, and the replay protection for ID tokens is weakened. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/y6oscfyggkdf5hrj518nl08v7l8rr40q


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Predictable HTTP session identifiers in embedded server ## { #CVE-2026-111259 }

CVE-2026-111259 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111259) [\[CVE json\]](./CVE-2026-111259.cve.json) [\[OSV json\]](./CVE-2026-111259.osv.json)



_Last updated: 2026-11-10T15:18:06.484Z_

### Affected

* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The embedded server generates HTTP session identifiers with a non-cryptographic random number generator by default. A remote attacker who observes a session identifier can predict the identifiers issued to other users and hijack their sessions, if the application relies on HTTP sessions for authentication. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/1sk4193kxtf18q2so25c62c2b73o94lg


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Security constraint bypass via request routing ## { #CVE-2026-111258 }

CVE-2026-111258 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111258) [\[CVE json\]](./CVE-2026-111258.cve.json) [\[OSV json\]](./CVE-2026-111258.osv.json)



_Last updated: 2026-11-10T15:19:04.836Z_

### Affected

* Apache TomEE from 1.5.0 through 1.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The optional request routing feature forwards requests to their configured destination without applying the security constraints of that destination or the protection of the web application's private directories. If a route copies client-controlled parts of the request path into its destination, a remote attacker can reach protected resources or read application configuration and class files. Only installations with such a routing configuration are affected. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/tr1mxp3vjk3zvc3k45ocz52ctg7wng9m


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Well-known administrative credentials created at startup ## { #CVE-2026-111257 }

CVE-2026-111257 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111257) [\[CVE json\]](./CVE-2026-111257.cve.json) [\[OSV json\]](./CVE-2026-111257.osv.json)



_Last updated: 2026-11-10T15:19:30.971Z_

### Affected

* Apache TomEE from 1.5.1 through 1.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

With the default configuration and no users defined in the default user database, TomEE silently adds an administrative user with a well-known password at startup. A remote attacker can use these credentials to authenticate to web applications that use the default realm and grant access to any authenticated user or to the TomEE administrative role. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/gzzn7jbzrfk8bo9ttmqhr3c6q3szc5vf


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Missing authentication for web service endpoints in embedded HTTP server ## { #CVE-2026-111256 }

CVE-2026-111256 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111256) [\[CVE json\]](./CVE-2026-111256.cve.json) [\[OSV json\]](./CVE-2026-111256.osv.json)



_Last updated: 2026-11-10T15:20:00.456Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 4.6.0 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

When JAX-WS or JAX-RS endpoints are published by the embedded OpenEJB HTTP server rather than Tomcat, some configured authentication methods are silently ignored and the endpoint is published without authentication. A remote unauthenticated attacker can invoke the exposed operations without credentials. Only deployments that use the embedded HTTP server and rely on such an authentication method are affected. Users are recommended to block network access to the embedded HTTP server from untrusted clients, or to migrate to the Tomcat based TomEE distributions.

### References
* https://lists.apache.org/thread/pfspkd8c0d5pxx3k04vnfvrn979tz1zo


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Markus Jung (remediation developer)


## Unauthenticated server shutdown via the admin port ## { #CVE-2026-111251 }

CVE-2026-111251 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111251) [\[CVE json\]](./CVE-2026-111251.cve.json) [\[OSV json\]](./CVE-2026-111251.osv.json)



_Last updated: 2026-11-10T15:20:24.580Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The admin service of the standalone OpenEJB server accepts stop requests without any authentication. Any local user or process able to connect to the admin port can stop the server, leading to denial of service; the admin service is enabled by default in the standalone server and bound to the loopback interface. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/btc4jq3k20xysf7kqsyyt7jg74v8768s


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Authentication bypass via programmatic authentication in embedded HTTP server ## { #CVE-2026-111250 }

CVE-2026-111250 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111250) [\[CVE json\]](./CVE-2026-111250.cve.json) [\[OSV json\]](./CVE-2026-111250.osv.json)



_Last updated: 2026-11-10T15:21:30.647Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

The embedded OpenEJB HTTP server reports every request as authenticated when an application requests authentication programmatically. A remote unauthenticated attacker can access functionality protected this way. Only applications served by the embedded HTTP server that rely on programmatic authentication are affected. Users are recommended to block network access to the embedded HTTP server from untrusted clients, or to migrate to the Tomcat based TomEE distributions.

### References
* https://lists.apache.org/thread/yr5sbbmyym2zfoho8qv3yxshoztqjk6k


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Unauthenticated LiveReload endpoint reachable from the network ## { #CVE-2026-111249 }

CVE-2026-111249 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111249) [\[CVE json\]](./CVE-2026-111249.cve.json) [\[OSV json\]](./CVE-2026-111249.osv.json)



_Last updated: 2026-11-10T15:22:15.016Z_

### Affected

* Apache TomEE from 7.0.0-M2 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The development-time LiveReload support listens on all network interfaces without authentication and accepts websocket connections from any origin. A network attacker, or a web page visited by the developer, can observe the names of changed files in the watched folder and the server version, and reach the deployed applications through the additional port. This only affects LiveReload enabled in the embedded Maven plugin. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/sssq84vj136dz964j1ooyr20jc9s6pnm


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Authentication with the stored password digest in Tomcat user identity store ## { #CVE-2026-111248 }

CVE-2026-111248 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111248) [\[CVE json\]](./CVE-2026-111248.cve.json) [\[OSV json\]](./CVE-2026-111248.osv.json)



_Last updated: 2026-11-10T15:22:44.423Z_

### Affected

* Apache TomEE from 8.0.0-M2 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The Jakarta Security identity store backed by the Tomcat user database compares the supplied password with the stored value as plain text and ignores the configured credential handler. When digested passwords are stored, an attacker who obtained a stored digest, for example from a leaked users file or backup, can authenticate with the digest instead of the password. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/47svr3bg4lchzlhkl55g5bfykhnx48jo


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Privilege escalation via user name matching a role name ## { #CVE-2026-111247 }

CVE-2026-111247 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111247) [\[CVE json\]](./CVE-2026-111247.cve.json) [\[OSV json\]](./CVE-2026-111247.osv.json)



_Last updated: 2026-11-10T15:23:19.897Z_

### Affected

* Apache TomEE from 8.0.7 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

When resolving security roles of a realm-authenticated caller, the caller's user name is also treated as a role name in addition to the roles assigned by the realm. An authenticated attacker who can obtain an account whose user name equals a role name, for example through self-registration, is granted that role wherever authorization is evaluated through the Jakarta Authorization policy. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/wmx75ytmp7d5h8cnd8jf1lg2gbw983f3


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## HTTP sessions shared across web applications in embedded HTTP server ## { #CVE-2026-111246 }

CVE-2026-111246 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111246) [\[CVE json\]](./CVE-2026-111246.cve.json) [\[OSV json\]](./CVE-2026-111246.osv.json)



_Last updated: 2026-11-10T15:23:44.271Z_

### Affected

* Apache TomEE from 4.5.2 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

The embedded OpenEJB HTTP server does not isolate HTTP sessions between web applications. A remote attacker can use a session established in one web application in another one, which then trusts session state set by the first application. Only deployments hosting several web applications on the embedded HTTP server are affected. Users are recommended to block network access to the embedded HTTP server from untrusted clients, or to migrate to the Tomcat based TomEE distributions.

### References
* https://lists.apache.org/thread/3l9twg2ywvgwjffv4wwop2fmtp05fp39


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Privilege escalation via WS-Security caller identity leaking between requests ## { #CVE-2026-111245 }

CVE-2026-111245 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111245) [\[CVE json\]](./CVE-2026-111245.cve.json) [\[OSV json\]](./CVE-2026-111245.osv.json)



_Last updated: 2026-11-10T15:24:06.415Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

After a successful WS-Security UsernameToken authentication, the caller identity stays associated with the worker thread once the request completes when web services are served by the standalone OpenEJB HTTP server. A remote unauthenticated attacker whose request is later processed on the same thread can invoke protected EJB methods with the identity of a previously authenticated user. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/6nr7gp3kxf919mhv2o0yg45t310x5go8


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Authorization bypass in MicroProfile JWT role checks for JAX-RS resources ## { #CVE-2026-111244 }

CVE-2026-111244 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111244) [\[CVE json\]](./CVE-2026-111244.cve.json) [\[OSV json\]](./CVE-2026-111244.osv.json)



_Last updated: 2026-11-10T15:27:00.731Z_

### Affected

* Apache TomEE from 7.1.0 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

When MicroProfile JWT role-based access control is used, the access constraints of JAX-RS resources are not always enforced as declared: resources that declare an empty set of allowed roles are accessible to every caller, resource classes that inherit the same method from a common superclass share their constraints, and class-level constraints declared on a superclass are ignored. A remote attacker can invoke resources that should be denied to them, in some configurations without authentication. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/flpx4mgmzqx36fm6gy3thcoh74b5yz7o


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Expired MicroProfile JWT tokens accepted with negative clock skew ## { #CVE-2026-111243 }

CVE-2026-111243 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111243) [\[CVE json\]](./CVE-2026-111243.cve.json) [\[OSV json\]](./CVE-2026-111243.osv.json)



_Last updated: 2026-11-10T15:29:15.045Z_

### Affected

* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

A negative MicroProfile JWT clock skew setting is not rejected and disables validation of the token expiration and other time-based claims. In such configurations, an attacker in possession of an expired token can still authenticate with it. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/zb9sshs1fhz72llk3bb20ksw50n9jhqp


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Privilege escalation via leaked MicroProfile JWT run-as identity ## { #CVE-2026-111242 }

CVE-2026-111242 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111242) [\[CVE json\]](./CVE-2026-111242.cve.json) [\[OSV json\]](./CVE-2026-111242.osv.json)



_Last updated: 2026-11-10T15:29:38.204Z_

### Affected

* Apache TomEE from 8.0.0-M2 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

When MicroProfile JWT authentication is used for servlets that declare a run-as identity, the security state established for a request is not always cleared from the processing thread when the request does not complete normally. A remote attacker holding a valid token can cause later, unrelated requests served by the same thread to invoke enterprise beans with the elevated run-as identity. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/opr1oob7p8xtqwcj1yv2dnsj4zqo9f03


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Local code execution via predictable passivation files in the shared temporary directory ## { #CVE-2026-111241 }

CVE-2026-111241 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111241) [\[CVE json\]](./CVE-2026-111241.cve.json) [\[OSV json\]](./CVE-2026-111241.osv.json)



_Last updated: 2026-11-10T15:30:01.861Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

When a non-default stateful session bean passivation strategy is configured, passivated bean state is written to predictably named files in the shared system temporary directory, reusing files that already exist there, and is deserialized on activation. A local attacker who can write to that directory can read passivated session state or supply data that the server deserializes, potentially leading to code execution as the server process. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/kbpc7t241483pnxo2sccrhyp6pjkwbq2


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Authentication bypass for accounts without a stored password in SQL login module ## { #CVE-2026-111240 }

CVE-2026-111240 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111240) [\[CVE json\]](./CVE-2026-111240.cve.json) [\[OSV json\]](./CVE-2026-111240.osv.json)



_Last updated: 2026-11-10T15:30:27.521Z_

### Affected

* Apache TomEE from 4.0.0-beta-1 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 before 10.3.0
* Apache TomEE from 11.0.0-M1 before 11.0.0-M2


### Description

The JDBC based JAAS login module accepts a login without a password for accounts whose stored password is NULL. A remote attacker who knows the user name of such an account can authenticate as that user and obtain its roles. Only deployments using this login module with NULL passwords in the user table are affected. Users are recommended to upgrade to version 10.3.0 or 11.0.0-M2, which fix the issue.

### References
* https://lists.apache.org/thread/1w1olwsbzpsj7mnv8v3vj30ohq0t0c52


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)


## Code execution by any authenticated user via the SSH administration shell ## { #CVE-2026-111239 }

CVE-2026-111239 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-111239) [\[CVE json\]](./CVE-2026-111239.cve.json) [\[OSV json\]](./CVE-2026-111239.osv.json)



_Last updated: 2026-11-10T15:30:56.576Z_

### Affected

* Apache TomEE from 4.0.0 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1
* Apache TomEE from 4.0.0 through 4.7.5
* Apache TomEE from 7.0.0-M1 before 10.0.0-M1
* Apache TomEE from 10.0.0-M1 through 10.2.0
* Apache TomEE at 11.0.0-M1


### Description

The optional SSH administration service grants full access to the administration shell to every user that authenticates against its configured login domain, without checking for an administrative role. An attacker holding the credentials of any user in that domain, including a low-privileged application user, can execute arbitrary code as the server process. Users are recommended to disable the SSH administration service, or to block network access to it from untrusted clients and restrict its login domain to administrative users.

### References
* https://lists.apache.org/thread/wfoxj510yol03lmzbzdftyphwvtq87wg


### Credits
* The Apache Software Foundation (finder)
* Claude Security (tool)
* Richard Zowalla (remediation developer)
