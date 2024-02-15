---
title: Apache Roller security advisories
description: Security information for Apache Roller
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Roller? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## regex injection leading to DoS ## { #CVE-2021-33580 }

CVE-2021-33580 [\[CVE json\]](./CVE-2021-33580.cve.json)

_Last updated: 2021-08-18T07:43:44.770Z_

### Affected

* Apache Roller from Apache Roller before 6.0.2


### Description

User controlled `request.getHeader("Referer")`, `request.getRequestURL()` and `request.getQueryString()` are used to build and run a regex expression.

The attacker doesn't have to use a browser and may send a specially crafted Referer header programmatically. Since the attacker controls the string and the regex pattern he may cause a ReDoS by regex catastrophic backtracking on the server side.  This problem has been fixed in Roller 6.0.2.





### References
* https://lists.apache.org/thread.html/r9d967d80af941717573e531db2c7353a90bfd0886e9b5d5d79f75506%40%3Cuser.roller.apache.org%3E


### Credits
* Apache Roller would like to thank Ed Ra (https://github.com/edvraa) for reporting this.


## Roller's weblog category, weblog settings and file-upload features did not properly sanitize input could be exploited to perform Reflected Cross Site Scripting (XSS) even on a Roller site configured for untrusted users. ## { #CVE-2023-37581 }

CVE-2023-37581 [\[CVE json\]](./CVE-2023-37581.cve.json)

_Last updated: 2023-08-24T08:15:22.581Z_

### Affected

* Apache Roller before 6.1.2


### Description

<span style="background-color: rgb(255, 255, 255);">Insufficient input validation and sanitation in Weblog Category name, Website About and File Upload features in all versions of Apache Roller on all platforms allows an authenticated user to perform an XSS attack. </span><span style="background-color: var(--wht);">Mitigation: if you do not have Roller configured for untrusted users, then you need to do nothing because you trust your users to author raw HTML and other web content. If you are running with untrusted users then you should upgrade to Roller 6.1.2 and you should disable Roller's File Upload feature. </span><br><br><p></p>

### References
* https://lists.apache.org/thread/n9mjhhlm7z7b7to646tkvf3otkf21flp
* https://www.openwall.com/lists/oss-security/2023/08/16/1


### Credits
* SecureLayer7 Technologies Pvt Ltd (finder)
