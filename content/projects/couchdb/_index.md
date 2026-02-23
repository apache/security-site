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
