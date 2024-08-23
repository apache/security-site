---
title: Apache Answer (Incubating) security advisories
description: Security information for Apache Answer (Incubating)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Answer (Incubating)? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Repeated submissions using scripts resulted in an abnormal number of collections for questions. ## { #CVE-2023-49619 }

CVE-2023-49619 [\[CVE json\]](./CVE-2023-49619.cve.json) [\[OSV json\]](./CVE-2023-49619.osv.json)



_Last updated: 2024-01-10T08:24:57.576Z_

### Affected

* Apache Answer through 1.2.0


### Description

Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition') vulnerability in Apache Answer.<br><br><span style="background-color: var(--wht);">This issue affects Apache Answer: through 1.2.0.<br><br></span><span style="background-color: rgb(255, 255, 255);">Under normal circumstances, a user can only bookmark a question once, and will only increase the number of questions bookmarked once. However, repeat submissions through the script can increase the number of collection of the question many times.<br><br></span><span style="background-color: var(--wht);">Users are recommended to upgrade to version [</span><span style="background-color: var(--wht);">1.2.1</span><span style="background-color: var(--wht);">], which fixes the issue.</span>

### References
* https://lists.apache.org/thread/nscrl3c7pn68q4j73y3ottql6n5x3hd4


### Credits
* ek1ng (reporter)


## Pixel Flood Attack by uploading the large pixel file ## { #CVE-2024-22393 }

CVE-2024-22393 [\[CVE json\]](./CVE-2024-22393.cve.json) [\[OSV json\]](./CVE-2024-22393.osv.json)



_Last updated: 2024-02-22T09:51:41.833Z_

### Affected

* Apache Answer through 1.2.1


### Description

Unrestricted Upload of File with Dangerous Type vulnerability in Apache Answer.<p>This issue affects Apache Answer: through 1.2.1.</p>Pixel Flood Attack by uploading large pixel files will cause server out of memory. A logged-in user&nbsp;can cause such an attack by uploading an image when posting content.<br><p>Users are recommended to upgrade to version [1.2.5], which fixes the issue.</p>

### References
* https://lists.apache.org/thread/f58l6dr4r74hl6o71gn47kmn44vw12cv


### Credits
* Mohammad Reza Omrani (reporter)


## XSS vulnerability when submitting summary ## { #CVE-2024-23349 }

CVE-2024-23349 [\[CVE json\]](./CVE-2024-23349.cve.json) [\[OSV json\]](./CVE-2024-23349.osv.json)



_Last updated: 2024-02-22T09:48:18.347Z_

### Affected

* Apache Answer through 1.2.1


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Answer.<p>This issue affects Apache Answer: through 1.2.1.</p>XSS attack when user enters summary. A logged-in user, when modifying their own submitted question, can input malicious code in the summary to create such an attack.<br><br><span style="background-color: var(--wht);">Users are recommended to upgrade to version [1.2.5], which fixes the issue.</span>

### References
* https://lists.apache.org/thread/y5902t09vfgy7892z3vzr1zq900sgyqg


### Credits
* Lyaa@JeeseenSec (reporter)


## Repeated submission at registration created duplicate users with the same name ## { #CVE-2024-26578 }

CVE-2024-26578 [\[CVE json\]](./CVE-2024-26578.cve.json) [\[OSV json\]](./CVE-2024-26578.osv.json)



_Last updated: 2024-02-22T09:28:11.636Z_

### Affected

* Apache Answer through 1.2.1


### Description

Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition') vulnerability in Apache Answer.<p>This issue affects Apache Answer: through 1.2.1.</p>Repeated submission during registration resulted in the registration of the same user. When users register, if they rapidly submit multiple registrations using scripts, it can result in the creation of multiple user accounts simultaneously with the same name.<br><p>Users are recommended to upgrade to version [1.2.5], which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ko0ksnznt2484lxt0zts2ygr82ldkhcb


### Credits
* Mohammad Reza Omrani (reporter)


## XSS vulnerability when changing personal website ## { #CVE-2024-29217 }

CVE-2024-29217 [\[CVE json\]](./CVE-2024-29217.cve.json) [\[OSV json\]](./CVE-2024-29217.osv.json)



_Last updated: 2024-04-21T16:04:07.662Z_

### Affected

* Apache Answer before 1.3.0


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Answer.<p>This issue affects Apache Answer: before 1.3.0.</p>XSS attack when user changes personal website. A logged-in user, when modifying their personal website, can input malicious code in the website to create such an attack.<br><p>Users are recommended to upgrade to version [1.3.0], which fixes the issue.</p><p></p>

### References
* https://lists.apache.org/thread/nc0g1borr0d3wx25jm39pn7nyf268n0x


### Credits
* Tsubasa Umeuchi (reporter)


## The link for resetting user password is not Single-Use ## { #CVE-2024-41888 }

CVE-2024-41888 [\[CVE json\]](./CVE-2024-41888.cve.json) [\[OSV json\]](./CVE-2024-41888.osv.json)



_Last updated: 2024-08-09T14:55:12.877Z_

### Affected

* Apache Answer through 1.3.5


### Description

<p>Missing Release of Resource after Effective Lifetime vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 1.3.5.</p>The password reset link remains valid within its expiration period even after it has been used. This could potentially lead to the link being misused or hijacked.<br><p>Users are recommended to upgrade to version 1.3.6, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/jbs1j2o9rqm5sc19jyk3jcfvkmfkmyf4


### Credits
* Mohammad Reza Omrani (reporter)


## The link to reset the user's password will remain valid after sending a new link ## { #CVE-2024-41890 }

CVE-2024-41890 [\[CVE json\]](./CVE-2024-41890.cve.json) [\[OSV json\]](./CVE-2024-41890.osv.json)



_Last updated: 2024-08-09T14:53:26.714Z_

### Affected

* Apache Answer through 1.3.5


### Description

<p>Missing Release of Resource after Effective Lifetime vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 1.3.5.</p>User sends multiple password reset emails, each containing a valid link. Within the link's validity period, this could potentially lead to the link being misused or hijacked.<br><p>Users are recommended to upgrade to version 1.3.6, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/j7c080xj31x8rvz1pyk2h47rdd9pwbv9


### Credits
* Mohammad Reza Omrani (reporter)
