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

CVE-2021-25642 [\[CVE json\]](./CVE-2021-25642.cve.json) [\[OSV json\]](./CVE-2021-25642.osv.json)



_Last updated: 2022-08-25T13:21:18.013Z_

### Affected

* Apache Hadoop at 2.9.0 to 2.10.1, 3.0.0-alpha1 to 3.1.4, 3.2.0 to 3.2.3, and 3.3.0 to 3.3.3


### Description

ZKConfigurationStore which is optionally used by CapacityScheduler of Apache Hadoop YARN deserializes data obtained from ZooKeeper without validation. An attacker having access to ZooKeeper can run arbitrary commands as YARN user by exploiting this.  Users should upgrade to Apache Hadoop 2.10.2, 3.2.4, 3.3.4 or later (containing YARN-11126) if ZKConfigurationStore is used.

### References
* https://lists.apache.org/thread/g6vf2h4wdgzzdgk91mqozhs58wotq150


### Credits
* Apache Hadoop would like to thank Liu Ximing for reporting this issue.


## Apache Hadoop Privilege escalation vulnerability ## { #CVE-2021-33036 }

CVE-2021-33036 [\[CVE json\]](./CVE-2021-33036.cve.json) [\[OSV json\]](./CVE-2021-33036.osv.json)



_Last updated: 2022-06-15T14:23:07.883Z_

### Affected

* Apache Hadoop at 2.2.0 to 2.10.1, 3.0.0-alpha1 to 3.1.4, 3.2.0 to 3.2.2, and 3.3.0 to 3.3.1


### Description

In Apache Hadoop 2.2.0 to 2.10.1, 3.0.0-alpha1 to 3.1.4, 3.2.0 to 3.2.2, and 3.3.0 to 3.3.1, a user who can escalate to yarn user can possibly run arbitrary commands as root user.  Users should upgrade to Apache Hadoop 2.10.2, 3.2.3, 3.3.2 or higher.

### References
* https://lists.apache.org/thread/ctr84rmo3xd2tzqcx2b277c8z692vhl5


### Credits
* Apache Hadoop would like to thank Hideyuki Furue for reporting and fixing this issue.


## Heap buffer overflow in libhdfs native library ## { #CVE-2021-37404 }

CVE-2021-37404 [\[CVE json\]](./CVE-2021-37404.cve.json) [\[OSV json\]](./CVE-2021-37404.osv.json)



_Last updated: 2022-06-13T06:58:30.060Z_

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

CVE-2022-25168 [\[CVE json\]](./CVE-2022-25168.cve.json) [\[OSV json\]](./CVE-2022-25168.osv.json)



_Last updated: 2022-08-04T14:28:32.587Z_

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

_Last updated: 2022-04-07T17:32:32.075Z_

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


## Privilege escalation in Apache Hadoop Yarn container-executor binary on Linux systems ## { #CVE-2023-26031 }

CVE-2023-26031 [\[CVE json\]](./CVE-2023-26031.cve.json) [\[OSV json\]](./CVE-2023-26031.osv.json)



_Last updated: 2024-05-07T00:58:06.325Z_

### Affected

* Apache Hadoop from 3.3.1 before 3.3.5


### Description

<br>Relative library resolution in linux container-executor binary in Apache Hadoop 3.3.1-3.3.4 on Linux allows local user to gain root privileges. If the YARN cluster is accepting work from remote (authenticated) users, this MAY permit remote users to gain root privileges.<br><br>Hadoop 3.3.0 updated the "<a target="_blank" rel="nofollow" href="https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/SecureContainer.html">YARN Secure Containers</a>" to add a feature for executing user-submitted applications in isolated linux containers.<br><br>The native binary HADOOP_HOME/bin/container-executor is used to launch these containers; it must be owned by root and have the suid bit set in order for the YARN processes to run the containers as the specific users submitting the jobs.<br><br>The patch "<a target="_blank" rel="nofollow" href="https://issues.apache.org/jira/browse/YARN-10495">YARN-10495</a>. make the rpath of container-executor configurable" modified the library loading path for loading .so files from "$ORIGIN/" to ""$ORIGIN/:../lib/native/". This is the a path through which libcrypto.so is located. Thus it is is possible for a user with reduced privileges to install a malicious libcrypto library into a path to which they have write access, invoke the container-executor command, and have their modified library executed as root.<br>If the YARN cluster is accepting work from remote (authenticated) users, and these users' submitted job are executed in the physical host, rather than a container, then the CVE permits remote users to gain root privileges.<br><br>The fix for the vulnerability is to revert the change, which is done in <a target="_blank" rel="nofollow" href="https://issues.apache.org/jira/browse/YARN-11441">YARN-11441</a>, "Revert YARN-10495". This patch is in hadoop-3.3.5.<br><br>To determine whether a version of container-executor is vulnerable, use the readelf command. If the RUNPATH or RPATH value contains the relative path "./lib/native/" then it  is at risk<br><br><tt>$ readelf -d container-executor|grep <span style="background-color: rgb(255, 255, 255);">'RUNPATH\|RPATH'</span> <br>0x000000000000001d (RUNPATH)  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Library runpath: [$ORIGIN/:../lib/native/]</tt><br><br>If it does not, then it is safe:<br><br><tt>$ readelf -d container-executor|grep <span style="background-color: rgb(255, 255, 255);">'RUNPATH\|RPATH'</span> <br>0x000000000000001d (RUNPATH)  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Library runpath: [$ORIGIN/]</tt><br><br>For an at-risk version of container-executor to enable privilege escalation, the owner must be root and the suid bit must be set<br><tt><br>$ ls -laF /opt/hadoop/bin/container-executor<br>---Sr-s---. 1 root hadoop 802968 May 9 20:21 /opt/hadoop/bin/container-executor</tt><br><br>A safe installation lacks the suid bit; ideally is also not owned by root.<br><br><tt>$ ls -laF /opt/hadoop/bin/container-executor<br>-rwxr-xr-x. 1 yarn hadoop 802968 May 9 20:21 /opt/hadoop/bin/container-executor</tt><br><br>This configuration does not support Yarn Secure Containers, but all other hadoop services, including YARN job execution outside secure containers continue to work.<br><br><br><br><br>

### References
* https://issues.apache.org/jira/browse/YARN-11441
* https://hadoop.apache.org/cve_list.html
* https://lists.apache.org/thread/q9qpdlv952gb4kphpndd5phvl7fkh71r


### Credits
* Esa Hiltunen (finder)
* Mikko Kortelainen (finder)
* The Teragrep Project (sponsor)


## Temporary File Local Information Disclosure ## { #CVE-2024-23454 }

CVE-2024-23454 [\[CVE json\]](./CVE-2024-23454.cve.json) [\[OSV json\]](./CVE-2024-23454.osv.json)



_Last updated: 2024-09-25T07:45:41.584Z_

### Affected

* Apache Hadoop before 3.4.0


### Description

<span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">Apache Hadoop’s RunJar.run()&nbsp;<span style="background-color: rgb(255, 255, 255);">does not set permissions for temporary directory&nbsp;by default. I</span></span>f sensitive data will be present in this file, all the other local users may be able to view the content.
This is because, on unix-like systems, the system temporary directory is
shared between all local users. As such, files written in this directory,
without setting the correct posix permissions explicitly, may be viewable
by all other local users.
</span><br><br>

### References
* https://issues.apache.org/jira/browse/HADOOP-19031
* https://lists.apache.org/thread/xlo7q8kn4tsjvx059r789oz19hzgfkfs


### Credits
* Andrea Cosentino (finder)
