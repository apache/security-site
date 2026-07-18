---
title: Apache Logging security advisories
description: Security information for Apache Logging
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Logging? Send your report to the [Apache Logging Security Team](mailto:security@logging.apache.org?subject=Logging).

You can read more about the security policy on:

- [Apache Logging security model](https://logging.apache.org/security.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improper serialization of non-finite floating-point values in MapMessage.asJson() ## { #CVE-2026-49844 }

CVE-2026-49844 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49844) [\[CVE json\]](./CVE-2026-49844.cve.json) [\[OSV json\]](./CVE-2026-49844.osv.json)



_Last updated: 2026-07-10T21:14:52.822Z_

### Affected

* Apache Log4j API from 2.13.1 before 2.25.5
* Apache Log4j API from 2.26.0 before 2.26.1
* Apache Log4j API from 3.0.0-alpha1 through 3.0.0-beta2


### Description

<p>Improper encoding of non-finite floating-point values during <code>MapMessage</code> JSON serialization in Apache Log4j API produces output that is not valid JSON. This issue affects Apache Log4j API versions 2.13.1 through 2.25.4 and version 2.26.0.</p><p>The fix for CVE-2026-34481 did not cover all code paths: when a <code>MapMessage</code> contains a non-finite IEEE 754 value (<code>NaN</code>, <code>Infinity</code>, or <code>-Infinity</code>), <code>MapMessage.asJson()</code> emits the corresponding bare token. RFC 8259 does not permit these tokens, so a conformant parser rejects the resulting document.</p><p>The defect is reachable only when both of the following conditions hold:</p><ul><li>The application uses the <a target="_blank" rel="nofollow" href="https://logging.apache.org/log4j/2.x/manual/json-template-layout.html#event-template-resolver-message"><code>message</code> resolver</a> of <code>JsonTemplateLayout</code> or any other layout that relies on <code>MapMessage.asJson()</code> or <code>MapMessage.getFormattedMessage(new String[]{"JSON"})</code>.</li><li>The application logs a <code>MapMessage</code> that contains an attacker-controlled floating-point value.</li></ul><p>An attacker who can supply a non-finite value can cause the affected layout to emit malformed JSON, which may corrupt the enclosing log record or disrupt downstream log ingestion and parsing.</p><p>Users are advised to upgrade to Apache Log4j API 2.25.5 or 2.26.1, both of which emit RFC 8259-compliant JSON for non-finite values.</p>

### References
* https://logging.apache.org/log4j/2.x/manual/json-template-layout.html#event-template-resolver-message
* https://github.com/apache/logging-log4j2/pull/4163
* https://logging.apache.org/cyclonedx/vdr.xml
* https://logging.apache.org/security.html#CVE-2026-49844


### Credits
* Himanshu Anand (finder)


## Silent log event loss in XMLLayout due to unescaped XML 1.0 forbidden characters ## { #CVE-2026-40023 }

CVE-2026-40023 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40023) [\[CVE json\]](./CVE-2026-40023.cve.json) [\[OSV json\]](./CVE-2026-40023.osv.json)



_Last updated: 2026-04-10T15:45:43.003Z_

### Affected

* Apache Log4cxx before 1.7.0
* Apache Log4cxx (Conan) before 1.7.0
* Apache Log4cxx (Brew) before 1.7.0


### Description

<p>Apache Log4cxx's <code><a target="_blank" rel="nofollow" href="https://logging.apache.org/log4cxx/1.7.0/classlog4cxx_1_1xml_1_1XMLLayout.html">XMLLayout</a></code>, in versions before 1.7.0, fails to sanitize characters forbidden by the <a target="_blank" rel="nofollow" href="https://www.w3.org/TR/xml/#charsets">XML 1.0 specification</a> in log messages, NDC, and MDC property keys and values, producing invalid XML output. Conforming XML parsers must reject such documents with a fatal error, which may cause downstream log processing systems to drop or fail to index affected records.</p><p>An attacker who can influence logged data can exploit this to suppress individual log records, impairing audit trails and detection of malicious activity.</p><p>Users are advised to upgrade to Apache Log4cxx <code>1.7.0</code>, which fixes this issue.</p>

### References
* https://github.com/apache/logging-log4cxx/pull/609
* https://logging.apache.org/security.html#CVE-2026-40023
* https://logging.apache.org/cyclonedx/vdr.xml
* https://logging.apache.org/log4cxx/1.7.0/classlog4cxx_1_1xml_1_1XMLLayout.html
* https://lists.apache.org/thread/y15cv3zblg3dfwr5vy6ddbnl4zyrzr8b


### Credits
* Olawale Titiloye (finder)


## Silent log event loss in XmlLayout and XmlLayoutSchemaLog4J due to unescaped XML 1.0 forbidden characters ## { #CVE-2026-40021 }

CVE-2026-40021 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40021) [\[CVE json\]](./CVE-2026-40021.cve.json) [\[OSV json\]](./CVE-2026-40021.osv.json)



_Last updated: 2026-04-10T15:44:08.554Z_

### Affected

* Apache Log4net before 3.3.0


### Description

<p>Apache Log4net's <code><a target="_blank" rel="nofollow" href="https://logging.apache.org/log4net/manual/configuration/layouts.html#layout-list">XmlLayout</a></code> and <code><a target="_blank" rel="nofollow" href="https://logging.apache.org/log4net/manual/configuration/layouts.html#layout-list">XmlLayoutSchemaLog4J</a></code>, in versions before 3.3.0, fail to sanitize characters forbidden by the <a target="_blank" rel="nofollow" href="https://www.w3.org/TR/xml/#charsets">XML 1.0 specification</a> in MDC property keys and values, as well as the identity field that may carry attacker-influenced data. This causes an exception during serialization and the silent loss of the affected log event.</p><p>An attacker who can influence any of these fields can exploit this to suppress individual log records, impairing audit trails and detection of malicious activity.</p><p>Users are advised to upgrade to Apache Log4net <code>3.3.0</code>, which fixes this issue.</p>

### References
* https://github.com/apache/logging-log4net/pull/280
* https://logging.apache.org/security.html#CVE-2026-40021
* https://logging.apache.org/cyclonedx/vdr.xml
* https://logging.apache.org/log4net/manual/configuration/layouts.html
* https://lists.apache.org/thread/q8otftjswhk69n3kxslqg7cobr0x4st7


### Credits
* f00dat (finder)


## Improper serialization of non-finite floating-point values in JsonTemplateLayout ## { #CVE-2026-34481 }

CVE-2026-34481 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34481) [\[CVE json\]](./CVE-2026-34481.cve.json) [\[OSV json\]](./CVE-2026-34481.osv.json)



_Last updated: 2026-07-11T04:55:35.716Z_

### Affected

* Apache Log4j JSON Template Layout from 2.14.0 before 2.25.4
* Apache Log4j JSON Template Layout from 3.0.0-alpha1 through 3.0.0-beta3


### Description

<p>Apache Log4j's <code><a target="_blank" rel="nofollow" href="https://logging.apache.org/log4j/2.x/manual/json-template-layout.html">JsonTemplateLayout</a></code>, in versions up to and including 2.25.3, produces invalid JSON output when log events contain non-finite floating-point values (<code>NaN</code>, <code>Infinity</code>, or <code>-Infinity</code>), which are prohibited by RFC 8259. This may cause downstream log processing systems to reject or fail to index affected records.</p><p>An attacker can exploit this issue only if both of the following conditions are met:</p><ul><li>The application uses <code>JsonTemplateLayout</code>.</li><li>The application logs a <code>MapMessage</code> containing an attacker-controlled floating-point value.</li></ul><p>Users are advised to upgrade to Apache Log4j JSON Template Layout 2.25.4, which corrects this issue.</p>

### References
* https://github.com/apache/logging-log4j2/pull/4080
* https://logging.apache.org/security.html#CVE-2026-34481
* https://logging.apache.org/cyclonedx/vdr.xml
* https://logging.apache.org/log4j/2.x/manual/json-template-layout.html
* https://lists.apache.org/thread/n34zdv00gbkdbzt2rx9rf5mqz6lhopcv


### Credits
* Ap4sh (Samy Medjahed) and Ethicxz (Eliott Laurie) (finder)


## Silent log event loss in XmlLayout due to unescaped XML 1.0 forbidden characters ## { #CVE-2026-34480 }

CVE-2026-34480 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34480) [\[CVE json\]](./CVE-2026-34480.cve.json) [\[OSV json\]](./CVE-2026-34480.osv.json)



_Last updated: 2026-04-10T15:41:58.452Z_

### Affected

* Apache Log4j Core from 2.0-alpha1 before 2.25.4
* Apache Log4j Core from 3.0.0-alpha1 through 3.0.0-beta3


### Description

<p>Apache Log4j Core's <code><a target="_blank" rel="nofollow" href="https://logging.apache.org/log4j/2.x/manual/layouts.html#XmlLayout">XmlLayout</a></code>, in versions up to and including 2.25.3, fails to sanitize characters forbidden by the <a target="_blank" rel="nofollow" href="https://www.w3.org/TR/xml/#charsets">XML 1.0 specification</a> producing invalid XML output whenever a log message or MDC value contains such characters.</p><p>The impact depends on the StAX implementation in use:</p><ul><li><strong>JRE built-in StAX:</strong> Forbidden characters are silently written to the output, producing malformed XML. Conforming parsers must reject such documents with a fatal error, which may cause downstream log-processing systems to drop the affected records.</li><li><strong>Alternative StAX implementations</strong> (e.g., <a target="_blank" rel="nofollow" href="https://github.com/FasterXML/woodstox">Woodstox</a>, a transitive dependency of the Jackson XML Dataformat module): An exception is thrown during the logging call, and the log event is never delivered to its intended appender, only to Log4j's internal status logger.</li></ul><p>Users are advised to upgrade to Apache Log4j Core <code>2.25.4</code>, which corrects this issue by sanitizing forbidden characters before XML output.</p>

### References
* https://github.com/apache/logging-log4j2/pull/4077
* https://logging.apache.org/security.html#CVE-2026-34480
* https://logging.apache.org/cyclonedx/vdr.xml
* https://logging.apache.org/log4j/2.x/manual/layouts.html#XmlLayout
* https://lists.apache.org/thread/5x0hcnng0chhghp6jgjdp3qmbbhfjzhb


### Credits
* Ap4sh (Samy Medjahed) and Ethicxz (Eliott Laurie) (original reporters) (finder)
* jabaltarik1 (independently) (finder)


## Silent log event loss in Log4j1XmlLayout due to unescaped XML 1.0 forbidden characters ## { #CVE-2026-34479 }

CVE-2026-34479 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34479) [\[CVE json\]](./CVE-2026-34479.cve.json) [\[OSV json\]](./CVE-2026-34479.osv.json)



_Last updated: 2026-04-10T15:41:04.182Z_

### Affected

* Apache Log4j 1 to Log4j 2 bridge from 2.7 before 2.25.4
* Apache Log4j 1 to Log4j 2 bridge from 3.0.0-alpha1 through 3.0.0-beta2


### Description

<p>The <code>Log4j1XmlLayout</code> from the Apache Log4j 1-to-Log4j 2 bridge fails to escape characters forbidden by the XML 1.0 standard, producing malformed XML output. Conforming XML parsers are required to reject documents containing such characters with a fatal error, which may cause downstream log processing systems to drop or fail to index affected records.</p><p>Two groups of users are affected:</p><ul><li>Those using <code>Log4j1XmlLayout</code> directly in a Log4j Core 2 configuration file.</li><li>Those using the Log4j 1 configuration compatibility layer with <code>org.apache.log4j.xml.XMLLayout</code> specified as the layout class.</li></ul><p>Users are advised to upgrade to Apache Log4j 1-to-Log4j 2 bridge version 2.25.4, which corrects this issue.</p><p><strong>Note:</strong> The Apache Log4j 1-to-Log4j 2 bridge is deprecated and will not be present in Log4j 3. Users are encouraged to consult the <a target="_blank" rel="nofollow" href="https://logging.apache.org/log4j/2.x/migrate-from-log4j1.html">Log4j 1 to Log4j 2 migration guide</a>, and specifically the section on eliminating reliance on the bridge.</p>

### References
* https://github.com/apache/logging-log4j2/pull/4078
* https://logging.apache.org/security.html#CVE-2026-34479
* https://logging.apache.org/cyclonedx/vdr.xml
* https://logging.apache.org/log4j/2.x/migrate-from-log4j1.html
* https://lists.apache.org/thread/gd0hp6mj17rn3kj279vgy4p7kd4zz5on


### Credits
* Ap4sh (Samy Medjahed) and Ethicxz (Eliott Laurie) (original reporters) (finder)
* jabaltarik1 (independently) (finder)


## Log injection in Rfc5424Layout due to silent configuration incompatibility ## { #CVE-2026-34478 }

CVE-2026-34478 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34478) [\[CVE json\]](./CVE-2026-34478.cve.json) [\[OSV json\]](./CVE-2026-34478.osv.json)



_Last updated: 2026-04-10T15:40:07.991Z_

### Affected

* Apache Log4j Core from 2.21.0 before 2.25.4
* Apache Log4j Core from 3.0.0-beta1 through 3.0.0-beta3


### Description

<p>Apache Log4j Core's <code><a target="_blank" rel="nofollow" href="https://logging.apache.org/log4j/2.x/manual/layouts.html#RFC5424Layout">Rfc5424Layout</a></code>, in versions 2.21.0 through 2.25.3, is vulnerable to log injection via CRLF sequences due to undocumented renames of security-relevant configuration attributes.</p><p>Two distinct issues affect users of stream-based syslog services who configure <code>Rfc5424Layout</code> directly:</p><ul><li>The <code>newLineEscape</code> attribute was silently renamed, causing newline escaping to stop working for users of TCP framing (RFC 6587), exposing them to CRLF injection in log output.</li><li>The <code>useTlsMessageFormat</code> attribute was silently renamed, causing users of TLS framing (RFC 5425) to be silently downgraded to unframed TCP (RFC 6587), without newline escaping.</li></ul><p>Users of the <code>SyslogAppender</code> are not affected, as its configuration attributes were not modified.</p><p>Users are advised to upgrade to Apache Log4j Core 2.25.4, which corrects this issue.</p>

### References
* https://github.com/apache/logging-log4j2/pull/4074
* https://logging.apache.org/security.html#CVE-2026-34478
* https://logging.apache.org/cyclonedx/vdr.xml
* https://logging.apache.org/log4j/2.x/manual/layouts.html#RFC5424Layout
* https://lists.apache.org/thread/3k1clr2l6vkdnl4cbhjrnt1nyjvb5gwt


### Credits
* Samuli Leinonen (finder)


## verifyHostName attribute silently ignored in TLS configuration, allowing hostname verification bypass ## { #CVE-2026-34477 }

CVE-2026-34477 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-34477) [\[CVE json\]](./CVE-2026-34477.cve.json) [\[OSV json\]](./CVE-2026-34477.osv.json)



_Last updated: 2026-04-10T15:36:10.071Z_

### Affected

* Apache Log4j Core from 2.12.0 before 2.25.4
* Apache Log4j Core from 3.0.0-alpha1 through 3.0.0-beta3


### Description

<p>The fix for <a target="_blank" rel="nofollow" href="https://logging.apache.org/security.html#CVE-2025-68161">CVE-2025-68161</a> was incomplete: it addressed hostname verification only when enabled via the <a target="_blank" rel="nofollow" href="https://logging.apache.org/log4j/2.x/manual/systemproperties.html#log4j2.sslVerifyHostName"><code>log4j2.sslVerifyHostName</code></a> system property, but not when configured through the <code><a target="_blank" rel="nofollow" href="https://logging.apache.org/log4j/2.x/manual/appenders/network.html#SslConfiguration-attr-verifyHostName">verifyHostName</a></code> attribute of the <code>&lt;Ssl&gt;</code> element.</p><p>Although the <code>verifyHostName</code> configuration attribute was introduced in Log4j Core 2.12.0, it was silently ignored in all versions through 2.25.3, leaving TLS connections vulnerable to interception regardless of the configured value.</p><p>A network-based attacker may be able to perform a man-in-the-middle attack when <strong>all</strong> of the following conditions are met:</p><ol><li>An SMTP, Socket, or Syslog appender is in use.</li><li>TLS is configured via a nested <code>&lt;Ssl&gt;</code> element.</li><li>The attacker can present a certificate issued by a CA trusted by the appender's configured trust store, or by the default Java trust store if none is configured.</li></ol><p>This issue does not affect users of the HTTP appender, which uses a separate <code><a target="_blank" rel="nofollow" href="https://logging.apache.org/log4j/2.x/manual/appenders/network.html#HttpAppender-attr-verifyHostName">verifyHostname</a></code> attribute that was not subject to this bug and verifies host names by default.</p><p>Users are advised to upgrade to Apache Log4j Core 2.25.4, which corrects this issue.</p>

### References
* https://github.com/apache/logging-log4j2/pull/4075
* https://logging.apache.org/security.html#CVE-2026-34477
* https://logging.apache.org/cyclonedx/vdr.xml
* https://logging.apache.org/log4j/2.x/manual/appenders/network.html#SslConfiguration-attr-verifyHostName
* https://lists.apache.org/thread/lkx8cl46t2bvkcwfcb2pd43ygc097lq4


### Credits
* Samuli Leinonen (original reporter) (finder)
* Naresh Kandula (independently) (finder)
* Vitaly Simonovich (independently) (finder)
* Raijuna (independently) (finder)
* Danish Siddiqui (djvirus, independently) (finder)
* Markus Magnuson (independently) (finder)
* Haruki Oyama (Waseda University, independently) (finder)


## Missing TLS hostname verification in Socket appender ## { #CVE-2025-68161 }

CVE-2025-68161 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-68161) [\[CVE json\]](./CVE-2025-68161.cve.json) [\[OSV json\]](./CVE-2025-68161.osv.json)



_Last updated: 2026-04-10T16:18:30.716Z_

### Affected

* Apache Log4j Core from 2.0-beta9 before 2.25.3
* Apache Log4j Core from 3.0.0-alpha1 through 3.0.0-beta3


### Description

<p>The Socket Appender in Apache Log4j Core versions <code>2.0-beta9</code> through <code>2.25.2</code> does not perform TLS hostname verification of the peer certificate, even when the <a target="_blank" rel="nofollow" href="https://logging.apache.org/log4j/2.x/manual/appenders/network.html#SslConfiguration-attr-verifyHostName">verifyHostName</a> configuration attribute or the <a target="_blank" rel="nofollow" href="https://logging.apache.org/log4j/2.x/manual/systemproperties.html#log4j2.sslVerifyHostName">log4j2.sslVerifyHostName</a> system property is set to <code>true</code>.</p><p>This issue may allow a man-in-the-middle attacker to intercept or redirect log traffic under the following conditions:</p><ul><li>The attacker is able to intercept or redirect network traffic between the client and the log receiver.</li><li>The attacker can present a server certificate issued by a certification authority trusted by the Socket Appender’s configured <strong>trust store</strong> (or by the default Java trust store if no custom trust store is configured).</li></ul><p>Users are advised to upgrade to Apache Log4j Core version <code>2.25.3</code>, which addresses this issue.</p><p>As an alternative mitigation, the Socket Appender may be configured to use a private or restricted trust root to limit the set of trusted certificates.</p>

### References
* https://github.com/apache/logging-log4j2/pull/4002
* https://logging.apache.org/security.html#CVE-2025-68161
* https://logging.apache.org/cyclonedx/vdr.xml
* https://logging.apache.org/log4j/2.x/manual/systemproperties.html#log4j2.sslVerifyHostName
* https://logging.apache.org/log4j/2.x/manual/appenders/network.html#SslConfiguration-attr-verifyHostName
* https://lists.apache.org/thread/xr33kyxq3sl67lwb61ggvm1fzc8k7dvx


### Credits
* Samuli Leinonen (finder)


## Improper escaping with JSONLayout ## { #CVE-2025-54813 }

CVE-2025-54813 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-54813) [\[CVE json\]](./CVE-2025-54813.cve.json) [\[OSV json\]](./CVE-2025-54813.osv.json)



_Last updated: 2025-08-22T18:45:40.110Z_

### Affected

* Apache Log4cxx from 0.11.0 before 1.5.0


### Description

<p>Improper Output Neutralization for Logs vulnerability in Apache Log4cxx.</p><p>When using <code>JSONLayout</code>, not all payload bytes are properly escaped. If an attacker-supplied message contains certain non-printable characters, these will be passed along in the message and written out as part of the JSON message. This may prevent applications that consume these logs from correctly interpreting the information within them.</p><p>This issue affects Apache Log4cxx: before <code>1.5.0</code>.</p><p>Users are recommended to upgrade to version <code>1.5.0</code>, which fixes the issue.</p>

### References
* https://logging.apache.org/security.html#CVE-2025-54813
* https://github.com/apache/logging-log4cxx/pull/512


### Credits
* Sovereign Tech Agency (sponsor)


## Improper HTML escaping in HTMLLayout ## { #CVE-2025-54812 }

CVE-2025-54812 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-54812) [\[CVE json\]](./CVE-2025-54812.cve.json) [\[OSV json\]](./CVE-2025-54812.osv.json)



_Last updated: 2025-08-22T18:46:44.374Z_

### Affected

* Apache Log4cxx before 1.5.0


### Description

<p>Improper Output Neutralization for Logs vulnerability in Apache Log4cxx.</p>
<p>When using <code>HTMLLayout</code>, logger names are not properly escaped when writing out to the HTML file.
If untrusted data is used to retrieve the name of a logger, an attacker could theoretically inject HTML or Javascript in order to hide information from logs or steal data from the user.
In order to activate this, the following sequence must occur:</p>
<ol>
<li>Log4cxx is configured to use <code>HTMLLayout</code>.</li>
<li>Logger name comes from an untrusted string</li>
<li>Logger with compromised name logs a message</li>
<li>User opens the generated HTML log file in their browser, leading to potential XSS</li>
</ol>
<p>Because logger names are generally constant strings, we assess the impact to users as LOW</p>
<p>This issue affects Apache Log4cxx: before <code>1.5.0</code>.</p>
<p>Users are recommended to upgrade to version <code>1.5.0</code>, which fixes the issue.</p>

### References
* https://logging.apache.org/security.html#CVE-2025-54812
* https://github.com/apache/logging-log4cxx/pull/509
* https://github.com/apache/logging-log4cxx/pull/514


### Credits
* Sovereign Tech Agency (sponsor)


## SQL injection when using ODBC appender ## { #CVE-2023-31038 }

CVE-2023-31038 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-31038) [\[CVE json\]](./CVE-2023-31038.cve.json) [\[OSV json\]](./CVE-2023-31038.osv.json)



_Last updated: 2023-05-08T08:55:53.262Z_

### Affected

* Apache Log4cxx from 0.9.0 before 1.1.0


### Description

<div>SQL injection in Log4cxx when using the ODBC appender to send log messages to a database.&nbsp; No fields sent to the database were properly escaped for SQL injection.&nbsp; This has been the case since at least version 0.9.0(released 2003-08-06)</div><div><br></div><div>Note that Log4cxx is a C++ framework, so only C++ applications are affected.</div><div>Before version 1.1.0, the ODBC appender was automatically part of Log4cxx if the library was found when compiling the library.&nbsp; As of version 1.1.0, this must be both explicitly enabled in order to be compiled in.</div><div><br></div><div>Three preconditions must be met for this vulnerability to be possible:</div><div>1. Log4cxx compiled with ODBC support(before version 1.1.0, this was auto-detected at compile time)</div><div>2. ODBCAppender enabled for logging messages to, generally done via a config file</div><div>3. User input is logged at some point. If your application does not have user input, it is unlikely to be affected.<br></div><div><br></div><div>Users are recommended to upgrade to version 1.1.0 which properly binds the parameters to the SQL statement, or migrate to the new DBAppender class which supports an ODBC connection in addition to other databases. <br>Note that this fix does require a configuration file update, as the old configuration files will not configure properly.&nbsp; An example is shown below, and more information may be found in the Log4cxx documentation on the ODBCAppender.<br></div><div><br></div><div>Example of old configuration snippet:</div><div>&lt;appender name="SqlODBCAppender" class="ODBCAppender"&gt;</div><div>&nbsp;&nbsp;&nbsp; &lt;param name="sql" value="INSERT INTO logs (message) VALUES ('%m')" /&gt;</div><div>&nbsp;&nbsp;&nbsp; ... other params here ...</div><div>&lt;/appender&gt;</div><div><br></div><div>The migrated configuration snippet with new ColumnMapping parameters:<br></div><div>&lt;appender name="SqlODBCAppender" class="ODBCAppender"&gt;<br></div><div><div></div><div>&nbsp; &nbsp; &lt;param name="sql" value="INSERT INTO logs (message) VALUES (?)" /&gt;</div><div>&nbsp;&nbsp;&nbsp; &lt;param name="ColumnMapping" value="message"/&gt;<br>&nbsp;&nbsp;&nbsp; ... other params here ...<br></div><div>&lt;/appender&gt;<br></div><br></div>

### References
* https://lists.apache.org/thread/vgjlpdf353vv91gryspwxrzj6p0fbjd9


## Apache Log4j 1.x (EOL) allows DoS in Chainsaw and SocketAppender ## { #CVE-2023-26464 }

CVE-2023-26464 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-26464) [\[CVE json\]](./CVE-2023-26464.cve.json)

_Last updated: 2023-04-20T07:55:37.341Z_

### Affected

* Apache Log4j from 1.0.4 before 2
* Apache Log4j from 2 through * unaffected


### Description

<div>** UNSUPPORTED WHEN ASSIGNED **</div><div>When using the Chainsaw or SocketAppender components with Log4j 1.x on JRE less than 1.7, an attacker that manages to cause a logging entry involving a specially-crafted (ie, deeply nested) 
hashmap or hashtable (depending on which logging component is in use) to be processed could exhaust the available memory in the virtual machine and achieve Denial of Service when the object is deserialized.</div><div>This issue affects Apache Log4j before 2. Affected users are recommended to update to Log4j 2.x.</div><div>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.<br></div><p></p>

### References
* https://lists.apache.org/thread/wkx6grrcjkh86crr49p4blc1v1nflj3t


### Credits
* Garrett Tucker of Red Hat (reporter)


##  A deserialization flaw in the Chainsaw component of Log4j 1 can lead to malicious code execution. ## { #CVE-2022-23307 }

CVE-2022-23307 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-23307) [\[CVE json\]](./CVE-2022-23307.cve.json) [\[OSV json\]](./CVE-2022-23307.osv.json)



_Last updated: 2022-01-18T15:19:48.077Z_

### Affected

* Apache Log4j 1.x from 1.2.1 before *


### Description

CVE-2020-9493 identified a deserialization issue that was present in Apache Chainsaw. Prior to Chainsaw V2.0 Chainsaw was a component of Apache Log4j 1.2.x where the same issue exists.

### References
* https://lists.apache.org/thread/rg4yyc89vs3dw6kpy3r92xop9loywyhh
* https://logging.apache.org/log4j/1.2/index.html


### Credits
* @kingkk


## SQL injection in JDBC Appender in Apache Log4j V1 ## { #CVE-2022-23305 }

CVE-2022-23305 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-23305) [\[CVE json\]](./CVE-2022-23305.cve.json) [\[OSV json\]](./CVE-2022-23305.osv.json)



_Last updated: 2022-01-18T15:19:05.615Z_

### Affected

* Apache Log4j 1.x  from 1.2.1 before *


### Description

By design, the JDBCAppender in Log4j 1.2.x accepts an SQL statement as a configuration parameter where the values to be inserted are converters from PatternLayout. The message converter, %m, is likely to always be included. This allows attackers to manipulate the SQL by entering crafted strings into input fields or headers of an application that are logged allowing unintended SQL queries to be executed.

Note this issue only affects Log4j 1.x when specifically configured to use the JDBCAppender, which is not the default. Beginning in version 2.0-beta8, the JDBCAppender was re-introduced with proper support for parameterized SQL queries and further customization over the columns written to in logs.

Apache Log4j 1.2 reached end of life in August 2015. Users should upgrade to Log4j 2 as it addresses numerous other issues from the previous versions.

### References
* https://lists.apache.org/thread/pt6lh3pbsvxqlwlp4c5l798dv2hkc85y
* https://logging.apache.org/log4j/1.2/index.html


### Credits
* Daniel Martin of NCC Group


## Deserialization of untrusted data in JMSSink in Apache Log4j 1.x ## { #CVE-2022-23302 }

CVE-2022-23302 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-23302) [\[CVE json\]](./CVE-2022-23302.cve.json) [\[OSV json\]](./CVE-2022-23302.osv.json)



_Last updated: 2022-01-18T16:52:09.053Z_

### Affected

* Apache Log4j 1.x from 1.0.1 before *


### Description

JMSSink in all versions of Log4j 1.x is vulnerable to deserialization of untrusted data when the attacker has write access to the Log4j configuration or if the configuration references an LDAP service the attacker has access to. The attacker can provide a TopicConnectionFactoryBindingName configuration causing JMSSink to perform JNDI requests that result in remote code execution in a similar fashion to CVE-2021-4104.  

Note this issue only affects Log4j 1.x when specifically configured to use JMSSink, which is not the default.

Apache Log4j 1.2 reached end of life in August 2015. Users should upgrade to Log4j 2 as it addresses numerous other issues from the previous versions.

### References
* https://lists.apache.org/thread/bsr3l5qz4g0myrjhy9h67bcxodpkwj4w
* https://logging.apache.org/log4j/1.2/index.html


### Credits
* Eduardo' Vela, Maksim Shudrak and Jacob Butler from Google.


## Apache Log4j2 does not always protect from infinite recursion in lookup evaluation ## { #CVE-2021-45105 }

CVE-2021-45105 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-45105) [\[CVE json\]](./CVE-2021-45105.cve.json) [\[OSV json\]](./CVE-2021-45105.osv.json)



_Last updated: 2021-12-23T21:55:58.182Z_

### Affected

* Apache Log4j2 from log4j-core before 2.17.0


### Description

Apache Log4j2 versions 2.0-alpha1 through 2.16.0 (excluding 2.12.3 and 2.3.1) did not protect from uncontrolled recursion from self-referential lookups. This allows an attacker with control over Thread Context Map data to cause a denial of service when a crafted string is interpreted. This issue was fixed in Log4j 2.17.0, 2.12.3, and 2.3.1.

### References
* https://logging.apache.org/log4j/2.x/security.html
* https://issues.apache.org/jira/browse/LOG4J2-3230


### Credits
* Independently discovered by Hideki Okamoto of Akamai Technologies, Guy Lederfein of Trend Micro Research working with Trend Micro’s Zero Day Initiative, and another anonymous vulnerability researcher


## Apache Log4j2 Thread Context Lookup Pattern vulnerable to remote code execution in certain non-default configurations ## { #CVE-2021-45046 }

CVE-2021-45046 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-45046) [\[CVE json\]](./CVE-2021-45046.cve.json) [\[OSV json\]](./CVE-2021-45046.osv.json)



_Last updated: 2022-02-04T08:46:08.709Z_

### Affected

* Apache Log4j2 from log4j-core before 2.16.0


### Description

It was found that the fix to address CVE-2021-44228 in Apache Log4j 2.15.0 was incomplete in certain non-default configurations. When the logging configuration uses a non-default Pattern Layout with a Context Lookup (for example, $${ctx:loginId}), attackers with control over Thread Context Map (MDC) input data can craft malicious input data using a JNDI Lookup pattern, resulting in an information leak and remote code execution in some environments and local code execution in all environments; remote code execution has been demonstrated in operating systems using glibc with the libnss_resolve provider, glibc versions before 2.28, musl, and systemd-resolvd.

Log4j 2.16.0 (Java 8), 2.12.2 (Java 7), and 2.3.1 (Java 6) fix this issue by removing support for message lookup patterns and disabling JNDI functionality by default.



### References
* https://logging.apache.org/log4j/2.x/security.html
* https://www.cve.org/CVERecord?id=CVE-2021-44228


### Credits
* This issue was discovered by Kai Mindermann of iC Consult and separately by 4ra1n.
* Additional vulnerability details discovered independently by Ash Fox of Google, Alvaro Muñoz and Tony Torralba from GitHub, Anthony Weems of Praetorian, and RyotaK (@ryotkak)


## Apache Log4j2 vulnerable to RCE via JDBC Appender when attacker controls configuration server ## { #CVE-2021-44832 }

CVE-2021-44832 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-44832) [\[CVE json\]](./CVE-2021-44832.cve.json) [\[OSV json\]](./CVE-2021-44832.osv.json)



_Last updated: 2021-12-30T08:25:52.491Z_

### Affected

* Apache Log4j2 from log4j-core before 2.17.1


### Description

Apache Log4j2 versions 2.0-beta7 through 2.17.0 (excluding security fix releases 2.3.2 and 2.12.4) are vulnerable to a remote code execution (RCE) attack when a configuration uses a JDBC Appender with a JNDI LDAP data source URI when an attacker has control of the target LDAP server. This issue is fixed by limiting JNDI data source names to the java protocol in Log4j2 versions 2.17.1, 2.12.4, and 2.3.2.

### References
* https://lists.apache.org/thread/s1o5vlo78ypqxnzn6p8zf6t9shtq5143
* https://issues.apache.org/jira/browse/LOG4J2-3293


## Apache Log4j2 JNDI features do not protect against attacker controlled LDAP and other JNDI related endpoints ## { #CVE-2021-44228 }

CVE-2021-44228 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-44228) [\[CVE json\]](./CVE-2021-44228.cve.json) [\[OSV json\]](./CVE-2021-44228.osv.json)



_Last updated: 2021-12-23T21:53:38.756Z_

### Affected

* Apache Log4j2 from 2.0-beta9 before log4j-core*


### Description

Apache Log4j2 2.0-beta9 through 2.15.0 (excluding security releases 2.12.2, 2.12.3, and 2.3.1) JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. An attacker who can control log messages or log message parameters can execute arbitrary code loaded from LDAP servers when message lookup substitution is enabled. From log4j 2.15.0, this behavior has been disabled by default. From version 2.16.0 (along with 2.12.2, 2.12.3, and 2.3.1), this functionality has been completely removed.

Note that this vulnerability is specific to log4j-core and does not affect log4net, log4cxx, or other Apache Logging Services projects.




### References
* https://logging.apache.org/log4j/2.x/security.html


### Credits
* This issue was discovered by Chen Zhaojun of Alibaba Cloud Security Team.


## Deserialization of untrusted data in JMSAppender in Apache Log4j 1.2 ## { #CVE-2021-4104 }

CVE-2021-4104 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-4104) [\[CVE json\]](./CVE-2021-4104.cve.json) [\[OSV json\]](./CVE-2021-4104.osv.json)



_Last updated: 2022-02-04T08:45:46.335Z_

### Affected

* Apache Log4j 1.x at Apache Log4j 1.2 1.2.x


### Description

JMSAppender in Log4j 1.2 is vulnerable to deserialization of untrusted data when the attacker has write access to the Log4j configuration. The attacker can provide TopicBindingName and TopicConnectionFactoryBindingName configurations causing JMSAppender to perform JNDI requests that result in remote code execution in a similar fashion to CVE-2021-44228.  

Note this issue only affects Log4j 1.2 when specifically configured to use JMSAppender, which is not the default.

Apache Log4j 1.2 reached end of life in August 2015. Users should upgrade to Log4j 2 as it addresses numerous other issues from the previous versions.

### References
* https://www.cve.org/CVERecord?id=CVE-2021-44228
* https://github.com/apache/logging-log4j2/pull/608#issuecomment-990494126
* https://access.redhat.com/security/cve/CVE-2021-4104


## Java deserialization in Chainsaw ## { #CVE-2020-9493 }

CVE-2020-9493 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2020-9493) [\[CVE json\]](./CVE-2020-9493.cve.json) [\[OSV json\]](./CVE-2020-9493.osv.json)



_Last updated: 2021-06-16T07:28:39.802Z_

### Affected

* Apache Chainsaw from Apache Chainsaw before 2.1.0


### Description

A deserialization flaw was found in Apache Chainsaw versions prior to 2.1.0 which could lead to malicious code execution. 

### References
* https://www.openwall.com/lists/oss-security/2021/06/16/1


### Credits
* This issue was reported by @kingkk
