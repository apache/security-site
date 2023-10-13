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

## Incorrect Authorization Validation for Rest Producer ## { #CVE-2023-30428 }

CVE-2023-30428 [\[CVE json\]](./CVE-2023-30428.cve.json)

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


## Incorrect Authorization for Function Worker Can Leak Sink/Source Credentials ## { #CVE-2023-37579 }

CVE-2023-37579 [\[CVE json\]](./CVE-2023-37579.cve.json)

### Affected

* Apache Pulsar Function Worker before 2.10.4
* Apache Pulsar Function Worker at 2.11.0


### Description

Incorrect Authorization vulnerability in Apache Software Foundation Apache Pulsar Function Worker.<br><br>This issue affects Apache Pulsar: before 2.10.4, and 2.11.0.<br><br>Any authenticated user can retrieve a source's configuration or a sink's configuration without authorization. Many sources and sinks contain credentials in the configuration, which could lead to leaked credentials. This vulnerability is mitigated by the fact that there is not a known way for an authenticated user to enumerate another tenant's sources or sinks, meaning the source or sink name would need to be guessed in order to exploit this vulnerability.<br><br>The recommended mitigation for impacted users is to upgrade the Pulsar Function Worker to a patched version.<br><br>2.10 Pulsar Function Worker users should upgrade to at least 2.10.4.<br>2.11 Pulsar Function Worker users should upgrade to at least 2.11.1.<br>3.0 Pulsar Function Worker users are unaffected.<br>Any users running the Pulsar Function Worker for 2.9.* and earlier should upgrade to one of the above patched versions.<br><br>

### References
* https://lists.apache.org/thread/0dmn3cb5n2p08o3cpj3ycfhzfqs2ppwz


### Credits
* Michael Marshall of DataStax (finder)
