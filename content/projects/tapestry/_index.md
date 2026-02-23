---
title: Apache Tapestry security advisories
description: Security information for Apache Tapestry
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Tapestry? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Tapestry prior to version 4 (EOL) allows RCE though deserialization of untrusted input ## { #CVE-2022-46366 }

CVE-2022-46366 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-46366) [\[CVE json\]](./CVE-2022-46366.cve.json) [\[OSV json\]](./CVE-2022-46366.osv.json)



_Last updated: 2022-12-02T13:44:12.576Z_

### Affected

* Apache Tapestry from Apache Tapestry before 4.0.0


### Description

Apache Tapestry 3.x allows deserialization of untrusted data, leading to remote code execution. This issue is similar to but distinct from CVE-2020-17531, which applies the the (also unsupported) 4.x version line. NOTE: This vulnerability only affects Apache Tapestry version line 3.x, which is no longer supported by the maintainer. Users are recommended to upgrade to a supported version line of Apache Tapestry

### References
* https://lists.apache.org/thread/bwn1vjrvz1hq0wbdzj23wz322244swhj


### Credits
* Apache would like to thank Ilyass El Hadi from Mandiant for reporting this issue


## Regular Expression Denial of Service (ReDoS) in ContentType.java. (GHSL-2022-022) ## { #CVE-2022-31781 }

CVE-2022-31781 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-31781) [\[CVE json\]](./CVE-2022-31781.cve.json) [\[OSV json\]](./CVE-2022-31781.osv.json)



_Last updated: 2022-07-13T07:23:23.997Z_

### Affected

* Apache Tapestry from 5.8.1 before 5.8.1


### Description

Apache Tapestry up to version 5.8.1 is vulnerable to Regular Expression Denial of Service (ReDoS) in the way it handles Content Types. Specially crafted Content Types may cause catastrophic backtracking, taking exponential time to complete. 

Specifically, this is about the regular expression used on the parameter of the org.apache.tapestry5.http.ContentType class.

Apache Tapestry 5.8.2 has a fix for this vulnerability. 

Notice the vulnerability cannot be triggered by web requests in Tapestry code alone. It would only happen if there's some non-Tapestry codepath passing some outside input to the ContentType class constructor.

### References
* https://www.openwall.com/lists/oss-security/2022/07/12/3


### Credits
* CodeQL team members [@atorralba (Tony Torralba)](https://github.com/atorralba) and [@joefarebrother (Joseph Farebrother)](https://github.com/joefarebrother).


## An Information Disclosure due to insufficient input validation exists in Apache Tapestry 5.4.0 and later ## { #CVE-2021-30638 }

CVE-2021-30638 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-30638) [\[CVE json\]](./CVE-2021-30638.cve.json) [\[OSV json\]](./CVE-2021-30638.osv.json)



_Last updated: 2021-04-27T18:27:24.498Z_

### Affected

* Apache Tapestry from Apache Tapestry  before Apache Tapestry 5.6.4
* Apache Tapestry from Apache Tapestry before Apache Tapestry 5.7.2


### Description

Information Exposure vulnerability in context asset handling of Apache Tapestry allows an attacker to download files inside WEB-INF if using a specially-constructed URL.  This was caused by an incomplete fix for CVE-2020-13953.  This issue affects Apache Tapestry Apache Tapestry 5.4.0 version to Apache Tapestry 5.6.3; Apache Tapestry 5.7.0 version and Apache Tapestry 5.7.1.



### References
* https://lists.apache.org/thread.html/r37dab61fc7f7088d4311e7f995ef4117d58d86a675f0256caa6991eb%40%3Cusers.tapestry.apache.org%3E


### Credits
* This vulnerability was discovered by Kc Udonsi of Trend Micro


## Bypass of the fix for CVE-2019-0195 ## { #CVE-2021-27850 }

CVE-2021-27850 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-27850) [\[CVE json\]](./CVE-2021-27850.cve.json) [\[OSV json\]](./CVE-2021-27850.osv.json)



_Last updated: 2021-04-15T07:35:21.760Z_

### Affected

* Apache Tapestry at Apache Tapestry 5.5.0
* Apache Tapestry at Apache Tapestry 5.7.0
* Apache Tapestry from Apache Tapestry 5.4.5 before Apache Tapestry 5.4.0*
* Apache Tapestry from Apache Tapestry 5.6.2 before Apache Tapestry 5.6.0*


### Description

A critical unauthenticated remote code execution vulnerability was found
all recent versions of Apache Tapestry.
The affected versions include 5.4.5, 5.5.0, 5.6.2 and 5.7.0.

The vulnerability I have found is a bypass of the fix for CVE-2019-0195.

Recap:

Before the fix of CVE-2019-0195 it was possible to download arbitrary
class files from the classpath by providing a crafted
asset file URL.
An attacker was able to download the file `AppModule.class` by
requesting the URL
`http://localhost:8080/assets/something/services/AppModule.class`
which contains a HMAC secret key.
The fix for that bug was a blacklist filter that checks if the URL
ends with `.class`, `.properties` or `.xml`.

Bypass:

Unfortunately, the blacklist solution can simply be bypassed by
appending a `/` at the end of the URL:

`http://localhost:8080/assets/something/services/AppModule.class/`
The slash is stripped after the blacklist check and the file
`AppModule.class` is loaded into the response.
This class usually contains the HMAC secret key which is used to sign
serialized Java objects.
With the knowledge of that key an attacker can sign a Java gadget
chain that leads to RCE (e.g. CommonsBeanUtils1 from ysoserial).Solution for this vulnerability:
* For Apache Tapestry 5.4.0 to 5.6.1, upgrade to 5.6.2 or later.
* For Apache Tapestry 5.7.0, upgrade to 5.7.1 or later.

### References
* https://lists.apache.org/thread.html/r237ff7f286bda31682c254550c1ebf92b0ec61329b32fbeb2d1c8751%40%3Cusers.tapestry.apache.org%3E


### Credits
* Apache Tapestry would like to thank Johannes Moritz for finding and notifying this vulnerability


## Deserialization flaw in EOL Tapestry 4. ## { #CVE-2020-17531 }

CVE-2020-17531 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17531) [\[CVE json\]](./CVE-2020-17531.cve.json) [\[OSV json\]](./CVE-2020-17531.osv.json)



_Last updated: 2020-12-08T12:41:08.137Z_

### Affected

* Apache Tapestry from Apache Tapestry 4 through 4


### Description

A Java Serialization vulnerability was found in Apache Tapestry 4. Apache Tapestry 4 will attempt to deserialize the "sp" parameter even before invoking the page's validate method, leading to deserialization without authentication.

Apache Tapestry 4 reached end of life in 2008 and no update to address this issue will be released.  Apache Tapestry 5 versions are not vulnerable to this issue.  Users of Apache Tapestry 4 should upgrade to the latest Apache Tapestry 5 version.

### References
* https://lists.apache.org/thread.html/r700a6aa234dbff0555d4187bdc8274d7e4c0afbf35b9a3457f09ee76%40%3Cusers.tapestry.apache.org%3E


### Credits
* Apache Tapestry would like to thank Adrian Bravo (@adrianbravon) for reporting this issue.
