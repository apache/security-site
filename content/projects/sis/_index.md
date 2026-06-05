---
title: Apache SIS security advisories
description: Security information for Apache SIS
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache SIS? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## XML External Entity (XXE) vulnerability ## { #CVE-2025-68280 }

CVE-2025-68280 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-68280) [\[CVE json\]](./CVE-2025-68280.cve.json) [\[OSV json\]](./CVE-2025-68280.osv.json)



_Last updated: 2026-04-10T15:58:12.739Z_

### Affected

* Apache SIS from 0.4 through 1.5


### Description

<p>Improper Restriction of XML External Entity Reference vulnerability in Apache SIS.</p>

<p>It is possible to write XML files in such a way that, when parsed by Apache SIS, an XML file reveals to the attacker the content of a local file on the server running Apache SIS. This vulnerability impacts the following SIS services:</p>

<ul>
<li>Reading of GeoTIFF files having the GEO_METADATA tag defined by the Defense Geospatial Information Working Group (DGIWG).</li>
<li>Parsing of ISO 19115 metadata in XML format.</li>
<li>Parsing of Coordinate Reference Systems defined in the GML format.</li>
<li>Parsing of files in GPS Exchange Format (GPX).</li>
</ul>

<p>This issue affects Apache SIS from versions 0.4 through 1.5 inclusive. Users are recommended to upgrade to version 1.6, which will fix the issue. In the meantime, the security vulnerability can be avoided by launching Java with the <code>javax.xml.accessExternalDTD</code> system property sets to a comma-separated list of authorized protocols. For example:</p>

<pre>java -Djavax.xml.accessExternalDTD="" ...</pre>

### References
* https://lists.apache.org/thread/s4ggy3zbtrrn93glgo2vn52lgcxk4bp4


### Credits
* LEE (finder)
