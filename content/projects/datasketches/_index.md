---
title: Apache DataSketches security advisories
description: Security information for Apache DataSketches
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache DataSketches? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=DataSketches).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Out-of-bounds write in REQ sketch deserialization allows memory corruption via a crafted sketch ## { #CVE-2026-123338 }

CVE-2026-123338 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-123338) [\[CVE json\]](./CVE-2026-123338.cve.json) [\[OSV json\]](./CVE-2026-123338.osv.json)



_Last updated: 2026-11-13T10:32:37.055Z_

### Affected

* Apache DataSketches C++ from 3.0.0 through 5.3.0


### Description

Out-of-bounds Write vulnerability in Apache DataSketches C++. An<br>  application that deserializes a REQ sketch from an untrusted source<br>  can have heap memory corrupted by a crafted sketch, because the<br>  serialized compactor headers were not validated.<br><br>  This issue affects Apache DataSketches C++: from 3.0.0 through 5.3.0.<br><br>  Users are recommended to upgrade to version 5.3.1, which fixes the<br>  issue.

### References
* https://lists.apache.org/thread/wjsso4wl0f0nczwh7gd74kc5wckn1635
* https://github.com/apache/datasketches-cpp/releases/tag/5.3.1
* https://github.com/apache/datasketches-cpp/commit/9839ffd2ccc038d453e38b545750a5ed2d589dea
* https://github.com/apache/datasketches-cpp/pull/568


## Out-of-bounds write in KLL sketch deserialization allows memory corruption via a crafted sketch ## { #CVE-2026-123274 }

CVE-2026-123274 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-123274) [\[CVE json\]](./CVE-2026-123274.cve.json) [\[OSV json\]](./CVE-2026-123274.osv.json)



_Last updated: 2026-11-13T10:34:24.297Z_

### Affected

* Apache DataSketches C++ from 1.0.0-incubating through 5.3.0


### Description

Out-of-bounds Write vulnerability in Apache DataSketches C++. An<br>  application that deserializes a KLL sketch from an untrusted source<br>  can have heap memory corrupted by a crafted sketch, because the<br>  serialized level boundaries were not validated.<br><br>  This issue affects Apache DataSketches C++: 2.0.0 through 5.3.0.<br><br>  Users are recommended to upgrade to version 5.3.1, which fixes the<br>  issue.

### References
* https://lists.apache.org/thread/t4rngyg9cbv1b42f1d0crgpgtpby0594
* https://github.com/apache/datasketches-cpp/releases/tag/5.3.1
* https://github.com/apache/datasketches-cpp/commit/bb86d439db494e3d362e54cc4f83481893974335
* https://github.com/apache/datasketches-cpp/pull/568


### Credits
* hataehoon (reporter)


## Uncontrolled resource consumption when deserializing crafted sketch images ## { #CVE-2026-122096 }

CVE-2026-122096 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-122096) [\[CVE json\]](./CVE-2026-122096.cve.json) [\[OSV json\]](./CVE-2026-122096.osv.json)



_Last updated: 2026-11-13T10:37:12.257Z_

### Affected

* Apache DataSketches Java through 9.0.0


### Description

<p>Uncontrolled Resource Consumption vulnerability in the sketch deserialization of Apache DataSketches Java.</p><p>Several deserializers trusted sizes and counts declared in the serialized input. A small crafted input could make an application allocate an excessive amount of memory, leading to an OutOfMemoryError. A crafted string passed to FrequentLongsSketch.getInstance(String) could also make deserialization, or a later update, loop indefinitely. Only applications that deserialize sketches from untrusted sources are affected.</p><p>This issue affects Apache DataSketches Java: through 9.0.0.</p><p>Users are recommended to upgrade to version 9.1.0, which fixes the issue.</p>

### References
* https://github.com/apache/datasketches-java/releases/tag/9.1.0
* https://github.com/apache/datasketches-java/pull/777
* https://github.com/apache/datasketches-java/pull/783
* https://lists.apache.org/thread/9wd7ngmho7hm8x74sq1p2fp1xgjd8kt6


### Credits
* Jaideep Pyne (finder)


## datasketches-cpp: Out-of-bounds read in VarOpt union deserialization allows denial of service via a truncated sketch ## { #CVE-2026-103636 }

CVE-2026-103636 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-103636) [\[CVE json\]](./CVE-2026-103636.cve.json) [\[OSV json\]](./CVE-2026-103636.osv.json)



_Last updated: 2026-10-10T10:23:57.384Z_

### Affected

* Apache DataSketches from 2.0.0-incubating through 5.2.0


### Description

Out-of-bounds read in the VarOpt union deserialization of Apache DataSketches C++ (repo: datasketches-cpp).<br><br>var_opt_union::deserialize() read the 32-byte preamble of a non-empty union after checking that only 8 bytes were available, so a truncated serialized union could cause a read of up to 24 bytes past the end of the input. For such inputs, the size remaining for the embedded sketch was also computed by an unsigned subtraction that could wrap around, so the embedded sketch's own size checks no longer limited reads to the input. The bytes read can become part of the deserialized union's state. This can cause a crash (denial of service) and could expose adjacent memory contents.<br><br>This issue affects Apache DataSketches C++: from 2.0.0-incubating before 5.3.0. Only applications that deserialize VarOpt unions from untrusted sources are affected.<br><br>Users are recommended to upgrade to version 5.3.0, which fixes this issue.

### References
* https://lists.apache.org/thread/znn94s463w7wy125khcywxsp82y2qkq5
* https://github.com/apache/datasketches-cpp/releases/tag/5.3.0


### Credits
* He Huang (finder)
* NexusSan (tool)


## datasketches-cpp: Out-of-bounds read in compact Theta sketch deserialization allows denial of service via a crafted sketch ## { #CVE-2026-103635 }

CVE-2026-103635 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-103635) [\[CVE json\]](./CVE-2026-103635.cve.json) [\[OSV json\]](./CVE-2026-103635.osv.json)



_Last updated: 2026-10-10T10:23:47.068Z_

### Affected

* Apache DataSketches from 3.1.0 through 5.2.0


### Description

Out-of-bounds read in the compact Theta sketch deserialization of Apache DataSketches C++ (repo: datasketches-cpp).<br><br>compact_theta_sketch::deserialize() and wrapped_compact_theta_sketch::wrap() read header fields before checking that the input was long enough. For the compressed format, the size check could be defeated by a 32-bit overflow, and two header fields that control decoding were not validated; this also affected deserialization from a stream. A crafted or truncated sketch could cause a read past the end of the input. In the compressed case the over-read can be large, and the bytes read can become part of the deserialized sketch. This can cause a crash (denial of service) and could expose adjacent memory contents.<br><br>This issue affects Apache DataSketches C++: from 3.1.0 before 5.3.0. Only applications that deserialize Theta sketches from untrusted sources are affected.<br><br>Users are recommended to upgrade to version 5.3.0, which fixes this issue.

### References
* https://lists.apache.org/thread/15b86y9jstco39kzppjw7l5kvhjvwqvv
* https://github.com/apache/datasketches-cpp/releases/tag/5.3.0


### Credits
* He Huang (finder)
* NexusSan (tool)


## datasketches-cpp: Out-of-bounds read and write in Count-Min sketch deserialization allows memory corruption via a crafted sketch ## { #CVE-2026-103634 }

CVE-2026-103634 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-103634) [\[CVE json\]](./CVE-2026-103634.cve.json) [\[OSV json\]](./CVE-2026-103634.osv.json)



_Last updated: 2026-10-10T10:23:36.255Z_

### Affected

* Apache DataSketches from 4.1.0 through 5.2.0


### Description

<div>Out-of-bounds read and write in the Count-Min sketch deserialization of Apache DataSketches C++ (repo: datasketches-cpp).<br><br>count_min_sketch::deserialize() did not include the preamble in its input size check, so a truncated sketch could cause a read of up to 16 bytes past the end of the input. In addition, the table size was computed from the serialized number of buckets and number of hash functions in 32-bit arithmetic. A crafted sketch could make it wrap to zero, so that the sketch deserialized with an empty table, and later updates and estimate queries read and wrote outside the heap allocation. This can corrupt heap memory, causing a crash and potentially enabling further exploitation.<br><br>This issue affects Apache DataSketches C++: from 4.1.0 before 5.3.0. Only applications that deserialize Count-Min sketches from untrusted sources are affected.<br><br>Users are recommended to upgrade to version 5.3.0, which fixes this issue.</div>

### References
* https://lists.apache.org/thread/rkx9oh06g5cjc6vmmpqloxwfz0gzz01h
* https://github.com/apache/datasketches-cpp/releases/tag/5.3.0


### Credits
* He Huang (finder)
* NexusSan (tool)


## datasketches-cpp: Out-of-bounds read and write in the CPC sketch deserialization allows memory corruption via a crafted sketch ## { #CVE-2026-103513 }

CVE-2026-103513 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-103513) [\[CVE json\]](./CVE-2026-103513.cve.json) [\[OSV json\]](./CVE-2026-103513.osv.json)



_Last updated: 2026-10-10T10:23:18.729Z_

### Affected

* Apache DataSketches from 2.0.0-incubating through 5.2.0


### Description

Out-of-bounds read and write in the CPC sketch deserialization of Apache DataSketches C++ (repo: datasketches-cpp).<br><br>A crafted serialized CPC sketch passed to cpc_sketch::deserialize(), from either a byte buffer or a stream, can cause the decompressor to read past the end of the compressed data, because the read position was only checked after decoding finished. In the hybrid flavor, it can also cause a write outside an internal heap buffer, because decoded row indices were not validated. Several other header fields and decoded values, including lg_k, were also not validated. This can corrupt heap memory, causing a crash and potentially enabling further exploitation.<br><br>This issue affects Apache DataSketches C++: from 2.0.0-incubating before 5.3.0. Only applications that deserialize CPC sketches from untrusted sources are affected.<br><br>Users are recommended to upgrade to version 5.3.0, which fixes this issue.

### References
* https://lists.apache.org/thread/s7wyoqyf120dl5ys8jtr26dskd6m485h
* https://github.com/apache/datasketches-cpp/releases/tag/5.3.0


### Credits
* He Huang (finder)
* NexusSan (tool)


## datasketches-cpp: HLL CouponList Deserialization Buffer Overflow allows memory corruption via a crafted sketch ## { #CVE-2026-103501 }

CVE-2026-103501 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-103501) [\[CVE json\]](./CVE-2026-103501.cve.json) [\[OSV json\]](./CVE-2026-103501.osv.json)



_Last updated: 2026-10-10T10:22:53.936Z_

### Affected

* Apache DataSketches from 1.0.0-incubating through 5.2.0


### Description

Heap buffer overflow in the HLL sketch deserialization of Apache DataSketches C++ (repo: datasketches-cpp).<br><br>When deserializing a sketch in LIST mode, from either a byte buffer or a stream, the coupon count was read from the input and used as the number of entries to copy into a fixed buffer of 8 entries, without checking it against the buffer's capacity. A crafted sketch could cause a write of up to 988 bytes past the end of this internal heap buffer. This can corrupt heap memory, causing a crash and potentially enabling further exploitation.<br><br>This issue affects Apache DataSketches C++: from 1.0.0-incubating before 5.3.0. Only applications that deserialize HLL sketches from untrusted sources are affected.<br><br>Users are recommended to upgrade to version 5.3.0, which fixes this issue.

### References
* https://lists.apache.org/thread/n2oc2j841dzsv4239jjp08of66bo79c5
* https://github.com/apache/datasketches-cpp/releases/tag/5.3.0


### Credits
* Reported anonymously. (finder)
