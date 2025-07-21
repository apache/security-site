---
title: Apache Traffic Server security advisories
description: Security information for Apache Traffic Server
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Traffic Server? You can read more about the projects' security policy on their [security page](https://github.com/apache/trafficserver/security/policy), and email your report to the [Apache Traffic Server Security Team](mailto:security@trafficserver.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://github.com/apache/trafficserver/security/policy). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Traffic Server ESI plugin has a memory disclosure vulnerability ## { #CVE-2020-17508 }

CVE-2020-17508 [\[CVE json\]](./CVE-2020-17508.cve.json) [\[OSV json\]](./CVE-2020-17508.osv.json)



_Last updated: 2021-01-11T09:27:29.639Z_

### Affected

* Apache Traffic Server from Apache Traffic Server through 6.2.3


### Description

The ESI plugin in Apache Traffic Server 6.0.0 to 6.2.3, 7.0.0 to 7.1.11, and 8.0.0 to 8.1.0 has a memory disclosure vulnerability.  If you are running the plugin please upgrade to 7.1.12 or 8.1.1 or later.


### References
* https://lists.apache.org/thread.html/r65434f7acca3aebf81b0588587149c893fe9f8f9f159eaa7364a70ff%40%3Cdev.trafficserver.apache.org%3E


## Apache Traffic Server negative cache option is vulnerable to a cache poisoning attack ## { #CVE-2020-17509 }

CVE-2020-17509 [\[CVE json\]](./CVE-2020-17509.cve.json) [\[OSV json\]](./CVE-2020-17509.osv.json)



_Last updated: 2021-01-11T09:31:44.280Z_

### Affected

* Apache Traffic Server from Apache Traffic Server through 6.2.3


### Description

Apache Traffic Server negative cache option is vulnerable to a cache poisoning attack affecting versions 6.0.0 through 6.2.3, 7.0.0 through 7.1.10, and 8.0.0 through 8.0.7.  If you have this option enabled, please upgrade or disable this feature.


### References
* https://lists.apache.org/thread.html/raa9f0589c26c4d146646425e51e2a33e1457492df9f7ea2019daa6d3%40%3Cdev.trafficserver.apache.org%3E


## Incorrect handling of url fragment leads to cache poisoning ## { #CVE-2021-27577 }

CVE-2021-27577 [\[CVE json\]](./CVE-2021-27577.cve.json) [\[OSV json\]](./CVE-2021-27577.osv.json)



_Last updated: 2021-06-28T17:28:40.345Z_

### Affected

* Apache Traffic Server at 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1


### Description

Incorrect handling of url fragment vulnerability of Apache Traffic Server allows an attacker to poison the cache.  This issue affects Apache Traffic Server 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread.html/ra1a41ff92a70d25bf576d7da2590575e8ff430393a3f4a0c34de4277%40%3Cusers.trafficserver.apache.org%3E


## slicer plugin crash ## { #CVE-2021-27737 }

CVE-2021-27737 [\[CVE json\]](./CVE-2021-27737.cve.json)

_Last updated: 2021-05-17T17:41:59.734Z_

### Affected

* Apache Traffic Server at 9.0.0


### Description

Apache Traffic Server 9.0.0 is vulnerable to a remote DOS attack on the experimental Slicer plugin.

## HTTP Request Smuggling, content length with invalid charters ## { #CVE-2021-32565 }

CVE-2021-32565 [\[CVE json\]](./CVE-2021-32565.cve.json) [\[OSV json\]](./CVE-2021-32565.osv.json)



_Last updated: 2021-06-28T17:31:31.239Z_

### Affected

* Apache Traffic Server at 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1


### Description

Invalid values in the Content-Length header sent to Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread.html/ra1a41ff92a70d25bf576d7da2590575e8ff430393a3f4a0c34de4277%40%3Cusers.trafficserver.apache.org%3E


## Specific sequence of HTTP/2 frames can cause ATS to crash ## { #CVE-2021-32566 }

CVE-2021-32566 [\[CVE json\]](./CVE-2021-32566.cve.json) [\[OSV json\]](./CVE-2021-32566.osv.json)



_Last updated: 2021-06-30T07:11:47.425Z_

### Affected

* Apache Traffic Server at 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1


### Description

Improper Input Validation vulnerability in HTTP/2 of Apache Traffic Server allows an attacker to DOS the server.  This issue affects Apache Traffic Server 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread.html/ra1a41ff92a70d25bf576d7da2590575e8ff430393a3f4a0c34de4277%40%3Cusers.trafficserver.apache.org%3E


## Reading HTTP/2 frames too many times ## { #CVE-2021-32567 }

CVE-2021-32567 [\[CVE json\]](./CVE-2021-32567.cve.json) [\[OSV json\]](./CVE-2021-32567.osv.json)



_Last updated: 2021-06-30T07:12:25.231Z_

### Affected

* Apache Traffic Server at 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1


### Description

Improper Input Validation vulnerability in HTTP/2 of Apache Traffic Server allows an attacker to DOS the server.  This issue affects Apache Traffic Server 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread.html/ra1a41ff92a70d25bf576d7da2590575e8ff430393a3f4a0c34de4277%40%3Cusers.trafficserver.apache.org%3E


## Dynamic stack buffer overflow in cachekey plugin ## { #CVE-2021-35474 }

CVE-2021-35474 [\[CVE json\]](./CVE-2021-35474.cve.json) [\[OSV json\]](./CVE-2021-35474.osv.json)



_Last updated: 2021-06-30T07:12:52.360Z_

### Affected

* Apache Traffic Server at 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1


### Description

Stack-based Buffer Overflow vulnerability in cachekey plugin of Apache Traffic Server.  This issue affects Apache Traffic Server 7.0.0 to 7.1.12, 8.0.0 to 8.1.1, 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread.html/ra1a41ff92a70d25bf576d7da2590575e8ff430393a3f4a0c34de4277%40%3Cusers.trafficserver.apache.org%3E


## Request Smuggling - LF line ending ## { #CVE-2021-37147 }

CVE-2021-37147 [\[CVE json\]](./CVE-2021-37147.cve.json) [\[OSV json\]](./CVE-2021-37147.osv.json)



_Last updated: 2021-11-02T21:14:21.298Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.1.2 and 9.0.0 to 9.1.0


### Description

Improper input validation vulnerability in header parsing of Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 8.0.0 to 8.1.2 and 9.0.0 to 9.1.0.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


### Credits
* Apache Traffic Server would like to thank Mattias Grenfeldt and Asta Olofsson for reporting this issue.


## Request Smuggling - transfer encoding validation ## { #CVE-2021-37148 }

CVE-2021-37148 [\[CVE json\]](./CVE-2021-37148.cve.json) [\[OSV json\]](./CVE-2021-37148.osv.json)



_Last updated: 2021-11-02T21:14:46.545Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.1.2 and 9.0.0 to 9.0.1


### Description

Improper input validation vulnerability in header parsing of Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 8.0.0 to 8.1.2 and 9.0.0 to 9.0.1.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


### Credits
* Apache Traffic Server would like to thank Mattias Grenfeldt and Asta Olofsson for reporting this issue


## Request Smuggling - multiple attacks ## { #CVE-2021-37149 }

CVE-2021-37149 [\[CVE json\]](./CVE-2021-37149.cve.json) [\[OSV json\]](./CVE-2021-37149.osv.json)



_Last updated: 2021-11-02T21:15:10.588Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.1.2 and 9.0.0 to 9.1.0


### Description

Improper Input Validation vulnerability in header parsing of Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 8.0.0 to 8.1.2 and 9.0.0 to 9.1.0.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


### Credits
* Apache Traffic Server would like to thank Mattias Grenfeldt and Asta Olofsson for reporting this issue


## Protocol vs scheme mismatch ## { #CVE-2021-37150 }

CVE-2021-37150 [\[CVE json\]](./CVE-2021-37150.cve.json) [\[OSV json\]](./CVE-2021-37150.osv.json)



_Last updated: 2022-08-10T05:43:13.024Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.1.2


### Description

Improper Input Validation vulnerability in header parsing of Apache Traffic Server allows an attacker to request secure resources.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


## Not validating origin TLS certificate ## { #CVE-2021-38161 }

CVE-2021-38161 [\[CVE json\]](./CVE-2021-38161.cve.json) [\[OSV json\]](./CVE-2021-38161.osv.json)



_Last updated: 2021-11-02T21:16:04.785Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.0.8


### Description

Improper Authentication vulnerability in TLS origin verification of Apache Traffic Server allows for man in the middle attacks.  This issue affects Apache Traffic Server 8.0.0 to 8.0.8.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


## ATS stops accepting connections on FreeBSD ## { #CVE-2021-41585 }

CVE-2021-41585 [\[CVE json\]](./CVE-2021-41585.cve.json) [\[OSV json\]](./CVE-2021-41585.osv.json)



_Last updated: 2021-11-02T21:16:43.796Z_

### Affected

* Apache Traffic Server at 7.0.0 to 9.1.0


### Description

Improper Input Validation vulnerability in accepting socket connections in Apache Traffic Server allows an attacker to make the server stop accepting new connections.  This issue affects Apache Traffic Server 5.0.0 to 9.1.0.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


### Credits
* Apache Traffic Server would like to thank Asbjorn Bjornstad for finding this issue.


## heap-buffer-overflow with stats-over-http plugin ## { #CVE-2021-43082 }

CVE-2021-43082 [\[CVE json\]](./CVE-2021-43082.cve.json) [\[OSV json\]](./CVE-2021-43082.osv.json)



_Last updated: 2021-11-02T21:16:59.675Z_

### Affected

* Apache Traffic Server at 9.1.0


### Description

Buffer Copy without Checking Size of Input ('Classic Buffer Overflow') vulnerability in the stats-over-http plugin of Apache Traffic Server allows an attacker to overwrite memory.  This issue affects Apache Traffic Server 9.1.0.

### References
* https://lists.apache.org/thread/k01797hyncx53659wr3o72s5cvkc3164


### Credits
* Apache Traffic Server would like to thank Masori Koshiba for finding this issue.


## HTTP request line fuzzing attacks ## { #CVE-2021-44040 }

CVE-2021-44040 [\[CVE json\]](./CVE-2021-44040.cve.json) [\[OSV json\]](./CVE-2021-44040.osv.json)



_Last updated: 2022-03-23T14:04:02.939Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.1.3 and 9.0.0 to 9.1.1


### Description

Improper Input Validation vulnerability in request line parsing of Apache Traffic Server allows an attacker to send invalid requests.  This issue affects Apache Traffic Server 8.0.0 to 8.1.3 and 9.0.0 to 9.1.1.

### References
* https://lists.apache.org/thread/zblwzcfs9ryhwjr89wz4osw55pxm6dx6


### Credits
* Apache Traffic Server would like to thank Bahruz Jabiyev, Steven Sprecher and Kaan Onarlioglu for reporting these issues.  We used his tool t-reqs (https://github.com/bahruzjabiyev/t-reqs-http-fuzzer) for discovering them.


## Improper authentication vulnerability in TLS origin verification ## { #CVE-2021-44759 }

CVE-2021-44759 [\[CVE json\]](./CVE-2021-44759.cve.json) [\[OSV json\]](./CVE-2021-44759.osv.json)



_Last updated: 2022-03-23T14:03:27.211Z_

### Affected

* Apache Traffic Server at 8.0.0 to 8.1.0


### Description

Improper Authentication vulnerability in TLS origin validation of Apache Traffic Server allows an attacker to create a man in the middle attack.  This issue affects Apache Traffic Server 8.0.0 to 8.1.0.

### References
* https://lists.apache.org/thread/zblwzcfs9ryhwjr89wz4osw55pxm6dx6


### Credits
* Apache Traffic Server would like to thank Takuya Kitano for reporting this issue.


## Improper input validation on HTTP/2 headers  ## { #CVE-2022-25763 }

CVE-2022-25763 [\[CVE json\]](./CVE-2022-25763.cve.json) [\[OSV json\]](./CVE-2022-25763.osv.json)



_Last updated: 2022-10-20T20:25:04.197Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.1.2


### Description

Improper Input Validation vulnerability in HTTP/2 request validation of Apache Traffic Server allows an attacker to create smuggle or cache poison attacks.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


### Credits
* Apache Traffic Server would like to thank Mazakatsu Kitajo, Dhana Sekaran, and Zhang Zeyu for reporting this issue.


##  Insufficient Validation of HTTP/1.x Headers ## { #CVE-2022-28129 }

CVE-2022-28129 [\[CVE json\]](./CVE-2022-28129.cve.json) [\[OSV json\]](./CVE-2022-28129.osv.json)



_Last updated: 2022-08-10T05:42:44.803Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.1.2


### Description

Improper Input Validation vulnerability in HTTP/1.1 header parsing of Apache Traffic Server allows an attacker to send invalid headers.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


### Credits
* Apache Traffic Server would like to thank Zhang Zeyu for reporting this issue.


## Transfer-Encoding not treated as hop-by-hop ## { #CVE-2022-31778 }

CVE-2022-31778 [\[CVE json\]](./CVE-2022-31778.cve.json) [\[OSV json\]](./CVE-2022-31778.osv.json)



_Last updated: 2022-08-10T05:44:15.239Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.0.2


### Description

Improper Input Validation vulnerability in handling the Transfer-Encoding header of Apache Traffic Server allows an attacker to poison the cache.  This issue affects Apache Traffic Server 8.0.0 to 9.0.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


### Credits
* Apache Traffic Server would like to thank Chris Lemmons for reporting this issue.


## Improper HTTP/2 scheme and method validation ## { #CVE-2022-31779 }

CVE-2022-31779 [\[CVE json\]](./CVE-2022-31779.cve.json) [\[OSV json\]](./CVE-2022-31779.osv.json)



_Last updated: 2022-10-27T00:00:36.092Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.1.2


### Description

Improper Input Validation vulnerability in HTTP/2 header parsing of Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


### Credits
* Apache Traffic Server would like to thank Dhana Sekaran for reporting this issue.


## HTTP/2 framing vulnerabilities  ## { #CVE-2022-31780 }

CVE-2022-31780 [\[CVE json\]](./CVE-2022-31780.cve.json) [\[OSV json\]](./CVE-2022-31780.osv.json)



_Last updated: 2022-08-10T05:45:38.174Z_

### Affected

* Apache Traffic Server at 8.0.0 to 9.1.2


### Description

Improper Input Validation vulnerability in HTTP/2 frame handling of Apache Traffic Server allows an attacker to smuggle requests.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/rc64lwbdgrkv674koc3zl1sljr9vwg21


### Credits
* Apache Traffic Server would like to thank Bahruz Jabiyev, Steven Sprecher, Anthony Gavazzi, Tommaso Innocenti, Kaan Onarlioglu, and Engin Kirda for reporting these issues.  


## Improperly handled requests can cause crashes in specific plugins ## { #CVE-2022-32749 }

CVE-2022-32749 [\[CVE json\]](./CVE-2022-32749.cve.json) [\[OSV json\]](./CVE-2022-32749.osv.json)



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


## Improperly reading the client requests ## { #CVE-2022-37392 }

CVE-2022-37392 [\[CVE json\]](./CVE-2022-37392.cve.json) [\[OSV json\]](./CVE-2022-37392.osv.json)



_Last updated: 2022-12-19T10:58:23.000Z_

### Affected

* Apache Traffic Server from 8.0.0 through 9.1.3


### Description

Improper Check for Unusual or Exceptional Conditions vulnerability in handling the requests to Apache Traffic Server.  This issue affects Apache Traffic Server 8.0.0 to 9.1.2.

### References
* https://lists.apache.org/thread/mrj2lg4s0hf027rk7gz8t7hbn9xpfg02


### Credits
* Menno de Gier (finder)


## Security issues with the xdebug plugin ## { #CVE-2022-40743 }

CVE-2022-40743 [\[CVE json\]](./CVE-2022-40743.cve.json) [\[OSV json\]](./CVE-2022-40743.osv.json)



_Last updated: 2023-07-17T14:33:07.403Z_

### Affected

* Apache Traffic Server from 9.0.0 through 9.1.3


### Description

Improper Input Validation vulnerability for the xdebug plugin in Apache Software Foundation Apache Traffic Server can lead to cross site scripting and cache poisoning attacks.<p>This issue affects Apache Traffic Server: 9.0.0 to 9.1.3. Users should upgrade to 9.1.4 or later versions.<br></p>

### References
* https://lists.apache.org/thread/mrj2lg4s0hf027rk7gz8t7hbn9xpfg02


### Credits
* Nick Frost (finder)


## The TRACE method can be use to disclose network information ## { #CVE-2022-47184 }

CVE-2022-47184 [\[CVE json\]](./CVE-2022-47184.cve.json) [\[OSV json\]](./CVE-2022-47184.osv.json)



_Last updated: 2023-06-14T07:42:29.792Z_

### Affected

* Apache Traffic Server from 8.0.0 through 9.2.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Traffic Server.<p>This issue affects Apache Traffic Server: 8.0.0 to 9.2.0.</p>

### References
* https://lists.apache.org/thread/tns2b4khyyncgs5v5p9y35pobg9z2bvs


### Credits
* Martin O'Neal (reporter)


## Invalid Range header causes a crash ## { #CVE-2022-47185 }

CVE-2022-47185 [\[CVE json\]](./CVE-2022-47185.cve.json) [\[OSV json\]](./CVE-2022-47185.osv.json)



_Last updated: 2023-08-09T06:57:36.707Z_

### Affected

* Apache Traffic Server through 9.2.1


### Description

Improper input validation vulnerability on the range header in Apache Software Foundation Apache Traffic Server.<p>This issue affects Apache Traffic Server: through 9.2.1.</p>

### References
* https://lists.apache.org/thread/jsl6dfdgs1mjjo1mbtyflyjr7xftswhc


### Credits
* Katsutoshi Ikenoya (finder)


## Configuration option to block the PUSH method in ATS didn't work ## { #CVE-2023-30631 }

CVE-2023-30631 [\[CVE json\]](./CVE-2023-30631.cve.json) [\[OSV json\]](./CVE-2023-30631.osv.json)



_Last updated: 2023-06-14T07:44:52.725Z_

### Affected

* Apache Traffic Server from 8.0.0 through 9.2.0


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Traffic Server.&nbsp; The configuration option&nbsp;proxy.config.http.push_method_enabled didn't function.&nbsp; However, by default the PUSH method is blocked in the ip_allow configuration file.<p>This issue affects Apache Traffic Server: from 8.0.0 through 9.2.0.</p><p>8.x users should upgrade to 8.1.7 or later versions<br>9.x users should upgrade to 9.2.1 or later versions<br></p>

### References
* https://lists.apache.org/thread/tns2b4khyyncgs5v5p9y35pobg9z2bvs


### Credits
* Chris Lemmons (finder)


## s3_auth plugin problem with hash calculation ## { #CVE-2023-33933 }

CVE-2023-33933 [\[CVE json\]](./CVE-2023-33933.cve.json) [\[OSV json\]](./CVE-2023-33933.osv.json)



_Last updated: 2023-08-31T19:49:23.749Z_

### Affected

* Apache Traffic Server from 8.0.0 through 9.2.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Traffic Server.<p>This issue affects Apache Traffic Server: from 8.0.0 through 9.2.0.</p><p>8.x users should upgrade to 8.1.7 or later versions<br>9.x users should upgrade to 9.2.1 or later versions<br></p>

### References
* https://lists.apache.org/thread/tns2b4khyyncgs5v5p9y35pobg9z2bvs


### Credits
* Masakazu Kitajo (reporter)


## Differential fuzzing for HTTP request parsing discrepancies ## { #CVE-2023-33934 }

CVE-2023-33934 [\[CVE json\]](./CVE-2023-33934.cve.json)

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


## Incomplete field name check allows request smuggling ## { #CVE-2023-38522 }

CVE-2023-38522 [\[CVE json\]](./CVE-2023-38522.cve.json) [\[OSV json\]](./CVE-2023-38522.osv.json)



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


## Malformed http/2 frames can cause an abort ## { #CVE-2023-39456 }

CVE-2023-39456 [\[CVE json\]](./CVE-2023-39456.cve.json) [\[OSV json\]](./CVE-2023-39456.osv.json)



_Last updated: 2023-10-17T06:58:15.367Z_

### Affected

* Apache Traffic Server from 9.0.0 through 9.2.2


### Description

Improper Input Validation vulnerability in Apache Traffic Server with malformed HTTP/2 frames.<p>This issue affects Apache Traffic Server: from 9.0.0 through 9.2.2.</p><p>Users are recommended to upgrade to version 9.2.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/5py8h42mxfsn8l1wy6o41xwhsjlsd87q


### Credits
*  Akshat Parikh (finder)


## s3_auth plugin problem with hash calculation ## { #CVE-2023-41752 }

CVE-2023-41752 [\[CVE json\]](./CVE-2023-41752.cve.json) [\[OSV json\]](./CVE-2023-41752.osv.json)



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


## HTTP/2 CONTINUATION frames can be utilized for DoS attack ## { #CVE-2024-31309 }

CVE-2024-31309 [\[CVE json\]](./CVE-2024-31309.cve.json) [\[OSV json\]](./CVE-2024-31309.osv.json)



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


## Incomplete check for chunked trailer section allows request smuggling ## { #CVE-2024-35161 }

CVE-2024-35161 [\[CVE json\]](./CVE-2024-35161.cve.json) [\[OSV json\]](./CVE-2024-35161.osv.json)



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


## Invalid Accept-Encoding can force forwarding requests ## { #CVE-2024-35296 }

CVE-2024-35296 [\[CVE json\]](./CVE-2024-35296.cve.json) [\[OSV json\]](./CVE-2024-35296.osv.json)



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


## Request smuggling via pipelining after a chunked message body ## { #CVE-2024-38311 }

CVE-2024-38311 [\[CVE json\]](./CVE-2024-38311.cve.json) [\[OSV json\]](./CVE-2024-38311.osv.json)



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


## Cache key plugin is vulnerable to cache poisoning attack ## { #CVE-2024-38479 }

CVE-2024-38479 [\[CVE json\]](./CVE-2024-38479.cve.json) [\[OSV json\]](./CVE-2024-38479.osv.json)



_Last updated: 2024-12-19T08:48:33.164Z_

### Affected

* Apache Traffic Server from 8.0.0 through 8.1.11
* Apache Traffic Server from 9.0.0 through 9.2.5


### Description

<p>Improper Input Validation vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 8.0.0 through 8.1.11, from 9.0.0 through 9.2.5.</p><p>Users are recommended to upgrade to version 9.2.6, which fixes the issue, or 10.0.2, which does not have the issue.</p>

### References
* https://lists.apache.org/thread/y15fh6c7kyqvzm0f9odw7c5jh4r4np0y


## Valid Host field value can cause crashes ## { #CVE-2024-50305 }

CVE-2024-50305 [\[CVE json\]](./CVE-2024-50305.cve.json) [\[OSV json\]](./CVE-2024-50305.osv.json)



_Last updated: 2024-11-14T09:54:18.691Z_

### Affected

* Apache Traffic Server from 9.2.0 through 9.2.5


### Description

<p>Valid Host header field can cause Apache Traffic Server to crash on some platforms.</p><p>This issue affects Apache Traffic Server: from 9.2.0 through 9.2.5.</p><p>Users are recommended to upgrade to version 9.2.6, which fixes the issue, or 10.0.2, which does not have the issue.</p>

### References
* https://lists.apache.org/thread/y15fh6c7kyqvzm0f9odw7c5jh4r4np0y


## Server process can fail to drop privilege ## { #CVE-2024-50306 }

CVE-2024-50306 [\[CVE json\]](./CVE-2024-50306.cve.json) [\[OSV json\]](./CVE-2024-50306.osv.json)



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


## Malformed chunked message body allows request smuggling ## { #CVE-2024-53868 }

CVE-2024-53868 [\[CVE json\]](./CVE-2024-53868.cve.json) [\[OSV json\]](./CVE-2024-53868.osv.json)



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


## Intercept plugins are not access controlled ## { #CVE-2024-56195 }

CVE-2024-56195 [\[CVE json\]](./CVE-2024-56195.cve.json) [\[OSV json\]](./CVE-2024-56195.osv.json)



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


## ACL is not fully compatible with older versions ## { #CVE-2024-56196 }

CVE-2024-56196 [\[CVE json\]](./CVE-2024-56196.cve.json) [\[OSV json\]](./CVE-2024-56196.osv.json)



_Last updated: 2025-03-06T11:21:46.767Z_

### Affected

* Apache Traffic Server from 10.0.0 through 10.0.3


### Description

<p>Improper Access Control vulnerability in Apache Traffic Server.</p><p>This issue affects Apache Traffic Server: from 10.0.0 through 10.0.3.</p><p>Users are recommended to upgrade to version 10.0.4, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/btofzws2yqskk2n7f01r3l1819x01023


### Credits
* Chris McFarlen (reporter)


## Expect header field can unreasonably retain resource ## { #CVE-2024-56202 }

CVE-2024-56202 [\[CVE json\]](./CVE-2024-56202.cve.json) [\[OSV json\]](./CVE-2024-56202.osv.json)



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


## Client IP address from PROXY protocol is not used for ACL ## { #CVE-2025-31698 }

CVE-2025-31698 [\[CVE json\]](./CVE-2025-31698.cve.json) [\[OSV json\]](./CVE-2025-31698.osv.json)



_Last updated: 2025-06-19T10:07:45.344Z_

### Affected

* Apache Traffic Server from 10.0.0 through 10.0.6
* Apache Traffic Server from 9.0.0 through 9.2.10


### Description

<p>ACL configured in ip_allow.config or remap.config does not use IP addresses that are provided by PROXY protocol.</p>Users can use a new setting (proxy.config.acl.subjects) to choose which IP addresses to use for the ACL if Apache Traffic Server is configured to accept PROXY protocol.&nbsp;<br><p>This issue affects undefined: from 10.0.0 through 10.0.6, from 9.0.0 through 9.2.10.</p><p>Users are recommended to upgrade to version 9.2.11 or 10.0.6, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/15t32nxbypqg1m2smp640vjx89o6v5f8


## Remote DoS via memory exhaustion in ESI Plugin ## { #CVE-2025-49763 }

CVE-2025-49763 [\[CVE json\]](./CVE-2025-49763.cve.json) [\[OSV json\]](./CVE-2025-49763.osv.json)



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
