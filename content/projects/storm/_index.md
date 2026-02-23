---
title: Apache Storm security advisories
description: Security information for Apache Storm
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Storm? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Local Information Disclosure Vulnerability in Storm-core on Unix-Like systems due temporary files ## { #CVE-2023-43123 }

CVE-2023-43123 [\[CVE json\]](./CVE-2023-43123.cve.json) [\[OSV json\]](./CVE-2023-43123.osv.json)



_Last updated: 2023-11-23T09:16:32.695Z_

### Affected

* Apache Storm from 2.0.0 before 2.6.0


### Description

<div>On unix-like systems, the temporary directory is shared between all user. As such, writing to this directory using APIs that do not explicitly set the file/directory permissions can lead to information disclosure. Of note, this does not impact modern MacOS Operating Systems.<br><br>The method File.createTempFile on unix-like systems creates a file with predefined name (so easily identifiable) and by default will create this file with the permissions -rw-r--r--. Thus, if sensitive information is written to this file, other local users can read this information.<br></div><div><br></div><div>File.createTempFile(String, String) will create a temporary file in the system temporary directory if the 'java.io.tmpdir' system property is not explicitly set. <br><br>This affects the class&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/storm/blob/master/storm-core/src/jvm/org/apache/storm/utils/TopologySpoutLag.java#L99">https://github.com/apache/storm/blob/master/storm-core/src/jvm/org/apache/storm/utils/TopologySpoutLag.java#L99</a>&nbsp;and was introduced by&nbsp;<a target="_blank" rel="nofollow" href="https://issues.apache.org/jira/browse/STORM-3123">https://issues.apache.org/jira/browse/STORM-3123</a><br></div><div><br>In practice, this has a very limited impact as this class is used only if&nbsp;<span style="background-color: rgb(206, 204, 247);">ui.disable.spout.lag.monitoring</span></div> <div><span style="background-color: var(--wht);">is set to false, but its value is true by default.<br>Moreover, the temporary file gets deleted soon after its creation.<br><br>The solution is to use&nbsp;</span><span style="background-color: var(--hig);"><a target="_blank" rel="nofollow" href="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/nio/file/Files.html#createTempFile(java.lang.String,java.lang.String,java.nio.file.attribute.FileAttribute...)">Files.createTempFile</a></span><span style="background-color: var(--wht);">&nbsp;instead.<br><br>We recommend that all users upgrade to the latest version of Apache Storm.</span></div><div><span style="background-color: var(--wht);"><br></span></div><br>

### References
* https://lists.apache.org/thread/88oc1vqfjtr29cz5xts0v2wm5pmhbm0l


### Credits
* Andrea Cosentino from Apache Software Foundation (finder)


## Unsafe Pre-Authentication Deserialization In Workers ## { #CVE-2021-40865 }

CVE-2021-40865 [\[CVE json\]](./CVE-2021-40865.cve.json) [\[OSV json\]](./CVE-2021-40865.osv.json)



_Last updated: 2021-10-21T21:27:58.697Z_

### Affected

* Apache Storm from v1.0.0 before Apache Storm *
* Apache Storm from Apache Storm before v1.2.4


### Description

An Unsafe Deserialization vulnerability exists in the worker services of the Apache Storm supervisor server allowing pre-auth Remote Code Execution (RCE).  Apache Storm 2.2.x users should upgrade to version 2.2.1 or 2.3.0. Apache Storm 2.1.x users should upgrade to version 2.1.1. Apache Storm 1.x users should upgrade to version 1.2.4

### References
* https://lists.apache.org/thread.html/r8d45e74299897b6734dd0f788c46a631009ce2eeb731523386f7a253%40%3Cuser.storm.apache.org%3E
* https://seclists.org/oss-sec/2021/q4/45


### Credits
* Apache Storm would like to thank @pwntester Alvaro Muñoz of the GitHub Security Lab team for reporting this issue.


## Shell Command Injection Vulnerability in Nimbus Thrift Server ## { #CVE-2021-38294 }

CVE-2021-38294 [\[CVE json\]](./CVE-2021-38294.cve.json) [\[OSV json\]](./CVE-2021-38294.osv.json)



_Last updated: 2021-10-21T22:16:43.838Z_

### Affected

* Apache Storm from v1.0.0 before Apache Storm*
* Apache Storm from Apache Storm before v1.2.4


### Description

A Command Injection vulnerability exists in the getTopologyHistory service of the Apache Storm 2.x prior to 2.2.1 and Apache Storm 1.x prior to 1.2.4. A specially crafted thrift request to the Nimbus server allows Remote Code Execution (RCE) prior to authentication. 

### References
* https://lists.apache.org/thread.html/r5fe881f6ca883908b7a0f005d35115af49f43beea7a8b0915e377859%40%3Cuser.storm.apache.org%3E
* https://seclists.org/oss-sec/2021/q4/44


### Credits
* Apache Storm would like to thank @pwntester Alvaro Muñoz of the GitHub Security Lab team for reporting this issue.
