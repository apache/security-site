---
title: Apache Logging security advisories
description: Security information for Apache Logging
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Logging? You can read more about the projects' security policy on their [security page](None), and email your report to the  [Apache Logging Security Team](mailto:security@logging.apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache Logging since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. It may also lack details found on the [project security page](None).

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Apache Log4j 1.x (EOL) allows DoS in Chainsaw and SocketAppender ## { #CVE-2023-26464 }

[CVE-2023-26464](./CVE-2023-26464.cve.json)

### Affected

* Apache Log4j from 1.0.4 before 2
* Apache Log4j from 2 through *


### Description

<div>** UNSUPPORTED WHEN ASSIGNED **</div><div>When using the Chainsaw or SocketAppender components with Log4j 1.x on JRE less than 1.7, an attacker that manages to cause a logging entry involving a specially-crafted (ie, deeply nested) 
hashmap or hashtable (depending on which logging component is in use) to be processed could exhaust the available memory in the virtual machine and achieve Denial of Service when the object is deserialized.</div><div>This issue affects Apache Log4j before 2. Affected users are recommended to update to Log4j 2.x.</div><div>NOTE: This vulnerability only affects products that are no longer supported by the maintainer.<br></div><p></p>

## SQL injection when using ODBC appender ## { #CVE-2023-31038 }

[CVE-2023-31038](./CVE-2023-31038.cve.json)

### Affected

* Apache Log4cxx from 0.9.0 before 1.1.0


### Description

<div>SQL injection in Log4cxx when using the ODBC appender to send log messages to a database.&nbsp; No fields sent to the database were properly escaped for SQL injection.&nbsp; This has been the case since at least version 0.9.0(released 2003-08-06)</div><div><br></div><div>Note that Log4cxx is a C++ framework, so only C++ applications are affected.</div><div>Before version 1.1.0, the ODBC appender was automatically part of Log4cxx if the library was found when compiling the library.&nbsp; As of version 1.1.0, this must be both explicitly enabled in order to be compiled in.</div><div><br></div><div>Three preconditions must be met for this vulnerability to be possible:</div><div>1. Log4cxx compiled with ODBC support(before version 1.1.0, this was auto-detected at compile time)</div><div>2. ODBCAppender enabled for logging messages to, generally done via a config file</div><div>3. User input is logged at some point. If your application does not have user input, it is unlikely to be affected.<br></div><div><br></div><div>Users are recommended to upgrade to version 1.1.0 which properly binds the parameters to the SQL statement, or migrate to the new DBAppender class which supports an ODBC connection in addition to other databases. <br>Note that this fix does require a configuration file update, as the old configuration files will not configure properly.&nbsp; An example is shown below, and more information may be found in the Log4cxx documentation on the ODBCAppender.<br></div><div><br></div><div>Example of old configuration snippet:</div><div>&lt;appender name="SqlODBCAppender" class="ODBCAppender"&gt;</div><div>&nbsp;&nbsp;&nbsp; &lt;param name="sql" value="INSERT INTO logs (message) VALUES ('%m')" /&gt;</div><div>&nbsp;&nbsp;&nbsp; ... other params here ...</div><div>&lt;/appender&gt;</div><div><br></div><div>The migrated configuration snippet with new ColumnMapping parameters:<br></div><div>&lt;appender name="SqlODBCAppender" class="ODBCAppender"&gt;<br></div><div><div></div><div>&nbsp; &nbsp; &lt;param name="sql" value="INSERT INTO logs (message) VALUES (?)" /&gt;</div><div>&nbsp;&nbsp;&nbsp; &lt;param name="ColumnMapping" value="message"/&gt;<br>&nbsp;&nbsp;&nbsp; ... other params here ...<br></div><div>&lt;/appender&gt;<br></div><br></div>