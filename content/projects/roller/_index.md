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

## Insufficient Session Expiration on Password Change ## { #CVE-2025-24859 }

CVE-2025-24859 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-24859) [\[CVE json\]](./CVE-2025-24859.cve.json) [\[OSV json\]](./CVE-2025-24859.osv.json)



_Last updated: 2025-04-18T15:26:03.795Z_

### Affected

* Apache Roller from 1.0.0 before 6.1.5


### Description

<p></p><pre><code>A session management vulnerability exists in Apache Roller before version 6.1.5 where active user sessions are not properly invalidated after password changes. When a user's password is changed, either by the user themselves or by an administrator, existing sessions remain active and usable. This allows continued access to the application through old sessions even after password changes, potentially enabling unauthorized access if credentials were compromised.

This issue affects Apache Roller versions up to and including 6.1.4.

The vulnerability is fixed in Apache Roller 6.1.5 by implementing centralized session management that properly invalidates all active sessions when passwords are changed or users are disabled.
</code></pre><br><br><p></p>

### References
* https://lists.apache.org/thread/vxv52vdr8nhtjlj6v02w43fdvo0cxw23
* https://lists.apache.org/thread/4j906k16v21kdx8hk87gl7663sw7lg7f


### Credits
* Haining Meng (finder)


## Weakness in CSRF protection allows privilege escalation ## { #CVE-2024-46911 }

CVE-2024-46911 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-46911) [\[CVE json\]](./CVE-2024-46911.cve.json) [\[OSV json\]](./CVE-2024-46911.osv.json)



_Last updated: 2024-10-11T21:53:17.272Z_

### Affected

* Apache Roller from 1.0.0 before 6.1.4


### Description

<p>Cross-site Resource Forgery (CSRF), Privilege escalation vulnerability in Apache Roller. On multi-blog/user Roller websites, by default weblog owners are trusted to publish arbitrary weblog content and this combined with a deficiency in Roller's CSRF protections allowed an escalation of privileges attack. This issue affects Apache Roller before 6.1.4.</p><p>Roller users who run multi-blog/user Roller websites are recommended to upgrade to version 6.1.4, which fixes the issue.</p>Roller 6.1.4 release announcement:&nbsp;<a target="_blank" rel="nofollow" href="https://lists.apache.org/thread/3c3f6rwqptyw6wdc95654fq5vlosqdpw">https://lists.apache.org/thread/3c3f6rwqptyw6wdc95654fq5vlosqdpw</a><br><br>

### References
* https://lists.apache.org/thread/6m0ghjo9j92qty00t2qb6qf2spds0p5t


### Credits
* Chi Tran from EEVEE (finder)


## Insufficient input validation for some user profile and bookmark fields when Roller in untested-users mode ## { #CVE-2024-25090 }

CVE-2024-25090 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-25090) [\[CVE json\]](./CVE-2024-25090.cve.json) [\[OSV json\]](./CVE-2024-25090.osv.json)



_Last updated: 2024-07-26T08:36:45.293Z_

### Affected

* Apache Roller from 5.0.0 before 6.1.3


### Description

<p>Insufficient input validation and sanitation in Profile name &amp; screenname, Bookmark name &amp; description and blogroll name features in all versions of Apache Roller on all platforms allows an authenticated user to perform an XSS attack. Mitigation: if you do not have Roller configured for untrusted users, then you need to do nothing because you trust your users to author raw HTML and other web content. If you are running with untrusted users then you should upgrade to Roller 6.1.3.</p><p>This issue affects Apache Roller: from 5.0.0 before 6.1.3.</p><p>Users are recommended to upgrade to version 6.1.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lb50jqyxwf8jrfpydl6dc5zpqtpgrrwd


### Credits
* Jacob Hazak (reporter)


## Roller's weblog category, weblog settings and file-upload features did not properly sanitize input could be exploited to perform Reflected Cross Site Scripting (XSS) even on a Roller site configured for untrusted users. ## { #CVE-2023-37581 }

CVE-2023-37581 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-37581) [\[CVE json\]](./CVE-2023-37581.cve.json)

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


## regex injection leading to DoS ## { #CVE-2021-33580 }

CVE-2021-33580 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-33580) [\[CVE json\]](./CVE-2021-33580.cve.json) [\[OSV json\]](./CVE-2021-33580.osv.json)



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
