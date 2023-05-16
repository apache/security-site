---
title: Apache Spark security advisories
description: Security information for Apache Spark
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Spark? You can read more about the projects' security policy on their [security page](https://spark.apache.org/security.html), and email your report to the  [Apache Spark Security Team](mailto:security@spark.apache.org).

# Advisories

## Apache Spark proxy-user privilege escalation from malicious configuration class ## { #CVE-2023-22946 }

[CVE-2023-22946](./CVE-2023-22946.cve.json)

### Affected

* Apache Spark versions  before 3.4.0


### Description

<div>In Apache Spark versions prior to 3.4.0, applications using spark-submit can specify a 'proxy-user' to run as, limiting privileges. The application can execute code with the privileges of the submitting user, however, by providing malicious configuration-related classes on the classpath. This affects architectures relying on proxy-user, for example those using Apache Livy to manage submitted applications.</div><div>Update to Apache Spark 3.4.0 or later, and ensure that 
spark.submit.proxyUser.allowCustomClasspathInClusterMode is set to its 
default of "false", and is not overridden by submitted applications.<br></div>

## Shell command injection via Spark UI ## { #CVE-2023-32007 }

[CVE-2023-32007](./CVE-2023-32007.cve.json)

### Affected

* Apache Spark versions 3.1.1 before 3.2.2


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** The Apache Spark UI offers the possibility to enable ACLs via the configuration option spark.acls.enable. With an authentication filter, this checks whether a user has access permissions to view or modify the application. If ACLs are enabled, a code path in HttpSecurityFilter can allow someone to perform impersonation by providing an arbitrary user name. A malicious user might then be able to reach a permission check function that will ultimately build a Unix shell command based on their input, and execute it. This will result in arbitrary shell command execution as the user Spark is currently running as. This issue was disclosed earlier as CVE-2022-33891, but incorrectly claimed version 3.1.3 (which has since gone EOL) would not be affected.</div><div>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</div><div>Users are recommended to upgrade to a supported version of Apache Spark, such as version 3.4.0.<br></div>