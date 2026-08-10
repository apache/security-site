---
title: Apache Qpid security advisories
description: Security information for Apache Qpid
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Qpid? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Qpid).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Unbounded echo flow responses can lead to denial of service ## { #CVE-2026-68080 }

CVE-2026-68080 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68080) [\[CVE json\]](./CVE-2026-68080.cve.json) [\[OSV json\]](./CVE-2026-68080.osv.json)



_Last updated: 2026-08-05T05:51:18.656Z_

### Affected

* Apache Qpid Broker-J through 10.0.1


### Description

<div>It was not possible to govern the rate at which the broker would respond to an echo flow, enabling an authenticated attacker to cause excessive resource usage and potential denial of service.</div><div>This issue affects Apache Qpid Broker-J: through 10.0.1.</div><div>Users are recommended to upgrade to version 10.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/tcnrv5nhmnsrzz92o4owxgycro6llt57


## Unable to govern the maximum number of transfer frames per incoming delivery ## { #CVE-2026-68078 }

CVE-2026-68078 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68078) [\[CVE json\]](./CVE-2026-68078.cve.json) [\[OSV json\]](./CVE-2026-68078.osv.json)



_Last updated: 2026-08-05T05:43:32.321Z_

### Affected

* Apache Qpid Broker-J through 10.0.1


### Description

<div>It was not possible to govern the maximum number of transfer frames per incoming delivery, enabling an authenticated attacker to cause excessive resource usage and potential denial of service.</div><div>This issue affects Apache Qpid Broker-J: through 10.0.1.</div><div>Users are recommended to upgrade to version 10.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/m8gs6pfp1fmbgwcjr8zsgn95hfh15f8o


## Unbounded disposition range handling can lead to denial of service ## { #CVE-2026-68077 }

CVE-2026-68077 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68077) [\[CVE json\]](./CVE-2026-68077.cve.json) [\[OSV json\]](./CVE-2026-68077.osv.json)



_Last updated: 2026-08-05T05:41:03.741Z_

### Affected

* Apache Qpid Broker-J through 10.0.1


### Description

<div>An authenticated attacker can craft a disposition frame with large or illegal ranges causing excessive CPU usage due to naive range handling, leading to denial of service.</div><div>This issue affects Apache Qpid Broker-J: through 10.0.1.</div><div>Users are recommended to upgrade to version 10.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/gzc78gdrlw2711v8jzgmsto8bqvg28y8


## Incoming session flow control window can be exceeded ## { #CVE-2026-68075 }

CVE-2026-68075 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68075) [\[CVE json\]](./CVE-2026-68075.cve.json) [\[OSV json\]](./CVE-2026-68075.osv.json)



_Last updated: 2026-08-05T05:35:58.182Z_

### Affected

* Apache Qpid Broker-J through 10.0.1


### Description

<div>An authenticated attacker could exceed the session flow control incoming window potentially leading to denial of service.</div><div>This issue affects Apache Qpid Broker-J: through 10.0.1.</div><div>Users are recommended to upgrade to version 10.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/lht725jgkowmyyjl039roffg6pyvbxz0


## Unbounded symbol value caching can lead to pre-authentication resource exhaustion ## { #CVE-2026-68074 }

CVE-2026-68074 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68074) [\[CVE json\]](./CVE-2026-68074.cve.json) [\[OSV json\]](./CVE-2026-68074.osv.json)



_Last updated: 2026-08-05T05:19:51.744Z_

### Affected

* Apache Qpid Broker-J through 10.0.1


### Description

<div>A pre-authentication attacker could leverage unbounded symbol value caching to cause resource exhaustion leading to denial of service.</div><div>This issue affects Apache Qpid Broker-J: through 10.0.1.</div><div>Users are recommended to upgrade to version 10.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/9t1pvl36z69ssww6449od5g0tszqnhjs


## Unbounded type nesting can lead to pre-authentication stack overflow ## { #CVE-2026-68073 }

CVE-2026-68073 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68073) [\[CVE json\]](./CVE-2026-68073.cve.json) [\[OSV json\]](./CVE-2026-68073.osv.json)



_Last updated: 2026-08-05T05:32:20.617Z_

### Affected

* Apache Qpid Broker-J through 10.0.1


### Description

<div>A pre-authentication attacker could leverage type nesting to cause a StackOverflowError potentially leading to denial of service.</div><div>This issue affects Apache Qpid Broker-J: through 10.0.1.</div><div>Users are recommended to upgrade to version 10.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/djz1gnrk882vzjo8rykyf9bnywqbvwwr


## Type size/count handling can lead to excessive allocation pre-authentication ## { #CVE-2026-68060 }

CVE-2026-68060 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68060) [\[CVE json\]](./CVE-2026-68060.cve.json) [\[OSV json\]](./CVE-2026-68060.osv.json)



_Last updated: 2026-08-05T05:26:23.306Z_

### Affected

* Apache Qpid Broker-J through 10.0.1


### Description

<div>A pre-authentication attacker could leverage type size/count handling to cause excessive allocation leading to potential denial of service.</div><div>This issue affects Apache Qpid Broker-J: through 10.0.1.</div><div>Users are recommended to upgrade to version 10.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/0slvl8h25w3z4opnh08yyn8l3chko5c9


## Unable to govern the maximum number of transfer frames per incoming delivery ## { #CVE-2026-67592 }

CVE-2026-67592 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67592) [\[CVE json\]](./CVE-2026-67592.cve.json) [\[OSV json\]](./CVE-2026-67592.osv.json)



_Last updated: 2026-08-05T05:44:14.457Z_

### Affected

* Apache Qpid ProtonJ2 through 1.1.0


### Description

<div>It was not possible to govern the maximum number of transfer frames per incoming delivery, enabling an authenticated attacker to cause excessive resource usage and potential denial of service.</div><div>This issue affects Apache Qpid ProtonJ2: through 1.1.0.</div><div>Users are recommended to upgrade to version 1.2.0, which fixes the issue</div>

### References
* https://lists.apache.org/thread/b4pv9hfdk7ox78pss77sb4nzwjrvqhhz


## Incoming session flow control window can be exceeded ## { #CVE-2026-67591 }

CVE-2026-67591 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67591) [\[CVE json\]](./CVE-2026-67591.cve.json) [\[OSV json\]](./CVE-2026-67591.osv.json)



_Last updated: 2026-08-05T05:38:21.990Z_

### Affected

* Apache Qpid ProtonJ2 through 1.1.0


### Description

<div>An authenticated attacker could exceed the session flow control incoming window potentially leading to denial of service.</div><div>This issue affects Apache Qpid ProtonJ2: through 1.1.0.</div><div>Users are recommended to upgrade to version 1.2.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/rwmggh2bkm6qotxpdfcplht3jgw5n036


## Unbounded type nesting can lead to pre-authentication stackoverflow ## { #CVE-2026-67590 }

CVE-2026-67590 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67590) [\[CVE json\]](./CVE-2026-67590.cve.json) [\[OSV json\]](./CVE-2026-67590.osv.json)



_Last updated: 2026-08-05T05:33:34.406Z_

### Affected

* Apache Qpid ProtonJ2 through 1.1.0


### Description

<div>A pre-authentication attacker could leverage type nesting to cause a StackOverflowError potentially leading to denial of service.</div><div>This issue affects Apache Qpid ProtonJ2: through 1.1.0.</div><div>Users are recommended to upgrade to version 1.2.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/kmov6k7f3moqy01m1s370fl61vgos3ly


## Type size/count handling can lead to excessive allocation pre-authentication ## { #CVE-2026-67589 }

CVE-2026-67589 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67589) [\[CVE json\]](./CVE-2026-67589.cve.json) [\[OSV json\]](./CVE-2026-67589.osv.json)



_Last updated: 2026-08-05T05:28:10.043Z_

### Affected

* Apache Qpid ProtonJ2 through 1.1.0


### Description

<div>A pre-authentication attacker could leverage type size/count handling to cause excessive allocation leading to potential denial of service.</div><div>This issue affects Apache Qpid ProtonJ2: through 1.1.0.</div><div>Users are recommended to upgrade to version 1.2.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/bs24x4778dh72xtfs299cy8krvdlo47q


### Credits
* Apache Qpid security team (finder)
* xxy010605@gmail.com (reporter)


## Unbounded symbol value caching can lead to pre-authentication resource exhaustion ## { #CVE-2026-67588 }

CVE-2026-67588 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67588) [\[CVE json\]](./CVE-2026-67588.cve.json) [\[OSV json\]](./CVE-2026-67588.osv.json)



_Last updated: 2026-08-05T05:21:39.842Z_

### Affected

* Apache Qpid ProtonJ2 through 1.1.0


### Description

<div>A pre-authentication attacker could leverage unbounded symbol value caching to cause resource exhaustion leading to denial of service.</div><div>This issue affects Apache Qpid ProtonJ2: through 1.1.0.</div><div>Users are recommended to upgrade to version 1.2.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/vk4j02dzggfdrdkwvzmqo4jro2tgj0jt


## Unable to govern the maximum number of transfer frames per incoming delivery ## { #CVE-2026-67555 }

CVE-2026-67555 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67555) [\[CVE json\]](./CVE-2026-67555.cve.json) [\[OSV json\]](./CVE-2026-67555.osv.json)



_Last updated: 2026-08-05T05:43:53.150Z_

### Affected

* Apache Qpid Proton Dotnet through 1.0.0


### Description

<div>It was not possible to govern the maximum number of transfer frames per incoming delivery, enabling an authenticated attacker to cause excessive resource usage and potential denial of service</div><div>This issue affects Apache Qpid Proton-Dotnet: through 1.0.0.</div><div>Users are recommended to upgrade to version 1.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/dwrb02dp714lvlfxdj4o5bc9h3z54sw3


## Unbounded disposition range handling can lead to denial of service ## { #CVE-2026-67554 }

CVE-2026-67554 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67554) [\[CVE json\]](./CVE-2026-67554.cve.json) [\[OSV json\]](./CVE-2026-67554.osv.json)



_Last updated: 2026-08-05T05:41:21.799Z_

### Affected

* Apache Qpid Proton Dotnet through 1.0.0


### Description

<div>An authenticated attacker can craft a disposition frame with large or illegal ranges causing excessive CPU usage due to naive range handling, leading to denial of service.</div><div>This issue affects Apache Qpid Proton-Dotnet: through 1.0.0.</div><div>Users are recommended to upgrade to version 1.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/5ndlowz29464ytj98gz9z9ljhwnmb2hm


## Incoming session flow control window can be exceeded ## { #CVE-2026-67553 }

CVE-2026-67553 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67553) [\[CVE json\]](./CVE-2026-67553.cve.json) [\[OSV json\]](./CVE-2026-67553.osv.json)



_Last updated: 2026-08-05T05:37:23.826Z_

### Affected

* Apache Qpid Proton Dotnet through 1.0.0


### Description

<div>An authenticated attacker could exceed the session flow control incoming window potentially leading to denial of service.</div><div>This issue affects Apache Qpid Proton-Dotnet: through 1.0.0.</div><div>Users are recommended to upgrade to version 1.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/hvsncmcbgjrn85crs909nf4y3dqqrywo


## Unbounded type nesting can lead to pre-authentication stackoverflow ## { #CVE-2026-67552 }

CVE-2026-67552 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67552) [\[CVE json\]](./CVE-2026-67552.cve.json) [\[OSV json\]](./CVE-2026-67552.osv.json)



_Last updated: 2026-08-05T05:32:53.769Z_

### Affected

* Apache Qpid Proton Dotnet through 1.0.0


### Description

<div>A pre-authentication attacker could leverage type nesting to cause a StackOverflowError potentially leading to denial of service.</div><div>This issue affects Apache Qpid Proton-Dotnet through 1.0.0.</div><div>Users are recommended to upgrade to version 1.1.0, which fixes the issue</div>

### References
* https://lists.apache.org/thread/4dyg0gycrv55ox4oywqght61b053g8xj


## Type size/count handling can lead to excessive allocation pre-authentication ## { #CVE-2026-67551 }

CVE-2026-67551 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67551) [\[CVE json\]](./CVE-2026-67551.cve.json) [\[OSV json\]](./CVE-2026-67551.osv.json)



_Last updated: 2026-08-05T05:27:20.446Z_

### Affected

* Apache Qpid Proton Dotnet through 1.0.0


### Description

<div> pre-authentication attacker could leverage type size/count handling to cause excessive allocation leading to potential denial of service.</div><div>This issue affects Apache Qpid Proton-Dotnet: through 1.0.0.</div><div>Users are recommended to upgrade to version 1.1.0, which fixes the issue.</div>

### References
* https://lists.apache.org/thread/o566fhkrr3gg0lyzt24xwvz9w94oo6ro


## Unbounded symbol value caching can lead to pre-authentication resource exhaustion ## { #CVE-2026-67465 }

CVE-2026-67465 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-67465) [\[CVE json\]](./CVE-2026-67465.cve.json) [\[OSV json\]](./CVE-2026-67465.osv.json)



_Last updated: 2026-08-05T05:21:00.415Z_

### Affected

* Apache Qpid Proton Dotnet through 1.0.0


### Description

<p>A pre-authentication attacker could leverage unbounded symbol value caching to cause resource exhaustion leading to denial of service.</p><p>This issue affects Apache Qpid Proton-Dotnet: through 1.0.0.</p><p>Users are recommended to upgrade to version 1.1.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zl2pj5fo32lbyrwof89tdyrgt67bbo0m


## Unable to govern the maximum number of transfer frames per incoming delivery ## { #CVE-2026-66277 }

CVE-2026-66277 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66277) [\[CVE json\]](./CVE-2026-66277.cve.json) [\[OSV json\]](./CVE-2026-66277.osv.json)



_Last updated: 2026-08-05T05:42:26.473Z_

### Affected

* Apache Qpid Proton-J through 0.34.1


### Description

<p>It was not possible to govern the maximum number of transfer frames per incoming delivery, enabling an authenticated attacker to cause excessive resource usage and potential denial of service.</p><p>This issue affects Apache Qpid Proton-J: through 0.34.1.</p><p>Users are recommended to upgrade to version 0.35.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/48tflr3sx0sxq9bcdy5rh06oy3gmwx02


## Unbounded disposition range handling can lead to denial of service ## { #CVE-2026-66276 }

CVE-2026-66276 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66276) [\[CVE json\]](./CVE-2026-66276.cve.json) [\[OSV json\]](./CVE-2026-66276.osv.json)



_Last updated: 2026-08-05T05:39:26.606Z_

### Affected

* Apache Qpid Proton-J through 0.34.1


### Description

<div>An authenticated attacker can craft a disposition frame with large or illegal ranges causing excessive CPU usage due to naive range handling, leading to denial of service.</div><p>This issue affects Apache Qpid Proton-J: through 0.34.1.</p><p>Users are recommended to upgrade to version 0.35.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/14nj0lpsqpnd3q0hw0t0tw44qvdo1jc2


## Incoming session flow control window can be exceeded ## { #CVE-2026-66275 }

CVE-2026-66275 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66275) [\[CVE json\]](./CVE-2026-66275.cve.json) [\[OSV json\]](./CVE-2026-66275.osv.json)



_Last updated: 2026-08-05T05:34:44.424Z_

### Affected

* Apache Qpid Proton-J through 0.34.1


### Description

<p>An authenticated attacker could exceed the session flow control incoming window potentially leading to denial of service.</p><p>This issue affects Apache Qpid Proton-J: through 0.34.1.</p><p>Users are recommended to upgrade to version 0.35.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/jds59nxrgcxtlx7xl0kvl5hqt07thxzt


## Unbounded type nesting can lead to pre-authentication stackoverflow ## { #CVE-2026-66274 }

CVE-2026-66274 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66274) [\[CVE json\]](./CVE-2026-66274.cve.json) [\[OSV json\]](./CVE-2026-66274.osv.json)



_Last updated: 2026-08-05T05:29:40.499Z_

### Affected

* Apache Qpid Proton-J through 0.34.1


### Description

<p>A pre-authentication attacker could leverage type nesting to cause a StackOverflowError potentially leading to denial of service.</p><p>This issue affects Apache Qpid Proton-J: through 0.34.1.</p><p>Users are recommended to upgrade to version 0.35.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/h7xolzws2by2qhdjf7scbx87foxojb5h


## Type size/count handling can lead to excessive allocation pre-authentication ## { #CVE-2026-66273 }

CVE-2026-66273 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66273) [\[CVE json\]](./CVE-2026-66273.cve.json) [\[OSV json\]](./CVE-2026-66273.osv.json)



_Last updated: 2026-08-05T05:23:28.044Z_

### Affected

* Apache Qpid Proton-J through 0.34.1


### Description

<p>A pre-authentication attacker could leverage type size/count handling to cause excessive allocation leading to potential denial of service.</p><p>This issue affects Apache Qpid Proton-J: through 0.34.1.</p><p>Users are recommended to upgrade to version 0.35.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/z34s9v5w05qk4qqtz5fs3v9wpxz6fnbh


## Unbounded symbol value caching can lead to pre-authentication resource exhaustion ## { #CVE-2026-66257 }

CVE-2026-66257 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66257) [\[CVE json\]](./CVE-2026-66257.cve.json) [\[OSV json\]](./CVE-2026-66257.osv.json)



_Last updated: 2026-08-05T05:17:56.848Z_

### Affected

* Apache Qpid Proton-J through 0.34.1


### Description

<p>A pre-authentication attacker could leverage unbounded symbol value caching to cause resource exhaustion leading to denial of service.</p><p>This issue affects Apache Qpid Proton-J: through 0.34.1.</p><p>Users are recommended to upgrade to version 0.35.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/dnczt6bgfcq2x6q8ljco177h1qmv59fm
