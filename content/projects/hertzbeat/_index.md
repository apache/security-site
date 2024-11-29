---
title: Apache HertzBeat (Incubating) security advisories
description: Security information for Apache HertzBeat (Incubating)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache HertzBeat (Incubating)? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## RCE by notice template injection vulnerability ## { #CVE-2024-41151 }

CVE-2024-41151 [\[CVE json\]](./CVE-2024-41151.cve.json) [\[OSV json\]](./CVE-2024-41151.osv.json)



_Last updated: 2024-11-18T08:45:47.594Z_

### Affected

* Apache HertzBeat before 1.6.1


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache HertzBeat.</p>This vulnerability can only be exploited by authorized attackers.<br><p></p><p>This issue affects Apache HertzBeat: before 1.6.1.</p><p>Users are recommended to upgrade to version 1.6.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/p33tg0vo5nh6kscth4262ktsqo3h5lqo
* https://lists.apache.org/thread/oor9nw6nh2ojnfw8d8oxrv40cbtk5mwj


### Credits
* Li Yi Wei (finder)
* Elin Kai (finder)


## RCE by snakeYaml deser load malicious xml  ## { #CVE-2024-42323 }

CVE-2024-42323 [\[CVE json\]](./CVE-2024-42323.cve.json) [\[OSV json\]](./CVE-2024-42323.osv.json)



_Last updated: 2024-09-21T09:30:13.062Z_

### Affected

* Apache HertzBeat before 1.6.0


### Description

<p>SnakeYaml Deser Load Malicious xml rce vulnerability in Apache HertzBeat (incubating).&nbsp;</p>This vulnerability can only be exploited by authorized attackers.<br><p>This issue affects Apache HertzBeat (incubating): before 1.6.0.</p><p>Users are recommended to upgrade to version 1.6.0, which fixes the issue.</p><br>

### References
* https://lists.apache.org/thread/r0c4tost4bllqc1n9q6rmzs1slgsq63t
* https://lists.apache.org/thread/dwpwm572sbwon1mknlwhkpbom2y7skbx


### Credits
* Yulate (reporter)
* Liufeng Yi  (reporter)


## Exists Native Deser RCE and file writing vulnerabilities ## { #CVE-2024-45505 }

CVE-2024-45505 [\[CVE json\]](./CVE-2024-45505.cve.json) [\[OSV json\]](./CVE-2024-45505.osv.json)



_Last updated: 2024-11-18T08:44:44.304Z_

### Affected

* Apache HertzBeat before 1.6.1


### Description

<p>Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache HertzBeat (incubating).</p>This vulnerability can only be exploited by authorized attackers.<br><p>This issue affects Apache HertzBeat (incubating): before 1.6.1.</p><p>Users are recommended to upgrade to version 1.6.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/h8k14o1bfyod66p113pkgnt1s52p6p19
* https://lists.apache.org/thread/gvbc68krhqhht7mkkkx7k13k6k6fdhy0


### Credits
* Unam4 (finder)
* Springkilll (finder)
* yemoli (finder)
* yulate (finder)


## Exposure sensitive token via http GET method with query string ## { #CVE-2024-45791 }

CVE-2024-45791 [\[CVE json\]](./CVE-2024-45791.cve.json) [\[OSV json\]](./CVE-2024-45791.osv.json)



_Last updated: 2024-11-18T08:45:21.798Z_

### Affected

* Apache HertzBeat before 1.6.1


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache HertzBeat.</p><p>This issue affects Apache HertzBeat: before 1.6.1.</p><p>Users are recommended to upgrade to version 1.6.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/jmbsfjsvrfnvosh1ftrm3ry4j3sb7doz
* https://lists.apache.org/thread/lvsczrp8kdynppmzyxtkh4ord4gpw1ph


### Credits
* Ícaro Torres (finder)
