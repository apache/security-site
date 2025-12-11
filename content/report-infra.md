---
title: Reporting security issues in ASF infrastructure
description: We strongly encourage you to report potential security vulnerabilities privately, before disclosing them in a public forum.
---

ASF infrastructure includes the apache.org websites, email infrastructure and version control systems.

There are some classes of common reports that we consider invalid up-front:

* We already know our domain has a weak `p=none` DMARC policy. This is because our mailservers only use DKIM for individual emails. We plan to support this for our mailinglists as well in the future, but this is nontrivial.
* As an open source organization with transparency at our core, read access to directory listings, source code repositories and build servers is intentionally public.
* Systems that disclose the versions of the servers and software we use
* Data that is publicly accessible in our bug tracking systems

If you think you have found an infrastructure issue other than the ones listed above, contact <a href="mailto:root@apache.org">root@apache.org</a>
