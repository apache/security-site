---
title: Apache ServiceComb security advisories
description: Security information for Apache ServiceComb
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ServiceComb? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## attacker can perform SSRF through the frontend API ## { #CVE-2023-44313 }

CVE-2023-44313 [\[CVE json\]](./CVE-2023-44313.cve.json) [\[OSV json\]](./CVE-2023-44313.osv.json)



_Last updated: 2024-01-31T08:49:43.083Z_

### Affected

* Apache ServiceComb Service-Center through 2.1.0


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache ServiceComb Service-Center. Attackers can obtain sensitive server information through specially crafted requests.<p>This issue affects Apache ServiceComb before 2.1.0(include).</p><p>Users are recommended to upgrade to version 2.2.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/kxovd455o9h4f2v811hcov2qknbwld5r


### Credits
* 苏 安 <suanwell@hotmail.com> (finder)


## attacker can query all environment variables of the service-center server ## { #CVE-2023-44312 }

CVE-2023-44312 [\[CVE json\]](./CVE-2023-44312.cve.json) [\[OSV json\]](./CVE-2023-44312.osv.json)



_Last updated: 2024-01-31T08:49:10.176Z_

### Affected

* Apache ServiceComb Service-Center through 2.1.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor in Apache ServiceComb Service-Center.<p>This issue affects 

Apache ServiceComb Service-Center

 before 2.1.0 (include).</p><p>Users are recommended to upgrade to version 2.2.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/dkvlgnrmc17qzjdy9k0cr60wpzcssk1s


### Credits
* 苏 安 <suanwell@hotmail.com> (finder)


## ServiceComb ServiceCenter Directory Traversal ## { #CVE-2021-21501 }

CVE-2021-21501 [\[CVE json\]](./CVE-2021-21501.cve.json) [\[OSV json\]](./CVE-2021-21501.osv.json)



_Last updated: 2021-08-10T09:15:53.939Z_

### Affected

* Apache ServiceComb from Apache ServiceComb-Service-Center 1.x before 2.0.0


### Description

Improper configuration will cause ServiceComb ServiceCenter Directory Traversal problem in ServcieCenter 1.x.x versions and fixed in 2.0.0.

### References
* https://lists.apache.org/thread.html/r337be65e504eac52a12e89d7de40345e5d335deee9dd7288f7f59b81%40%3Cdev.servicecomb.apache.org%3E


## Apache ServiceComb Yaml remote deserialization vulnerability ## { #CVE-2020-17532 }

CVE-2020-17532 [\[CVE json\]](./CVE-2020-17532.cve.json) [\[OSV json\]](./CVE-2020-17532.osv.json)



_Last updated: 2021-01-25T09:21:23.271Z_

### Affected

* Apache ServiceComb-Java-Chassis at Apache ServiceComb-Java-Chassis 2.x 2.0.0 to 2.1.3


### Description

When handler-router component is enabled in servicecomb-java-chassis, authenticated user may inject some data and cause arbitrary code execution.
The problem happens in versions between 2.0.0 ~ 2.1.3 and fixed in Apache ServiceComb-Java-Chassis 2.1.5

### References
* https://seclists.org/oss-sec/2021/q1/60
* https://issues.apache.org/jira/browse/SCB-2145
