---
title: Apache DB security advisories
description: Security information for Apache DB
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache DB? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache ddlutils 1.0 readobject vulnerability ## { #CVE-2021-41616 }

CVE-2021-41616 [\[CVE json\]](./CVE-2021-41616.cve.json)

_Last updated: 2021-09-30T07:51:31.141Z_

### Affected

* Apache DB ddlutils at 1.0


### Description

Apache DB DdlUtils 1.0 included a BinaryObjectsHelper that was intended for use when migrating database data with a SQL data type of BINARY, VARBINARY, LONGVARBINARY, or BLOB between databases using the ddlutils features. The BinaryObjectsHelper  class was insecure and used ObjectInputStream.readObject without validating that the input data was safe to deserialize.

Please note that DdlUtils is no longer being actively developed. To address the insecurity of the BinaryObjectHelper class, the following changes to DdlUtils have been made: (1) BinaryObjectsHelper.java has been deleted from the DdlUtils source repository and the DdlUtils feature of propagating data of SQL binary types is therefore no longer present in DdlUtils; (2) The ddlutils-1.0 release has been removed from the Apache Release Distribution Infrastructure; (3) The DdlUtils web site has been updated to indicate that DdlUtils is now available only as source code, not as a packaged release.

### References
* https://lists.apache.org/thread.html/r3d7a8303a820144f5e2d1fd0b067e18d419421b58346b53b58d3fa72%40%3Cannounce.apache.org%3E


## LDAP injection vulnerability in authenticator ## { #CVE-2022-46337 }

CVE-2022-46337 [\[CVE json\]](./CVE-2022-46337.cve.json)

_Last updated: 2024-01-02T18:36:19.559Z_

### Affected

* Apache Derby from 10.1.1.0 through 10.16.1.1


### Description

A cleverly devised username might bypass LDAP authentication checks. In 
LDAP-authenticated Derby installations, this could let an attacker fill 
up the disk by creating junk Derby databases. In LDAP-authenticated 
Derby installations, this could also allow the attacker to execute 
malware which was visible to and executable by the account which booted 
the Derby server. In LDAP-protected databases which weren't also 
protected by SQL GRANT/REVOKE authorization, this vulnerability could 
also let an attacker view and corrupt sensitive data and run sensitive 
database functions and procedures.
<br>
<br>Mitigation:
<br>Users should upgrade to Java 21 and Derby 10.17.1.0.
<br>Alternatively, users who wish to remain on older Java versions should 
build their own Derby distribution from one of the release families to 
which the fix was backported: 10.16, 10.15, and 10.14. Those are the 
releases which correspond, respectively, with Java LTS versions 17, 11, 
and 8.
<br>
<br>

### References
* https://lists.apache.org/thread/q23kvvtoohgzwybxpwozmvvk17rp0td3


### Credits
* This issue was discovered by ﻿4ra1n and Y4tacker, who also proposed the fix. (finder)
