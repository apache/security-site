---
title: Apache Spark security advisories
description: Security information for Apache Spark
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Spark? You can read more about the projects' security policy on their [security page](https://spark.apache.org/security.html), and email your report to the [Apache Spark Security Team](mailto:security@spark.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://spark.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Spark Key Negotiation Vulnerability ## { #CVE-2021-38296 }

CVE-2021-38296 [\[CVE json\]](./CVE-2021-38296.cve.json) [\[OSV json\]](./CVE-2021-38296.osv.json)



_Last updated: 2022-03-10T08:16:48.042Z_

### Affected

* Apache Spark from up to and including version 3.1.2 through 3.1.2


### Description

Apache Spark supports end-to-end encryption of RPC connections via "spark.authenticate" and "spark.network.crypto.enabled". In versions 3.1.2 and earlier, it uses a bespoke mutual authentication protocol that allows for full encryption key recovery. After an initial interactive attack, this would allow someone to decrypt plaintext traffic offline. Note that this does not affect security mechanisms controlled by "spark.authenticate.enableSaslEncryption", "spark.io.encryption.enabled", "spark.ssl", "spark.ui.strictTransportSecurity".  Update to Apache Spark 3.1.3 or later

### References
* https://lists.apache.org/thread/70x8fw2gx3g9ty7yk0f2f1dlpqml2smd


### Credits
* Steve Weis (Databricks)


## Apache Spark XSS vulnerability in log viewer UI Javascript ## { #CVE-2022-31777 }

CVE-2022-31777 [\[CVE json\]](./CVE-2022-31777.cve.json) [\[OSV json\]](./CVE-2022-31777.osv.json)



_Last updated: 2022-11-01T15:31:47.242Z_

### Affected

* Apache Spark at 3.3.0
* Apache Spark from 3.2.1 and earlier through 3.2.1


### Description

A stored cross-site scripting (XSS) vulnerability in Apache Spark 3.2.1 and earlier, and 3.3.0, allows remote attackers to execute arbitrary JavaScript in the web browser of a user, by including a malicious payload into the logs which would be returned in logs rendered in the UI.

### References
* https://lists.apache.org/thread/60mgbswq2lsmrxykfxpqq13ztkm2ht6q


### Credits
* Florian Walter (Veracode)


## Apache Spark shell command injection vulnerability via Spark UI ## { #CVE-2022-33891 }

CVE-2022-33891 [\[CVE json\]](./CVE-2022-33891.cve.json) [\[OSV json\]](./CVE-2022-33891.osv.json)



_Last updated: 2022-07-18T06:58:42.467Z_

### Affected

* Apache Spark from 3.0.3 and earlier through 3.0.3
* Apache Spark from 3.1.1 to 3.1.2 through 3.1.2
* Apache Spark from 3.2.0 to 3.2.1 through 3.2.1


### Description

The Apache Spark UI offers the possibility to enable ACLs via the configuration option spark.acls.enable. With an authentication filter, this checks whether a user has access permissions to view or modify the application. If ACLs are enabled, a code path in HttpSecurityFilter can allow someone to perform impersonation by providing an arbitrary user name. A malicious user might then be able to reach a permission check function that will ultimately build a Unix shell command based on their input, and execute it. This will result in arbitrary shell command execution as the user Spark is currently running as. This affects Apache Spark versions 3.0.3 and earlier, versions 3.1.1 to 3.1.2, and versions 3.2.0 to 3.2.1.

### References
* https://lists.apache.org/thread/p847l3kopoo5bjtmxrcwk21xp6tjxqlc


### Credits
*  Kostya Kortchinsky (Databricks)


## Apache Spark proxy-user privilege escalation from malicious configuration class ## { #CVE-2023-22946 }

CVE-2023-22946 [\[CVE json\]](./CVE-2023-22946.cve.json) [\[OSV json\]](./CVE-2023-22946.osv.json)



_Last updated: 2023-04-17T07:30:17.426Z_

### Affected

* Apache Spark before 3.4.0


### Description

<div>In Apache Spark versions prior to 3.4.0, applications using spark-submit can specify a 'proxy-user' to run as, limiting privileges. The application can execute code with the privileges of the submitting user, however, by providing malicious configuration-related classes on the classpath. This affects architectures relying on proxy-user, for example those using Apache Livy to manage submitted applications.</div><div>Update to Apache Spark 3.4.0 or later, and ensure that 
spark.submit.proxyUser.allowCustomClasspathInClusterMode is set to its 
default of "false", and is not overridden by submitted applications.<br></div>

### References
* https://lists.apache.org/thread/yllfl25xh5tbotjmg93zrq4bzwhqc0gv


### Credits
* Hideyuki Furue (finder)
* Yi Wu (Databricks) (remediation developer)


## Shell command injection via Spark UI ## { #CVE-2023-32007 }

CVE-2023-32007 [\[CVE json\]](./CVE-2023-32007.cve.json) [\[OSV json\]](./CVE-2023-32007.osv.json)



_Last updated: 2023-05-02T08:37:02.283Z_

### Affected

* Apache Spark from 3.1.1 before 3.2.2


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** The Apache Spark UI offers the possibility to enable ACLs via the configuration option spark.acls.enable. With an authentication filter, this checks whether a user has access permissions to view or modify the application. If ACLs are enabled, a code path in HttpSecurityFilter can allow someone to perform impersonation by providing an arbitrary user name. A malicious user might then be able to reach a permission check function that will ultimately build a Unix shell command based on their input, and execute it. This will result in arbitrary shell command execution as the user Spark is currently running as. This issue was disclosed earlier as CVE-2022-33891, but incorrectly claimed version 3.1.3 (which has since gone EOL) would not be affected.</div><div>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</div><div>Users are recommended to upgrade to a supported version of Apache Spark, such as version 3.4.0.<br></div>

### References
* https://www.cve.org/CVERecord?id=CVE-2022-33891
* https://spark.apache.org/security.html
* https://lists.apache.org/thread/poxgnxhhnzz735kr1wos366l5vdbb0nv


### Credits
* Sven Krewitt, Flashpoint (reporter)
