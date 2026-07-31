---
title: Apache Traffic Server security advisories
description: Security information for Apache Traffic Server
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Traffic Server? Send your report to the [Apache Traffic Server Security Team](mailto:security@trafficserver.apache.org?subject=Traffic%20Server).

You can read more about the security policy on:

- [Apache Traffic Server security model](https://github.com/apache/trafficserver/security/policy)
- [Apache Traffic Server Ingress Controller security model](https://github.com/apache/trafficserver-ingress-controller/security/policy)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security pages linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## HTTP/2 multiplexed origin sessions are reused without certificate re-verification ## { #CVE-2026-65325 }

CVE-2026-65325 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-65325) [\[CVE json\]](./CVE-2026-65325.cve.json) [\[OSV json\]](./CVE-2026-65325.osv.json)



_Last updated: 2026-07-29T08:23:24.104Z_

### Affected

* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server reuses multiplexed HTTP/2 origin connections without verifying the server certificate covers the new request hostname.</p><p>This issue affects Apache Traffic Server: from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## HTTP/2 and HTTP/3 dechunking removes per-stream buffer cap, allowing memory exhaustion ## { #CVE-2026-65324 }

CVE-2026-65324 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-65324) [\[CVE json\]](./CVE-2026-65324.cve.json) [\[OSV json\]](./CVE-2026-65324.osv.json)



_Last updated: 2026-07-29T08:17:42.240Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server drops the per-stream buffer cap when dechunking HTTP/2 or HTTP/3 responses, letting a slow client exhaust server memory.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## HPACK encoder desynchronizes from the decoder after a failed header encode ## { #CVE-2026-65100 }

CVE-2026-65100 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-65100) [\[CVE json\]](./CVE-2026-65100.cve.json) [\[OSV json\]](./CVE-2026-65100.osv.json)



_Last updated: 2026-07-29T09:06:12.502Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server updates the HTTP/2 HPACK dynamic table before confirming the header block encoded successfully, so an encode failure leaves the encoder out of sync with the peer decoder and corrupts subsequent header blocks on the connection.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)
* Apache Community (reporter)


## DoS vulnerability in HTTP/2 via stalled flow-control conditions ## { #CVE-2026-59173 }

CVE-2026-59173 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-59173) [\[CVE json\]](./CVE-2026-59173.cve.json) [\[OSV json\]](./CVE-2026-59173.osv.json)



_Last updated: 2026-07-18T12:52:08.684Z_

### Affected

* Apache Traffic Server from 9.0.0 through 9.2.13
* Apache Traffic Server from 10.0.0 through 10.1.2


### Description

<p>Uncontrolled Resource Consumption vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 9.0.0 through 9.1.13, from 10.0.0 through 10.1.2.</p><p>Users are recommended to upgrade to version 9.1.14 or 10.1.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lhlbhphmv5dsfgx1fx84mgonzbocpzhd


### Credits
* Okta Red Team (reporter)


## Plugins resetting the redirect counter enable SSRF amplification ## { #CVE-2026-58189 }

CVE-2026-58189 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58189) [\[CVE json\]](./CVE-2026-58189.cve.json) [\[OSV json\]](./CVE-2026-58189.osv.json)



_Last updated: 2026-07-29T09:05:13.041Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server allows redirect-limit bypass when plugins reset the retry counter, enabling SSRF amplification.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## Memory-safety and limit-bypass errors across experimental plugins ## { #CVE-2026-58188 }

CVE-2026-58188 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58188) [\[CVE json\]](./CVE-2026-58188.cve.json) [\[OSV json\]](./CVE-2026-58188.osv.json)



_Last updated: 2026-07-29T09:04:20.085Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Several Apache Traffic Server experimental plugins have memory-safety and limit-bypass errors.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Yon Harlicaj (reporter)
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## Multiplexer plugin chunk decoder enables a denial of service ## { #CVE-2026-58187 }

CVE-2026-58187 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58187) [\[CVE json\]](./CVE-2026-58187.cve.json) [\[OSV json\]](./CVE-2026-58187.osv.json)



_Last updated: 2026-07-29T09:03:17.157Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server multiplexer plugin overruns its chunk-decode buffer on upstream input, enabling denial of service.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## webp_transform plugin decodes unsafely and mislabels degraded responses ## { #CVE-2026-58186 }

CVE-2026-58186 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58186) [\[CVE json\]](./CVE-2026-58186.cve.json) [\[OSV json\]](./CVE-2026-58186.osv.json)



_Last updated: 2026-07-29T09:01:35.556Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server webp_transform plugin can decode unsafely and serve mislabeled, cacheable responses.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## Use-after-free in the intercept plugin ## { #CVE-2026-58185 }

CVE-2026-58185 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58185) [\[CVE json\]](./CVE-2026-58185.cve.json) [\[OSV json\]](./CVE-2026-58185.osv.json)



_Last updated: 2026-07-29T08:57:42.562Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server intercept plugin has a use-after-free.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## header_rewrite plugin cookie handling can corrupt memory ## { #CVE-2026-58184 }

CVE-2026-58184 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58184) [\[CVE json\]](./CVE-2026-58184.cve.json) [\[OSV json\]](./CVE-2026-58184.osv.json)



_Last updated: 2026-07-29T08:56:45.008Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server header_rewrite plugin can crash or corrupt memory during cookie operations and CIDR condition matching.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## prefetch plugin can crash on attacker-influenced input ## { #CVE-2026-58183 }

CVE-2026-58183 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58183) [\[CVE json\]](./CVE-2026-58183.cve.json) [\[OSV json\]](./CVE-2026-58183.osv.json)



_Last updated: 2026-07-29T08:55:45.403Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server prefetch plugin can crash when processing attacker-influenced input.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## ts_lua plugin has initialization and resource-handling errors ## { #CVE-2026-58182 }

CVE-2026-58182 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58182) [\[CVE json\]](./CVE-2026-58182.cve.json) [\[OSV json\]](./CVE-2026-58182.osv.json)



_Last updated: 2026-07-29T08:54:41.470Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server ts_lua plugin mishandles initialization, transform context, and per-instance state.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## uri_signing and url_sig plugins can exhaust the stack or crash ## { #CVE-2026-58181 }

CVE-2026-58181 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58181) [\[CVE json\]](./CVE-2026-58181.cve.json) [\[OSV json\]](./CVE-2026-58181.osv.json)



_Last updated: 2026-07-29T08:46:00.299Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server uri_signing and url_sig plugins can exhaust the stack or crash on attacker input.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## txn_box plugin overflows the stack from attacker input ## { #CVE-2026-58180 }

CVE-2026-58180 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58180) [\[CVE json\]](./CVE-2026-58180.cve.json) [\[OSV json\]](./CVE-2026-58180.osv.json)



_Last updated: 2026-07-29T08:45:10.821Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server txn_box plugin overflows the stack from attacker-controlled input.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)


## regex_remap plugin overflows the stack from attacker input ## { #CVE-2026-58179 }

CVE-2026-58179 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58179) [\[CVE json\]](./CVE-2026-58179.cve.json) [\[OSV json\]](./CVE-2026-58179.osv.json)



_Last updated: 2026-07-29T08:44:28.901Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server regex_remap plugin overflows the stack and integers from substitution input.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)


## ESI plugin allows uncontrolled recursion and server-side request forgery ## { #CVE-2026-58178 }

CVE-2026-58178 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58178) [\[CVE json\]](./CVE-2026-58178.cve.json) [\[OSV json\]](./CVE-2026-58178.osv.json)



_Last updated: 2026-07-29T08:43:21.506Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server ESI plugin can recurse without bound and fetch attacker-controlled URLs.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)


## Memory-safety and path-traversal errors in the Cripts framework ## { #CVE-2026-58177 }

CVE-2026-58177 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58177) [\[CVE json\]](./CVE-2026-58177.cve.json) [\[OSV json\]](./CVE-2026-58177.osv.json)



_Last updated: 2026-07-29T08:42:36.014Z_

### Affected

* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server Cripts framework has out-of-bounds writes, path traversal, and use-after-free errors.</p><p>This issue affects Apache Traffic Server: from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## HostDB SRV handling leaks memory ## { #CVE-2026-58175 }

CVE-2026-58175 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58175) [\[CVE json\]](./CVE-2026-58175.cve.json) [\[OSV json\]](./CVE-2026-58175.osv.json)



_Last updated: 2026-07-29T08:41:45.146Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server leaks memory when handling HostDB SRV records.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## Remap configuration lifetime and TOCTOU errors cause use-after-free ## { #CVE-2026-58164 }

CVE-2026-58164 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58164) [\[CVE json\]](./CVE-2026-58164.cve.json) [\[OSV json\]](./CVE-2026-58164.osv.json)



_Last updated: 2026-07-29T08:37:38.531Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server has use-after-free and time-of-check/time-of-use errors in remap configuration handling.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## Cache deserialization and lifetime errors can corrupt state or crash the server ## { #CVE-2026-58163 }

CVE-2026-58163 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58163) [\[CVE json\]](./CVE-2026-58163.cve.json) [\[OSV json\]](./CVE-2026-58163.osv.json)



_Last updated: 2026-07-29T08:36:53.072Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server mishandles on-disk cache fields and object lifetimes, corrupting state or crashing.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## Certifier plugin trusts client SNI when generating certificates ## { #CVE-2026-58162 }

CVE-2026-58162 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58162) [\[CVE json\]](./CVE-2026-58162.cve.json) [\[OSV json\]](./CVE-2026-58162.osv.json)



_Last updated: 2026-07-29T08:36:12.596Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>The Apache Traffic Server certifier plugin generates certificates based on attacker-controlled client SNI.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## Memory-safety errors in TLS and SNI handling can crash the server ## { #CVE-2026-58161 }

CVE-2026-58161 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58161) [\[CVE json\]](./CVE-2026-58161.cve.json) [\[OSV json\]](./CVE-2026-58161.osv.json)



_Last updated: 2026-07-29T08:35:35.583Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server can crash from null dereferences and dangling references in TLS and SNI handling.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## Out-of-bounds reads while parsing DNS responses ## { #CVE-2026-58160 }

CVE-2026-58160 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58160) [\[CVE json\]](./CVE-2026-58160.cve.json) [\[OSV json\]](./CVE-2026-58160.osv.json)



_Last updated: 2026-07-29T08:34:31.111Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server reads out of bounds while parsing DNS answers.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## Listener and ACL handling allow access-control bypass ## { #CVE-2026-58159 }

CVE-2026-58159 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58159) [\[CVE json\]](./CVE-2026-58159.cve.json) [\[OSV json\]](./CVE-2026-58159.osv.json)



_Last updated: 2026-07-29T08:31:14.552Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server can bypass IP access controls on UDS listeners and through ACL matching errors.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## PROXY protocol parsing has port truncation and a stack overflow ## { #CVE-2026-58158 }

CVE-2026-58158 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58158) [\[CVE json\]](./CVE-2026-58158.cve.json) [\[OSV json\]](./CVE-2026-58158.osv.json)



_Last updated: 2026-07-29T08:26:27.296Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server mishandles PROXY protocol input, truncating ports and overflowing the stack.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)


## Improper server-session reuse can expose data across client connections ## { #CVE-2026-58157 }

CVE-2026-58157 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58157) [\[CVE json\]](./CVE-2026-58157.cve.json) [\[OSV json\]](./CVE-2026-58157.osv.json)



_Last updated: 2026-07-29T08:25:47.725Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server can reuse server sessions and tunnels improperly, exposing data across client connections.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## URL and port parsing errors allow access-control bypass ## { #CVE-2026-58156 }

CVE-2026-58156 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58156) [\[CVE json\]](./CVE-2026-58156.cve.json) [\[OSV json\]](./CVE-2026-58156.osv.json)



_Last updated: 2026-07-29T08:25:07.986Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server mis-parses ports in URLs and userinfo, allowing port-based access-control bypass.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## Header-name length truncation enables header aliasing and request smuggling ## { #CVE-2026-58155 }

CVE-2026-58155 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58155) [\[CVE json\]](./CVE-2026-58155.cve.json) [\[OSV json\]](./CVE-2026-58155.osv.json)



_Last updated: 2026-07-29T08:24:30.308Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server truncates over-long header names, allowing header aliasing, request smuggling, and policy bypass.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)


## Memory-safety errors in MIME and header parsing ## { #CVE-2026-58154 }

CVE-2026-58154 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58154) [\[CVE json\]](./CVE-2026-58154.cve.json) [\[OSV json\]](./CVE-2026-58154.osv.json)



_Last updated: 2026-07-29T08:23:57.475Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server can write out of bounds or overflow integers while parsing MIME and HTTP headers.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Michael Bommarito (reporter)
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## HTTP/2 to HTTP/1 conversion forwards origin trailers to clients unsafely ## { #CVE-2026-58153 }

CVE-2026-58153 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58153) [\[CVE json\]](./CVE-2026-58153.cve.json) [\[OSV json\]](./CVE-2026-58153.osv.json)



_Last updated: 2026-07-29T08:17:07.259Z_

### Affected

* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server forwards HTTP/2 origin trailers to HTTP/1 clients without proper chunked framing when converting HTTP/2 to HTTP/1.</p><p>This issue affects Apache Traffic Server: from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## Integer-handling errors in HPACK/XPACK decoding corrupt memory ## { #CVE-2026-58152 }

CVE-2026-58152 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58152) [\[CVE json\]](./CVE-2026-58152.cve.json) [\[OSV json\]](./CVE-2026-58152.osv.json)



_Last updated: 2026-07-29T08:16:17.147Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server mishandles integers while decoding HPACK/XPACK headers, corrupting memory.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Javid Khan (reporter)


## Abusive HTTP/2 framing can exhaust resources and crash the server ## { #CVE-2026-58151 }

CVE-2026-58151 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58151) [\[CVE json\]](./CVE-2026-58151.cve.json) [\[OSV json\]](./CVE-2026-58151.osv.json)



_Last updated: 2026-07-29T08:15:41.513Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server can be crashed or driven to resource exhaustion by abusive HTTP/2 framing and flow-control.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)
* Omkhar Arasaratnam (reporter)


## HTTP/2 requests with Transfer-Encoding are not rejected, allowing request smuggling ## { #CVE-2026-58150 }

CVE-2026-58150 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58150) [\[CVE json\]](./CVE-2026-58150.cve.json) [\[OSV json\]](./CVE-2026-58150.osv.json)



_Last updated: 2026-07-29T07:30:24.423Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server does not reject Transfer-Encoding in HTTP/2 requests, allowing downgrade request smuggling.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Apache Community (reporter)


## Malformed chunked message body allows request smuggling ## { #CVE-2026-57834 }

CVE-2026-57834 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-57834) [\[CVE json\]](./CVE-2026-57834.cve.json) [\[OSV json\]](./CVE-2026-57834.osv.json)



_Last updated: 2026-07-29T07:25:43.006Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server allows request smuggling if chunked messages are malformed.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Haruki Oyama (reporter)
* Katsutoshi Ikenoya (LY Corporation) (reporter)
* Apache Community (reporter)


## SNI to Host header matching policy is not properly enforced ## { #CVE-2026-41920 }

CVE-2026-41920 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41920) [\[CVE json\]](./CVE-2026-41920.cve.json) [\[OSV json\]](./CVE-2026-41920.osv.json)



_Last updated: 2026-07-29T07:17:57.749Z_

### Affected

* Apache Traffic Server from 9.0.0 through 9.1.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Improper Access Control vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 9.0.0 through 9.1.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.1.15 or 10.1.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* JD Marsters (Bhut Red) (reporter)
* Apache Community (reporter)


## Buffer overflow via Host field that has a long string value ## { #CVE-2026-33930 }

CVE-2026-33930 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33930) [\[CVE json\]](./CVE-2026-33930.cve.json) [\[OSV json\]](./CVE-2026-33930.osv.json)



_Last updated: 2026-07-29T07:23:50.719Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.14
* Apache Traffic Server from 10.0.0 through 10.1.3


### Description

<p>Apache Traffic Server copies the client Host header into a fixed-size stack buffer without a bound during redirect handling, so an over-long Host header overflows the stack when redirect following is enabled.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.14, from 10.0.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fix the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Pengpeng Hou (reporter)


## Untrusted @ headers can spoof ATS internal metadata ## { #CVE-2026-33267 }

CVE-2026-33267 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-33267) [\[CVE json\]](./CVE-2026-33267.cve.json) [\[OSV json\]](./CVE-2026-33267.osv.json)



_Last updated: 2026-07-29T07:21:47.559Z_

### Affected

* Apache Traffic Server from 9.2.0 through 9.2.14
* Apache Traffic Server from 10.1.0 through 10.1.3


### Description

<p>Improper Input Validation vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 9.2.0 through 9.2.14, from 10.1.0 through 10.1.3.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Charlie Campbell (reporter)
* Apache Community (reporter)


## Request smuggling via chunked extension quoted-string parsing ## { #CVE-2026-24033 }

CVE-2026-24033 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24033) [\[CVE json\]](./CVE-2026-24033.cve.json) [\[OSV json\]](./CVE-2026-24033.osv.json)



_Last updated: 2026-07-29T07:22:37.470Z_

### Affected

* Apache Traffic Server from 10.0.0 through 10.1.3
* Apache Traffic Server from 9.0.0 through 9.2.14


### Description

<p>Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling') vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 10.0.0 through 10.1.3, from 9.0.0 through 9.2.14.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Rajat Raghav (reporter)
* Katsutoshi Ikenoya (LY Corporation) (reporter)


## Regex mappings match with malicious domain names ## { #CVE-2026-22068 }

CVE-2026-22068 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-22068) [\[CVE json\]](./CVE-2026-22068.cve.json) [\[OSV json\]](./CVE-2026-22068.osv.json)



_Last updated: 2026-07-29T07:18:58.921Z_

### Affected

* Apache Traffic Server from 10.0.x through 10.1.3
* Apache Traffic Server from 9.0.x through 9.2.14


### Description

<p>Regular Expression without Anchors vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 10.0.X through 10.1.3, from 9.0.X through 9.2.14.</p><p>Users are recommended to upgrade to version 9.2.15 or 10.1.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/5prl9glcm9g2swnq9hqxvnokylm1gr6d


### Credits
* Omkhar Arasaratnam (reporter)
* Apache Community (reporter)


## Malformed chunked message body allows request smuggling ## { #CVE-2025-65114 }

CVE-2025-65114 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-65114) [\[CVE json\]](./CVE-2025-65114.cve.json) [\[OSV json\]](./CVE-2025-65114.osv.json)



_Last updated: 2026-04-10T15:56:14.648Z_

### Affected

* Apache Traffic Server from 9.0.0 through 9.2.12
* Apache Traffic Server from 10.0.0 through 10.1.1


### Description

<p><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">Apache Traffic Server allows request smuggling if c</span>hunked messages are malformed.</span>&nbsp;</p><p>This issue affects Apache Traffic Server: from 9.0.0 through 9.2.12, from 10.0.0 through 10.1.1.</p><p>Users are recommended to upgrade to version 9.2.13 or 10.1.2, which fix the issue.</p>

### References
* https://lists.apache.org/thread/2s11roxlv1j8ph6q52rqo1klvl01n14q


### Credits
* Katsutoshi Ikenoya (reporter)


## A simple legitimate POST request causes a crash ## { #CVE-2025-58136 }

CVE-2025-58136 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-58136) [\[CVE json\]](./CVE-2025-58136.cve.json) [\[OSV json\]](./CVE-2025-58136.osv.json)



_Last updated: 2026-04-10T15:53:47.491Z_

### Affected

* Apache Traffic Server from 10.0.0 through 10.1.1
* Apache Traffic Server from 9.0.0 through 9.2.12


### Description

<p>A bug in POST request handling causes a crash under a certain condition.</p><p>This issue affects Apache Traffic Server: from 10.0.0 through 10.1.1, from 9.0.0 through 9.2.12.</p><p>Users are recommended to upgrade to version 10.1.2 or 9.2.13, which fix the issue.</p>A workaround for older versions is to set&nbsp;<span style="background-color: rgb(255, 255, 255);">proxy.config.http.request_buffer_enabled to 0 (the default value is 0).&nbsp;</span><br>

### References
* https://lists.apache.org/thread/2s11roxlv1j8ph6q52rqo1klvl01n14q


## Remote DoS via memory exhaustion in ESI Plugin ## { #CVE-2025-49763 }

CVE-2025-49763 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-49763) [\[CVE json\]](./CVE-2025-49763.cve.json) [\[OSV json\]](./CVE-2025-49763.osv.json)



_Last updated: 2025-06-19T10:07:13.563Z_

### Affected

* Apache Traffic Server from 10.0.0 through 10.0.5
* Apache Traffic Server from 9.0.0 through 9.2.10


### Description

<p>ESI plugin does not have the limit for maximum inclusion depth, and that allows excessive memory consumption if malicious instructions are inserted.</p>Users can use a new setting for the plugin (--max-inclusion-depth) to limit it.<br><p>This issue affects Apache Traffic Server: from 10.0.0 through 10.0.5, from 9.0.0 through 9.2.10.</p><p>Users are recommended to upgrade to version 9.2.11 or 10.0.6,  which fixes the issue.</p>

### References
* https://lists.apache.org/thread/15t32nxbypqg1m2smp640vjx89o6v5f8


### Credits
* Yohann Sillam (reporter)


## Client IP address from PROXY protocol is not used for ACL ## { #CVE-2025-31698 }

CVE-2025-31698 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-31698) [\[CVE json\]](./CVE-2025-31698.cve.json) [\[OSV json\]](./CVE-2025-31698.osv.json)



_Last updated: 2025-06-19T10:07:45.344Z_

### Affected

* Apache Traffic Server from 10.0.0 through 10.0.6
* Apache Traffic Server from 9.0.0 through 9.2.10


### Description

<p>ACL configured in ip_allow.config or remap.config does not use IP addresses that are provided by PROXY protocol.</p>Users can use a new setting (proxy.config.acl.subjects) to choose which IP addresses to use for the ACL if Apache Traffic Server is configured to accept PROXY protocol.&nbsp;<br><p>This issue affects undefined: from 10.0.0 through 10.0.6, from 9.0.0 through 9.2.10.</p><p>Users are recommended to upgrade to version 9.2.11 or 10.0.6, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/15t32nxbypqg1m2smp640vjx89o6v5f8


## Expect header field can unreasonably retain resource ## { #CVE-2024-56202 }

CVE-2024-56202 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-56202) [\[CVE json\]](./CVE-2024-56202.cve.json) [\[OSV json\]](./CVE-2024-56202.osv.json)



_Last updated: 2025-03-06T11:09:09.771Z_

### Affected

* Apache Traffic Server from 9.0.0 through 9.2.8
* Apache Traffic Server from 10.0.0 through 10.0.3


### Description

<p>Expected Behavior Violation vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 9.0.0 through 9.2.8, from 10.0.0 through 10.0.3.</p><p>Users are recommended to upgrade to versions 9.2.9 or 10.0.4 or newer, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/btofzws2yqskk2n7f01r3l1819x01023


### Credits
* David Carlin (reporter)


## ACL is not fully compatible with older versions ## { #CVE-2024-56196 }

CVE-2024-56196 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-56196) [\[CVE json\]](./CVE-2024-56196.cve.json) [\[OSV json\]](./CVE-2024-56196.osv.json)



_Last updated: 2025-03-06T11:21:46.767Z_

### Affected

* Apache Traffic Server from 10.0.0 through 10.0.3


### Description

<p>Improper Access Control vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 10.0.0 through 10.0.3.</p><p>Users are recommended to upgrade to version 10.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/btofzws2yqskk2n7f01r3l1819x01023


### Credits
* Chris McFarlen (reporter)


## Intercept plugins are not access controlled ## { #CVE-2024-56195 }

CVE-2024-56195 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-56195) [\[CVE json\]](./CVE-2024-56195.cve.json) [\[OSV json\]](./CVE-2024-56195.osv.json)



_Last updated: 2025-03-06T11:23:34.892Z_

### Affected

* Apache Traffic Server from 9.2.0 through 9.2.8
* Apache Traffic Server from 10.0.0 through 10.0.3


### Description

<p>Improper Access Control vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 9.2.0 through 9.2.8, from 10.0.0 through 10.0.3.</p><p>Users are recommended to upgrade to version 9.2.9 or 10.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/btofzws2yqskk2n7f01r3l1819x01023


### Credits
* Masaori Koshiba (reporter)


## Malformed chunked message body allows request smuggling ## { #CVE-2024-53868 }

CVE-2024-53868 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-53868) [\[CVE json\]](./CVE-2024-53868.cve.json) [\[OSV json\]](./CVE-2024-53868.osv.json)



_Last updated: 2025-04-03T08:58:55.409Z_

### Affected

* Apache Traffic Server from 9.2.0 through 9.2.9
* Apache Traffic Server from 10.0.0 through 10.0.4


### Description

<p></p><p><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">Apache Traffic Server allows request smuggling if c</span>hunked messages are malformed.</span>&nbsp;</p><p></p><p></p><p>This issue affects Apache Traffic Server: from 9.2.0 through 9.2.9, from 10.0.0 through 10.0.4.</p><p>Users are recommended to upgrade to version 9.2.10 or 10.0.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/rwyx91rsrnmpjbm04footfjjf6m9d1c9


### Credits
* Jeppe Bonde Weikop (reporter)


## Server process can fail to drop privilege ## { #CVE-2024-50306 }

CVE-2024-50306 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-50306) [\[CVE json\]](./CVE-2024-50306.cve.json) [\[OSV json\]](./CVE-2024-50306.osv.json)



_Last updated: 2024-11-14T09:55:41.120Z_

### Affected

* Apache Traffic Server from 9.2.0 through 9.2.5
* Apache Traffic Server from 10.0.0 through 10.0.1


### Description

<p>Unchecked return value can allow Apache Traffic Server to retain privileges on startup.</p><p>This issue affects Apache Traffic Server: from 9.2.0 through 9.2.5, from 10.0.0 through 10.0.1.</p><p>Users are recommended to upgrade to version 9.2.6 or 10.0.2, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/y15fh6c7kyqvzm0f9odw7c5jh4r4np0y


### Credits
* Jeffrey BENCTEUX (reporter)


## Valid Host field value can cause crashes ## { #CVE-2024-50305 }

CVE-2024-50305 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-50305) [\[CVE json\]](./CVE-2024-50305.cve.json) [\[OSV json\]](./CVE-2024-50305.osv.json)



_Last updated: 2024-11-14T09:54:18.691Z_

### Affected

* Apache Traffic Server from 9.2.0 through 9.2.5


### Description

<p>Valid Host header field can cause Apache Traffic Server to crash on some platforms.</p><p>This issue affects Apache Traffic Server: from 9.2.0 through 9.2.5.</p><p>Users are recommended to upgrade to version 9.2.6, which fixes the issue, or 10.0.2, which does not have the issue.</p>

### References
* https://lists.apache.org/thread/y15fh6c7kyqvzm0f9odw7c5jh4r4np0y


## Cache key plugin is vulnerable to cache poisoning attack ## { #CVE-2024-38479 }

CVE-2024-38479 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-38479) [\[CVE json\]](./CVE-2024-38479.cve.json) [\[OSV json\]](./CVE-2024-38479.osv.json)



_Last updated: 2024-12-19T08:48:33.164Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.11
* Apache Traffic Server from 9.0.0 through 9.2.5


### Description

<p>Improper Input Validation vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.11, from 9.0.0 through 9.2.5.</p><p>Users are recommended to upgrade to version 9.2.6, which fixes the issue, or 10.0.2, which does not have the issue.</p>

### References
* https://lists.apache.org/thread/y15fh6c7kyqvzm0f9odw7c5jh4r4np0y


## Request smuggling via pipelining after a chunked message body ## { #CVE-2024-38311 }

CVE-2024-38311 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-38311) [\[CVE json\]](./CVE-2024-38311.cve.json) [\[OSV json\]](./CVE-2024-38311.osv.json)



_Last updated: 2025-03-06T11:34:14.593Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.11
* Apache Traffic Server from 9.0.0 through 9.2.8
* Apache Traffic Server from 10.0.0 through 10.0.3


### Description

<p>Improper Input Validation vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.11, from 9.0.0 through 9.2.8, from 10.0.0 through 10.0.3.</p><p>Users are recommended to upgrade to version 9.2.9 or 10.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/btofzws2yqskk2n7f01r3l1819x01023


### Credits
* Ben Kallus (reporter)


## Invalid Accept-Encoding can force forwarding requests ## { #CVE-2024-35296 }

CVE-2024-35296 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-35296) [\[CVE json\]](./CVE-2024-35296.cve.json) [\[OSV json\]](./CVE-2024-35296.osv.json)



_Last updated: 2024-07-26T09:11:09.740Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.10
* Apache Traffic Server from 9.0.0 through 9.2.4


### Description

<p>Invalid Accept-Encoding header can cause Apache Traffic Server to fail cache lookup and force forwarding requests.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.10, from 9.0.0 through 9.2.4.</p><p>Users are recommended to upgrade to version 8.1.11 or 9.2.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/c4mcmpblgl8kkmyt56t23543gp8v56m0


### Credits
* Min Chen (reporter)


## Incomplete check for chunked trailer section allows request smuggling ## { #CVE-2024-35161 }

CVE-2024-35161 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-35161) [\[CVE json\]](./CVE-2024-35161.cve.json) [\[OSV json\]](./CVE-2024-35161.osv.json)



_Last updated: 2024-08-13T08:48:31.440Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.10
* Apache Traffic Server from 9.0.0 through 9.2.4


### Description

<p>Apache Traffic Server forwards malformed HTTP chunked trailer section to origin servers. This can be utilized for request smuggling and may also lead cache poisoning if the origin servers are vulnerable.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.10, from 9.0.0 through 9.2.4.</p>Users can set a new setting (proxy.config.http.drop_chunked_trailers) not to forward chunked trailer section.<br><p>Users are recommended to upgrade to version 8.1.11 or 9.2.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/c4mcmpblgl8kkmyt56t23543gp8v56m0


### Credits
* Keran Mu (reporter)


## HTTP/2 CONTINUATION frames can be utilized for DoS attack ## { #CVE-2024-31309 }

CVE-2024-31309 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-31309) [\[CVE json\]](./CVE-2024-31309.cve.json) [\[OSV json\]](./CVE-2024-31309.osv.json)



_Last updated: 2024-04-10T15:16:21.844Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.9
* Apache Traffic Server from 9.0.0 through 9.2.3


### Description

<p>HTTP/2 <span style="background-color: rgb(255, 255, 255);">CONTINUATION</span>&nbsp;DoS attack can cause Apache Traffic Server to consume more resources on the server.&nbsp; Version from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.3 are&nbsp;affected.</p>Users can set a new setting (proxy.config.http2.max_continuation_frames_per_minute) to limit the number of CONTINUATION frames per minute. &nbsp;ATS does have a fixed amount of memory a request can use and ATS adheres to these limits in previous releases.<br><p>Users are recommended to upgrade to versions 8.1.10 or 9.2.4 which fixes the issue.</p>

### References
* https://lists.apache.org/thread/f9qh3g3jvy153wh82pz4onrfj1wh13kc


### Credits
* Bartek Nowotarski (reporter)


## s3_auth plugin problem with hash calculation ## { #CVE-2023-41752 }

CVE-2023-41752 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-41752) [\[CVE json\]](./CVE-2023-41752.cve.json) [\[OSV json\]](./CVE-2023-41752.osv.json)



_Last updated: 2023-10-17T06:57:44.046Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.8
* Apache Traffic Server from 9.0.0 through 9.2.2


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Traffic Server.<p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.8, from 9.0.0 through 9.2.2.</p><p>Users are recommended to upgrade to version 8.1.9 or 9.2.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/5py8h42mxfsn8l1wy6o41xwhsjlsd87q


### Credits
* Masakazu Kitajo (finder)


## Malformed http/2 frames can cause an abort ## { #CVE-2023-39456 }

CVE-2023-39456 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-39456) [\[CVE json\]](./CVE-2023-39456.cve.json) [\[OSV json\]](./CVE-2023-39456.osv.json)



_Last updated: 2023-10-17T06:58:15.367Z_

### Affected

* Apache Traffic Server from 9.0.0 through 9.2.2


### Description

Improper Input Validation vulnerability in Apache Traffic Server with malformed HTTP/2 frames.<p>This issue affects Apache Traffic Server: from 9.0.0 through 9.2.2.</p><p>Users are recommended to upgrade to version 9.2.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/5py8h42mxfsn8l1wy6o41xwhsjlsd87q


### Credits
*  Akshat Parikh (finder)


## Incomplete field name check allows request smuggling ## { #CVE-2023-38522 }

CVE-2023-38522 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-38522) [\[CVE json\]](./CVE-2023-38522.cve.json) [\[OSV json\]](./CVE-2023-38522.osv.json)



_Last updated: 2024-08-13T08:46:41.192Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.10
* Apache Traffic Server from 9.0.0 through 9.2.4


### Description

<p>Apache Traffic Server accepts characters that are not allowed for HTTP field names and forwards malformed requests to origin servers. This can be utilized for request smuggling and may also lead cache poisoning if the origin servers are vulnerable.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.10, from 9.0.0 through 9.2.4.</p><p>Users are recommended to upgrade to version 8.1.11 or 9.2.5, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/c4mcmpblgl8kkmyt56t23543gp8v56m0


### Credits
* Ben Kallus (finder)


## Differential fuzzing for HTTP request parsing discrepancies ## { #CVE-2023-33934 }

CVE-2023-33934 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-33934) [\[CVE json\]](./CVE-2023-33934.cve.json) [\[OSV json\]](./CVE-2023-33934.osv.json)



_Last updated: 2023-09-28T08:24:06.964Z_

### Affected

* Apache Traffic Server through 9.2.1


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Traffic Server.<p>This issue affects Apache Traffic Server: through 9.2.1.</p>

### References
* https://lists.apache.org/thread/jsl6dfdgs1mjjo1mbtyflyjr7xftswhc
* https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/BOTOM2MFKOLK46Q3BQHO662HTPZFRQUC/


### Credits
* Bahruz Jabiyev, Anthony Gavazzi, Engin Kirda, Kaan Onarlioglu, Adi Peleg, Harvey Tuch (finder)


## s3_auth plugin problem with hash calculation ## { #CVE-2023-33933 }

CVE-2023-33933 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-33933) [\[CVE json\]](./CVE-2023-33933.cve.json) [\[OSV json\]](./CVE-2023-33933.osv.json)



_Last updated: 2023-08-31T19:49:23.749Z_

### Affected

* Apache Traffic Server from 8.0.0 through 9.2.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Traffic Server.<p>This issue affects Apache Traffic Server: from 8.0.0 through 9.2.0.</p><p>8.x users should upgrade to 8.1.7 or later versions<br>9.x users should upgrade to 9.2.1 or later versions<br></p>

### References
* https://lists.apache.org/thread/tns2b4khyyncgs5v5p9y35pobg9z2bvs


### Credits
* Masakazu Kitajo (reporter)


## Configuration option to block the PUSH method in ATS didn't work ## { #CVE-2023-30631 }

CVE-2023-30631 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-30631) [\[CVE json\]](./CVE-2023-30631.cve.json) [\[OSV json\]](./CVE-2023-30631.osv.json)



_Last updated: 2023-06-14T07:44:52.725Z_

### Affected

* Apache Traffic Server from 8.0.0 through 9.2.0


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Traffic Server.&nbsp; The configuration option&nbsp;proxy.config.http.push_method_enabled didn't function.&nbsp; However, by default the PUSH method is blocked in the ip_allow configuration file.<p>This issue affects Apache Traffic Server: from 8.0.0 through 9.2.0.</p><p>8.x users should upgrade to 8.1.7 or later versions<br>9.x users should upgrade to 9.2.1 or later versions<br></p>

### References
* https://lists.apache.org/thread/tns2b4khyyncgs5v5p9y35pobg9z2bvs


### Credits
* Chris Lemmons (finder)


## Invalid Range header causes a crash ## { #CVE-2022-47185 }

CVE-2022-47185 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-47185) [\[CVE json\]](./CVE-2022-47185.cve.json) [\[OSV json\]](./CVE-2022-47185.osv.json)



_Last updated: 2023-08-09T06:57:36.707Z_

### Affected

* Apache Traffic Server through 9.2.1


### Description

Improper input validation vulnerability on the range header in Apache Software Foundation Apache Traffic Server.<p>This issue affects Apache Traffic Server: through 9.2.1.</p>

### References
* https://lists.apache.org/thread/jsl6dfdgs1mjjo1mbtyflyjr7xftswhc


### Credits
* Katsutoshi Ikenoya (finder)


## The TRACE method can be use to disclose network information ## { #CVE-2022-47184 }

CVE-2022-47184 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-47184) [\[CVE json\]](./CVE-2022-47184.cve.json) [\[OSV json\]](./CVE-2022-47184.osv.json)



_Last updated: 2023-06-14T07:42:29.792Z_

### Affected

* Apache Traffic Server from 8.0.0 through 9.2.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Traffic Server.<p>This issue affects Apache Traffic Server: 8.0.0 to 9.2.0.</p>

### References
* https://lists.apache.org/thread/tns2b4khyyncgs5v5p9y35pobg9z2bvs


### Credits
* Martin O'Neal (reporter)


## Security issues with the xdebug plugin ## { #CVE-2022-40743 }

CVE-2022-40743 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-40743) [\[CVE json\]](./CVE-2022-40743.cve.json) [\[OSV json\]](./CVE-2022-40743.osv.json)



_Last updated: 2023-07-17T14:33:07.403Z_

### Affected

* Apache Traffic Server from 9.0.0 through 9.1.3


### Description

Improper Input Validation vulnerability for the xdebug plugin in Apache Software Foundation Apache Traffic Server can lead to cross site scripting and cache poisoning attacks.<p>This issue affects Apache Traffic Server: 9.0.0 to 9.1.3. Users should upgrade to 9.1.4 or later versions.<br></p>

### References
* https://lists.apache.org/thread/mrj2lg4s0hf027rk7gz8t7hbn9xpfg02


### Credits
* Nick Frost (finder)


## Improperly reading the client requests ## { #CVE-2022-37392 }

CVE-2022-37392 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-37392) [\[CVE json\]](./CVE-2022-37392.cve.json) [\[OSV json\]](./CVE-2022-37392.osv.json)



_Last updated: 2022-12-19T10:58:23.000Z_

### Affected

* Apache Traffic Server from 8.0.0 through 9.1.3


### Description

Improper Check for Unusual or Exceptional Conditions vulnerability in handling the requests to Apache Traffic Server.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/mrj2lg4s0hf027rk7gz8t7hbn9xpfg02


### Credits
* Menno de Gier (finder)


## Improperly handled requests can cause crashes in specific plugins ## { #CVE-2022-32749 }

CVE-2022-32749 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-32749) [\[CVE json\]](./CVE-2022-32749.cve.json) [\[OSV json\]](./CVE-2022-32749.osv.json)



_Last updated: 2022-12-19T10:51:20.718Z_

### Affected

* Apache Traffic Server from 8.0.0 through 9.1.3


### Description



Improper Check for Unusual or Exceptional Conditions vulnerability handling requests in Apache Traffic Server allows an attacker to crash the server under certain conditions.

<p>This issue affects Apache Traffic Server: from 8.0.0 through 9.1.3.</p>

### References
* https://lists.apache.org/thread/mrj2lg4s0hf027rk7gz8t7hbn9xpfg02


### Credits
* Vijay Mamidi (finder)


## HTTP/2 framing vulnerabilities  ## { #CVE-2022-31780 }

CVE-2022-31780 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-31780) [\[CVE json\]](./CVE-2022-31780.cve.json) [\[OSV json\]](./CVE-2022-31780.osv.json)



_Last updated: 2022-08-10T05:45:38.174Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.1.2


### Description

Improper Input Validation vulnerability in HTTP/2 frame handling of Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


### Credits
* Apache Traffic Server would like to thank Bahruz Jabiyev, Steven Sprecher, Anthony Gavazzi, Tommaso Innocenti, Kaan Onarlioglu, and Engin Kirda for reporting these issues.  


## Improper HTTP/2 scheme and method validation ## { #CVE-2022-31779 }

CVE-2022-31779 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-31779) [\[CVE json\]](./CVE-2022-31779.cve.json) [\[OSV json\]](./CVE-2022-31779.osv.json)



_Last updated: 2022-10-27T00:00:36.092Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.1.2


### Description

Improper Input Validation vulnerability in HTTP/2 header parsing of Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


### Credits
* Apache Traffic Server would like to thank Dhana Sekaran for reporting this issue.


## Transfer-Encoding not treated as hop-by-hop ## { #CVE-2022-31778 }

CVE-2022-31778 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-31778) [\[CVE json\]](./CVE-2022-31778.cve.json) [\[OSV json\]](./CVE-2022-31778.osv.json)



_Last updated: 2022-08-10T05:44:15.239Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.0.2


### Description

Improper Input Validation vulnerability in handling the Transfer-Encoding header of Apache Traffic Server allows an attacker to poison the cache.  This issue affects Apache Traffic Server 8.0.0 to 9.0.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


### Credits
* Apache Traffic Server would like to thank Chris Lemmons for reporting this issue.


##  Insufficient Validation of HTTP/1.x Headers ## { #CVE-2022-28129 }

CVE-2022-28129 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-28129) [\[CVE json\]](./CVE-2022-28129.cve.json) [\[OSV json\]](./CVE-2022-28129.osv.json)



_Last updated: 2022-08-10T05:42:44.803Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.1.2


### Description

Improper Input Validation vulnerability in HTTP/1.1 header parsing of Apache Traffic Server allows an attacker to send invalid headers.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


### Credits
* Apache Traffic Server would like to thank Zhang Zeyu for reporting this issue.


## Improper input validation on HTTP/2 headers  ## { #CVE-2022-25763 }

CVE-2022-25763 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-25763) [\[CVE json\]](./CVE-2022-25763.cve.json) [\[OSV json\]](./CVE-2022-25763.osv.json)



_Last updated: 2022-10-20T20:25:04.197Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.1.2


### Description

Improper Input Validation vulnerability in HTTP/2 request validation of Apache Traffic Server allows an attacker to create smuggle or cache poison attacks.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


### Credits
* Apache Traffic Server would like to thank Mazakatsu Kitajo, Dhana Sekaran, and Zhang Zeyu for reporting this issue.


## Improper authentication vulnerability in TLS origin verification ## { #CVE-2021-44759 }

CVE-2021-44759 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-44759) [\[CVE json\]](./CVE-2021-44759.cve.json) [\[OSV json\]](./CVE-2021-44759.osv.json)



_Last updated: 2022-03-23T14:03:27.211Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.1.0


### Description

Improper Authentication vulnerability in TLS origin validation of Apache Traffic Server allows an attacker to create a man in the middle attack.  This issue affects Apache Traffic Server 8.0.0 to 8.1.0.

### References
* https://lists.apache.org/thread/zblwzcfs9ryhwjr89wz4osw55pxm6dx6


### Credits
* Apache Traffic Server would like to thank Takuya Kitano for reporting this issue.


## HTTP request line fuzzing attacks ## { #CVE-2021-44040 }

CVE-2021-44040 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-44040) [\[CVE json\]](./CVE-2021-44040.cve.json) [\[OSV json\]](./CVE-2021-44040.osv.json)



_Last updated: 2022-03-23T14:04:02.939Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.1.3 and 9.0.0 to 9.1.1


### Description

Improper Input Validation vulnerability in request line parsing of Apache Traffic Server allows an attacker to send invalid requests.  This issue affects Apache Traffic Server 8.0.0 to 8.1.3 and 9.0.0 to 9.1.1.

### References
* https://lists.apache.org/thread/zblwzcfs9ryhwjr89wz4osw55pxm6dx6


### Credits
* Apache Traffic Server would like to thank Bahruz Jabiyev, Steven Sprecher and Kaan Onarlioglu for reporting these issues.  We used his tool t-reqs (https://github.com/bahruzjabiyev/t-reqs-http-fuzzer) for discovering them.


## heap-buffer-overflow with stats-over-http plugin ## { #CVE-2021-43082 }

CVE-2021-43082 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-43082) [\[CVE json\]](./CVE-2021-43082.cve.json) [\[OSV json\]](./CVE-2021-43082.osv.json)



_Last updated: 2021-11-02T21:16:59.675Z_

### Affected

* Apache Traffic Server at 9.1.0


### Description

Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') vulnerability in the stats-over-http plugin of Apache Traffic Server allows an attacker to overwrite memory.  This issue affects Apache Traffic Server 9.1.0.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


### Credits
* Apache Traffic Server would like to thank Masori Koshiba for finding this issue.


## ATS stops accepting connections on FreeBSD ## { #CVE-2021-41585 }

CVE-2021-41585 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-41585) [\[CVE json\]](./CVE-2021-41585.cve.json) [\[OSV json\]](./CVE-2021-41585.osv.json)



_Last updated: 2021-11-02T21:16:43.796Z_

### Affected

* Apache Traffic Server at 7.0.0 to 9.1.0


### Description

Improper Input Validation vulnerability in accepting socket connections in Apache Traffic Server allows an attacker to make the server stop accepting new connections.  This issue affects Apache Traffic Server 5.0.0 to 9.1.0.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


### Credits
* Apache Traffic Server would like to thank Asbjorn Bjornstad for finding this issue.


## Not validating origin TLS certificate ## { #CVE-2021-38161 }

CVE-2021-38161 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-38161) [\[CVE json\]](./CVE-2021-38161.cve.json) [\[OSV json\]](./CVE-2021-38161.osv.json)



_Last updated: 2021-11-02T21:16:04.785Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.0.8


### Description

Improper Authentication vulnerability in TLS origin verification of Apache Traffic Server allows for man in the middle attacks.  This issue affects Apache Traffic Server 8.0.0 to 8.0.8.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


## Protocol vs scheme mismatch ## { #CVE-2021-37150 }

CVE-2021-37150 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-37150) [\[CVE json\]](./CVE-2021-37150.cve.json) [\[OSV json\]](./CVE-2021-37150.osv.json)



_Last updated: 2022-08-10T05:43:13.024Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.1.2


### Description

Improper Input Validation vulnerability in header parsing of Apache Traffic Server allows an attacker to request secure resources.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


## Request Smuggling - multiple attacks ## { #CVE-2021-37149 }

CVE-2021-37149 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-37149) [\[CVE json\]](./CVE-2021-37149.cve.json) [\[OSV json\]](./CVE-2021-37149.osv.json)



_Last updated: 2021-11-02T21:15:10.588Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.1.2 and 9.0.0 to 9.1.0


### Description

Improper Input Validation vulnerability in header parsing of Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 8.0.0 to 8.1.2 and 9.0.0 to 9.1.0.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


### Credits
* Apache Traffic Server would like to thank Mattias Grenfeldt and Asta Olofsson for reporting this issue


## Request Smuggling - transfer encoding validation ## { #CVE-2021-37148 }

CVE-2021-37148 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-37148) [\[CVE json\]](./CVE-2021-37148.cve.json) [\[OSV json\]](./CVE-2021-37148.osv.json)



_Last updated: 2021-11-02T21:14:46.545Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.1.2 and 9.0.0 to 9.0.1


### Description

Improper input validation vulnerability in header parsing of Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 8.0.0 to 8.1.2 and 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


### Credits
* Apache Traffic Server would like to thank Mattias Grenfeldt and Asta Olofsson for reporting this issue


## Request Smuggling - LF line ending ## { #CVE-2021-37147 }

CVE-2021-37147 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-37147) [\[CVE json\]](./CVE-2021-37147.cve.json) [\[OSV json\]](./CVE-2021-37147.osv.json)



_Last updated: 2021-11-02T21:14:21.298Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.1.2 and 9.0.0 to 9.1.0


### Description

Improper input validation vulnerability in header parsing of Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 8.0.0 to 8.1.2 and 9.0.0 to 9.1.0.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


### Credits
* Apache Traffic Server would like to thank Mattias Grenfeldt and Asta Olofsson for reporting this issue.


## Dynamic stack buffer overflow in cachekey plugin ## { #CVE-2021-35474 }

CVE-2021-35474 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-35474) [\[CVE json\]](./CVE-2021-35474.cve.json) [\[OSV json\]](./CVE-2021-35474.osv.json)



_Last updated: 2021-06-30T07:12:52.360Z_

### Affected

* Apache Traffic Server at 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1


### Description

Stack-based Buffer Overflow vulnerability in cachekey plugin of Apache Traffic Server.  This issue affects Apache Traffic Server 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread.html/ra1a41ff92a70d25bf576d7da2590575e8ff430393a3f4a0c34de4277%40%3Cusers.trafficserver.apache.org%3E


## Reading HTTP/2 frames too many times ## { #CVE-2021-32567 }

CVE-2021-32567 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-32567) [\[CVE json\]](./CVE-2021-32567.cve.json) [\[OSV json\]](./CVE-2021-32567.osv.json)



_Last updated: 2021-06-30T07:12:25.231Z_

### Affected

* Apache Traffic Server at 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1


### Description

Improper Input Validation vulnerability in HTTP/2 of Apache Traffic Server allows an attacker to DOS the server.  This issue affects Apache Traffic Server 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread.html/ra1a41ff92a70d25bf576d7da2590575e8ff430393a3f4a0c34de4277%40%3Cusers.trafficserver.apache.org%3E


## Specific sequence of HTTP/2 frames can cause ATS to crash ## { #CVE-2021-32566 }

CVE-2021-32566 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-32566) [\[CVE json\]](./CVE-2021-32566.cve.json) [\[OSV json\]](./CVE-2021-32566.osv.json)



_Last updated: 2021-06-30T07:11:47.425Z_

### Affected

* Apache Traffic Server at 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1


### Description

Improper Input Validation vulnerability in HTTP/2 of Apache Traffic Server allows an attacker to DOS the server.  This issue affects Apache Traffic Server 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread.html/ra1a41ff92a70d25bf576d7da2590575e8ff430393a3f4a0c34de4277%40%3Cusers.trafficserver.apache.org%3E


## HTTP Request Smuggling, content length with invalid charters ## { #CVE-2021-32565 }

CVE-2021-32565 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-32565) [\[CVE json\]](./CVE-2021-32565.cve.json) [\[OSV json\]](./CVE-2021-32565.osv.json)



_Last updated: 2021-06-28T17:31:31.239Z_

### Affected

* Apache Traffic Server at 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1


### Description

Invalid values in the Content-Length header sent to Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread.html/ra1a41ff92a70d25bf576d7da2590575e8ff430393a3f4a0c34de4277%40%3Cusers.trafficserver.apache.org%3E


## slicer plugin crash ## { #CVE-2021-27737 }

CVE-2021-27737 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-27737) [\[CVE json\]](./CVE-2021-27737.cve.json)

_Last updated: 2021-05-17T17:41:59.734Z_

### Affected

* Apache Traffic Server at 9.0.0


### Description

Apache Traffic Server 9.0.0 is vulnerable to a remote DOS attack on the experimental Slicer plugin.

## Incorrect handling of url fragment leads to cache poisoning ## { #CVE-2021-27577 }

CVE-2021-27577 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-27577) [\[CVE json\]](./CVE-2021-27577.cve.json) [\[OSV json\]](./CVE-2021-27577.osv.json)



_Last updated: 2021-06-28T17:28:40.345Z_

### Affected

* Apache Traffic Server at 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1


### Description

Incorrect handling of url fragment vulnerability of Apache Traffic Server allows an attacker to poison the cache.  This issue affects Apache Traffic Server 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread.html/ra1a41ff92a70d25bf576d7da2590575e8ff430393a3f4a0c34de4277%40%3Cusers.trafficserver.apache.org%3E


## Apache Traffic Server negative cache option is vulnerable to a cache poisoning attack ## { #CVE-2020-17509 }

CVE-2020-17509 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17509) [\[CVE json\]](./CVE-2020-17509.cve.json) [\[OSV json\]](./CVE-2020-17509.osv.json)



_Last updated: 2021-01-11T09:31:44.280Z_

### Affected

* Apache Traffic Server from Apache Traffic Server through 6.2.3


### Description

Apache Traffic Server negative cache option is vulnerable to a cache poisoning attack affecting versions 6.0.0 through 6.2.3, 7.0.0 through 7.1.10, and 8.0.0 through 8.0.7.  If you have this option enabled, please upgrade or disable this feature.


### References
* https://lists.apache.org/thread.html/raa9f0589c26c4d146646425e51e2a33e1457492df9f7ea2019daa6d3%40%3Cdev.trafficserver.apache.org%3E


## Apache Traffic Server ESI plugin has a memory disclosure vulnerability ## { #CVE-2020-17508 }

CVE-2020-17508 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-17508) [\[CVE json\]](./CVE-2020-17508.cve.json) [\[OSV json\]](./CVE-2020-17508.osv.json)



_Last updated: 2021-01-11T09:27:29.639Z_

### Affected

* Apache Traffic Server from Apache Traffic Server through 6.2.3


### Description

The ESI plugin in Apache Traffic Server 6.0.0 to 6.2.3, 7.0.0 to 7.1.11, and 8.0.0 to 8.1.0 has a memory disclosure vulnerability.  If you are running the plugin please upgrade to 7.1.12 or 8.1.1 or later.


### References
* https://lists.apache.org/thread.html/r65434f7acca3aebf81b0588587149c893fe9f8f9f159eaa7364a70ff%40%3Cdev.trafficserver.apache.org%3E
