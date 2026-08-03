---
title: Apache Thrift security advisories
description: Security information for Apache Thrift
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Thrift? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Thrift).

You can read more about the security policy on:

- [Apache Thrift security model](https://github.com/apache/thrift/blob/master/doc/thrift-threat-model.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Python TSSLSocket Hostname Matcher Import ## { #CVE-2026-66053 }

CVE-2026-66053 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66053) [\[CVE json\]](./CVE-2026-66053.cve.json) [\[OSV json\]](./CVE-2026-66053.osv.json)



_Last updated: 2026-07-27T11:18:43.366Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Improper Validation of Certificate with Host Mismatch vulnerability in Apache Thrift Python bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.<br><br>This replaces&nbsp;CVE-2026-41603</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/w4k5dnv1x58knwlhpo9x0or5xh220y65


### Credits
* Yu Bao – yubao@paypal.com, who works for paypal.com (finder)


## C++ THeaderTransport::readString() info-header length bounds bypass ## { #CVE-2026-58662 }

CVE-2026-58662 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58662) [\[CVE json\]](./CVE-2026-58662.cve.json) [\[OSV json\]](./CVE-2026-58662.osv.json)



_Last updated: 2026-07-27T11:17:20.407Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Improper Validation of Specified Quantity in Input, Out-of-bounds Read vulnerability in Apache Thrift C++ bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/13mzvylr3r3nktxrh5k1h30ng1t1sw1d


### Credits
* Javid Khan <dxbjavid@gmail.com> (finder)


## Rust binary protocol non-strict path missing string size limit ## { #CVE-2026-58389 }

CVE-2026-58389 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58389) [\[CVE json\]](./CVE-2026-58389.cve.json) [\[OSV json\]](./CVE-2026-58389.osv.json)



_Last updated: 2026-07-27T11:14:25.617Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Allocation of Resources Without Limits or Throttling vulnerability in Apache Thrift Rust bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/ht2mjt8m3vz9v0h5pqzvc4r4nzfxwtrw


### Credits
* Javid Khan <dxbjavid@gmail.com> (finder)


## c_glib heap out-of-bounds read in transport leftover-bytes path ## { #CVE-2026-58023 }

CVE-2026-58023 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58023) [\[CVE json\]](./CVE-2026-58023.cve.json) [\[OSV json\]](./CVE-2026-58023.osv.json)



_Last updated: 2026-07-27T11:12:35.855Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Out-of-bounds Read vulnerability in Apache Thrift c_glib bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/z2myopbovxngfvchdz8hddots9p5ffbt


## C++ ZLIB heap buffer overflow (write) in THeaderTransport::untransform() ## { #CVE-2026-55971 }

CVE-2026-55971 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-55971) [\[CVE json\]](./CVE-2026-55971.cve.json) [\[OSV json\]](./CVE-2026-55971.osv.json)



_Last updated: 2026-07-27T11:11:18.790Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Heap-based Buffer Overflow vulnerability in Apache Thrift C++ bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/xjs36m6kjxpmrmzwck636msg3nvoqnmx


### Credits
* Ghaith Abdulreda (finder)


## C++ heap out-of-bounds read in THeaderTransport::readHeaderFormat() ## { #CVE-2026-55970 }

CVE-2026-55970 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-55970) [\[CVE json\]](./CVE-2026-55970.cve.json) [\[OSV json\]](./CVE-2026-55970.osv.json)



_Last updated: 2026-07-27T11:09:36.113Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Buffer Over-read vulnerability in Apache Thrift C++ bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/8pbnw4dyxxc9opp6qq725jhrzg25v8q7


### Credits
* Ghaith Abdulreda (finder)


## integer overflow in TProtocol::checkReadBytesAvailable() ## { #CVE-2026-55969 }

CVE-2026-55969 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-55969) [\[CVE json\]](./CVE-2026-55969.cve.json) [\[OSV json\]](./CVE-2026-55969.osv.json)



_Last updated: 2026-07-27T11:07:43.565Z_

### Affected

* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0


### Description

<p>Integer Overflow or Wraparound vulnerability in Apache Thrift C++, c_glib, Go, netstd, Delphi and Haxe bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/xmkgd107k795hyrg5kf97mny30sgl5bo


### Credits
* Ghaith Abdulreda (finder)
* Javid Khan (finder)
* Apache Thrift Developers (finder)


## Node.js quadratic-time DoS in server receive transports ## { #CVE-2026-55968 }

CVE-2026-55968 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-55968) [\[CVE json\]](./CVE-2026-55968.cve.json) [\[OSV json\]](./CVE-2026-55968.osv.json)



_Last updated: 2026-07-27T11:06:12.486Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Inefficient Algorithmic Complexity, Allocation of Resources Without Limits or Throttling vulnerability in Apache Thrift Node.js bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/gxhhfyr6flr5vzr4qnxm13p6fc41qstp


### Credits
* Song Jihoon (finder)


## Ruby THeaderTransport ZLIB Decompression Bomb ## { #CVE-2026-49158 }

CVE-2026-49158 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49158) [\[CVE json\]](./CVE-2026-49158.cve.json) [\[OSV json\]](./CVE-2026-49158.osv.json)



_Last updated: 2026-07-27T11:05:01.307Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Improper Handling of Highly Compressed Data (Data Amplification) vulnerability in Apache Thrift Ruby bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/fmjl8l415tj9zwlob8v2dr5hq1d0hts7


### Credits
* LTSHFWJT <1719636402@qq.com> (finder)


## TZlibTransport Decompression Size Limit ## { #CVE-2026-48586 }

CVE-2026-48586 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48586) [\[CVE json\]](./CVE-2026-48586.cve.json) [\[OSV json\]](./CVE-2026-48586.osv.json)



_Last updated: 2026-07-27T11:02:50.181Z_

### Affected

* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0


### Description

<p>Improper Handling of Highly Compressed Data (Data Amplification) vulnerability in Apache Thrift C++, Java, Python, Go, D, C/GLib bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/p008svsjf9p6bj47wyyf5dgglq5z7xoq


## C++ TSSLSocket matchName() RFC 6125 Wildcard Bypass ## { #CVE-2026-48145 }

CVE-2026-48145 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48145) [\[CVE json\]](./CVE-2026-48145.cve.json) [\[OSV json\]](./CVE-2026-48145.osv.json)



_Last updated: 2026-07-27T10:59:40.690Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Improper Validation of Certificate with Host Mismatch vulnerability in Apache Thrift C++ bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/2popgc4ks1l87jjho1w5fpk5k4x06b7h


## c_glib TLS Client Missing Hostname Verification ## { #CVE-2026-48144 }

CVE-2026-48144 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48144) [\[CVE json\]](./CVE-2026-48144.cve.json) [\[OSV json\]](./CVE-2026-48144.osv.json)



_Last updated: 2026-07-27T10:58:24.417Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Improper Validation of Certificate with Host Mismatch vulnerability in Apache Thrift c_glib bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/2xoltfxgzf5jyhcwq6y07spts5cn6ppj


## Unbounded Read Leading to Denial of Service ## { #CVE-2026-45112 }

CVE-2026-45112 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45112) [\[CVE json\]](./CVE-2026-45112.cve.json) [\[OSV json\]](./CVE-2026-45112.osv.json)



_Last updated: 2026-07-27T10:57:25.527Z_

### Affected

* Apache Thrift from 0.19.0 before 0.24.0


### Description

<p>Allocation of Resources Without Limits or Throttling vulnerability in Apache Thrift Java bindings.</p><p>This issue affects Apache Thrift: from 0.19.0 before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/hl9kmf1z2o3lxvspoj3g9ykl8lj9mdxc


### Credits
* IcySun & Yashon (finder)


## TCompactProtocol varint byte-count limit ## { #CVE-2026-43871 }

CVE-2026-43871 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43871) [\[CVE json\]](./CVE-2026-43871.cve.json) [\[OSV json\]](./CVE-2026-43871.osv.json)



_Last updated: 2026-07-27T10:56:06.868Z_

### Affected

* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0
* Apache Thrift before 0.24.0


### Description

Loop with Unreachable Exit Condition ('Infinite Loop') vulnerability in Apache Thrift Python, Go, PHP and Java bindings.<p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/l4dwf14zbyqsmkc28c99ojj3t3gg9qby


### Credits
* Yu Bao - yubao@paypal.com, who works for paypal.com (finder)


## Node.js web_server.js multi-vulnerability ## { #CVE-2026-43870 }

CVE-2026-43870 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43870) [\[CVE json\]](./CVE-2026-43870.cve.json) [\[OSV json\]](./CVE-2026-43870.osv.json)



_Last updated: 2026-08-01T15:14:33.689Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Origin Validation Error, Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'), Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Request/Response Splitting'), Uncontrolled Resource Consumption vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/pgtfq44ltc9t63kxcbqmwqzt45pnhqdy


## TSSLTransportFactory.java hostname verification ## { #CVE-2026-43869 }

CVE-2026-43869 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43869) [\[CVE json\]](./CVE-2026-43869.cve.json) [\[OSV json\]](./CVE-2026-43869.osv.json)



_Last updated: 2026-08-01T15:15:50.815Z_

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



_Last updated: 2026-07-15T20:56:45.279Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Uncontrolled Recursion vulnerability in Apache Thrift Node.js bindings</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lb4j0zyd5f3g36cos0wql925przpnwql


### Credits
* Sion Park (L3G4CY Security Research) (finder)
* Yu Bao – yubao@paypal.com (finder)


## Unbounded Zlib Decompression in Python THeaderTransport ## { #CVE-2026-41608 }

CVE-2026-41608 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41608) [\[CVE json\]](./CVE-2026-41608.cve.json) [\[OSV json\]](./CVE-2026-41608.osv.json)



_Last updated: 2026-08-01T15:15:08.921Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Improper Handling of Highly Compressed Data (Data Amplification) vulnerability in Apache Thrift Python bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/vwsbcwqdpwdtp8qkjo11ol6rodbfm21f


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
