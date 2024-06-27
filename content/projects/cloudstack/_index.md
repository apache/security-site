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

CVE-2022-26779 [\[CVE json\]](./CVE-2022-26779.cve.json) [\[OSV json\]](./CVE-2022-26779.osv.json)



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

CVE-2022-35741 [\[CVE json\]](./CVE-2022-35741.cve.json) [\[OSV json\]](./CVE-2022-35741.osv.json)



_Last updated: 2022-07-18T14:26:13.768Z_

### Affected

* Apache CloudStack from 4.5.0 before Apache CloudStack*


### Description

Apache CloudStack version 4.5.0 and later has a SAML 2.0 authentication Service Provider plugin which is found to be vulnerable to XML external entity (XXE) injection. This plugin is not enabled by default and the attacker would require that this plugin be enabled to exploit the vulnerability. When the SAML 2.0 plugin is enabled in affected versions of Apache CloudStack could potentially allow the exploitation of XXE vulnerabilities. The SAML 2.0 messages constructed during the authentication flow in Apache CloudStack are XML-based and the XML data is parsed by various standard libraries that are now understood to be vulnerable to XXE injection attacks such as arbitrary file reading, possible denial of service, server-side request forgery (SSRF) on the CloudStack management server.

### References
* https://lists.apache.org/thread/hwhxvtwp1d5dsm156bsf1cnyvtmrfv3f


### Credits
* This issue was reported by v3ged0ge


## x-forwarded-for HTTP header parsed by default ## { #CVE-2024-29006 }

CVE-2024-29006 [\[CVE json\]](./CVE-2024-29006.cve.json) [\[OSV json\]](./CVE-2024-29006.osv.json)



_Last updated: 2024-04-04T10:59:16.384Z_

### Affected

* Apache CloudStack from 4.11.0.0 through 4.18.1.0, 4.19.0.0


### Description

<div>By default the CloudStack management server honours the x-forwarded-for HTTP header and logs it as the source IP of an API request. This could lead to authentication bypass and other operational problems should an attacker decide to spoof their IP address this way. Users are recommended to upgrade to CloudStack version 4.18.1.1 or 4.19.0.1, which fixes this issue.</div>

### References
* https://lists.apache.org/thread/82f46pv7mvh95ybto5hn8wlo6g8jhjvp
* https://cloudstack.apache.org/blog/security-release-advisory-4.19.0.1-4.18.1.1


### Credits
* Yuyang Xiao <superxyyang@gmail.com> (finder)


## When downloading templates or ISOs, the management server and SSVM follow HTTP redirects with potentially dangerous consequences ## { #CVE-2024-29007 }

CVE-2024-29007 [\[CVE json\]](./CVE-2024-29007.cve.json) [\[OSV json\]](./CVE-2024-29007.osv.json)



_Last updated: 2024-04-04T10:58:20.239Z_

### Affected

* Apache CloudStack from 4.9.1.0 through 4.18.1.0, 4.19.0.0


### Description

<div>The CloudStack management server and secondary storage VM could be tricked into making requests to restricted or random resources by means of following 301 HTTP redirects presented by external servers when downloading templates or ISOs. Users are recommended to upgrade to version 4.18.1.1 or 4.19.0.1, which fixes this issue.</div>

### References
* https://lists.apache.org/thread/82f46pv7mvh95ybto5hn8wlo6g8jhjvp
* https://cloudstack.apache.org/blog/security-release-advisory-4.19.0.1-4.18.1.1


### Credits
* Yuyang Xiao <superxyyang@gmail.com> (finder)


## The extraconfig feature can be abused to load hypervisor resources on a VM instance ## { #CVE-2024-29008 }

CVE-2024-29008 [\[CVE json\]](./CVE-2024-29008.cve.json) [\[OSV json\]](./CVE-2024-29008.osv.json)



_Last updated: 2024-04-04T10:58:44.745Z_

### Affected

* Apache CloudStack from 4.14.0.0 through 4.18.1.0, 4.19.0.0


### Description

<div>A problem has been identified in the CloudStack additional VM configuration (extraconfig) feature which can be misused by anyone who has privilege to deploy a VM instance or configure settings of an already deployed VM instance, to configure additional VM configuration even when the feature is not explicitly enabled by the administrator. In a KVM based CloudStack environment, an attacker can exploit this issue to&nbsp;attach host devices such as storage disks, and PCI and USB devices such as network adapters and GPUs, in a regular VM instance that can be further exploited to gain access to the underlying network and storage infrastructure resources, and access any VM instance disks on the local storage.</div><br><div>Users are advised to upgrade to version 4.18.1.1 or 4.19.0.1, which fixes this issue.<br></div>

### References
* https://lists.apache.org/thread/82f46pv7mvh95ybto5hn8wlo6g8jhjvp
* https://cloudstack.apache.org/blog/security-release-advisory-4.19.0.1-4.18.1.1


### Credits
* Wei Zhou <ustcweizhou@gmail.com> (finder)
