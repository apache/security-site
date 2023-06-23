---
title: Apache CouchDB security advisories
description: Security information for Apache CouchDB
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache CouchDB? You can read more about the projects' security policy on their [security page](None), and email your report to the  [Apache CouchDB Security Team](mailto:security@couchdb.apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache CouchDB since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. It may also lack details found on the [project security page](None).

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Information sharing via couchjs processes ## { #CVE-2023-26268 }

[CVE-2023-26268](./CVE-2023-26268.cve.json)

### Affected

* Apache CouchDB versions  including 3.3.1
* IBM Cloudant versions  including 8349


### Description

<span style="background-color: rgb(255, 255, 255);">Design documents with matching document IDs, from databases on the same cluster, may share a mutable Javascript environment when using these design document functions:<br><ul><li><span style="background-color: rgb(255, 255, 255);">validate_doc_update<br></span></li><li><span style="background-color: rgb(255, 255, 255);">list<br></span></li><li><span style="background-color: rgb(255, 255, 255);">filter<br></span></li><li><span style="background-color: rgb(255, 255, 255);">filter views (using view functions as filters)<br></span></li><li><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">r</span><span style="background-color: rgb(255, 255, 255);">ewrite</span><br></span></li><li><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">update<br></span></span></li></ul></span><div><span style="background-color: rgb(255, 255, 255);">This doesn't affect map/reduce or search (Dreyfus) index functions.</span></div><div><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to a version that is no longer affected by this issue (Apache CouchDB 3.3.2 or 3.2.3).</span></span></div><div><span style="background-color: rgb(255, 255, 255);">Workaround: Avoid using design documents from untrusted sources which may attempt to cache or store data in the Javascript environment.</span></div>