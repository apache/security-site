---
title: Apache Portable Runtime (APR) security advisories
description: Security information for Apache Portable Runtime (APR)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Portable Runtime (APR)? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Portable%20Runtime%20%28APR%29).

You can read more about the security policy on:

- [Apache Portable Runtime (APR) security model](https://apr.apache.org/security_report.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Heap buffer overflow in APR memcached client ## { #CVE-2026-34502 }

CVE-2026-34502 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34502) [\[CVE json\]](./CVE-2026-34502.cve.json) [\[OSV json\]](./CVE-2026-34502.osv.json)



_Last updated: 2026-08-06T14:31:06.399Z_

### Affected

* Apache Portable Runtime Utility from 1.3.0 through 1.6.3


### Description

<p>Heap-based Buffer Overflow vulnerability in Apache Portable Runtime Utility memcached client</p><p>This issue affects Apache Portable Runtime Utility: from 1.3.0 through 1.6.3.<br></p>

### References
* https://lists.apache.org/thread/spk5643m4vq0mb8h5b9hz9gkp57ombl8


### Credits
* Elhanan Haenel (finder)


## Heap buffer overflow in APR redis client ## { #CVE-2026-34501 }

CVE-2026-34501 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34501) [\[CVE json\]](./CVE-2026-34501.cve.json) [\[OSV json\]](./CVE-2026-34501.osv.json)



_Last updated: 2026-08-06T14:31:46.904Z_

### Affected

* Apache Portable Runtime Utility from 1.6.0 through 1.6.3


### Description

<p>Heap-based Buffer Overflow vulnerability in Apache Portable Runtime Utility redis client.</p><p>This issue affects Apache Portable Runtime Utility: from 1.6.0 through 1.6.3.</p><p>Users are recommended to upgrade to version 1.6.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/o8h6c7cq86fplxlnry6c3rn9x0ovq8mv


### Credits
* Elhanan Haenel (finder)


## SQL Injection in apr_dbd_oracle ## { #CVE-2026-34191 }

CVE-2026-34191 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34191) [\[CVE json\]](./CVE-2026-34191.cve.json) [\[OSV json\]](./CVE-2026-34191.osv.json)



_Last updated: 2026-08-06T14:32:23.055Z_

### Affected

* Apache Portable Runtime Utility from 1.6.0 through 1.6.3


### Description

<p>Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Portable Runtime Utility via apr_dbd_oracle provider.</p><p>This issue affects Apache Portable Runtime Utility: from 1.6.0 through 1.6.3<br></p>

### References
* https://lists.apache.org/thread/8xch90zogywwpo5wnsf4o088mkxy4qtf


### Credits
* Elhanan Haenel (finder)


## apr-util XML stack recursion crash ## { #CVE-2026-32327 }

CVE-2026-32327 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-32327) [\[CVE json\]](./CVE-2026-32327.cve.json) [\[OSV json\]](./CVE-2026-32327.osv.json)



_Last updated: 2026-08-06T14:32:41.688Z_

### Affected

* Apache Portable Runtime Utility through 1.6.3


### Description

A bug in APR-util version 1.6.3 (and earlier) allows a stack recursion attack against any library consumer which parses XML from untrusted sources and uses the&nbsp;apr_xml_quote_elem() function.<br><br>Users are recommended to upgrade to version 1.6.4, which fixes this issue.

### References
* https://lists.apache.org/thread/hq27vj8yfno9tkwv0fpj6jksfzgxvth1


### Credits
* Younghyo Cho @ CISLab, SeoulTech (finder)
* 4ra1n, pyn3rd and unam4 (finder)


## apr_password_validate() vulnerable to timing attack ## { #CVE-2025-49506 }

CVE-2025-49506 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-49506) [\[CVE json\]](./CVE-2025-49506.cve.json) [\[OSV json\]](./CVE-2025-49506.osv.json)



_Last updated: 2026-08-06T14:33:11.589Z_

### Affected

* Apache Portable Runtime Utility from 1.2.0 through 1.6.3


### Description

<div>APR-util versions 1.6.3 (and earlier) function apr_password_validate() was not constant-time with regards to hashes or passwords comparisons, potentially leaking their content via a side channel timing attack particularly on platforms without crypt() such as&nbsp;<span style="background-color: rgb(255, 255, 255);">&nbsp;Windows, BeOS, NetWare, or Android.</span></div><div>Users are recommended to upgrade to version 1.6.4, which fixes this issue.<br></div><div></div>

### References
* https://lists.apache.org/thread/2v8o3bj9pb7lfcr57bdnjg9xfkj04mg5


### Credits
* Michael Rowley <michael csirt.global> (finder)


## Unexpected lax shared memory permissions ## { #CVE-2023-49582 }

CVE-2023-49582 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49582) [\[CVE json\]](./CVE-2023-49582.cve.json) [\[OSV json\]](./CVE-2023-49582.osv.json)



_Last updated: 2026-08-06T13:47:55.389Z_

### Affected

* Apache Portable Runtime (APR) from 0.9.0 through 1.7.4


### Description

Lax permissions set by the Apache Portable Runtime library on Unix platforms would allow local users read access to named shared memory segments, potentially revealing sensitive application data. <br><br>This issue does not affect non-Unix platforms, or builds with&nbsp;APR_USE_SHMEM_SHMGET=1 (apr.h)<br><br>Users are recommended to upgrade to APR version 1.7.5, which fixes this issue.

### References
* https://lists.apache.org/thread/sntjc04t1rvjhdzz2tzmtz2zdnmv7dc4


### Credits
* Thomas Stangner (reporter)


##  Windows out-of-bounds write in apr_socket_sendv function ## { #CVE-2022-28331 }

CVE-2022-28331 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-28331) [\[CVE json\]](./CVE-2022-28331.cve.json) [\[OSV json\]](./CVE-2022-28331.osv.json)



_Last updated: 2023-07-07T15:26:37.824Z_

### Affected

* Apache Portable Runtime (APR) through 1.7.0


### Description

On Windows, Apache Portable Runtime 1.7.0 and earlier may write beyond the end of a stack based buffer in apr_socket_sendv(). This is a result of integer overflow.

### References
* https://lists.apache.org/thread/5pfdfn7h0vsdo5xzjn97vghp0x42jj2r


### Credits
* Ronald Crane (Zippenhop LLC) (finder)


## out-of-bounds writes in the apr_base64 family of functions ## { #CVE-2022-25147 }

CVE-2022-25147 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-25147) [\[CVE json\]](./CVE-2022-25147.cve.json) [\[OSV json\]](./CVE-2022-25147.osv.json)



_Last updated: 2023-01-31T15:54:46.758Z_

### Affected

* Apache Portable Runtime Utility (APR-util) through 1.6.1


### Description

<div>Integer Overflow or Wraparound vulnerability in apr_base64 functions of Apache Portable Runtime Utility (APR-util) allows an attacker to write beyond bounds of a buffer.</div><div><br></div><div>This issue affects Apache Portable Runtime Utility (APR-util) 1.6.1 and prior versions.</div>

### References
* https://lists.apache.org/thread/np5gjqlohc4f62lr09vrn61vl44cylh8


### Credits
* Ronald Crane (Zippenhop LLC) (reporter)


## out-of-bound writes in the apr_encode family of functions  ## { #CVE-2022-24963 }

CVE-2022-24963 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-24963) [\[CVE json\]](./CVE-2022-24963.cve.json) [\[OSV json\]](./CVE-2022-24963.osv.json)



_Last updated: 2023-01-31T15:51:53.920Z_

### Affected

* Apache Portable Runtime (APR) at 1.7.0


### Description

Integer Overflow or Wraparound vulnerability in apr_encode functions of Apache Portable Runtime (APR) allows an attacker to write beyond bounds of a buffer.<br>This issue affects Apache Portable Runtime (APR) version 1.7.0.

### References
* https://lists.apache.org/thread/fw9p6sdncwsjkstwc066vz57xqzfksq9


### Credits
* Ronald Crane (Zippenhop LLC) (finder)


## Regression of CVE-2017-12613 ## { #CVE-2021-35940 }

CVE-2021-35940 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-35940) [\[CVE json\]](./CVE-2021-35940.cve.json) [\[OSV json\]](./CVE-2021-35940.osv.json)



_Last updated: 2021-10-11T14:15:55.651Z_

### Affected

* Apache Portable Runtime (APR) at Apache Portable Runtime 1.7.0


### Description

An out-of-bounds array read in the apr_time_exp*() functions was fixed in the Apache Portable Runtime 1.6.3 release (CVE-2017-12613).  The fix for this issue was not carried forward to the APR 1.7.x branch, and hence version 1.7.0 regressed compared to 1.6.3 and is vulnerable to the same issue.

### References
* http://svn.apache.org/viewvc?view=revision&revision=1891198%20
* http://mail-archives.apache.org/mod_mbox/www-announce/201710.mbox/%3CCACsi251B8UaLvM-rrH9fv57-zWi0zhyF3275_jPg1a9VEVVoxw%40mail.gmail.com%3E
* https://downloads.apache.org/apr/patches/apr-1.7.0-CVE-2021-35940.patch
* https://lists.apache.org/thread.html/ra2868b53339a6af65577146ad87016368c138388b09bff9d2860f50e%40%3Cdev.apr.apache.org%3E


### Credits
* The Apache Portable Runtime project would like to thank Iveta Cesalova (Red Hat) for reporting this issue.
