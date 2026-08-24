---
title: Apache Struts security advisories
description: Security information for Apache Struts
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Struts? Send your report to the [Apache Struts Security Team](mailto:security@struts.apache.org?subject=Struts).

You can read more about the security policy on:

- [Apache Struts security model](https://github.com/apache/struts/blob/main/THREAT_MODEL.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unbounded growth of localized-text caches driven by the request locale ## { #CVE-2026-73635 }

CVE-2026-73635 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73635) [\[CVE json\]](./CVE-2026-73635.cve.json) [\[OSV json\]](./CVE-2026-73635.osv.json)



_Last updated: 2026-08-15T10:38:06.706Z_

### Affected

* Apache Struts from 2.0.0 through 2.3.37
* Apache Struts from 2.5.0 through 2.5.33
* Apache Struts from 6.0.0 through 6.10.0
* Apache Struts from 7.0.0 through 7.2.1


### Description

Allocation of resources without limits or throttling vulnerability in Apache Struts. When no fixed locale is configured, the locale used for localized-text lookups is taken from the incoming request, allowing an unauthenticated remote client to cause the framework's internal localized-text caches to grow without bound and exhaust the Java heap, denying service to other users. Applications that configure a fixed locale are not affected.<br><br>This issue affects Apache Struts: from 2.0.0 through 2.3.37, from 2.5.0 through 2.5.33, from 6.0.0 through 6.10.0, from 7.0.0 through 7.2.1.<br><br>Users are recommended to upgrade to version 6.11.0 or 7.3.0, which fixes the issue.

### References
* https://cwiki.apache.org/confluence/display/WW/S2-074


### Credits
* Kuniyoshi Noguchi (野口 晋義), (@KuniNogu) (finder)


## Unbounded read of a Content Security Policy violation report ## { #CVE-2026-73634 }

CVE-2026-73634 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73634) [\[CVE json\]](./CVE-2026-73634.cve.json) [\[OSV json\]](./CVE-2026-73634.osv.json)



_Last updated: 2026-08-15T10:37:36.431Z_

### Affected

* Apache Struts from 6.0.0 through 6.10.0
* Apache Struts from 7.0.0 through 7.2.1


### Description

Uncontrolled resource consumption vulnerability in Apache Struts. An application that exposes an endpoint collecting Content Security Policy violation reports reads the submitted report into memory without bounding how much it will accept, so a single request can exhaust the heap and deny service to other users. Such endpoints are ordinarily reachable without authentication. The core distribution maps no such endpoint by default; applications that do not collect violation reports are not affected.<br><br>This issue affects Apache Struts: from 6.0.0 through 6.10.0, from 7.0.0 through 7.2.1.<br><br>Users are recommended to upgrade to version 6.11.0 or 7.3.0, which fixes the issue.

### References
* https://cwiki.apache.org/confluence/display/WW/S2-073


### Credits
* Michael Mullins (finder)


## Unbounded read of a JSON request body ## { #CVE-2026-73633 }

CVE-2026-73633 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73633) [\[CVE json\]](./CVE-2026-73633.cve.json) [\[OSV json\]](./CVE-2026-73633.osv.json)



_Last updated: 2026-08-14T13:48:43.280Z_

### Affected

* Apache Struts from 2.1.8 through 2.3.37
* Apache Struts from 2.5.0 through 2.5.33
* Apache Struts from 6.0.0 through 6.10.0
* Apache Struts from 7.0.0 through 7.2.1


### Description

Uncontrolled resource consumption vulnerability in the JSON plugin of Apache Struts. When an application is configured to populate actions from a JSON request body, the plugin reads that body into memory without bounding how much it will accept, so a single request can exhaust the heap and deny service to other users. The plugin's configurable JSON input length limit does not bound this read. The JSON plugin is an optional component; applications that do not use it, or use it without enabling JSON request-body handling, are not affected.<br><br>This issue affects Apache Struts: from 2.1.8 through 2.3.37, from 2.5.0 through 2.5.33, from 6.0.0 through 6.10.0, from 7.0.0 through 7.2.1.<br><br>Users are recommended to upgrade to version 6.11.0 or 7.3.0, which fixes the issue.

### References
* https://cwiki.apache.org/confluence/display/WW/S2-072


### Credits
* Michael Mullins (finder)


## Shared serialization state in the JSON plugin ## { #CVE-2026-73632 }

CVE-2026-73632 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73632) [\[CVE json\]](./CVE-2026-73632.cve.json) [\[OSV json\]](./CVE-2026-73632.osv.json)



_Last updated: 2026-08-15T10:38:52.132Z_

### Affected

* Apache Struts at 7.2.1


### Description

Exposure of data element to wrong session vulnerability in the JSON plugin of Apache Struts. Per-response serialization state could be shared across concurrent requests, allowing response content associated with one request to become observable in another. Only the SMD / JSON-RPC handling of the JSON interceptor is affected, which is not enabled by default; applications using the json result type are not affected.<br><br>This issue affects Apache Struts: 7.2.1.<br><br>Users are recommended to upgrade to version 7.3.0, which fixes the issue.

### References
* https://cwiki.apache.org/confluence/display/WW/S2-071


### Credits
* g0w6y (https://github.com/g0w6y) (finder)


## Shared parsing state in the JSON plugin ## { #CVE-2026-73631 }

CVE-2026-73631 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73631) [\[CVE json\]](./CVE-2026-73631.cve.json) [\[OSV json\]](./CVE-2026-73631.osv.json)



_Last updated: 2026-08-15T10:38:27.083Z_

### Affected

* Apache Struts at 7.2.1


### Description

Exposure of data element to wrong session vulnerability in the JSON plugin of Apache Struts. Per-request parsing state could be shared across concurrent requests, allowing data associated with one request to become observable in another, and configured parsing limits not to be enforced as intended. Populating actions from a JSON request body is not enabled by default; applications that do not use the JSON plugin are not affected.<br><br>This issue affects Apache Struts: 7.2.1.<br><br>Users are recommended to upgrade to version 7.3.0, which fixes the issue.

### References
* https://cwiki.apache.org/confluence/display/WW/S2-070


### Credits
* g0w6y (https://github.com/g0w6y) (finder)


## XXE vulnerability in outdated XWork component ## { #CVE-2025-68493 }

CVE-2025-68493 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-68493) [\[CVE json\]](./CVE-2025-68493.cve.json) [\[OSV json\]](./CVE-2025-68493.osv.json)



_Last updated: 2026-03-11T15:11:35.231Z_

### Affected

* Apache Struts from 2.0.0 before 2.2.1
* Apache Struts from 2.2.1 through 6.1.0


### Description

<p>Missing XML Validation vulnerability in Apache Struts, Apache Struts.</p><p>This issue affects Apache Struts: from 2.0.0 before 2.2.1; Apache Struts: from 2.2.1 through 6.1.0.</p><p>Users are recommended to upgrade to version 6.1.1, which fixes the issue.</p>

### References
* https://cwiki.apache.org/confluence/display/WW/S2-069


## File leak in multipart request processing causes disk exhaustion (DoS) - version ranges fixed ## { #CVE-2025-66675 }

CVE-2025-66675 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-66675) [\[CVE json\]](./CVE-2025-66675.cve.json) [\[OSV json\]](./CVE-2025-66675.osv.json)



_Last updated: 2025-12-10T07:13:32.174Z_

### Affected

* Apache Struts from 2.0.0 through 6.7.*
* Apache Struts from 7.0.0 through 7.0.*


### Description

<p>Denial of Service vulnerability in Apache Struts, f<span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">ile leak in multipart request processing causes disk exhaustion.</span></span></p><p>This issue affects Apache Struts: from 2.0.0 through 6.7.4, from 7.0.0 through 7.0.3.</p><p>Users are recommended to upgrade to version 6.8.0 or 7.1.1, which fixes the issue.<br><br>It's related to&nbsp;<span style="background-color: rgb(255, 255, 255);"><a target="_blank" rel="nofollow" href="https://cve.org/CVERecord?id=CVE-2025-64775">https://cve.org/CVERecord?id=CVE-2025-64775</a>&nbsp;- this CVE addresses missing affected version 6.7.4</span></p>

### References
* https://cwiki.apache.org/confluence/display/WW/S2-068
* https://cve.org/CVERecord?id=CVE-2025-64775


### Credits
* Nicolas Fournier (reporter)


## File leak in multipart request processing causes disk exhaustion (DoS) ## { #CVE-2025-64775 }

CVE-2025-64775 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-64775) [\[CVE json\]](./CVE-2025-64775.cve.json) [\[OSV json\]](./CVE-2025-64775.osv.json)



_Last updated: 2025-12-07T08:27:17.883Z_

### Affected

* Apache Struts from 2.0.0 through 6.7.0
* Apache Struts from 7.0.0 through 7.0.3


### Description

<p>Denial of Service vulnerability in Apache Struts, f<span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">ile leak in multipart request processing causes disk exhaustion.</span></span></p><p>This issue affects Apache Struts: from 2.0.0 through 6.7.0, from 7.0.0 through 7.0.3.</p><p>Users are recommended to upgrade to version 6.8.0 or 7.1.1, which fixes the issue.</p>

### References
* https://cwiki.apache.org/confluence/display/WW/S2-068


### Credits
* Nicolas Fournier (reporter)


## Improper Output Neutralization for Logs ## { #CVE-2025-54656 }

CVE-2025-54656 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-54656) [\[CVE json\]](./CVE-2025-54656.cve.json) [\[OSV json\]](./CVE-2025-54656.osv.json)



_Last updated: 2025-07-30T15:58:00.516Z_

### Affected

* Apache Struts Extras before 2


### Description

<p>** UNSUPPORTED WHEN ASSIGNED ** Improper Output Neutralization for Logs vulnerability in Apache Struts.</p><p>This issue affects Apache Struts Extras: before 2.</p><p>When using LookupDispatchAction, in some cases, Struts may print untrusted input to the logs without any filtering. Specially-crafted input may lead to log output where part of the message masquerades as a separate log line, confusing consumers of the logs (either human or automated).&nbsp;</p><p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.</p><p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://lists.apache.org/thread/so5cn07j2zn9vlf1xnfqp630wts719rr


### Credits
* Ryan Murphy of HeroDevs (finder)


## Mixing setters for uploaded files and normal fields can allow bypass file upload checks ## { #CVE-2024-53677 }

CVE-2024-53677 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-53677) [\[CVE json\]](./CVE-2024-53677.cve.json) [\[OSV json\]](./CVE-2024-53677.osv.json)



_Last updated: 2024-12-20T15:44:02.694Z_

### Affected

* Apache Struts from 2.0.0 before 6.4.0


### Description

<p>File upload logic in Apache Struts is flawed.&nbsp;<span style="background-color: rgb(255, 255, 255);">An attacker can manipulate file upload params to enable paths traversal and under some circumstances this can lead to uploading a malicious file which can be used to perform Remote Code Execution.</span></p><p>This issue affects Apache Struts: from 2.0.0 before 6.4.0.</p><p>Users are recommended to upgrade to version 6.4.0 at least and <span style="background-color: rgb(255, 255, 255);">migrate to the new </span><a target="_blank" rel="nofollow" href="https://struts.apache.org/core-developers/file-upload">file upload mechanism</a><span style="background-color: rgb(255, 255, 255);">. If you are not using an old file upload logic based on&nbsp;<b>FileuploadInterceptor</b>&nbsp;your application is safe.</span></p>You can find more details in&nbsp;<a target="_blank" rel="nofollow" href="https://cwiki.apache.org/confluence/display/WW/S2-067">https://cwiki.apache.org/confluence/display/WW/S2-067</a>

### References
* https://cwiki.apache.org/confluence/display/WW/S2-067


## File upload component had a directory traversal vulnerability ## { #CVE-2023-50164 }

CVE-2023-50164 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-50164) [\[CVE json\]](./CVE-2023-50164.cve.json) [\[OSV json\]](./CVE-2023-50164.osv.json)



_Last updated: 2023-12-12T09:26:27.763Z_

### Affected

* Apache Struts from 2.0.0 through 2.5.32
* Apache Struts from 6.0.0 through 6.3.0.1


### Description

<span style="background-color: rgb(255, 255, 255);">An attacker can manipulate file upload params to enable paths traversal and under some circumstances this can lead to uploading a malicious file which can be used to perform Remote Code Execution.</span><br>Users are recommended to upgrade to versions <span style="background-color: rgb(255, 255, 255);">Struts 2.5.33 or Struts 6.3.0.2 or greater to</span>&nbsp;fix this issue.<br>

### References
* https://lists.apache.org/thread/yh09b3fkf6vz5d6jdgrlvmg60lfwtqhj
* https://www.openwall.com/lists/oss-security/2023/12/07/1


### Credits
* Steven Seeley of Source Incite (reporter)


## excessive disk usage ## { #CVE-2023-41835 }

CVE-2023-41835 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-41835) [\[CVE json\]](./CVE-2023-41835.cve.json) [\[OSV json\]](./CVE-2023-41835.osv.json)



_Last updated: 2023-12-12T08:42:17.762Z_

### Affected

* Apache Struts from 2.0.0 through 2.5.31
* Apache Struts from 6.1.2.1 through 6.3.0


### Description

<span style="background-color: rgb(255, 255, 255);">When a Multipart request is performed but some of the fields exceed the </span><code>maxStringLength</code><span style="background-color: rgb(255, 255, 255);">&nbsp; limit, the upload files will remain in </span><code>struts.multipart.saveDir</code><span style="background-color: rgb(255, 255, 255);">&nbsp; even if the request has been denied.</span><br>Users are recommended to upgrade to versions <span style="background-color: rgb(255, 255, 255);">Struts 2.5.32 or 6.1.2.2 or Struts 6.3.0.1 or greater</span>, which fixe this issue.

### References
* https://lists.apache.org/thread/6wj530kh3ono8phr642y9sqkl67ys2ft
* https://www.openwall.com/lists/oss-security/2023/12/09/1


## DoS via OOM owing to no sanity limit on normal form fields in multipart forms ## { #CVE-2023-34396 }

CVE-2023-34396 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-34396) [\[CVE json\]](./CVE-2023-34396.cve.json) [\[OSV json\]](./CVE-2023-34396.osv.json)



_Last updated: 2023-06-14T07:50:57.318Z_

### Affected

* Apache Struts through 2.5.30
* Apache Struts through 6.1.2


### Description

Allocation of Resources Without Limits or Throttling vulnerability in Apache Software Foundation Apache Struts.<p>This issue affects Apache Struts: through 2.5.30, through 6.1.2.</p><p>Upgrade to Struts 2.5.31 or 6.1.2.1 or greater<br></p>

### References
* https://cwiki.apache.org/confluence/display/WW/S2-064


### Credits
* Matthew McClain (finder)


## DoS via OOM owing to not properly checking of list bounds ## { #CVE-2023-34149 }

CVE-2023-34149 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-34149) [\[CVE json\]](./CVE-2023-34149.cve.json) [\[OSV json\]](./CVE-2023-34149.osv.json)



_Last updated: 2023-06-14T07:48:49.995Z_

### Affected

* Apache Struts through 2.5.30
* Apache Struts through 6.1.2


### Description

Allocation of Resources Without Limits or Throttling vulnerability in Apache Software Foundation Apache Struts.<p>This issue affects Apache Struts: through 2.5.30, through 6.1.2.</p><p>Upgrade to Struts 2.5.31 or 6.1.2.1 or greater.<br></p>

### References
* https://cwiki.apache.org/confluence/display/WW/S2-063


### Credits
* Matthew McClain (finder)


## Forced OGNL evaluation, when evaluated on raw not validated user input in tag attributes, may lead to RCE. ## { #CVE-2021-31805 }

CVE-2021-31805 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-31805) [\[CVE json\]](./CVE-2021-31805.cve.json) [\[OSV json\]](./CVE-2021-31805.osv.json)



_Last updated: 2022-04-12T15:23:33.186Z_

### Affected

* Apache Struts at 2.0.0 to 2.5.29


### Description

The fix issued for CVE-2020-17530 was incomplete. So from Apache Struts 2.0.0 to 2.5.29, still some of the tag’s attributes could perform a double evaluation if a developer applied forced OGNL evaluation by using the %{...} syntax. Using forced OGNL evaluation on untrusted user input can lead to a Remote Code Execution and security degradation.

### References
* https://cwiki.apache.org/confluence/display/WW/S2-062


### Credits
* Apache Struts would like to thank Chris McCown for reporting this issue!
