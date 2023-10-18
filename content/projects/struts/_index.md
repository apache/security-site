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

CVE-2021-31805 [\[CVE json\]](./CVE-2021-31805.cve.json)

### Affected

* Apache Struts at 2.0.0 to 2.5.29


### Description

The fix issued for CVE-2020-17530 was incomplete. So from Apache Struts 2.0.0 to 2.5.29, still some of the tag’s attributes could perform a double evaluation if a developer applied forced OGNL evaluation by using the %{...} syntax. Using forced OGNL evaluation on untrusted user input can lead to a Remote Code Execution and security degradation.

### References
* https://cwiki.apache.org/confluence/display/WW/S2-062


### Credits
* Apache Struts would like to thank Chris McCown for reporting this issue!


## DoS via OOM owing to not properly checking of list bounds ## { #CVE-2023-34149 }

CVE-2023-34149 [\[CVE json\]](./CVE-2023-34149.cve.json)

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

CVE-2023-34396 [\[CVE json\]](./CVE-2023-34396.cve.json)

### Affected

* Apache Struts through 2.5.30
* Apache Struts through 6.1.2


### Description

Allocation of Resources Without Limits or Throttling vulnerability in Apache Software Foundation Apache Struts.<p>This issue affects Apache Struts: through 2.5.30, through 6.1.2.</p><p>Upgrade to Struts 2.5.31 or 6.1.2.1 or greater<br></p>

### References
* https://cwiki.apache.org/confluence/display/WW/S2-064


### Credits
* Matthew McClain (finder)
