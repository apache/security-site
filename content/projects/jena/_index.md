---
title: Apache Jena security advisories
description: Security information for Apache Jena
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Jena? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Display information UI XSS ## { #CVE-2021-33192 }

CVE-2021-33192 [\[CVE json\]](./CVE-2021-33192.cve.json)

_Last updated: 2021-07-05T09:09:33.148Z_

### Affected

* Apache Jena Fuseki at Apache Jena Fuseki2 2.0.0 to 4.0.0


### Description

A vulnerability in the HTML pages of Apache Jena Fuseki allows an attacker to execute arbitrary javascript on certain page views.  This issue affects Apache Jena Fuseki from version 2.0.0 to version 4.0.0 (inclusive).

### References
* https://lists.apache.org/thread.html/r684d8943d755a96fe90f8cd8df196737b6bde3f2b74e15a9bd479975%40%3Cusers.jena.apache.org%3E


### Credits
* Apache Jena would like to thank Luka Safonov for reporting this issue.


## XML External Entity (XXE) vulnerability ## { #CVE-2021-39239 }

CVE-2021-39239 [\[CVE json\]](./CVE-2021-39239.cve.json)

_Last updated: 2021-09-16T14:16:06.658Z_

### Affected

* Apache Jena from unspecified before 4.1.0


### Description

A vulnerability in XML processing in Apache Jena, in versions up to 4.1.0, may allow an attacker to execute XML External Entities (XXE), including exposing the contents of local files to a remote server.

### References
* https://lists.apache.org/thread.html/rf44d529c54ef1d0097e813f576a0823a727e1669a9f610d3221d493d%40%3Cusers.jena.apache.org%3E


## Processing external DTDs ## { #CVE-2022-28890 }

CVE-2022-28890 [\[CVE json\]](./CVE-2022-28890.cve.json)

_Last updated: 2022-05-05T08:34:36.622Z_

### Affected

* Apache Jena from Apache Jena through 4.4.0


### Description

A vulnerability in the RDF/XML parser of Apache Jena allows an attacker to cause an external DTD to be retrieved.  This issue affects Apache Jena version 4.4.0 and prior versions.  Apache Jena 4.2.x and 4.3.x do not allow external entities.

### References
* https://lists.apache.org/thread/h88oh642455wljo0p5jgzs9phk4gj878


### Credits
* Apache Jena would like to thank Feras Daragma, Avishag Shapira & Amit Laish (GE Digital, Cyber Security Lab) for their report.


## Apache Jena SDB allows arbitrary deserialisation via JDBC ## { #CVE-2022-45136 }

CVE-2022-45136 [\[CVE json\]](./CVE-2022-45136.cve.json)

_Last updated: 2022-11-14T15:41:09.479Z_

### Affected

* Apache Jena SDB from unspecified through 3.17.0


### Description

Apache Jena SDB 3.17.0 and earlier is vulnerable to a JDBC Deserialisation attack if the attacker is able to control the JDBC URL used or cause the underlying database server to return malicious data.  The mySQL JDBC driver in particular is known to be vulnerable to this class of attack.  As a result an application using Apache Jena SDB can be subject to RCE when connected to a malicious database server.

Apache Jena SDB has been EOL since December 2020 and users should migrate to alternative options e.g. Apache Jena TDB 2

### References
* https://lists.apache.org/thread/mc77cdl5stgjtjoldk467gdf756qjt31


### Credits
* Apache Jena would like to thank Crilwa & LaNyer640 for reporting this issue


## Exposure of arbitrary execution in script engine expressions. ## { #CVE-2023-22665 }

CVE-2023-22665 [\[CVE json\]](./CVE-2023-22665.cve.json)

_Last updated: 2023-04-25T07:09:43.803Z_

### Affected

* Apache Jena through 4.7.0


### Description

There is insufficient checking of user queries in Apache Jena versions 4.7.0 and earlier, when invoking custom scripts. It allows a remote user to execute arbitrary javascript via a SPARQL query.

### References
* https://lists.apache.org/thread/s0dmpsxcwqs57l4qfs415klkgmhdxq7s


### Credits
* L3yx of Syclover Security Team (reporter)


## Exposure of execution in script engine expressions. ## { #CVE-2023-32200 }

CVE-2023-32200 [\[CVE json\]](./CVE-2023-32200.cve.json)

_Last updated: 2023-07-12T07:50:01.786Z_

### Affected

* Apache Jena from 3.7.0 through 4.8.0


### Description

There is insufficient restrictions of called script functions in Apache Jena
 versions 4.8.0 and earlier. It allows a 
remote user to execute javascript via a SPARQL query.<br><p>This issue affects Apache Jena: from 3.7.0 through 4.8.0.</p>

### References
* https://www.cve.org/CVERecord?id=CVE-2023-22665
* https://lists.apache.org/thread/7hg0t2kws3fyr75dl7lll8389xzzc46z


### Credits
* s3gundo of Alibaba (reporter)
