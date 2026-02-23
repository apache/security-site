---
title: Apache MINA security advisories
description: Security information for Apache MINA
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache MINA? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## MINA applications using unbounded deserialization may allow RCE ## { #CVE-2024-52046 }

CVE-2024-52046 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-52046) [\[CVE json\]](./CVE-2024-52046.cve.json)

_Last updated: 2025-02-12T09:33:34.969Z_

### Affected

* Apache MINA from 2.0 through 2.0.26 unknown
* Apache MINA from 2.1 through 2.1.9
* Apache MINA from 2.2 through 2.2.3


### Description

<div>
			<div>
				<div>
					<div>
						<p>The ObjectSerializationDecoder in Apache MINA uses Java’s native deserialization protocol to process
incoming serialized data but lacks the necessary security checks and defenses. This vulnerability allows
attackers to exploit the deserialization process by sending specially crafted malicious serialized data,
potentially leading to remote code execution (RCE) attacks.
</p>
					</div>
				</div>
			</div>
		</div><div>
	
This issue affects MINA core versions 2.0.X, 2.1.X and 2.2.X, and will be fixed by the releases 2.0.27, 2.1.10 and 2.2.4.<br></div><div><br></div><div>It's also important to note that an application using MINA core library will only be affected if the <span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">IoBuffer#getObject</span></span>() method is called, and this specific method is potentially called when adding a ProtocolCodecFilter instance using the <span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(212, 212, 212);">ObjectSerializationCodecFactory</span></span></span> class in the filter chain. If your application is specifically using those classes, you have to upgrade to the latest version of MINA core library.</div><div><br></div><div>Upgrading will&nbsp; not be enough: you also need to explicitly allow the classes the decoder will accept in the <span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(212, 212, 212);">ObjectSerializationDecoder</span></span></span> instance, using one of the three new methods:</div><div><br></div><div><div><div><p>    /**</p><p>&nbsp; &nbsp;&nbsp; * Accept class names where the supplied ClassNameMatcher matches for</p><p>     * deserialization, unless they are otherwise rejected.</p><p>     *</p><p>     * @param classNameMatcher the matcher to use</p><p>     */</p><p>    public void <span style="background-color: rgb(212, 212, 212);">accept</span>(ClassNameMatcher classNameMatcher)</p><p><br></p><p>    /**</p><p>     * Accept class names that match the supplied pattern for</p><p>     * deserialization, unless they are otherwise rejected.</p><p>     *</p><p>     * @param pattern standard Java regexp</p><p>     */</p><p>    public void accept(Pattern pattern) <br></p><p><br></p><p>    /**</p><p>     * Accept the wildcard specified classes for deserialization,</p><p>     * unless they are otherwise rejected.</p><p>     *</p><p>     * @param patterns Wildcard file name patterns as defined by</p><p>     *                  {@link org.apache.commons.io.FilenameUtils#wildcardMatch(String, String) FilenameUtils.wildcardMatch}</p><p>     */</p><p>    public void accept(String... patterns)<br></p></div><div><br></div><div>By default, the decoder will reject *all* classes that will be present in the incoming data.</div><div><br></div><div><br></div><div>Note: The FtpServer, SSHd and Vysper sub-project are not affected by this issue.<br></div></div></div>

### References
* https://lists.apache.org/thread/4wxktgjpggdbto15d515wdctohb0qmv8


### Credits
* The initial report was submitted by Bofei Chen, with all the necessary bits to reproduce the RCE (finder)


## integrity check bypass ## { #CVE-2024-41909 }

CVE-2024-41909 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-41909) [\[CVE json\]](./CVE-2024-41909.cve.json) [\[OSV json\]](./CVE-2024-41909.osv.json)



_Last updated: 2024-08-12T16:00:27.622Z_

### Affected

* Apache MINA SSHD through 2.11.0


### Description

<div>Like many other SSH implementations, Apache MINA SSHD suffered from the issue that is more widely known as CVE-2023-48795. An attacker that can intercept traffic between client and server could drop certain packets from the stream, potentially causing client and server to consequently end up with a connection for which 
some security features have been downgraded or disabled, aka a Terrapin 
attack<br></div><div><br></div><div>The mitigations to prevent this type of attack were implemented in Apache MINA SSHD 2.12.0, both client and server side. Users are recommended to upgrade to at least this version. Note that both the client and the server implementation must have mitigations applied against this issue, otherwise the connection may still be affected.<br></div>

### References
* https://github.com/apache/mina-sshd/issues/445
* https://lists.apache.org/thread/vwf1ot8wx1njyy8n19j5j2tcnjnozt3b


### Credits
* Fabian Bäumer (finder)


## Information disclosure bugs with RootedFilesystem ## { #CVE-2023-35887 }

CVE-2023-35887 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-35887) [\[CVE json\]](./CVE-2023-35887.cve.json) [\[OSV json\]](./CVE-2023-35887.osv.json)



_Last updated: 2023-07-19T07:18:05.211Z_

### Affected

* Apache MINA SSHD from 1.0 before 2.10


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache MINA.<br><br>In SFTP servers implemented using Apache MINA SSHD that use a RootedFileSystem, logged users may be able to discover "exists/does not exist" information about items outside the rooted tree via paths including parent navigation ("..") beyond the root, or involving symlinks.<br><br>This issue affects Apache MINA: from 1.0 before 2.10. Users are recommended to upgrade to 2.10<br>

### References
* https://lists.apache.org/thread/b9qgtqvhnvgfpn0w1gz918p21p53tqk2


### Credits
* Andrew Pikler (finder)


## Apache MINA SSHD: Java unsafe deserialization vulnerability ## { #CVE-2022-45047 }

CVE-2022-45047 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-45047) [\[CVE json\]](./CVE-2022-45047.cve.json) [\[OSV json\]](./CVE-2022-45047.osv.json)



_Last updated: 2022-11-16T09:03:02.600Z_

### Affected

* Apache MINA SSHD from unspecified through 2.9.1


### Description

Class org.apache.sshd.server.keyprovider.SimpleGeneratorHostKeyProvider in Apache MINA SSHD <= 2.9.1 uses Java deserialization to load a serialized java.security.PrivateKey. The class is one of several implementations that an implementor using Apache MINA SSHD can choose for loading the host keys of an SSH server.

### References
* https://www.mail-archive.com/dev%40mina.apache.org/msg39312.html


### Credits
* The Apache MINA SSHD team would like to thank Zhang Zewei, NOFOCUS, for reporting this issue.


## Apache MINA HTTP listener DOS ## { #CVE-2021-41973 }

CVE-2021-41973 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-41973) [\[CVE json\]](./CVE-2021-41973.cve.json) [\[OSV json\]](./CVE-2021-41973.osv.json)



_Last updated: 2021-11-01T08:33:24.585Z_

### Affected

* Apache MINA from Apache MINA before 2.1.5


### Description

In Apache MINA, a specifically crafted, malformed HTTP request may cause the HTTP Header decoder to loop indefinitely.  The decoder assumed that the HTTP Header begins at the beginning of the buffer and loops if there is more data than expected.  Please update MINA to 2.1.5 or greater.

### References
* https://lists.apache.org/thread.html/r0b907da9340d5ff4e6c1a4798ef4e79700a668657f27cca8a39e9250%40%3Cdev.mina.apache.org%3E


## DoS/OOM leak vulnerability in Apache Mina SSHD Server ## { #CVE-2021-30129 }

CVE-2021-30129 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-30129) [\[CVE json\]](./CVE-2021-30129.cve.json) [\[OSV json\]](./CVE-2021-30129.osv.json)



_Last updated: 2021-07-12T12:00:59.616Z_

### Affected

* Apache Mina SSHD from 2.0.0 before Apache Mina SSHD*


### Description

A vulnerability in sshd-core of Apache Mina SSHD allows an attacker to overflow the server causing an OutOfMemory error.  This issue affects the SFTP and port forwarding features of Apache Mina SSHD version 2.0.0 and later versions.  It was addressed in Apache Mina SSHD 2.7.0

### References
* https://lists.apache.org/thread.html/r6d4f78e192a0c8eabd671a018da464024642980ecd24096bde6db36f%40%3Cusers.mina.apache.org%3E
