---
title: Apache APISIX security advisories
description: Security information for Apache APISIX
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache APISIX? You can read more about the projects' security policy on their [security page](https://github.com/apache/apisix/blob/master/THREAT_MODEL.md), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://github.com/apache/apisix/blob/master/THREAT_MODEL.md). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Improper authentication in cas-auth plugin ## { #CVE-2026-49872 }

CVE-2026-49872 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49872) [\[CVE json\]](./CVE-2026-49872.cve.json) [\[OSV json\]](./CVE-2026-49872.osv.json)



_Last updated: 2026-06-19T13:19:29.418Z_

### Affected

* Apache APISIX from 3.0.0 through 3.16.0


### Description

<p>Improper Authentication vulnerability in Apache APISIX.</p>When the cas-auth plugin is used in a route, an attacker can possibly authenticate itself with credentials from a different source.<br><p>This issue affects Apache APISIX: from 3.0.0 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/bzjpo60ygxo7kxdqf7vw3l5zw2lh6m5k


### Credits
* lokerxxx (reporter)


## cas-auth login CSRF / session injection issue ## { #CVE-2026-49871 }

CVE-2026-49871 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49871) [\[CVE json\]](./CVE-2026-49871.cve.json) [\[OSV json\]](./CVE-2026-49871.osv.json)



_Last updated: 2026-06-19T13:18:27.333Z_

### Affected

* Apache APISIX from 3.0.0 through 3.16.0


### Description

<p>Cross-Site Request Forgery (CSRF) vulnerability in the cas-auth plugin under default configurations.</p><p><span style="background-color: rgb(255, 255, 255);">This defect allows a</span><span style="background-color: rgb(255, 255, 255);">&nbsp;</span><span style="background-color: rgb(255, 255, 255);">remote attacker that manages to send a victim to a webpage controlled by them can cause the victim's browser to become authenticated as a different identity</span><span style="background-color: rgb(255, 255, 255);">.</span></p><p><span style="background-color: rgb(255, 255, 255);">Actions the victim takes upstream are then attributed to attackers identity.</span><br></p><p>This issue affects Apache APISIX: from 3.0.0 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/1ozsnss0lof4gpwq763d66oxwxt3sycp


### Credits
* lokerxxx (reporter)


## Identity spoofing issue in APISIX opa plugin ## { #CVE-2026-49231 }

CVE-2026-49231 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49231) [\[CVE json\]](./CVE-2026-49231.cve.json) [\[OSV json\]](./CVE-2026-49231.osv.json)



_Last updated: 2026-06-19T13:14:23.085Z_

### Affected

* Apache APISIX from 3.5.0 through 3.16.0


### Description

<p>Authentication Bypass by Spoofing vulnerability in opa plugin.</p>An attacker could relay spoofed identity headers to upstream capitalising on non-default configuration in opa plugin.<br><br>This could allow the attacker to assume higher privileges on the upstream service.<br><p>This issue affects Apache APISIX: from 3.5.0 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/s1jd1vxm59p6ghx47xhmpjdk1cobo4hn


### Credits
* lokerxxx (reporter)


## Authentication bypass in jwe-decrypt ## { #CVE-2026-49230 }

CVE-2026-49230 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-49230) [\[CVE json\]](./CVE-2026-49230.cve.json) [\[OSV json\]](./CVE-2026-49230.osv.json)



_Last updated: 2026-06-19T13:13:32.638Z_

### Affected

* Apache APISIX from 3.8.0 through 3.16.0


### Description

<p>Improper Validation of Integrity Check Value vulnerability in Apache APISIX.</p>The jwe-decrypt plugin under default configuration is vulnerable to authentication bypass.&nbsp;<br><p>This issue affects Apache APISIX: from 3.8.0 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/n0blgkpvz38ghh5rrh6wtl476919xj1b


### Credits
* lokerxxx (reporter)


## Cas-auth Host header influence on CAS service URL ## { #CVE-2026-48895 }

CVE-2026-48895 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-48895) [\[CVE json\]](./CVE-2026-48895.cve.json) [\[OSV json\]](./CVE-2026-48895.osv.json)



_Last updated: 2026-06-19T13:16:18.311Z_

### Affected

* Apache APISIX from 3.0.0 through 3.16.0


### Description

<p>URL Redirection to Untrusted Site ('Open Redirect') vulnerability in Apache APISIX.</p><p>The attacker could manipulate some client headers to perform an open-redirect, to potentially expose the session token.</p><p>This issue affects Apache APISIX: from 3.0.0 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/yo1kq93ds69zbgjjopop7dmzm7zhj1gq


### Credits
* lokerxxx (reporter)


## Session replay issue in hmac-auth ## { #CVE-2026-47341 }

CVE-2026-47341 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-47341) [\[CVE json\]](./CVE-2026-47341.cve.json) [\[OSV json\]](./CVE-2026-47341.osv.json)



_Last updated: 2026-06-19T13:17:16.260Z_

### Affected

* Apache APISIX from 3.11.0 through 3.16.0


### Description

<p>Authentication Bypass by Capture-replay vulnerability in Apache APISIX.</p>Attacker can benefit from certain configurations in hmac-auth to re-use a token forever, bypassing expiry.<br><p>This issue affects Apache APISIX: from 3.11.0 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/ob6ng9x2hxtyfojs839hs1n0v18xxzf2


### Credits
* leon (reporter)


## authz-casdoor incorrect session sharing ## { #CVE-2026-47339 }

CVE-2026-47339 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-47339) [\[CVE json\]](./CVE-2026-47339.cve.json) [\[OSV json\]](./CVE-2026-47339.osv.json)



_Last updated: 2026-06-19T13:10:09.663Z_

### Affected

* Apache APISIX from 2.14.1 through 3.16.0


### Description

<p>Incorrect Authorization vulnerability in Apache APISIX.</p>An attacker can capitalise on authz-casdoor plugin under default configuration to authenticate themselves with credentials from a different source.<br><p>This issue affects Apache APISIX: from 2.14.1 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lk4q5o855cocc7zq5wh1zlctfmcq6f76


### Credits
* leon (reporter)


## Cas-auth plugin open redirect via unsanitized cookie value ## { #CVE-2026-44915 }

CVE-2026-44915 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44915) [\[CVE json\]](./CVE-2026-44915.cve.json) [\[OSV json\]](./CVE-2026-44915.osv.json)



_Last updated: 2026-06-19T13:12:20.566Z_

### Affected

* Apache APISIX from 3.0.0 through 3.16.0


### Description

<p>URL Redirection to Untrusted Site ('Open Redirect') vulnerability in Apache APISIX.</p><p>The default configuration of cas-auth in Apache APISIX is vulnerable to p<span style="background-color: rgb(255, 255, 255);">hishing and credential theft.</span></p><p>This issue affects Apache APISIX: from 3.0.0 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/2syk2kkzjnpzrdh98plbzj8os7wn521c


### Credits
* Qi Deng (reporter)
* lokerxxx (reporter)


## Openid-connect plugin Identity Header Spoofing ## { #CVE-2026-44087 }

CVE-2026-44087 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44087) [\[CVE json\]](./CVE-2026-44087.cve.json) [\[OSV json\]](./CVE-2026-44087.osv.json)



_Last updated: 2026-06-19T13:11:08.855Z_

### Affected

* Apache APISIX from 2.3 through 3.16.0


### Description

<p>Insufficient Verification of Data Authenticity vulnerability in Apache APISIX.</p>The openid-connect plugin under default configuration has an attack surface that allows the attacker to spoof identity headers allowing the attacker to get unauthorized access the protected resources.<br><p>This issue affects Apache APISIX: from 2.3 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/72ryrgdssk6s2x9d6xn14bxyyl878xfm


### Credits
* Qi Deng (finder)


## wolf-rbac plugin Identity Spoofing ## { #CVE-2026-44046 }

CVE-2026-44046 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-44046) [\[CVE json\]](./CVE-2026-44046.cve.json) [\[OSV json\]](./CVE-2026-44046.osv.json)



_Last updated: 2026-06-19T13:08:47.282Z_

### Affected

* Apache APISIX from 1.2.0 through 3.16.0


### Description

<p>Use of Less Trusted Source vulnerability in Apache APISIX.</p>Attacker can take advantage of wolf-rbac plugin under default configuration to potentially pollute logs with spoofed identity information and exploit IP based access control rules.<br><p>This issue affects Apache APISIX: from 1.2.0 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/xkshmps51b24yw0qckl5h5ddyv0x6qf9


### Credits
* Qi Deng (reporter)


## JWT Algorithm Confusion allows authentication bypass ## { #CVE-2026-39999 }

CVE-2026-39999 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-39999) [\[CVE json\]](./CVE-2026-39999.cve.json) [\[OSV json\]](./CVE-2026-39999.osv.json)



_Last updated: 2026-06-19T13:07:45.459Z_

### Affected

* Apache APISIX from 2.2 through 3.16.0


### Description

<p>Authentication Bypass by Spoofing vulnerability in Apache APISIX.</p>The attacker can completely bypass authentication capitalising on certain configurations of jwt-auth plugin.<br><p>This issue affects Apache APISIX: from v2.2 through v3.16.0.</p><p>Users are recommended to upgrade to version v3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/nfopt8cnxd3k0rs1oxtr7lzxrdw4mojq


### Credits
* Marco Capuano (reporter)


## Identity Injection via forward-auth Plugin Missing Header Cleanup ## { #CVE-2026-39998 }

CVE-2026-39998 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-39998) [\[CVE json\]](./CVE-2026-39998.cve.json) [\[OSV json\]](./CVE-2026-39998.osv.json)



_Last updated: 2026-06-19T13:05:07.084Z_

### Affected

* Apache APISIX from 2.12.0 through 3.16.0


### Description

<p>Improper Input Validation vulnerability in Apache APISIX.</p>The attacker can take advantage of certain configuration in forward-auth plugin to spoof identity headers.<br><p>This issue affects Apache APISIX: from 2.12.0 through 3.16.0.</p><p>Users are recommended to upgrade to version 3.17.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/vgkvy396010d7g6m0jrn4d3hjf2svlvv


### Credits
* Fernando Mecozzi (reporter)


## Plugin tencent-cloud-cls log export uses plaintext HTTP ## { #CVE-2026-31924 }

CVE-2026-31924 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31924) [\[CVE json\]](./CVE-2026-31924.cve.json) [\[OSV json\]](./CVE-2026-31924.osv.json)



_Last updated: 2026-04-14T08:08:04.772Z_

### Affected

* Apache APISIX from 2.99.0 through 3.15.0


### Description

<p>Cleartext Transmission of Sensitive Information vulnerability in Apache APISIX.</p>tencent-cloud-cls log export uses plaintext HTTP<br><p>This issue affects Apache APISIX: from 2.99.0 through 3.15.0.</p><p>Users are recommended to upgrade to version 3.16.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/sqxjjlt87c1q28db28ztdxylm5pgwohq


### Credits
* Oleh Konko (finder)


## Openid-connect `tls_verify` field is disabled by default ## { #CVE-2026-31923 }

CVE-2026-31923 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31923) [\[CVE json\]](./CVE-2026-31923.cve.json) [\[OSV json\]](./CVE-2026-31923.osv.json)



_Last updated: 2026-04-14T08:38:57.640Z_

### Affected

* Apache APISIX from 0.7 through 3.15.0


### Description

<p>Cleartext Transmission of Sensitive Information vulnerability in Apache APISIX.</p>This can occur due to `ssl_verify` in openid-connect plugin configuration being set to false by default.<br><p>This issue affects Apache APISIX: from 0.7 through 3.15.0.</p><p>Users are recommended to upgrade to version 3.16.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/0pjs72l7qj83j3srw1l1toyj24bsgkds


### Credits
* Oleh Konko (reporter)


## forward auth plugin allows header injection ## { #CVE-2026-31908 }

CVE-2026-31908 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31908) [\[CVE json\]](./CVE-2026-31908.cve.json) [\[OSV json\]](./CVE-2026-31908.osv.json)



_Last updated: 2026-04-14T08:06:15.933Z_

### Affected

* Apache APISIX from 2.12.0 through 3.15.0


### Description

<p>Header injection vulnerability in Apache APISIX.</p><span style="background-color: rgb(255, 255, 255);">The attacker can take advantage of certain configuration in forward-auth plugin to inject malicious headers.</span><br><p>This issue affects Apache APISIX: from 2.12.0 through 3.15.0.</p><p>Users are recommended to upgrade to version 3.16.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/sob643s5lztov7x579j8o0c444t36n6b


### Credits
* SeungMyung Lee (reporter)


## basic-auth logs plaintext credentials at info level ## { #CVE-2025-62232 }

CVE-2025-62232 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-62232) [\[CVE json\]](./CVE-2025-62232.cve.json) [\[OSV json\]](./CVE-2025-62232.osv.json)



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

CVE-2025-46647 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-46647) [\[CVE json\]](./CVE-2025-46647.cve.json) [\[OSV json\]](./CVE-2025-46647.osv.json)



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

CVE-2025-27446 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-27446) [\[CVE json\]](./CVE-2025-27446.cve.json) [\[OSV json\]](./CVE-2025-27446.osv.json)



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

CVE-2024-32638 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-32638) [\[CVE json\]](./CVE-2024-32638.cve.json) [\[OSV json\]](./CVE-2024-32638.osv.json)



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

CVE-2022-29266 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-29266) [\[CVE json\]](./CVE-2022-29266.cve.json) [\[OSV json\]](./CVE-2022-29266.osv.json)



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

CVE-2022-25757 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-25757) [\[CVE json\]](./CVE-2022-25757.cve.json) [\[OSV json\]](./CVE-2022-25757.osv.json)



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

CVE-2022-24112 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-24112) [\[CVE json\]](./CVE-2022-24112.cve.json) [\[OSV json\]](./CVE-2022-24112.osv.json)



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

CVE-2021-45232 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-45232) [\[CVE json\]](./CVE-2021-45232.cve.json) [\[OSV json\]](./CVE-2021-45232.osv.json)



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

CVE-2021-43557 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-43557) [\[CVE json\]](./CVE-2021-43557.cve.json) [\[OSV json\]](./CVE-2021-43557.osv.json)



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

CVE-2021-33190 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-33190) [\[CVE json\]](./CVE-2021-33190.cve.json) [\[OSV json\]](./CVE-2021-33190.osv.json)



_Last updated: 2021-06-08T15:01:51.802Z_

### Affected

* Apache APISIX Dashboard at Apache APISIX Dashboard 2.6 2.6


### Description

In Apache APISIX Dashboard version 2.6, we changed the default value of listen host to 0.0.0.0 in order to facilitate users to configure external network access. In the IP allowed list restriction, a risky function was used for the IP acquisition, which made it possible to bypass the network limit. At the same time, the default account and password are fixed.Ultimately these factors lead to the issue of security risks.  This issue is fixed in APISIX Dashboard 2.6.1


### References
* https://lists.apache.org/thread.html/re736aea55e8fd2478f0739c0c38a9375c4204fc1f0bd1ea687f57049%40%3Cdev.apisix.apache.org%3E
