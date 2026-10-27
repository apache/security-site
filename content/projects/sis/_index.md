---
title: Apache SIS security advisories
description: Security information for Apache SIS
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache SIS? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=SIS).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## CWE-22: improper limitation of paths to GML, GeoTIFF, NADCON or NTv2 files ## { #CVE-2026-110748 }

CVE-2026-110748 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-110748) [\[CVE json\]](./CVE-2026-110748.cve.json) [\[OSV json\]](./CVE-2026-110748.osv.json)



_Last updated: 2026-10-26T14:32:07.621Z_

### Affected

* Apache SIS from 0.7 through 1.6.0


### Description

<p>This issue affects Apache SIS from version 0.7 through 1.6 inclusive. When a data file contains links to other files, Apache SIS opened these files regardless their paths. It was possible, for example, to specify a path to a local file. However, these files were always expected to be in some specific formats and the reading stops at the first parsing error, which makes this vulnerability unlikely to leak sensitive information. The impacted formats are:</p><ul><li>Geographic Markup Language (GML) with `xlink:href` attributes for other files in GML format.</li><li>Well Known Text (WKT) with parameter elements for datum shift grids in NADCON, NTv2 or RGF93 formats.</li><li>Landsat scene with paths to files for each band in the GeoTIFF format.</li></ul><p>Users are recommended to upgrade to version 1.7, which fixes the issue by restricting the paths to the same directory as the file containing the references to other files, or to a predetermined directory for datum shift grids.</p>

### References
* https://lists.apache.org/thread.html/j43dd1okv97o0qygbox381l01rsszsln


### Credits
* n0mi1k Security (finder)
* Ho1aAs <xxy010605@gmail.com> (finder)


## SQL injection via unvalidated ORDER BY sort expression in the SQL feature store ## { #CVE-2026-110733 }

CVE-2026-110733 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-110733) [\[CVE json\]](./CVE-2026-110733.cve.json) [\[OSV json\]](./CVE-2026-110733.osv.json)



_Last updated: 2026-10-26T11:13:03.112Z_

### Affected

* Apache SIS from 1.0 through 1.6.0


### Description

<p>Vulnerability in the SQL storage module of Apache SIS. When sorting a stream of features, the clause is copied after <code>ORDER BY</code> without quoting the identifier character. A crafter sort clause could inject SQL in the query.</p>

<p>This issue affects the <code>sql-storage</code> module of Apache SIS from version 1.0 through 1.6 inclusive. Other modules such as <code>sis-referencing</code> are not impacted. Users are recommended to upgrade to version 1.7, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/j43dd1okv97o0qygbox381l01rsszsln


### Credits
* Ho1aAs <xxy010605@gmail.com> (reporter)


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
