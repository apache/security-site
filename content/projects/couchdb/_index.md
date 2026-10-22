---
title: Apache CouchDB security advisories
description: Security information for Apache CouchDB
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache CouchDB? Send your report to the [Apache CouchDB Security Team](mailto:security@couchdb.apache.org?subject=CouchDB).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Auth bypass in prefixed _users and _replicator databases ## { #CVE-2026-90800 }

CVE-2026-90800 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90800) [\[CVE json\]](./CVE-2026-90800.cve.json) [\[OSV json\]](./CVE-2026-90800.osv.json)



_Last updated: 2026-10-20T15:40:46.476Z_

### Affected

* Apache CouchDB before 3.5.3


### Description

Missing authorisation checks in chttpd in Apache CouchDB 3.5.2 and below on all platforms allows any request to read the full contents of a prefixed _user or _replicator database via an unauthorised API endpoint.<div><br></div><div>The use of prefixed system databases is very rare.<br><br><div>Users are recommended to upgrade to version 3.5.3, which fixes this issue.</div></div>

### References
* https://lists.apache.org/thread.html/pj83174r8f8f64odf47fwhozbfjtot0f
* https://lists.apache.org/thread/vng8vqjwgy1qlrv14wzrgs7pv4gj7gwr


### Credits
* Qing Xu & ZeroVuln Labs reported this issue independently (reporter)


## Atom-table exhaustion in _changes sequences and _search bookmarks with specially crafted sequence values ## { #CVE-2026-90799 }

CVE-2026-90799 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90799) [\[CVE json\]](./CVE-2026-90799.cve.json) [\[OSV json\]](./CVE-2026-90799.osv.json)



_Last updated: 2026-10-20T15:40:15.444Z_

### Affected

* Apache CouchDB before 3.5.3


### Description

Unsafe binary deserialisation in chttpd in Apache CouchDB 3.5.2 and below on all platforms allows an authenticated user to cause a denial of service via memory exhaustion.<br><br><div>Users are recommended to upgrade to version 3.5.3, which fixes this issue.</div>

### References
* https://lists.apache.org/thread.html/pj83174r8f8f64odf47fwhozbfjtot0f
* https://lists.apache.org/thread/bqxkm19hw8985t7opz675b29hs1zl4z9


### Credits
* Piotr Karwasz & ZeroVuln Labs reported this issue independently (finder)


## Replicator follows redirects indefinitely ## { #CVE-2026-90798 }

CVE-2026-90798 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90798) [\[CVE json\]](./CVE-2026-90798.cve.json) [\[OSV json\]](./CVE-2026-90798.osv.json)



_Last updated: 2026-10-20T15:39:50.951Z_

### Affected

* Apache CouchDB before 3.5.3


### Description

A missing circuit-breaker in the replicator in Apache CouchDB 3.5.2 and below on all platforms allows the owner of a replication source or target to cause a denial of service via creating an infinite HTTP redirect loop.<br><br><div>Users are recommended to upgrade to version 3.5.3, which fixes this issue.</div>

### References
* https://lists.apache.org/thread.html/pj83174r8f8f64odf47fwhozbfjtot0f
* https://lists.apache.org/thread/m6d526fj57pvq5pswm2lp1shbdz3f417


### Credits
* The Apache CouchDB Team (finder)


## Pre-authentication gzip decompression bomb via POST /_session ## { #CVE-2026-90797 }

CVE-2026-90797 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-90797) [\[CVE json\]](./CVE-2026-90797.cve.json) [\[OSV json\]](./CVE-2026-90797.osv.json)



_Last updated: 2026-10-20T15:39:22.336Z_

### Affected

* Apache CouchDB before 3.5.3


### Description

An unlimited gzip decompression routine in chttpd in Apache CouchDB 3.5.2 and below on all platforms allows any remote client to cause a denial of service via memory exhaustion.<div><br>Users are recommended to upgrade to version 3.5.3, which fixes this issue.</div>

### References
* https://lists.apache.org/thread.html/pj83174r8f8f64odf47fwhozbfjtot0f
* https://lists.apache.org/thread/gsbotof0qn8x6zlpd7t568ny4053jo0n


### Credits
* ZeroVuln labs (reporter)


## Admin credentials leading to code execution as operating system user ## { #CVE-2026-86471 }

CVE-2026-86471 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86471) [\[CVE json\]](./CVE-2026-86471.cve.json) [\[OSV json\]](./CVE-2026-86471.osv.json)



_Last updated: 2026-10-20T15:38:08.323Z_

### Affected

* Apache CouchDB before 3.5.3


### Description

An unvalidated runtime configuration value in Apache CouchDB 3.5.2 and below on all platforms allows a CouchDB server admin to run arbitrary shell commands as the CouchDB operating system user.<br><br><div>Users are recommended to upgrade to version 3.5.3, which fixes this issue.</div>

### References
* https://lists.apache.org/thread.html/pj83174r8f8f64odf47fwhozbfjtot0f
* https://lists.apache.org/thread/c8p73gswgogtnzvk7hpw8jb8d4mnosdp


## Credential Disclosure to Non-Owner Members via Object-Form Replication Endpoint URLs ## { #CVE-2026-107755 }

CVE-2026-107755 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-107755) [\[CVE json\]](./CVE-2026-107755.cve.json) [\[OSV json\]](./CVE-2026-107755.osv.json)



_Last updated: 2026-10-20T15:41:21.272Z_

### Affected

* Apache CouchDB before 3.5.3


### Description

Insufficient filtering of credentials in the _replicator database in Apache CouchDB 3.5.2 and below on all platforms allows an authenticated user to read replication credentials of other users’ replications, not just their own.<br><br><div>Users are recommended to upgrade to version 3.5.3, which fixes this issue.</div>

### References
* https://lists.apache.org/thread.html/pj83174r8f8f64odf47fwhozbfjtot0f
* https://lists.apache.org/thread/ro57p4r2lhxn2n4712ppx7r11oqq900n


### Credits
* Sakil Ahamed Gayen (reporter)


## Privilege Escalation Using _design Documents ## { #CVE-2023-45725 }

CVE-2023-45725 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-45725) [\[CVE json\]](./CVE-2023-45725.cve.json) [\[OSV json\]](./CVE-2023-45725.osv.json)



_Last updated: 2023-12-13T08:02:15.239Z_

### Affected

* Apache CouchDB through 3.3.2
* IBM Cloudant before 8413


### Description

Design document functions which receive a user http request object may expose authorization or session cookie headers of the user who accesses the document.<br><br>These design document functions are:<br><ul><li>&nbsp; list</li><li>&nbsp; show</li><li>&nbsp; rewrite</li><li>&nbsp; update</li></ul>An attacker can leak the session component using an HTML-like output, insert the session as an external resource (such as an image), or store the credential in a _local document with an "update" function.<br><br>For the attack to succeed the attacker has to be able to insert the design documents into the database, then manipulate a user to access a function from that design document.<br><br>Workaround: Avoid using design documents from untrusted sources which may attempt to access or manipulate request object's headers<br>

### References
* https://lists.apache.org/thread/pqjq9zt8vq9rsobkc1cow9sqm9vozlrg
* https://docs.couchdb.org/en/stable/cve/2023-45725.html


### Credits
* Natan Nehorai from the JFrog Vulnerability Research Team (finder)
* Or Peles from the JFrog Vulnerability Research Team (reporter)
* Richard Ellis from IBM/Cloudant Team (finder)
* Mike Rhodes from IBM/Cloudant Team (finder)


## Information sharing via couchjs processes ## { #CVE-2023-26268 }

CVE-2023-26268 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-26268) [\[CVE json\]](./CVE-2023-26268.cve.json) [\[OSV json\]](./CVE-2023-26268.osv.json)



_Last updated: 2023-12-12T22:58:48.382Z_

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


## Remote Code Execution Vulnerability in Packaging ## { #CVE-2022-24706 }

CVE-2022-24706 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-24706) [\[CVE json\]](./CVE-2022-24706.cve.json) [\[OSV json\]](./CVE-2022-24706.osv.json)



_Last updated: 2022-04-26T09:18:02.724Z_

### Affected

* Apache CouchDB from Apache CouchDB through 3.2.1


### Description

In Apache CouchDB prior to 3.2.2, an attacker can access an improperly secured default installation without authenticating and gain admin privileges.  The CouchDB documentation has always made recommendations for properly securing an installation, including recommending using a firewall in front of all CouchDB installations.


### References
* https://lists.apache.org/thread/w24wo0h8nlctfps65txvk0oc5hdcnv00
* https://docs.couchdb.org/en/3.2.2/setup/cluster.html


### Credits
* The Apache CouchDB Team would like to thank Alex Vandiver <alexmv@zulip.com> for the report of this issue.


## Privilege escalation vulnerability when using HTML attachments ## { #CVE-2021-38295 }

CVE-2021-38295 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-38295) [\[CVE json\]](./CVE-2021-38295.cve.json) [\[OSV json\]](./CVE-2021-38295.osv.json)



_Last updated: 2021-10-14T16:26:03.894Z_

### Affected

* Apache CouchDB from Apache CouchDB before 3.1.2
* IBM Cloudant from IBM Cloudant before 8201


### Description

In Apache CouchDB, a malicious user with permission to create documents in a database is able to attach a HTML attachment to a document. If a CouchDB admin opens that attachment in a browser, e.g. via the CouchDB admin interface Fauxton, any JavaScript code embedded in that HTML attachment will be executed within the security context of that admin. A similar route is available with the already deprecated _show and _list functionality.

This privilege escalation vulnerability allows an attacker to add or remove data in any database or make configuration changes.  This issue affected Apache CouchDB prior to 3.1.2

### References
* https://docs.couchdb.org/en/stable/cve/2021-38295.html


### Credits
* This issue was identified by Cory Sabol of Secure Ideas.
