---
title: Reporting security issues in dependencies
description: We strongly encourage you to report potential security vulnerabilities privately, before disclosing them in a public forum.
---

When an advisory is published for a library in the dependency tree of an ASF project or artifact, more often than not, the project does not use the dependency in a way that is affected by the problem described in the advisory. For this reason we don't accept the simple fact that an advisory exists for a dependency as a vulnerability report in itself.

Practical steps you can take in this situation are:

* Check the projects' public communication channels, such as their website, issue tracker and development mailinglists, to see if the advisory has already been discussed there.
* Check the projects' current source version control system to see if the dependency has already been upgraded. If so, then you can expect the next release to mitigate this risk.

If your organization has a mature software engineering culture, and you cannot find existing information on whether the project is affected by the issue in the advisory, it may be up to you to participate in its handling.

Contributions upgrading the dependency to a version that is not affected by the problem are generally welcomed, though will not typically expedite the release schedule.

If your analysis confirms the issue described in the advisory does impact this project, please share that information with us with the appropriate level of detail though the private channels described [here](https://security.apache.org/report-code).

If you have verified the issue does not impact the project, it would be appreciated to share this analysis through the project's public channels, so others can review this work and make their own risk assessment.
