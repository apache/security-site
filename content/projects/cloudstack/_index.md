---
title: Apache CloudStack security advisories
description: Security information for Apache CloudStack
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache CloudStack? You can read more about the projects' security policy on their [security page](https://cloudstack.apache.org/security.html), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://cloudstack.apache.org/security.html). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Cloudstack insecure random number generation affects project email invitation ## { #CVE-2022-26779 }

CVE-2022-26779 [\[CVE json\]](./CVE-2022-26779.cve.json)

_Last updated: 2022-07-13T11:28:52.383Z_

### Affected

* Apache CloudStack from Apache CloudStack before 4.16.1


### Description

Apache CloudStack prior to 4.16.1.0 used insecure random number generation for project invitation tokens. If a project invite is created based only on an email address, a random token is generated. An attacker with knowledge of the project ID and the fact that the invite is sent, could generate time deterministic tokens and brute force attempt to use them prior to the legitimate receiver accepting the invite. This feature is not enabled by default, the attacker is required to know or guess the project ID for the invite in addition to the invitation token, and the attacker would need to be an existing authorized user of CloudStack.

### References
* https://lists.apache.org/thread/dmm07b1cyosovqr12ddhkko501p11h2h
* https://github.com/JLLeitschuh/security-research/security/advisories/GHSA-vpcc-9rh2-8jfp


### Credits
* This issue was reported by Jonathan Leitschuh


## Apache CloudStack SAML Single Sign-On XXE ## { #CVE-2022-35741 }

CVE-2022-35741 [\[CVE json\]](./CVE-2022-35741.cve.json)

_Last updated: 2022-07-18T14:26:13.768Z_

### Affected

* Apache CloudStack from 4.5.0 before Apache CloudStack*


### Description

Apache CloudStack version 4.5.0 and later has a SAML 2.0 authentication Service Provider plugin which is found to be vulnerable to XML external entity (XXE) injection. This plugin is not enabled by default and the attacker would require that this plugin be enabled to exploit the vulnerability. When the SAML 2.0 plugin is enabled in affected versions of Apache CloudStack could potentially allow the exploitation of XXE vulnerabilities. The SAML 2.0 messages constructed during the authentication flow in Apache CloudStack are XML-based and the XML data is parsed by various standard libraries that are now understood to be vulnerable to XXE injection attacks such as arbitrary file reading, possible denial of service, server-side request forgery (SSRF) on the CloudStack management server.

### References
* https://lists.apache.org/thread/hwhxvtwp1d5dsm156bsf1cnyvtmrfv3f


### Credits
* This issue was reported by v3ged0ge
