---
title: Apache MINA security advisories
description: Security information for Apache MINA
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache MINA? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Information disclosure bugs with RootedFilesystem ## { #CVE-2023-35887 }

CVE-2023-35887 [\[CVE json\]](./CVE-2023-35887.cve.json)

### Affected

* Apache MINA SSHD from 1.0 before 2.10


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache MINA.<br><br>In SFTP servers implemented using Apache MINA SSHD that use a RootedFileSystem, logged users may be able to discover "exists/does not exist" information about items outside the rooted tree via paths including parent navigation ("..") beyond the root, or involving symlinks.<br><br>This issue affects Apache MINA: from 1.0 before 2.10. Users are recommended to upgrade to 2.10<br>

### References
* https://lists.apache.org/thread/b9qgtqvhnvgfpn0w1gz918p21p53tqk2


### Credits
* Andrew Pikler (finder)
