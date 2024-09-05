---
title: Credits for finding security vulnerabilities
author: Arnout Engelen
date: 2024-03-01
description: This post describes when and how we give credit to people who report security issues.
---

We highly appreciate everyone who responsibly [reports security issues](https://www.apache.org/security/)
to us: a diverse mix of community members, independent security researchers,
software auditing firms, etc.

When we release a fix for a vulnerability in one of our projects, we
publish a security advisory crediting the reporter, and distribute it though
various Apache [mailinglists](https://www.apache.org/foundation/mailinglists.html), [oss-security](https://www.openwall.com/lists/oss-security/) and the
[CVE](https://www.cve.org/) programme: this way, we proactively signal the
urgency to upgrade to our users.

The Apache Software Foundation, being a volunteer organization, does not have
a bug bounty program. However, some Apache projects are covered under 3rd-party
bounty programs such as the
[HackerOne Internet Bug Bounty](https://hackerone.com/ibb).

Notifications about possible security issues in the infrastructure that makes
development possible, such as websites, CI systems and other supporting
software, are also very welcome.

There are some classes of common reports that we consider invalid up-front:

* We already know our mailservers do not use DKIM/DMARC. We plan to support this in the future, but this is nontrivial given our strong reliance on mailinglists.
* As an open source organization with transparency at our core, read access to directory listings, source code repositories and build servers is intentionally public.
* If a project has a dependency for which a security advisory has been published, this is not in itself a vulnerability in the project, as more often than not the dependency is used in a way that is not affected by the issue in the advisory. Only if you have additional analysis to confirm the project is affected you're invited to report this through the private reporting mechanism.
* Similarly, results from source code security analysis tools are not accepted without additional analysis showing the problem indeed violates the projects' security model, as such tools commonly produce a significant amount of false positives.

Valid reports about our project infrastructure are typically not eligible
for a CVE, as downstream users do not need to take any action,
so they do not need to be notified.

Still, as a token of our appreciation, we'd like to thank a number of such reporters here:

* [Aviv Keller](https://linkedin.com/in/redyetidev) for helping identify a number of XSS problems in various Apache project websites, and for helping fix a large number of complex GitHub Actions permissions issues.
* [Harish](https://www.linkedin.com/in/harish-p-62b38a158) for working with us to resolve a [GitHub Actions issue](https://medium.com/apache-airflow/unraveling-the-code-navigating-a-ci-release-security-vulnerability-in-apache-airflow-620214a96297)
* [Li Jiantao](https://twitter.com/Cursered) of [STAR Labs SG Pte. Ltd.](https://twitter.com/starlabs_sg) for reporting a problem with an internal administrative tool.
* Gaurang Maheta for notifying us of a remaining reference to polyfill.io on an ASF domain.
* Ahmed Ghazy for notifying us of leaked credentials
