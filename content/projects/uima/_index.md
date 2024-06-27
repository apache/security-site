---
title: Apache UIMA security advisories
description: Security information for Apache UIMA
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache UIMA? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache UIMA prior to 3.3.1 has a path traversal vulnerability when extracting (PEAR) archives ## { #CVE-2022-32287 }

CVE-2022-32287 [\[CVE json\]](./CVE-2022-32287.cve.json) [\[OSV json\]](./CVE-2022-32287.osv.json)



_Last updated: 2022-11-03T11:49:10.523Z_

### Affected

* Apache UIMA from Java SDK through 3.3.0


### Description

A relative path traversal vulnerability in a FileUtil class used by the PEAR management component of Apache UIMA allows an attacker to create files outside the designated target directory using carefully crafted ZIP entry names. This issue affects Apache UIMA Apache UIMA version 3.3.0 and prior versions. 

Note that PEAR files should never be installed into an UIMA installation from untrusted sources because PEAR archives are executable plugins that will be able to perform any actions with the same privileges as the host Java Virtual Machine.

### References
* https://lists.apache.org/thread/57vk0d79j94d0lk0vol8xn935yv1shdd


### Credits
* Apache UIMA would like to thank Huangzhicong from CodeSafe Team of Legendsec at Qi'anxin Group


## DUCC (EOL) allows RCE ## { #CVE-2023-28935 }

CVE-2023-28935 [\[CVE json\]](./CVE-2023-28935.cve.json) [\[OSV json\]](./CVE-2023-28935.osv.json)



_Last updated: 2023-03-30T09:10:09.175Z_

### Affected

* Apache UIMA DUCC through *


### Description

<div>** UNSUPPORTED WHEN ASSIGNED ** Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache UIMA DUCC.<br></div><div>When using the "Distributed UIMA Cluster Computing" (DUCC) module of Apache UIMA, an authenticated user that has the permissions to modify core entities can cause command execution as the system user that runs the web process.<br></div><div>As the "Distributed UIMA Cluster Computing" module for UIMA is retired, we do not plan to release a fix for this issue.<br>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</div>

### References
* https://lists.apache.org/thread/r19z14b9rrfxv72r93q5trq5tyffo75g


### Credits
* Crilwa (finder)


## Potential untrusted code execution when deserializing certain binary CAS formats ## { #CVE-2023-39913 }

CVE-2023-39913 [\[CVE json\]](./CVE-2023-39913.cve.json) [\[OSV json\]](./CVE-2023-39913.osv.json)



_Last updated: 2023-11-08T08:04:19.712Z_

### Affected

* Apache UIMA Java SDK Core before 3.5.0
* Apache UIMA Java SDK CPE before 3.5.0
* Apache UIMA Java SDK Vinci adapter before 3.5.0
* Apache UIMA Java SDK tools before 3.5.0


### Description

Deserialization of Untrusted Data, Improper Input Validation vulnerability in Apache UIMA Java SDK, Apache UIMA Java SDK, Apache UIMA Java SDK, Apache UIMA Java SDK.<p>This issue affects Apache UIMA Java SDK: before 3.5.0.</p><p>Users are recommended to upgrade to version 3.5.0, which fixes the issue.</p>There are several locations in the code where serialized Java objects are deserialized without verifying the data. This affects in particular:<br><ul><li><span style="background-color: var(--wht);">the deserialization of a Java-serialized CAS, but also other binary CAS formats that include TSI information using the CasIOUtils class;</span></li><li><span style="background-color: var(--wht);">the CAS Editor Eclipse plugin which uses the&nbsp;the CasIOUtils class to load data;</span></li><li><span style="background-color: var(--wht);">the deserialization of a Java-serialized CAS of the Vinci Analysis Engine service which can receive using Java-serialized CAS objects over network connections;</span></li><li><span style="background-color: var(--wht);">the CasAnnotationViewerApplet and the CasTreeViewerApplet;</span></li><li><span style="background-color: var(--wht);">the checkpointing feature of the CPE module.</span></li></ul>Note that the UIMA framework by default does not start any remotely accessible services (i.e. Vinci) that would be vulnerable to this issue. A user or developer would need to make an active choice to start such a service. However, users or developers may use the CasIOUtils in their own applications and services to parse serialized CAS data. They are affected by this issue unless they ensure that the data passed to CasIOUtils is <b>not</b> a serialized Java object.<br><br>When using Vinci or using CasIOUtils in own services/applications,&nbsp;<span style="background-color: rgb(255, 255, 255);">the unrestricted deserialization of Java-serialized CAS files may allow arbitrary (remote) code execution.</span><br><br>As a remedy, it is possible to set up a global or context-specific ObjectInputFilter (cf. <a target="_blank" rel="nofollow" href="https://openjdk.org/jeps/290">https://openjdk.org/jeps/290</a>&nbsp;and&nbsp;<a target="_blank" rel="nofollow" href="https://openjdk.org/jeps/415">https://openjdk.org/jeps/415</a>) if running UIMA on a Java version that supports it. <br><br>Note that Java 1.8 does not support the ObjectInputFilter, so there is no remedy when running on this out-of-support platform. An upgrade to a recent Java version is strongly recommended if you need to secure an UIMA version that is affected by this issue.<br><br>To mitigate the issue on a Java 9+ platform, you can configure a filter pattern through the <i>"jdk.serialFilter"</i> system property using a semicolon as a separator:<br><br>To allow deserializing Java-serialized binary CASes, add the classes:<br><ul><li><span style="background-color: var(--wht);">org.apache.uima.cas.impl.CASCompleteSerializer</span></li><li>org.apache.uima.cas.impl.CASMgrSerializer</li><li>org.apache.uima.cas.impl.CASSerializer</li><li>java.lang.String</li></ul>To allow deserializing CPE Checkpoint data, add the following classes (and any custom classes your application uses to store its checkpoints):<br><ul><li>org.apache.uima.collection.impl.cpm.CheckpointData</li><li>org.apache.uima.util.ProcessTrace</li><li>org.apache.uima.util.impl.ProcessTrace_impl</li><li>org.apache.uima.collection.base_cpm.SynchPoint</li></ul>Make sure to use "!*" as the final component to the filter pattern to disallow deserialization of any classes not listed in the pattern.<br><br>Apache UIMA 3.5.0 uses tightly scoped ObjectInputFilters when reading Java-serialized data depending on the type of data being expected. Configuring a global filter is not necessary with this version.<br><br>

### References
* https://lists.apache.org/thread/lw30f4qlq3mhkhpljj16qw4fot3rg7v4


### Credits
* Huangzhicong from CodeSafe Team of Legendsec at Qi’anxin (reporter)
