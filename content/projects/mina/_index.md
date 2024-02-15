---
title: Apache MINA security advisories
description: Security information for Apache MINA
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache MINA? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## DoS/OOM leak vulnerability in Apache Mina SSHD Server ## { #CVE-2021-30129 }

CVE-2021-30129 [\[CVE json\]](./CVE-2021-30129.cve.json)

_Last updated: 2021-07-12T12:00:59.616Z_

### Affected

* Apache Mina SSHD from 2.0.0 before Apache Mina SSHD*


### Description

A vulnerability in sshd-core of Apache Mina SSHD allows an attacker to overflow the server causing an OutOfMemory error.  This issue affects the SFTP and port forwarding features of Apache Mina SSHD version 2.0.0 and later versions.  It was addressed in Apache Mina SSHD 2.7.0

### References
* https://lists.apache.org/thread.html/r6d4f78e192a0c8eabd671a018da464024642980ecd24096bde6db36f%40%3Cusers.mina.apache.org%3E


## Apache MINA HTTP listener DOS ## { #CVE-2021-41973 }

CVE-2021-41973 [\[CVE json\]](./CVE-2021-41973.cve.json)

_Last updated: 2021-11-01T08:33:24.585Z_

### Affected

* Apache MINA from Apache MINA before 2.1.5


### Description

In Apache MINA, a specifically crafted, malformed HTTP request may cause the HTTP Header decoder to loop indefinitely.  The decoder assumed that the HTTP Header begins at the beginning of the buffer and loops if there is more data than expected.  Please update MINA to 2.1.5 or greater.

### References
* https://lists.apache.org/thread.html/r0b907da9340d5ff4e6c1a4798ef4e79700a668657f27cca8a39e9250%40%3Cdev.mina.apache.org%3E


## Apache MINA SSHD: Java unsafe deserialization vulnerability ## { #CVE-2022-45047 }

CVE-2022-45047 [\[CVE json\]](./CVE-2022-45047.cve.json)

_Last updated: 2022-11-16T09:03:02.600Z_

### Affected

* Apache MINA SSHD from unspecified through 2.9.1


### Description

Class org.apache.sshd.server.keyprovider.SimpleGeneratorHostKeyProvider in Apache MINA SSHD <= 2.9.1 uses Java deserialization to load a serialized java.security.PrivateKey. The class is one of several implementations that an implementor using Apache MINA SSHD can choose for loading the host keys of an SSH server.

### References
* https://www.mail-archive.com/dev%40mina.apache.org/msg39312.html


### Credits
* The Apache MINA SSHD team would like to thank Zhang Zewei, NOFOCUS, for reporting this issue.


## Information disclosure bugs with RootedFilesystem ## { #CVE-2023-35887 }

CVE-2023-35887 [\[CVE json\]](./CVE-2023-35887.cve.json)

_Last updated: 2023-07-19T07:18:05.211Z_

### Affected

* Apache MINA SSHD from 1.0 before 2.10


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache MINA.<br><br>In SFTP servers implemented using Apache MINA SSHD that use a RootedFileSystem, logged users may be able to discover "exists/does not exist" information about items outside the rooted tree via paths including parent navigation ("..") beyond the root, or involving symlinks.<br><br>This issue affects Apache MINA: from 1.0 before 2.10. Users are recommended to upgrade to 2.10<br>

### References
* https://lists.apache.org/thread/b9qgtqvhnvgfpn0w1gz918p21p53tqk2


### Credits
* Andrew Pikler (finder)
