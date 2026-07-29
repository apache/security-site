---
title: Reporting security issues in ASF code
description: We strongly encourage you to report potential security vulnerabilities privately, before disclosing them in a public forum.
---

We warmly welcome reports of potential security vulnerabilities in our codebases.

Only use the security contacts to report **undisclosed security vulnerabilities in ASF projects**
and manage the process of fixing such vulnerabilities.
In particular, this means that:

* Your report must concern a **security vulnerability**.
  We cannot accept regular bug reports, support requests, or other security-related queries at these addresses.
* The vulnerability must be **undisclosed**.
  A vulnerability with a CVE number is in most cases already publicly disclosed by the ASF itself.
  In particular, do not forward security scanner findings that report an ASF project as affected by a known CVE.
* The vulnerability must affect an **ASF project**.
  If it affects a dependency of an ASF project instead,
  see [Reporting security issues in dependencies](/report-dependency).

We will ignore mail sent to these addresses
that does not meet these requirements.

A **security vulnerability** is a bug that breaks reasonable expectations of the project
in a way that affects confidentiality, integrity, or availability.
Some projects have published a 'Security Model'
to clarify which guarantees can be expected.
You can find the security model pages on the [projects overview](/projects).
Note that results from source code security analysis tools are not accepted without additional analysis
showing that the problem indeed violates the project's security model,
as such tools commonly produce a significant amount of false positives.

Send your report to the project's security address
listed on the [projects overview](/projects).
If the affected project is not listed there,
or you are unsure which project is affected,
send your report to [security@apache.org](mailto:security@apache.org) instead.

Every email you send must meet the following requirements:

* Start the subject line with `[SECURITY]`.
  This matches an exclusion rule on our spam filter
  and ensures that your report is not accidentally discarded.
* Report only one vulnerability per email.
* Write your report in plain text and do not encrypt it.
* Explain why you believe the defect is a security issue.
  If the project publishes a security model
  on the [projects overview](/projects),
  describe which of its guarantees the defect breaks.
* Do not send your report as an image, movie, HTML, Markdown, or PDF attachment
  when you could as easily describe it in plain text.
  We will reject such reports and ask you to resubmit them.

By sending your report you agree
that information from it may be made public
after triage (for invalid issues) or after the release of the fix,
unless you explicitly request otherwise.

## Handling

An overview of the vulnerability handling process is:

* The reporter reports the vulnerability privately to Apache.
* The appropriate project's security team works privately with the reporter to resolve the vulnerability.
* The project creates a new release of the package the vulnerability affects to deliver its fix.
* The project publicly announces the vulnerability and describes how to apply the fix.

We will [credit](https://security.apache.org/blog/credits/) you in the public advisory.
As a rule we will use the credit information from the initial report, we may not honor later requests for credit updates or additions.

Committers should read a [more detailed description of the process](https://apache.org/security/committers.html). Reporters of security vulnerabilities may also find it useful.
