---
title: Apache StreamPipes security advisories
description: Security information for Apache StreamPipes
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache StreamPipes? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Leverage of User ID for Privilege Escalation ## { #CVE-2025-47411 }

CVE-2025-47411 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-47411) [\[CVE json\]](./CVE-2025-47411.cve.json) [\[OSV json\]](./CVE-2025-47411.osv.json)



_Last updated: 2026-01-01T16:41:48.353Z_

### Affected

* Apache StreamPipes from 0.69.0 through 0.97.0


### Description

<div>A user with a legitimate non-administrator account can exploit a vulnerability in the user ID creation mechanism in Apache StreamPipes that allows them to swap the username of an existing user with that of an administrator.&nbsp;</div><div>This vulnerability allows an attacker to gain administrative control over the application by manipulating JWT tokens, which can lead to data tampering, unauthorized access and other security issues.</div><div></div><div><br></div><div><p>This issue affects Apache StreamPipes: through 0.97.0.</p><p>Users are recommended to upgrade to version 0.98.0, which fixes the issue.</p></div>

### References
* https://lists.apache.org/thread/lngko4ht2ok3o0rk9h0clgm4kb0lmt36


### Credits
* darren.xuan@mantelgroup.com.au (finder)


## Possibility of SSRF in pipeline element installation process ## { #CVE-2024-31979 }

CVE-2024-31979 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-31979) [\[CVE json\]](./CVE-2024-31979.cve.json) [\[OSV json\]](./CVE-2024-31979.osv.json)



_Last updated: 2024-07-17T09:03:15.953Z_

### Affected

* Apache StreamPipes through 0.93.0


### Description

Server-Side Request Forgery (SSRF) vulnerability in Apache StreamPipes during installation process of pipeline elements.<br>Previously, StreamPipes allowed users to configure custom endpoints from which to install additional pipeline elements. <br>These endpoints were not properly validated, allowing an attacker to get StreamPipes to send an HTTP GET request to an arbitrary address.<br><p>This issue affects Apache StreamPipes: through 0.93.0.</p><p>Users are recommended to upgrade to version 0.95.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/8lryp3bxnby9kmk13odkz2jbfdjfvf0y


### Credits
* L0ne1y (finder)


## Potential remote code execution (RCE) via file upload ## { #CVE-2024-31411 }

CVE-2024-31411 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-31411) [\[CVE json\]](./CVE-2024-31411.cve.json) [\[OSV json\]](./CVE-2024-31411.osv.json)



_Last updated: 2024-07-17T09:22:06.439Z_

### Affected

* Apache StreamPipes through 0.93.0


### Description

Unrestricted Upload of File with dangerous type vulnerability in Apache StreamPipes.<br>Such a dangerous type might be an executable file that may lead to a remote code execution (RCE).<br>The unrestricted upload is only possible for authenticated and authorized users.<br><p>This issue affects Apache StreamPipes: through 0.93.0.</p><p>Users are recommended to upgrade to version 0.95.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/b0657okbwzg5xxs11hphvc9qrd9s70mt


### Credits
* L0ne1y (finder)


## Potential creation of multiple identical accounts ## { #CVE-2024-30471 }

CVE-2024-30471 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-30471) [\[CVE json\]](./CVE-2024-30471.cve.json) [\[OSV json\]](./CVE-2024-30471.osv.json)



_Last updated: 2024-07-17T09:01:50.452Z_

### Affected

* Apache StreamPipes through 0.93.0


### Description

Time-of-check Time-of-use (TOCTOU) Race Condition vulnerability in Apache StreamPipes in user self-registration.<br>This allows an attacker to potentially request the creation of multiple accounts with the same email address until the email address is registered, creating many identical users and corrupting StreamPipe's user management.<br><p>This issue affects Apache StreamPipes: through 0.93.0.</p><p>Users are recommended to upgrade to version 0.95.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/8yodrmohgcybq900or3d4hc1msl230fr


### Credits
* TonyNT from VNPT-NET (finder)


## Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG) in Recovery Token Generation ## { #CVE-2024-29868 }

CVE-2024-29868 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-29868) [\[CVE json\]](./CVE-2024-29868.cve.json) [\[OSV json\]](./CVE-2024-29868.osv.json)



_Last updated: 2024-06-24T09:59:38.377Z_

### Affected

* Apache StreamPipes from 0.69.0 through 0.93.0
* Apache StreamPipes from 0.69.0 through 0.93.0


### Description

Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG) vulnerability in Apache StreamPipes&nbsp;<span style="background-color: rgb(255, 255, 255);">user self-registration and password recovery mechanism</span>.<br>This allows an attacker to guess the recovery token in a reasonable time and thereby to take over the attacked user's account.<br><p>This issue affects Apache StreamPipes: from 0.69.0 through 0.93.0.</p><p>Users are recommended to upgrade to version 0.95.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/g7t7zctvq2fysrw1x17flnc12592nhx7


### Credits
* Alessandro Albani, Digital Security Division Var Group (finder)


## Resources Permission Escalation ## { #CVE-2024-24778 }

CVE-2024-24778 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-24778) [\[CVE json\]](./CVE-2024-24778.cve.json) [\[OSV json\]](./CVE-2024-24778.osv.json)



_Last updated: 2025-03-03T10:37:02.610Z_

### Affected

* Apache StreamPipes through 0.95.1


### Description

<div></div><div></div><p>Improper privilege management in a REST interface allowed registered users to access unauthorized resources if the resource ID was know. </p><div></div><div></div><p>This issue affects Apache StreamPipes: through 0.95.1.</p><p>Users are recommended to upgrade to version 0.97.0 which fixes the issue.</p>

### References
* https://lists.apache.org/thread/j14w6wghlwwrgfgc6hoz9f94fwxtlgzh


## Privilege escalation through non-admin user ## { #CVE-2023-31469 }

CVE-2023-31469 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-31469) [\[CVE json\]](./CVE-2023-31469.cve.json) [\[OSV json\]](./CVE-2023-31469.osv.json)



_Last updated: 2023-06-23T07:07:40.534Z_

### Affected

* Apache StreamPipes from 0.69.0 through 0.91.0


### Description



A REST interface in Apache StreamPipes (versions 0.69.0 to 0.91.0) <span style="background-color: rgb(255, 255, 255);">was not properly restricted to admin-only access. This </span>allowed a non-admin user with valid login credentials to elevate privileges beyond the initially assigned roles.<br>The issue is resolved by upgrading to StreamPipes 0.92.0.



### References
* https://lists.apache.org/thread/c4y8kf9bzpf36v4bottfmd8tc9cxo19m


### Credits
* Xun Bai, LJQC Open Source Security Institute (finder)
