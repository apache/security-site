---
title: "ASF Security Report: 2022"
author: Mark Cox, VP Security
date: 2023-01-31
description: This report explores the state of security across all of The Apache Software Foundation (ASF) projects for the calendar year 2022. We review key metrics, specific vulnerabilities, and the most common ways users of ASF projects were affected by security issues.
---

## Background

The security committee of The Apache Software Foundation (ASF) oversees and coordinates the handling of vulnerabilities across all of the 350+ Apache projects handling over 60 incoming emails a day. Established in 2002, we have a [consistent process](https://s.apache.org/cveprocess) for how issues are handled, and this process includes how our projects must disclose security issues. During 2022, the ASF hired an administrator to help deal with incoming vulnerability handling work, with the rest of the team being volunteers.

Anyone finding security issues in any ASF project can report them to [security@apache.org](mailto:security@apache.org), where they are recorded and passed on to the relevant [dedicated security teams](https://apache.org/security/projects.html) or private project management committees (PMC) to handle. In general; each community, or PMC, is responsible for handling their own vulnerabilities. The security committee monitors all the issues reported across all the projects and keeps track of the issues throughout the vulnerability lifecycle. It also helps the various communities with their security response and process. And finally, the security committee reports on this to the ASF Board as part of the ASF oversight and governance function.

The security committee is responsible for ensuring that issues are dealt with properly and actively reminds projects of their outstanding issues and responsibilities. As a Board committee, we have the ability to take action including blocking a project's future releases or, worst case, archiving a project if such projects are unresponsive to handling their security issues. This, along with the Apache License v2,0, are key parts of the ASF’s general oversight function around official releases, allowing the ASF to protect individual developers and giving users confidence to deploy and rely on ASF software.

The oversight into all security reports, along with tools we have developed, gives us the ability to easily create metrics on the issues. Our last report [covered the metrics for 2021](https://news.apache.org/foundation/entry/apache-software-foundation-security-report2).

## Statistics for 2022

In 2022 our security email addresses received in total just over 22,600 emails (2021: 18,500). After spam filtering and thread grouping there were 1402 non-spam threads (2021: 1272, 2020: 946, 2019: 620). Unfortunately security reports do sometimes look like spam, especially if they include lots of attachments or large videos, and so we are careful to review all messages to ensure real reports are not missed.

![Diagram 1: Breakdown of ASF security email threads for calendar year 2022 (after removal of 'spam' messages)](ac48e16c-8639-4671-b028-0aecdd723cf4.png "Diagram 1: Breakdown of ASF security email threads for calendar year 2022 (after removal of 'spam' messages)")

Diagram 1 gives the breakdown of those 1402 threads. 305 threads (22%) were people confused by the Apache License. As many projects use the Apache License, not just ASF projects, people can get confused when they see the Apache License and they don't understand what it is. This is most common, for example, on mobile phones where the licenses are displayed in the settings menu, usually due to the inclusion of software by Google released under the Apache License. We do not reply to these emails. This is a similar volume to the 359 we received in 2021.

The next 415 of the 1402 (30%) were email threads with people asking non-security (usually support-type) questions. We send a templated reply to these emails.

The next 83 (6%) of those reports were researchers reporting infrastructure issues such as those affecting our web sites. These are almost always rejected; where a researcher reports us having directory listings enabled, source code visible, public “.git” directories, and so on. These reports are generally the unfiltered output of some publicly available scanning tool, and often come along with a request for some sort of monetary reward (bounty).

That left 599 (42%) reports of new vulnerabilities in 2022 (up from 2021: 441, 2020: 376, 2019:320), which spanned 122 of the top-level projects. These 599 reports include both external reports, as well as issues found internally by projects and their communities. We don’t keep track of the breakdown between those categories. For example, where a project has found an issue themselves they will follow the same ASF process to assign it a CVE (Common Vulnerabilities and Exposures) name and address it, and we still count it here. 

The next step is having the project triage the report to see if it's really an issue. Invalid reports and reports of things that are not actually vulnerabilities get rejected back to the reporter. Of the remaining issues that are accepted, they are assigned appropriate CVE names and eventually fixes are released.

As of January 1st 2023, 109 of those 599 reports were still under triage and investigation. This is where a project was working on an issue and had not yet rejected the issue or assigned it a CVE at that date. This number seems quite high but it does vary through the year and tends to be higher at the end of the calendar year, when many developers take holidays. It’s not uncommon for lower severity issues to take some time before they become part of a new release, so at any given time there will always be a number of issues open and currently being worked on.

The remaining 490 reports (up from 2021: 391, 2020: 341, 2019: 301) led to us assigning 210 CVE names (up from 2021: 183, 2020: 151, 2019: 122). Some vulnerability reports may include multiple issues, some reports are across multiple projects, and some reports are duplicates where the same issue is found by different reporters, so there isn't an exact one-to-one mapping of accepted reports to CVE names. 

The four projects with the most reports in 2022 were Airflow with 49 reports (and 19 CVE released in 2022), Commons with 37 reports (4 CVE), HTTP Server with 36 reports (13 CVE), and Tomcat with 26 reports (6 CVE). Airflow and HTTP Server are part of the [HackerOne Internet Bug Bounty program](https://hackerone.com/ibb).

The Apache Security committee handles CVE name allocation and is a MITRE Candidate Naming Authority (CNA), so all requests for CVE names in any ASF project are routed through us, even if the reporter is unaware and contacts MITRE directly or goes public with an issue before contacting us.

## Noteworthy vulnerabilities and events

During 2022 there were a few vulnerabilities worth highlighting; either because they were severe and high risk, they had readily available exploits, or there was media attention. These included:

*   January: A flaw in Apache ShenYu could allow access without authentication ([CVE-2022-23944](https://www.cve.org/CVERecord?id=CVE-2022-23944))
*   February: A flaw in Apache APISIX allowing the bypass of IP restrictions ([CVE-2022-24112](https://www.cve.org/CVERecord?id=CVE-2022-24112)), which could affect instances still using a default API key. Various public exploits are available for this issue.
*   April: The Cybersecurity and Infrastructure Security Agency (CISA) included Log4Shell on their list of [Top 15 Routinely Exploited Vulnerabilities](https://www.cisa.gov/uscert/ncas/current-activity/2022/04/27/2021-top-routinely-exploited-vulnerabilities).
*   April: A flaw in Apache APISIX can allow an attacker to gain access via a leaked secret ([CVE-2022-29266](https://www.cve.org/CVERecord?id=CVE-2022-29266))
*   April: A flaw in Apache CouchDB ([CVE-2022-24706](https://www.cve.org/CVERecord?id=CVE-2022-24706)) could allow a remote user to gain admin privileges without authenticating if CouchDB was not properly secured when installed. A number of public exploits including a MetaSploit exploit exist for this issue.
*   April: A flaw affecting configuration/script file used by a GitHub workflow was reported in Apache Camel in April, fixed the next day, and then mentioned in the press some months later: [Merge requests and insecure GitHub workflows may lead to supply-chain attacks](https://www.theregister.com/2022/09/01/google_firebase_apache_camel_github/). There was no CVE issued as there was no security vulnerability in Camel itself and no action for end users. 
*   July: A flaw in the Apache Spark UI ([CVE-2022-33891](https://www.cve.org/CVERecord?id=CVE-2022-33891)) could allow a malicious authorised user to execute arbitrary code where ACLs are enabled. Public exploits including a MetaSploit exploit exist for this issue.
*   September: A flaw in Apache Pulsar ([CVE-2022-33682](https://www.cve.org/CVERecord?id=CVE-2022-33682)), where TLS hostname verification could not be enabled. 
*   October: Apache Commons Text was updated to remove variable interpolation by default ([CVE 2022-42889](https://www.cve.org/CVERecord?id=CVE-2022-42889)).This was branded by others as “Text4Shell” however this issue is different from Log4Shell (CVE-2021-44228) because in Log4Shell, string interpolation was possible from the log message body, which commonly contains untrusted input. In the Apache Common Text issue, the relevant method was explicitly intended and clearly documented to perform string interpolation, so it is much less likely that applications would inadvertently pass in untrusted input without proper validation.
*   December: [Microsoft reported that the Zerobt bot network](https://www.microsoft.com/en-us/security/blog/2022/12/21/microsoft-research-uncovers-new-zerobot-capabilities/) had been updated to attempt to exploit CVE-2021-43013 (Apache HTTP Server) and CVE-2022-33891 (Apache Spark).

## Conclusion

The ASF projects are highly diverse and independent. They have different languages, communities, management, and security models. However one of the things every project has in common is a consistent process for how reported security issues are handled. 

The ASF Security Committee works closely with the project teams, communities, and reporters to ensure that issues get handled quickly and correctly. In 2022 we hired an administrator to work with the volunteer resources on issue handling. This responsible oversight is a principle of The Apache Way and helps ensure Apache software is stable and can be trusted.

This report gave metrics for calendar year 2022 showing from the 22,600 emails received we triaged over 599 vulnerability reports relating to ASF projects, leading to fixing 210 (CVE) issues. The number of non-spam threads dealt with was up 23% from 2021 with the number of actual vulnerability reports up 36% and assigned CVE up 15%. We also highlighted the work we did in helping organisations understand the Log4Shell issue and the role of foundations such as the ASF, and highlighted a number of new security initiatives we worked on.

If you have vulnerability information you would like to share [please contact us](https://apache.org/security/#reporting-a-vulnerability) or for comments on this report use the public [security-discuss mailing list](https://lists.apache.org/list.html?security-discuss@community.apache.org).
