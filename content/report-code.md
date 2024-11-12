---
title: Reporting security issues in ASF infrastructure
description: We strongly encourage you to report potential security vulnerabilities privately, before disclosing them in a public forum.
---

We warmly welcome reports of potential security vulnerabilities in our codebases.

**Only use the security contacts to report undisclosed security vulnerabilities in Apache projects and manage the process of fixing such vulnerabilities. We cannot accept regular bug reports or other security-related queries at these addresses. We will ignore mail sent to these addresses that does not relate to an undisclosed security problem in an Apache project.**

Note that results from source code security analysis tools are not accepted without additional analysis showing the problem indeed violates the projects' security model, as such tools commonly produce a significant amount of false positives.

A security vulnerability is a bug that breaks reasonable expectations of the
project in a way that affects confidentiality, integrity or availability. Some
projects have published a 'Security Model' to clarify which guarantees can be
expected. You can find the security model pages, as well as the email address
you can use to report potential vulnerabilities, [here](/projects).

Please send one plain-text, unencrypted, email for each vulnerability you are reporting. We may ask you to resubmit your report if you send it as an image, movie, HTML, or PDF attachment when you could as easily describe it with plain text.

## Handling

An overview of the vulnerability handling process is:

* The reporter reports the vulnerability privately to Apache.
* The appropriate project's security team works privately with the reporter to resolve the vulnerability.
* The project creates a new release of the package the vulnerability affects to deliver its fix.
* The project publicly announces the vulnerability and describes how to apply the fix.

Committers should read a [more detailed description of the process](https://apache.org/security/committers.html). Reporters of security vulnerabilities may also find it useful.
