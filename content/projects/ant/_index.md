---
title: Apache Ant security advisories
description: Security information for Apache Ant
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Ant? You can read more about the projects' security policy on their [security page](https://ant.apache.org/security.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://ant.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Ant TAR archive denial of service vulnerability ## { #CVE-2021-36373 }

CVE-2021-36373 [\[CVE json\]](./CVE-2021-36373.cve.json)

_Last updated: 2021-07-14T06:08:32.303Z_

### Affected

* Apache Ant from Apache Ant 1.9.x through 1.9.15
* Apache Ant from Apache Ant 1.10.x through 1.10.10
* Apache Ant from Apache Ant before 1.9.0


### Description

When reading a specially crafted TAR archive an Apache Ant build can be made to allocate large amounts of memory that finally leads to an out of memory error, even for small inputs. This can be used to disrupt builds using Apache Ant.
Apache Ant prior to 1.9.16 and 1.10.11 were affected.

### References
* https://ant.apache.org/security.html
* https://lists.apache.org/thread.html/r54afdab05e01de970649c2d91a993f68a6b00cd73e6e34e16c832d46%40%3Cuser.ant.apache.org%3E


### Credits
* This issue is similar to https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35517 present in Apache Commons Compress which has been detected by OSS Fuzz.


## Apache Ant ZIP, and ZIP based, archive denial of service vulnerability ## { #CVE-2021-36374 }

CVE-2021-36374 [\[CVE json\]](./CVE-2021-36374.cve.json) [\[OSV json\]](./CVE-2021-36374.osv.json)



_Last updated: 2021-07-19T07:37:04.488Z_

### Affected

* Apache Ant from 1.4 before Apache Ant*
* Apache Ant from Apache Ant 1.9.x through 1.9.15
* Apache Ant from Apache Ant 1.10.x through 1.10.10


### Description

When reading a specially crafted ZIP archive, or a derived formats, an Apache Ant build can be made to allocate large amounts of memory that leads to an out of memory error, even for small inputs. This can be used to disrupt builds using Apache Ant.

Commonly used derived formats from ZIP archives are for instance JAR files and many office files.  Apache Ant prior to 1.9.16 and 1.10.11 were affected.

### References
* https://ant.apache.org/security.html
* https://lists.apache.org/thread.html/rdd5412a5b9a25aed2a02c3317052d38a97128314d50bc1ed36e81d38%40%3Cuser.ant.apache.org%3E


### Credits
* This issue is similar to https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36090 present in Apache Commons Compress which has been detected by OSS Fuzz.


## Apache Ivy allows creating/overwriting any file on the system ## { #CVE-2022-37865 }

CVE-2022-37865 [\[CVE json\]](./CVE-2022-37865.cve.json) [\[OSV json\]](./CVE-2022-37865.osv.json)



_Last updated: 2022-11-07T10:53:07.179Z_

### Affected

* Apache Ivy from 2.4.0 before *


### Description

With Apache Ivy 2.4.0 an optional packaging attribute has been
introduced that allows artifacts to be unpacked on the fly if they used
pack200 or zip packaging.

For artifacts using the "zip", "jar" or "war" packaging Ivy prior to
2.5.1 doesn't verify the target path when extracting the archive. An
archive containing absolute paths or paths that try to traverse
"upwards" using ".." sequences can then write files to any location on
the local fie system that the user executing Ivy has write access to.

Ivy users of version 2.4.0 to 2.5.0 should upgrade to Ivy 2.5.1.

### References
* https://lists.apache.org/thread/gqvvv7qsm2dfjg6xzsw1s2h08tbr0sdy


### Credits
* This issue was discovered by Kostya Kortchinsky of the Databricks Security Team.


## Apache Ivy allows path traversal in the presence of a malicious repository ## { #CVE-2022-37866 }

CVE-2022-37866 [\[CVE json\]](./CVE-2022-37866.cve.json) [\[OSV json\]](./CVE-2022-37866.osv.json)



_Last updated: 2022-11-07T13:15:44.826Z_

### Affected

* Apache Ivy from 2.0.0 before *


### Description

When Apache Ivy downloads artifacts from a repository it stores them in
the local file system based on a user-supplied "pattern" that may
include placeholders for artifacts coordinates like the organisation,
module or version.

If said coordinates contain "../" sequences - which are valid characters
for Ivy coordinates in general - it is possible the artifacts are stored
outside of Ivy's local cache or repository or can overwrite different
artifacts inside of the local cache.

In order to exploit this vulnerability an attacker needs collaboration
by the remote repository as Ivy will issue http requests containing ".."
sequences and a "normal" repository will not interpret them as part of
the artifact coordinates.

Users of Apache Ivy 2.0.0 to 2.5.1 should upgrade to Ivy 2.5.1.

### References
* https://lists.apache.org/thread/htxbr8oc464hxrgroftnz3my70whk93b


### Credits
* This issue was discovered by Kostya Kortchinsky of the Databricks Security Team.


## XML External Entity vulnerability in Apache Ivy ## { #CVE-2022-46751 }

CVE-2022-46751 [\[CVE json\]](./CVE-2022-46751.cve.json) [\[OSV json\]](./CVE-2022-46751.osv.json)



_Last updated: 2023-08-21T06:54:55.281Z_

### Affected

* Apache Ivy from 1.0.0 through 2.5.1


### Description

Improper Restriction of XML External Entity Reference, XML Injection (aka Blind XPath Injection) vulnerability in Apache Software Foundation Apache Ivy.<p>This issue affects any version of Apache Ivy prior to 2.5.2.</p><p>When Apache Ivy prior to 2.5.2 parses XML files - either its own configuration, Ivy files or Apache Maven POMs - it will allow downloading external document type definitions and expand any entity references contained therein when used.</p><p>This can be used to exfiltrate data, access resources only the machine running Ivy has access to or disturb the execution of Ivy in different ways.</p><p>Starting with Ivy 2.5.2 DTD processing is disabled by default except when parsing Maven POMs where the default is to allow DTD processing but only to include a DTD snippet shipping with Ivy that is needed to deal with existing Maven POMs that are not valid XML files but are nevertheless accepted by Maven. Access can be be made more lenient via newly introduced system properties where needed.<br></p><p>Users of Ivy prior to version 2.5.2 can use Java system properties to restrict processing of external DTDs, see the section about "JAXP Properties for External Access restrictions" inside Oracle's "Java API for XML Processing (JAXP) Security Guide".<br></p>

### References
* https://docs.oracle.com/en/java/javase/13/security/java-api-xml-processing-jaxp-security-guide.html#GUID-94ABC0EE-9DC8-44F0-84AD-47ADD5340477
* https://gitbox.apache.org/repos/asf?p=ant-ivy.git;a=commit;h=2be17bc18b0e1d4123007d579e43ba1a4b6fab3d
* https://lists.apache.org/thread/9gcz4xrsn8c7o9gb377xfzvkb8jltffr
* https://lists.apache.org/thread/1dj60hg5nr36kjr4p1100dwjrqookps8


### Credits
* CC Bomber, Kitri BoB (finder)
* Jenkins Security Team (reporter)
