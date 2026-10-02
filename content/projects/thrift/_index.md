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

## Erlang thrift_json_protocol reads a whole message with no size bound ## { #CVE-2026-96990 }

CVE-2026-96990 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-96990) [\[CVE json\]](./CVE-2026-96990.cve.json) [\[OSV json\]](./CVE-2026-96990.osv.json)



_Last updated: 2026-10-02T11:00:25.502Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of Resources Without Limits or Throttling vulnerability in Apache Thrift Erlang bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/hrgcqlms4ksrz4qkqdjwoxxggdty7dgh


## nodejs web server: no `error` listener on an upgraded WebSocket connection ## { #CVE-2026-96294 }

CVE-2026-96294 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-96294) [\[CVE json\]](./CVE-2026-96294.cve.json) [\[OSV json\]](./CVE-2026-96294.osv.json)



_Last updated: 2026-10-02T11:09:53.242Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncaught exception, Improper Handling of Exceptional Conditions vulnerability in Apache Thrift NodeJS bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/52gwhsy947hj9qhgn0dql726z1q927g4


## Lua `THttpTransport:_parseHeaders` matches each header line with a backtracking pattern (quadratic) ## { #CVE-2026-96292 }

CVE-2026-96292 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-96292) [\[CVE json\]](./CVE-2026-96292.cve.json) [\[OSV json\]](./CVE-2026-96292.osv.json)



_Last updated: 2026-10-02T11:11:30.594Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Inefficient regular expression complexity, Inefficient Algorithmic Complexity vulnerability in Apache Thrift Lua bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/3wmvtvv56rky5wtszn4zr8w12kg928qn


## php `--gen php:inlined` struct readers (and `TProtocol::skipBinary`) have no recursion-depth guard ## { #CVE-2026-96289 }

CVE-2026-96289 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-96289) [\[CVE json\]](./CVE-2026-96289.cve.json) [\[OSV json\]](./CVE-2026-96289.osv.json)



_Last updated: 2026-10-02T12:07:00.960Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncontrolled Recursion vulnerability in Apache Thrift PHP bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/kv1zkwlt82lkkv20g29txr5pjnvo0pf8


## Erlang generated struct reads have no recursion-depth guard (unbounded memory) ## { #CVE-2026-96288 }

CVE-2026-96288 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-96288) [\[CVE json\]](./CVE-2026-96288.cve.json) [\[OSV json\]](./CVE-2026-96288.osv.json)



_Last updated: 2026-10-02T11:18:35.296Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncontrolled Recursion, Allocation of resources without limits or throttling vulnerability in Apache Thrift Erlang bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/vxnk7cmdtoqjn97b8szlqym1mxx0xtzb


## Perl `FramedTransport` reads and TLS socket writes re-slice the remaining buffer on every call (quadratic) ## { #CVE-2026-96287 }

CVE-2026-96287 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-96287) [\[CVE json\]](./CVE-2026-96287.cve.json) [\[OSV json\]](./CVE-2026-96287.osv.json)



_Last updated: 2026-10-02T12:05:57.430Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Inefficient Algorithmic Complexity vulnerability in Apache Thrift Perl bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/tcg16jr59z5nry066dw7ym60vl25dxt9


## Perl servers end `serve()` when serving one connection fails ## { #CVE-2026-96286 }

CVE-2026-96286 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-96286) [\[CVE json\]](./CVE-2026-96286.cve.json) [\[OSV json\]](./CVE-2026-96286.osv.json)



_Last updated: 2026-10-02T12:04:24.079Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncaught exception vulnerability in Apache Thrift Perl bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/o5386v7ytbbjv9sx7dbszw46ypod5yd9


## Ruby `SimpleServer` ends `serve()` on any non-Transport/Protocol exception ## { #CVE-2026-96277 }

CVE-2026-96277 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-96277) [\[CVE json\]](./CVE-2026-96277.cve.json) [\[OSV json\]](./CVE-2026-96277.osv.json)



_Last updated: 2026-10-02T12:03:22.302Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncaught exception, Improper Handling of Exceptional Conditions vulnerability in Apache Thrift Ruby bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/k1t5r9sz7k5tn57cnf5khw2ywlxv6098


## Lua `TFramedTransport`/`THttpTransport` re-slice the buffer on every read (quadratic) ## { #CVE-2026-94658 }

CVE-2026-94658 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94658) [\[CVE json\]](./CVE-2026-94658.cve.json) [\[OSV json\]](./CVE-2026-94658.osv.json)



_Last updated: 2026-10-02T12:02:20.074Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Inefficient Algorithmic Complexity vulnerability in Apache Thrift Lua bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/hv6b1nyk2p15gy5pmtprwo7z9m46mfcx


## javame `TJsonProtocol`/`TJSONProtocol` has no string size bound ## { #CVE-2026-94657 }

CVE-2026-94657 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94657) [\[CVE json\]](./CVE-2026-94657.cve.json) [\[OSV json\]](./CVE-2026-94657.osv.json)



_Last updated: 2026-10-02T12:01:35.174Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of resources without limits or throttling vulnerability in Apache Thrift JavaME bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/lpcmo2xjfyfww474xdyyfypkqthk9s14


### Credits
* Sylwester Lachiewicz (finder)


## rb `TJsonProtocol`/`TJSONProtocol` has no string size bound ## { #CVE-2026-94656 }

CVE-2026-94656 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94656) [\[CVE json\]](./CVE-2026-94656.cve.json) [\[OSV json\]](./CVE-2026-94656.osv.json)



_Last updated: 2026-10-02T12:00:46.391Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of resources without limits or throttling vulnerability in Apache Thrift ruby bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/lg97w2yvg3c6z06l8m5xs3j3v2m6mvj8


### Credits
* Sylwester Lachiewicz (finder)


## Lua `TJsonProtocol` string/number readers have no size bound and are quadratic ## { #CVE-2026-94655 }

CVE-2026-94655 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94655) [\[CVE json\]](./CVE-2026-94655.cve.json) [\[OSV json\]](./CVE-2026-94655.osv.json)



_Last updated: 2026-10-02T11:59:15.906Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of resources without limits or throttling, Inefficient Algorithmic Complexity vulnerability in Apache Thrift Lua bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/wdjyf4y115ybgdzz5m3gspo97lcmz1dt


### Credits
* Sylwester Lachiewicz (finder)


## Python `TNonblockingServer` busy-loops and stops selecting all fds after an 8192-byte-boundary frame ## { #CVE-2026-94654 }

CVE-2026-94654 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94654) [\[CVE json\]](./CVE-2026-94654.cve.json) [\[OSV json\]](./CVE-2026-94654.osv.json)



_Last updated: 2026-10-02T11:58:47.375Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Loop with unreachable exit condition ('infinite loop') vulnerability in Apache Thrift python bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/kx3xdttoypl8j4dcxmqbq9dwy1w0kr7j


## PHP framed/memory/HTTP transports re-slice the buffer on every read (quadratic) ## { #CVE-2026-94653 }

CVE-2026-94653 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94653) [\[CVE json\]](./CVE-2026-94653.cve.json) [\[OSV json\]](./CVE-2026-94653.osv.json)



_Last updated: 2026-10-02T11:56:33.859Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Inefficient Algorithmic Complexity vulnerability in Apache Thrift PHP bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/8zbv1y4wzr3nn5mzmdph7b0n6tm0lc4m


## C++ `TEvhttpServer` leaks its `RequestContext` when the processor throws before calling back ## { #CVE-2026-94652 }

CVE-2026-94652 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94652) [\[CVE json\]](./CVE-2026-94652.cve.json) [\[OSV json\]](./CVE-2026-94652.osv.json)



_Last updated: 2026-10-02T11:54:39.118Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Missing release of memory after effective lifetime vulnerability in Apache Thrift c++ bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/nodwz7gjvogkkh3w1jwbsslk1c7t0727


### Credits
* Sylwester Lachiewicz (finder)


## Java `TSaslNonblockingServer` `Computation.run` orphans a connection on a pre-auth parse error ## { #CVE-2026-94651 }

CVE-2026-94651 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94651) [\[CVE json\]](./CVE-2026-94651.cve.json) [\[OSV json\]](./CVE-2026-94651.osv.json)



_Last updated: 2026-10-02T10:48:32.419Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>improper handling of exceptional conditions, Missing release of resource after effective lifetime vulnerability in Apache Thrift java bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/rflzpdvtk8yhpzg99wkf5yf277nn7267


## c_glib generated struct readers have no recursion-depth guard (native stack exhaustion) ## { #CVE-2026-94650 }

CVE-2026-94650 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94650) [\[CVE json\]](./CVE-2026-94650.cve.json) [\[OSV json\]](./CVE-2026-94650.osv.json)



_Last updated: 2026-10-02T10:49:35.651Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncontrolled Recursion vulnerability in Apache Thrift c_glib bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/poskkt3p754b2f293g63934hw160o86j


### Credits
* Sylwester Lachiewicz (finder)


## dart `TJsonProtocol`/`TJSONProtocol` has no string size bound ## { #CVE-2026-94648 }

CVE-2026-94648 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94648) [\[CVE json\]](./CVE-2026-94648.cve.json) [\[OSV json\]](./CVE-2026-94648.osv.json)



_Last updated: 2026-10-02T11:52:47.045Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of resources without limits or throttling vulnerability in Apache Thrift dart bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/f9w4q6ttlc3k9404x4do25gdhqodtjnn


### Credits
* Sylwester Lachiewicz (finder)


## Node.js `server.js` ends the process on any per-connection error (+ two triggers) ## { #CVE-2026-94646 }

CVE-2026-94646 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94646) [\[CVE json\]](./CVE-2026-94646.cve.json) [\[OSV json\]](./CVE-2026-94646.osv.json)



_Last updated: 2026-10-02T11:57:22.883Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncaught exception, Improper validation of specified quantity in input, Improperly controlled modification of object prototype attributes ('prototype pollution') vulnerability in Apache Thrift nodejs bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/5hjh0gz8wf6bo7ydxjpqj92m42hwmfo8


### Credits
* Sylwester Lachiewicz (finder)


## Node.js `TJSONProtocol` uses a peer-declared container size as an unbounded loop bound ## { #CVE-2026-94645 }

CVE-2026-94645 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94645) [\[CVE json\]](./CVE-2026-94645.cve.json) [\[OSV json\]](./CVE-2026-94645.osv.json)



_Last updated: 2026-10-02T10:51:36.420Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Improper validation of specified quantity in input, Allocation of resources without limits or throttling vulnerability in Apache Thrift nodejs bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/p96mokqfy16mnqfyon46mf6g8nr9ghb6


### Credits
* Sylwester Lachiewicz (finder)


## PHP `TJSONProtocol` string/number readers have no size bound ## { #CVE-2026-94644 }

CVE-2026-94644 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94644) [\[CVE json\]](./CVE-2026-94644.cve.json) [\[OSV json\]](./CVE-2026-94644.osv.json)



_Last updated: 2026-10-02T10:53:33.571Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of resources without limits or throttling vulnerability in Apache Thrift PHP bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/8y04vvxw7ozxxh3c44vhoy7jsd6bonzq


### Credits
* Sylwester Lachiewicz (finder)


## PHP `TSimpleServer` exits the whole process on any non-transport exception ## { #CVE-2026-94642 }

CVE-2026-94642 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94642) [\[CVE json\]](./CVE-2026-94642.cve.json) [\[OSV json\]](./CVE-2026-94642.osv.json)



_Last updated: 2026-10-02T10:57:13.128Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncaught exception vulnerability in Apache Thrift PHP bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/5tjwbbyympbj16lblocv9b12s32sg113


### Credits
* Sylwester Lachiewicz (finder)


## Java `TSaslNonblockingServer`: residual of CVE-2026-61373 (thread-death black hole + no cross-connection budget) ## { #CVE-2026-94639 }

CVE-2026-94639 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94639) [\[CVE json\]](./CVE-2026-94639.cve.json) [\[OSV json\]](./CVE-2026-94639.osv.json)



_Last updated: 2026-10-02T09:33:49.406Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>improper handling of exceptional conditions, Allocation of resources without limits or throttling, Uncaught exception vulnerability in Apache Thrift Java bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/5okpz47dv8hy0s3r6tmrplg3y7jzhhyw


### Credits
* Sylwester Lachiewicz (finder)


## PHP `thrift_protocol` C extension ignores the configured `maxStringSize` ## { #CVE-2026-94638 }

CVE-2026-94638 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94638) [\[CVE json\]](./CVE-2026-94638.cve.json) [\[OSV json\]](./CVE-2026-94638.osv.json)



_Last updated: 2026-10-02T11:49:41.453Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of resources without limits or throttling vulnerability in Apache Thrift PHP bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/v60w786pqr7njzz9425grby8yjrgmbsj


### Credits
* Sylwester Lachiewicz (finder)


## Go `THeaderTransport` does not bound the inflated size of a ZLIB frame ## { #CVE-2026-94637 }

CVE-2026-94637 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94637) [\[CVE json\]](./CVE-2026-94637.cve.json) [\[OSV json\]](./CVE-2026-94637.osv.json)



_Last updated: 2026-10-02T11:49:01.158Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Improper handling of highly compressed data (data amplification) vulnerability in Apache Thrift Go bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/6hxll1jcnod9gfr225tz7my08lpj3jmt


### Credits
* Sylwester Lachiewicz (finder)


## Python `TZlibTransport` stops enforcing its decompressed-size limit once the limit is exactly used up ## { #CVE-2026-94636 }

CVE-2026-94636 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94636) [\[CVE json\]](./CVE-2026-94636.cve.json) [\[OSV json\]](./CVE-2026-94636.osv.json)



_Last updated: 2026-10-02T11:47:52.635Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Improper handling of highly compressed data (data amplification), Function call with incorrectly specified arguments, Improper validation of specified quantity in input vulnerability in Apache Thrift py bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/1rpq0d0g6yzjjzl1z27lwmvhzkn6rbrs


### Credits
* Sylwester Lachiewicz (finder)


## Lua `TBinaryProtocol:readMessageBegin` bypasses `checkStringSize` on the pre-versioned name ## { #CVE-2026-94635 }

CVE-2026-94635 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94635) [\[CVE json\]](./CVE-2026-94635.cve.json) [\[OSV json\]](./CVE-2026-94635.osv.json)



_Last updated: 2026-10-02T09:05:56.419Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of resources without limits or throttling, Improper handling of length parameter inconsistency vulnerability in Apache Thrift Lua bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/ow8994gb5g8ssmmbkbl48xqb0tpvqyr3


### Credits
* Ho1aAs <xxy010605@gmail.com> (finder)


## Python `TJSONProtocol` has a string length limit that is off by default ## { #CVE-2026-94634 }

CVE-2026-94634 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94634) [\[CVE json\]](./CVE-2026-94634.cve.json) [\[OSV json\]](./CVE-2026-94634.osv.json)



_Last updated: 2026-10-02T10:11:18.689Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of resources without limits or throttling, Initialization of a resource with an insecure default vulnerability in Apache Thrift Python bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/dgy8ox9t4bh1xhf74ovf29ht87x7dno4


### Credits
* Ho1aAs <xxy010605@gmail.com> (finder)


## Dart `TBinaryProtocol.readMessageBegin` allocates from the pre-versioned name length ## { #CVE-2026-94633 }

CVE-2026-94633 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-94633) [\[CVE json\]](./CVE-2026-94633.cve.json) [\[OSV json\]](./CVE-2026-94633.osv.json)



_Last updated: 2026-10-02T10:12:57.695Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Memory allocation with excessive size value, Improper handling of length parameter inconsistency vulnerability in Apache Thrift Dart bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/cxkbblyht7988p2o6yvnmd6536qmt88k


### Credits
* Ho1aAs <xxy010605@gmail.com> (finder)
* Sylwester Lachiewicz (finder)


## C++ `THeaderTransport::untransform()` leaks the zlib stream on the error path ## { #CVE-2026-93926 }

CVE-2026-93926 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-93926) [\[CVE json\]](./CVE-2026-93926.cve.json) [\[OSV json\]](./CVE-2026-93926.osv.json)



_Last updated: 2026-10-02T10:14:57.912Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Missing release of memory after effective lifetime, Missing release of resource after effective lifetime vulnerability in Apache Thrift THeaderTransport.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/9353rb8mpoq4ltff88h1j2y3hfy6blgb


### Credits
* glit3h from ZeroVuln Labs (finder)


## C++ `THeaderTransport::writeVarint32()` stack buffer overflow on a negative protocol id ## { #CVE-2026-93925 }

CVE-2026-93925 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-93925) [\[CVE json\]](./CVE-2026-93925.cve.json) [\[OSV json\]](./CVE-2026-93925.osv.json)



_Last updated: 2026-10-02T10:16:09.141Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Stack-based buffer overflow, Incorrect bitwise shift of integer vulnerability in Apache Thrift C++ THeaderProtocol.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.<br></p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/b4rrkrwoyqb9g7hk58d3fx09cbvp1tg9


### Credits
* glit3h from ZeroVuln Labs (finder)


## C++ WebSocket server transport does not read a full request length ## { #CVE-2026-92834 }

CVE-2026-92834 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-92834) [\[CVE json\]](./CVE-2026-92834.cve.json) [\[OSV json\]](./CVE-2026-92834.osv.json)



_Last updated: 2026-10-02T11:45:22.654Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Use of uninitialized resource, Return of wrong status code vulnerability in Apache Thrift C++ WebSocket server.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/bjor9ttx7hk23gzcx60ohz0f20xzvgv0


## PHP `thrift_protocol` accelerator: zero-byte container elements ## { #CVE-2026-91137 }

CVE-2026-91137 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91137) [\[CVE json\]](./CVE-2026-91137.cve.json) [\[OSV json\]](./CVE-2026-91137.osv.json)



_Last updated: 2026-10-02T10:18:34.190Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Improper validation of specified quantity in input, Allocation of resources without limits or throttling, Excessive Iteration vulnerability in Apache Thrift PHP bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/bf12g1b11r4x9x3wsy4mgwfgd0t779h7


### Credits
* glit3h from ZeroVuln Labs (finder)


## C++ `THeaderTransport::transform()` heap buffer overflow (write direction) ## { #CVE-2026-91135 }

CVE-2026-91135 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91135) [\[CVE json\]](./CVE-2026-91135.cve.json) [\[OSV json\]](./CVE-2026-91135.osv.json)



_Last updated: 2026-10-02T10:28:47.666Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Heap-based buffer overflow vulnerability in Apache Thrift C++ THeaderTransport.</p><p>When an application enables the ZLIB transform for the frames it sends, THeaderTransport::transform() copies the compressed frame into the write buffer without making sure it fits. Data that does not compress, such as content a remote peer supplied, grows under compression, so the copy writes past the end of the heap buffer by an amount that grows with the size of the frame, and for large frames it also reads past the end of the transform buffer.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/rbpwlhlxnv2qgyk8cfscp2d2fd3p0ojb


### Credits
* glit3h from ZeroVuln Labs (finder)


## An exception escaping a libevent callback stops the D library's non-blocking server, allowing an unauthenticated remote attacker to deny service ## { #CVE-2026-90440 }

CVE-2026-90440 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90440) [\[CVE json\]](./CVE-2026-90440.cve.json) [\[OSV json\]](./CVE-2026-90440.osv.json)



_Last updated: 2026-10-02T11:44:09.882Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncaught exception, improper handling of exceptional conditions, improper resource shutdown vulnerability in Apache Thrift D thrift.server.nonblocking.TNonblockingServer.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/s8fjltl6c1pkm7vg9v4qkr89b5b74jbg


## PHP `thrift_protocol` accelerator dereferences a missing container-element spec ## { #CVE-2026-87117 }

CVE-2026-87117 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-87117) [\[CVE json\]](./CVE-2026-87117.cve.json) [\[OSV json\]](./CVE-2026-87117.osv.json)



_Last updated: 2026-10-02T11:43:10.120Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>NULL pointer dereference vulnerability in Apache Thrift PHP bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/y05tvpv19ow44j16gtbcy9ht7lb0qjpy


### Credits
* The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Thrift. (finder)


## A truncated HTTP request stops the D library's server, allowing an unauthenticated remote attacker to deny service ## { #CVE-2026-86537 }

CVE-2026-86537 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86537) [\[CVE json\]](./CVE-2026-86537.cve.json) [\[OSV json\]](./CVE-2026-86537.osv.json)



_Last updated: 2026-10-02T11:40:50.109Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncaught exception, Loop with unreachable exit condition ('infinite loop'), Integer underflow (wrap or wraparound) vulnerability in Apache Thrift D language bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/k14jfr1xwc0vtmm2s7xro6lt7q4y6s7m


## A map key from the wire can replace a decoded object's prototype in generated JavaScript ## { #CVE-2026-86536 }

CVE-2026-86536 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86536) [\[CVE json\]](./CVE-2026-86536.cve.json) [\[OSV json\]](./CVE-2026-86536.osv.json)



_Last updated: 2026-10-02T11:39:59.296Z_

### Affected

* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0


### Description

<p>Improperly controlled modification of object prototype attributes ('prototype pollution') vulnerability in Apache Thrift all JS bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0 and re-generate JS code, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/xckvfky30kdnk8vqnhy0wndthvc9nymp


### Credits
* The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Thrift. (finder)


## A JSON member name can stall the Node server's event loop indefinitely ## { #CVE-2026-86535 }

CVE-2026-86535 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86535) [\[CVE json\]](./CVE-2026-86535.cve.json) [\[OSV json\]](./CVE-2026-86535.osv.json)



_Last updated: 2026-10-02T11:38:14.489Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Loop with unreachable exit condition ('infinite loop'), Improperly controlled modification of object prototype attributes ('prototype pollution') vulnerability in Apache Thrift NodeJS bindings with TJSONProtocol.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/94cvvzzl0rh707bn2j4zt844v547508g


### Credits
* The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Thrift. (finder)


## Framed transport and binary protocol size read buffers from a peer-declared length without a limit (multi-language) ## { #CVE-2026-85494 }

CVE-2026-85494 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-85494) [\[CVE json\]](./CVE-2026-85494.cve.json) [\[OSV json\]](./CVE-2026-85494.osv.json)



_Last updated: 2026-10-02T10:42:42.564Z_

### Affected

* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0


### Description

<p>Improper handling of length parameter inconsistency, Uncaught exception, Inefficient Algorithmic Complexity, Memory allocation with excessive size value, Initialization of a resource with an insecure default vulnerability in Apache Thrift Python, Ruby, Erlang, Lua, Dart, JavaME, Perl, PHP and D language bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/rm0m34gt6fh1flvt16wty559hfg191qr


### Credits
* Ho1aAs <xxy010605@gmail.com> for py, rb, erl, lua, dart, javame, d bindings (finder)
* Perl/PHP bindings were found by the Apache Thrift project's own cross-language sweep (finder)
* The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Thrift. (finder)


## TProtocolUtil.skip follows peer-chosen nesting to any depth the stack allows (Dart, Java ME) ## { #CVE-2026-85493 }

CVE-2026-85493 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-85493) [\[CVE json\]](./CVE-2026-85493.cve.json) [\[OSV json\]](./CVE-2026-85493.osv.json)



_Last updated: 2026-10-02T10:45:55.375Z_

### Affected

* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0


### Description

<p>Uncontrolled Recursion vulnerability in Apache Thrift Dart and Java ME bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/oqr0h2k1cg9hho3oh8trmovmxc04fl5m


### Credits
* Ho1aAs <xxy010605@gmail.com> (finder)


## c_glib TZlibTransport reports a full read after a premature stream end ## { #CVE-2026-85483 }

CVE-2026-85483 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-85483) [\[CVE json\]](./CVE-2026-85483.cve.json) [\[OSV json\]](./CVE-2026-85483.osv.json)



_Last updated: 2026-10-02T10:46:53.193Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Use of uninitialized resource, Return of wrong status code vulnerability in Apache Thrift c_glib bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/ro1y0ckzfzcc45yk9qkt1p6t4g2jvrfy


### Credits
* Ho1aAs <xxy010605@gmail.com> (finder)
* The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Thrift. (finder)


## c_glib `read_all` spins when the underlying read returns 0 ## { #CVE-2026-85476 }

CVE-2026-85476 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-85476) [\[CVE json\]](./CVE-2026-85476.cve.json) [\[OSV json\]](./CVE-2026-85476.osv.json)



_Last updated: 2026-10-02T12:12:37.604Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Loop with unreachable exit condition ('infinite loop') vulnerability in Apache Thrift c_glib bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/1zdvscq7p3hf3z30s26h4tm9dvljm1jj


### Credits
* Ho1aAs <xxy010605@gmail.com> (finder)


## The C++ and D clients fall back to the certificate Common Name when subjectAltName entries are present but do not match ## { #CVE-2026-85088 }

CVE-2026-85088 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-85088) [\[CVE json\]](./CVE-2026-85088.cve.json) [\[OSV json\]](./CVE-2026-85088.osv.json)



_Last updated: 2026-10-02T11:37:12.940Z_

### Affected

* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0


### Description

<p>Improper Validation of Certificate with Host Mismatch in the C++ and D libraries of Apache Thrift.
<br>
<br>Both libraries install a default access manager for client sockets — TSSLSocketFactory does so in C++, and the accessManager property does so in D — which compares the peer certificate against the host
<br>name that was connected to. That comparison walks the subjectAltName dNSName entries first and consults the certificate Common Name afterwards. A name that does not match yields a "skip" result rather than
<br>a rejection, so a certificate whose subjectAltName entries are all present and all non-matching falls through to the Common Name, which can then satisfy the check.
<br>
<br>RFC 6125 section 6.4.4, and RFC 9525 section 2, require that the Common Name is not consulted when a dNSName subjectAltName is present. A certificate carrying subjectAltName entries for one name and a
<br>Common Name for another is therefore accepted for a connection to the second name.
<br>
<br>Exploitation requires an attacker positioned on the network path who holds a certificate that chains to a certificate authority in the client's trust store and whose Common Name matches the connected host
<br>name. Public certificate authorities have not issued on Common Name alone for many years, so this is principally a concern for deployments using a private or enterprise public-key infrastructure.
<br>
<br>This issue affects the C++ library of Apache Thrift from 0.7.0 through 0.24.0 and the D library from 0.9.0 through 0.24.0. Users should upgrade to 0.25.0.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/zcgm7lx6037lvgvn87rc1tj3p0zhv371


### Credits
* The ASF — found using Claude agents to study the security of open-source projects, validated and reported by Apache Thrift. (finder)


## Python ≥3.12 host-name check silently becomes a no-op ## { #CVE-2026-85087 }

CVE-2026-85087 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-85087) [\[CVE json\]](./CVE-2026-85087.cve.json) [\[OSV json\]](./CVE-2026-85087.osv.json)



_Last updated: 2026-10-02T11:35:42.674Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Improper certificate validation, Return of wrong status code vulnerability in Apache Thrift python bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/l2rgp3dqhpy2w347forzdt9g7o2d6k0d


### Credits
* The ASF — found using Claude agents to study the security of open-source projects, validated and reported by Apache Thrift. (finder)


## Perl TLS client disables certificate verification by default ## { #CVE-2026-85086 }

CVE-2026-85086 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-85086) [\[CVE json\]](./CVE-2026-85086.cve.json) [\[OSV json\]](./CVE-2026-85086.osv.json)



_Last updated: 2026-10-02T11:33:58.761Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Improper certificate validation, Initialization of a resource with an insecure default vulnerability in Apache Thrift perl bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/c7f9g4027ok0gocyso2y84r2mhgc2xmy


### Credits
* The ASF — found using Claude agents to study the security of open-source projects, validated and reported by Apache Thrift (finder)


## WebSocket frame decoders allocate the payload buffer from the declared length, not the bytes received (Node.js, D) ## { #CVE-2026-83745 }

CVE-2026-83745 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-83745) [\[CVE json\]](./CVE-2026-83745.cve.json) [\[OSV json\]](./CVE-2026-83745.osv.json)



_Last updated: 2026-10-02T12:16:12.360Z_

### Affected

* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0


### Description

<p>Memory allocation with excessive size value, Improper handling of length parameter inconsistency vulnerability in Apache Thrift&nbsp;
nodejs and D lang bindings.<br><br>Both bindings' WebSocket server transports read the payload length out of the&nbsp;frame header and allocate that many bytes immediately, without checking that the&nbsp;bytes have arrived. A single ~14-byte frame therefore commits as much memory as it cares to declare -- measured at 513 MiB against the Node.js server and 2 GiB against the D transport -- and in the Node.js case the connection is left open afterwards, so the frame can simply be sent again.<br></p><p>This issue affects Apache Thrift before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/64y7f0b89mnq4xoqcn4h26to8kskolgc


### Credits
* Ho1aAs <xxy010605@gmail.com> for Node.js (finder)
* Apache Thrift Developers for D language (finder)


## TFramedTransport and THeaderTransport re-enter Read once per frame that carries no payload (Go) ## { #CVE-2026-83663 }

CVE-2026-83663 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-83663) [\[CVE json\]](./CVE-2026-83663.cve.json) [\[OSV json\]](./CVE-2026-83663.osv.json)



_Last updated: 2026-10-02T12:18:15.518Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Uncontrolled Recursion vulnerability in Apache Thrift go bindings.</p><p>Both Go transports satisfy a read out of a buffered frame and, when that frame&nbsp;yields no payload bytes, read the next frame and call `Read` again instead of&nbsp;looping. A peer produces such a frame for 4 bytes in `TFramedTransport` (a&nbsp;declared size of zero) or 18 bytes in `THeaderTransport` (a header block that&nbsp;fills the frame), so nothing bounds the depth. The Go stack limit is reached as&nbsp;a `fatal error`, which `recover()` cannot catch, so the whole process dies.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/yjz317wq7h86q9k8ws6ton0ojgl8hjct


### Credits
* Ho1aAs <xxy010605@gmail.com> for TFramedTransport (finder)
* Apache Thrift Developers for THeaderTransport (finder)


## C++ THttpTransport grows its line buffer without bound ## { #CVE-2026-83632 }

CVE-2026-83632 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-83632) [\[CVE json\]](./CVE-2026-83632.cve.json) [\[OSV json\]](./CVE-2026-83632.osv.json)



_Last updated: 2026-10-02T12:22:22.014Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of resources without limits or throttling, Integer overflow or wraparound, Heap-based buffer overflow vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/zjv6hjmhl4tb4l4l1dk4bmc2whxh0lb4


### Credits
* Ho1aAs <xxy010605@gmail.com> (finder)
* The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Thrift. (finder)


## Integer underflow in C++ THeaderTransport allows an unauthenticated remote peer to terminate a 32-bit process ## { #CVE-2026-82459 }

CVE-2026-82459 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82459) [\[CVE json\]](./CVE-2026-82459.cve.json) [\[OSV json\]](./CVE-2026-82459.osv.json)



_Last updated: 2026-10-02T11:32:28.180Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Integer underflow (wrap or wraparound), Out-of-bounds write vulnerability in Apache Thrift C++ 32 bit THeaderTransport.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/zf8ppfpl6nqhp53sxnz6osnjw93g9fw2


### Credits
* The ASF -- found using Claude agents to study the security of open-source projects, validated and reported by Apache Thrift (finder)


## Container element count not bounded by the bytes available ## { #CVE-2026-82458 }

CVE-2026-82458 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82458) [\[CVE json\]](./CVE-2026-82458.cve.json) [\[OSV json\]](./CVE-2026-82458.osv.json)



_Last updated: 2026-10-02T11:30:13.881Z_

### Affected

* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0


### Description

<p>Memory allocation with excessive size value, Allocation of resources without limits or throttling vulnerability in Apache Thrift Go,&nbsp;netstd, OCaml, Erlang, JavaME,&nbsp;Rust, C++, Java,&nbsp;Kotlin and&nbsp;D language bindings.<br></p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/7xqf651pvjykw0xr9vw0ooz0bwx7wzy7


### Credits
* denyspakizh-tob (Trail of Bits) for the Go bindings (finder)
* David Walker (Workiva, Inc) independent co-discoverer (finder)
* Ho1aAs <xxy010605@gmail.com> independent rediscovery (Go THeaderTransport transform count) (finder)
* Apache Thrift Developers (finder)


## c_glib multiplexed processor crashes on a message it cannot route ## { #CVE-2026-66859 }

CVE-2026-66859 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66859) [\[CVE json\]](./CVE-2026-66859.cve.json) [\[OSV json\]](./CVE-2026-66859.osv.json)



_Last updated: 2026-10-02T12:23:46.689Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>NULL Pointer Dereference, Use of Uninitialized Variable vulnerability in Apache Thrift c_glib bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/n9rogg2166hl9y4ycq5njpvnxndr8y5o


## skip() does not apply the recursion limit (Python accelerator, PHP, Perl, Lua, Smalltalk, OCaml) ## { #CVE-2026-66858 }

CVE-2026-66858 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66858) [\[CVE json\]](./CVE-2026-66858.cve.json) [\[OSV json\]](./CVE-2026-66858.osv.json)



_Last updated: 2026-10-02T12:27:29.550Z_

### Affected

* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0


### Description

<p>The protocol skip routine in several Apache Thrift bindings did not apply the binding's recursion limit, so a message that nests unknown fields deeply enough can exhaust the stack. Affected: the Python C++ accelerator (the pure-Python protocols are not affected), the PHP library and its thrift_protocol extension, and the Perl, Lua, Smalltalk and OCaml libraries.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/6kl6g40tpl8zt3opd8fwn6bsgyddzhd5


### Credits
* Claude (Anthropic Research) (finder)
* Arthur Chan, Ada Logics (analyst)
* Apache Thrift Developers (finder)


## PHP accelerator sizes a stack buffer from a wire-controlled string length ## { #CVE-2026-66837 }

CVE-2026-66837 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66837) [\[CVE json\]](./CVE-2026-66837.cve.json) [\[OSV json\]](./CVE-2026-66837.osv.json)



_Last updated: 2026-10-02T12:29:07.376Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Stack-based Buffer Overflow, Integer Overflow or Wraparound vulnerability in Apache Thrift php bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/7o985t84551tpo55v6fsd3g42gs3zps1


### Credits
* Claude (Anthropic Research) (finder)
* Arthur Chan, Ada Logics (arthur.chan@adalogics.com) (analyst)


## Buffered transport reads are not accounted against MaxMessageSize ## { #CVE-2026-66331 }

CVE-2026-66331 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66331) [\[CVE json\]](./CVE-2026-66331.cve.json) [\[OSV json\]](./CVE-2026-66331.osv.json)



_Last updated: 2026-10-02T12:32:44.751Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of Resources Without Limits or Throttling vulnerability in Apache Thrift Delphi bindings buffered transport.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.<br></p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/971572orz86jdwlg58wqv8o50oqqb143


## c_glib read_message_begin leaves output parameters unset for non-versioned messages ## { #CVE-2026-66081 }

CVE-2026-66081 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66081) [\[CVE json\]](./CVE-2026-66081.cve.json) [\[OSV json\]](./CVE-2026-66081.osv.json)



_Last updated: 2026-10-02T12:33:12.312Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Access of Uninitialized Pointer vulnerability in Apache Thrift c_glib bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/9d51ygo6hrsdo5ndwckbwt3mnp290m57


### Credits
* Akhil Koul (finder)
* Claude (Anthropic Research) (finder)
* Arthur Chan, Ada Logics (arthur.chan@adalogics.com) (analyst)


## TJSONProtocol accepts a single JSON string/number exceeding the configured size limit (multi-language) ## { #CVE-2026-66055 }

CVE-2026-66055 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66055) [\[CVE json\]](./CVE-2026-66055.cve.json) [\[OSV json\]](./CVE-2026-66055.osv.json)



_Last updated: 2026-10-02T12:49:39.024Z_

### Affected

* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0
* Apache Thrift before 0.25.0


### Description

<p>Allocation of Resources Without Limits or Throttling vulnerability in Apache Thrift C++, Java, Go, netstd, Python and Delphi bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/nxlmlhgsh7fwr4mo1fkhtkw3v266qhcx


### Credits
* Bin Luo, University of Electronic Science and Technology of China (UESTC) (C++) (finder)
* Apache Thrift Developers (Java/Go/netstd/Python/Delphi) (finder)


## C++ THeaderTransport does not enforce configured maxFrameSize ## { #CVE-2026-66054 }

CVE-2026-66054 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66054) [\[CVE json\]](./CVE-2026-66054.cve.json) [\[OSV json\]](./CVE-2026-66054.osv.json)



_Last updated: 2026-10-02T12:51:20.441Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of Resources Without Limits or Throttling, Improper Handling of Highly Compressed Data (Data Amplification) vulnerability in Apache Thrift C++ bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/7c23sgowkb3ssmolqofqsn8wzsddvf33


### Credits
* Bin Luo, University of Electronic Science and Technology of China (UESTC) (finder)


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


## Unauthenticated single-packet crash of Go Thrift servers via the THeader transform count ## { #CVE-2026-63772 }

CVE-2026-63772 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-63772) [\[CVE json\]](./CVE-2026-63772.cve.json) [\[OSV json\]](./CVE-2026-63772.osv.json)



_Last updated: 2026-10-02T12:52:05.727Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of Resources Without Limits or Throttling vulnerability in Apache Thrift go bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/6kpzdw29gsfxptv4b65y9s6f42tdyo8k


### Credits
* Anthropic (agentic research) + Ada Logics; reported by Adam Korczynski (finder)


## Java TSaslTransport post-auth data-frame missing size limit ## { #CVE-2026-61374 }

CVE-2026-61374 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-61374) [\[CVE json\]](./CVE-2026-61374.cve.json) [\[OSV json\]](./CVE-2026-61374.osv.json)



_Last updated: 2026-10-02T12:52:58.028Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of Resources Without Limits or Throttling vulnerability in Apache Thrift Java bindings.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/35831rngzrqky1gvc32t06psgq1b8441


### Credits
* 周雪松 / Xuesong Zhou (xuesong.zhou@qingteng.cn), 73Lab of Qingteng.cn (finder)
* n0mi1k (finder)


## Java TSaslNonblockingServer pre-auth unbounded SASL frame allocation ## { #CVE-2026-61373 }

CVE-2026-61373 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-61373) [\[CVE json\]](./CVE-2026-61373.cve.json) [\[OSV json\]](./CVE-2026-61373.osv.json)



_Last updated: 2026-10-02T11:07:26.862Z_

### Affected

* Apache Thrift before 0.25.0


### Description

<p>Allocation of Resources Without Limits or Throttling vulnerability in Apache Thrift Java TSaslNonblockingServer.</p><p>This issue affects Apache Thrift: before 0.25.0.</p><p>Users are recommended to upgrade to version 0.25.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/33otcgbqd27wf6qq810q56znzbomnhg1
* https://lists.apache.org/thread/shy1rrm2g383wlbdb2p7w19c868ntdjp


### Credits
* Claude (Anthropic Research) (finder)
* Arthur Chan, Ada Logics (arthur.chan@adalogics.com) (reporter)
* n0mi1k (finder)


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


### Credits
* sec-reports@outlook.com (finder)


## TSSLTransportFactory.java hostname verification ## { #CVE-2026-43869 }

CVE-2026-43869 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43869) [\[CVE json\]](./CVE-2026-43869.cve.json) [\[OSV json\]](./CVE-2026-43869.osv.json)



_Last updated: 2026-08-01T15:15:50.815Z_

### Affected

* Apache Thrift before 0.23.0


### Description

<p>Improper Validation of Certificate with Host Mismatch vulnerability in Apache Thrift.</p><p>This issue affects Apache Thrift: before 0.23.0.</p><p>Users are recommended to upgrade to version 0.23.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/3hsgl1b69wzq3ry39scqbv2dhyl3j52r


### Credits
* sec-reports@outlook.com (finder)


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



_Last updated: 2026-09-14T21:15:42.689Z_

### Affected

* Apache Thrift before 0.24.0


### Description

<p>Improper Handling of Highly Compressed Data (Data Amplification) vulnerability in Apache Thrift Python bindings.</p><p>This issue affects Apache Thrift: before 0.24.0.</p><p>Users are recommended to upgrade to version 0.24.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7v3jhgwfbmhx42424phydlnzb109g8b9
* https://lists.apache.org/thread/vwsbcwqdpwdtp8qkjo11ol6rodbfm21f


### Credits
* sec-reports@outlook.com (finder)


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
