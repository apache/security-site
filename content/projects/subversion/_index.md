---
title: Apache Subversion security advisories
description: Security information for Apache Subversion
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Subversion? You can read more about the projects' security policy on their [security page](https://subversion.apache.org/security/), and email your report to the [Apache Subversion Security Team](mailto:security@subversion.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://subversion.apache.org/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Remote unauthenticated denial-of-service in Subversion mod_authz_svn ## { #CVE-2020-17525 }

CVE-2020-17525 [\[CVE json\]](./CVE-2020-17525.cve.json)

_Last updated: 2021-03-17T09:12:33.507Z_

### Affected

* Apache Subversion at mod_authz_svn 1.10.7
* Apache Subversion from mod_authz_svn before 1.14.1


### Description

Subversion's mod_authz_svn module will crash if the server is using in-repository authz rules with the AuthzSVNReposRelativeAccessFile option and a client sends a request for a non-existing repository URL. This can lead to disruption for users of the service.  This issue was fixed in mod_dav_svn+mod_authz_svn servers 1.14.1 and mod_dav_svn+mod_authz_svn servers 1.10.7

### References
* https://subversion.apache.org/security/CVE-2020-17525-advisory.txt


### Credits
* Thomas Åkesson (simonsoft.se)


## Apache Subversion SVN authz protected copyfrom paths regression ## { #CVE-2021-28544 }

CVE-2021-28544 [\[CVE json\]](./CVE-2021-28544.cve.json)

_Last updated: 2022-04-12T17:46:18.140Z_

### Affected

* Apache Subversion at 1.10.0 to 1.14.1


### Description

Apache Subversion SVN authz protected copyfrom paths regression  Subversion servers reveal 'copyfrom' paths that should be hidden according to configured path-based authorization (authz) rules.  When a node has been copied from a protected location, users with access to the copy can see the 'copyfrom' path of the original.  This also reveals the fact that the node was copied.  Only the 'copyfrom' path is revealed; not its contents. Both httpd and svnserve servers are vulnerable.

### References
* https://subversion.apache.org/security/CVE-2021-28544-advisory.txt


### Credits
* Apache Subversion would like to thank Evgeny Kotkov, visualsvn.com.


## Apache Subversion mod_dav_svn is vulnerable to memory corruption ## { #CVE-2022-24070 }

CVE-2022-24070 [\[CVE json\]](./CVE-2022-24070.cve.json)

_Last updated: 2022-04-12T17:46:14.441Z_

### Affected

* Apache Subversion at 1.10.0 to 1.14.1


### Description

Subversion's mod_dav_svn is vulnerable to memory corruption.  While looking up path-based authorization rules, mod_dav_svn servers may attempt to use memory which has already been freed.  Affected Subversion mod_dav_svn servers 1.10.0 through 1.14.1 (inclusive). Servers that do not use mod_dav_svn are not affected.

### References
* https://issues.apache.org/jira/browse/SVN-4880
* https://bz.apache.org/bugzilla/show_bug.cgi?id=65861
* https://cwiki.apache.org/confluence/display/HTTPD/ModuleLife


### Credits
* Apache Subversion would like to thank Thomas Weißschuh, cis-solutions.eu.
