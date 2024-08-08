---
title: Apache CloudStack security advisories
description: Security information for Apache CloudStack
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache CloudStack? You can read more about the projects' security policy on their [security page](https://cloudstack.apache.org/security/), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://cloudstack.apache.org/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
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


## Unauthenticated cluster service port leads to remote execution ## { #CVE-2024-38346 }

CVE-2024-38346 [\[CVE json\]](./CVE-2024-38346.cve.json) [\[OSV json\]](./CVE-2024-38346.osv.json)



_Last updated: 2024-07-05T13:39:11.185Z_

### Affected

* Apache CloudStack from 4.0.0 through 4.18.2.0
* Apache CloudStack from 4.19.0.0 through 4.19.0.1


### Description

<p>The CloudStack cluster service runs on unauthenticated port (default 9090) that can be misused to run arbitrary commands on targeted hypervisors and CloudStack management server hosts. Some of these commands were found to have command injection vulnerabilities that can result in arbitrary code execution via agents on the hosts that may run as a privileged user.&nbsp;<span style="background-color: rgb(255, 255, 255);">An attacker that can reach the cluster service on the unauthenticated&nbsp;port (default 9090), can exploit this to perform remote code execution on CloudStack managed hosts and result in complete</span>&nbsp;compromise of the confidentiality, integrity, and availability of CloudStack managed infrastructure.</p><span style="background-color: rgb(255, 255, 255);"><div><span style="background-color: rgb(255, 255, 255);"><br></span></div><div><span style="background-color: rgb(255, 255, 255);">Users are recommended to restrict the network access to the cluster service port (default 9090) on a CloudStack management server host to only its peer CloudStack management server hosts.&nbsp;</span>Users are recommended to upgrade to version 4.18.2.1, 4.19.0.2 or later, which addresses this issue.</div></span>

### References
* https://lists.apache.org/thread/6l51r00csrct61plkyd3qg3fj99215d1
* https://cloudstack.apache.org/blog/security-release-advisory-4.19.0.2-4.18.2.1
* https://www.shapeblue.com/shapeblue-security-advisory-apache-cloudstack-security-releases-4-18-2-1-and-4-19-0-2/


### Credits
* Adam Pond of Apple Services Engineering Security (finder)
* Terry Thibault of Apple Services Engineering Security (finder)
* Damon Smith of Apple Services Engineering Security (finder)


## Integration API service uses dynamic port when disabled ## { #CVE-2024-39864 }

CVE-2024-39864 [\[CVE json\]](./CVE-2024-39864.cve.json) [\[OSV json\]](./CVE-2024-39864.osv.json)



_Last updated: 2024-07-05T13:39:23.006Z_

### Affected

* Apache CloudStack from 4.0.0 through 4.18.2.0
* Apache CloudStack from 4.19.0.0 through 4.19.0.1


### Description

<div><p>The CloudStack integration API service allows running its unauthenticated API server (usually on port 8096 when configured and enabled via integration.api.port global setting) for internal portal integrations and for testing purposes. By default, the integration API service port is disabled and is considered disabled when integration.api.port is set to 0 or negative. Due to an improper initialisation logic, the integration API service would listen on a random port when its port value is set to 0 (default value).&nbsp;<span style="background-color: rgb(255, 255, 255);">An attacker that can access the CloudStack management network could scan and find the randomised integration API service port and exploit it to perform unauthorised administrative actions and perform remote code execution on CloudStack managed hosts and result in complete</span>&nbsp;compromise of the confidentiality, integrity, and availability of CloudStack managed infrastructure.<span style="background-color: rgb(255, 255, 255);"><br></span></p><span style="background-color: rgb(255, 255, 255);"><div><span style="background-color: rgb(255, 255, 255);">Users are recommended to restrict the network access on the CloudStack management server hosts to only essential ports. </span>Users are recommended to upgrade to version 4.18.2.1, 4.19.0.2 or later, which addresses this issue.</div></span></div>

### References
* https://lists.apache.org/thread/6l51r00csrct61plkyd3qg3fj99215d1
* https://cloudstack.apache.org/blog/security-release-advisory-4.19.0.2-4.18.2.1
* https://www.shapeblue.com/shapeblue-security-advisory-apache-cloudstack-security-releases-4-18-2-1-and-4-19-0-2/


### Credits
* Adam Pond of Apple Services Engineering Security (finder)
* Terry Thibault of Apple Services Engineering Security (finder)
* Damon Smith of Apple Services Engineering Security (finder)


## SAML Signature Exclusion ## { #CVE-2024-41107 }

CVE-2024-41107 [\[CVE json\]](./CVE-2024-41107.cve.json) [\[OSV json\]](./CVE-2024-41107.osv.json)



_Last updated: 2024-07-19T10:11:15.224Z_

### Affected

* Apache CloudStack from 4.5.0 through 4.18.2.1
* Apache CloudStack from 4.19.0.0 through 4.19.0.2


### Description

<div>The CloudStack SAML authentication (disabled by default) does not enforce signature check. In CloudStack environments where SAML authentication is enabled, an attacker that initiates CloudStack SAML single sign-on authentication can bypass SAML authentication by submitting a spoofed SAML response with no signature and <span style="background-color: rgb(255, 255, 255);">known or guessed username and other user details of a SAML-enabled CloudStack user-account</span>.&nbsp;In such environments, this can result in a complete compromise of the resources owned and/or accessible by a SAML enabled user-account.<br></div><div><br><span style="background-color: rgb(255, 255, 255);">Affected users are recommended to disable the SAML authentication plugin by setting the&nbsp;"saml2.enabled" global setting to "false", or upgrade to version 4.18.2.2, 4.19.1.0 or later, which addresses this issue.</span></div>

### References
* https://lists.apache.org/thread/5q06g8zvmhcw6w3tjr6r5prqdw6zckg3
* https://cloudstack.apache.org/blog/security-release-advisory-cve-2024-41107
* https://github.com/apache/cloudstack/issues/4519
* https://www.shapeblue.com/shapeblue-security-advisory-apache-cloudstack-cve-2024-41107


### Credits
* Christian Gross of Netcloud AG (finder)
* Damon Smith of Apple Services Engineering Security (finder)
* Adam Pond of Apple Services Engineering Security (finder)
* Terry Thibault of Apple Services Engineering Security (finder)


## User Key Exposure to Domain Admins ## { #CVE-2024-42062 }

CVE-2024-42062 [\[CVE json\]](./CVE-2024-42062.cve.json) [\[OSV json\]](./CVE-2024-42062.osv.json)



_Last updated: 2024-08-07T06:49:20.134Z_

### Affected

* Apache CloudStack from 4.10.0 through 4.18.2.2
* Apache CloudStack from 4.19.0.0 through 4.19.1.0


### Description

CloudStack account-users by default use username and password based authentication for API and UI access. Account-users can<span style="background-color: rgb(255, 255, 255);">&nbsp;generate and register randomised API and secret keys and use them for the purpose of API-based automation and integrations.&nbsp;</span><span style="background-color: rgb(255, 255, 255);">Due to an access permission validation issue that affects Apache CloudStack versions 4.10.0 up to 4.19.1.0, domain admin accounts were found to be able to query all registered account-users API and secret keys in an environment, including that of a root admin.&nbsp;</span>An attacker who has domain admin access can exploit this to gain root admin and other-account privileges and perform malicious operations that can result in compromise of resources integrity and confidentiality, data loss,&nbsp;<span style="background-color: rgb(255, 255, 255);">denial of service</span>&nbsp;and availability of CloudStack managed infrastructure.<br><br>Users are recommended to upgrade to Apache CloudStack 4.18.2.3 or 4.19.1.1, or later, which addresses this issue.&nbsp;Additionally, all account-user API and secret keys should be regenerated.<br>

### References
* https://cloudstack.apache.org/blog/security-release-advisory-4.19.1.1-4.18.2.3
* https://lists.apache.org/thread/lxqtfd6407prbw3801hb4fz3ot3t8wlj
* https://www.shapeblue.com/shapeblue-security-advisory-apache-cloudstack-security-releases-4-18-2-3-and-4-19-1-1/


### Credits
* Fabricio Duarte (finder)


## Unauthorised Network List Access ## { #CVE-2024-42222 }

CVE-2024-42222 [\[CVE json\]](./CVE-2024-42222.cve.json) [\[OSV json\]](./CVE-2024-42222.osv.json)



_Last updated: 2024-08-07T06:49:40.024Z_

### Affected

* Apache CloudStack at 4.19.1.0


### Description

<div>In Apache CloudStack 4.19.1.0, a regression in the network listing API allows unauthorised list access of network details for domain admin and normal user accounts. This vulnerability compromises tenant isolation, potentially leading to unauthorised access to network details, configurations and data.<br><br>Affected users are advised to upgrade to version 4.19.1.1 to address this issue. Users on older versions of CloudStack considering to upgrade, can skip 4.19.1.0 and upgrade directly to 4.19.1.1.<br></div>

### References
* https://github.com/apache/cloudstack/issues/9456
* https://cloudstack.apache.org/blog/security-release-advisory-4.19.1.1-4.18.2.3
* https://lists.apache.org/thread/lxqtfd6407prbw3801hb4fz3ot3t8wlj
* https://www.shapeblue.com/shapeblue-security-advisory-apache-cloudstack-security-releases-4-18-2-3-and-4-19-1-1/


### Credits
* Christian Gross of Netcloud AG (finder)
* Midhun Jose (finder)
