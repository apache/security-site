---
title: Apache OpenNLP security advisories
description: Security information for Apache OpenNLP
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache OpenNLP? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## OOM DoS via Unbounded Array Allocation in AbstractModelReader ## { #CVE-2026-42440 }

CVE-2026-42440 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42440) [\[CVE json\]](./CVE-2026-42440.cve.json) [\[OSV json\]](./CVE-2026-42440.osv.json)



_Last updated: 2026-06-30T04:39:58.456Z_

### Affected

* Apache OpenNLP from 2.0 before 2.5.9
* Apache OpenNLP from 3.0.0-M1 before 3.0.0-M3
* Apache OpenNLP before 1.9.5


### Description

<p><b>OOM Denial of Service via Unbounded Array Allocation in Apache OpenNLP AbstractModelReader&nbsp;</b></p><p><b>Versions Affected:</b>&nbsp;</p>before 1.9.5<br><p>before 2.5.9</p><p>before 3.0.0-M3&nbsp;</p><p><b>Description:</b></p>
<p>The <code>AbstractModelReader</code> methods <code>getOutcomes()</code>, <code>getOutcomePatterns()</code>, and <code>getPredicates()</code> each read a 32-bit signed integer count field from a binary model stream and pass that value directly to an array allocation (<code>new String[numOutcomes]</code>, <code>new int[numOCTypes][]</code>, <code>new String[NUM_PREDS]</code>) without validating that the value is non-negative or within a reasonable bound. The count is therefore fully attacker-controlled when the model file originates from an untrusted source.</p>
<p>A crafted <code>.bin</code> model file in which any of these count fields is set to <code>Integer.MAX_VALUE</code> (or any value large enough to exhaust the available heap) triggers an <code>OutOfMemoryError</code> at the array allocation itself, before the corresponding label or pattern data is consumed from the stream. The error occurs very early in deserialization: for a GIS model, <code>getOutcomes()</code> is reached after only the model-type string, the correction constant, and the correction parameter have been read; so the attacker pays no meaningful size cost to weaponize a payload, and a single small file can crash a JVM that loads it. Any code path that deserializes a <code>.bin</code> model is affected, including direct use of <code>GenericModelReader</code> and any higher-level component that delegates to it during model load.</p>
<p>The practical impact is denial of service against processes that load model files from untrusted or semi-trusted origins.&nbsp;&nbsp;</p>
<p><b>Mitigation:</b></p>
<ul>
<li>2.x users should upgrade to 2.5.9.</li>
<li>3.x users should upgrade to 3.0.0-M3.</li>
</ul>
<p><b>Note:</b> The fix introduces an upper bound on each of the three count fields, checked before array allocation; counts that are negative or exceed the bound cause an <code>IllegalArgumentException</code> to be thrown and the read to fail fast with no large allocation. The default bound is 10,000,000, which is well above the entry counts of legitimate OpenNLP models but far below any value that would threaten heap exhaustion. Deployments that legitimately need to load models with more entries than the default can raise the limit at JVM startup by setting the <code>OPENNLP_MAX_ENTRIES</code> system property to the desired positive integer (e.g. <code>-DOPENNLP_MAX_ENTRIES=50000000</code>); invalid or non-positive values fall back to the default.</p>
<p>Users who cannot upgrade immediately should treat all <code>.bin</code> model files as untrusted input unless their provenance is verified, and should avoid loading models supplied by end users or fetched from third-party repositories without integrity checks.&nbsp;</p>

### References
* https://lists.apache.org/thread/s8xlkx1gqbxfsq48py5h6jphjvgqp1jo


### Credits
* Subramanian S (finder)


## Arbitrary Class Instantiation via Model Manifest in ExtensionLoader ## { #CVE-2026-42027 }

CVE-2026-42027 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42027) [\[CVE json\]](./CVE-2026-42027.cve.json) [\[OSV json\]](./CVE-2026-42027.osv.json)



_Last updated: 2026-06-30T07:17:51.901Z_

### Affected

* Apache OpenNLP from 2.0 before 2.5.9
* Apache OpenNLP from 3.0.0-M1 before 3.0.0-M3
* Apache OpenNLP before 1.9.5


### Description

<div><div><p><b>Arbitrary Class Instantiation via Model Manifest in Apache OpenNLP ExtensionLoader</b></p></div></div><div><div><p><b>Versions Affected:&nbsp;</b>before 1.9.5, before 2.5.9, before 3.0.0-M3</p></div></div><div><div><p><b>Description:</b>&nbsp;</p><p>The <code>ExtensionLoader.instantiateExtension(Class, String)</code>&nbsp;method loads a class by its fully-qualified name via <code>Class.forName()</code>&nbsp;and invokes its no-arg constructor, with the class name sourced from the <code>manifest.properties</code>&nbsp;entry of a model archive. The existing <code>isAssignableFrom</code>&nbsp;check correctly rejects classes that are not subtypes of the expected extension interface (<code>BaseToolFactory</code>&nbsp;for <code>factory=</code>, <code>ArtifactSerializer</code>&nbsp;for <code>serializer-class-*</code>), but the check runs <em><b>after</b></em>&nbsp;<code>Class.forName()</code>&nbsp;has already loaded and initialized the named class. </p><p><code>Class.forName()</code>&nbsp;with default initialization semantics executes the target class's static initializer before returning, so an attacker who can supply a crafted model archive can cause the static initializer of any class on the classpath to run during model loading, regardless of whether that class passes the subsequent type check. </p><p>Exploitation requires a class with attacker-useful side effects in its static initializer (for example, JNDI lookup, outbound network I/O, or filesystem access) to be <b>present on the classpath</b>, so this is not a drop-in remote code execution; however, the attack surface grows as third-party model distribution becomes more common (community model repositories, Hugging Face-style sharing), where users routinely load model files from origins they do not control. A secondary, narrower vector affects deployments that ship legitimate <code>BaseToolFactory</code>&nbsp;or <code>ArtifactSerializer</code>&nbsp;subclasses with side-effecting no-arg constructors: a malicious manifest can name such a class and force its constructor to run during model load.</p></div></div><div><div><p><b>Mitigation:</b>&nbsp;</p><p></p><ul><li>2.x users should upgrade to 2.5.9. </li><li>3.x users should upgrade to 3.0.0-M3. </li></ul><p></p><p>Note: The fix introduces a package-prefix allowlist that is consulted before <code>Class.forName()</code>&nbsp;is invoked, so the static initializer of a disallowed class is never executed. Classes under the <code>opennlp.</code>&nbsp;prefix remain permitted by default. Deployments that load models referencing factories or serializers outside <code>opennlp.*</code>&nbsp;must opt those packages in, either programmatically via <code>ExtensionLoader.registerAllowedPackage(String)</code>&nbsp;before the first model load, or by setting the <code><b>OPENNLP_EXT_ALLOWED_PACKAGES</b></code>&nbsp;system property to a comma-separated list of allowed package prefixes. </p><p>Users who cannot upgrade immediately should ensure that all model files are sourced from <b>trusted origins</b>&nbsp;and should audit their classpath for classes with side-effecting static initializers or constructors, particularly any that perform JNDI lookups, network requests, or filesystem operations during class initialization.</p></div></div><br><br>

### References
* https://lists.apache.org/thread/ltlo4powjfc0w2w2yyl1o5tc7q1gcb2y


### Credits
* Subramanian S (finder)


## XXE via Dictionary Parsing in DictionaryEntryPersistor ## { #CVE-2026-40682 }

CVE-2026-40682 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40682) [\[CVE json\]](./CVE-2026-40682.cve.json) [\[OSV json\]](./CVE-2026-40682.osv.json)



_Last updated: 2026-06-30T04:40:05.111Z_

### Affected

* Apache OpenNLP from 2.0 before 2.5.9
* Apache OpenNLP from 3.0.0-M1 before 3.0.0-M3
* Apache OpenNLP before 1.9.5


### Description

<p><strong>XML External Entity (XXE) via Unsanitized Dictionary Parsing in Apache OpenNLP DictionaryEntryPersistor</strong></p>
<p><strong>Versions Affected:</strong> before 2.5.9, before 3.0.0-M3</p>
<p><strong>Description:</strong> The <code>DictionaryEntryPersistor</code> class initializes a static <code>SAXParserFactory</code> at class-load time without enabling <code>FEATURE_SECURE_PROCESSING</code> or disabling DTD processing. When <code>create(InputStream, EntryInserter)</code> is invoked, the only feature set on the <code>XMLReader</code> is namespace support — external entity resolution and DOCTYPE declarations remain fully enabled. An attacker who can supply a crafted dictionary file (e.g., a stop-word list or domain dictionary) containing a malicious DOCTYPE declaration can trigger local file disclosure via <code>file://</code> entity references or server-side request forgery via <code>http://</code> entity references during SAX parsing, before the application processes a single dictionary entry. This is inconsistent with the project's own <code>XmlUtil.createSaxParser()</code> helper, which correctly sets <code>FEATURE_SECURE_PROCESSING</code> and <code>disallow-doctype-decl</code> and is used by all other XML parsing paths in the codebase. The public <code>Dictionary(InputStream)</code> constructor delegates directly to this method and is the documented API for loading user-supplied dictionaries, making untrusted input a realistic scenario.</p>
<p><strong>Mitigation:</strong> 2.x users should upgrade to 2.5.9. 3.x users should upgrade to 3.0.0-M3. Users who cannot upgrade immediately should ensure that all dictionary files are sourced from trusted origins and should consider wrapping the <code>Dictionary(InputStream)</code> constructor with input validation that rejects any XML containing a DOCTYPE declaration before it reaches the parser.<br></p>

### References
* https://lists.apache.org/thread/r6jpt0qr9nj67gqhppqg7jxf8vsbo0w6


### Credits
* Subramanian S (finder)
