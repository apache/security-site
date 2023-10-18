---
title: Apache Ozone security advisories
description: Security information for Apache Ozone
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Ozone? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Ozone S3 Gateway allows bucket and key access to non authenticated users  ## { #CVE-2020-17517 }

CVE-2020-17517 [\[CVE json\]](./CVE-2020-17517.cve.json)

### Affected

* Apache Ozone from Apache Ozone through 1.0.0


### Description

The S3 buckets and keys in a secure Apache Ozone Cluster must be inaccessible to anonymous access by default. The current security vulnerability allows access to keys and buckets through a curl command or an unauthenticated HTTP request. This enables unauthorized access to buckets and keys thereby exposing data to anonymous clients or users.  This affected Apache Ozone prior to the 1.1.0 release.


### References
* https://lists.apache.org/thread.html/rdd59a176b32c63f7fc0865428bf9bbc69297fa17f6130c80c25869aa%40%3Cdev.ozone.apache.org%3E


### Credits
* Apache Ozone would like to thank Kota Uenishi for reporting this issue.


## Original block tokens are persisted and can be retrieved ## { #CVE-2021-36372 }

CVE-2021-36372 [\[CVE json\]](./CVE-2021-36372.cve.json)

### Affected

* Apache Ozone from 1.1 through 1.1


### Description

In Apache Ozone versions prior to 1.2.0, Initially generated block tokens are persisted to the metadata database and can be retrieved with authenticated users with permission to the key. Authenticated users may use them even after access is revoked. 

### References
* https://mail-archives.apache.org/mod_mbox/ozone-dev/202111.mbox/%3C5029c1ac-4685-8492-e3cb-ab48c5c370cf%40apache.org%3E


### Credits
* Apache Ozone would like to thank Marton Elek for reporting this issue.


## Missing authentication/authorization on internal RPC endpoints ## { #CVE-2021-39231 }

CVE-2021-39231 [\[CVE json\]](./CVE-2021-39231.cve.json)

### Affected

* Apache Ozone from 1.0 through 1.0


### Description

In Apache Ozone versions prior to 1.2.0, Various internal server-to-server RPC endpoints are available for connections, making it possible for an attacker to download raw data from Datanode and Ozone manager and modify Ratis replication configuration. 

### References
* https://mail-archives.apache.org/mod_mbox/ozone-dev/202111.mbox/%3C110cd117-75ed-364b-cd38-3effd20f2183%40apache.org%3E


### Credits
* Apache Ozone would like to thank Marton Elek for reporting this issue.


## Missing admin check for SCM related admin commands ## { #CVE-2021-39232 }

CVE-2021-39232 [\[CVE json\]](./CVE-2021-39232.cve.json)

### Affected

* Apache Ozone from 1.0 through 1.0


### Description

In Apache Ozone versions prior to 1.2.0, certain admin related SCM commands can be executed by any authenticated users, not just by admins. 

### References
* https://mail-archives.apache.org/mod_mbox/ozone-dev/202111.mbox/%3C3c30a7f2-13a4-345e-6c8a-c23a2b937041%40apache.org%3E


### Credits
*     Apache Ozone would like to thank Wei-Chiu Chuang for reporting this issue.


## Container-related datanode operations can be called without authorization ## { #CVE-2021-39233 }

CVE-2021-39233 [\[CVE json\]](./CVE-2021-39233.cve.json)

### Affected

* Apache Ozone from 1.1 through 1.1


### Description

In Apache Ozone versions prior to 1.2.0, Container related Datanode requests of Ozone Datanode were not properly authorized and can be called by any client. 

### References
* https://mail-archives.apache.org/mod_mbox/ozone-dev/202111.mbox/%3C394a9a73-44dd-b5db-84d8-607c3226eb00%40apache.org%3E


### Credits
* Apache Ozone would like to thank Marton Elek for reporting this issue.


## Raw block data can be read bypassing ACL/authorization ## { #CVE-2021-39234 }

CVE-2021-39234 [\[CVE json\]](./CVE-2021-39234.cve.json)

### Affected

* Apache Ozone from 1.1 through 1.1


### Description

In Apache Ozone versions prior to 1.2.0, Authenticated users knowing the ID of an existing block can craft specific request allowing access those blocks, bypassing other security checks like ACL. 

### References
* https://mail-archives.apache.org/mod_mbox/ozone-dev/202111.mbox/%3C97d65498-7f8c-366f-1bea-5a74b6378f0d%40apache.org%3E


### Credits
* Apache Ozone would like to thank Marton Elek for reporting this issue.


## Access mode of block tokens are not enforced ## { #CVE-2021-39235 }

CVE-2021-39235 [\[CVE json\]](./CVE-2021-39235.cve.json)

### Affected

* Apache Ozone from 1.0 through 1.0


### Description

In Apache Ozone before 1.2.0, Ozone Datanode doesn't check the access mode parameter of the block token. Authenticated users with valid READ block token can do any write operation on the same block. 

### References
* https://mail-archives.apache.org/mod_mbox/ozone-dev/202111.mbox/%3C93f88246-4320-7423-0dac-ec7a07f47455%40apache.org%3E


### Credits
* Apache Ozone would like to thank Marton Elek for reporting this issue.


## Owners of the S3 tokens are not validated ## { #CVE-2021-39236 }

CVE-2021-39236 [\[CVE json\]](./CVE-2021-39236.cve.json)

### Affected

* Apache Ozone from 1.0 through 1.0


### Description

In Apache Ozone before 1.2.0, Authenticated users with valid Ozone S3 credentials can create specific OM requests, impersonating any other user. 

### References
* https://mail-archives.apache.org/mod_mbox/ozone-dev/202111.mbox/%3C0fd74baa-88a0-39a2-8f3a-b982acb25d5a%40apache.org%3E


### Credits
* Apache Ozone would like to thank Marton Elek for reporting this issue.


## Unauthenticated access to Ozone Recon HTTP endpoints ## { #CVE-2021-41532 }

CVE-2021-41532 [\[CVE json\]](./CVE-2021-41532.cve.json)

### Affected

* Apache Ozone from Everglades (1.1.0) through 1.1.0


### Description

In Apache Ozone before 1.2.0, Recon HTTP endpoints provide access to OM, SCM and Datanode metadata. Due to a bug, any unauthenticated user can access the data from these endpoints.

### References
* https://mail-archives.apache.org/mod_mbox/ozone-dev/202111.mbox/%3Ce0bc6598-9669-b897-fc28-de8a896e36aa%40apache.org%3E


### Credits
* Apache Ozone would like to thank Ethan Rose for reporting this issue.
