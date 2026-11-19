---
title: Reporting security issues in dependencies
description: Is the issue already public?
---

If you have identified a **new** potential security vulnerability in the dependency of an Apache Software Foundation project, we strongly encourage you to report it privately to the owners of that dependency first. If the relationship between the software is more complex, for example one project is a fork of another, then jointly reporting privately to both may be more appropriate.

If the issue is already public, for example an already published CVE from the dependency, do not contact a private security mailing list. When an advisory is published for a library in the dependency tree of an ASF project or artifact, more often than not, the project does not use the dependency in a way that is affected by the problem described in the advisory. For this reason we don't accept the simple fact that an advisory exists for a dependency as a vulnerability report in itself.

Practical steps you can take in this situation are:

* Check the projects' public communication channels, such as their website, issue tracker and development mailinglists, to see if the advisory has already been discussed there.
* Check the projects' current source version control system to see if the dependency has already been upgraded. If so, then you can expect the next release to mitigate this risk.
* Check the projects' current source version control system to see if automation has already flagged the issue, for example Dependabot opening pull requests on GitHub.

If you cannot find existing information on whether the project is affected by the issue in the advisory, it may be up to you, as a part of the project community, to participate in its handling. Ensure you provide detailed information when starting a discussion - review how the project uses the dependency and have your opinion on the priority to upgrade, or even remove, the dependency. Contributions upgrading the dependency to a version that is not affected by the problem are generally welcomed, though will not typically expedite the release schedule.

To influence release schedules, please provide a proof-of-concept report that the advisory affects the Apache Software Foundation project in question (not the dependency) through the private channels described [here](https://security.apache.org/report-code). If your analysis identifies other or related issues affecting the project, report these through the private channels.

If you have verified the issue does not impact the project, it is an appreciated contribution if you can share this analysis through the project's public channels, so others can review this work and make their own risk assessment.
