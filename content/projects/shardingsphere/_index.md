---
title: Apache ShardingSphere security advisories
description: Security information for Apache ShardingSphere
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ShardingSphere? You can read more about the projects' security policy on their [security page](https://shardingsphere.apache.org/community/en/security/), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://shardingsphere.apache.org/community/en/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Deserialization of Untrusted Data ## { #CVE-2021-26558 }

CVE-2021-26558 [\[CVE json\]](./CVE-2021-26558.cve.json)

_Last updated: 2021-11-11T09:28:11.863Z_

### Affected

* Apache ShardingSphere-UI from 4.1.1 before Apache ShardingSphere-UI*


### Description

Deserialization of Untrusted Data vulnerability of Apache ShardingSphere-UI allows an attacker to inject outer link resources.  This issue affects Apache ShardingSphere-UI Apache ShardingSphere-UI version 4.1.1 and later versions; Apache ShardingSphere-UI versions prior to 5.0.0.

### References
* https://lists.apache.org/thread/4gzkm1zb6c97v9gl8lcz8ll5xr8o484c


## Access-Token in ElasticJob UI causes password disclosure ## { #CVE-2022-22733 }

CVE-2022-22733 [\[CVE json\]](./CVE-2022-22733.cve.json)

_Last updated: 2022-01-27T12:11:17.849Z_

### Affected

* Apache ShardingSphere ElasticJob-UI from Apache ShardingSphere ElasticJob-UI 3.x through 3.0.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache ShardingSphere ElasticJob-UI allows an attacker who has guest account to do privilege escalation. This issue affects Apache ShardingSphere ElasticJob-UI Apache ShardingSphere ElasticJob-UI 3.x version 3.0.0 and prior versions.

### References
* https://lists.apache.org/thread/qpdsm936n9bhksb0rzn6bq1h7ord2nm6


## Apache ShardingSphere ElasticJob-UI allows RCE via event trace data source JDBC ## { #CVE-2022-31764 }

CVE-2022-31764 [\[CVE json\]](./CVE-2022-31764.cve.json)

_Last updated: 2022-11-01T08:18:58.682Z_

### Affected

* Apache ShardingSphere ElasticJob-UI from Apache ShardingSphere ElasticJob-UI 3.x through 3.0.1


### Description

The Lite UI of Apache ShardingSphere ElasticJob-UI allows an attacker to perform RCE by constructing a special JDBC URL of H2 database. This issue affects Apache ShardingSphere ElasticJob-UI version 3.0.1 and prior versions. This vulnerability has been fixed in ElasticJob-UI 3.0.2.
The premise of this attack is that the attacker has obtained the account and password. Otherwise, the attacker cannot perform this attack.

## MySQL authentication bypass ## { #CVE-2022-45347 }

CVE-2022-45347 [\[CVE json\]](./CVE-2022-45347.cve.json)

_Last updated: 2023-02-15T02:21:01.314Z_

### Affected

* Apache ShardingSphere-Proxy before 5.3.0


### Description

Apache ShardingSphere-Proxy prior to 5.3.0 when using MySQL as database backend didn't cleanup the database session completely after client authentication failed, which allowed an attacker to execute normal commands by constructing a special MySQL client. This vulnerability has been fixed in Apache ShardingSphere 5.3.0.

### References
* https://lists.apache.org/thread/l5rz7j4rg10o7ywtgknh2f5hxnv6yw3l


### Credits
* smoking (finder)


## Deserialization vulnerability in ShardingSphere Agent ## { #CVE-2023-28754 }

CVE-2023-28754 [\[CVE json\]](./CVE-2023-28754.cve.json)

_Last updated: 2023-07-19T07:15:27.885Z_

### Affected

* ShardingSphere-Agent through 5.3.2


### Description

Deserialization of Untrusted Data vulnerability in Apache ShardingSphere-Agent, which allows attackers to execute arbitrary code by constructing a special YAML configuration file.<br><div></div><div></div><span style="background-color: var(--wht);"><div>The attacker needs to have permission to modify the ShardingSphere Agent YAML configuration file on the target machine, and the target machine can access the URL with the arbitrary code JAR.
An attacker can use SnakeYAML to deserialize java.net.URLClassLoader and make it load a JAR from a specified URL, and then deserialize javax.script.ScriptEngineManager to load code using that ClassLoader. When the ShardingSphere JVM process starts and uses the ShardingSphere-Agent, the arbitrary code specified by the attacker will be executed during the deserialization of the YAML configuration file by the Agent.</div>This issue affects ShardingSphere-Agent: through 5.3.2. This vulnerability is fixed in Apache ShardingSphere 5.4.0.</span>

### References
* https://lists.apache.org/thread/p8onhqox5kkwow9lc6gs03z28wtyp1cg


### Credits
* Liav Gutman of the JFrog CSO Research team (finder)
