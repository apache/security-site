---
title: Apache Pulsar security advisories
description: Security information for Apache Pulsar
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Pulsar? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Authentication with JWT allows use of “none”-algorithm ## { #CVE-2021-22160 }

CVE-2021-22160 [\[CVE json\]](./CVE-2021-22160.cve.json)

_Last updated: 2021-05-25T13:39:14.223Z_

### Affected

* Apache Pulsar from Apache Pulsar before 2.7.1


### Description

If Apache Pulsar is configured to authenticate clients using tokens based on JSON Web Tokens (JWT), the signature of the token is not validated if the algorithm of the presented token is set to "none". This allows an attacker to connect to Pulsar instances as any user (incl. admins).

### References
* https://lists.apache.org/thread.html/r347650d15a3e9c5f58b83e918b6ad6dedc2a63d3eb63da8e6a7be87e%40%3Cusers.pulsar.apache.org%3E


## Pulsar Admin API allows access to data from other tenants using getMessageById API ## { #CVE-2021-41571 }

CVE-2021-41571 [\[CVE json\]](./CVE-2021-41571.cve.json)

_Last updated: 2022-01-31T12:57:16.188Z_

### Affected

* Apache Pulsar from Apache Pulsar through 2.8.0


### Description

In Apache Pulsar it is possible to access data from BookKeeper that does not belong to the topics accessible by the authenticated user.

The Admin API get-message-by-id requires the user to input a topic and a ledger id. The ledger id is a pointer to the data, and it is supposed to be a valid it for the topic.
Authorisation controls are performed against the topic name and there is not proper validation the that ledger id is valid in the context of such ledger.
So it may happen that the user is able to read from a ledger that contains data owned by another tenant.

This issue affects Apache Pulsar Apache Pulsar version 2.8.0 and prior versions; Apache Pulsar version 2.7.3 and prior versions; Apache Pulsar version 2.6.4 and prior versions.

### References
* https://pulsar.apache.org/admin-rest-api/#operation/getLastMessageId
* https://github.com/apache/pulsar/issues/11814
* https://lists.apache.org/thread/8n3k7pvyh4cf9q2jfzb6pb32ync6xlvr


## Apache Pulsar Proxy target broker address isn't validated ## { #CVE-2022-24280 }

CVE-2022-24280 [\[CVE json\]](./CVE-2022-24280.cve.json)

_Last updated: 2022-09-23T09:22:34.280Z_

### Affected

* Apache Pulsar from 2.7 through 2.7.4
* Apache Pulsar from 2.8 through 2.8.2
* Apache Pulsar from 2.9 through 2.9.1
* Apache Pulsar from 2.6 and earlier through 2.6.4


### Description

Improper Input Validation vulnerability in Proxy component of Apache Pulsar allows an attacker to make TCP/IP connection attempts that originate from the Pulsar Proxy's IP address.

When the Apache Pulsar Proxy component is used, it is possible to attempt to open TCP/IP connections to any IP address and port that the Pulsar Proxy can connect to. An attacker could use this as a way for DoS attacks that originate from the Pulsar Proxy's IP address.
It hasn’t been detected that the Pulsar Proxy authentication can be bypassed. The attacker will have to have a valid token to a properly secured Pulsar Proxy.

This issue affects Apache Pulsar Proxy versions 2.7.0 to 2.7.4; 2.8.0 to 2.8.2; 2.9.0 to 2.9.1; 2.6.4 and earlier.

### References
* https://lists.apache.org/thread/ghs9jtjfbpy4c6xcftyvkl6swznlom1v


### Credits
* This issue was discovered by Lari Hotari of DataStax.


## Improper Hostname Verification in Java Client and Proxy can expose authentication data via MITM ## { #CVE-2022-33681 }

CVE-2022-33681 [\[CVE json\]](./CVE-2022-33681.cve.json)

_Last updated: 2022-09-23T09:22:48.001Z_

### Affected

* Apache Pulsar at 2.10.0
* Apache Pulsar from 2.7 through 2.7.4
* Apache Pulsar from 2.8 through 2.8.3
* Apache Pulsar from 2.9 through 2.9.2
* Apache Pulsar from 2.6 and earlier through 2.6.4


### Description

Delayed TLS hostname verification in the Pulsar Java Client and the Pulsar Proxy make each client vulnerable to a man in the middle attack. Connections from the Pulsar Java Client to the Pulsar Broker/Proxy and connections from the Pulsar Proxy to the Pulsar Broker are vulnerable. Authentication data is sent before verifying the server’s TLS certificate matches the hostname, which means authentication data could be exposed to an attacker.

An attacker can only take advantage of this vulnerability by taking control of a machine 'between' the client and the server. The attacker must then actively manipulate traffic to perform the attack by providing the client with a cryptographically valid certificate for an unrelated host. Because the client sends authentication data before performing hostname verification, an attacker could gain access to the client’s authentication data. The client eventually closes the connection when it verifies the hostname and identifies the targeted hostname does not match a hostname on the certificate.

Because the client eventually closes the connection, the value of the intercepted authentication data depends on the authentication method used by the client. Token based authentication and username/password authentication methods are vulnerable because the authentication data can be used to impersonate the client in a separate session.

This issue affects Apache Pulsar Java Client versions 2.7.0 to 2.7.4; 2.8.0 to 2.8.3; 2.9.0 to 2.9.2; 2.10.0; 2.6.4 and earlier.

### References
* https://lists.apache.org/thread/fpo6x10trvn20hlk0dmnr5vlz5v4kl3d


### Credits
* This issue was discovered by Michael Marshall of DataStax.


## Disabled Hostname Verification makes Brokers, Proxies vulnerable to MITM attack ## { #CVE-2022-33682 }

CVE-2022-33682 [\[CVE json\]](./CVE-2022-33682.cve.json)

_Last updated: 2022-09-23T09:23:08.927Z_

### Affected

* Apache Pulsar at 2.10.0
* Apache Pulsar from 2.7 through 2.7.4
* Apache Pulsar from 2.8 through 2.8.3
* Apache Pulsar from 2.9 through 2.9.2
* Apache Pulsar from 2.6 and earlier through 2.6.4


### Description

TLS hostname verification cannot be enabled in the Pulsar Broker's Java Client, the Pulsar Broker's Java Admin Client, the Pulsar WebSocket Proxy's Java Client, and the Pulsar Proxy's Admin Client leaving intra-cluster connections and geo-replication connections vulnerable to man in the middle attacks, which could leak credentials, configuration data, message data, and any other data sent by these clients. The vulnerability is for both the pulsar+ssl protocol and HTTPS.

An attacker can only take advantage of this vulnerability by taking control of a machine 'between' the client and the server. The attacker must then actively manipulate traffic to perform the attack by providing the client with a cryptographically valid certificate for an unrelated host.

This issue affects Apache Pulsar Broker, Proxy, and WebSocket Proxy versions 2.7.0 to 2.7.4; 2.8.0 to 2.8.3; 2.9.0 to 2.9.2; 2.10.0; 2.6.4 and earlier.

### References
* https://lists.apache.org/thread/l0ynfl161qghwfcgbbl8ld9hzbl9t3yx


### Credits
* This issue was discovered by Michael Marshall of DataStax.


## Disabled Certificate Validation makes Broker, Proxy Admin Clients vulnerable to MITM attack  ## { #CVE-2022-33683 }

CVE-2022-33683 [\[CVE json\]](./CVE-2022-33683.cve.json)

_Last updated: 2022-09-23T09:23:30.771Z_

### Affected

* Apache Pulsar at 2.10.0
* Apache Pulsar from 2.7 through 2.7.4
* Apache Pulsar from 2.8 through 2.8.3
* Apache Pulsar from 2.9 through 2.9.2
* Apache Pulsar from 2.6 and earlier through 2.6.4


### Description

Apache Pulsar Brokers and Proxies create an internal Pulsar Admin Client that does not verify peer TLS certificates, even when tlsAllowInsecureConnection is disabled via configuration. The Pulsar Admin Client's intra-cluster and geo-replication HTTPS connections are vulnerable to man in the middle attacks, which could leak authentication data, configuration data, and any other data sent by these clients.

An attacker can only take advantage of this vulnerability by taking control of a machine 'between' the client and the server. The attacker must then actively manipulate traffic to perform the attack.

This issue affects Apache Pulsar Broker and Proxy versions 2.7.0 to 2.7.4; 2.8.0 to 2.8.3; 2.9.0 to 2.9.2; 2.10.0; 2.6.4 and earlier.

### References
* https://lists.apache.org/thread/42v5rsxj36r3nhfxhmhb2x12r5jmvx3x


### Credits
* This issue was discovered by Michael Marshall of DataStax.


## Apache Pulsar C++/Python OAuth Clients prior to 3.0.0 were vulnerable to an MITM attack due to Disabled Certificate Validation ## { #CVE-2022-33684 }

CVE-2022-33684 [\[CVE json\]](./CVE-2022-33684.cve.json)

_Last updated: 2022-11-04T15:46:59.823Z_

### Affected

* Apache Pulsar from 2.7 through 2.7.4
* Apache Pulsar from 2.8 through 2.8.3
* Apache Pulsar from 2.9 through 2.9.2
* Apache Pulsar from 2.10 through 2.10.1
* Apache Pulsar from 2.6 and earlier through 2.6.4
* Apache Pulsar from 3.0.0 before 3.0*


### Description

The Apache Pulsar C++ Client does not verify peer TLS certificates when making HTTPS calls for the OAuth2.0 Client Credential Flow, even when tlsAllowInsecureConnection is disabled via configuration. This vulnerability allows an attacker to perform a man in the middle attack and intercept and/or modify the GET request that is sent to the ClientCredentialFlow 'issuer url'. The intercepted credentials can be used to acquire authentication data from the OAuth2.0 server to then authenticate with an Apache Pulsar cluster.

An attacker can only take advantage of this vulnerability by taking control of a machine 'between' the client and the server. The attacker must then actively manipulate traffic to perform the attack.

The Apache Pulsar Python Client wraps the C++ client, so it is also vulnerable in the same way. This issue affects Apache Pulsar C++ Client and Python Client versions 2.7.0 to 2.7.4; 2.8.0 to 2.8.3; 2.9.0 to 2.9.2; 2.10.0 to 2.10.1; 2.6.4 and earlier.

Any users running affected versions of the C++ Client or the Python Client should rotate vulnerable OAuth2.0 credentials, including client_id and client_secret.

2.7 C++ and Python Client users should upgrade to 2.7.5 and rotate vulnerable OAuth2.0 credentials.
2.8 C++ and Python Client users should upgrade to 2.8.4 and rotate vulnerable OAuth2.0 credentials.
2.9 C++ and Python Client users should upgrade to 2.9.3 and rotate vulnerable OAuth2.0 credentials.
2.10 C++ and Python Client users should upgrade to 2.10.2 and rotate vulnerable OAuth2.0 credentials.
3.0 C++ users are unaffected and 3.0 Python Client users will be unaffected when it is released.

Any users running the C++ and Python Client for 2.6 or less should upgrade to one of the above patched versions.

### References
* https://lists.apache.org/thread/ky1ssskvkj00y36k7nys9b5gm5jjrzwv


### Credits
* This issue was discovered by Michael Rowley, michaellrowley@protonmail.com


## Incorrect Authorization Validation for Rest Producer ## { #CVE-2023-30428 }

CVE-2023-30428 [\[CVE json\]](./CVE-2023-30428.cve.json)

_Last updated: 2023-07-12T09:11:23.044Z_

### Affected

* Apache Pulsar Broker from 2.9.0 through 2.9.5
* Apache Pulsar Broker from 2.10.0 before 2.10.4
* Apache Pulsar Broker at 2.11.0


### Description

Incorrect Authorization vulnerability in Apache Software Foundation Apache Pulsar Broker's Rest Producer allows authenticated user with a custom HTTP header to produce a message to any topic using the broker's admin role.<br>This issue affects Apache Pulsar Brokers: from 2.9.0 through 2.9.5, from 2.10.0 before 2.10.4, 2.11.0.<br><br>The vulnerability is exploitable when an attacker can connect directly to the Pulsar Broker. If an attacker is connecting through the Pulsar Proxy, there is no known way to exploit this authorization vulnerability.<br><br>There are two known risks for affected users. First, an attacker could produce garbage messages to any topic in the cluster. Second, an attacker could produce messages to the topic level policies topic for other tenants and influence topic settings that could lead to exfiltration and/or deletion of messages for other tenants.<br><br>2.8 Pulsar Broker users and earlier are unaffected.<br>2.9 Pulsar Broker users should upgrade to one of the patched versions.<br>2.10 Pulsar Broker users should upgrade to at least 2.10.4.<br>2.11 Pulsar Broker users should upgrade to at least 2.11.1.<br>3.0 Pulsar Broker users are unaffected.<br><br>

### References
* https://lists.apache.org/thread/v39hqtgrmyxr85rmofwvgrktnflbq3q5


### Credits
* Michael Marshall of DataStax (finder)


## Incorrect Authorization for Function Worker when using mTLS Authentication through Pulsar Proxy ## { #CVE-2023-30429 }

CVE-2023-30429 [\[CVE json\]](./CVE-2023-30429.cve.json)

_Last updated: 2023-07-12T09:08:18.670Z_

### Affected

* Apache Pulsar before 2.10.4
* Apache Pulsar at 2.11.0


### Description

Incorrect Authorization vulnerability in Apache Software Foundation Apache Pulsar.<br><br>This issue affects Apache Pulsar: before 2.10.4, and 2.11.0.<br><br>When a client connects to the Pulsar Function Worker via the Pulsar Proxy where the Pulsar Proxy uses mTLS authentication to authenticate with the Pulsar Function Worker, the Pulsar Function Worker incorrectly performs authorization by using the Proxy's role for authorization instead of the client's role, which can lead to privilege escalation, especially if the proxy is configured with a superuser role.<br><br>The recommended mitigation for impacted users is to upgrade the Pulsar Function Worker to a patched version.<br><br>2.10 Pulsar Function Worker users should upgrade to at least 2.10.4.<br>2.11 Pulsar Function Worker users should upgrade to at least 2.11.1.<br>3.0 Pulsar Function Worker users are unaffected.<br>Any users running the Pulsar Function Worker for 2.9.* and earlier should upgrade to one of the above patched versions.<br>

### References
* https://lists.apache.org/thread/v0gcvvxswr830314q4b1kybsfmcf3jf8


### Credits
* Michael Marshall of DataStax (finder)


## Broker does not always disconnect client when authentication data expires ## { #CVE-2023-31007 }

CVE-2023-31007 [\[CVE json\]](./CVE-2023-31007.cve.json)

_Last updated: 2023-07-13T08:27:41.124Z_

### Affected

* Apache Pulsar before 2.9.5
* Apache Pulsar from 2.10.0 through 2.10.3
* Apache Pulsar at 2.11.0


### Description

Improper Authentication vulnerability in Apache Software Foundation Apache Pulsar Broker allows a client to stay connected to a broker after authentication data expires if the client connected through the Pulsar Proxy when the broker is configured with authenticateOriginalAuthData=false or if a client connects directly to a broker with a specially crafted connect command when the broker is configured with authenticateOriginalAuthData=false.<br><br>This issue affects Apache Pulsar: through 2.9.4, from 2.10.0 through 2.10.3, 2.11.0.<br><br>2.9 Pulsar Broker users should upgrade to at least 2.9.5.<br>2.10 Pulsar Broker users should upgrade to at least 2.10.4.<br>2.11 Pulsar Broker users should upgrade to at least 2.11.1.<br>3.0 Pulsar Broker users are unaffected.<br>Any users running the Pulsar Broker for 2.8.* and earlier should upgrade to one of the above patched versions.<br>

### References
* https://lists.apache.org/thread/qxn99xxyp0zv6jchjggn3soyo5gvqfxj


### Credits
* Michael Marshall of DataStax (finder)


## Improper Authentication for WebSocket Proxy Endpoint Allows DoS ## { #CVE-2023-37544 }

CVE-2023-37544 [\[CVE json\]](./CVE-2023-37544.cve.json)

_Last updated: 2023-12-20T08:33:58.071Z_

### Affected

* Apache Pulsar WebSocket Proxy from 2.8.0 through 2.8.*
* Apache Pulsar WebSocket Proxy from 2.9.0 through 2.9.*
* Apache Pulsar WebSocket Proxy from 2.10.0 through 2.10.4
* Apache Pulsar WebSocket Proxy from 2.11.0 through 2.11.1
* Apache Pulsar WebSocket Proxy at 3.0.0


### Description

Improper Authentication vulnerability in Apache Pulsar WebSocket Proxy allows an attacker to connect to the /pingpong endpoint without authentication.<br><br>This issue affects Apache Pulsar WebSocket Proxy: from 2.8.0 through 2.8.*, from 2.9.0 through 2.9.*, from 2.10.0 through 2.10.4, from 2.11.0 through 2.11.1, 3.0.0.<br><br>The known risks include a denial of service due to the WebSocket Proxy accepting any connections, and excessive data transfer due to misuse of the WebSocket ping/pong feature.<br><br>2.10 Pulsar WebSocket Proxy users should upgrade to at least 2.10.5.<br>2.11 Pulsar WebSocket Proxy users should upgrade to at least 2.11.2.<br>3.0 Pulsar WebSocket Proxy users should upgrade to at least 3.0.1.<br>3.1 Pulsar WebSocket Proxy users are unaffected.<br>Any users running the Pulsar WebSocket Proxy for 2.8, 2.9, and earlier should upgrade to one of the above patched versions.

### References
* https://lists.apache.org/thread/od0k9zts1toc9h9snbqq4pjpyx28mv4m


### Credits
* Michael Marshall of DataStax (finder)


## Incorrect Authorization for Function Worker Can Leak Sink/Source Credentials ## { #CVE-2023-37579 }

CVE-2023-37579 [\[CVE json\]](./CVE-2023-37579.cve.json)

_Last updated: 2023-07-12T09:05:20.256Z_

### Affected

* Apache Pulsar Function Worker before 2.10.4
* Apache Pulsar Function Worker at 2.11.0


### Description

Incorrect Authorization vulnerability in Apache Software Foundation Apache Pulsar Function Worker.<br><br>This issue affects Apache Pulsar: before 2.10.4, and 2.11.0.<br><br>Any authenticated user can retrieve a source's configuration or a sink's configuration without authorization. Many sources and sinks contain credentials in the configuration, which could lead to leaked credentials. This vulnerability is mitigated by the fact that there is not a known way for an authenticated user to enumerate another tenant's sources or sinks, meaning the source or sink name would need to be guessed in order to exploit this vulnerability.<br><br>The recommended mitigation for impacted users is to upgrade the Pulsar Function Worker to a patched version.<br><br>2.10 Pulsar Function Worker users should upgrade to at least 2.10.4.<br>2.11 Pulsar Function Worker users should upgrade to at least 2.11.1.<br>3.0 Pulsar Function Worker users are unaffected.<br>Any users running the Pulsar Function Worker for 2.9.* and earlier should upgrade to one of the above patched versions.<br><br>

### References
* https://lists.apache.org/thread/0dmn3cb5n2p08o3cpj3ycfhzfqs2ppwz


### Credits
* Michael Marshall of DataStax (finder)


## Timing attack in SASL token signature verification ## { #CVE-2023-51437 }

CVE-2023-51437 [\[CVE json\]](./CVE-2023-51437.cve.json)

_Last updated: 2024-02-07T09:18:08.965Z_

### Affected

* Apache Pulsar through 2.10.5
* Apache Pulsar from 2.11.0 through 2.11.2
* Apache Pulsar from 3.0.0 through 3.0.1
* Apache Pulsar at 3.1.0


### Description

Observable timing discrepancy vulnerability in Apache Pulsar SASL Authentication Provider can allow an attacker to forge a SASL Role Token that will pass signature verification.<br><p>Users are recommended to upgrade to version 2.11.3, 3.0.2, or 3.1.1 which fixes the issue. Users should also consider updating the configured secret in the `saslJaasServerRoleTokenSignerSecretPath` file.<br></p><p>Any component matching an above version running the SASL Authentication Provider is affected. That includes the Pulsar Broker, Proxy, Websocket Proxy, or Function Worker.</p>2.11 Pulsar users should upgrade to at least 2.11.3.<br>3.0 Pulsar users should upgrade to at least 3.0.2.<br>3.1 Pulsar users should upgrade to at least 3.1.1.<br><div>Any users running Pulsar 2.8, 2.9, 2.10, and earlier should upgrade to one of the above patched versions.</div><div><br></div><p>For additional details on this attack vector, please refer to <a target="_blank" rel="nofollow" href="https://codahale.com/a-lesson-in-timing-attacks/">https://codahale.com/a-lesson-in-timing-attacks/</a>.</p>

### References
* https://lists.apache.org/thread/5kgmvvolf5tzp5rz9xjwfg2ncwvqqgl5


### Credits
* Yiheng Cao (finder)
* Chenhao Lu  (finder)
* Kaifeng Huang (finder)
