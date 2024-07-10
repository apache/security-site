---
title: Data Processing, Compliance Statements and SLA
author: Arnout Engelen
date: 2024-07-10
---

The Apache Software Foundation is a non commercial, open source organization that relies on a large community of volunteers and companies to maintain its software. It provides this software free (and gratis) 'as is' - as per [its license](https://www.apache.org/licenses/LICENSE-2.0).

As such we are not a 'vendor' or a 'supplier'. So while you agree to our aforementioned [license](https://www.apache.org/licenses/LICENSE-2.0) agremement, the Apache Software Foundation does not commit to things that a vendor or supplier would usually commit to. Such as providing a typical commercial helpdesk, commercial support, a 24x7 service level agreement and so on. 

For readers not yet familiar, it might be interesting to read more about [how the ASF works](https://apache.org/foundation/how-it-works.html).

# Data processing

While The Apache Software Foundation provides software that can process user data, we do not process your user data for you. We only provide the software under an  [open source license](https://www.apache.org/licenses/LICENSE-2.0). We do not run it. And thus are not involved in any processing of Personally Identifiable Data (PII) that it may do.

This means we are not a Data Processor in the sense of the GDPR or its international equivalents: whoever is running the software is the data processor.
Therefore there is no reason to sign any kind of Data Processing Agreement (DPA) with us.

If someone else is running Apache software on your behalf, such as Amazon WebServices, you might need a DPA with them. For example when that party processes data for you.

# Compliance statements

We do not directly provide any compliance statements (such as CC, STIG, CJIS, USGBC, 508, Army NW, etc).

Nonetheless, many organizations that use Apache software projects have successfully passed various audits and received the corresponding certification.

This is in part due to the fact that as a responsible Open Source Steward, we have a solid [governance structure](https://apache.org/foundation/governance/) in place, with [Program Management Committees](https://apache.org/foundation/governance/pmcs.html) overseeing the projects, and [the board](https://apache.org/foundation/governance/board.html) setting overall policy for the foundation.

In particular, any software that is released will adhere to the [release policy](https://www.apache.org/legal/release-policy.html) and follows [best practices](https://infra.apache.org/release-publishing.html), and security issues are handled according to our [security process](https://apache.org/security/committers.html).

You may either complete various certifications in house, by using a third party or by procuring the software from a commercial entity that provides such services. We cannot make any particular recommendations, but if that is relevant to you that might be something to seek out.

# Service Level Agreement

While we strive to keep our software secure and up to date - the [license](https://www.apache.org/licenses/LICENSE-2.0), under which our software was provided to you, does *not* come with a Service Level Agreement. 

There are no strict pre-agreed timelines for Apache releases or security patches:
when handling security issues projects take a risk-based approach, where issues
that are likely to have serious downstream consequences are dealt with quickly,
while issues with less impact may be fixed in the regular release cadence. The
[Apache Security Team](https://apache.org/security) monitors this process, and
projects that fail to meet reasonable response times will be retired following
our [Attic process](https://attic.apache.org).

# Attic

The Attic contains historic code that is no longer fit for purpose. It is code that can no longer be used as it was originally intended. A project that was moved to the [Attic](https://attic.apache.org) is not subject to our various security- and release-policies. It is no longer considered a release by the Apache Software Foundation. 
