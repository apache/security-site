---
title: STF/OSTIF commission audit of three Apache Commons projects
author: Arnout Engelen
date: 2024-07-08
description: No vulnerabilities found, a number of security hardening improvements identified and implemented.
---

The [Open Source Technology Improvement Fund (OSTIF)](https://ostif.org/),
funded by the [Sovereign Tech Fund (STF)](https://sovereigntechfund.de)'s [Bug Resilience Program](https://www.sovereigntechfund.de/programs/bug-resilience),
recently commissioned an audit of three
[Apache Commons](https://commons.apache.org/) projects:
[Apache Commons Lang](https://commons.apache.org/proper/commons-lang/),
[Apache Commons IO](https://commons.apache.org/proper/commons-io/) and 
[Apache Commons Codec](https://commons.apache.org/proper/commons-codec/).
We are proud to announce that [Ada Logics](https://adalogics.com/), who
performed the audit, did not find any vulnerabilities.

The Apache Commons libraries are low-level building blocks, often used in
internal applications on trusted input. As such, unless otherwise specified,
it is the responsibility of the application invoking the libraries to make sure
any untrusted parameters are sanitized. When that layer of defense fails,
we try to limit the possible impact of such a breach by making sure malicious or
otherwise invalid input can cause minimal disruption. During their analysis, which
included both manual auditing and code fuzzing, Ada Logics identified a number of
new opportunities for such security hardening improvements, and contributed code
to implement several of these.

We thank the [Sovereign Tech Fund](https://sovereigntechfund.de),
[OSTIF](https://ostif.org/) and [Ada Logics](https://adalogics.com/) for
their help in ensuring the security of projects that use Apache Commons.

You can find additional information about this audit at [the OSTIF blog](https://ostif.org/apachec-audit-complete/).
