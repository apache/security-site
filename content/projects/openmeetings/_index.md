---
title: Apache OpenMeetings security advisories
description: Security information for Apache OpenMeetings
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache OpenMeetings? You can read more about the projects' security policy on their [security page](https://openmeetings.apache.org/security.html), and email your report to the [Apache OpenMeetings Security Team](mailto:security@openmeetings.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://openmeetings.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Arbitrary File Read ## { #CVE-2026-49488 }

CVE-2026-49488 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49488) [\[CVE json\]](./CVE-2026-49488.cve.json) [\[OSV json\]](./CVE-2026-49488.osv.json)



_Last updated: 2026-07-14T09:51:40.069Z_

### Affected

* Apache OpenMeetings from 5.0.0 before 9.1.0


### Description

<p>Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache OpenMeetings.</p><p>This issue affects Apache OpenMeetings: from 5.0.0 before 9.1.0.<br><span style="background-color: rgb(255, 255, 255);">An attacker with moderator rights in any room can read arbitrary files accessible to the OS account running the OM server, including credentials and secrets, via a crafted download request.</span></p><p>Users are recommended to upgrade to version 9.1.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/74zf32shox9oy62b7t55mvcj874bxqnj


### Credits
* follycat and Y0n3er (finder)


## Login Credentials Passed via GET Query Parameters ## { #CVE-2026-34020 }

CVE-2026-34020 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34020) [\[CVE json\]](./CVE-2026-34020.cve.json) [\[OSV json\]](./CVE-2026-34020.osv.json)



_Last updated: 2026-04-09T15:52:02.110Z_

### Affected

* Apache OpenMeetings from 3.1.3 before 9.0.0


### Description

<p>Use of GET Request Method With Sensitive Query Strings vulnerability in Apache OpenMeetings.</p><p>The REST login endpoint uses HTTP GET method with username and password passed as query parameters.&nbsp;<span style="background-color: rgb(255, 255, 255);">Please check references regarding possible impact</span><br></p><p>This issue affects Apache OpenMeetings: from 3.1.3 before 9.0.0.</p><p>Users are recommended to upgrade to version 9.0.0, which fixes the issue.</p>

### References
* https://owasp.org/www-community/vulnerabilities/Information_exposure_through_query_strings_in_url
* https://lists.apache.org/thread/2h3h9do5tp17xldr0nps1yjmkx4vs3db


### Credits
* 4ra2n (A code security AI agent) (finder)


## Hardcoded Remember-Me Cookie Encryption Key and Salt ## { #CVE-2026-33266 }

CVE-2026-33266 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33266) [\[CVE json\]](./CVE-2026-33266.cve.json) [\[OSV json\]](./CVE-2026-33266.osv.json)



_Last updated: 2026-04-09T15:52:32.475Z_

### Affected

* Apache OpenMeetings from 6.1.0 before 9.0.0


### Description

<p>Use of Hard-coded Cryptographic Key vulnerability in Apache OpenMeetings.</p><p>The remember-me cookie encryption key is set to default value in openmeetings.properties and not being auto-rotated. <span style="background-color: rgb(255, 255, 255);">In case OM admin hasn't changed the default encryption key, an attacker who has stolen a cookie from a logged-in user can get full user credentials.</span><br></p><p>This issue affects Apache OpenMeetings: from 6.1.0 before 9.0.0.</p><p>Users are recommended to upgrade to version 9.0.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/b05jnp9563v49zq494lox9kjbhhf2w66


### Credits
* 4ra2n (A code security AI agent) (finder)


## Insufficient checks in FileWebService ## { #CVE-2026-33005 }

CVE-2026-33005 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33005) [\[CVE json\]](./CVE-2026-33005.cve.json) [\[OSV json\]](./CVE-2026-33005.osv.json)



_Last updated: 2026-04-09T15:52:49.573Z_

### Affected

* Apache OpenMeetings from 3.1.0 before 9.0.0


### Description

<p>Improper Handling of Insufficient Privileges vulnerability in Apache OpenMeetings.</p><p>Any registered user can query web service with their credentials and get files/sub-folders of any folder by ID (metadata only NOT contents). Metadata includes id, type, name and some other field. Full list of fields get be checked at&nbsp;FileItemDTO&nbsp;object.</p><p>This issue affects Apache OpenMeetings: from 3.10 before 9.0.0.</p><p>Users are recommended to upgrade to version 9.0.0, which fixes the issue.</p>

### References
* https://openmeetings.apache.org/openmeetings-db/apidocs/org.apache.openmeetings.db/org/apache/openmeetings/db/dto/file/FileItemDTO.html
* https://lists.apache.org/thread/pttoprd628g3xr6lpp3bm1z8m3z8t4p7


### Credits
* 4ra2n (A code security AI agent) (finder)


## Deserialisation of untrusted data in cluster mode ## { #CVE-2024-54676 }

CVE-2024-54676 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-54676) [\[CVE json\]](./CVE-2024-54676.cve.json) [\[OSV json\]](./CVE-2024-54676.osv.json)



_Last updated: 2025-01-08T08:40:01.385Z_

### Affected

* Apache OpenMeetings from 2.1 before 8.0.0


### Description

<p>Vendor: The Apache Software Foundation</p><p>Versions Affected: Apache OpenMeetings from 2.1.0 before 8.0.0</p>Description: Default clustering instructions at <a target="_blank" rel="nofollow" href="https://openmeetings.apache.org/Clustering.html">https://openmeetings.apache.org/Clustering.html</a>&nbsp;doesn't specify white/black lists for OpenJPA this leads to possible <span style="background-color: rgb(255, 255, 255);">deserialisation of untrusted data</span>.<br>Users are recommended to upgrade to version 8.0.0 and <span style="background-color: rgb(255, 255, 255);">update their startup scripts to include the relevant </span><code>'openjpa.serialization.class.blacklist' and 'openjpa.serialization.class.whitelist' configurations as shown in the documentation</code>.

### References
* https://lists.apache.org/thread/o0k05jxrt5tp4nm45lj14yfjxmg67m95


### Credits
* m0d9 from Tencent Yunding Lab (reporter)


## allows null-byte Injection ## { #CVE-2023-29246 }

CVE-2023-29246 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-29246) [\[CVE json\]](./CVE-2023-29246.cve.json) [\[OSV json\]](./CVE-2023-29246.osv.json)



_Last updated: 2023-05-12T01:21:14.732Z_

### Affected

* Apache OpenMeetings from 2.0.0 before 7.1.0


### Description

<span style="background-color: rgb(255, 255, 255);">An attacker who has gained access to an admin account can perform RCE via null-byte injection</span><br><br>Vendor: The Apache Software Foundation<br><br>Versions Affected: Apache OpenMeetings from 2.0.0 before 7.1.0

### References
* https://lists.apache.org/thread/230plvhbdx26m43b0sy942wlwt6kkmmr


### Credits
* Stefan Schiller (reporter)


## allows bypass authentication ## { #CVE-2023-29032 }

CVE-2023-29032 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-29032) [\[CVE json\]](./CVE-2023-29032.cve.json) [\[OSV json\]](./CVE-2023-29032.osv.json)



_Last updated: 2023-05-12T01:19:51.993Z_

### Affected

* Apache OpenMeetings from 3.1.3 before 7.1.0


### Description

<span style="background-color: rgb(255, 255, 255);">An attacker that has gained access to certain private information can use this to act as other user.</span><br><br>Vendor: The Apache Software Foundation<br><br>Versions Affected: Apache OpenMeetings from 3.1.3 before 7.1.0

### References
* https://lists.apache.org/thread/j2d6mg3rzcphfd8vvvk09d8p4o9lvnqp


### Credits
* Stefan Schiller (reporter)


## insufficient check of invitation hash ## { #CVE-2023-28936 }

CVE-2023-28936 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-28936) [\[CVE json\]](./CVE-2023-28936.cve.json) [\[OSV json\]](./CVE-2023-28936.osv.json)



_Last updated: 2023-05-12T01:19:31.368Z_

### Affected

* Apache OpenMeetings from 2.0.0 before 7.1.0


### Description

Attacker can access arbitrary recording/room<br><br>Vendor: The Apache Software Foundation<br><br>Versions&nbsp;Affected: Apache OpenMeetings from 2.0.0 before 7.1.0<br>

### References
* https://lists.apache.org/thread/y6vng44c22ll221rtvsv208x1pbjmdoc


### Credits
* Stefan Schiller (reporter)


## allows user impersonation ## { #CVE-2023-28326 }

CVE-2023-28326 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-28326) [\[CVE json\]](./CVE-2023-28326.cve.json) [\[OSV json\]](./CVE-2023-28326.osv.json)



_Last updated: 2023-03-28T14:34:57.762Z_

### Affected

* Apache OpenMeetings from 2.0.0 before 7.0.0


### Description

<p>Vendor: The Apache Software Foundation</p><p>Versions Affected: Apache OpenMeetings from 2.0.0 before 7.0.0</p><p>Description: Attacker can elevate their privileges in any room</p><br>

### References
* https://lists.apache.org/thread/r9vn12dp5yofn1h3wd5x4h7c3vmmr5d9


### Credits
* Dennis Zimmt (reporter)


## Apache OpenMeetings: bandwidth can be overloaded with public web service ## { #CVE-2021-27576 }

CVE-2021-27576 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-27576) [\[CVE json\]](./CVE-2021-27576.cve.json) [\[OSV json\]](./CVE-2021-27576.osv.json)



_Last updated: 2021-03-14T11:56:54.481Z_

### Affected

* Apache OpenMeetings from 4.0.0 before Apache OpenMeetings 4*
* Apache OpenMeetings from Apache OpenMeetings 5 through 5.1.0


### Description

If was found that the NetTest web service can be used to overload the bandwidth of a Apache OpenMeetings server.  This issue was addressed in Apache OpenMeetings 6.0.0

### References
* https://lists.apache.org/thread.html/r9bb615bd70a0197368f5f3ffc887162686caeb0b5fc30592a7a871e9%40%3Cuser.openmeetings.apache.org%3E


### Credits
* This issue was identified by Trung Le, Chi Tran, Linh Cua
