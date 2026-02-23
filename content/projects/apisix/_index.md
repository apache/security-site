---
title: Apache APISIX security advisories
description: Security information for Apache APISIX
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache APISIX? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## basic-auth logs plaintext credentials at info level ## { #CVE-2025-62232 }

CVE-2025-62232 [\[CVE json\]](./CVE-2025-62232.cve.json) [\[OSV json\]](./CVE-2025-62232.osv.json)



_Last updated: 2025-10-31T08:48:32.770Z_

### Affected

* Apache APISIX from 1.0 before 3.14


### Description

Sensitive data exposure via logging in basic-auth leads to plaintext usernames and passwords written to error logs and forwarded to log sinks when log level is INFO/DEBUG. This creates a high risk of credential compromise through log access.<br>It has been fixed in the following commit:&nbsp;<a target="_blank" rel="nofollow" href="https://github.com/apache/apisix/pull/12629">https://github.com/apache/apisix/pull/12629</a><br>Users are recommended to upgrade to version 3.14, which fixes this issue.

### References
* https://lists.apache.org/thread/32hdgh570btfhg02hfc7p7ckf9v83259


### Credits
* Mapta / BugBunny_ai (reporter)


## improper validation of issuer from introspection discovery url in plugin openid-connect ## { #CVE-2025-46647 }

CVE-2025-46647 [\[CVE json\]](./CVE-2025-46647.cve.json) [\[OSV json\]](./CVE-2025-46647.osv.json)



_Last updated: 2025-07-02T01:08:54.683Z_

### Affected

* Apache APISIX before 3.12.0


### Description

<p>A vulnerability of plugin&nbsp;openid-connect in Apache APISIX.</p>This vulnerability will only have an impact if all of the following conditions are met:<br>1. Use the openid-connect plugin with introspection mode<br>2. The auth service connected to openid-connect provides services to multiple issuers<br>3. Multiple issuers share the same private key and relies only on the issuer being different<br><br><div><div>If affected by this vulnerability, it would allow an attacker with a valid account on one of the issuers to log into the other issuer.</div></div><br><p>This issue affects Apache APISIX: until 3.12.0.</p><p>Users are recommended to upgrade to version 3.12.0 or higher.<br><br></p>

### References
* https://lists.apache.org/thread/yrpp2cd3o4qkxlrh421mq8gsrt0k4x0w


### Credits
* Tiernan Messmer (finder)


## Local listening file permissions in APISIX plugin runner allow a local attacker to elevate privileges ## { #CVE-2025-27446 }

CVE-2025-27446 [\[CVE json\]](./CVE-2025-27446.cve.json) [\[OSV json\]](./CVE-2025-27446.osv.json)



_Last updated: 2025-07-06T03:41:43.412Z_

### Affected

* Apache APISIX Java Plugin Runner from 0.2.0 through 0.5.0


### Description

<p>Incorrect Permission Assignment for Critical Resource vulnerability in Apache APISIX(java-plugin-runner).</p>Local listening file permissions in APISIX plugin runner allow a local attacker to elevate privileges.<br><p>This issue affects Apache APISIX(java-plugin-runner): from 0.2.0 through 0.5.0.</p><p>Users are recommended to upgrade to version 0.6.0 or higher, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/qwxnxolt0j5nvjfpr0mlz6h7nrtvyzng


### Credits
* Benoit TELLIER (reporter)


## Forward-Auth Request Smuggling ## { #CVE-2024-32638 }

CVE-2024-32638 [\[CVE json\]](./CVE-2024-32638.cve.json) [\[OSV json\]](./CVE-2024-32638.osv.json)



_Last updated: 2025-10-15T03:54:43.662Z_

### Affected

* Apache APISIX from 3.8.0 through 3.9.0


### Description

<span style="background-color: rgb(255, 255, 255);">Inconsistent Interpretation of HTTP Requests ('HTTP Request Smuggling')</span>&nbsp;vulnerability in Apache APISIX when using `forward-auth` plugin.<p>This issue affects Apache APISIX: from 3.8.0, 3.9.0.</p><p>Users are recommended to upgrade to version 3.8.1, 3.9.1 or higher, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ngvgxllw4zn4hgngkqw2o225kf9wotov


### Credits
* Discovered and reported by Brandon Arp and Bruno Green of Topsort. (reporter)


## apisix/jwt-auth may leak secrets in error response ## { #CVE-2022-29266 }

CVE-2022-29266 [\[CVE json\]](./CVE-2022-29266.cve.json) [\[OSV json\]](./CVE-2022-29266.osv.json)



_Last updated: 2022-05-03T06:58:33.689Z_

### Affected

* Apache APISIX from Apache APISIX through 2.13.0


### Description

In Apache APISIX before 2.13.1, the jwt-auth plugin has a security issue that leaks the user's secret key because the error message returned from the dependency lua-resty-jwt contains sensitive information.

### References
* https://lists.apache.org/thread/6qpfyxogbvn18g9xr8g218jjfjbfsbhr


### Credits
* Discovered and reported by a team from Kingdee Software (China) Ltd. consisting of Zhongyuan Tang, Hongfeng Xie, and Bing Chen.


## Apache APISIX: the body_schema check in request-validation plugin can be bypassed ## { #CVE-2022-25757 }

CVE-2022-25757 [\[CVE json\]](./CVE-2022-25757.cve.json) [\[OSV json\]](./CVE-2022-25757.osv.json)



_Last updated: 2022-03-28T06:57:28.175Z_

### Affected

* Apache APISIX from Apache APISIX through 2.12.1


### Description

In Apache APISIX before 2.13.0, when decoding JSON with duplicate keys, lua-cjson will choose the last occurred value as the result. By passing a JSON with a duplicate key, the attacker can bypass the body_schema validation in the request-validation plugin. For example, `{"string_payload":"bad","string_payload":"good"}` can be used to hide the "bad" input.

Systems satisfy three conditions below are affected by this attack:
1. use body_schema validation in the request-validation plugin
2. upstream application uses a special JSON library that chooses the first occurred value, like jsoniter or gojay
3. upstream application does not validate the input anymore.

The fix in APISIX is to re-encode the validated JSON input back into the request body at the side of APISIX.Improper Input Validation vulnerability in __COMPONENT__ of Apache APISIX allows an attacker to __IMPACT__.  This issue affects Apache APISIX Apache APISIX version 2.12.1 and prior versions.

### References
* https://lists.apache.org/thread/03vd2j81krxmpz6xo8p1dl642flpo6fv


### Credits
* Thanks for Guangli Dong from www.huoxian.cn


## apisix/batch-requests plugin allows overwriting the X-REAL-IP header ## { #CVE-2022-24112 }

CVE-2022-24112 [\[CVE json\]](./CVE-2022-24112.cve.json) [\[OSV json\]](./CVE-2022-24112.osv.json)



_Last updated: 2022-02-11T12:00:02.021Z_

### Affected

* Apache APISIX from Apache APISIX 2.12 before 2.12.1
* Apache APISIX from Apache APISIX 2.10 before 2.10.4
* Apache APISIX from 1.3 before Apache APISIX 1*


### Description

An attacker can abuse the batch-requests plugin to send requests to bypass the IP restriction of Admin API.
A default configuration of Apache APISIX (with default API key) is vulnerable to remote code execution.
When the admin key was changed or the port of Admin API was changed to a port different from the data panel, the impact is lower. But there is still a risk to bypass the IP restriction of Apache APISIX's data panel.

There is a check in the batch-requests plugin which overrides the client IP with its real remote IP. But due to a bug in the code, this check can be bypassed.

### References
* https://lists.apache.org/thread/lcdqywz8zy94mdysk7p3gfdgn51jmt94


### Credits
* Original discovery by Real World CTF at Chaitin Tech. Reported by Sauercloud.


## security vulnerability on unauthorized access. ## { #CVE-2021-45232 }

CVE-2021-45232 [\[CVE json\]](./CVE-2021-45232.cve.json) [\[OSV json\]](./CVE-2021-45232.osv.json)



_Last updated: 2021-12-27T14:49:25.542Z_

### Affected

* Apache APISIX Dashboard at 2.7 and 2.7.1
* Apache APISIX Dashboard at 2.8
* Apache APISIX Dashboard at 2.9
* Apache APISIX Dashboard at 2.10


### Description

In Apache APISIX Dashboard before 2.10.1, the Manager API uses two frameworks and introduces framework `droplet` on the basis of framework `gin`, all APIs and authentication middleware are developed based on framework `droplet`, but some API directly use the interface of framework `gin` thus bypassing the authentication.  

### References
* https://lists.apache.org/thread/979qbl6vlm8269fopfyygnxofgqyn6k5


### Credits
* Independently discovered by ZHU Yucheng of YuanbaoTeach Security Team.


## Path traversal in request_uri variable ## { #CVE-2021-43557 }

CVE-2021-43557 [\[CVE json\]](./CVE-2021-43557.cve.json) [\[OSV json\]](./CVE-2021-43557.osv.json)



_Last updated: 2021-11-22T08:20:29.238Z_

### Affected

* Apache APISIX from 1.5 before Apache APISIX 1.5*


### Description

The uri-block plugin in Apache APISIX before 2.10.2 uses $request_uri without verification. The $request_uri is the full original request URI without normalization.
This makes it possible to construct a URI to bypass the block list on some occasions. For instance, when the block list contains "^/internal/", a URI like `//internal/` can be used to bypass it.

Some other plugins also have the same issue. And it may affect the developer's custom plugin.

### References
* https://lists.apache.org/thread/18jyd458ptocr31rnkjs71w4h366mv7h


## Bypass network access control ## { #CVE-2021-33190 }

CVE-2021-33190 [\[CVE json\]](./CVE-2021-33190.cve.json) [\[OSV json\]](./CVE-2021-33190.osv.json)



_Last updated: 2021-06-08T15:01:51.802Z_

### Affected

* Apache APISIX Dashboard at Apache APISIX Dashboard 2.6 2.6


### Description

In Apache APISIX Dashboard version 2.6, we changed the default value of listen host to 0.0.0.0 in order to facilitate users to configure external network access. In the IP allowed list restriction, a risky function was used for the IP acquisition, which made it possible to bypass the network limit. At the same time, the default account and password are fixed.Ultimately these factors lead to the issue of security risks.  This issue is fixed in APISIX Dashboard 2.6.1


### References
* https://lists.apache.org/thread.html/re736aea55e8fd2478f0739c0c38a9375c4204fc1f0bd1ea687f57049%40%3Cdev.apisix.apache.org%3E
