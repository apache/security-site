---
title: Apache Isis security advisories
description: Security information for Apache Isis
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Isis? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## XSS vulnerability, eg for String properties. ## { #CVE-2022-42466 }

CVE-2022-42466 [\[CVE json\]](./CVE-2022-42466.cve.json)

_Last updated: 2022-10-19T07:20:06.791Z_

### Affected

* Apache Isis from unspecified before 2.0.0-M9


### Description

Prior to 2.0.0-M9, it was possible for an end-user to set the value of an editable string property of a domain object to a value that would be rendered unchanged when the value was saved.  In particular, the end-user could enter javascript or similar and this would be executed.

As of this release, the inputted strings are properly escaped when rendered.

### References
* https://lists.apache.org/thread/83ftj5jgtv3mbm28w3trjyvd591jztrz


### Credits
* Apache Isis would like to thank Qing Xu for reporting this issue


## h2 webconsole (available only in prototype mode) should nevertheless be disabled by default. ## { #CVE-2022-42467 }

CVE-2022-42467 [\[CVE json\]](./CVE-2022-42467.cve.json)

_Last updated: 2022-10-19T07:19:59.555Z_

### Affected

* Apache Isis from Apache Isis before 2.0.0-M8


### Description

When running in prototype mode, the h2 webconsole module (accessible from the Prototype menu) is automatically made available with the ability to directly query the database.  

It was felt that it is safer to require the developer to explicitly enable this capability.  As of 2.0.0-M8, this can now be done using the 'isis.prototyping.h2-console.web-allow-remote-access'  configuration property; the web console will be unavailable without setting this configuration.  

As an additional safeguard, the new 'isis.prototyping.h2-console.generate-random-web-admin-password' configuration parameter (enabled by default) requires that the administrator use a randomly generated password to use the console.  The password is printed to the log, as "webAdminPass: xxx" (where "xxx") is the password.  

To revert to the original behaviour, the administrator would therefore need to set these configuration parameter:

    isis.prototyping.h2-console.web-allow-remote-access=true
    isis.prototyping.h2-console.generate-random-web-admin-password=false

Note also that the h2 webconsole is never available in production mode, so these safeguards are only to ensure that the webconsole is secured by default also in prototype mode.  

### References
* https://lists.apache.org/thread/jbv2ddt00h7ntlbm6vkk4wdmb31pm8q3


### Credits
* William Thomson
