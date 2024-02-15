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

## SQL injection from unauthorized login ## { #CVE-2023-37924 }

CVE-2023-37924 [\[CVE json\]](./CVE-2023-37924.cve.json)

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


## Fix CVE-2022-1471 SnakeYaml unsafe deserialization ## { #CVE-2023-46302 }

CVE-2023-46302 [\[CVE json\]](./CVE-2023-46302.cve.json)

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
