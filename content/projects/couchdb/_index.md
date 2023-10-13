---
title: Apache CouchDB security advisories
description: Security information for Apache CouchDB
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache CouchDB? Send your report to the [Apache CouchDB Security Team](mailto:security@couchdb.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Information sharing via couchjs processes ## { #CVE-2023-26268 }

CVE-2023-26268 [\[CVE json\]](./CVE-2023-26268.cve.json)

### Affected

* Apache CouchDB through 3.3.1
* IBM Cloudant through 8349


### Description

<span style="background-color: rgb(255, 255, 255);">Design documents with matching document IDs, from databases on the same cluster, may share a mutable Javascript environment when using these design document functions:<br><ul><li><span style="background-color: rgb(255, 255, 255);">validate_doc_update<br></span></li><li><span style="background-color: rgb(255, 255, 255);">list<br></span></li><li><span style="background-color: rgb(255, 255, 255);">filter<br></span></li><li><span style="background-color: rgb(255, 255, 255);">filter views (using view functions as filters)<br></span></li><li><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">r</span><span style="background-color: rgb(255, 255, 255);">ewrite</span><br></span></li><li><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">update<br></span></span></li></ul></span><div><span style="background-color: rgb(255, 255, 255);">This doesn't affect map/reduce or search (Dreyfus) index functions.</span></div><div><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to a version that is no longer affected by this issue (Apache CouchDB 3.3.2 or 3.2.3).</span></span></div><div><span style="background-color: rgb(255, 255, 255);">Workaround: Avoid using design documents from untrusted sources which may attempt to cache or store data in the Javascript environment.</span></div>

### References
* https://lists.apache.org/thread/r2wvjfysg3d92lhhjd1qh3wfr8mlp0pp
* https://docs.couchdb.org/en/stable/cve/2023-26268.html
* https://lists.apache.org/thread/ldkqs0nhpmho26bdxf4fon7w75hsq5gl


### Credits
* Nick Vatamaniuc vatamane@apache.org (finder)
