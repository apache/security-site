---
title: Apache James security advisories
description: Security information for Apache James
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache James? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache James: denial of service through JMAP HTML to text conversion ## { #CVE-2024-45626 }

CVE-2024-45626 [\[CVE json\]](./CVE-2024-45626.cve.json) [\[OSV json\]](./CVE-2024-45626.osv.json)



_Last updated: 2025-02-06T11:21:05.038Z_

### Affected

* Apache James server from 3.8.0 through 3.8.1
* Apache James server through 3.7.5


### Description

Apache James server JMAP HTML to text plain implementation in versions below 3.8.2 and 3.7.6 is subject to unbounded memory consumption that can result in a denial of service.<br><br>Users are recommended to upgrade to version 3.7.6 and 3.8.2, which fix this issue.

### References
* https://lists.apache.org/thread/1fr9hvpsylomwwfr3rv82g84sxszn4kl


### Credits
* Benoit TELLIER (finder)
* Wojciech Kapcia (finder)


## Apache James: denial of service through the use of IMAP literals ## { #CVE-2024-37358 }

CVE-2024-37358 [\[CVE json\]](./CVE-2024-37358.cve.json) [\[OSV json\]](./CVE-2024-37358.osv.json)



_Last updated: 2025-09-01T09:40:16.733Z_

### Affected

* Apache James server through 3.7.5
* Apache James server from 3.8.0 through 3.8.1


### Description

Similarly to CVE-2024-34055, Apache James is vulnerable to denial of service through the abuse of IMAP literals from both authenticated and unauthenticated users, which could be used to cause unbounded memory allocation and very long computations<br><br>Version 3.7.6 and 3.8.2 restrict such illegitimate use of IMAP literals.<br>

### References
* https://lists.apache.org/thread/1pxsh11v5s3fkvhnqvkmlqwt3fgpcrqc


### Credits
* Xavier GUIMARD (reporter)
* Benoit TELLIER (coordinator)


## Mime4J DOM header injection ## { #CVE-2024-21742 }

CVE-2024-21742 [\[CVE json\]](./CVE-2024-21742.cve.json) [\[OSV json\]](./CVE-2024-21742.osv.json)



_Last updated: 2025-05-06T13:11:31.892Z_

### Affected

* Apache James Mime4J through 0.8.9


### Description

Improper input validation allows for header injection in MIME4J library when using MIME4J DOM for composing message.<br>This can be exploited by an attacker to add unintended headers to MIME messages.<br>

### References
* https://lists.apache.org/thread/nrqzg93219wdj056pqfszsd33dc54kfy


### Credits
* Benoit TELLIER (finder)


## SMTP smuggling in Apache James ## { #CVE-2023-51747 }

CVE-2023-51747 [\[CVE json\]](./CVE-2023-51747.cve.json) [\[OSV json\]](./CVE-2023-51747.osv.json)



_Last updated: 2024-02-27T13:07:59.703Z_

### Affected

* Apache James server through 3.7.4
* Apache James server from 3.8 through 3.8.0


### Description

Apache James prior to versions 3.8.1 and 3.7.5 is vulnerable to SMTP smuggling.<br><br>A lenient behaviour in line delimiter handling might create a difference of interpretation between the sender and the receiver which can be exploited by an attacker to forge an SMTP envelop, allowing for instance to bypass SPF checks.<br><br>The patch implies enforcement of CRLF as a line delimiter as part of the DATA transaction.<br><br>We recommend James users to upgrade to non vulnerable versions.<br>

### References
* https://sec-consult.com/blog/detail/smtp-smuggling-spoofing-e-mails-worldwide/
* https://postfix.org/smtp-smuggling.html
* https://lists.apache.org/thread/rxkwbkh9vgbl9rzx1fkllyk3krhgydko


### Credits
* Benoit TELLIER (coordinator)


## Privilege escalation via JMX pre-authentication deserialisation ## { #CVE-2023-51518 }

CVE-2023-51518 [\[CVE json\]](./CVE-2023-51518.cve.json) [\[OSV json\]](./CVE-2023-51518.osv.json)



_Last updated: 2024-02-27T09:09:28.523Z_

### Affected

* Apache James server through 3.7.4
* Apache James server from 3.8 through 3.8.0


### Description

Apache James prior to version 3.7.5 and 3.8.0 exposes a JMX endpoint on localhost subject to pre-authentication deserialisation of untrusted data.<br>Given a deserialisation gadjet, this could be leveraged as part of an exploit chain that could result in privilege escalation.<br><div>Note that by default JMX endpoint is only bound locally.</div><div><br></div>We recommend users to:<br><div>&nbsp;- Upgrade to a non-vulnerable Apache James version</div><div>&nbsp;- Run Apache James isolated from other processes (docker - dedicated virtual machine)<br>&nbsp;- If possible turn off JMX<br></div>

### References
* https://lists.apache.org/thread/wbdm61ch6l0kzjn6nnfmyqlng82qz0or


### Credits
* Mal Aware (reporter)
* Arnout Engelen (analyst)


## Privilege escalation through unauthenticated JMX ## { #CVE-2023-26269 }

CVE-2023-26269 [\[CVE json\]](./CVE-2023-26269.cve.json) [\[OSV json\]](./CVE-2023-26269.osv.json)



_Last updated: 2023-04-03T07:59:07.659Z_

### Affected

* Apache James server through 3.7.3


### Description

<div>Apache James server version 3.7.3 and earlier provides a JMX management service without authentication by default. This allows privilege escalation by a 
malicious local user.</div><div>Administrators are advised to disable JMX, or set up a JMX password.</div><div>Note that version 3.7.4 onward will set up a JMX password automatically for Guice users.<br></div>

### References
* https://lists.apache.org/thread/2z44rg93pflbjhvbwy3xtz505bx41cbs


### Credits
* Matei "Mal" Badanoiu (reporter)


## Temporary File Information Disclosure ## { #CVE-2022-45935 }

CVE-2022-45935 [\[CVE json\]](./CVE-2022-45935.cve.json) [\[OSV json\]](./CVE-2022-45935.osv.json)



_Last updated: 2023-07-12T10:18:16.935Z_

### Affected

* Apache James server through 3.7.2


### Description

Usage of temporary files with insecure permissions by the Apache James server allows an attacker with local access to access private user data in transit. <br><br>Vulnerable components includes the SMTP stack and IMAP APPEND command.<br><br>This issue affects Apache James server version 3.7.2 and prior versions.

### References
* https://lists.apache.org/thread/j61fo8xc1rxtofrn8vc33whx35s9cj1d


### Credits
* Benoit Tellier (reporter)


## Temporary File Information Disclosure in MIME4J TempFileStorageProvider ## { #CVE-2022-45787 }

CVE-2022-45787 [\[CVE json\]](./CVE-2022-45787.cve.json) [\[OSV json\]](./CVE-2022-45787.osv.json)



_Last updated: 2023-01-16T10:25:33.637Z_

### Affected

* Apache James MIME4J through 0.8.8


### Description

Unproper laxist permissions on the temporary files used by MIME4J TempFileStorageProvider may lead to information disclosure to other local users. This issue affects Apache James MIME4J version 0.8.8 and prior versions.<br><br>We recommend users to upgrade to MIME4j version 0.8.9 or later.<br>

### References
* https://lists.apache.org/thread/26s8p9stl1z261c4qw15bsq03tt7t0rj


### Credits
* Jonathan Leitschuh (finder)


## STARTTLS command injection in Apache JAMES ## { #CVE-2022-28220 }

CVE-2022-28220 [\[CVE json\]](./CVE-2022-28220.cve.json) [\[OSV json\]](./CVE-2022-28220.osv.json)



_Last updated: 2022-09-20T08:36:32.785Z_

### Affected

* Apache James from Apache James through 3.6.2


### Description

Apache James prior to release 3.6.3 and 3.7.1 is vulnerable to a buffering attack relying on the use of the STARTTLS command. 

Fix of CVE-2021-38542, which solved similar problem fron Apache James 3.6.1, is subject to a parser differential and do not take into account concurrent requests.



### References
* https://james.apache.org/james/update/2022/08/26/james-3.7.1.html


### Credits
* Apache James PMC would like to thanks Benoit TELLIER for this report, and Fabian Ising for his support.


## Path traversal in Apache James 3.6.1 ## { #CVE-2022-22931 }

CVE-2022-22931 [\[CVE json\]](./CVE-2022-22931.cve.json) [\[OSV json\]](./CVE-2022-22931.osv.json)



_Last updated: 2022-02-07T18:45:09.142Z_

### Affected

* Apache James at 3.6.1


### Description

Fix of CVE-2021-40525 do not prepend delimiters upon valid directory validations.

Affected implementations include:
 - maildir mailbox store
 - Sieve file repository

This enables a user to access other users data stores (limited to user names being prefixed by the value of the username being used).

### References
* https://lists.apache.org/thread/bp8yql4wws56jlh0vxoowj7foothsmpr
* https://www.openwall.com/lists/oss-security/2022/02/07/1


### Credits
* These issues were discovered and reported by GHSL team member Jaroslav Lobačevski


## Sieve file storage vulnerable to path traversal attacks ## { #CVE-2021-40525 }

CVE-2021-40525 [\[CVE json\]](./CVE-2021-40525.cve.json) [\[OSV json\]](./CVE-2021-40525.osv.json)



_Last updated: 2022-01-04T08:49:17.932Z_

### Affected

* Apache James from Apache James through 3.6.0


### Description

Apache James ManagedSieve implementation alongside with the file storage for sieve scripts is vulnerable to path traversal, allowing reading and writing any file. This vulnerability had been patched in Apache James 3.6.1 and higher. We recommend the upgrade.

Distributed and Cassandra based products are also not impacted.

### References
* https://www.openwall.com/lists/oss-security/2022/01/04/4


### Credits
* The Apache James PMC would like to thanks Benoit TELLIER for the report.


## Apache James IMAP parsing Denial Of Service ## { #CVE-2021-40111 }

CVE-2021-40111 [\[CVE json\]](./CVE-2021-40111.cve.json) [\[OSV json\]](./CVE-2021-40111.osv.json)



_Last updated: 2022-01-04T08:48:24.795Z_

### Affected

* Apache James from Apache James through 3.6.0


### Description

In Apache James, while fuzzing with Jazzer the IMAP parsing stack, we discover that crafted APPEND and STATUS IMAP command could be used to trigger infinite loops resulting in expensive CPU computations and OutOfMemory exceptions. This can be used for a Denial Of Service attack. The IMAP user needs to be authenticated to exploit this vulnerability.  This affected Apache James prior to version 3.6.1.

This vulnerability had been patched in Apache James 3.6.1 and higher. We recommend the upgrade.

### References
* https://www.openwall.com/lists/oss-security/2022/01/04/3


### Credits
* The Apache James PMC would like to thanks Benoit TELLIER for the report.


## Apache James IMAP vulnerable to a ReDoS ## { #CVE-2021-40110 }

CVE-2021-40110 [\[CVE json\]](./CVE-2021-40110.cve.json) [\[OSV json\]](./CVE-2021-40110.osv.json)



_Last updated: 2022-01-04T08:47:33.579Z_

### Affected

* Apache James from Apache James through 3.6.0


### Description

In Apache James, using Jazzer fuzzer, we identified that an IMAP user can craft IMAP LIST commands to orchestrate a Denial Of Service using a vulnerable Regular expression.  This affected Apache James prior to 3.6.1

We recommend upgrading to Apache James 3.6.1 or higher , which enforce the use of RE2J regular expression engine to execute regex in linear time without back-tracking.

### References
* https://www.openwall.com/lists/oss-security/2022/01/04/2


### Credits
* Apache James PMC would like to thanks Benoit TELLIER for this report.


## Apache James vulnerable to STARTTLS command injection (IMAP and POP3) ## { #CVE-2021-38542 }

CVE-2021-38542 [\[CVE json\]](./CVE-2021-38542.cve.json) [\[OSV json\]](./CVE-2021-38542.osv.json)



_Last updated: 2022-01-04T08:46:18.750Z_

### Affected

* Apache James from Apache James before 3.6.1


### Description

Apache James prior to release 3.6.1 is vulnerable to a buffering attack relying on the use of the STARTTLS command. This can result in Man-in -the-middle command injection attacks, leading potentially to leakage of sensible information.


### References
* https://www.openwall.com/lists/oss-security/2022/01/04/1


### Credits
* We thanks Benoit Tellier, Raphael Ouazana for reporting this vulnerability as well as Damian Poddebniak, Fabian Ising, Hanno Böck, and Sebastian Schinzel Münster University of Applied Science for their research and tools regarding STARTTLS security.
