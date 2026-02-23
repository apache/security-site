---
title: Apache Submarine security advisories
description: Security information for Apache Submarine
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Submarine? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## authorization bypass ## { #CVE-2024-36265 }

CVE-2024-36265 [\[CVE json\]](./CVE-2024-36265.cve.json) [\[OSV json\]](./CVE-2024-36265.osv.json)



_Last updated: 2024-06-12T14:12:08.874Z_

### Affected

* Apache Submarine Server Core from 0.8.0 through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Incorrect Authorization vulnerability in Apache Submarine Server Core.</p><p>This issue affects Apache Submarine Server Core: from 0.8.0.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/prckhhst19qxof064hsm8cccxtofvflz


### Credits
* L0ne1y (finder)


## default secret ## { #CVE-2024-36264 }

CVE-2024-36264 [\[CVE json\]](./CVE-2024-36264.cve.json) [\[OSV json\]](./CVE-2024-36264.osv.json)



_Last updated: 2024-10-14T08:55:23.574Z_

### Affected

* Apache Submarine Commons Utils from 0.8.0 through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Improper Authentication vulnerability in Apache Submarine Commons Utils.</p><p>This issue affects Apache Submarine Commons Utils: from 0.8.0.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://github.com/apache/submarine/pull/1125
* https://lists.apache.org/thread/7mo0c7vbhpo8thvybl8wwvb0bccrg7r4


### Credits
* Jonathan Leitschuh (finder)
* L0ne1y (finder)


## SQL injection ## { #CVE-2024-36263 }

CVE-2024-36263 [\[CVE json\]](./CVE-2024-36263.cve.json) [\[OSV json\]](./CVE-2024-36263.osv.json)



_Last updated: 2024-06-12T14:05:08.215Z_

### Affected

* Apache Submarine Server Core through *


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Submarine Server Core.</p><p>This issue affects Apache Submarine Server Core: all versions.</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://github.com/apache/submarine/pull/1121
* https://lists.apache.org/thread/8q9kbdg9gk9kpz5p8x6t7q8709l3vrmt


### Credits
* BaoChengZhang of LengJingQiCaiSecurityLab (finder)
* L0ne1y (finder)


## Fix CVE-2022-1471 SnakeYaml unsafe deserialization ## { #CVE-2023-46302 }

CVE-2023-46302 [\[CVE json\]](./CVE-2023-46302.cve.json) [\[OSV json\]](./CVE-2023-46302.osv.json)



_Last updated: 2023-11-20T08:46:49.527Z_

### Affected

* Apache Submarine from 0.7.0 before 0.8.0


### Description

Apache Software Foundation Apache Submarine has a bug when serializing against yaml. The bug is caused by snakeyaml <a target="_blank" rel="nofollow" href="https://nvd.nist.gov/vuln/detail/CVE-2022-1471">https://nvd.nist.gov/vuln/detail/CVE-2022-1471</a>.<br><br>Apache Submarine uses JAXRS to define REST endpoints.  In order to
handle YAML requests (using application/yaml content-type), it defines
a YamlEntityProvider entity provider that will process all incoming
YAML requests.  In order to unmarshal the request, the readFrom method
is invoked, passing the entityStream containing the user-supplied data in `submarine-server/server-core/src/main/java/org/apache/submarine/server/utils/YamlUtils.java`.<br> <br>We have now fixed this issue in the new version by replacing to `jackson-dataformat-yaml`.<br>This issue affects Apache Submarine: from 0.7.0 before 0.8.0.&nbsp;<span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 0.8.0, which fixes this issue.<br><span style="background-color: rgb(255, 255, 255);">If using the version smaller than 0.8.0  and not want to upgrade, you can try cherry-pick PR <a target="_blank" rel="nofollow" href="https://github.com/apache/submarine/pull/1054">https://github.com/apache/submarine/pull/1054</a> and rebuild the submart-server image to fix this.</span><br><br></span><br>

### References
* https://issues.apache.org/jira/browse/SUBMARINE-1371
* https://github.com/apache/submarine/pull/1054
* https://lists.apache.org/thread/zf0wppzh239j4h131hm1dbswfnztxrr5


### Credits
* GHSL team member @jorgectf (Jorge Rosillo) (reporter)


## SQL injection from unauthorized login ## { #CVE-2023-37924 }

CVE-2023-37924 [\[CVE json\]](./CVE-2023-37924.cve.json) [\[OSV json\]](./CVE-2023-37924.osv.json)



_Last updated: 2023-11-22T09:19:18.697Z_

### Affected

* Apache Submarine from 0.7.0 before 0.8.0


### Description

Apache Software Foundation Apache Submarine has an SQL injection vulnerability when a user logs in. This issue can result in unauthorized login.<br><span style="background-color: rgb(255, 255, 255);">Now we have fixed this issue and now user must have the correct login to access workbench.</span><br><p>This issue affects Apache Submarine: from 0.7.0 before 0.8.0.&nbsp;<span style="background-color: rgb(255, 255, 255);">We recommend that all submarine users with 0.7.0 upgrade to 0.8.0, which not only fixes the issue, supports the oidc authentication mode, but also removes the case of unauthenticated logins.</span><span style="background-color: rgb(255, 255, 255);"><br><span style="background-color: rgb(255, 255, 255);">If using the version lower than 0.8.0 and not want to upgrade, you can try cherry-pick PR <a target="_blank" rel="nofollow" href="https://github.com/apache/submarine/pull/1054">https://github.com/apache/submarine/pull/1037</a> and rebuild the submarine-server image to fix this.</span><br></span></p>

### References
* https://issues.apache.org/jira/browse/SUBMARINE-1361
* https://github.com/apache/submarine/pull/1037
* https://lists.apache.org/thread/g99h773vd49n1wyghdq1llv2f83w1b3r


### Credits
* lengjingqicai(棱镜七彩开源安全研究院) (reporter)
