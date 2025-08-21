---
title: Apache Commons security advisories
description: Security information for Apache Commons
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Commons? You can read more about the projects' security policy on their [security page](https://commons.apache.org/security.html), and email your report to the [Apache Commons Security Team](mailto:security@commons.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://commons.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Possible limited path traversal vulnerabily in Apache Commons IO  ## { #CVE-2021-29425 }

CVE-2021-29425 [\[CVE json\]](./CVE-2021-29425.cve.json) [\[OSV json\]](./CVE-2021-29425.osv.json)



_Last updated: 2021-04-13T06:36:54.192Z_

### Affected

* Apache Commons IO at 2.2
* Apache Commons IO at 2.3
* Apache Commons IO at 2.4
* Apache Commons IO at 2.5
* Apache Commons IO at 2.6


### Description

In Apache Commons IO before 2.7, When invoking the method FileNameUtils.normalize with an improper input string, like "//../foo", or "\\..\foo", the result would be the same value, thus possibly providing access to files in the parent directory, but not further above (thus "limited" path traversal), if the calling code would use the result to construct a path value.



### References
* https://issues.apache.org/jira/browse/IO-556
* https://lists.apache.org/thread.html/rc359823b5500e9a9a2572678ddb8e01d3505a7ffcadfa8d13b8780ab%40%3Cuser.commons.apache.org%3E


## Apache Commons Compress 1.6 to 1.20 denial of service vulnerability ## { #CVE-2021-35515 }

CVE-2021-35515 [\[CVE json\]](./CVE-2021-35515.cve.json) [\[OSV json\]](./CVE-2021-35515.osv.json)



_Last updated: 2021-07-13T07:11:36.980Z_

### Affected

* Apache Commons Compress from 1.6 before Apache Commons Compress*


### Description

When reading a specially crafted 7Z archive, the construction of the list of codecs that decompress an entry can result in an infinite loop.  This could be used to mount a denial of service attack against services that use Compress' sevenz package.


### References
* https://commons.apache.org/proper/commons-compress/security-reports.html
* https://lists.apache.org/thread.html/r19ebfd71770ec0617a9ea180e321ef927b3fefb4c81ec5d1902d20ab%40%3Cuser.commons.apache.org%3E


### Credits
* This issue was discovered by OSS Fuzz.


## Apache Commons Compress 1.6 to 1.20 denial of service vulnerability ## { #CVE-2021-35516 }

CVE-2021-35516 [\[CVE json\]](./CVE-2021-35516.cve.json) [\[OSV json\]](./CVE-2021-35516.osv.json)



_Last updated: 2021-07-13T07:11:43.957Z_

### Affected

* Apache Commons Compress from 1.6 before Apache Commons Compress*


### Description

When reading a specially crafted 7Z archive, Compress can be made to allocate large amounts of memory that finally leads to an out of memory error even for very small inputs. This could be used to mount a denial of service attack against services that use Compress' sevenz package.


### References
* https://commons.apache.org/proper/commons-compress/security-reports.html
* https://lists.apache.org/thread.html/rf68442d67eb166f4b6cf0bbbe6c7f99098c12954f37332073c9822ca%40%3Cuser.commons.apache.org%3E


### Credits
* This issue was first reported to the project's issue tracker as COMPRESS-542 by Robin Schimpf. Later OSS Fuzz detected ways to exploit this issue which managed to escape the initial attempt to fix it.


## Apache Commons Compress 1.1 to 1.20 denial of service vulnerability ## { #CVE-2021-35517 }

CVE-2021-35517 [\[CVE json\]](./CVE-2021-35517.cve.json) [\[OSV json\]](./CVE-2021-35517.osv.json)



_Last updated: 2021-07-13T07:11:53.430Z_

### Affected

* Apache Commons Compress from 1.1 before Apache Commons Compress*


### Description

When reading a specially crafted TAR archive, Compress can be made to allocate large amounts of memory that finally leads to an out of memory error even for very small inputs. This could be used to mount a denial of service attack against services that use Compress' tar package.


### References
* https://commons.apache.org/proper/commons-compress/security-reports.html
* https://lists.apache.org/thread.html/r605d906b710b95f1bbe0036a53ac6968f667f2c249b6fbabada9a940%40%3Cuser.commons.apache.org%3E


### Credits
* This issue was discovered by OSS Fuzz.


## Apache Commons Compress 1.0 to 1.20 denial of service vulnerability ## { #CVE-2021-36090 }

CVE-2021-36090 [\[CVE json\]](./CVE-2021-36090.cve.json) [\[OSV json\]](./CVE-2021-36090.osv.json)



_Last updated: 2021-07-13T07:12:34.084Z_

### Affected

* Apache Commons Compress from Apache Commons Compress through 1.20


### Description

When reading a specially crafted ZIP archive, Compress can be made to allocate large amounts of memory that finally leads to an out of memory error even for very small inputs. This could be used to mount a denial of service attack against services that use Compress' zip package.


### References
* https://commons.apache.org/proper/commons-compress/security-reports.html
* https://lists.apache.org/thread.html/rc4134026d7d7b053d4f9f2205531122732405012c8804fd850a9b26f%40%3Cuser.commons.apache.org%3E


### Credits
* This issue was discovered by OSS Fuzz.


## Apache Commons Net's FTP client trusts the host from PASV response by default ## { #CVE-2021-37533 }

CVE-2021-37533 [\[CVE json\]](./CVE-2021-37533.cve.json) [\[OSV json\]](./CVE-2021-37533.osv.json)



_Last updated: 2022-12-03T14:53:25.293Z_

### Affected

* Apache Commons Net from Apache Commons Net before 3.9.0


### Description

Prior to Apache Commons Net 3.9.0, Net's FTP client trusts the host from PASV response by default. A malicious server can redirect the Commons Net code to use a different host, but the user has to connect to the malicious server in the first place. This may lead to leakage of information about services running on the private network of the client.
The default in version 3.9.0 is now false to ignore such hosts, as cURL does. See https://issues.apache.org/jira/browse/NET-711.


### References
* https://lists.apache.org/thread/o6yn9r9x6s94v97264hmgol1sf48mvx7


### Credits
* Apache Commons would like to thank ZeddYu Lu for reporting this issue.


## Apache Commons Configuration insecure interpolation defaults ## { #CVE-2022-33980 }

CVE-2022-33980 [\[CVE json\]](./CVE-2022-33980.cve.json) [\[OSV json\]](./CVE-2022-33980.osv.json)



_Last updated: 2022-07-06T13:03:54.020Z_

### Affected

* Apache Commons Configuration from Apache Commons Configuration before 2.8.0


### Description

Apache Commons Configuration performs variable interpolation, allowing properties to be dynamically evaluated and expanded. The standard format for interpolation is "${prefix:name}", where "prefix" is used to locate an instance of org.apache.commons.configuration2.interpol.Lookup that performs the interpolation. Starting with version 2.4 and continuing through 2.7, the set of default Lookup instances included interpolators that could result in arbitrary code execution or contact with remote servers. These lookups are:
- "script" - execute expressions using the JVM script execution engine (javax.script)
- "dns" - resolve dns records
- "url" - load values from urls, including from remote servers

Applications using the interpolation defaults in the affected versions may be vulnerable to remote code execution or unintentional contact with remote servers if untrusted configuration values are used.

Users are recommended to upgrade to Apache Commons Configuration 2.8.0, which disables the problematic interpolators by default.

### References
* https://lists.apache.org/thread/tdf5n7j80lfxdhs2764vn0xmpfodm87s


## Apache Commons Text prior to 1.10.0 allows RCE when applied to untrusted input due to insecure interpolation defaults ## { #CVE-2022-42889 }

CVE-2022-42889 [\[CVE json\]](./CVE-2022-42889.cve.json) [\[OSV json\]](./CVE-2022-42889.osv.json)



_Last updated: 2022-10-13T13:03:35.541Z_

### Affected

* Apache Commons Text from 1.5 before Apache Commons Text*
* Apache Commons Text from unspecified through 1.9


### Description

Apache Commons Text performs variable interpolation, allowing properties to be dynamically evaluated and expanded. The standard format for interpolation is "${prefix:name}", where "prefix" is used to locate an instance of org.apache.commons.text.lookup.StringLookup that performs the interpolation. Starting with version 1.5 and continuing through 1.9, the set of default Lookup instances included interpolators that could result in arbitrary code execution or contact with remote servers. These lookups are:

- "script" - execute expressions using the JVM script execution engine (javax.script)
- "dns" - resolve dns records
- "url" - load values from urls, including from remote servers

Applications using the interpolation defaults in the affected versions may be vulnerable to remote code execution or unintentional contact with remote servers if untrusted configuration values are used. Users are recommended to upgrade to Apache Commons Text 1.10.0, which disables the problematic interpolators by default.

### References
* https://lists.apache.org/thread/n2bd4vdsgkqh2tm14l1wyc3jyol7s1om


## Apache Commons BCEL prior to 6.6.0 allows producing arbitrary bytecode via out-of-bounds writing ## { #CVE-2022-42920 }

CVE-2022-42920 [\[CVE json\]](./CVE-2022-42920.cve.json) [\[OSV json\]](./CVE-2022-42920.osv.json)



_Last updated: 2022-11-07T12:25:20.461Z_

### Affected

* Apache Commons BCEL from Apache Commons BCEL before 6.6.0


### Description

Apache Commons BCEL has a number of APIs that would normally only allow changing specific class characteristics. However, due to an out-of-bounds writing issue, these APIs can be used to produce arbitrary bytecode. This could be abused in applications that pass attacker-controllable data to those APIs, giving the attacker more control over the resulting bytecode than otherwise expected. Update to Apache Commons BCEL 6.6.0.

### References
* https://lists.apache.org/thread/lfxk7q8qmnh5bt9jm6nmjlv5hsxjhrz4


### Credits
* Reported by Felix Wilhelm (Google); GitHub pull request to Apache Commons BCEL #147 by Richard Atkins (https://github.com/rjatkins); PR derived from OpenJDK (https://github.com/openjdk/jdk11u/) commit 13bf52c8d876528a43be7cb77a1f452d29a21492 by Aleksei Voitylov and RealCLanger (Christoph Langer https://github.com/RealCLanger)


## FileUpload DoS with excessive parts ## { #CVE-2023-24998 }

CVE-2023-24998 [\[CVE json\]](./CVE-2023-24998.cve.json) [\[OSV json\]](./CVE-2023-24998.osv.json)



_Last updated: 2023-02-23T09:34:40.480Z_

### Affected

* Apache Commons FileUpload before 1.5
* Apache Tomcat at 11.0.0-M1
* Apache Tomcat from 10.0.0-M1 through 10.1.4
* Apache Tomcat from 9.0.0-M1 through 9.0.70
* Apache Tomcat from 8.5.0 through 8.5.84


### Description

<div>Apache Commons FileUpload before 1.5 does not limit the number of request parts to be processed resulting in the possibility of an attacker triggering a DoS with a malicious upload or series of uploads.</div><div><br></div><div>Note that, like all of the file upload limits, the
          new configuration option (FileUploadBase#setFileCountMax) is not
          enabled by default and must be explicitly configured.<br></div>

### References
* https://lists.apache.org/thread/4xl4l09mhwg4vgsk7dxqogcjrobrrdoy


### Credits
* Jakob Ackermann (finder)


## Denial of service via CPU consumption for malformed TAR file ## { #CVE-2023-42503 }

CVE-2023-42503 [\[CVE json\]](./CVE-2023-42503.cve.json) [\[OSV json\]](./CVE-2023-42503.osv.json)



_Last updated: 2023-09-14T07:45:08.532Z_

### Affected

* Apache Commons Compress from 1.22 before 1.24.0


### Description

Improper Input Validation, Uncontrolled Resource Consumption vulnerability in Apache Commons Compress in TAR parsing.<p>This issue affects Apache Commons Compress:&nbsp;from 1.22 before 1.24.0.</p><p>Users are recommended to upgrade to version 1.24.0, which fixes the issue.</p><span style="background-color: rgb(255, 255, 255);">A third party can create a malformed TAR file by manipulating file modification times headers, which when parsed with Apache Commons Compress, will cause a denial of service issue via CPU consumption.</span><br><br><span style="background-color: rgb(255, 255, 255);">In version 1.22 of Apache Commons Compress, support was added for file modification times with higher precision (issue # COMPRESS-612 [1]). The format for the PAX extended headers carrying this data consists of two numbers separated by a period [2], indicating seconds and subsecond precision (for example “1647221103.5998539”). The impacted fields are “atime”, “ctime”, “mtime” and “LIBARCHIVE.creationtime”. No input validation is performed prior to the parsing of header values.</span><br><br><span style="background-color: rgb(255, 255, 255);">Parsing of these numbers uses the BigDecimal [3] class from the JDK which has a publicly known algorithmic complexity issue when doing operations on large numbers, causing denial of service (see issue # JDK-6560193 [4]). A third party can manipulate file time headers in a TAR file by placing a number with a very long fraction (300,000 digits) or a number with exponent notation (such as “9e9999999”) within a file modification time header, and the parsing of files with these headers will take hours instead of seconds, leading to a denial of service via exhaustion of CPU resources. This issue is similar to CVE-2012-2098 [5].</span><br><br><span style="background-color: rgb(255, 255, 255);">[1]: </span><a target="_blank" rel="nofollow" href="https://issues.apache.org/jira/browse/COMPRESS-612">https://issues.apache.org/jira/browse/COMPRESS-612</a><br><span style="background-color: rgb(255, 255, 255);">[2]: </span><a target="_blank" rel="nofollow" href="https://pubs.opengroup.org/onlinepubs/9699919799/utilities/pax.html#tag_20_92_13_05">https://pubs.opengroup.org/onlinepubs/9699919799/utilities/pax.html#tag_20_92_13_05</a><br><span style="background-color: rgb(255, 255, 255);">[3]: </span><a target="_blank" rel="nofollow" href="https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html">https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html</a><br><span style="background-color: rgb(255, 255, 255);">[4]: </span><a target="_blank" rel="nofollow" href="https://bugs.openjdk.org/browse/JDK-6560193">https://bugs.openjdk.org/browse/JDK-6560193</a><br><span style="background-color: rgb(255, 255, 255);">[5]: </span><a target="_blank" rel="nofollow" href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-2098">https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-2098</a><br><br><span style="background-color: rgb(255, 255, 255);">Only applications using CompressorStreamFactory class (with auto-detection of file types), TarArchiveInputStream and TarFile classes to parse TAR files are impacted. Since this code was introduced in v1.22, only that version and later versions are impacted.</span><br><br>

### References
* https://lists.apache.org/thread/5xwcyr600mn074vgxq92tjssrchmc93c


### Credits
* Yakov Shafranovich, Amazon Web Services (reporter)


## Denial of service caused by an infinite loop for a corrupted DUMP file ## { #CVE-2024-25710 }

CVE-2024-25710 [\[CVE json\]](./CVE-2024-25710.cve.json) [\[OSV json\]](./CVE-2024-25710.osv.json)



_Last updated: 2024-02-19T08:33:36.725Z_

### Affected

* Apache Commons Compress from 1.3 through 1.25.0


### Description

Loop with Unreachable Exit Condition ('Infinite Loop') vulnerability in Apache Commons Compress.<p>This issue affects Apache Commons Compress: from 1.3 through 1.25.0.</p><p>Users are recommended to upgrade to version 1.26.0 which fixes the issue.</p>

### References
* https://lists.apache.org/thread/cz8qkcwphy4cx8gltn932ln51cbtq6kf


### Credits
* Yakov Shafranovich, Amazon Web Services (reporter)


## OutOfMemoryError unpacking broken Pack200 file ## { #CVE-2024-26308 }

CVE-2024-26308 [\[CVE json\]](./CVE-2024-26308.cve.json) [\[OSV json\]](./CVE-2024-26308.osv.json)



_Last updated: 2024-02-19T08:31:48.197Z_

### Affected

* Apache Commons Compress from 1.21 before 1.26.0


### Description

Allocation of Resources Without Limits or Throttling vulnerability in Apache Commons Compress.<p>This issue affects Apache Commons Compress: from 1.21 before 1.26.</p><p>Users are recommended to upgrade to version 1.26, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ch5yo2d21p7vlqrhll9b17otbyq4npfg


### Credits
* Yakov Shafranovich, Amazon Web Services (reporter)


## StackOverflowError adding property in AbstractListDelimiterHandler.flattenIterator() ## { #CVE-2024-29131 }

CVE-2024-29131 [\[CVE json\]](./CVE-2024-29131.cve.json) [\[OSV json\]](./CVE-2024-29131.osv.json)



_Last updated: 2024-03-21T09:07:12.130Z_

### Affected

* Apache Commons Configuration from 2.0 before 2.10.1


### Description

Out-of-bounds Write vulnerability in Apache Commons Configuration.<p>This issue affects Apache Commons Configuration: from 2.0 before 2.10.1.</p><p>Users are recommended to upgrade to version 2.10.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/03nzzzjn4oknyw5y0871tw7ltj0t3r37


### Credits
* Bob Marinier (finder)


## StackOverflowError calling ListDelimiterHandler.flatten(Object, int) with a cyclical object tree ## { #CVE-2024-29133 }

CVE-2024-29133 [\[CVE json\]](./CVE-2024-29133.cve.json) [\[OSV json\]](./CVE-2024-29133.osv.json)



_Last updated: 2024-03-21T09:05:45.826Z_

### Affected

* Apache Commons Configuration from 2.0 before 2.10.1


### Description

Out-of-bounds Write vulnerability in Apache Commons Configuration.<p>This issue affects Apache Commons Configuration: from 2.0 before 2.10.1.</p><p>Users are recommended to upgrade to version 2.10.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ccb9w15bscznh6tnp3wsvrrj9crbszh2


### Credits
* Gary Gregory (finder)


## Possible denial of service attack on untrusted input to XmlStreamReader ## { #CVE-2024-47554 }

CVE-2024-47554 [\[CVE json\]](./CVE-2024-47554.cve.json) [\[OSV json\]](./CVE-2024-47554.osv.json)



_Last updated: 2024-10-03T11:32:46.805Z_

### Affected

* Apache Commons IO from 2.0 before 2.14.0


### Description

<p>Uncontrolled Resource Consumption vulnerability in Apache Commons IO.</p><p>The org.apache.commons.io.input.XmlStreamReader class may excessively consume CPU resources when processing maliciously crafted input.<br></p><p>This issue affects Apache Commons IO: from 2.0 before 2.14.0.</p><p>Users are recommended to upgrade to version 2.14.0 or later, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/6ozr91rr9cj5lm0zyhv30bsp317hk5z1


### Credits
* CodeQL (tool)


## Possible path traversal issue when using NameScope.DESCENDENT ## { #CVE-2025-27553 }

CVE-2025-27553 [\[CVE json\]](./CVE-2025-27553.cve.json) [\[OSV json\]](./CVE-2025-27553.osv.json)



_Last updated: 2025-03-23T14:16:17.945Z_

### Affected

* Apache Commons VFS before 2.10.0


### Description

<p>Relative Path Traversal vulnerability in Apache Commons VFS before 2.10.0.</p><span style="background-color: rgb(255, 255, 255);">The FileObject API in Commons VFS has a 'resolveFile' method that
takes a 'scope' parameter. Specifying 'NameScope.DESCENDENT' promises that "an exception is thrown if the resolved file is not a descendent of
the base file". However, when the path contains encoded ".."
characters (for example, "%2E%2E/bar.txt"), it might return file objects that are not
a descendent of the base file, without throwing an exception.</span><br><p>This issue affects Apache Commons VFS: before 2.10.0.</p><p>Users are recommended to upgrade to version 2.10.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/cnzqowyw9r2pl263cylmxhnvh41hyjcb


### Credits
* Arnout Engelen (finder)


## Failing to find an FTP file can reveal the URI's password in an error message ## { #CVE-2025-30474 }

CVE-2025-30474 [\[CVE json\]](./CVE-2025-30474.cve.json) [\[OSV json\]](./CVE-2025-30474.osv.json)



_Last updated: 2025-03-23T14:15:49.617Z_

### Affected

* Apache Commons VFS before 2.10.0


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Commons VFS.</p>The FtpFileObject class can throw an exception when a file is not found, revealing the original URI in its message, which may include a password. <span style="background-color: rgb(255, 255, 255);">The fix is to mask the password in the exception message</span><br><p>This issue affects Apache Commons VFS: before 2.10.0.</p><p>Users are recommended to upgrade to version 2.10.0, which fixes the issue.</p>

### References
* https://issues.apache.org/jira/browse/VFS-169
* https://lists.apache.org/thread/w6ztgnbk6ccry3470x191g3xwrpgy6f4


### Credits
* Marek Šunda (finder)


## Uncontrolled Resource Consumption when loading untrusted configurations in 1.x ## { #CVE-2025-46392 }

CVE-2025-46392 [\[CVE json\]](./CVE-2025-46392.cve.json) [\[OSV json\]](./CVE-2025-46392.osv.json)



_Last updated: 2025-05-09T09:34:18.561Z_

### Affected

* Apache Commons Configuration from 1 before 2.0.0


### Description

<p>Uncontrolled Resource Consumption vulnerability in Apache Commons Configuration 1.x.</p><p>There are a number of issues in Apache Commons Configuration 1.x that allow excessive resource consumption when loading untrusted configurations or using unexpected usage patterns. The Apache Commons Configuration team does not intend to fix these issues in 1.x. Apache Commons Configuration 1.x is still safe to use in scenario's where you only load trusted configurations. <br></p><p>Users that load untrusted configurations or give attackers control over usage patterns are recommended to upgrade to the 2.x version line, which fixes these issues. Apache Commons Configuration 2.x is not a drop-in replacement, but as it uses a separate Maven groupId and Java package namespace they can be loaded side-by-side, making it possible to do a gradual migration.</p>

### References
* https://www.cve.org/CVERecord?id=CVE-2024-29131
* https://www.cve.org/CVERecord?id=CVE-2024-29133
* https://lists.apache.org/thread/y1pl0mn3opz6kwkm873zshjdxq3dwq5s


## Apache Commons BeanUtils: PropertyUtilsBean does not suppresses an enum's declaredClass property by default ## { #CVE-2025-48734 }

CVE-2025-48734 [\[CVE json\]](./CVE-2025-48734.cve.json) [\[OSV json\]](./CVE-2025-48734.osv.json)



_Last updated: 2025-05-28T13:32:13.606Z_

### Affected

* Apache Commons BeanUtils 1.x from 1.0 before 1.11.0
* Apache Commons BeanUtils 2.x from 2.0.0-M1 before 2.0.0-M2


### Description

<p>Improper Access Control vulnerability in Apache Commons.</p><p></p><div><div><p>A special BeanIntrospector class was added in version 1.9.2. This can be used to stop attackers from using the declared class property of Java enum objects to get access to the classloader. However this protection was not enabled by default. PropertyUtilsBean (and consequently BeanUtilsBean) now disallows declared class level property access by default.</p></div></div>Releases 1.11.0 and 2.0.0-M2 address a potential security issue when accessing enum properties in an uncontrolled way. If an application using Commons BeanUtils passes property paths from an external source directly to the getProperty() method of PropertyUtilsBean, an attacker can access the enum’s class loader via the “declaredClass” property available on all Java “enum” objects. Accessing the enum’s “declaredClass” allows remote attackers to access the ClassLoader and execute arbitrary code. The same issue exists with PropertyUtilsBean.getNestedProperty().<br>Starting in versions 1.11.0 and 2.0.0-M2 a special BeanIntrospector suppresses the “declaredClass” property. Note that this new BeanIntrospector is enabled by default, but you can disable it to regain the old behavior; see section 2.5 of the user's guide and the unit tests.<p></p>This issue affects Apache Commons BeanUtils 1.x before 1.11.0, and 2.x before 2.0.0-M2.<p>Users of the artifact commons-beanutils:commons-beanutils

 1.x are recommended to upgrade to version 1.11.0, which fixes the issue.</p><p>
Users of the artifact org.apache.commons:commons-beanutils2

 2.x are recommended to upgrade to version 2.0.0-M2, which fixes the issue.

<br></p>

### References
* https://lists.apache.org/thread/s0hb3jkfj5f3ryx6c57zqtfohb0of1g9


### Credits
* Raj (mailto:denesh.raj@zohocorp.com) (reporter)
* Muthukumar Marikani (mailto:muthukumar.marikani@zohocorp.com) (finder)


## ClassUtils.getClass(...) can throw a StackOverflowError on very long inputs ## { #CVE-2025-48924 }

CVE-2025-48924 [\[CVE json\]](./CVE-2025-48924.cve.json) [\[OSV json\]](./CVE-2025-48924.osv.json)



_Last updated: 2025-07-11T14:56:54.861Z_

### Affected

* Apache Commons Lang from 2.0 through 2.6
* Apache Commons Lang from 3.0 before 3.18.0


### Description

<p>Uncontrolled Recursion vulnerability in Apache Commons Lang.</p><p>This issue affects Apache Commons Lang: Starting with&nbsp;<span style="background-color: rgb(255, 255, 255);">commons-lang:commons-lang&nbsp;</span>2.0 to 2.6, and, from org.apache.<span style="background-color: rgb(255, 255, 255);">commons:commons-lang3 3.0 before&nbsp;</span>3.18.0.</p><p>The methods ClassUtils.getClass(...) can throw&nbsp;StackOverflowError on very long inputs. Because an Error is usually not handled by applications and libraries, a 
StackOverflowError could&nbsp;cause an application to stop.</p><p>Users are recommended to upgrade to version 3.18.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/bgv0lpswokgol11tloxnjfzdl7yrc1g1


### Credits
* OSS-Fuzz Issue 42522972 (finder)


## FileUpload DoS via part headers ## { #CVE-2025-48976 }

CVE-2025-48976 [\[CVE json\]](./CVE-2025-48976.cve.json) [\[OSV json\]](./CVE-2025-48976.osv.json)



_Last updated: 2025-06-16T15:00:47.037Z_

### Affected

* Apache Commons FileUpload from 1.0 before 1.6
* Apache Commons FileUpload from 2.0.0-M1 before 2.0.0-M4


### Description

<p>Allocation of resources for multipart headers with insufficient limits enabled a DoS vulnerability in Apache Commons FileUpload.</p><p>This issue affects Apache Commons FileUpload: from 1.0 before 1.6; from 2.0.0-M1 before 2.0.0-M4.</p><p>Users are recommended to upgrade to versions 1.6 or 2.0.0-M4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/fbs3wrr3p67vkjcxogqqqqz45pqtso12


### Credits
* TERASOLUNA Framework Security Team of NTT DATA Group Corporation (finder)


## Expression Injection leading to RCE ## { #CVE-2025-53192 }

CVE-2025-53192 [\[CVE json\]](./CVE-2025-53192.cve.json) [\[OSV json\]](./CVE-2025-53192.osv.json)



_Last updated: 2025-08-18T20:09:29.375Z_

### Affected

* Apache Commons OGNL before *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Improper Neutralization of Expression/Command Delimiters vulnerability in Apache Commons OGNL.</p><p>This issue affects Apache Commons OGNL: all versions.</p><p></p><div><p>When using the API <code>Ognl.getValue</code>​, the OGNL engine parses and evaluates the provided expression with powerful capabilities, including accessing and invoking related methods,
 etc. Although <code>OgnlRuntime</code> attempts to restrict certain dangerous classes and methods (such as <code>java.lang.Runtime</code>) through a blocklist, these restrictions are not comprehensive. 
Attackers may be able to bypass the restrictions by leveraging class objects that are not covered by the blocklist and potentially achieve arbitrary code execution.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.<br></p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</div>

### References
* https://lists.apache.org/thread/2gj8tjl6vz949nnp3yxz3okm9xz2k7sp


### Credits
* yyjLF (finder)
