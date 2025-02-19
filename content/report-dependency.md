---
title: Reporting security issues in dependencies
description: We strongly encourage you to report potential security vulnerabilities privately, before disclosing them in a public forum.
---

When an advisory is published for a library in the dependency tree of an ASF project or artifact, more often than not, the project does not use the dependency in a way that is affected by the problem described in the advisory. For this reason we don't accept the simple fact that an advisory exists for a dependency as a security issue in itself.

If you have done any analysis to confirm the issue described in the advisory does impact this project, please share that information with us though the private channels described [here](https://security.apache.org/report-code).

If you have verified the issue does not impact the project, it would be appreciated to share this analysis through the project's public channels.

If you have not done any analysis on whether the advisory for the dependency impacts the project, you can consult the projects' public channels to find out if anyone else has done any research into this advisory. Some projects (such as [Solr](https://solr.apache.org/security.html)) have a dedicated page for such information, otherwise you could look at their issue tracker or public mailinglists. If no existing analysis on the issue can be found, you may open a public issue or discussion on the mailinglist. Contributions upgrading the dependency to a version that is not affected by the problem are also generally welcomed.
