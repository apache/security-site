---
title: "Apache vulnerability severity rating system"
author: Mark Cox
date: 2023-04-25
description: We introduce a default severity rating system, based on the scales we've been using with some specific projects
---

When disclosing a security vulnerability in a previous version of an Apache software project, the project typically assigns a severity level such as "low" or "critical". For most projects we've have never defined what those levels mean.  In this blogpost we introduce a default severity rating system, based on the scales we've been using with some specific projects for a long time.

From the early days of the Apache HTTP Server project we assigned an impact rating to security flaws, designed to be "How worried should I be about this vulnerability".  The rating had four levels, "Low", "Moderate", "Important", and "Critical" and was written to try to match the levels used by other vendors.  The idea being to use a scale that is well-known and understood. One of the earliest vendors using this scale for example was [Microsoft.](https://www.microsoft.com/en-us/msrc/security-update-severity-rating-system)

The [HTTP Server ratings](https://httpd.apache.org/security/impact_levels.html) have had mostly the same language around these levels for 20 years, and other Apache projects such as [Tomcat](https://tomcat.apache.org/security-impact.html) aligned to the same scale.   Other OSS projects, such as OpenSSL, and vendors, such as [Red Hat,](https://access.redhat.com/security/updates/classification) also aligned to these scales.  The Red Hat scale has reworded descriptions based on their experience of handling and rating thousands of open source vulnerabilities each year.  So we can use those descriptions as the basis for our default system.

Other scoring systems, such as CVSS (v2 and later v3) are available, but we've found that these don't work well for libraries, and they don't work particularly well for OSS projects in general.  That's worth another blog post in the future.

Apache projects are free to use these default levels or choose their own rating systems, either with specific threat models outlined in the scale, or to use a different system completely.  They can choose to just use (or additionally include) CVSS scores for example and some like the [Logging project already do](https://logging.apache.org/log4j/2.x/security.html).

So here's the default project severity levels and description for the levels:

| Severity | Description |
| --- | --- |
| Critical | This rating is given to flaws that could be easily exploited by a remote unauthenticated attacker and lead to system compromise (arbitrary code execution) without requiring user interaction. Flaws that require authentication, local or physical access to a system, or an unlikely configuration are not classified as Critical. |
| Important | This rating is given to flaws that can easily compromise the confidentiality, integrity, or availability of resources. These are the types of vulnerabilities that allow local or authenticated users to gain additional privileges, allow unauthenticated remote users to view resources that should otherwise be protected by authentication or other controls, allow authenticated remote users to execute arbitrary code, or allow remote users to cause a denial of service. |
| Moderate | This rating is given to flaws that may be more difficult to exploit but could still lead to some compromise of the confidentiality, integrity or availability of resources under certain circumstances. These are the types of vulnerabilities that could have been Critical or Important but are less easily exploited based on a technical evaluation of the flaw, affect unlikely configurations, and/or have a limited scope of impact. |
| Low | This rating is given to all other issues that may have a security impact. These are the types of vulnerabilities that are believed to require unlikely circumstances to be able to be exploited, or where a successful exploit would have minimal consequences. |
