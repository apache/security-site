---
title: Apache Hadoop security advisories
description: Security information for Apache Hadoop
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Hadoop? You can read more about the projects' security policy on their [security page](https://hadoop.apache.org/mailing_lists.html), and email your report to the [Apache Hadoop Security Team](mailto:security@hadoop.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://hadoop.apache.org/mailing_lists.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Hadoop YARN remote code execution in ZKConfigurationStore of capacity scheduler ## { #CVE-2021-25642 }

CVE-2021-25642 [\[CVE json\]](./CVE-2021-25642.cve.json)

### Affected

* Apache Hadoop at 2.9.0 to 2.10.1, 3.0.0-alpha1 to 3.1.4, 3.2.0 to 3.2.3, and 3.3.0 to 3.3.3


### Description

ZKConfigurationStore which is optionally used by CapacityScheduler of Apache Hadoop YARN deserializes data obtained from ZooKeeper without validation. An attacker having access to ZooKeeper can run arbitrary commands as YARN user by exploiting this.  Users should upgrade to Apache Hadoop 2.10.2, 3.2.4, 3.3.4 or later (containing YARN-11126) if ZKConfigurationStore is used.

### References
* https://lists.apache.org/thread/g6vf2h4wdgzzdgk91mqozhs58wotq150


### Credits
* Apache Hadoop would like to thank Liu Ximing for reporting this issue.


## Apache Hadoop Privilege escalation vulnerability ## { #CVE-2021-33036 }

CVE-2021-33036 [\[CVE json\]](./CVE-2021-33036.cve.json)

### Affected

* Apache Hadoop at 2.2.0 to 2.10.1, 3.0.0-alpha1 to 3.1.4, 3.2.0 to 3.2.2, and 3.3.0 to 3.3.1


### Description

In Apache Hadoop 2.2.0 to 2.10.1, 3.0.0-alpha1 to 3.1.4, 3.2.0 to 3.2.2, and 3.3.0 to 3.3.1, a user who can escalate to yarn user can possibly run arbitrary commands as root user.  Users should upgrade to Apache Hadoop 2.10.2, 3.2.3, 3.3.2 or higher.

### References
* https://lists.apache.org/thread/ctr84rmo3xd2tzqcx2b277c8z692vhl5


### Credits
* Apache Hadoop would like to thank Hideyuki Furue for reporting and fixing this issue.


## Heap buffer overflow in libhdfs native library ## { #CVE-2021-37404 }

CVE-2021-37404 [\[CVE json\]](./CVE-2021-37404.cve.json)

### Affected

* Apache Hadoop at 2.9.0 to 2.10.1
* Apache Hadoop at 3.0.0 to 3.1.4
* Apache Hadoop at  3.2.0 to 3.2.2
* Apache Hadoop at 3.3.0 to 3.3.1


### Description

There is a potential heap buffer overflow in Apache Hadoop libhdfs native code. Opening a file path provided by user without validation may result in a denial of service or arbitrary code execution.  Users should upgrade to Apache Hadoop 2.10.2, 3.2.3, 3.3.2 or higher.

### References
* https://lists.apache.org/thread/2h56ztcj3ojc66qzf1nno88vjw9vd4wo


### Credits
* This issue was discovered by Igor Chervatyuk.


## Command injection in org.apache.hadoop.fs.FileUtil.unTarUsingTar ## { #CVE-2022-25168 }

CVE-2022-25168 [\[CVE json\]](./CVE-2022-25168.cve.json)

### Affected

* Apache Hadoop at 2.0.0 to 2.10.1
* Apache Hadoop at 3.0.0-alpha to 3.2.3
* Apache Hadoop at 3.3.0 to 3.3.2


### Description

Apache Hadoop's FileUtil.unTar(File, File) API does not escape the input file name before being passed to the shell. An attacker can inject arbitrary commands.

This is only used in Hadoop 3.3 InMemoryAliasMap.completeBootstrapTransfer, which is only ever run by a local user.

It has been used in Hadoop 2.x for yarn localization, which does enable remote code execution.

It is used in Apache Spark, from the SQL command ADD ARCHIVE. As the ADD ARCHIVE command adds new binaries to the classpath, being able to execute shell scripts does not confer new permissions to the caller.

SPARK-38305. "Check existence of file before untarring/zipping", which is included in 3.3.0, 3.1.4, 3.2.2, prevents shell commands being executed, regardless of which version of the hadoop libraries are in use.

Users should upgrade to Apache Hadoop 2.10.2, 3.2.4, 3.3.3 or upper (including HADOOP-18136).

### References
* https://lists.apache.org/thread/mxqnb39jfrwgs3j6phwvlrfq4mlox130


### Credits
* Apache Hadoop would like to thank Kostya Kortchinsky for reporting this issue.


## Arbitrary file write in FileUtil#unpackEntries on Windows ## { #CVE-2022-26612 }

CVE-2022-26612 [\[CVE json\]](./CVE-2022-26612.cve.json)

### Affected

* Apache Hadoop at 3.3.1
* Apache Hadoop at 3.3.2
* Apache Hadoop from unspecified before 3.2.3
* Apache Hadoop from 3.4 before All*


### Description

In Apache Hadoop, The unTar function uses unTarUsingJava function on Windows and the built-in tar utility on Unix and other OSes.  As a result, a TAR entry may create a symlink under the expected extraction directory which points to an external directory. A subsequent TAR entry may extract an arbitrary file into the external directory using the symlink name. This however would be caught by the same targetDirPath check on Unix because of the getCanonicalPath call. However on Windows, getCanonicalPath doesn't resolve symbolic links, which bypasses the check.  unpackEntries during TAR extraction follows symbolic links which allows writing outside expected base directory on Windows.

This was addressed in Apache Hadoop 3.2.3

### References
* https://lists.apache.org/thread/hslo7wzw2449gv1jyjk8g6ttd7935fyz


### Credits
* This issue was reported by a member of GitHub Security Lab, Jaroslav Lobačevski (https://github.com/JarLob).
