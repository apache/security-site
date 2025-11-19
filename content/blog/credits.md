---
title: Credits for finding security vulnerabilities
author: Arnout Engelen
date: 2024-03-01
description: This post describes when and how we give credit to people who report security issues.
---

We highly appreciate everyone who responsibly [reports security issues](/report/)
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

Valid reports about our project infrastructure are typically not eligible
for a CVE, as downstream users do not need to take any action,
so they do not need to be notified.

Still, as a token of our appreciation, we'd like to thank a number of such reporters here:

* [dodo doda](https://hackerone.com/owen0x) for notifying us of a leaked Nx Cloud read-write token.
* [Priya Dharshan (JPD)](https://www.linkedin.com/in/priya-dharshan-474246225/) for notifying us of a problematic reference to an unclaimed NPM package namespace allowing resource squatting.
* [Aviv Keller](https://linkedin.com/in/redyetidev) for helping identify a number of XSS problems in various Apache project websites, and for helping fix a large number of complex GitHub Actions permissions issues.
* [Max CM](https://nopcorn.run) and [Andrew Buchanan](https://www.linkedin.com/in/abuchanan560) for identifying GHA issues where Git credentials could leak into public artifacts.
* [Harish](https://www.linkedin.com/in/harish-p-62b38a158) for working with us to resolve a [GitHub Actions issue](https://medium.com/apache-airflow/unraveling-the-code-navigating-a-ci-release-security-vulnerability-in-apache-airflow-620214a96297)
* [Li Jiantao](https://twitter.com/Cursered) of [STAR Labs SG Pte. Ltd.](https://twitter.com/starlabs_sg) for reporting a problem with an internal administrative tool.
* Gaurang Maheta for notifying us of a remaining reference to polyfill.io on an ASF domain.
* [Ahmed Ghazy](https://www.linkedin.com/in/ahmedd-ghazy) for notifying us of leaked credentials
* [Maulik Mehta](https://www.linkedin.com/in/maulik-mehta-root) for notifying us of incorrectly exposed secrets
* [Dror Peleg](https://x.com/pelsecurity) for reporting an XSS in one of our project websites
