---
title: Apache Answer security advisories
description: Security information for Apache Answer
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache Answer? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Answer).

You can read more about the security policy on:

- [Apache Answer security model](https://answer.apache.org/community/security-model)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Reaction API authorization bypass for restricted content ## { #CVE-2026-90910 }

CVE-2026-90910 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90910) [\[CVE json\]](./CVE-2026-90910.cve.json) [\[OSV json\]](./CVE-2026-90910.osv.json)



_Last updated: 2026-10-19T09:35:53.657Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>Missing authentication for critical function vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p><p>The reaction API did not enforce content visibility controls, allowing unauthorized users to read reaction metadata from restricted content or add and remove their own reactions.</p><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/bhw80mvmnt9206wyqz80rcbwx1znv1p3


### Credits
* Maksim Hayder (reporter)


## User Center integration does not revoke first-login sessions after central account suspension ## { #CVE-2026-86589 }

CVE-2026-86589 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86589) [\[CVE json\]](./CVE-2026-86589.cve.json) [\[OSV json\]](./CVE-2026-86589.osv.json)



_Last updated: 2026-10-19T09:35:25.843Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>Incorrect implementation of authentication algorithm vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p><p>A flaw in the User Center login integration can cause a newly created external user session to omit its external identity, allowing subsequent requests to bypass central account suspension or deletion checks until the session<br>  expires or is revoked.</p><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/t8mbzfolzlqz4z5hcwq3v0lnwjqb2tl5


### Credits
* ascanner (reporter)


## Missing Authorization Allows Mutations of Non-Public Content ## { #CVE-2026-79633 }

CVE-2026-79633 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-79633) [\[CVE json\]](./CVE-2026-79633.cve.json) [\[OSV json\]](./CVE-2026-79633.osv.json)



_Last updated: 2026-10-19T09:35:04.330Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p> vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p><p>Missing authorization checks allowed authenticated users to perform actions on non-public content they were not permitted to access.</p><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/m301yrn0fwgr957q8qzfzt8tpjklocv9


### Credits
* Luigi Colluto (reporter)


## Stale Visit Tokens Retain Access to Private Uploads After Session Revocation ## { #CVE-2026-79624 }

CVE-2026-79624 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-79624) [\[CVE json\]](./CVE-2026-79624.cve.json) [\[OSV json\]](./CVE-2026-79624.osv.json)



_Last updated: 2026-10-19T09:34:39.031Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>Insufficient session expiration vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p><p>Insufficient session invalidation allowed revoked users to continue accessing known private uploaded files with a stale visit token.</p><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lpwc1hpnt3fkfwkh00v5j0dvpzqmnoqk


### Credits
* Maksim Hayder (reporter)


## Improper Authorization Allows Disclosure of Non-Public Question Metadata ## { #CVE-2026-79620 }

CVE-2026-79620 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-79620) [\[CVE json\]](./CVE-2026-79620.cve.json) [\[OSV json\]](./CVE-2026-79620.osv.json)



_Last updated: 2026-10-19T09:34:09.974Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>Exposure of sensitive information through data queries vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p><p>An improper authorization check in the similar-question search allowed authenticated users to view metadata of non-public questions.</p><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/p6oqj9b27o4nppc0kv00rn7yb7n2l6o8


### Credits
* n0mi1k (reporter)


## Exposure of Hidden Question Metadata Through Public Answer Profiles ## { #CVE-2026-76994 }

CVE-2026-76994 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-76994) [\[CVE json\]](./CVE-2026-76994.cve.json) [\[OSV json\]](./CVE-2026-76994.osv.json)



_Last updated: 2026-10-19T09:33:12.978Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p>Unauthenticated attackers could obtain metadata associated with hidden questions through public answer profiles.<div><br><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p></div>

### References
* https://lists.apache.org/thread/b9whow167cr0lkhqk6xzk0c2bb86srhy


### Credits
* sec-reex (reporter)


## MCP Answer Retrieval Exposes Content from Non-Public Questions ## { #CVE-2026-71563 }

CVE-2026-71563 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-71563) [\[CVE json\]](./CVE-2026-71563.cve.json) [\[OSV json\]](./CVE-2026-71563.osv.json)



_Last updated: 2026-10-19T09:32:39.465Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>Missing Authorization vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p>An authorization flaw in the MCP answer retrieval tool allows holders of a global API key to access answer content associated with hidden, deleted, or pending-review questions.<div><br><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p></div>

### References
* https://lists.apache.org/thread/msodd7g2r6xdn9wpkpdp04m9g1jb2xtl


### Credits
* Han, JunGyu (reporter)
* VK, AzeFox Foundations (reporter)


## Improper Authorization in Question Invite User Lookup ## { #CVE-2026-68482 }

CVE-2026-68482 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68482) [\[CVE json\]](./CVE-2026-68482.cve.json) [\[OSV json\]](./CVE-2026-68482.osv.json)



_Last updated: 2026-10-19T09:31:49.451Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>Missing Authorization vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p>An unauthenticated or unauthorized user can retrieve the invited-user list associated with a non-public question due to missing visibility authorization checks.<div><br><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p></div>

### References
* https://lists.apache.org/thread/m2tbvdv12hmr9sw6ft53rjnww8hqzds0


### Credits
* Yash Shendge (reporter)


## Email Code Purpose Confusion May Allow Account Takeover ## { #CVE-2026-67249 }

CVE-2026-67249 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67249) [\[CVE json\]](./CVE-2026-67249.cve.json) [\[OSV json\]](./CVE-2026-67249.osv.json)



_Last updated: 2026-10-19T09:31:19.395Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>A vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p>A verification code issued for one email-based workflow could be accepted by another sensitive workflow because the code purpose was not properly enforced.<div><br><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p></div>

### References
* https://lists.apache.org/thread/kbdgj9vzd24zb4r2d9ydqyr6f70rpg0v


### Credits
* Arpit Jain (reporter)


## Incorrect permission mapping allows users with only the unpin permission to hide/show questions ## { #CVE-2026-64945 }

CVE-2026-64945 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-64945) [\[CVE json\]](./CVE-2026-64945.cve.json) [\[OSV json\]](./CVE-2026-64945.osv.json)



_Last updated: 2026-10-19T09:30:50.536Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>A vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p>The question operation controller gates hide/show operations on the wrong permission check result (the unpin permission instead of the hide permission), so in custom role configurations that separate these permissions, a user granted only question.unpin can hide or restore questions without holding question.hide or question.show.<div><br><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p></div>

### References
* https://lists.apache.org/thread/3wdqq1vp449bty5ovs02f0894km07wmz


### Credits
* meifukun (reporter)


## Stored XSS via unsanitized HTML in imported question content ## { #CVE-2026-64944 }

CVE-2026-64944 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-64944) [\[CVE json\]](./CVE-2026-64944.cve.json) [\[OSV json\]](./CVE-2026-64944.osv.json)



_Last updated: 2026-10-19T09:26:51.147Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p>The importer stores imported question bodies as raw HTML without passing them through the normal Markdown-to-HTML sanitization path, so attacker-controlled HTML embedded in an imported data source is persisted and rendered to all viewers (including privileged users) as stored XSS.<div><br><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p></div>

### References
* https://lists.apache.org/thread/2cjdm4pdrrvj0t6cgcfyo3hot9vq72kb


### Credits
* meifukun (reporter)


## API keys logged in plaintext during authentication ## { #CVE-2026-64943 }

CVE-2026-64943 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-64943) [\[CVE json\]](./CVE-2026-64943.cve.json) [\[OSV json\]](./CVE-2026-64943.osv.json)



_Last updated: 2026-10-19T09:26:12.414Z_

### Affected

* Apache Answer through 2.0.2


### Description

<p>Insertion of Sensitive Information into Log File vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.2.</p>Full API keys are written to application logs on every authenticated request, allowing anyone with log-read access to recover and replay active bearer credentials.<div><br><p>Users are recommended to upgrade to version 2.0.3, which fixes the issue.</p></div>

### References
* https://lists.apache.org/thread/gczojx5ypncn1x1pg9z1cphb54t23zzg


### Credits
* meifukun (reporter)


## Residual Administrative API Key Access After Role or Account Revocation ## { #CVE-2026-60053 }

CVE-2026-60053 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-60053) [\[CVE json\]](./CVE-2026-60053.cve.json) [\[OSV json\]](./CVE-2026-60053.osv.json)



_Last updated: 2026-08-05T15:13:06.027Z_

### Affected

* Apache Answer through 2.0.1


### Description

<p>Insufficient Session Expiration vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.1.</p>Administrative API keys remained usable after the owning administrator was demoted or the account was marked inactive, suspended, or deleted, allowing continued access until the keys were explicitly removed.<br><p>Users are recommended to upgrade to version 2.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/2vkcj3bdvso6cywnklt2vtkc2m4o0b5c


### Credits
* yangxi (reporter)


## Unauthorized disclosure of deleted or pending answer content ## { #CVE-2026-60023 }

CVE-2026-60023 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-60023) [\[CVE json\]](./CVE-2026-60023.cve.json) [\[OSV json\]](./CVE-2026-60023.osv.json)



_Last updated: 2026-08-05T15:12:01.731Z_

### Affected

* Apache Answer through 2.0.1


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.1.</p>Deleted or pending answers could be retrieved by unauthorized users through the single-answer read path when the parent question remained visible, exposing answer content that should not have been accessible.<br><p>Users are recommended to upgrade to version 2.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/rq3ygd0j9cchkbmh99dqf8624s7r8y49


### Credits
* yangxi (reporter)


## Missing authorization in revision audit reject allows authenticated users to reject pending revisions ## { #CVE-2026-50749 }

CVE-2026-50749 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50749) [\[CVE json\]](./CVE-2026-50749.cve.json) [\[OSV json\]](./CVE-2026-50749.osv.json)



_Last updated: 2026-08-05T15:11:00.104Z_

### Affected

* Apache Answer through 2.0.1


### Description

<p>Improper Authorization vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.1.</p>Any authenticated user can reject arbitrary pending edit-revisions without review permission due to a missing authorization check on the reject operation.<br><p>Users are recommended to upgrade to version 2.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ogk461yr4w9o95k15bkjxk2kpbkrbnln


### Credits
* tonghuaroot (reporter)
* Mattia Campanelli (reporter)
* Cavan Loughran (reporter)
* Xi Yang (reporter)


## Improper authorization in avatar update cleanup allows authenticated users to delete arbitrary uploaded files by URL ## { #CVE-2026-48912 }

CVE-2026-48912 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48912) [\[CVE json\]](./CVE-2026-48912.cve.json) [\[OSV json\]](./CVE-2026-48912.osv.json)



_Last updated: 2026-08-05T15:10:03.446Z_

### Affected

* Apache Answer through 2.0.1


### Description

<p>Improper Input Validation vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.1.</p> A missing ownership check in the avatar-cleanup logic allows any authenticated user to delete other users' uploaded files by supplying their file URLs.<br><p>Users are recommended to upgrade to version 2.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/b9jnttmspd9kp4vgbvb32dcqb4201flq


### Credits
* tonghuaroot (reporter)


## Unauthenticated OAuth Email-Binding Account Takeover via Existing User Confirmation Flow ## { #CVE-2026-48911 }

CVE-2026-48911 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48911) [\[CVE json\]](./CVE-2026-48911.cve.json) [\[OSV json\]](./CVE-2026-48911.osv.json)



_Last updated: 2026-08-05T15:09:10.774Z_

### Affected

* Apache Answer through 2.0.1


### Description

<p>Insufficient Verification of Data Authenticity vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.1.</p>A missing authorization check in the external-login email binding flow allows unauthenticated attackers to take over arbitrary user accounts by tricking victims into clicking a crafted confirmation link.<br><p>Users are recommended to upgrade to version 2.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/mrlwtdnhqqgfbchjgq6rffkz67o8wyv8


### Credits
* tonghuaroot (reporter)
* yangxi (reporter)


## Denial of service via crafted Accept-Language header parsing ## { #CVE-2026-48834 }

CVE-2026-48834 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48834) [\[CVE json\]](./CVE-2026-48834.cve.json) [\[OSV json\]](./CVE-2026-48834.osv.json)



_Last updated: 2026-08-05T15:07:31.168Z_

### Affected

* Apache Answer through 2.0.1


### Description

<p>Improper Handling of Length Parameter Inconsistency vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.1.</p>Unauthenticated attackers can cause a denial of service via a specially crafted Accept-Language header that triggers excessive CPU consumption during parsing.<br><p>Users are recommended to upgrade to version 2.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/0yg5smwnbrhqs55m5h61gn42mcs8s95p


### Credits
* tonghuaroot (reporter)


## Unlisted Questions Accessible via Direct API Access ## { #CVE-2026-34905 }

CVE-2026-34905 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34905) [\[CVE json\]](./CVE-2026-34905.cve.json) [\[OSV json\]](./CVE-2026-34905.osv.json)



_Last updated: 2026-06-09T07:35:55.677Z_

### Affected

* Apache Answer through 2.0.0


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.0.</p>The unlisted question feature did not enforce access restrictions on direct API endpoints, allowing authenticated users to discover and access unlisted questions, their answers, comments, and revision history.<br><p>Users are recommended to upgrade to version 2.0.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/khxoft96sptr2kh0cpzgw7f6qwv0ltcf


### Credits
* Hamed Kohi (reporter)


## HTML Content Injection in Email ## { #CVE-2026-34033 }

CVE-2026-34033 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34033) [\[CVE json\]](./CVE-2026-34033.cve.json) [\[OSV json\]](./CVE-2026-34033.osv.json)



_Last updated: 2026-06-09T07:35:14.622Z_

### Affected

* Apache Answer through 2.0.0


### Description

<p>Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.0.</p>User-supplied content was included in notification emails without proper escaping, allowing authenticated users to inject arbitrary HTML into emails sent to other users.<br><p>Users are recommended to upgrade to version 2.0.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/wrfd9blbfotfg479jr8vlwfx6pwr9sgj


### Credits
* Reimar Fritz (reporter)


## The custom avatar was not properly validated ## { #CVE-2026-34031 }

CVE-2026-34031 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34031) [\[CVE json\]](./CVE-2026-34031.cve.json) [\[OSV json\]](./CVE-2026-34031.osv.json)



_Last updated: 2026-06-09T07:34:37.370Z_

### Affected

* Apache Answer through 2.0.0


### Description

<p>Unrestricted Upload of File with Dangerous Type vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.0.</p>The server did not sufficiently validate user-supplied image URLs, allowing arbitrary external content to be embedded as profile images, which could expose users to unintended external requests and tracking by third-party servers.<br><p>Users are recommended to upgrade to version 2.0.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/rwtxy39t54to9kv3dqtbjsbdpyk4jkd2


### Credits
* Reimar Fritz (reporter)


## Uploading specially crafted TIFF files causes an Out-of-Memory error ## { #CVE-2026-33582 }

CVE-2026-33582 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33582) [\[CVE json\]](./CVE-2026-33582.cve.json) [\[OSV json\]](./CVE-2026-33582.osv.json)



_Last updated: 2026-06-09T07:34:00.786Z_

### Affected

* Apache Answer through 2.0.0


### Description

<p>Unrestricted Upload of File with Dangerous Type vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.0.</p>A crafted TIFF image could trigger excessive memory allocation during image decoding, allowing an authenticated user to cause the server process to crash.<br><p>Users are recommended to upgrade to version 2.0.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/3sgpx4cwsgpnt66xv3cqvtc8z4st1kbq


### Credits
* Andy Gill, ZephrSec Ltd (reporter)


## AdminToken not invalidated after admin deactivation ## { #CVE-2026-25700 }

CVE-2026-25700 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-25700) [\[CVE json\]](./CVE-2026-25700.cve.json) [\[OSV json\]](./CVE-2026-25700.osv.json)



_Last updated: 2026-06-10T14:56:58.543Z_

### Affected

* Apache Answer through 2.0.0


### Description

<p>Improper Restriction of Security Token Assignment vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.0.</p>Previously issued administrative tokens were not invalidated after an administrator account was suspended, deleted, or deactivated, allowing continued access to administrative APIs until the token expired.<br><p>Users are recommended to upgrade to version 2.0.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ftw52mlxknjm29vo1mnqovj53z2kh96y


### Credits
* Sho Odagiri (reporter)


## Authorization Bypass in Timeline API ## { #CVE-2026-25699 }

CVE-2026-25699 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-25699) [\[CVE json\]](./CVE-2026-25699.cve.json) [\[OSV json\]](./CVE-2026-25699.osv.json)



_Last updated: 2026-06-09T07:33:11.641Z_

### Affected

* Apache Answer through 2.0.0


### Description

<p>Exposure of Private Personal Information to an Unauthorized Actor vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.0.</p>Timeline-related APIs lacked proper authorization checks, allowing regular authenticated users to access deleted, private, or unapproved content and its revision history.<br><p>Users are recommended to upgrade to version 2.0.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/c36k4hzwhncqo0qfn5fg57f1gkjhyfv8


### Credits
* Sho Odagiri (reporter)


## XSS in AI Answer Rendering ## { #CVE-2026-25688 }

CVE-2026-25688 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-25688) [\[CVE json\]](./CVE-2026-25688.cve.json) [\[OSV json\]](./CVE-2026-25688.osv.json)



_Last updated: 2026-06-09T07:32:22.140Z_

### Affected

* Apache Answer through 2.0.0


### Description

<p>Improper Neutralization of Alternate XSS Syntax vulnerability in Apache Answer.</p><p>This issue affects Apache Answer: through 2.0.0.</p>AI-generated response content was rendered in the browser without proper sanitization, allowing malicious scripts to be executed when the content was viewed.<br><p>Users are recommended to upgrade to version 2.0.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/x42joj43rqb38ms5q60f7bgq3qbo7t5q


### Credits
* Sho Odagiri (reporter)


## Revision API Improper Access Control leads to Information Disclosure ## { #CVE-2026-24735 }

CVE-2026-24735 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24735) [\[CVE json\]](./CVE-2026-24735.cve.json) [\[OSV json\]](./CVE-2026-24735.osv.json)



_Last updated: 2026-06-03T06:48:19.838Z_

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
