---
title: Apache Answer security advisories
description: Security information for Apache Answer
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Answer? You can read more about the projects' security policy on their [security page](https://answer.apache.org/community/security-model), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://answer.apache.org/community/security-model). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Revision API Improper Access Control leads to Information Disclosure ## { #CVE-2026-24735 }

CVE-2026-24735 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24735) [\[CVE json\]](./CVE-2026-24735.cve.json) [\[OSV json\]](./CVE-2026-24735.osv.json)



_Last updated: 2026-02-04T10:41:53.728Z_

### Affected

* Apache Answer through 1.7.1


### Description

<p>Exposure of Private Personal Information to an Unauthorized Actor vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 1.7.1.</p>An unauthenticated API endpoint incorrectly exposes full revision history for deleted content. This allows unauthorized user to retrieve restricted or sensitive information.<br><p>Users are recommended to upgrade to version 2.0.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/whxloom7mpxlyt5wzdskflsg5mzdzd60


### Credits
* Sho Odagiri of GMO Cybersecurity by Ierae, Inc. (reporter)


## Using externally referenced images can leak user privacy. ## { #CVE-2025-29868 }

CVE-2025-29868 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-29868) [\[CVE json\]](./CVE-2025-29868.cve.json) [\[OSV json\]](./CVE-2025-29868.osv.json)



_Last updated: 2025-04-01T07:56:26.883Z_

### Affected

* Apache Answer through 1.4.2


### Description

<p>Private Data Structure Returned From A Public Method vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 1.4.2.</p>If a user uses an externally referenced image, when a user accesses this image, the provider of the image may obtain private information about the ip address of that accessing user.<br><p>Users are recommended to upgrade to version 1.4.5, which fixes the issue.&nbsp;In the new version, administrators can set whether external content can be displayed.</p>

### References
* https://lists.apache.org/thread/l7pohw5g03g3qsvrz8pqc9t29mdv5lhf


### Credits
* Hamed Kohi (reporter)
* Luke Smith (reporter)


## Predictable Authorization Token Using UUIDv1 ## { #CVE-2024-45719 }

CVE-2024-45719 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45719) [\[CVE json\]](./CVE-2024-45719.cve.json) [\[OSV json\]](./CVE-2024-45719.osv.json)



_Last updated: 2024-11-22T14:36:42.714Z_

### Affected

* Apache Answer through 1.4.0


### Description

<p>Inadequate Encryption Strength vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 1.4.0.</p>The ids generated using the UUID v1 version are to some extent not secure enough. It can cause the generated token to be predictable.<br><p>Users are recommended to upgrade to version 1.4.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/sz2d0z39k01nbx3r9pj65t76o1hy9491


### Credits
* Chi Tran from Eevee (reporter)


## The link to reset the user's password will remain valid after sending a new link ## { #CVE-2024-41890 }

CVE-2024-41890 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-41890) [\[CVE json\]](./CVE-2024-41890.cve.json) [\[OSV json\]](./CVE-2024-41890.osv.json)



_Last updated: 2024-08-09T14:53:26.714Z_

### Affected

* Apache Answer through 1.3.5


### Description

<p>Missing Release of Resource after Effective Lifetime vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 1.3.5.</p>User sends multiple password reset emails, each containing a valid link. Within the link's validity period, this could potentially lead to the link being misused or hijacked.<br><p>Users are recommended to upgrade to version 1.3.6, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/j7c080xj31x8rvz1pyk2h47rdd9pwbv9


### Credits
* Mohammad Reza Omrani (reporter)


## The link for resetting user password is not Single-Use ## { #CVE-2024-41888 }

CVE-2024-41888 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-41888) [\[CVE json\]](./CVE-2024-41888.cve.json) [\[OSV json\]](./CVE-2024-41888.osv.json)



_Last updated: 2024-08-09T14:55:12.877Z_

### Affected

* Apache Answer through 1.3.5


### Description

<p>Missing Release of Resource after Effective Lifetime vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 1.3.5.</p>The password reset link remains valid within its expiration period even after it has been used. This could potentially lead to the link being misused or hijacked.<br><p>Users are recommended to upgrade to version 1.3.6, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/jbs1j2o9rqm5sc19jyk3jcfvkmfkmyf4


### Credits
* Mohammad Reza Omrani (reporter)


## Avatar URL leaked user email addresses ## { #CVE-2024-40761 }

CVE-2024-40761 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-40761) [\[CVE json\]](./CVE-2024-40761.cve.json) [\[OSV json\]](./CVE-2024-40761.osv.json)



_Last updated: 2024-09-25T07:31:07.119Z_

### Affected

* Apache Answer through 1.3.5


### Description

<p>Inadequate Encryption Strength vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 1.3.5.</p>Using the MD5 value of a user's email to access Gravatar is insecure and can lead to the leakage of user email. The official recommendation is to use SHA256 instead.<br><p>Users are recommended to upgrade to version 1.4.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/mmrhsfy16qwrw0pkv0p9kj40vy3sg08x


### Credits
* 张岳熙 (reporter)


## XSS vulnerability when changing personal website ## { #CVE-2024-29217 }

CVE-2024-29217 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-29217) [\[CVE json\]](./CVE-2024-29217.cve.json) [\[OSV json\]](./CVE-2024-29217.osv.json)



_Last updated: 2024-04-21T16:04:07.662Z_

### Affected

* Apache Answer before 1.3.0


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Answer.<p>This issue affects Apache Answer: before 1.3.0.</p>XSS attack when user changes personal website. A logged-in user, when modifying their personal website, can input malicious code in the website to create such an attack.<br><p>Users are recommended to upgrade to version [1.3.0], which fixes the issue.</p><p></p>

### References
* https://lists.apache.org/thread/nc0g1borr0d3wx25jm39pn7nyf268n0x


### Credits
* Tsubasa Umeuchi (reporter)


## Repeated submission at registration created duplicate users with the same name ## { #CVE-2024-26578 }

CVE-2024-26578 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-26578) [\[CVE json\]](./CVE-2024-26578.cve.json) [\[OSV json\]](./CVE-2024-26578.osv.json)



_Last updated: 2024-02-22T09:28:11.636Z_

### Affected

* Apache Answer through 1.2.1


### Description

Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition') vulnerability in Apache Answer.<p>This issue affects Apache Answer: through 1.2.1.</p>Repeated submission during registration resulted in the registration of the same user. When users register, if they rapidly submit multiple registrations using scripts, it can result in the creation of multiple user accounts simultaneously with the same name.<br><p>Users are recommended to upgrade to version [1.2.5], which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ko0ksnznt2484lxt0zts2ygr82ldkhcb


### Credits
* Mohammad Reza Omrani (reporter)


## XSS vulnerability when submitting summary ## { #CVE-2024-23349 }

CVE-2024-23349 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23349) [\[CVE json\]](./CVE-2024-23349.cve.json) [\[OSV json\]](./CVE-2024-23349.osv.json)



_Last updated: 2024-02-22T09:48:18.347Z_

### Affected

* Apache Answer through 1.2.1


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Answer.<p>This issue affects Apache Answer: through 1.2.1.</p>XSS attack when user enters summary. A logged-in user, when modifying their own submitted question, can input malicious code in the summary to create such an attack.<br><br><span style="background-color: var(--wht);">Users are recommended to upgrade to version [1.2.5], which fixes the issue.</span>

### References
* https://lists.apache.org/thread/y5902t09vfgy7892z3vzr1zq900sgyqg


### Credits
* Lyaa@JeeseenSec (reporter)


## Pixel Flood Attack by uploading the large pixel file ## { #CVE-2024-22393 }

CVE-2024-22393 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-22393) [\[CVE json\]](./CVE-2024-22393.cve.json) [\[OSV json\]](./CVE-2024-22393.osv.json)



_Last updated: 2024-02-22T09:51:41.833Z_

### Affected

* Apache Answer through 1.2.1


### Description

Unrestricted Upload of File with Dangerous Type vulnerability in Apache Answer.<p>This issue affects Apache Answer: through 1.2.1.</p>Pixel Flood Attack by uploading large pixel files will cause server out of memory. A logged-in user&nbsp;can cause such an attack by uploading an image when posting content.<br><p>Users are recommended to upgrade to version [1.2.5], which fixes the issue.</p>

### References
* https://lists.apache.org/thread/f58l6dr4r74hl6o71gn47kmn44vw12cv


### Credits
* Mohammad Reza Omrani (reporter)


## Repeated submissions using scripts resulted in an abnormal number of collections for questions. ## { #CVE-2023-49619 }

CVE-2023-49619 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49619) [\[CVE json\]](./CVE-2023-49619.cve.json) [\[OSV json\]](./CVE-2023-49619.osv.json)



_Last updated: 2024-01-10T08:24:57.576Z_

### Affected

* Apache Answer through 1.2.0


### Description

Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition') vulnerability in Apache Answer.<br><br><span style="background-color: var(--wht);">This issue affects Apache Answer: through 1.2.0.<br><br></span><span style="background-color: rgb(255, 255, 255);">Under normal circumstances, a user can only bookmark a question once, and will only increase the number of questions bookmarked once. However, repeat submissions through the script can increase the number of collection of the question many times.<br><br></span><span style="background-color: var(--wht);">Users are recommended to upgrade to version [</span><span style="background-color: var(--wht);">1.2.1</span><span style="background-color: var(--wht);">], which fixes the issue.</span>

### References
* https://lists.apache.org/thread/nscrl3c7pn68q4j73y3ottql6n5x3hd4


### Credits
* ek1ng (reporter)
