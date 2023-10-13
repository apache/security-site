---
title: Apache Portable Runtime (APR) security advisories
description: Security information for Apache Portable Runtime (APR)
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Portable Runtime (APR)? You can read more about the projects' security policy on their [security page](https://apr.apache.org/security_report.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://apr.apache.org/security_report.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## out-of-bounds writes in the apr_base64 family of functions ## { #CVE-2022-25147 }

CVE-2022-25147 [\[CVE json\]](./CVE-2022-25147.cve.json)

### Affected

* Apache Portable Runtime Utility (APR-util) through 1.6.1


### Description

<div>Integer Overflow or Wraparound vulnerability in apr_base64 functions of Apache Portable Runtime Utility (APR-util) allows an attacker to write beyond bounds of a buffer.</div><div><br></div><div>This issue affects Apache Portable Runtime Utility (APR-util) 1.6.1 and prior versions.</div>

### References
* https://lists.apache.org/thread/np5gjqlohc4f62lr09vrn61vl44cylh8


### Credits
* Ronald Crane (Zippenhop LLC) (reporter)


## out-of-bound writes in the apr_encode family of functions  ## { #CVE-2022-24963 }

CVE-2022-24963 [\[CVE json\]](./CVE-2022-24963.cve.json)

### Affected

* Apache Portable Runtime (APR) at 1.7.0


### Description

Integer Overflow or Wraparound vulnerability in apr_encode functions of Apache Portable Runtime (APR) allows an attacker to write beyond bounds of a buffer.<br>This issue affects Apache Portable Runtime (APR) version 1.7.0.

### References
* https://lists.apache.org/thread/fw9p6sdncwsjkstwc066vz57xqzfksq9


### Credits
* Ronald Crane (Zippenhop LLC) (finder)


##  Windows out-of-bounds write in apr_socket_sendv function ## { #CVE-2022-28331 }

CVE-2022-28331 [\[CVE json\]](./CVE-2022-28331.cve.json)

### Affected

* Apache Portable Runtime (APR) through 1.7.0


### Description

On Windows, Apache Portable Runtime 1.7.0 and earlier may write beyond the end of a stack based buffer in apr_socket_sendv(). This is a result of integer overflow.

### References
* https://lists.apache.org/thread/5pfdfn7h0vsdo5xzjn97vghp0x42jj2r


### Credits
* Ronald Crane (Zippenhop LLC) (finder)
