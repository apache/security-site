---
title: Apache Struts security advisories
description: Security information for Apache Struts
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Struts? You can read more about the projects' security policy on their [security page](https://struts.apache.org/security.html), and email your report to the [Apache Struts Security Team](mailto:security@struts.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://struts.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Forced OGNL evaluation, when evaluated on raw not validated user input in tag attributes, may lead to RCE. ## { #CVE-2021-31805 }

CVE-2021-31805 [\[CVE json\]](./CVE-2021-31805.cve.json) [\[OSV json\]](./CVE-2021-31805.osv.json)



_Last updated: 2022-04-12T15:23:33.186Z_

### Affected

* Apache Struts at 2.0.0 to 2.5.29


### Description

The fix issued for CVE-2020-17530 was incomplete. So from Apache Struts 2.0.0 to 2.5.29, still some of the tag’s attributes could perform a double evaluation if a developer applied forced OGNL evaluation by using the %{...} syntax. Using forced OGNL evaluation on untrusted user input can lead to a Remote Code Execution and security degradation.

### References
* https://cwiki.apache.org/confluence/display/WW/S2-062


### Credits
* Apache Struts would like to thank Chris McCown for reporting this issue!


## DoS via OOM owing to not properly checking of list bounds ## { #CVE-2023-34149 }

CVE-2023-34149 [\[CVE json\]](./CVE-2023-34149.cve.json) [\[OSV json\]](./CVE-2023-34149.osv.json)



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


## DoS via OOM owing to no sanity limit on normal form fields in multipart forms ## { #CVE-2023-34396 }

CVE-2023-34396 [\[CVE json\]](./CVE-2023-34396.cve.json) [\[OSV json\]](./CVE-2023-34396.osv.json)



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


## excessive disk usage ## { #CVE-2023-41835 }

CVE-2023-41835 [\[CVE json\]](./CVE-2023-41835.cve.json)

_Last updated: 2023-12-12T08:42:17.762Z_

### Affected

* Apache Struts from 2.0.0 through 2.5.31
* Apache Struts from 6.1.2.1 through 6.3.0


### Description

<span style="background-color: rgb(255, 255, 255);">When a Multipart request is performed but some of the fields exceed the </span><code>maxStringLength</code><span style="background-color: rgb(255, 255, 255);">&nbsp; limit, the upload files will remain in </span><code>struts.multipart.saveDir</code><span style="background-color: rgb(255, 255, 255);">&nbsp; even if the request has been denied.</span><br>Users are recommended to upgrade to versions <span style="background-color: rgb(255, 255, 255);">Struts 2.5.32 or 6.1.2.2 or Struts 6.3.0.1 or greater</span>, which fixe this issue.

### References
* https://lists.apache.org/thread/6wj530kh3ono8phr642y9sqkl67ys2ft
* https://www.openwall.com/lists/oss-security/2023/12/09/1


## File upload component had a directory traversal vulnerability ## { #CVE-2023-50164 }

CVE-2023-50164 [\[CVE json\]](./CVE-2023-50164.cve.json)

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
