---
title: ASF Security Resources
description: Resources available to ASF projects
---

If you're an Apache Software Foundation project, there are
a number of resources available to you:

## Information

You can find information around security topics with an ASF-specific
slant at https://cwiki.apache.org/confluence/display/SECURITY

For a more interactive experience, [join the conversation](/contributing/#join-the-conversation)

## Security report triage

The Security Team provides initial triage for reports coming in through
[mailto:security@apache.org](security@apache.org), so as project you won't even
have to see the most obvious invalid ones. Of course, we cannot be experts on
all ASF projects and will err on the safe side. You can make our triage more
effective by clearly [documenting your security model](https://cwiki.apache.org/confluence/display/SECURITY/Documenting+your+security+model),
which we will use as a basis for the triage.

## Project-specific security lists

If you're a mature project, you can apply for a direct project-specific
`security@project.apache.org` list and take more responsibility for the
vulnerability handling process for your project. This will remove the
initial triage by the Security Team from your process, and put you in the
driver's seat. The Security Team will still monitor your list as a line
of defense against things falling through the cracks, but it is now
primarily your responsibility.

## Tracking of in-flight security reports

The Security Team keeps track of your in-flight security reports. If you
would like an overview of your projects' open issues, feel free to request
one through [mailto:security@apache.org](security@apache.org). We may make
this available more easily in the future, but generally it is more effective
to focus more on making sure fewer reports are in-flight (e.g. fast triage,
prioritizing fixes, making frequent releases) than on improving the capacity
for tracking more of them.

## Bug Bounty Programs

The ASF [does not run a bug bounty program](/blog/credits), and a number of
the Bug Bounty programs have stopped around beginning of April 2026 as they
need redefinition of their models with AI generated security reports. The
industry works on ways to supplant the bug bounty programs.

## Security Audit

The ASF does not routinely perform security audits of ASF projects, but
there are several 3rd-party initiatives that may be interested in this.
If you would like to see a security audit done for your project, make sure
your security model is well-documented, you're ready to process any findings,
and contact [mailto:security@apache.org](security@apache.org) so we can see
if we can find someone to perform such an audit.

## Fuzzing

Especially if your project is written in a language that does not provide
memory-safety and it has clearly-defined interfaces that are designed to
process untrusted input, it can be helpful to 'fuzz' these interfaces. The
Google OSS-FUZZ project can provide resources to help build and run these
fuzzers.
