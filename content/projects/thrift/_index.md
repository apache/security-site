---
title: Apache Thrift security advisories
description: Security information for Apache Thrift
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Thrift? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Node.js web_server.js multi-vulnerability ## { #CVE-2026-43870 }

CVE-2026-43870 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43870) [\[CVE json\]](./CVE-2026-43870.cve.json) [\[OSV json\]](./CVE-2026-43870.osv.json)



_Last updated: 2026-05-05T07:45:34.804Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Origin Validation Error, Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'), Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Request/Response Splitting'), Uncontrolled Resource Consumption vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/pgtfq44ltc9t63kxcbqmwqzt45pnhqdy


## TSSLTransportFactory.java hostname verification ## { #CVE-2026-43869 }

CVE-2026-43869 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43869) [\[CVE json\]](./CVE-2026-43869.cve.json) [\[OSV json\]](./CVE-2026-43869.osv.json)



_Last updated: 2026-05-05T07:25:46.713Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Improper Validation of Certificate with Host Mismatch vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/3hsgl1b69wzq3ry39scqbv2dhyl3j52r


## Rust implementation vulnerable to CVE-2020-13949 pattern ## { #CVE-2026-43868 }

CVE-2026-43868 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43868) [\[CVE json\]](./CVE-2026-43868.cve.json) [\[OSV json\]](./CVE-2026-43868.osv.json)



_Last updated: 2026-05-05T07:49:46.378Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Memory Allocation with Excessive Size Value vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zj76dtwnbbs1m7z3focf4wd51pqpsmn9


## Node.js skip() recursion ## { #CVE-2026-41636 }

CVE-2026-41636 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41636) [\[CVE json\]](./CVE-2026-41636.cve.json) [\[OSV json\]](./CVE-2026-41636.osv.json)



_Last updated: 2026-05-18T16:56:58.433Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Uncontrolled Recursion vulnerability in Apache Thrift Node.js bindings</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lb4j0zyd5f3g36cos0wql925przpnwql


### Credits
* Sion Park (L3G4CY Security Research) (finder)
* Yu Bao – yubao@paypal.com (finder)


## C++ JSON OOB read ## { #CVE-2026-41607 }

CVE-2026-41607 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41607) [\[CVE json\]](./CVE-2026-41607.cve.json) [\[OSV json\]](./CVE-2026-41607.osv.json)



_Last updated: 2026-04-28T09:21:46.727Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Out-of-bounds Read vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lb4j0zyd5f3g36cos0wql925przpnwql


### Credits
* Hasnain Lakhani (finder)


## c_glib dispatch stack overflow ## { #CVE-2026-41606 }

CVE-2026-41606 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41606) [\[CVE json\]](./CVE-2026-41606.cve.json) [\[OSV json\]](./CVE-2026-41606.osv.json)



_Last updated: 2026-04-28T09:21:09.783Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Uncontrolled Recursion vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lb4j0zyd5f3g36cos0wql925przpnwql


### Credits
* Hasnain Lakhani (finder)


## Swift Compact Protocol integer overflow ## { #CVE-2026-41605 }

CVE-2026-41605 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41605) [\[CVE json\]](./CVE-2026-41605.cve.json) [\[OSV json\]](./CVE-2026-41605.osv.json)



_Last updated: 2026-04-28T09:20:43.166Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Integer Overflow or Wraparound vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lb4j0zyd5f3g36cos0wql925przpnwql


### Credits
* Hasnain Lakhani (finder)


## Swift Range crash in skip() ## { #CVE-2026-41604 }

CVE-2026-41604 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41604) [\[CVE json\]](./CVE-2026-41604.cve.json) [\[OSV json\]](./CVE-2026-41604.osv.json)



_Last updated: 2026-04-28T09:20:12.306Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Out-of-bounds Read vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lb4j0zyd5f3g36cos0wql925przpnwql


### Credits
* Hasnain Lakhani (finder)


## Java TSSLTransportFactory hostname verification ## { #CVE-2026-41603 }

CVE-2026-41603 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41603) [\[CVE json\]](./CVE-2026-41603.cve.json) [\[OSV json\]](./CVE-2026-41603.osv.json)



_Last updated: 2026-05-18T16:57:00.465Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Improper Validation of Certificate with Host Mismatch vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lb4j0zyd5f3g36cos0wql925przpnwql


### Credits
* Yu Bao – yubao@paypal.com (finder)
*  (finder)


## Go TFramedTransport uint32 overflow ## { #CVE-2026-41602 }

CVE-2026-41602 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41602) [\[CVE json\]](./CVE-2026-41602.cve.json) [\[OSV json\]](./CVE-2026-41602.osv.json)



_Last updated: 2026-04-28T09:19:05.731Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Integer Overflow or Wraparound vulnerability in Apache Thrift TFramedTransport Go language implementation</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lb4j0zyd5f3g36cos0wql925przpnwql


### Credits
* 김범수 (finder)


## Specially crafted input can crash a c_glib Thrift server with invalid pointer error. ## { #CVE-2025-48431 }

CVE-2025-48431 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-48431) [\[CVE json\]](./CVE-2025-48431.cve.json) [\[OSV json\]](./CVE-2025-48431.osv.json)



_Last updated: 2026-04-28T09:11:42.895Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Mismatched Memory Management Routines vulnerability in Apache Thrift c_glib language bindings.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.<br><br>Description: Specially crafted requests can crash an c_glib-based Thrift server with a clean but fatal "free(): invalid pointer" error message.<br><br></p>

### References
* https://lists.apache.org/thread/lb4j0zyd5f3g36cos0wql925przpnwql


### Credits
* Hasnain Lakhani (finder)
* Hasnain Lakhani (remediation developer)
