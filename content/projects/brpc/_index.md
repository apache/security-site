---
title: Apache bRPC security advisories
description: Security information for Apache bRPC
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache bRPC? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=bRPC).

You can read more about the security policy on:

- [Apache bRPC security model](https://github.com/apache/brpc/blob/master/THREAT_MODEL.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Null pointer dereference in MySQL reply parser leading to client crash ## { #CVE-2026-90484 }

CVE-2026-90484 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90484) [\[CVE json\]](./CVE-2026-90484.cve.json) [\[OSV json\]](./CVE-2026-90484.osv.json)



_Last updated: 2026-10-21T12:19:33.574Z_

### Affected

* Apache bRPC from <= 1.11.0 before 1.18.0


### Description

<p>The MySQL client response parser in Apache bRPC dereferences a null pointer when the server peer sends a zero-payload-length response packet. A response packet whose declared payload length is zero is accepted by the frame-length check (is_full_package), after which the parser reads the response type byte via an unbounded 5-byte fetch that returns nullptr, and type = p[4] dereferences it, crashing the client process.</p><p>Root Cause: In brpc::policy::MysqlReply::ConsumePartialIOBuf, buf.fetch(header, 5) returns nullptr when the buffered data only holds the 4-byte header of a zero-length packet, then the code reads p[4] (and, in the fast-auth path, p2[4]) without checking for a null or zero-length packet.</p><p>Affected Scenarios: A brpc MySQL client connecting to a malicious or compromised MySQL server (or a MITM) can be crashed by a zero-length server response packet, resulting in denial of service of the client.</p><p>Fix: The fix rejects zero-length response packets (returning PARSE_ERROR_ABSOLUTELY_WRONG) both for the initial response type determination and after a fast-auth marker, before reading the type byte. Upgrade to the Apache bRPC version 1.18.0 or apply the PR patch at https://github.com/apache/brpc/pull/3536.</p>

### References
* https://github.com/apache/brpc/pull/3536
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


## Out-of-bounds read via non-object fields in Discovery naming-service reply parsing ## { #CVE-2026-87849 }

CVE-2026-87849 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-87849) [\[CVE json\]](./CVE-2026-87849.cve.json) [\[OSV json\]](./CVE-2026-87849.osv.json)



_Last updated: 2026-10-21T12:18:25.626Z_

### Affected

* Apache bRPC before 1.18.0


### Description

<pre>The Discovery naming-service reply parser in Apache bRPC (versions &lt; 1.18.0) calls RapidJSON object-only accessors (FindMember) on JSON values without first validating that those values are objects. A malformed Discovery response whose data/service members or instances list contain non-object entries (e.g. a bare integer) triggers the RapidJSON object-access precondition on the client, reading memory out of bounds and potentially crashing the bRPC client.<br><br>Root Cause:<br>In src/brpc/policy/discovery_naming_service.cpp, DiscoveryNamingService::GetServers() and DiscoveryNames::ListDiscoveryNodes() access JSON values with member functions on non-object values. RapidJSON only defines these operations for object types; invoking them on a non-object violates the class invariant and results in undefined behavior (out-of-bounds read), commonly crashing the process.<br><br>Affected Scenarios: <br>An operator-configured (or compromised) Discovery backend returns a malformed /discovery/nodes or /discovery/fetchs response whose data/service/instance entries are not JSON objects, crashing any bRPC client that refreshes its server list.<br><br>How to Fix:<br>1. Upgrade bRPC to version 1.18.0 or later, which fixes this issue.<br>2. Apply this patch: https://github.com/apache/brpc/pull/3533<br><br>The fix validates that the Discovery response data, per-service data, and instance entries are JSON objects (and skips non-object node/instance entries and rejects non-object data/service values) before calling member accessors.</pre>

### References
* https://github.com/apache/brpc/pull/3533
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Authentication bypass when a server sets ServerOptions.internal_port and ServerOptions.auth ## { #CVE-2026-86249 }

CVE-2026-86249 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86249) [\[CVE json\]](./CVE-2026-86249.cve.json) [\[OSV json\]](./CVE-2026-86249.osv.json)



_Last updated: 2026-10-21T12:17:38.765Z_

### Affected

* Apache bRPC before 1.18.0


### Description

<p>On a brpc::Server that sets both ServerOptions.auth and ServerOptions.internal_port, the HTTP built-in service exemption on internal_port can be abused to bypass authentication entirely. VerifyHttpRequest() returns true without checking any credential when a built-in service is requested on internal_port, and this verdict is not per - request: verification runs only for the first message of a connection and the result latches the connection. Sending a request such as GET /status to internal_port first authenticates the whole connection, after which every subsequent request dispatched on the same connection is handled without ever calling VerifyHttpRequest(). This lets a remote attacker reach ordinary (non-built-in, non-tabbed) authenticated services without supplying valid credentials whenever the server uses ServerOptions.internal_port together with an Authenticator. The fix restricts internal_port so that it carries only built-in and Tabbed services; requests for ordinary services sent to internal_port are rejected with EPREM / HTTP 403.&nbsp;</p><p>Mitigation / Fix: upgrade to 1.18.0 or apply PR https://github.com/apache/brpc/pull/3525 .&nbsp;</p><p>Users who rely on serving normal services on internal_port must move those requests to the port passed to Server::Start().</p>

### References
* https://github.com/apache/brpc/pulls/3525
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


## Arbitrary file creation/truncation via /flags and unbounded profiling duration via /pprof ## { #CVE-2026-86147 }

CVE-2026-86147 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86147) [\[CVE json\]](./CVE-2026-86147.cve.json) [\[OSV json\]](./CVE-2026-86147.osv.json)



_Last updated: 2026-10-21T12:16:19.138Z_

### Affected

* Apache bRPC before 1.18.0


### Description

External control of file name or path and uncontrolled resource consumption in Apache bRPC (version &lt; 1.18.0) on all platforms allows remote attackers who can reach the builtin service port to create directories and truncate/overwrite files with the privileges of the server process, or to hold the process-wide CPU/contention profiler for an arbitrarily long time.<br><br>Root Cause:<br>1. The builtin /flags service allows gflags carrying a validator to be modified at runtime via ?setvalue=. The bvar/mbvar dump path gflags (bvar_dump_file, bvar_dump_tabs, mbvar_dump_file) were registered with an accept-anything validator whose only purpose was to wake the dumping thread. A remote attacker could therefore repoint the dump path (e.g. GET /flags/bvar_dump_file?setvalue=/victim/dir/target followed by GET /flags/bvar_dump?setvalue=true, or the equivalent for mbvar_dump_file, which is used verbatim without a forced suffix), making the dumping thread recursively create directories and open/truncate files at attacker-chosen locations. Tab names in bvar_dump_tabs were appended to the path without sanitization, allowing '..' to escape the configured directory.<br>2. The /pprof builtin service did not clamp the ?seconds= parameter to FLAGS_max_profiling_seconds (a limit that /hotspots enforced). A single request such as ?seconds=2147483647 made the handler sleep for decades while holding the process-wide gperftools CPU profiler or bthread contention profiler, so /hotspots/cpu and /hotspots/contention returned 503 for everyone else during that time.<br><br>Affected Scenarios:<br>Any Apache bRPC server exposing the builtin services (enabled by default on the same port as normal RPC traffic) to untrusted networks.<br><br>How to Fix:<br>(<span>Choose one of the following options)</span><br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br><span>2. Apply this patch: </span><a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3523">https://github.com/apache/brpc/pull/3523</a><br><br>Note:<br>After the fix, bvar_dump_file, bvar_dump_tabs and mbvar_dump_file can no longer be modified at runtime through the /flags builtin service. They can still be changed programmatically via google::SetCommandLineOption(), taking effect on the next dump cycle. The profiling duration of /pprof is now capped by the -max_profiling_seconds gflag (default 300 seconds), which can be adjusted by the server owner.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


## HTTP Request Smuggling and Header Injection via Lenient HTTP/1.1 Header Parsing ## { #CVE-2026-86146 }

CVE-2026-86146 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86146) [\[CVE json\]](./CVE-2026-86146.cve.json) [\[OSV json\]](./CVE-2026-86146.osv.json)



_Last updated: 2026-10-21T12:15:24.502Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Inconsistent interpretation of HTTP requests (HTTP request/response smuggling) in the bundled HTTP/1.1 parser of Apache bRPC (version &lt; 1.18.0) on all platforms allows remote attackers to smuggle requests and inject headers when bRPC is deployed behind a proxy or load balancer that parses the same bytes differently.<br><br>Root Cause:<br>The bRPC fork of http-parser accepts and acts on several HTTP/1.1 header forms that a conforming front-end either rejects or interprets differently, so the framing or the header set of a message can differ between the front-end and bRPC:<br>1. A space before the colon of framing headers (e.g. <code>Content-Length : 5</code>) is accepted; the value still drives bRPC's framing while the reported field name contains the trailing space.<br>2. Interior spaces inside a <code>Content-Length</code> value (e.g. <code>Content-Length: 1 3</code>) are skipped, so bRPC reads 13 where a front-end reads 1 or rejects the message (same class as CVE-2022-32213 in Node.js).<br>3. Obsolete line folding (obs-fold, RFC 7230 3.2.4) of <code>Content-Length</code> and <code>Transfer-Encoding</code> values is accepted, so a folded framing value drives bRPC's framing while a front-end that does not unfold sees a different message.<br>4. Chunked trailer fields are fed to the same header callbacks as the header section and are merged into the header map like real headers. A front-end only inspects the header section, so any chunked request can smuggle fields such as <code>Authorization</code> or <code>X-Forwarded-For</code> past it.<br>5. <code>Transfer-Encoding</code> lists with optional whitespace after a comma (e.g. <code>Transfer-Encoding: gzip, chunked</code>) are not recognized as chunked: such requests are rejected, and responses are read until connection close instead of as chunked, causing response desync.<br><br>Affected Scenarios:<br>bRPC server or client communicating over HTTP/1.1 with a front proxy, load balancer, or any peer that parses the message independently. An attacker able to send requests through the front-end can desynchronize the two parsers to smuggle requests, forge headers (e.g. <code>Authorization</code>, <code>X-Forwarded-For</code>) via chunked trailers, or desynchronize responses.<br><br>How to Fix:<br>(Choose one of the following options)<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3521">https://github.com/apache/brpc/pull/3521</a><br><br>Note:<br>After applying the fix, the four header forms above are rejected by default and chunked trailers are dropped instead of merged into the header map. Two gflags are provided for compatibility: <code>http_allow_obs_fold=true</code> restores acceptance of folded <code>Content-Length</code>/<code>Transfer-Encoding</code> values, and <code>http_strict_header_token=true</code> additionally rejects spaces inside any header field name (not only the ones that decide framing). Legitimate clients that do not use these obsolete forms are unaffected.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Builtin services reachable from the public port via protobuf protocols despite ServerOptions.internal_port configuration ## { #CVE-2026-84748 }

CVE-2026-84748 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-84748) [\[CVE json\]](./CVE-2026-84748.cve.json) [\[OSV json\]](./CVE-2026-84748.osv.json)



_Last updated: 2026-10-21T12:14:24.490Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Improper authorization in Apache bRPC (versions &lt; 1.18.0) on all platforms allows remote attackers to access builtin services through the public port.<br><br>Root Cause:<br>ServerOptions.internal_port is documented to make builtin services (and Tabbed services) reachable only from the internal port, and the HTTP/h2 dispatch path enforced this. However, all protobuf-based protocol dispatch paths (baidu_std, hulu_pbrpc, sofa_pbrpc, and the nshead-based protocols public_pbrpc, nshead_mcpack, nova_pbrpc and ubrpc2pb) computed the security_mode flag but never enforced it between method resolution and method invocation. Since builtin services share the method map with user services, a client able to reach the public port could invoke builtin services such as brpc.vars or hotspots by name over these pb protocols and disclose sensitive runtime information (metrics, flags, profiler data) that the operator intended to expose only via the internal port.<br><br>Affected Scenarios:<br>Use a bRPC server with ServerOptions.internal_port configured (or with builtin/Tabbed services otherwise expected to be gated by it) while the public port is reachable from an untrusted network and any pb-based protocol is enabled.<br><br>How to Fix: <br>(<span>Choose one of the following options)&nbsp;</span><br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br><span>2. Apply this patch: </span><a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3511">https://github.com/apache/brpc/pull/3511</a>

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Access Control Bypass via HTTP Request Paths Containing Empty Path Segments ## { #CVE-2026-84747 }

CVE-2026-84747 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-84747) [\[CVE json\]](./CVE-2026-84747.cve.json) [\[OSV json\]](./CVE-2026-84747.osv.json)



_Last updated: 2026-10-21T12:13:24.202Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Interpretation conflict in the HTTP protocol implementation in Apache bRPC (version &lt; 1.18.0) on all platforms allows remote attackers to bypass access control rules enforced by a front proxy.<br><br>Root Cause:<br>The method dispatch function FindMethodPropertyByURI() in bRPC's HTTP protocol splits the request path with a string splitter that skips empty fields, so paths containing empty path segments (consecutive slashes), such as //flags, /flags// and /flags//port, are dispatched to the same method as their collapsed form /flags. Per RFC 3986 these are distinct paths. A front proxy that enforces an ACL (e.g. blocking access to builtin services such as /flags) matches the collapsed form only, and therefore forwards the padded literal to the bRPC server, where it is dispatched as if it were the collapsed form. This differential allows //flags?setvalue= to reach a builtin service that /flags is not allowed to reach. Additionally, the HTTP/2 implementation never validated the :path pseudo-header, so requests without a :path, or with a :path that neither begins with '/' nor is the asterisk-form '*', contrary to RFC 9113 section 8.3.1, were not rejected.<br><br>Affected Scenarios:<br>Deployments of Apache bRPC behind a front proxy or gateway that performs access control (ACL) decisions on the literal request path, where the bRPC server accepts HTTP or HTTP/2 traffic from that proxy. In such deployments an attacker can send a path containing empty path segments to reach a resource that the front proxy intended to block.<br><br>How to Fix:<br>(<span>Choose one of the following options)</span><br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br><span>2. Apply this patch: </span><a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3512">https://github.com/apache/brpc/pull/3512</a><br><br>Note:<br>After applying the fix, HTTP and HTTP/2 request paths containing empty path segments (consecutive slashes) are rejected by default, and HTTP/2 :path values that are empty or neither begin with '/' nor equal '*' are rejected. Deployments that depend on the previous lenient behavior can restore it by turning on the gflag -http_allow_empty_path_segments, which is not recommended for servers exposed to untrusted traffic.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Use-After-Free in RTMP Chunk Stream Handling via Abort Message ## { #CVE-2026-84727 }

CVE-2026-84727 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-84727) [\[CVE json\]](./CVE-2026-84727.cve.json) [\[OSV json\]](./CVE-2026-84727.osv.json)



_Last updated: 2026-10-21T12:11:43.687Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Use-after-free in the RTMP protocol implementation in Apache bRPC (version &lt; 1.18.0) on all platforms allows a malicious RTMP peer to crash the process or potentially corrupt memory via a crafted Abort message.<br><br>Root Cause:<br>When processing an RTMP Abort (protocol control message type 2), the RTMP policy implementation deleted the target RtmpChunkStream object. The send path (RtmpUnsentMessage::AppendAndDestroySelf -&gt; RtmpChunkStream::SerializeMessage) runs concurrently on sender threads and dereferences the same RtmpChunkStream object without synchronization. If a remote peer sends an Abort message naming a chunk stream that is concurrently being used to serialize an outgoing message, the stream object is freed while still in use, resulting in a use-after-free. Additionally, deleting the chunk stream discarded its previous message header, so subsequent compressed (type-3) chunk headers on that stream could no longer be decoded.<br><br>Affected Scenarios:<br>Any application using the bRPC RTMP protocol implementation (rtmp policy), either as an RTMP server or as an RTMP client, where the remote endpoint is untrusted. The attacker needs to send an Abort message targeting a chunk stream id that is concurrently used for sending, which can crash the process or lead to memory corruption.<br><br>How to Fix:<br>(<span>Choose one of the following options)</span><br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br><span>2. Apply this patch: </span><a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3515">https://github.com/apache/brpc/pull/3515</a>

### References
* https://github.com/apache/brpc/pull/3515
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


## NULL Pointer Dereference in RTMP createStream Error Path Leading to Remote Denial of Service ## { #CVE-2026-82953 }

CVE-2026-82953 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82953) [\[CVE json\]](./CVE-2026-82953.cve.json) [\[OSV json\]](./CVE-2026-82953.osv.json)



_Last updated: 2026-10-21T12:10:02.258Z_

### Affected

* Apache bRPC before 1.18.0


### Description

NULL pointer dereference in the RTMP protocol implementation in Apache bRPC (version &lt; 1.18.0) on all platforms allows remote attackers to crash the server (denial of service) via a crafted createStream command.<br><br>Root Cause:<br>When an RTMP service rejects a createStream request by returning a null stream from RtmpService::NewStream(), the server sends an error response to the client. If writing this rejection response fails (for example, because the client closes the connection immediately after sending the createStream command), the error-handling path in RtmpChunkStream::OnCreateStream() dereferences the null stream pointer to access stream-&gt;_onfail_id, causing the process to crash.<br><br>Affected Scenarios:<br>Run an Apache bRPC RTMP server whose RtmpService::NewStream() may return null (i.e., the service rejects createStream requests). A remote client that sends a createStream command and then closes the connection before the rejection response is written can crash the server.<br><br>How to Fix:<br>(Choose one of the following options)<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3508">https://github.com/apache/brpc/pull/3508</a>

### References
* https://github.com/apache/brpc/pull/3508
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Race Condition on the Shared Socket Input Buffer in the RDMA Transport Causes Remote Denial of Service ## { #CVE-2026-82942 }

CVE-2026-82942 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82942) [\[CVE json\]](./CVE-2026-82942.cve.json) [\[OSV json\]](./CVE-2026-82942.osv.json)



_Last updated: 2026-10-21T12:07:11.226Z_

### Affected

* Apache bRPC before 1.18.0


### Description

A data race in the RDMA transport of Apache bRPC (versions &lt; 1.18.0) allows a remote client to crash the server process (denial of service) when RDMA is enabled at build time and runtime.<br><br>Root Cause:<br>When a bRPC server negotiates RDMA with a client, the handshake completes on the TCP fd, but the server kept parsing that fd afterwards as if it were still an RPC channel. The TCP-fd input stream and the RDMA QP input stream (driven by CQ events) shared the same Socket::_read_buf, preferred_index and parsing_context without synchronization. In addition, CQ event processing could start while the handshake parsing was still in progress, and the handshake ACK phase could consume bytes belonging to the next protocol. A remote, unauthenticated client that has completed the RDMA handshake can send data on the TCP fd at the same time RDMA messages are being processed, corrupting the shared input buffer and parser state and crashing the server process (CWE-362, availability impact).<br><br>Affected Scenarios:<br>Use a bRPC server with RDMA support enabled (built with BRPC_WITH_RDMA and serving rdma:// / SOCKET_MODE_RDMA sockets) and accept connections from untrusted clients. Deployments without RDMA are not affected.<br><br>How to Fix:<br>(Choose one of the following options)<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3505">https://github.com/apache/brpc/pull/3505</a>

### References
* https://github.com/apache/brpc/issues/3479
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* bzs1118 (finder)


## Reachable Assertion in Socket::OnInputEvent Allows Remote Denial of Service ## { #CVE-2026-82425 }

CVE-2026-82425 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82425) [\[CVE json\]](./CVE-2026-82425.cve.json) [\[OSV json\]](./CVE-2026-82425.osv.json)



_Last updated: 2026-10-21T12:05:02.609Z_

### Affected

* Apache bRPC before 1.18.0


### Description

A reachable assertion in Apache bRPC (version &lt; 1.18.0) on all platforms allows a malicious remote peer to crash the process, resulting in denial of service.<br><br>Root Cause:<br>When a Socket with health checking enabled fails, Socket::WaitAndReset closes its file descriptor while the event dispatcher may still be delivering an input event (EPOLLIN/EVFILT_READ) that was fetched for the just-closed fd. If the health check then succeeds and revives the Socket, Socket::Address succeeds again while the fd is still -1 (the next write reconnects on demand). In that window, Socket::OnInputEvent hits CHECK(!(events &amp; EPOLLIN)) (or the kqueue equivalent) because the Socket is addressable but has no fd. CHECK failures terminate the process when bRPC is built with glog or when the gflag -crash_on_fatal_log is enabled (CHECK always terminates in OFFICIAL_BUILD/NDEBUG builds as well).<br><br>Affected Scenarios:<br>Applications using bRPC clients with health check enabled (-health_check_interval). A malicious remote peer that the client connects to can deliberately abort connections and immediately accept the health check probes, racing connection teardown against health check revival to trigger the assertion and abort the process.<br><br>How to Fix:<br>(Choose one of the following options)<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3510">https://github.com/apache/brpc/pull/3510</a><br><br>Note:<br>After applying the fix, stale input events on a Socket revived without an fd are silently dropped instead of triggering the assertion. No user-visible interface or wire protocol is changed.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* condy0919 (finder)


## Malformed Thrift T_EXCEPTION reply causes process termination in Thrift client ## { #CVE-2026-82231 }

CVE-2026-82231 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82231) [\[CVE json\]](./CVE-2026-82231.cve.json) [\[OSV json\]](./CVE-2026-82231.osv.json)



_Last updated: 2026-10-21T12:04:13.441Z_

### Affected

* Apache bRPC before 1.18.0


### Description

A Thrift client in Apache bRPC (version &lt; 1.18.0, built with WITH_THRIFT which is off by default) can be crashed by the server peer it talks to. When the server returns a T_EXCEPTION reply whose exception struct is malformed, the client decodes it without catching what Apache Thrift throws (TProtocolException, TTransportException or std::length_error). The exception unwinds out of the bthread task function and the process calls std::terminate(), terminating the whole process along with every other in-flight RPC.<br><br>This is the client response path, so the adversary is the server peer, which THREAT_MODEL.md treats as untrusted. It requires a WITH_THRIFT build (off by default).<br><br>How to Fix:<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch:&nbsp;https://github.com/apache/brpc/pull/3500

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Kaixuan Li (finder)


## Stack Exhaustion via Unbounded Recursion in mcpack2pb Parser ## { #CVE-2026-82230 }

CVE-2026-82230 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82230) [\[CVE json\]](./CVE-2026-82230.cve.json) [\[OSV json\]](./CVE-2026-82230.osv.json)



_Last updated: 2026-10-21T12:02:52.863Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Uncontrolled recursion in the mcpack2pb component in Apache bRPC (version &lt; 1.18.0) on all platforms allows remote attackers to make the server crash via sending deeply nested mcpack data.<br><br>Root Cause:<br>The bRPC mcpack2pb parser (used to serve nshead_mcpack / ubrpc / public_pbrpc requests) recursively parses nested objects and arrays without any depth limit. For a protobuf message that references itself (e.g. a repeated message field), the generated parser recurses once per nesting level of the incoming mcpack object. A deeply nested request makes the recursion grow unbounded, overflow the stack and crash the process.<br><br>Affected Scenarios:<br>Use bRPC server with a recursive-schema protobuf message to serve nshead_mcpack / ubrpc / public_pbrpc requests from untrusted network.<br><br>How to Fix:<br>(Choose one of the following options)<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: https://github.com/apache/brpc/pull/3499<br><br>Note:<br>No matter which option you choose, you should know that the fix enforces the documented parsing depth limit MAX_DEPTH (128) on the parse path, the same limit the serializer already applies. If your requests contain mcpack messages nested deeper than 128 levels, the request will be failed after applying the fix.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Kaixuan Li (finder)


## Remote denial of service (crash) via malformed stream feedback frames ## { #CVE-2026-82210 }

CVE-2026-82210 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82210) [\[CVE json\]](./CVE-2026-82210.cve.json) [\[OSV json\]](./CVE-2026-82210.osv.json)



_Last updated: 2026-10-21T12:01:27.110Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Enforceable assertion in the streaming feature of Apache bRPC (version &lt; 1.18.0) on all platforms allows a remote attacker to crash the server process by sending a malformed stream feedback frame.<br><br>Root Cause:<br>When handling FRAME_TYPE_FEEDBACK frames, bRPC calls Stream::SetRemoteConsumed() which contains CHECK(_cur_buf_size &gt; 0) and unconditionally asserts CHECK(buf.IsEmpty()) on the frame payload. A feedback frame that carries an unexpected payload, or a feedback frame received on a stream where flow control is disabled (cur_buf_size == 0), reaches these assertions. On failure, CHECK failures abort the process, allowing an unauthenticated single client (once a stream is established) to terminate the server and cause a denial of service.<br><br>Affected Scenarios:<br>Use bRPC server with the streaming control feature (Stream API) served from untrusted network.<br><br>How to Fix:<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3494">https://github.com/apache/brpc/pull/3494</a><br><br>The fix rejects malformed feedback frames with EPROTO and closes only the affected stream instead of crashing the whole process, and it bounds buffer shrinking so cur_buf_size never drops to 0 while flow control is enabled.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Uncontrolled Resource Consumption via Excessive Streams in a Single RPC Request ## { #CVE-2026-81755 }

CVE-2026-81755 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-81755) [\[CVE json\]](./CVE-2026-81755.cve.json) [\[OSV json\]](./CVE-2026-81755.osv.json)



_Last updated: 2026-10-21T11:58:22.255Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Uncontrolled resource consumption in the streaming RPC component of Apache bRPC (version &lt; 1.18.0) allows a remote attacker to exhaust server memory and cause denial of service by sending a single RPC request that declares an excessive number of streams.<br><br>Root Cause:<br>In the streaming RPC feature, a client can declare multiple streams in one RPC request by putting extra stream identifiers into the repeated field <span>`stream_settings.extra_stream_ids`</span> of the RPC meta. On the server side, <span>`StreamAccept`</span> creates one response stream for every stream identifier declared by the request, without limiting the number of streams accepted in a single RPC. The request body size is only bounded by <span>`max_body_size`</span> (default 64MB), which is enough to carry millions of stream identifiers. Each accepted stream allocates its own bthread execution queue and associated resources, so a single crafted request can make the server create a huge number of streams and exhaust memory, leading to denial of service.<br><br>Affected Scenarios:<br>Use a bRPC server that serves streaming RPC and calls <span>`StreamAccept`</span> to accept streams from untrusted clients.<br><br>How to Fix: <br>(<span>Choose one of the following options)&nbsp;</span><br>1. Upgrade bRPC to the 1.18.0 version.<br><span>2. Apply this patch: </span><a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3493">https://github.com/apache/brpc/pull/3493</a>
<br><br>Note:<br>The fix adds a new gflag <span>`stream_max_streams_per_request`</span> with a default value of 64. Requests declaring more streams than the limit are rejected before any response stream is created. Applications that legitimately need to accept more than 64 streams in one RPC must raise this flag; otherwise such requests will fail after applying the fix.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Unbounded Memory Accumulation in Stream Message Reassembly ## { #CVE-2026-80463 }

CVE-2026-80463 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-80463) [\[CVE json\]](./CVE-2026-80463.cve.json) [\[OSV json\]](./CVE-2026-80463.osv.json)



_Last updated: 2026-10-21T11:57:26.109Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Unbounded memory accumulation in the stream message reassembly path of Apache bRPC (version &lt; 1.18.0) on all platforms allows remote attackers to exhaust the memory of a server (denial of service) by sending an endless sequence of continuation data frames.<br><br>Root Cause:<br>The streaming RPC protocol bounds every single data frame by max_body_size, but a fragmented stream message accumulates continuation frames into one buffer (_pending_buf) without any limit on the accumulated size. A malicious peer that can open a stream can therefore keep sending continuation frames to make the receiver accumulate an arbitrarily large in-memory message. Since the default flow-control settings (socket_max_streams_unconsumed_bytes=0) do not throttle the sending rate, the receiver's memory grows until the process runs out of memory and crashes or becomes unavailable.<br><br>Affected Scenarios:<br>Services that accept streams from untrusted clients (for example using brpc::StreamAccept or brpc::StreamCreate with the built-in streaming protocol) are affected.<br><br><br>How to Fix:<br>(Choose one of the following options)<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3489">https://github.com/apache/brpc/pull/3489</a><br><br><br>Note:<br>The fix limits the accumulated payload of a fragmented stream message to max_body_size (default 64MB). When the accumulated payload exceeds the limit, the pending fragments are released and the stream is closed with error EMSGSIZE. After applying the fix, legitimate fragmented stream messages larger than max_body_size will be rejected; you can adjust the gflag max_body_size to change the limit.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Out-of-bounds Read in Multi-stream RPC Response Handling ## { #CVE-2026-79704 }

CVE-2026-79704 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-79704) [\[CVE json\]](./CVE-2026-79704.cve.json) [\[OSV json\]](./CVE-2026-79704.osv.json)



_Last updated: 2026-10-21T11:56:17.980Z_

### Affected

* Apache bRPC from 1.11.0 before 1.18.0


### Description

An out-of-bounds read vulnerability exists in the streaming RPC client of Apache bRPC (versions 1.11.0 through&nbsp; 1.17.0) on all platforms. A client that creates multiple streams in a single RPC expects the server response to carry exactly one extra_stream_id for every additional stream. The response handling path indexed the returned identifiers using the locally created stream count without first validating the size of the returned list, so a malicious or compromised server (or an on-path attacker) can trigger an out-of-bounds read in the client by returning a malformed StreamSettings response with fewer extra_stream_ids than expected. This may crash the client process (denial of service) or leak unintended memory contents into subsequent stream handling; surplus identifiers have no valid client-stream mapping and are processed inconsistently.<br><br>Root Cause:<br>Since bRPC 1.11.0, a client can create multiple streams in one RPC via batch StreamCreate. The expected behavior is that the server response must return exactly (N-1) extra_stream_ids, where N is the number of locally created streams. In Controller::HandleStreamConnection, the response path reads extra_stream_ids[i-1] for each additional local stream without first comparing the returned list size with (N-1). If the server returns fewer identifiers, the read runs past the end of the returned list (out-of-bounds read); if it returns more, the surplus identifiers have no corresponding client-side stream.<br><br>Affected Scenarios:<br>A bRPC client using multi-stream RPC (creating more than one stream in a single RPC) that connects to an untrusted, malicious, or compromised server or to a server reached through an untrusted network path. The server sends a malformed StreamSettings response to trigger the issue.<br><br><br>How to Fix: <br>(Choose one of the following options)&nbsp;<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3485">https://github.com/apache/brpc/pull/3485</a><br><br><br>Note:<br>The fix makes the client reject responses whose extra_stream_ids count does not exactly match the number of additional client streams. Such mismatched responses now fail the RPC with ERESPONSE and go through the existing stream cleanup path, instead of being partially processed.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Missing Authentication for Streaming RPC Frames ## { #CVE-2026-78334 }

CVE-2026-78334 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-78334) [\[CVE json\]](./CVE-2026-78334.cve.json) [\[OSV json\]](./CVE-2026-78334.osv.json)



_Last updated: 2026-10-21T11:54:18.946Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Missing authentication in the streaming RPC path of Apache bRPC (version &lt; 1.18.0) on all platforms allows a remote attacker to bypass server authentication and inject or deliver streaming frames, when a server is configured with an Authenticator.<br><br>Root Cause:<br>When authentication is configured, streaming RPC frames are consumed directly by the streaming parser (ParseStreamingMessage) and never pass through InputMessenger's authentication hook, so an unauthenticated peer can exchange frames without being authenticated. In addition, a server-accepted stream is bound lazily to the first frame that happens to carry its id, so a stream could accept a frame carrying its id from a socket other than the socket that created the stream.<br><br>Affected Scenarios:<br>A bRPC server configured with authentication that serves streaming RPC from an untrusted network, or a deployment where a foreign connection can impersonate a stream by id, can be made to accept unauthorized streaming frames.<br><br>How to Fix:<br>Upgrade bRPC to 1.18.0, which fixes this issue, or apply the patch in PR https://github.com/apache/brpc/pull/3481. <br><br>Note:<br>The fix rejects streaming frames on server sockets when configured authentication has not completed, and keeps server-accepted streams bound to the socket of their creating RPC and rejects frames arriving from another socket. Authenticated streaming RPC behavior and the wire format are unchanged; only unauthenticated or foreign-socket frames are now rejected.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Resource Exhaustion via Unbounded Decompression and Unvalidated Wire-Declared Sizes ## { #CVE-2026-78066 }

CVE-2026-78066 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-78066) [\[CVE json\]](./CVE-2026-78066.cve.json) [\[OSV json\]](./CVE-2026-78066.osv.json)



_Last updated: 2026-10-21T11:53:37.827Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Resource exhaustion in Apache bRPC (version &lt; 1.18.0) on all platforms: multiple parsers that accept wire-controlled input bound no limit on the sizes declared by the client or on decompressed output, which attackers can use to drive disproportionate memory use and crash the process.<br><br>Root Cause:<br>1) The gzip/zlib/snappy decompressors enforce no output limit: -max_body_size is checked against the compressed bytes only, so a cap-compliant body (e.g.&nbsp;64&nbsp;MiB) can decompress to tens of GiB.<br>2) The AMF string readers allocate the declared length before the bytes are actually available.<br>3) RTMP chunk headers may re-declare a message length mid-stream; the declared length was never bounded and the partial reassembly buffer kept growing.<br>4) The sofa-pbrpc parser does not bound meta_size.<br>5) mcpack2pb trusts wire-declared item counts for Reserve() and a string value_size of 0 underflows the buffer size, aborting the process.<br><br>Affected Scenarios:<br>Any bRPC service accepting gzip/zlib/snappy-compressed bodies or rtmp, sofa-pbrpc, or mcpack2pb messages from untrusted clients.<br><br>How to Fix:<span>(Choose one of the following options)&nbsp;</span><div><span>1. Upgrade bRPC to version 1.18.0, which fixes this issue.</span></div><div><span>2. Apply this patch:&nbsp;</span>https://github.com/apache/brpc/pull/3476<br><br>Note:<br>After the fix, requests whose decompressed size, RTMP message length, or mcpack declared count exceed the new limits are rejected. Operators who legitimately need larger values can raise the corresponding flag (-max_decompressed_body_size, max_body_size).</div>

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Unbounded Resource Consumption and Crash in the HTTP/2 Receive Path ## { #CVE-2026-78058 }

CVE-2026-78058 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-78058) [\[CVE json\]](./CVE-2026-78058.cve.json) [\[OSV json\]](./CVE-2026-78058.osv.json)



_Last updated: 2026-10-21T11:52:50.016Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Uncontrolled resource consumption in the HTTP/2 (h2) receive path of Apache bRPC (version &lt; 1.18.0) on all platforms allows a remote unauthenticated attacker to crash the server or grow its memory without bound by sending crafted HTTP/2 frames.<br><br>Root Cause:<br>The h2 parser, enabled by default on every bRPC server port and used by h2/gRPC clients, trusts the peer to respect receive-side limits that bRPC advertises but never enforces:<br>1. SETTINGS_MAX_CONCURRENT_STREAMS defaulted to unlimited and was never checked on the server, letting a peer pin an unbounded number of pending streams per connection (~100x memory amplification).<br>2. SETTINGS_MAX_HEADER_LIST_SIZE defaulted to unlimited and was never enforced; 1-byte HPACK indexed references amplify a small HEADERS frame ~4000x into an unbounded decoded header list ("HPACK bomb"), and a never-completed HEADERS/CONTINUATION block accumulates memory without limit.<br>3. Control-frame acks (PING/SETTINGS acks, RST_STREAM, GOAWAY, WINDOW_UPDATE) unconditionally bypassed the -socket_max_unwritten_bytes write cap, so a PING flood combined with withheld TCP reads grew the connection buffer without the documented bound.<br>4. The HPACK dynamic table size update was validated against the protocol default (4096) instead of the advertised SETTINGS_HEADER_TABLE_SIZE, which together with the dynamic-table queue/accounting issue can desynchronize the decoder and dereference NULL (crash).<br><br>Affected scenarios:<br>Any bRPC server serving HTTP/h2/gRPC to an untrusted network, and any bRPC h2/gRPC client connecting to an untrusted backend. The h2 parser runs before any Authenticator check on the shared port.<br><br>How to fix: <br>Upgrade bRPC, or apply the patch in https://github.com/apache/brpc/pull/3474.<br><br>Note:<br>After applying the fix the following limits are enforced by default:<br>- max_concurrent_streams: 1024 per connection (4294967295 restores unlimited).<br>- max_header_list_size: 1 MiB decoded size per stream (4294967295 restores unlimited; -h2_client_max_header_list_size for clients).<br>- h2 control-frame acks respect -socket_max_unwritten_bytes (-h2_ack_ignore_eovercrowded restores the old behavior).<br>Requests exceeding these limits are rejected (RST_STREAM(REFUSED_STREAM) or a connection error).

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Claude (finder)


## Remote Denial of Service via Out-of-Bounds Dynamic Table Sizing in HPACK Decoder ## { #CVE-2026-78048 }

CVE-2026-78048 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-78048) [\[CVE json\]](./CVE-2026-78048.cve.json) [\[OSV json\]](./CVE-2026-78048.osv.json)



_Last updated: 2026-10-21T11:51:48.789Z_

### Affected

* Apache bRPC before 1.18.0


### Description

A reachable-assertion flaw in the HPACK header-compression decoder of the HTTP/2 (h2/gRPC) stack in Apache bRPC (version &lt; 1.18.0) on all platforms allows a remote attacker to crash the server process by sending a crafted sequence of HPACK headers, resulting in a denial of service.<br><br>Root Cause:<br>In src/brpc/details/hpack.cpp, IndexTable::Init sizes the dynamic-table ring buffer as num_headers = max_size / (32 + 2), i.e. it assumes a minimum table entry of 34 bytes (name &gt;= 1 byte + value &gt;= 1 byte + 32 bytes of overhead). However, RFC 7541 section 4.1 specifies that the minimum entry size is 33 bytes, because the value may be empty (name &gt;= 1 byte + value == 0 + 32 bytes). For the default 4096-byte table this allocates only 120 slots (4096/34). Eviction in AddHeader is driven by byte usage (_max_size), not by slot count, so a peer can add 121 minimal 33-byte entries (121*33 = 3993 &lt;= 4096) without triggering eviction. The 121st AddHeader then hits CHECK(!_header_queue.full()), which aborts the process.<br><br>Affected Scenarios:<br>Use a bRPC server that serves HTTP/2 or gRPC requests (e.g. via the h2 protocol) from an untrusted network. The malicious header block is processed during HPACK decoding of incoming requests without authentication.<br><br>How to Fix: <br><span>(Choose one of the following options)&nbsp;</span><br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br><span>2. Apply this patch:&nbsp;</span>https://github.com/apache/brpc/pull/3462<br><br>Note:<br>The fix sizes the dynamic table for the 33-byte minimum entry (max_size / (32 + 1)) and ensures at least one ring-buffer slot is kept when max_size is smaller than the minimum entry, so that initialization cannot fail on malloc(0).

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* ubeddulla khan (finder)


## Heap Use-After-Free in RTMP Abort Message Handling ## { #CVE-2026-74758 }

CVE-2026-74758 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-74758) [\[CVE json\]](./CVE-2026-74758.cve.json) [\[OSV json\]](./CVE-2026-74758.osv.json)



_Last updated: 2026-10-21T11:48:19.107Z_

### Affected

* Apache bRPC before 1.18.0


### Description

A heap use-after-free in the RTMP protocol component of Apache bRPC (versions &lt; 1.18.0) allows a remote attacker to crash a bRPC RTMP server by sending a crafted Abort control message. No authentication or application-level request is required.<br><br>Root Cause:<br>When an RTMP Abort control message names the chunk stream that is currently being parsed (the chunk stream carrying the message itself), RtmpChunkStream::OnAbortMessage calls RtmpContext::ClearChunkStream, which deletes the RtmpChunkStream while its Feed() is still running. After the message handler returns, Feed() continues to access members of the deleted object, resulting in a heap-use-after-free.<br><br>Affected Scenarios:<br>bRPC servers that enable RTMP support (ServerOptions.rtmp_service set) and accept connections from untrusted networks.<br><br>How to Fix:<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3452">https://github.com/apache/brpc/pull/3452</a><br><br>The fix skips clearing the chunk stream when the Abort message targets the chunk stream that is currently being parsed.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Feng Zhijie (Dopamine) (finder)


## Uncontrolled Memory Allocation via Malicious mcpack Array Item Count ## { #CVE-2026-74757 }

CVE-2026-74757 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-74757) [\[CVE json\]](./CVE-2026-74757.cve.json) [\[OSV json\]](./CVE-2026-74757.osv.json)



_Last updated: 2026-10-21T11:46:13.134Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Uncontrolled resource allocation in the mcpack2pb component in Apache bRPC (version &lt; 1.18.0) on all platforms allows remote attackers to make the server allocate a large amount of memory via sending a crafted mcpack request with a huge array item count.<br><br>Root Cause:<br>The bRPC&nbsp;mcpack2pb parser trusts the item count stored in the mcpack array header without validating it against the actual payload size. The code generated by the mcpack2pb protoc plugin uses this count to preallocate memory for repeated protobuf fields via Reserve(). A malformed request declaring item_count = 0x7fffffff can force the server to preallocate about 16GB of virtual memory, which may abort the process (SIGABRT) on memory-constrained hosts.<br><br>Affected Scenarios:<br>Use a bRPC server that wires a NsheadService to UbrpcMcpack2Adaptor (the Baidu ubrpc deployment pattern) and parses requests with code generated by the mcpack2pb protoc plugin. The request body is parsed before authentication.<br><br>How to Fix:<br>(Choose one of the following options)<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br><span>2. Apply this patch: </span><a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3451">https://github.com/apache/brpc/pull/3451</a><br><br>Note:<br>No matter which option <span>you choose</span>, you should know that the fix caps the array item count to the remaining bytes of the array payload.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Feng Zhijie (Dopamine) (finder)


## Integer Underflow in mcpack2pb Parser Leading to Denial of Service ## { #CVE-2026-74755 }

CVE-2026-74755 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-74755) [\[CVE json\]](./CVE-2026-74755.cve.json) [\[OSV json\]](./CVE-2026-74755.osv.json)



_Last updated: 2026-10-21T11:45:21.645Z_

### Affected

* Apache bRPC before 1.18.0


### Description

An integer underflow in the mcpack2pb component of Apache bRPC (version &lt; 1.18.0) on all platforms allows remote attackers to crash a bRPC server by sending a request containing a string field with a zero value_size. The UnparsedValue::as_string() function computes `_size - 1` without validating `_size`; when value_size is 0 the expression underflows to SIZE_MAX, resize() throws std::length_error, and because the exception is not caught on the request parsing path the process aborts (SIGABRT).<br><br>Root Cause:<br>In src/mcpack2pb/parser.cpp, UnparsedValue::as_string() resizes the output string to `_size - 1`, where `_size` is the value_size of a string field taken directly from the network data. A value_size of 0 underflows the unsigned size_t, and the subsequent resize() throws an exception that is not caught.<br><br>Affected Scenarios:<br>bRPC servers that accept nshead frames wired to the ubrpc mcpack2 adaptor (for example the NsheadService + UbrpcMcpack2Adaptor deployment pattern) can be crashed by a single unauthenticated request. Stock open-source bRPC registers the ubrpc/nshead_mcpack protocols as client-only, so default server configurations are not affected.<br><br>How to Fix:<br>1. Upgrade bRPC to a version that includes this fix.<br>2. Apply the patch in PR&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3450">https://github.com/apache/brpc/pull/3450</a>&nbsp;

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Feng Zhijie (Independent security researcher) (finder)


## TLS Client Accepts Certificates for Mismatched Peer Names ## { #CVE-2026-66392 }

CVE-2026-66392 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66392) [\[CVE json\]](./CVE-2026-66392.cve.json) [\[OSV json\]](./CVE-2026-66392.osv.json)



_Last updated: 2026-10-21T11:43:48.041Z_

### Affected

* Apache bRPC before 1.18.0


### Description

<div><div>Apache bRPC versions before 1.18.0 validate the server certificate chain when client TLS peer verification is enabled, but do not bind the certificate to an expected DNS name or IP address. A network attacker who can redirect or intercept a connection and who possesses a certificate issued by a CA trusted by the client for another name may impersonate the requested TLS endpoint.</div><br><div>Affected Scenarios:<br>Applications use a bRPC client Channel to connect to an untrusted network with certificate verification enabled and trust a CA that can issue certificates for identities other than the intended endpoint.</div><br><div>How to Fix:<br>Upgrade to Apache bRPC 1.18.0 and enable VERIFY_PEER with a positive verify_depth. HTTPS Channels automatically verify the certificate against the host in the Channel URL. Callers may set VerifyOptions::expected_peer_name explicitly when the certificate identity differs from the URL host. Alternatively, apply the patch from <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3408">https://github.com/apache/brpc/pull/3408</a>.<br><br>Note:<br>The new option performs DNS SAN or IP SAN verification during the TLS handshake. Configurations that set expected_peer_name while peer verification is disabled are rejected.</div></div>

<br>

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* ZenDuk (finder)


## Out-of-bounds Read in URL and Header Lookup Tables on Unsigned-char Platforms ## { #CVE-2026-61916 }

CVE-2026-61916 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-61916) [\[CVE json\]](./CVE-2026-61916.cve.json) [\[OSV json\]](./CVE-2026-61916.osv.json)



_Last updated: 2026-10-21T11:42:40.219Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Out-of-bounds reads in URL parsing and case-insensitive header lookup in Apache bRPC before version 1.18.0 on platforms where plain <code>char</code> is unsigned, such as ARM64, allow remote attackers to cause a process crash and denial of service by sending crafted input containing bytes with the high bit set.<br><br><strong>Root Cause:</strong><br>Two 256-entry lookup tables are accessed through pointers biased by 128 so that valid indices are in the range -128 to 127. Input bytes are promoted from plain <code>char</code> to <code>int</code> without first normalizing them to the signed-char range. On affected platforms, bytes in the range 0x80 to 0xFF therefore become indices 128 to 255 and read up to 127 bytes beyond the end of the underlying tables.<br><br><strong>Affected Scenarios:</strong><br>A remotely accessible bRPC HTTP server on an affected platform can reach the vulnerable URL lookup through an unauthenticated request URI containing a high-bit byte. The case-insensitive lookup is also reachable when untrusted header names are processed through APIs such as the HTTP/2 HPACK path. HTTP/1 header names containing high-bit bytes are rejected by the HTTP/1 parser before reaching the vulnerable lookup. Builds where plain <code>char</code> is signed, which commonly include x86_64 builds, are not affected by this issue.<br><br><strong>How to Fix:</strong><br>Choose one of the following options:<br>1. Upgrade Apache bRPC to version 1.18.0 or later.<br>2. Apply the patch from <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3376">https://github.com/apache/brpc/pull/3376</a>.<br><br>The fix normalizes lookup-table indices to the signed-char range before accessing the biased tables.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Ubeddulla Khan (finder)


## Memory Exhaustion Through Inconsistent Message Body Limits ## { #CVE-2026-61902 }

CVE-2026-61902 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-61902) [\[CVE json\]](./CVE-2026-61902.cve.json) [\[OSV json\]](./CVE-2026-61902.osv.json)



_Last updated: 2026-10-21T11:41:51.065Z_

### Affected

* Apache bRPC before 1.18.0


### Description

<div><div>Apache bRPC versions before 1.18.0 do not consistently enforce the configured max_body_size limit in non-progressive HTTP/1 and HTTP/2 parsing and in memcache and couchbase response parsing.</div><div>A remote unauthenticated peer can cause an affected process to buffer message data beyond the configured limit, which may lead to memory exhaustion and denial of service. <br>Users should upgrade to 1.18.0 or apply the patch from PR <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3382">https://github.com/apache/brpc/pull/3382</a>. The fix rejects oversized buffered HTTP bodies, returns HTTP 413 for HTTP/1 requests, resets oversized HTTP/2 streams, and rejects oversized memcache and couchbase responses from their declared lengths. Progressive HTTP reading remains supported because it uses bounded buffering.</div></div>



### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* BeaCox (finder)


## Denial of Service via Unbounded Redis Inline Command Allocation ## { #CVE-2026-58064 }

CVE-2026-58064 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-58064) [\[CVE json\]](./CVE-2026-58064.cve.json) [\[OSV json\]](./CVE-2026-58064.osv.json)



_Last updated: 2026-10-21T11:41:08.445Z_

### Affected

* Apache bRPC before 1.18.0


### Description

<div><div>The Redis protocol implementation in Apache bRPC allowed inline command parsing to allocate and copy the full connection buffer before a complete CRLF-terminated command was available. A remote attacker with access to a Redis-protocol bRPC service could send long inline inputs without a terminating CRLF to increase memory usage and CPU copy overhead, potentially causing denial of service.</div><br><div>Root Cause:<br>The Redis inline command parser allocated memory based on the current input buffer size and copied the entire buffer before determining the current inline command boundary. The existing redis_max_allocation_size limit was applied to RESP bulk strings and arrays, but not effectively to the inline command path before allocation.</div><br><div>Affected Scenarios:<br>Use Apache bRPC server with Redis protocol enabled and reachable by untrusted clients.</div><br><div>How to Fix:<br>1. Upgrade Apache bRPC to version 1.18.0, which fixes this issue.<br>2. Apply the patch from PR <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3363">https://github.com/apache/brpc/pull/3363</a>.</div><br><div>Note:<br>The fix applies redis_max_allocation_size to Redis inline command lines and scans for CRLF before allocating parser arena memory. Inline command lines exceeding this limit are rejected.</div></div>

<br>

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* 73Lab of Qingteng.cn (finder)


## Out-of-Bounds Write in Redis Command Parser ## { #CVE-2026-56388 }

CVE-2026-56388 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-56388) [\[CVE json\]](./CVE-2026-56388.cve.json) [\[OSV json\]](./CVE-2026-56388.osv.json)



_Last updated: 2026-10-21T11:40:32.499Z_

### Affected

* Apache bRPC before 1.18.0


### Description

The Redis server command parser in Apache bRPC accepts an empty RESP array as a command header. A remote unauthenticated attacker who can reach a bRPC server with Redis service enabled can send an empty array header followed by a bulk string, causing an out-of-bounds write in the parser and crashing the process.<br><br>Root Cause:<br>RedisCommandParser::ConsumeImpl rejected negative RESP array counts but accepted zero. It resized the command argument vector to zero elements and continued parsing. When a following bulk string was parsed, the only index guard was a CHECK. In configurations where fatal logs do not abort immediately, execution could continue and write to _args[0] even though the vector was empty.<br><br>Affected Scenarios:<br>Deployments that enable ServerOptions.redis_service and accept Redis protocol traffic from untrusted clients. The issue is reached during parsing before command handling or authentication.<br><br>How to Fix:<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3354">https://github.com/apache/brpc/pull/3354</a><br><br>Note:<br>The fix rejects empty RESP arrays as invalid Redis commands and replaces the internal index CHECK with an explicit parse error so malformed command streams cannot fall through to an indexed vector write.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Nikko Enggaliano Pratama (finder)


## Remote Memory Exhaustion in RTMP AMF Parser ## { #CVE-2026-56387 }

CVE-2026-56387 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-56387) [\[CVE json\]](./CVE-2026-56387.cve.json) [\[OSV json\]](./CVE-2026-56387.osv.json)



_Last updated: 2026-10-21T11:39:07.076Z_

### Affected

* Apache bRPC before 1.18.0


### Description

The RTMP AMF parser in Apache bRPC accepts AMF string lengths and array counts directly from untrusted input. A remote unauthenticated attacker who can reach a bRPC server with RTMP enabled can send a small AMF payload with an excessive declared long string length or array count, causing excessive memory allocation or resource consumption before the parser rejects the incomplete payload.<br><br>Root Cause:<br>The AMF long string parser resized the destination string to the declared 32-bit length before validating that the stream contained that many bytes. ECMA array and strict array parsers also accepted 32-bit element counts without a configurable upper bound.<br><br>Affected Scenarios:<br>Deployments that enable the bRPC RTMP server component and accept RTMP traffic from untrusted clients. Direct uses of the AMF parser on untrusted data are also affected.<br><br>How to Fix:<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3353">https://github.com/apache/brpc/pull/3353</a><br><br>Note:<br>The fix introduces configurable AMF parsing limits. The default maximum string size is 64 MiB and the default maximum array element count is 1,048,576. Payloads above these limits are rejected. The limits can be adjusted with amf_max_string_size and amf_max_array_size.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Nikko Enggaliano Pratama (finder)
* 73Lab of Qingteng.cn (finder)


## Integer Underflow and Out-of-Bounds Read in HTTP/2 DATA Frame Parser ## { #CVE-2026-56386 }

CVE-2026-56386 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-56386) [\[CVE json\]](./CVE-2026-56386.cve.json) [\[OSV json\]](./CVE-2026-56386.osv.json)



_Last updated: 2026-10-21T11:37:41.065Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Integer underflow and out-of-bounds read in the HTTP/2 server DATA frame parser in Apache bRPC allows an unauthenticated remote attacker to cause denial of service by sending a malformed DATA frame with the PADDED flag set and a zero-length payload.<br><br>Root Cause:<br>The HTTP/2 DATA frame handler computed the fragment size from the attacker-controlled payload length and, when the PADDED flag was present, decremented the fragment size before ensuring that the frame contained the mandatory pad length byte. A zero-length padded DATA frame could therefore underflow the unsigned fragment size and read the pad length byte past the end of the frame buffer.<br><br>Affected Scenarios:<br>Apache bRPC servers that accept HTTP/2 traffic are affected when a remote client can send crafted HTTP/2 frames to the server. HTTP/2 may be reached through cleartext h2c detection on an HTTP port or through TLS ALPN negotiation.<br><br>How to Fix:<br>(Choose one of the following options)<br>1. Upgrade Apache bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3325">https://github.com/apache/brpc/pull/3325</a><br><br>Note:<br>The fix validates that a padded DATA frame has enough payload bytes for the pad length field before decrementing the fragment size or reading the pad length byte. Malformed zero-length padded DATA frames are rejected with HTTP/2 FRAME_SIZE_ERROR.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Nikko Enggaliano Pratama (finder)


## Stack Exhaustion via Unbounded Recursion in AMF Parser ## { #CVE-2026-54427 }

CVE-2026-54427 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-54427) [\[CVE json\]](./CVE-2026-54427.cve.json) [\[OSV json\]](./CVE-2026-54427.osv.json)



_Last updated: 2026-10-21T11:36:35.018Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Uncontrolled recursion in the AMF parser in Apache bRPC &lt; 1.18.0 allows a remote RTMP peer to crash a bRPC process by sending deeply nested AMF objects or arrays. The parser recursively processed nested AMF containers without enforcing a depth limit, which could exhaust the native stack.<br><br>Affected Scenarios:<br>Applications using bRPC RTMP support and parsing AMF data from an untrusted RTMP peer. This includes RTMP servers parsing client command messages, RTMP clients parsing server responses or status messages, and either side parsing inbound AMF script data such as metadata or cue points. Direct callers of ReadAMFObject or ReadAMFArray on untrusted input are also affected.<br><br>How to Fix:<br>1. Upgrade Apache bRPC to 1.18.0.<br>2. Apply the patch from PR <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3344">https://github.com/apache/brpc/pull/3344</a>.<br><br>Note:<br>The fix introduces a configurable AMF nesting depth limit with default value 128. AMF objects or arrays deeper than amf_max_depth are rejected after applying the fix.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


## Stack Exhaustion via Unbounded Recursion in Redis Reply Parser ## { #CVE-2026-54426 }

CVE-2026-54426 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-54426) [\[CVE json\]](./CVE-2026-54426.cve.json) [\[OSV json\]](./CVE-2026-54426.osv.json)



_Last updated: 2026-10-21T11:32:15.221Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Uncontrolled recursion in the Redis reply parser in Apache bRPC &lt; 1.18.0 allows a remote Redis server peer to crash a bRPC Redis client process by returning a deeply nested RESP array reply. The parser recursed once for each nested array level without enforcing a depth limit. The fix adds a configurable Redis reply depth limit with default value 128 and rejects replies exceeding that limit.&nbsp;<br><br>Affected Scenarios:<br>Applications using bRPC as a Redis client with ChannelOptions.protocol="redis" and receiving replies from an untrusted or faulty Redis server peer.<br><br>How to Fix:<br>1. Upgrade Apache bRPC to 1.18.0.<br>2. Apply the patch from PR <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3344">https://github.com/apache/brpc/pull/3344</a>.<br><br>Note:<br>After applying the fix, Redis replies with array nesting deeper than redis_max_reply_depth are rejected.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Nikko Enggaliano Pratama (nikkoenggaliano@gmail.com) on Github (finder)


## Stack Exhaustion via Recursive HPACK Dynamic Table Size Update Decoding ## { #CVE-2026-54425 }

CVE-2026-54425 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-54425) [\[CVE json\]](./CVE-2026-54425.cve.json) [\[OSV json\]](./CVE-2026-54425.osv.json)



_Last updated: 2026-10-21T11:31:13.860Z_

### Affected

* Apache bRPC before 1.18.0


### Description

Uncontrolled recursion in the HTTP/2 HPACK decoder in Apache bRPC before 1.18.0 allows remote attackers to cause denial of service by sending a crafted HTTP/2 header block containing many consecutive Dynamic Table Size Update entries. Each update was decoded by recursively invoking the HPACK decoder, which could exhaust the thread stack before a header field or end of input was reached.<br><br>Root Cause:<br>The bRPC HPACK decoder recursively decoded the next entry after processing a Dynamic Table Size Update. The decoder did not bound the recursion depth, so a long sequence of update entries could consume excessive stack space.<br><br>Affected Scenarios:<br>Use bRPC with the built-in HTTP/2 implementation to accept HTTP/2 traffic from an untrusted network.<br><br>How to Fix:<br>1. Upgrade bRPC to version 1.18.0, which fixes this issue.<br>2. Apply this patch: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3343">https://github.com/apache/brpc/pull/3343</a><br><br>Note:<br>The fix changes HPACK Dynamic Table Size Update decoding to use iterative parsing instead of recursive parsing.

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* 黄宏洋(Huang Hongyang) (finder)


## HTTP builtin request can mark a connection authenticated and bypass auth for later requests ## { #CVE-2026-48830 }

CVE-2026-48830 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48830) [\[CVE json\]](./CVE-2026-48830.cve.json)

_Last updated: 2026-10-21T11:30:10.882Z_

### Affected

* Apache bRPC through 1.17.0
* Apache bRPC at 1.18.0 unaffected


### Description

Improper authentication in Apache bRPC through 1.17.0 allows a remote unauthenticated attacker to bypass authentication for protected non-builtin HTTP endpoints by first sending a builtin HTTP request on the same HTTP/1.1 keep-alive connection.<br><br>When <code>ServerOptions.auth</code> is enabled and builtin HTTP services are exposed on the public listener, a builtin request received as the first message on a socket may cause the connection to be treated as authenticated for later requests on that socket. Users are recommended to upgrade to version 1.18.0, which fixes this issue, or apply this PR separately: <a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3308">https://github.com/apache/brpc/pull/3308</a>

### References
* https://lists.apache.org/thread/2pf15ojj0vr7rtx95677kgtl1mx3gdgb


### Credits
* Brubbish of VARAS@IIE (finder)


## Remote command injection vulnerability in heap builtin service ## { #CVE-2025-60021 }

CVE-2025-60021 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-60021) [\[CVE json\]](./CVE-2025-60021.cve.json) [\[OSV json\]](./CVE-2025-60021.osv.json)



_Last updated: 2026-01-16T08:39:21.612Z_

### Affected

* Apache bRPC from 1.11.0 before 1.15.0


### Description

<p>Remote command injection vulnerability in heap profiler builtin service in Apache bRPC ((all versions &lt; 1.15.0)) on all platforms allows attacker to inject remote command.</p><p></p>Root Cause: The bRPC heap profiler built-in service (/pprof/heap) does not validate the user-provided extra_options parameter and executes it as a command-line argument. Attackers can execute remote commands using the extra_options parameter..<br><br>Affected scenarios:&nbsp;Use the built-in bRPC heap profiler service to perform jemalloc memory profiling.<br><br>How to Fix: we provide two methods, you can choose one of them:<br><br>1. Upgrade bRPC to version 1.15.0.<br>2. Apply this patch (<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3101">https://github.com/apache/brpc/pull/3101</a>) manually.<b><br></b><p></p>

### References
* https://lists.apache.org/thread/xy51d2fx6drzhfp92xptsx5845q7b37m


### Credits
* Simcha Kosman (reporter)


## Stack Exhaustion via Unbounded Recursion in JSON Parser ## { #CVE-2025-59789 }

CVE-2025-59789 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-59789) [\[CVE json\]](./CVE-2025-59789.cve.json) [\[OSV json\]](./CVE-2025-59789.osv.json)



_Last updated: 2025-12-01T02:28:22.223Z_

### Affected

* Apache bRPC before 1.15.0


### Description

Uncontrolled recursion in the json2pb component in Apache bRPC (version &lt; 1.15.0) on all platforms allows remote attackers to make the server crash via sending deep recursive json data.<br><br>Root Cause:<br>The bRPC&nbsp;json2pb component uses rapidjson to parse json data from the network. The rapidjson parser uses a recursive parsing method by default. If the input json has a large depth of recursive structure, the parser function may run into stack overflow.<br><br>Affected Scenarios:<br>Use bRPC server with protobuf message to serve http+json requests from untrusted network. Or directly use&nbsp;JsonToProtoMessage to convert json from&nbsp;untrusted input.

<br><br>How to Fix: <br>(<span style="background-color: rgb(255, 255, 255);">Choose one of the following options)&nbsp;</span><br>1. Upgrade bRPC to version 1.15.0, which fixes this issue.<br><span style="background-color: rgb(255, 255, 255);">2. Apply this patch: </span><a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3099">https://github.com/apache/brpc/pull/3099</a>

<br><br>Note:<br>No matter which option 

<span style="background-color: rgb(255, 255, 255);">you choose</span>, you should know that the fix introduces a recursion depth limit with default value 100. It affects these functions:&nbsp;

<span style="background-color: rgb(255, 255, 255);">ProtoMessageToJson, ProtoMessageToProtoJson, JsonToProtoMessage, and ProtoJsonToProtoMessage.</span>

 If your requests contain json or protobuf messages that have a depth exceeding the limit, the request will be failed after applying the fix. You can modify the gflag json2pb_max_recursion_depth to change the limit.

### References
* https://lists.apache.org/thread/ozmcsztcpxn61jxod8jo8q46jo0oc1zx


### Credits
* Tyler Zars (finder)


## Redis Parser Remote Denial of Service ## { #CVE-2025-54472 }

CVE-2025-54472 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-54472) [\[CVE json\]](./CVE-2025-54472.cve.json) [\[OSV json\]](./CVE-2025-54472.osv.json)



_Last updated: 2025-08-12T02:14:20.765Z_

### Affected

* Apache bRPC before 1.14.1


### Description

Unlimited memory allocation in redis protocol parser in Apache bRPC (all versions &lt; 1.14.1) on all platforms allows attackers to crash the service via network.<br><br>

<span style="background-color: rgb(255, 255, 255);">Root Cause: In the bRPC Redis protocol parser code, memory for arrays or strings of corresponding sizes is allocated based on the integers read from the network. If the integer read from the network is too large, it may cause a bad alloc error and lead to the program crashing. Attackers can exploit this feature by sending special data packets to the bRPC service to carry out a denial-of-service attack on it.<br></span>The bRPC 1.14.0 version tried to fix this issue by limited the memory allocation size, however, the limitation checking code is not well implemented that may cause integer overflow and evade such limitation. So the&nbsp;1.14.0 version is also vulnerable, although the integer range that affect version 1.14.0 is different from that affect version &lt; 1.14.0.<br><br>

<span style="background-color: rgb(255, 255, 255);">Affected scenarios: Using bRPC as a Redis server to provide network services to untrusted clients, or using bRPC as a Redis client to call untrusted Redis services.</span>

<br><br>How to Fix: we provide two methods, you can choose one of them:<br><br>1. Upgrade bRPC to version 1.14.1.<br>2. Apply this patch (<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/3050">https://github.com/apache/brpc/pull/3050</a>) manually.<br><br><span style="background-color: rgb(255, 255, 255);">No matter you choose which method, you should note that the patch limits the maximum length of memory allocated for each time in the bRPC Redis parser. The default limit is 64M. If some of you redis request or response have a size larger than 64M, you might encounter error after upgrade. For such case, you can modify the gflag&nbsp;<span style="background-color: rgb(255, 255, 255);">redis_max_allocation_size to set a larger limit.</span></span><br><br>

### References
* https://lists.apache.org/thread/r3xsy3wvs4kmfhc281173k5b6ll1xt2m


### Credits
* Tyler Zars (reporter)


## HTTP request smuggling vulnerability ## { #CVE-2024-23452 }

CVE-2024-23452 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23452) [\[CVE json\]](./CVE-2024-23452.cve.json) [\[OSV json\]](./CVE-2024-23452.osv.json)



_Last updated: 2024-02-08T09:00:00.820Z_

### Affected

* Apache bRPC from 0.9.5 before 1.8.0


### Description

Request smuggling vulnerability in HTTP server in Apache bRPC 0.9.5~1.7.0 on all platforms allows attacker to smuggle request.<br><br><p><b>Vulnerability Cause Description：</b><u></u><u></u></p><p>The http_parser does not comply with the RFC-7230 HTTP 1.1 specification.</p><br><b>Attack&nbsp;scenario:<br></b><span style="background-color: rgb(255, 255, 255);">If a message is received with both a Transfer-Encoding and a Content-Length header field, such a message might indicate an attempt to perform request smuggling or response splitting.</span><br><p>One particular attack scenario is that a bRPC made http server on the backend receiving requests in one persistent connection from frontend server that uses TE to parse request with the logic that 'chunk' is contained in the TE field. in that case an attacker can smuggle a request into the connection to the backend server.&nbsp;<br></p><br><b>Solution:<br></b>You can choose one solution from below:<br><span style="background-color: rgb(255, 255, 255);">1. Upgrade bRPC to version 1.8.0, which fixes this issue. Download link: </span><a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/releases/tag/1.8.0">https://github.com/apache/brpc/releases/tag/1.8.0<br></a>2. Apply this patch:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/2518">https://github.com/apache/brpc/pull/2518</a><br><br>

### References
* https://github.com/apache/brpc/releases/tag/1.8.0
* https://github.com/apache/brpc/pull/2518
* https://lists.apache.org/thread/kkvdpwyr2s2yt9qvvxfdzon012898vxd


### Credits
* Pingtao Wei of 2012 Laboratories (finder)
* Ziyang Chen of 2012 Laboratories (finder)
* Haoran Zhi of 2012 Laboratories (finder)
* Hongpei Li of 2012 Laboratories (finder)


## The builtin service rpcz page has an XSS attack vulnerability ## { #CVE-2023-45757 }

CVE-2023-45757 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-45757) [\[CVE json\]](./CVE-2023-45757.cve.json) [\[OSV json\]](./CVE-2023-45757.osv.json)



_Last updated: 2023-10-16T08:01:36.036Z_

### Affected

* Apache bRPC from 0.9.0 through 1.6.0


### Description

<span style="background-color: rgb(255, 255, 255);">Security vulnerability </span>in Apache bRPC &lt;=1.6.0 on all platforms allows attackers to inject XSS code to the builtin rpcz page.<br>An attacker that can send http request to bRPC server with rpcz enabled can&nbsp;inject arbitrary XSS code to the builtin rpcz page.<br><br>Solution<span style="background-color: rgba(0, 0, 0, 0.2);">&nbsp;(choose one of three)</span>:<br>1. upgrade to bRPC &gt; 1.6.0, download link: <a target="_blank" rel="nofollow" href="https://dist.apache.org/repos/dist/release/brpc/1.6.1/">https://dist.apache.org/repos/dist/release/brpc/1.6.1/</a><br>2. If you are using an old version of bRPC and hard to upgrade, you can apply this patch:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/2411">https://github.com/apache/brpc/pull/2411</a><br>3. disable rpcz feature

### References
* https://lists.apache.org/thread/6syxv32fqgl30brfpttrk4rfsb983hl4


## ServerOptions.pid_file may cause arbitrary code execution ## { #CVE-2023-31039 }

CVE-2023-31039 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-31039) [\[CVE json\]](./CVE-2023-31039.cve.json) [\[OSV json\]](./CVE-2023-31039.osv.json)



_Last updated: 2023-05-08T08:57:09.633Z_

### Affected

* Apache bRPC from 0.9.0 before 1.5.0


### Description

<span style="background-color: rgb(255, 255, 255);">Security vulnerability&nbsp;</span>in Apache bRPC &lt;1.5.0 on all platforms allows attackers to execute arbitrary code via ServerOptions::pid_file.<br>An attacker that can influence the ServerOptions pid_file parameter with which the bRPC server is started can execute arbitrary code with the permissions of the bRPC process.<br><br>Solution:<br>1. upgrade to bRPC &gt;= 1.5.0, download link:&nbsp;<a target="_blank" rel="nofollow" href="https://dist.apache.org/repos/dist/release/brpc/1.5.0/">https://dist.apache.org/repos/dist/release/brpc/1.5.0/</a><br>2. If you are using an old version of bRPC and hard to upgrade, you can apply this patch:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/brpc/pull/2218">https://github.com/apache/brpc/pull/2218</a>

### References
* https://lists.apache.org/thread/jqpttrqbc38yhckgp67xk399hqxnz7jn
