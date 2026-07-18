---
title: Apache Kafka security advisories
description: Security information for Apache Kafka
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Kafka? Send your report to the [Apache Kafka Security Team](mailto:security@kafka.apache.org?subject=Kafka).

You can read more about the security policy on:

- [Apache Kafka security model](https://kafka.apache.org/project-security.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improper Authorization in CONSUMER_GROUP_DESCRIBE API ## { #CVE-2026-41115 }

CVE-2026-41115 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41115) [\[CVE json\]](./CVE-2026-41115.cve.json) [\[OSV json\]](./CVE-2026-41115.osv.json)



_Last updated: 2026-06-02T08:56:41.838Z_

### Affected

* Apache Kafka from 4.0.0 through 4.3.0


### Description

<div>An improper authorization vulnerability has been identified in Apache Kafka.</div><div>The implementation of the CONSUMER_GROUP_DESCRIBE (69) API validates the DESCRIBE operation on the GROUP resource instead of the READ operation that documented in the official kafka documentation and the KIP-848. This discrepancy can result in misconfigured Access Control Lists (ACLs) and unintended security postures, like granting READ permission to users who should not be able to join/sync groups, or allowing users without READ permission (but with DESCRIBE permission) to access sensitive group metadata.<br><br>The correct permission for CONSUMER_GROUP_DESCRIBE API is DESCRIBE GROUP so the current implementation is correct. However, the kafka documentation as well as the KIP-848 will be updated to reflect the correct permission. We advise the Kafka users to review existing group ACLs to ensure the principle of least privilege.</div><div><br></div>

### References
* https://kafka.apache.org/cve-list


### Credits
* Luke Chen <showuon@gmail.com> (finder)


## Kafka Producer Message Corruption and Misrouting via Buffer Pool Race Condition ## { #CVE-2026-35554 }

CVE-2026-35554 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-35554) [\[CVE json\]](./CVE-2026-35554.cve.json) [\[OSV json\]](./CVE-2026-35554.osv.json)



_Last updated: 2026-04-07T13:07:01.788Z_

### Affected

* Apache Kafka Clients from 2.8.0 through 3.9.1
* Apache Kafka Clients from 4.0.0 through 4.0.1
* Apache Kafka Clients from 4.1.0 through 4.1.1


### Description

<p></p><p>A race condition in the <strong>Apache Kafka Java producer client’s buffer pool management</strong> can cause messages to be silently delivered to incorrect topics.</p><p>When a produce batch expires due to <code>delivery.timeout.ms</code> while a network request containing that batch is still in flight, the batch’s <code>ByteBuffer</code> is prematurely deallocated and returned to the buffer pool. If a subsequent producer batch—potentially destined for a different topic—reuses this freed buffer before the original network request completes, the buffer contents may become corrupted. This can result in messages being delivered to unintended topics without any error being reported to the producer.<br></p><p><strong>Data Confidentiality:</strong><br>Messages intended for one topic may be delivered to a different topic, potentially exposing sensitive data to consumers who have access to the destination topic but not the intended source topic.</p><p><strong>Data Integrity:</strong><br>Consumers on the receiving topic may encounter unexpected or incompatible messages, leading to deserialization failures, processing errors, and corrupted downstream data.</p><p>This issue affects <strong>Apache Kafka versions ≤ 3.9.1, ≤ 4.0.1, and&nbsp; ≤ 4.1.1</strong>.</p><p>Kafka users are advised to upgrade to <strong>3.9.2, 4.0.2, 4.1.2, 4.2.0, or later</strong> to address this vulnerability.</p><br><p></p>

### References
* https://issues.apache.org/jira/browse/KAFKA-19012
* https://lists.apache.org/thread/f07x7j8ovyqhjd1to25jsnqbm6wj01d6


### Credits
* Bharath Vissapragada <bharathv@apache.org> (reporter)
* Donny Nadolny <donny.nadolny@hotmail.com> (finder)
* Donny Nadolny <donny.nadolny@hotmail.com> (remediation developer)


## Information Exposure Through Network Client Log Output ## { #CVE-2026-33558 }

CVE-2026-33558 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33558) [\[CVE json\]](./CVE-2026-33558.cve.json) [\[OSV json\]](./CVE-2026-33558.osv.json)



_Last updated: 2026-04-18T14:13:55.292Z_

### Affected

* Apache Kafka from 0.11.0 through 3.9.1
* Apache Kafka at 4.0.0
* Apache Kafka Clients from 0.11.0 through 3.9.1
* Apache Kafka Clients at 4.0.0


### Description

<div>Information exposure vulnerability has been identified in Apache Kafka.</div><div>The NetworkClient component will output entire requests and responses information in the DEBUG log level in the logs. By default, the log level is set to INFO level. If the DEBUG level is enabled, the sensitive information will be exposed via the requests and responses output log. The entire lists of impacted requests and responses are:</div><div><ol>
<li>AlterConfigsRequest</li>
<li>AlterUserScramCredentialsRequest</li>
<li>ExpireDelegationTokenRequest</li>
<li>IncrementalAlterConfigsRequest</li>
<li>RenewDelegationTokenRequest</li>
<li>SaslAuthenticateRequest</li>
<li>createDelegationTokenResponse</li>
<li>describeDelegationTokenResponse</li>
<li>SaslAuthenticateResponse</li>
</ol><br>This issue affects Apache Kafka: from any version supported the listed API above through v3.9.1, v4.0.0. We advise the Kafka users to upgrade to v3.9.2, v4.0.1, or later to avoid this vulnerability.&nbsp;&nbsp;<br><br></div>

### References
* https://kafka.apache.org/cve-list
* https://lists.apache.org/thread/pz5g4ky3h0k91tfd14p0dzqjp80960kl


### Credits
* Alyssa Huang <ahuang@confluent.io> (finder)
* Luke Chen <showuon@gmail.com> (finder)


## Missing JWT token validation in OAUTHBEARER authentication ## { #CVE-2026-33557 }

CVE-2026-33557 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33557) [\[CVE json\]](./CVE-2026-33557.cve.json) [\[OSV json\]](./CVE-2026-33557.osv.json)



_Last updated: 2026-04-18T14:14:44.004Z_

### Affected

* Apache Kafka from 4.1.0 through 4.1.1


### Description

<div>A possible security vulnerability has been identified in Apache Kafka.</div><div>By default, the broker property `sasl.oauthbearer.jwt.validator.class` is&nbsp;set to `org.apache.kafka.common.security.oauthbearer.DefaultJwtValidator`. It accepts any JWT token without validating its&nbsp;signature, issuer, or audience. An attacker can generate a JWT&nbsp;token from any issuer with the `preferred_username` set to any user, and the broker will accept it.</div><div>We advise the Kafka users using kafka v4.1.0 or v4.1.1 to set the config `sasl.oauthbearer.jwt.validator.class` to `org.apache.kafka.common.security.oauthbearer.BrokerJwtValidator` explicitly to avoid this vulnerability. Since Kafka v4.1.2 and v4.2.0 and later, the issue is fixed and will correctly validate the JWT token.</div><br>

### References
* https://kafka.apache.org/cve-list
* https://lists.apache.org/thread/v57o00hm6yszdpdnvqx2ss4561yh953h


### Credits
* Павел Романов <promanov1994@gmail.com> (finder)


## Possible RCE/Denial of service attack via SASL JAAS JndiLoginModule configuration ## { #CVE-2025-27819 }

CVE-2025-27819 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27819) [\[CVE json\]](./CVE-2025-27819.cve.json) [\[OSV json\]](./CVE-2025-27819.osv.json)



_Last updated: 2025-06-10T07:54:40.206Z_

### Affected

* Apache Kafka from 2.0.0 through 3.3.2


### Description

<div>In CVE-2023-25194, we announced the RCE/Denial of service attack via SASL JAAS JndiLoginModule configuration in Kafka Connect API. But not only Kafka Connect API is vulnerable to this attack, the Apache Kafka brokers also have this vulnerability. To exploit this vulnerability, the attacker needs to be able to connect to the Kafka cluster and have the AlterConfigs permission on the cluster resource.</div><div><br>Since Apache Kafka 3.4.0, we have added a system property ("-Dorg.apache.kafka.disallowed.login.modules") to disable the problematic login modules usage in SASL JAAS configuration. Also by default "com.sun.security.auth.module.JndiLoginModule" is disabled in Apache Kafka 3.4.0, and "com.sun.security.auth.module.JndiLoginModule,com.sun.security.auth.module.LdapLoginModule" is disabled by default in in Apache Kafka 3.9.1/4.0.0<br></div>

### References
* https://kafka.apache.org/cve-list


### Credits
* Ziyang Li (finder)
* Ji'an Zhou (finder)
* Ying Zhu (finder)


## Possible RCE attack via SASL JAAS LdapLoginModule configuration ## { #CVE-2025-27818 }

CVE-2025-27818 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27818) [\[CVE json\]](./CVE-2025-27818.cve.json) [\[OSV json\]](./CVE-2025-27818.osv.json)



_Last updated: 2025-06-10T07:53:14.155Z_

### Affected

* Apache Kafka from 2.3.0 through 3.9.0


### Description

A possible security vulnerability has been identified in Apache Kafka.<br>This requires access to a alterConfig to the&nbsp;cluster resource, or Kafka Connect worker, and the ability to create/modify connectors on it with an arbitrary Kafka client SASL JAAS config<br>and a SASL-based security protocol, which has been possible on Kafka clusters since Apache Kafka 2.0.0 (Kafka Connect 2.3.0).<br>When configuring the broker via config file or AlterConfig command, or connector via the Kafka Kafka Connect REST API, an <span style="background-color: rgb(255, 255, 255);">authenticated operator</span>&nbsp;can set the <span style="background-color: rgb(255, 255, 255);">`sasl.jaas.config`<br></span>property for any of the connector's Kafka clients to "com.sun.security.auth.module.LdapLoginModule", which can be done via the<br>`producer.override.sasl.jaas.config`, `consumer.override.sasl.jaas.config`, or `admin.override.sasl.jaas.config` properties.<br>This will allow the server to connect to the attacker's LDAP server<br>and deserialize the LDAP response, which the attacker can use to execute java deserialization gadget chains on the Kafka connect server.<br>Attacker can cause <span style="background-color: rgb(255, 255, 255);">unrestricted deserialization of untrusted data (or) </span>RCE vulnerability when there are gadgets in the classpath.<br><br>Since Apache Kafka 3.0.0, users are allowed to specify these properties in connector configurations for Kafka Connect clusters running with out-of-the-box<br>configurations. Before Apache Kafka 3.0.0, users may not specify these properties unless the Kafka Connect cluster has been reconfigured with a connector<br>client override policy that permits them.<br><br>Since Apache Kafka 3.9.1/4.0.0, we have added a system property ("-Dorg.apache.kafka.disallowed.login.modules") to disable the problematic login modules usage<br>in SASL JAAS configuration. Also by default "com.sun.security.auth.module.JndiLoginModule,com.sun.security.auth.module.LdapLoginModule" are disabled in Apache Kafka Connect 3.9.1/4.0.0. <br><br>We advise the Kafka users to validate connector configurations and only allow trusted LDAP configurations. Also examine connector dependencies for <br>vulnerable versions and either upgrade their connectors, upgrading that specific dependency, or removing the connectors as options for remediation. Finally,<br><span style="background-color: rgb(255, 255, 255);">in addition to leveraging the "org.apache.kafka.disallowed.login.modules" system property, Kafka Connect users can also implement their own connector<br>client config override policy, which can be used to control which Kafka client properties can be overridden directly in a connector config and which cannot.</span><br><br>

### References
* https://kafka.apache.org/cve-list


### Credits
* 罗鑫 <lx2317103712@gmail.com> (finder)
* ra1lgun <ra1lgun@foxmail.com> (finder)


## Arbitrary file read and SSRF vulnerability ## { #CVE-2025-27817 }

CVE-2025-27817 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27817) [\[CVE json\]](./CVE-2025-27817.cve.json) [\[OSV json\]](./CVE-2025-27817.osv.json)



_Last updated: 2025-06-10T07:55:12.969Z_

### Affected

* Apache Kafka Client from 3.1.0 through 3.9.0


### Description

<div>A possible arbitrary file read and SSRF vulnerability has been identified in Apache Kafka Client. Apache Kafka Clients accept configuration data for setting the SASL/OAUTHBEARER connection with the brokers, including "sasl.oauthbearer.token.endpoint.url" and "sasl.oauthbearer.jwks.endpoint.url". Apache Kafka allows clients to read an arbitrary file and return the content in the error log, or sending requests to an unintended location. In applications where Apache Kafka Clients configurations can be specified by an untrusted party, attackers may use the "sasl.oauthbearer.token.endpoint.url" and "sasl.oauthbearer.jwks.endpoint.url" configuratin to read arbitrary contents of the disk and environment variables or make requests to an unintended location. In particular, this flaw may be used in Apache Kafka Connect to escalate from REST API access to filesystem/environment/URL access, which may be undesirable in certain environments, including SaaS products. </div><p>Since Apache Kafka 3.9.1/4.0.0, we have added a system property ("-Dorg.apache.kafka.sasl.oauthbearer.allowed.urls") to set the allowed urls in SASL JAAS configuration. In 3.9.1, it accepts all urls by default for backward compatibility. However in 4.0.0 and newer, the default value is empty list and users have to set the allowed urls explicitly.<br></p>

      <br>

### References
* https://kafka.apache.org/cve-list


### Credits
* 罗鑫 <lx2317103712@gmail.com> (finder)
* 1ue (https://github.com/luelueking) (finder)
* 4ra1n (https://github.com/4ra1n) (finder)
* enokiy <846800628@qq.com> (finder)
* VulTeam of ThreatBook (finder)


## SCRAM authentication vulnerable to replay attacks when used without encryption ## { #CVE-2024-56128 }

CVE-2024-56128 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-56128) [\[CVE json\]](./CVE-2024-56128.cve.json)

_Last updated: 2024-12-18T13:38:00.297Z_

### Affected

* Apache Kafka from 0.10.2.0 before 3.7.2
* Apache Kafka at 3.8.0


### Description

<p>Incorrect Implementation of Authentication Algorithm in Apache Kafka's SCRAM implementation.<br><br>Issue Summary:<br>Apache Kafka's implementation of the Salted Challenge Response Authentication Mechanism (SCRAM) did not fully adhere to the requirements of RFC 5802 [1].<br>Specifically, as per RFC 5802, the server must verify that the nonce sent by the client in the second message matches the nonce sent by the server in its first message.<br>However, Kafka's SCRAM implementation did not perform this validation.<br><br>Impact:<br>This vulnerability is exploitable only when an attacker has plaintext access to the SCRAM authentication exchange. However, the usage of SCRAM over plaintext is strongly<br>discouraged as it is considered an insecure practice [2]. Apache Kafka recommends deploying SCRAM exclusively with TLS encryption to protect SCRAM exchanges from interception [3].<br>Deployments using SCRAM with TLS are not affected by this issue.</p>How to Detect If You Are Impacted:<br>If your deployment uses SCRAM authentication over plaintext communication channels (without TLS encryption), you are likely impacted.<br>To check if TLS is enabled, review your server.properties configuration file for listeners property. If you have SASL_PLAINTEXT in the listeners, then you are likely impacted.<br><br><span style="background-color: var(--wht);">Fix Details:<br></span><span style="background-color: var(--wht);">The issue has been addressed by introducing nonce verification in the final message of the SCRAM authentication exchange to ensure compliance with RFC 5802.<br><br></span><span style="background-color: var(--wht);">Affected Versions:<br></span><span style="background-color: var(--wht);">Apache Kafka versions 0.10.2.0 through 3.9.0, excluding the fixed versions below.<br><br></span><span style="background-color: var(--wht);">Fixed Versions:<br></span><span style="background-color: var(--wht);">3.9.0<br></span><span style="background-color: var(--wht);">3.8.1<br></span><span style="background-color: var(--wht);">3.7.2<br><br></span><span style="background-color: var(--wht);">Users are advised to upgrade to 3.7.2 or later to mitigate this issue.<br><br></span><span style="background-color: var(--wht);">Recommendations for Mitigation:<br></span><span style="background-color: var(--wht);">Users unable to upgrade to the fixed versions can mitigate the issue by:<br></span><span style="background-color: var(--wht);">- Using TLS with SCRAM Authentication:<br></span><span style="background-color: var(--wht);">Always deploy SCRAM over TLS to encrypt authentication exchanges and protect against interception.<br></span><span style="background-color: var(--wht);">- Considering Alternative Authentication Mechanisms:<br></span><span style="background-color: var(--wht);">Evaluate alternative authentication mechanisms, such as PLAIN, Kerberos or OAuth with TLS, which provide additional layers of security.</span><br>

### References
* https://datatracker.ietf.org/doc/html/rfc5802
* https://datatracker.ietf.org/doc/html/rfc5802#section-9
* https://kafka.apache.org/documentation/#security_sasl_scram_security
* https://lists.apache.org/thread/84dh4so32lwn7wr6c5s9mwh381vx9wkw


### Credits
* Tim Fox (timvolpe@gmail.com) (finder)
* Vikas Singh <vikas@confluent.io> (remediation developer)


## Privilege escalation to filesystem read-access via automatic ConfigProvider ## { #CVE-2024-31141 }

CVE-2024-31141 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-31141) [\[CVE json\]](./CVE-2024-31141.cve.json) [\[OSV json\]](./CVE-2024-31141.osv.json)



_Last updated: 2024-11-19T08:40:15.880Z_

### Affected

* Apache Kafka Clients from 2.3.0 through 3.5.2
* Apache Kafka Clients from 3.6.0 through 3.6.2
* Apache Kafka Clients at 3.7.0


### Description

Files or Directories Accessible to External Parties, Improper Privilege Management vulnerability in Apache Kafka Clients.<br><br>Apache Kafka Clients accept configuration data for customizing behavior, and includes ConfigProvider plugins in order to manipulate these configurations. Apache Kafka also provides FileConfigProvider, DirectoryConfigProvider, and EnvVarConfigProvider implementations which include the ability to read from disk or environment variables.<br>In applications where Apache Kafka Clients configurations can be specified by an untrusted party, attackers may use these ConfigProviders to read arbitrary contents of the disk and environment variables.<br><br>In particular, this flaw may be used in Apache Kafka Connect to escalate from REST API access to filesystem/environment access, which may be undesirable in certain environments, including SaaS products.<br><p>This issue affects Apache Kafka Clients: from 2.3.0 through 3.5.2, 3.6.2, 3.7.0.<br></p><p>Users with affected applications are recommended to upgrade kafka-clients to version &gt;=3.8.0, and set the JVM system property "org.apache.kafka.automatic.config.providers=none".<br>Users of Kafka Connect with one of the listed ConfigProvider implementations specified in their worker config are also recommended to add appropriate "allowlist.pattern" and "allowed.paths" to restrict their operation to appropriate bounds.<br></p>For users of Kafka Clients or Kafka Connect in environments that trust users with disk and environment variable access, it is not recommended to set the system property.<br><span style="background-color: var(--wht);">For users of the Kafka Broker, Kafka MirrorMaker 2.0, Kafka Streams, and Kafka command-line tools, it is not recommended to set the system property.<br></span>

### References
* https://lists.apache.org/thread/9whdzfr0zwdhr364604w5ssnzmg4v2lv


### Credits
* Greg Harris (finder)
* Mickael Maison (remediation reviewer)
* Chris Egerton (remediation reviewer)


## Potential incorrect access control during migration from ZK mode to KRaft mode ## { #CVE-2024-27309 }

CVE-2024-27309 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-27309) [\[CVE json\]](./CVE-2024-27309.cve.json) [\[OSV json\]](./CVE-2024-27309.osv.json)



_Last updated: 2024-04-12T06:58:42.007Z_

### Affected

* Apache Kafka from 3.5.0 through 3.5.2
* Apache Kafka from 3.6.0 through 3.6.1


### Description

<div><div><div><div><div><div><div><div><div><div><div><div>While an Apache Kafka cluster is being migrated from ZooKeeper mode to KRaft mode, in some cases ACLs will not be correctly enforced.</div><div><br>Two preconditions are needed to trigger the bug:<br>1. The administrator decides to remove an ACL<br>2. The resource associated with the removed ACL continues to have two or more other ACLs associated with it after the removal.<br><br>When those two preconditions are met, Kafka will treat the resource as if it had only one ACL associated with it after the removal, rather than the two or more that would be correct.</div><br><div>The incorrect condition is cleared by removing all brokers in ZK mode, or by adding a new ACL to the affected resource. Once the migration is completed, there is no metadata loss (the ACLs all remain).</div><br><div>The full impact depends on the ACLs in use. If only ALLOW ACLs were configured during the migration, the impact would be limited to availability impact. if DENY ACLs were configured, the impact could include confidentiality and integrity impact depending on the ACLs configured, as the DENY ACLs might be ignored due to this vulnerability during the migration period.</div></div></div></div></div></div></div></div></div></div></div></div><div><div><div><div><div><div></div></div></div></div></div></div>

### References
* https://lists.apache.org/thread/6536rmzyg076lzzdw2xdktvnz163mjpy


## Possible RCE/Denial of service attack via SASL JAAS JndiLoginModule configuration using Kafka Connect  ## { #CVE-2023-25194 }

CVE-2023-25194 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-25194) [\[CVE json\]](./CVE-2023-25194.cve.json)

_Last updated: 2023-07-21T11:35:22.991Z_

### Affected

* Apache Kafka Connect API from 2.3.0 before 3.4.0


### Description

A possible security vulnerability has been identified in Apache Kafka Connect API.<br>This requires access to a Kafka Connect worker, and the ability to create/modify connectors on it with an arbitrary Kafka client SASL JAAS config<br>and a SASL-based security protocol, which has been possible on Kafka Connect clusters since Apache Kafka Connect 2.3.0.<br>When configuring the connector via the Kafka Connect REST API, an&nbsp;<span style="background-color: rgb(255, 255, 255);">authenticated operator</span>&nbsp;can set the <span style="background-color: rgb(255, 255, 255);">`sasl.jaas.config`<br></span>property for any of the connector's Kafka clients&nbsp;to "com.sun.security.auth.module.JndiLoginModule", which can be done via the<br>`producer.override.sasl.jaas.config`, `consumer.override.sasl.jaas.config`, or `admin.override.sasl.jaas.config` properties.<br>This will allow the server to connect to the attacker's LDAP server<br>and deserialize the LDAP response, which the attacker can use to execute java deserialization gadget chains on the Kafka connect server.<br>Attacker can cause <span style="background-color: rgb(255, 255, 255);">unrestricted deserialization of untrusted data (or)&nbsp;</span>RCE vulnerability when there are gadgets in the classpath.<br><br>Since Apache Kafka 3.0.0, users are allowed to specify these properties in connector configurations for Kafka Connect clusters running with out-of-the-box<br>configurations. Before Apache Kafka 3.0.0, users may not specify these properties unless the Kafka Connect cluster has been reconfigured with a connector<br>client override policy that permits them.<br><br>Since Apache Kafka 3.4.0, we have added a system property ("-Dorg.apache.kafka.disallowed.login.modules") to disable the problematic login modules usage<br>in SASL JAAS configuration. Also by default "com.sun.security.auth.module.JndiLoginModule" is disabled in Apache Kafka Connect 3.4.0. <br><br>We advise the Kafka Connect users to validate connector configurations and only allow trusted JNDI configurations. Also examine connector dependencies for <br>vulnerable versions and either upgrade their connectors, upgrading that specific dependency, or removing the connectors as options for remediation. Finally,<br><span style="background-color: rgb(255, 255, 255);">in addition to leveraging the "org.apache.kafka.disallowed.login.modules" system property, Kafka Connect users can also implement their own connector<br>client config override policy, which can be used to control which Kafka client properties can be overridden directly in a connector config and which cannot.</span><br>

### References
* https://kafka.apache.org/cve-list
* https://lists.apache.org/thread/vy1c7fqcdqvq5grcqp6q5jyyb302khyz
* http://packetstormsecurity.com/files/173151/Apache-Druid-JNDI-Injection-Remote-Code-Execution.html


### Credits
* Apache Kafka would like to thank to Jari Jääskelä (https://hackerone.com/reports/1529790) and 4ra1n and Y4tacker (they found vulnerabilities in other Apache projects. After discussion between PMC of the two projects, it was finally confirmed that it was the vulnerability of Kafka then they reported it to us) (finder)


## Unauthenticated clients may cause OutOfMemoryError on Apache Kafka Brokers ## { #CVE-2022-34917 }

CVE-2022-34917 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-34917) [\[CVE json\]](./CVE-2022-34917.cve.json) [\[OSV json\]](./CVE-2022-34917.osv.json)



_Last updated: 2022-09-30T05:44:20.899Z_

### Affected

* Apache Kafka at Apache Kafka 2.8.0 2.8.0 
* Apache Kafka at Apache Kafka 2.8.1 2.8.1
* Apache Kafka at Apache Kafka 3.0.0 3.0.0
* Apache Kafka at Apache Kafka 3.0.1 3.0.1
* Apache Kafka at Apache Kafka 3.1.0 3.1.0
* Apache Kafka at Apache Kafka 3.1.1 3.1.1
* Apache Kafka at Apache Kafka 3.2.0 3.2.0
* Apache Kafka at Apache Kafka 3.2.1 3.2.1


### Description

A security vulnerability has been identified in Apache Kafka. It affects all releases since 2.8.0. The vulnerability allows malicious
unauthenticated clients to allocate large amounts of memory on brokers. This can lead to brokers hitting OutOfMemoryException and
causing denial of service.

Example scenarios:
- Kafka cluster without authentication: Any clients able to establish
a network connection to a broker can trigger the issue.
- Kafka cluster with SASL authentication: Any clients able to
establish a network connection to a broker, without the need for valid
SASL credentials, can trigger the issue.
- Kafka cluster with TLS authentication: Only clients able to
successfully authenticate via TLS can trigger the issue.

We advise the users to upgrade the Kafka installations to one of the 3.2.3, 3.1.2, 3.0.2, 2.8.2 versions.

### References
* https://kafka.apache.org/cve-list


### Credits
* Apache Kafka would like to thank Mickael Maison, Tom Bentley and Daniel Collins for reporting this issue.


## Timing Attack Vulnerability for Apache Kafka Connect and Clients ## { #CVE-2021-38153 }

CVE-2021-38153 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-38153) [\[CVE json\]](./CVE-2021-38153.cve.json) [\[OSV json\]](./CVE-2021-38153.osv.json)



_Last updated: 2021-09-22T08:43:16.777Z_

### Affected

* Apache Kafka from Apache Kafka 2.0.x through 2.0.1
* Apache Kafka from Apache Kafka 2.1.x through 2.1.1
* Apache Kafka from Apache Kafka 2.2.x through 2.2.2
* Apache Kafka from Apache Kafka 2.3.x through 2.3.1
* Apache Kafka from Apache Kafka 2.4.x through 2.4.1
* Apache Kafka from Apache Kafka 2.5.x through 2.5.1
* Apache Kafka from Apache Kafka 2.6.x through 2.6.2
* Apache Kafka from Apache Kafka 2.7.x through 2.7.1
* Apache Kafka from Apache Kafka 2.8.x through 2.8.0


### Description

Some components in Apache Kafka use `Arrays.equals` to validate a password or key, which is vulnerable to timing attacks that make brute force attacks for such credentials more likely to be successful. Users should upgrade to 2.8.1 or higher, or 3.0.0 or higher where this vulnerability has been fixed. The affected versions include Apache Kafka 2.0.0, 2.0.1, 2.1.0, 2.1.1, 2.2.0, 2.2.1, 2.2.2, 2.3.0, 2.3.1, 2.4.0, 2.4.1, 2.5.0, 2.5.1, 2.6.0, 2.6.1, 2.6.2, 2.7.0, 2.7.1, and 2.8.0.

### References
* https://kafka.apache.org/cve-list


### Credits
* Apache Kafka would like to thank J. Santilli for reporting this issue.
