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



_Last updated: 2024-08-19T13:43:36.243Z_

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


## Uploaded and registered templates and volumes can be used to abuse KVM-based infrastructure ## { #CVE-2024-45219 }

CVE-2024-45219 [\[CVE json\]](./CVE-2024-45219.cve.json) [\[OSV json\]](./CVE-2024-45219.osv.json)



_Last updated: 2024-10-15T18:32:48.536Z_

### Affected

* Apache CloudStack from 4.0.0 through 4.18.2.3
* Apache CloudStack from 4.19.0.0 through 4.19.1.1


### Description

Account users in Apache CloudStack by default are allowed to upload and register templates for deploying instances and volumes for attaching them as data disks to their existing instances. Due to missing validation checks for KVM-compatible templates or volumes in CloudStack 4.0.0 through 4.18.2.3 and 4.19.0.0 through 4.19.1.1, an attacker that can upload or register templates and volumes, can use them to deploy malicious instances or attach uploaded volumes to their existing instances on KVM-based environments and exploit this to gain access to the host filesystems that could result in the compromise of resource integrity and confidentiality, data loss, denial of service, and availability of KVM-based infrastructure managed by CloudStack.<div><br></div><div><span style="background-color: rgb(252, 252, 252);">Users are recommended to upgrade to Apache CloudStack 4.18.2.4 or 4.19.1.2, or later, which addresses this issue. <br><br></span>Additionally, all user-uploaded or registered KVM-compatible templates and volumes can be scanned and checked that they are flat files that should not be using any additional or unnecessary features. For example, operators can run this on their secondary storage(s) and inspect output. An empty output for the disk being validated means it has no references to the host filesystems; on the other hand, if the output for the disk being validated is not empty, it might indicate a compromised disk.<br></div><blockquote>for file in $(find /path/to/storage/ -type f -regex [a-f0-9\-]*.*); do echo "Retrieving file [$file] info. If the output is not empty, that might indicate a compromised disk; check it carefully."; qemu-img info -U $file | grep file: ; printf "\n\n"; done</blockquote><div><br>The command can also be run for the file-based primary storages; however, bear in mind that (i) volumes created from templates will have references for the templates at first and (ii) volumes can be consolidated while migrating, losing their references to the templates. Therefore, the command execution for the primary storages can show both false positives and false negatives.<br><br>For checking the whole template/volume features of each disk, operators can run the following command:<br></div><blockquote>for file in $(find /path/to/storage/ -type f -regex [a-f0-9\-]*.*); do echo "Retrieving file [$file] info."; qemu-img info -U $file; printf "\n\n"; done</blockquote><div><span style="background-color: rgb(252, 252, 252);"><br></span></div>

### References
* https://cloudstack.apache.org/blog/security-release-advisory-4.18.2.4-4.19.1.2
* https://lists.apache.org/thread/ktsfjcnj22x4kg49ctock3d9tq7jnvlo
* https://www.shapeblue.com/shapeblue-security-advisory-apache-cloudstack-security-releases-4-18-2-4-and-4-19-1-2/


### Credits
* Daniel Augusto Veronezi Salvador <gutoveronezi@apache.org> (reporter)


## Access checks not enforced in Quota ## { #CVE-2024-45461 }

CVE-2024-45461 [\[CVE json\]](./CVE-2024-45461.cve.json) [\[OSV json\]](./CVE-2024-45461.osv.json)



_Last updated: 2025-02-12T09:30:16.539Z_

### Affected

* Apache CloudStack Quota plugin from 4.7.0 through 4.18.2.3
* Apache CloudStack Quota plugin from 4.19.0.0 through 4.19.1.1


### Description

<div>The CloudStack Quota feature allows cloud administrators to implement a quota or usage limit system for cloud resources, and is disabled by default. In environments where the feature is enabled, due to missing access check enforcements, non-administrative CloudStack user accounts are able to access and modify quota-related configurations and data. This issue affects Apache CloudStack from 4.7.0 through 4.18.2.3; and from 4.19.0.0 through 4.19.1.1, where the Quota feature is enabled.</div><div><br></div><span style="background-color: rgb(252, 252, 252);">Users are recommended to upgrade to Apache CloudStack 4.18.2.4 or 4.19.1.2, or later, which addresses this issue.&nbsp;</span>Alternatively, users that do not use the Quota feature are advised to disabled the plugin by setting the global setting "quota.enable.service" to "false".

### References
* https://cloudstack.apache.org/blog/security-release-advisory-4.18.2.4-4.19.1.2
* https://lists.apache.org/thread/ktsfjcnj22x4kg49ctock3d9tq7jnvlo
* https://www.shapeblue.com/shapeblue-security-advisory-apache-cloudstack-security-releases-4-18-2-4-and-4-19-1-2/


### Credits
* Fabrício Duarte <fabricio.duarte.jr@gmail.com> (reporter)


## Incomplete session invalidation on web interface logout ## { #CVE-2024-45462 }

CVE-2024-45462 [\[CVE json\]](./CVE-2024-45462.cve.json) [\[OSV json\]](./CVE-2024-45462.osv.json)



_Last updated: 2024-10-16T10:39:03.528Z_

### Affected

* Apache CloudStack from 4.15.1.0 through 4.18.2.3
* Apache CloudStack from 4.19.0.0 through 4.19.1.1


### Description

<div>The logout operation in the CloudStack web interface does not expire the user session completely which is valid until expiry by time or restart of the backend service. An attacker that has access to a user's browser can use an unexpired session to gain access to resources owned by the logged out user account. This issue affects Apache CloudStack from 4.15.1.0 through 4.18.2.3; and from 4.19.0.0 through 4.19.1.1.</div><div><br></div><div><span style="background-color: rgb(252, 252, 252);">Users are recommended to upgrade to Apache CloudStack 4.18.2.4 or 4.19.1.2, or later, which addresses this issue.</span></div>

### References
* https://cloudstack.apache.org/blog/security-release-advisory-4.18.2.4-4.19.1.2
* https://lists.apache.org/thread/ktsfjcnj22x4kg49ctock3d9tq7jnvlo
* https://www.shapeblue.com/shapeblue-security-advisory-apache-cloudstack-security-releases-4-18-2-4-and-4-19-1-2/


### Credits
* Arthur Souza (reporter)
* Felipe Olivaes (reporter)


## Request origin validation bypass makes account takeover possible ## { #CVE-2024-45693 }

CVE-2024-45693 [\[CVE json\]](./CVE-2024-45693.cve.json) [\[OSV json\]](./CVE-2024-45693.osv.json)



_Last updated: 2024-10-16T10:39:13.974Z_

### Affected

* Apache CloudStack from 4.15.1.0 through 4.18.2.3
* Apache CloudStack from 4.19.0.0 through 4.19.1.1


### Description

<p>Users logged into the Apache CloudStack's web interface can be tricked to submit malicious CSRF requests due to missing validation of the origin of the requests. This can allow an attacker to gain privileges and access to resources of the authenticated users and may lead<span style="background-color: rgb(255, 255, 255);">&nbsp;to account takeover,&nbsp;</span>disruption, exposure of sensitive data and compromise integrity of the resources owned by the user account that are managed by the platform.</p><p>This issue affects Apache CloudStack from 4.15.1.0 through 4.18.2.3 and 4.19.0.0 through 4.19.1.1</p><p></p><div><span style="background-color: rgb(252, 252, 252);">Users are recommended to upgrade to Apache CloudStack 4.18.2.4 or 4.19.1.2, or later, which addresses this issue.</span><br></div><div><div><div><div></div></div></div></div><div></div><p></p>

### References
* https://cloudstack.apache.org/blog/security-release-advisory-4.18.2.4-4.19.1.2
* https://lists.apache.org/thread/ktsfjcnj22x4kg49ctock3d9tq7jnvlo
* https://www.shapeblue.com/shapeblue-security-advisory-apache-cloudstack-security-releases-4-18-2-4-and-4-19-1-2/


### Credits
* Arthur Souza (reporter)
* Felipe Olivaes (reporter)


## Directly downloaded templates can be used to abuse KVM-based infrastructure ## { #CVE-2024-50386 }

CVE-2024-50386 [\[CVE json\]](./CVE-2024-50386.cve.json) [\[OSV json\]](./CVE-2024-50386.osv.json)



_Last updated: 2024-11-12T13:52:37.947Z_

### Affected

* Apache CloudStack from 4.0.0 through 4.18.2.4
* Apache CloudStack from 4.19.0.0 through 4.19.1.2


### Description

Account users in Apache CloudStack by default are allowed to register templates to be downloaded directly to the primary storage for deploying instances. Due to missing validation checks for KVM-compatible templates in CloudStack 4.0.0 through 4.18.2.4 and 4.19.0.0 through 4.19.1.2, an attacker that can register templates, can use them to deploy malicious instances on KVM-based environments and exploit this to gain access to the host filesystems that could result in the compromise of resource integrity and confidentiality, data loss, denial of service, and availability of KVM-based infrastructure managed by CloudStack.<div><br></div><div><span style="background-color: rgb(252, 252, 252);">Users are recommended to upgrade to Apache CloudStack 4.18.2.5 or 4.19.1.3, or later, which addresses this issue. <br><br></span>Additionally, all user-registered KVM-compatible templates can be scanned and checked that they are flat files that should not be using any additional or unnecessary features. For example, operators can run the following command on their file-based primary storage(s) and inspect the output. An empty output for the disk being validated means it has no references to the host filesystems; on the other hand, if the output for the disk being validated is not empty, it might indicate a compromised disk. H<span style="background-color: rgb(255, 255, 255);">owever, bear in mind that (i) volumes created from templates will have references for the templates at first and (ii) volumes can be consolidated while migrating, losing their references to the templates. Therefore, the command execution for the primary storages can show both false positives and false negatives.</span><br></div><blockquote>for file in $(find /path/to/storage/ -type f -regex [a-f0-9\-]*.*); do echo "Retrieving file [$file] info. If the output is not empty, that might indicate a compromised disk; check it carefully."; qemu-img info -U $file | grep file: ; printf "\n\n"; done</blockquote><div><br>For checking the whole template/volume features of each disk, operators can run the following command:<br></div><blockquote>for file in $(find /path/to/storage/ -type f -regex [a-f0-9\-]*.*); do echo "Retrieving file [$file] info."; qemu-img info -U $file; printf "\n\n"; done</blockquote><div><span style="background-color: rgb(252, 252, 252);"><br></span></div><br>

### References
* https://cloudstack.apache.org/blog/security-release-advisory-4.18.2.5-4.19.1.3
* https://lists.apache.org/thread/d0x83c2cyglzzdw8csbop7mj7h83z95y
* https://www.shapeblue.com/shapeblue-security-advisory-apache-cloudstack-security-releases-4-18-2-5-and-4-19-1-3/


### Credits
* Kiran Chavala <kiranchavala@apache.org> (reporter)


## Unauthorised access to annotations ## { #CVE-2025-22828 }

CVE-2025-22828 [\[CVE json\]](./CVE-2025-22828.cve.json) [\[OSV json\]](./CVE-2025-22828.osv.json)



_Last updated: 2025-01-13T12:40:18.771Z_

### Affected

* Apache CloudStack from 4.16.0 through *


### Description

<div>CloudStack users can add and read comments (annotations) on resources they are authorised to access.&nbsp;</div><div>Due to an access validation issue that affects Apache CloudStack versions from 4.16.0, users who have access, prior access or knowledge of resource UUIDs can list and add comments (annotations) to such resources.&nbsp;</div><div>An attacker with a user-account and access or prior knowledge of resource UUIDs may exploit this issue to read contents of the comments (annotations) or add malicious comments (annotations) to such resources.&nbsp;</div><div>This may cause potential loss of confidentiality of CloudStack environments and resources if the comments (annotations) contain any privileged information. However, guessing or brute-forcing resource UUIDs are generally hard to impossible and access to listing or adding comments isn't same as access to CloudStack resources, making this issue of very low severity and general low impact.</div><br><div>CloudStack admins may also disallow listAnnotations and addAnnotation API access to non-admin roles in their environment as an interim measure.</div><br>

### References
* https://lists.apache.org/thread/bbsm9fdwrgfyostzojh6ghpocgdmx8rs


### Credits
* Alex Perrakis <alexperrakis1@gmail.com> (reporter)
* Efstratios Chatzoglou <efchatzoglou@gmail.com> (reporter)


## Unauthorised access to dedicated resources in Quota plugin ## { #CVE-2025-22829 }

CVE-2025-22829 [\[CVE json\]](./CVE-2025-22829.cve.json) [\[OSV json\]](./CVE-2025-22829.osv.json)



_Last updated: 2025-06-11T04:00:28.410Z_

### Affected

* Apache CloudStack from 4.20.0.0 before 4.20.1.0


### Description

The CloudStack Quota plugin has an improper privilege management logic in version 4.20.0.0. Anyone with authenticated user-account access in CloudStack 4.20.0.0 environments, where this plugin is enabled and have access to specific APIs can enable or disable reception of quota-related emails for any account in the environment and list their configurations.<br><br>Quota plugin users using CloudStack 4.20.0.0 are recommended to upgrade to CloudStack version 4.20.1.0, which fixes this issue.

### References
* https://cloudstack.staged.apache.org/blog/cve-advisories-4.19.3.0-4.20.1.0
* https://www.shapeblue.com/shapeblue-security-advisory-cloudstack-4-19-3-0-and-4-20-1-0/
* https://lists.apache.org/thread/y3qnwn59t8qggtdohv7k7vw39bgb3d60


### Credits
* Fabricio Duarte <fabricio.duarte.jr@gmail.com> (finder)


## CKS cluster in project exposes user API keys ## { #CVE-2025-26521 }

CVE-2025-26521 [\[CVE json\]](./CVE-2025-26521.cve.json) [\[OSV json\]](./CVE-2025-26521.osv.json)



_Last updated: 2025-06-11T04:00:17.648Z_

### Affected

* Apache CloudStack from 4.17.0.0 before 4.19.3.0
* Apache CloudStack from 4.20.0.0 before 4.20.1.0


### Description

When an Apache CloudStack user-account creates a CKS-based Kubernetes cluster in a project, the API key and the secret key of the 'kubeadmin' user of the caller account are used to create the secret config in the CKS-based Kubernetes cluster. A member of the project who can access the CKS-based Kubernetes cluster, can also access the API key and secret key of the 'kubeadmin' user of the CKS cluster's creator's account. An attacker who's a member of the project can exploit this to impersonate and perform privileged actions that can result in complete compromise of the confidentiality, integrity, and availability of resources owned by the creator's account.<br><br>CKS users are recommended to upgrade to version 4.19.3.0 or 4.20.1.0, which fixes this issue.<h3>Updating Existing Kubernetes Clusters in Projects</h3>A <b>service account</b> should be created for each project to provide limited access specifically for Kubernetes cluster providers and autoscaling. Follow the steps below to create a new service account, update the secret inside the cluster, and regenerate existing API and service keys:<h3>1. Create a New Service Account</h3><div>Create a new account using the role <b>"Project Kubernetes Service Role"</b> with the following details:</div><div><table><tbody><tr><td><b>Account Name</b><br></td><td>kubeadmin-&lt;FIRST_EIGHT_CHARACTERS_OF_PROJECT_ID&gt;<br></td></tr><tr><td><b>First Name</b><br></td><td>Kubernetes<br></td></tr><tr><td><b>Last Name</b><br></td><td>Service User<br></td></tr><tr><td><b>Account Type</b><br></td><td>0 (Normal User)<br></td></tr><tr><td><b>Role ID</b><br></td><td>&lt;ID_OF_SERVICE_ROLE&gt;<br></td></tr></tbody></table><br></div><h3>2. Add the Service Account to the Project</h3>Add this account to the <b>project</b> where the Kubernetes cluster(s) are hosted.<br><h3>3. Generate API and Secret Keys</h3>Generate <b>API Key</b> and <b>Secret Key</b> for the <i>default user</i> of this account.<br><h3>4. Update the CloudStack Secret in the Kubernetes Cluster</h3>Create a temporary file `/tmp/cloud-config` with the following data:<br>&nbsp;&nbsp;<tt>&nbsp;api-url = &lt;API_URL&gt;  &nbsp; &nbsp;  # For example: &lt;MS_URL&gt;/client/api<br>&nbsp; api-key = &lt;SERVICE_USER_API_KEY&gt;<br>&nbsp; secret-key = &lt;SERVICE_USER_SECRET_KEY&gt;<br></tt><div><tt>&nbsp; project-id = &lt;PROJECT_ID&gt;</tt></div><div><tt><br></tt></div>Delete the existing secret using kubectl and Kubernetes cluster config:<br><div>&nbsp;&nbsp;<tt>&nbsp;./kubectl --kubeconfig kube.conf -n kube-system delete secret cloudstack-secret</tt></div><div><tt><br></tt></div>Create a new secret using kubectl and Kubernetes cluster config:<br><div>&nbsp; &nbsp; ./kubectl --kubeconfig kube.conf -n kube-system create secret generic cloudstack-secret --from-file=/tmp/cloud-config</div><div><br></div>Remove the temporary file:<br>&nbsp; &nbsp; rm /tmp/cloud-config<h3>5. Regenerate API and Secret Keys</h3>Regenerate the API and secret keys for the <b>original user account</b> that was used to create the Kubernetes cluster.<br>

### References
* https://cloudstack.apache.org/blog/cve-advisories-4.19.3.0-4.20.1.0/
* https://www.shapeblue.com/shapeblue-security-advisory-cloudstack-4-19-3-0-and-4-20-1-0/
* https://lists.apache.org/thread/y3qnwn59t8qggtdohv7k7vw39bgb3d60


### Credits
* Wei Zhou (weizhou@apache.org) (finder)


## Unauthorised template/ISO list access to the domain/resource admins ## { #CVE-2025-30675 }

CVE-2025-30675 [\[CVE json\]](./CVE-2025-30675.cve.json) [\[OSV json\]](./CVE-2025-30675.osv.json)



_Last updated: 2025-06-11T04:00:06.854Z_

### Affected

* Apache CloudStack from 4.0.0 before 4.19.3.0
* Apache CloudStack from 4.20.0.0 before 4.20.1.0


### Description

<div><span style="background-color: rgba(232, 232, 232, 0.04);">In Apache CloudStack, a flaw in access control affects the listTemplates and listIsos APIs. A malicious Domain Admin or Resource Admin can exploit this issue by intentionally specifying the 'domainid' parameter along with the 'filter=self' or 'filter=selfexecutable' values. This allows the attacker to gain unauthorized visibility into templates and ISOs under the ROOT domain.</span></div><div><span style="background-color: rgba(232, 232, 232, 0.04);">A malicious admin can enumerate and extract metadata of templates and ISOs that belong to unrelated domains, violating isolation boundaries and potentially exposing sensitive or internal configuration details.&nbsp;</span></div><div><span style="background-color: rgba(232, 232, 232, 0.04);">This vulnerability has been fixed by ensuring the domain resolution strictly adheres to the caller's scope rather than defaulting to the ROOT domain.</span></div><div><span style="background-color: rgba(232, 232, 232, 0.04);"><br></span></div><div><span style="background-color: rgba(232, 232, 232, 0.04);">Affected users are recommended to upgrade to Apache CloudStack 4.19.3.0 or 4.20.1.0.</span></div>

### References
* https://cloudstack.apache.org/blog/cve-advisories-4.19.3.0-4.20.1.0/
* https://www.shapeblue.com/shapeblue-security-advisory-cloudstack-4-19-3-0-and-4-20-1-0/
* https://lists.apache.org/thread/y3qnwn59t8qggtdohv7k7vw39bgb3d60


### Credits
* Bernardo De Marco Gonçalves <bernardomg2004@gmail.com> (finder)


## Domain Admin can reset Admin password in Root Domain ## { #CVE-2025-47713 }

CVE-2025-47713 [\[CVE json\]](./CVE-2025-47713.cve.json) [\[OSV json\]](./CVE-2025-47713.osv.json)



_Last updated: 2025-06-11T03:59:55.628Z_

### Affected

* Apache CloudStack from 4.10.0 before 4.19.3.0
* Apache CloudStack from 4.20.0.0 before 4.20.1.0


### Description

<p></p><div><span style="background-color: rgba(232, 232, 232, 0.04);">A privilege escalation vulnerability exists in Apache CloudStack versions 4.10.0.0 through 4.20.0.0 where a malicious Domain Admin user in the ROOT domain can reset the password of user-accounts of Admin role type. This operation is not appropriately restricted and allows the attacker to assume control over higher-privileged user-accounts.&nbsp;</span><span style="background-color: rgba(232, 232, 232, 0.04);">A malicious Domain Admin attacker can impersonate an Admin user-account and gain access to sensitive APIs and resources that&nbsp;<span style="background-color: rgb(255, 255, 255);">could result in the compromise of resource integrity and confidentiality, data loss, denial of service, and availability of infrastructure managed by CloudStack.</span><br><br></span></div><div><span style="background-color: rgba(232, 232, 232, 0.04);">Users are recommended to upgrade to Apache CloudStack 4.19.3.0 or 4.20.1.0, which fixes the issue with the following:<br></span><span style="background-color: rgba(232, 232, 232, 0.04);"><div><ul><li><span style="background-color: rgba(232, 232, 232, 0.04);"><span style="background-color: rgba(232, 232, 232, 0.04);">Strict validation on Role Type hierarchy: the caller's user-account role must be equal to or higher than the target user-account's role.</span></span></li><li><span style="background-color: rgba(232, 232, 232, 0.04);"><span style="background-color: rgba(232, 232, 232, 0.04);">API privilege comparison: the caller must possess all privileges of the user they are operating on. </span></span></li><li><span style="background-color: rgba(232, 232, 232, 0.04);"><span style="background-color: rgba(232, 232, 232, 0.04);">Two new domain-level settings (restricted to the default Admin): <br> - role.types.allowed.for.operations.on.accounts.of.same.role.type: Defines which role types are allowed to act on users of the same role type. Default: "Admin, DomainAdmin, ResourceAdmin". <br>&nbsp; &nbsp;- allow.operations.on.users.in.same.account: Allows/disallows user operations within the same account. Default: true.</span></span></li></ul></div></span></div><p></p>

### References
* https://cloudstack.apache.org/blog/cve-advisories-4.19.3.0-4.20.1.0/
* https://www.shapeblue.com/shapeblue-security-advisory-cloudstack-4-19-3-0-and-4-20-1-0/
* https://lists.apache.org/thread/y3qnwn59t8qggtdohv7k7vw39bgb3d60


### Credits
* Scott Schmitz <sschmitz@ussignal.com> (finder)


## Insecure access of user's API/Secret Keys in the same domain ## { #CVE-2025-47849 }

CVE-2025-47849 [\[CVE json\]](./CVE-2025-47849.cve.json) [\[OSV json\]](./CVE-2025-47849.osv.json)



_Last updated: 2025-06-11T03:59:42.176Z_

### Affected

* Apache CloudStack from 4.10.0 before 4.19.3.0
* Apache CloudStack from 4.20.0.0 before 4.20.1.0


### Description

<div><span style="background-color: rgba(232, 232, 232, 0.04);"><span style="background-color: rgba(232, 232, 232, 0.04);">A privilege escalation vulnerability exists in Apache CloudStack versions 4.10.0.0 through 4.20.0.0 where a malicious Domain Admin user in the ROOT domain can get the API key and secret key of user-accounts of Admin role type in the same domain. This operation is not appropriately restricted and allows the attacker to assume control over higher-privileged user-accounts. </span><span style="background-color: rgba(232, 232, 232, 0.04);">A malicious Domain Admin attacker can impersonate an Admin user-account and gain access to sensitive APIs and resources that <span style="background-color: rgb(255, 255, 255);">could result in the compromise of resource integrity and confidentiality, data loss, denial of service, and availability of infrastructure managed by CloudStack.</span><br></span><br><span style="background-color: rgba(232, 232, 232, 0.04);">Users are recommended to upgrade to Apache CloudStack 4.19.3.0 or 4.20.1.0, which fixes the issue with the following:<br></span></span></div><div><ul><li><span style="background-color: rgba(232, 232, 232, 0.04);">Strict validation on Role Type hierarchy: the caller's role must be equal to or higher than the target user's role.&nbsp;</span></li><li><span style="background-color: rgba(232, 232, 232, 0.04);">API privilege comparison: the caller must possess all privileges of the user they are operating on.&nbsp;</span></li><li><span style="background-color: rgba(232, 232, 232, 0.04);">Two new domain-level settings (restricted to the default admin):&nbsp;<br> - role.types.allowed.for.operations.on.accounts.of.same.role.type: Defines which role types are allowed to act on users of the same role type. Default: "Admin, DomainAdmin, ResourceAdmin".&nbsp;<br> - allow.operations.on.users.in.same.account: Allows/disallows user operations within the same account. Default: true.</span></li></ul></div>

### References
* https://cloudstack.apache.org/blog/cve-advisories-4.19.3.0-4.20.1.0/
* https://www.shapeblue.com/shapeblue-security-advisory-cloudstack-4-19-3-0-and-4-20-1-0/
* https://lists.apache.org/thread/y3qnwn59t8qggtdohv7k7vw39bgb3d60


### Credits
* Kevin Li <kli74@apple.com> (finder)
* Scott Schmitz <sschmitz@ussignal.com> (finder)
