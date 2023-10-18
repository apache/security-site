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

## Apache James vulnerable to STARTTLS command injection (IMAP and POP3) ## { #CVE-2021-38542 }

CVE-2021-38542 [\[CVE json\]](./CVE-2021-38542.cve.json)

### Affected

* Apache James from Apache James before 3.6.1


### Description

Apache James prior to release 3.6.1 is vulnerable to a buffering attack relying on the use of the STARTTLS command. This can result in Man-in -the-middle command injection attacks, leading potentially to leakage of sensible information.


### References
* https://www.openwall.com/lists/oss-security/2022/01/04/1


### Credits
* We thanks Benoit Tellier, Raphael Ouazana for reporting this vulnerability as well as Damian Poddebniak, Fabian Ising, Hanno Böck, and Sebastian Schinzel Münster University of Applied Science for their research and tools regarding STARTTLS security.


## Apache James IMAP vulnerable to a ReDoS ## { #CVE-2021-40110 }

CVE-2021-40110 [\[CVE json\]](./CVE-2021-40110.cve.json)

### Affected

* Apache James from Apache James through 3.6.0


### Description

In Apache James, using Jazzer fuzzer, we identified that an IMAP user can craft IMAP LIST commands to orchestrate a Denial Of Service using a vulnerable Regular expression.  This affected Apache James prior to 3.6.1

We recommend upgrading to Apache James 3.6.1 or higher , which enforce the use of RE2J regular expression engine to execute regex in linear time without back-tracking.

### References
* https://www.openwall.com/lists/oss-security/2022/01/04/2


### Credits
* Apache James PMC would like to thanks Benoit TELLIER for this report.


## Apache James IMAP parsing Denial Of Service ## { #CVE-2021-40111 }

CVE-2021-40111 [\[CVE json\]](./CVE-2021-40111.cve.json)

### Affected

* Apache James from Apache James through 3.6.0


### Description

In Apache James, while fuzzing with Jazzer the IMAP parsing stack, we discover that crafted APPEND and STATUS IMAP command could be used to trigger infinite loops resulting in expensive CPU computations and OutOfMemory exceptions. This can be used for a Denial Of Service attack. The IMAP user needs to be authenticated to exploit this vulnerability.  This affected Apache James prior to version 3.6.1.

This vulnerability had been patched in Apache James 3.6.1 and higher. We recommend the upgrade.

### References
* https://www.openwall.com/lists/oss-security/2022/01/04/3


### Credits
* The Apache James PMC would like to thanks Benoit TELLIER for the report.


## Sieve file storage vulnerable to path traversal attacks ## { #CVE-2021-40525 }

CVE-2021-40525 [\[CVE json\]](./CVE-2021-40525.cve.json)

### Affected

* Apache James from Apache James through 3.6.0


### Description

Apache James ManagedSieve implementation alongside with the file storage for sieve scripts is vulnerable to path traversal, allowing reading and writing any file. This vulnerability had been patched in Apache James 3.6.1 and higher. We recommend the upgrade.

Distributed and Cassandra based products are also not impacted.

### References
* https://www.openwall.com/lists/oss-security/2022/01/04/4


### Credits
* The Apache James PMC would like to thanks Benoit TELLIER for the report.


## Path traversal in Apache James 3.6.1 ## { #CVE-2022-22931 }

CVE-2022-22931 [\[CVE json\]](./CVE-2022-22931.cve.json)

### Affected

* Apache James at Apache James 3.6.1


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


## STARTTLS command injection in Apache JAMES ## { #CVE-2022-28220 }

CVE-2022-28220 [\[CVE json\]](./CVE-2022-28220.cve.json)

### Affected

* Apache James from Apache James through 3.6.2


### Description

Apache James prior to release 3.6.3 and 3.7.1 is vulnerable to a buffering attack relying on the use of the STARTTLS command. 

Fix of CVE-2021-38542, which solved similar problem fron Apache James 3.6.1, is subject to a parser differential and do not take into account concurrent requests.



### References
* https://james.apache.org/james/update/2022/08/26/james-3.7.1.html


### Credits
* Apache James PMC would like to thanks Benoit TELLIER for this report, and Fabian Ising for his support.


## Temporary File Information Disclosure ## { #CVE-2022-45935 }

CVE-2022-45935 [\[CVE json\]](./CVE-2022-45935.cve.json)

### Affected

* Apache James server through 3.7.2


### Description

Usage of temporary files with insecure permissions by the Apache James server allows an attacker with local access to access private user data in transit. <br><br>Vulnerable components includes the SMTP stack and IMAP APPEND command.<br><br>This issue affects Apache James server version 3.7.2 and prior versions.

### References
* https://lists.apache.org/thread/j61fo8xc1rxtofrn8vc33whx35s9cj1d


### Credits
* Benoit Tellier (reporter)


## Temporary File Information Disclosure in MIME4J TempFileStorageProvider ## { #CVE-2022-45787 }

CVE-2022-45787 [\[CVE json\]](./CVE-2022-45787.cve.json)

### Affected

* Apache James MIME4J through 0.8.8


### Description

Unproper laxist permissions on the temporary files used by MIME4J TempFileStorageProvider may lead to information disclosure to other local users. This issue affects Apache James MIME4J version 0.8.8 and prior versions.<br><br>We recommend users to upgrade to MIME4j version 0.8.9 or later.<br>

### References
* https://lists.apache.org/thread/26s8p9stl1z261c4qw15bsq03tt7t0rj


### Credits
* Jonathan Leitschuh (finder)


## Privilege escalation through unauthenticated JMX ## { #CVE-2023-26269 }

CVE-2023-26269 [\[CVE json\]](./CVE-2023-26269.cve.json)

### Affected

* Apache James server through 3.7.3


### Description

<div>Apache James server version 3.7.3 and earlier provides a JMX management service without authentication by default. This allows privilege escalation by a 
malicious local user.</div><div>Administrators are advised to disable JMX, or set up a JMX password.</div><div>Note that version 3.7.4 onward will set up a JMX password automatically for Guice users.<br></div>

### References
* https://lists.apache.org/thread/2z44rg93pflbjhvbwy3xtz505bx41cbs


### Credits
* Matei "Mal" Badanoiu (reporter)
