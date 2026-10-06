---
title: Apache Roller security advisories
description: Security information for Apache Roller
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache Roller? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Roller).

You can read more about the security policy on:

- [Apache Roller security model](https://github.com/apache/roller/blob/master/docs/security-model.md)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Reflected XSS in the optional LDAP comment authenticator ## { #CVE-2026-91206 }

CVE-2026-91206 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91206) [\[CVE json\]](./CVE-2026-91206.cve.json) [\[OSV json\]](./CVE-2026-91206.osv.json)



_Last updated: 2026-09-28T07:33:12.734Z_

### Affected

* Apache Roller at 6.1.5


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') in Apache Roller 6.1.5 allows a remote attacker to perform reflected cross-site scripting through the optional LDAP comment authenticator, which writes request parameter values into its HTML form without escaping. This affects only sites configured to use LdapCommentAuthenticator, and a victim whose session has already loaded the authenticator form must follow a crafted link. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which escapes the reflected values.

### References
* https://github.com/apache/roller/pull/191
* https://lists.apache.org/thread/tljwqdttq8tgg6hr8sxlcnwpxl6pch4s


### Credits
* 姬珏 (CyberLeo) (finder)


## Stored javascript: URI in HTML comments ## { #CVE-2026-91204 }

CVE-2026-91204 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-91204) [\[CVE json\]](./CVE-2026-91204.cve.json) [\[OSV json\]](./CVE-2026-91204.osv.json)



_Last updated: 2026-09-28T07:34:32.127Z_

### Affected

* Apache Roller at 6.1.5


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') in Apache Roller 6.1.5 allows an anonymous remote attacker to store a comment containing a javascript: URI link that survives HTML comment formatting and can execute script in the browser of a visitor who clicks it. This affects only sites that enable HTML in comments (users.comments.htmlenabled=true) together with the HTMLSubset comment formatter; comment moderation, where enabled, delays publication. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which restricts restored links to http, https and mailto URIs.

### References
* https://github.com/apache/roller/pull/190
* https://lists.apache.org/thread/4qzp8m0438056l5t6m6719ob79gx72lz


### Credits
* 姬珏 (CyberLeo) (finder)


## Stored XSS in comment moderation via comment author URL ## { #CVE-2026-86507 }

CVE-2026-86507 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-86507) [\[CVE json\]](./CVE-2026-86507.cve.json) [\[OSV json\]](./CVE-2026-86507.osv.json)



_Last updated: 2026-09-28T08:27:19.589Z_

### Affected

* Apache Roller at 6.1.5


### Description

Improper neutralization of input in Apache Roller 6.1.5 allows an anonymous remote attacker to store a crafted comment-author URL that can execute script in the session of a weblog moderator or global administrator when the comment management page is viewed. This affects sites that permit comments on at least one weblog and whose moderator subsequently reviews the submitted comment; no non-default server setting is required. Users are recommended to upgrade to Apache Roller 6.1.6 or later.

### References
* https://github.com/apache/roller/pull/181
* https://lists.apache.org/thread/rjyxvm0fgtdfxwkj5qv532htdbs05wff


### Credits
* Ivan Iushkevich (Steph) (finder)


## Stored cross-site scripting through incoming Trackback links ## { #CVE-2026-82546 }

CVE-2026-82546 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82546) [\[CVE json\]](./CVE-2026-82546.cve.json) [\[OSV json\]](./CVE-2026-82546.osv.json)



_Last updated: 2026-09-28T07:35:37.118Z_

### Affected

* Apache Roller at 6.1.5


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') in Apache Roller 6.1.5 allows an unauthenticated remote attacker to store a crafted comment-author URL through the incoming Trackback endpoint when a published entry accepts comments and Trackbacks. The shipped Trackback, verification and moderation defaults allow the value to be approved and rendered as an active link; a visitor who clicks the link executes script in the weblog's origin. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which removes incoming Trackback support and suppresses non-HTTP(S) comment-author links. Users unable to upgrade should disable Trackbacks and remove untrusted Trackback comments.

### References
* https://github.com/apache/roller/pull/178
* https://lists.apache.org/thread/ddrykzvs67zpmzwsbqyfjmlydboln8x1


### Credits
* m4dn355 (finder)


## Stored cross-site scripting via uploaded media content type ## { #CVE-2026-82387 }

CVE-2026-82387 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82387) [\[CVE json\]](./CVE-2026-82387.cve.json) [\[OSV json\]](./CVE-2026-82387.osv.json)



_Last updated: 2026-09-28T07:36:11.303Z_

### Affected

* Apache Roller at 6.1.5


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') in Apache Roller 6.1.5 allows a user with media-upload rights to store active content on Roller's origin, because the media upload feature trusts the upload-supplied content type and serves the stored file back with that type. A victim who opens the uploaded file executes the stored script. Media uploads are disabled by default; only installations that enable them are affected, and the shipped type restrictions do not block active content once uploads are on. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which derives the stored type from file content and serves non-image media as a download.

### References
* https://github.com/apache/roller/pull/174
* https://lists.apache.org/thread/9h1d77xjjk6q90k7l8y7nyffg6ltdzxo


### Credits
* m4dn355 (finder)


## XML external entity processing in OPML bookmark import ## { #CVE-2026-82386 }

CVE-2026-82386 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82386) [\[CVE json\]](./CVE-2026-82386.cve.json) [\[OSV json\]](./CVE-2026-82386.osv.json)



_Last updated: 2026-09-28T07:43:30.531Z_

### Affected

* Apache Roller at 6.1.5


### Description

Improper Restriction of XML External Entity Reference in Apache Roller 6.1.5 allows a weblog administrator to read files readable by the Roller process and reach internal network addresses by importing a crafted OPML document, because the bookmark import parser does not disable external entity resolution. No non-default configuration is required; the import is reached through the administrator bookmark-import action. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which uses a hardened parser that disables external entities and document type declarations.

### References
* https://github.com/apache/roller/pull/173
* https://lists.apache.org/thread/mrtstv8odj7l9mcrto445lftrcpw0sxl


### Credits
* n0mi1k (finder)


## Weblog template include escapes the Velocity sandbox and reads classpath files ## { #CVE-2026-82385 }

CVE-2026-82385 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82385) [\[CVE json\]](./CVE-2026-82385.cve.json) [\[OSV json\]](./CVE-2026-82385.osv.json)



_Last updated: 2026-09-28T07:44:06.239Z_

### Affected

* Apache Roller at 6.1.5


### Description

Exposure of Sensitive Information to an Unauthorized Actor in Apache Roller 6.1.5 allows a weblog administrator to read files on the application classpath, including Roller configuration files containing secrets, by authoring a Velocity template that uses an include directive to load a classpath resource outside the theme namespace. Roller treats weblog administrators as untrusted and enables a Velocity sandbox, but the include and parse directives are not confined by it. No non-default configuration is required; this affects any weblog whose administrator can author templates. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which confines includes to the active theme and removes classpath resource loading from weblog rendering.

### References
* https://github.com/apache/roller/pull/172
* https://lists.apache.org/thread/wfy8jrwf4xk6r8xgd4rosnxwjwdn4znx


### Credits
* n0mi1k (finder)


## Unauthenticated deserialization in the XML-RPC endpoint ## { #CVE-2026-82384 }

CVE-2026-82384 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82384) [\[CVE json\]](./CVE-2026-82384.cve.json) [\[OSV json\]](./CVE-2026-82384.osv.json)



_Last updated: 2026-09-28T07:47:42.534Z_

### Affected

* Apache Roller at 6.1.5


### Description

Deserialization of Untrusted Data in Apache Roller 6.1.5 allows an unauthenticated remote attacker to cause deserialization of attacker-controlled bytes, because the XML-RPC endpoint accepts vendor extension types that are deserialized during request parsing, before authentication. The servlet is mapped unconditionally, so parsing occurs even when the global XML-RPC feature is set to disabled; no non-default configuration is required for this path. This can lead to remote code execution. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which disables the extension types and rejects requests when the XML-RPC feature is disabled.

### References
* https://github.com/apache/roller/pull/171
* https://lists.apache.org/thread/21p1dh6x179gmcdpw84kkx9yclrdp410


### Credits
* n0mi1k (finder)


## Anonymous setup action allows frontpage configuration tampering ## { #CVE-2026-82383 }

CVE-2026-82383 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82383) [\[CVE json\]](./CVE-2026-82383.cve.json) [\[OSV json\]](./CVE-2026-82383.osv.json)



_Last updated: 2026-09-28T07:48:33.373Z_

### Affected

* Apache Roller at 6.1.5


### Description

Missing Authentication for Critical Function in Apache Roller 6.1.5 allows an unauthenticated remote attacker to persistently change a site-global configuration value (the frontpage weblog selection) on any installed instance, because the setup action remains anonymously reachable after installation and persists configuration without an authorization check. No optional feature or non-default configuration is required; the result can redirect or break the site's public frontpage, with administrative recovery available. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which restricts the write to global administrators.

### References
* https://github.com/apache/roller/pull/170
* https://lists.apache.org/thread/7oof135zr05zfkslj9s6m5o0brll47dz


### Credits
* meifukun (finder)


## Reflected cross-site scripting in the frontpage directory parameter ## { #CVE-2026-82382 }

CVE-2026-82382 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82382) [\[CVE json\]](./CVE-2026-82382.cve.json) [\[OSV json\]](./CVE-2026-82382.osv.json)



_Last updated: 2026-09-28T07:51:29.958Z_

### Affected

* Apache Roller at 6.1.5


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') in Apache Roller 6.1.5 allows a remote attacker to perform reflected cross-site scripting against a visitor to a weblog using the bundled frontpage theme, by supplying a crafted blog-directory parameter that the directory page reflects without proper escaping. This affects only weblogs that use the bundled frontpage theme, and a victim must follow a crafted link for the script to execute. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which validates and contextually escapes the reflected parameter.

### References
* https://github.com/apache/roller/pull/169
* https://lists.apache.org/thread/mt01qhjq701o3v7kddgskn2ryb6l6y2x


### Credits
* meifukun (finder)


## Stored cross-site scripting in the authoring UI ## { #CVE-2026-82381 }

CVE-2026-82381 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82381) [\[CVE json\]](./CVE-2026-82381.cve.json) [\[OSV json\]](./CVE-2026-82381.osv.json)



_Last updated: 2026-09-28T07:51:53.740Z_

### Affected

* Apache Roller at 6.1.5


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') in Apache Roller 6.1.5 allows a user with authoring rights on a weblog to store crafted content that is later written into the authoring UI's JavaScript string literals and markup sinks without proper encoding, causing the stored script to execute in another author's or administrator's browser. No optional feature or non-default configuration is required; this affects weblogs with multiple authors or administrators who are not mutually trusted. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which moves those values out of JavaScript literals and writes them as text.

### References
* https://github.com/apache/roller/pull/168
* https://lists.apache.org/thread/5qvk6j5r8ttm4vx4ntxqt6bjz6pg4r46


### Credits
* meifukun (finder)


## CSRF protection bypass via self-generated salt validation ## { #CVE-2026-82380 }

CVE-2026-82380 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82380) [\[CVE json\]](./CVE-2026-82380.cve.json) [\[OSV json\]](./CVE-2026-82380.osv.json)



_Last updated: 2026-09-28T07:52:26.837Z_

### Affected

* Apache Roller at 6.1.5


### Description

Cross-Site Request Forgery (CSRF) in Apache Roller 6.1.5 allows a remote attacker to cause a logged-in user to perform state-changing actions under the victim's authority, because the CSRF validation filters accept a request that does not submit the required salt token, validating instead against a value the server itself generated for the request. No optional feature or non-default configuration is required; any logged-in author or administrator is affected when induced to visit a crafted page. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which validates only the submitted salt and applies the same check to multipart forms.

### References
* https://github.com/apache/roller/pull/167
* https://lists.apache.org/thread/db5zl0wrf2c888qwkqmxymddfjc594q8


### Credits
* meifukun (finder)


## WSSE digest authentication headers can be replayed ## { #CVE-2026-82379 }

CVE-2026-82379 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82379) [\[CVE json\]](./CVE-2026-82379.cve.json) [\[OSV json\]](./CVE-2026-82379.osv.json)



_Last updated: 2026-09-28T07:53:04.246Z_

### Affected

* Apache Roller at 6.1.5


### Description

Authentication Bypass by Capture-replay in Apache Roller 6.1.5 allows an attacker who captures a valid WSSE digest authentication header to replay it and gain the victim's AtomPub authority, because the authentication does not enforce nonce uniqueness or timestamp freshness. Only installations that enable the non-default AtomPub API with WSSE authentication and plaintext-compatible password storage are affected. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which removes WSSE as an AtomPub authentication method; existing installations configured for WSSE fail closed until an administrator explicitly selects a supported authentication method.

### References
* https://github.com/apache/roller/pull/166
* https://lists.apache.org/thread/bg5r225c3z4148z6kf7s3fwwgrs2lx02


### Credits
* meifukun (finder)


## OAuth authorization endpoint trusts request-supplied identity ## { #CVE-2026-82378 }

CVE-2026-82378 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82378) [\[CVE json\]](./CVE-2026-82378.cve.json) [\[OSV json\]](./CVE-2026-82378.osv.json)



_Last updated: 2026-09-28T07:45:09.902Z_

### Affected

* Apache Roller at 6.1.5


### Description

Incorrect Authorization in the OAuth 1.0a authorization endpoint of Apache Roller 6.1.5 allows an unauthenticated remote attacker who learns an outstanding request token for a configured site-wide consumer to bind that token to an arbitrary user account, including an administrator, by submitting an unsigned authorization request. The endpoint derives the authorizing identity from a request-supplied value rather than the authenticated session. Only installations that configure an OAuth 1.0a site-wide consumer are affected, and exploitation requires knowledge of one of its outstanding request tokens. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which binds authorization to the logged-in session.

### References
* https://github.com/apache/roller/pull/165
* https://lists.apache.org/thread/fq512gy70zj9yx8v4c4zm54x43wqb04b


### Credits
* meifukun (finder)


## Missing weblog authorization in XML-RPC Blogger/MetaWeblog handlers ## { #CVE-2026-82377 }

CVE-2026-82377 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82377) [\[CVE json\]](./CVE-2026-82377.cve.json) [\[OSV json\]](./CVE-2026-82377.osv.json)



_Last updated: 2026-09-28T07:45:39.178Z_

### Affected

* Apache Roller at 6.1.5


### Description

Missing Authorization in Apache Roller 6.1.5 allows an authenticated user to read, modify, or delete weblog content belonging to other weblogs through the legacy XML-RPC Blogger and MetaWeblog APIs, because the handlers authenticate the caller but do not verify the caller's permission on the weblog or entry actually affected. Only installations that enable the non-default global XML-RPC setting are affected; the per-weblog API flag defaults to enabled for UI-created weblogs. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which applies an explicit per-method permission check, or to keep the XML-RPC feature disabled.

### References
* https://github.com/apache/roller/pull/164
* https://lists.apache.org/thread/phxx56n0w6jjqzto2my3ot8hto0qjvn8


### Credits
* meifukun (finder)
* n0mi1k (finder)
* Ivan Iushkevich (Steph) (finder)


## XML external entity processing in trackback response parser ## { #CVE-2026-82376 }

CVE-2026-82376 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82376) [\[CVE json\]](./CVE-2026-82376.cve.json) [\[OSV json\]](./CVE-2026-82376.osv.json)



_Last updated: 2026-09-28T07:46:09.207Z_

### Affected

* Apache Roller at 6.1.5


### Description

Improper Restriction of XML External Entity Reference in Apache Roller 6.1.5 allows a user with entry-editing rights on a weblog to cause the server to parse an attacker-influenced trackback response with an XML parser that does not disable external entity resolution, leading to disclosure of files readable by the Roller process. The Trackback control is hidden in the standard UI, but its action remains directly reachable, and no non-default server configuration is required. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which removes the outbound trackback response parser.

### References
* https://github.com/apache/roller/pull/163
* https://lists.apache.org/thread/dxqmd3873q87h06xpjjc9lnvp4jblz0l


### Credits
* meifukun (finder)


## Server-side request forgery via entry trackback and enclosure URLs ## { #CVE-2026-82375 }

CVE-2026-82375 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82375) [\[CVE json\]](./CVE-2026-82375.cve.json) [\[OSV json\]](./CVE-2026-82375.osv.json)



_Last updated: 2026-09-28T07:46:47.447Z_

### Affected

* Apache Roller at 6.1.5


### Description

Server-Side Request Forgery (SSRF) in Apache Roller 6.1.5 allows an authenticated user with entry-editing rights on a weblog to cause outbound HTTP requests to attacker-chosen destinations through legacy outbound Trackback and entry enclosure handling. The Trackback control is hidden in the standard UI, but its action remains directly reachable; the enclosure path is relevant only when an author supplies an enclosure URL. No non-default server configuration is required, and the default empty Trackback allow-list permits all destinations. Requests can reach loopback and private-network addresses, while enclosure handling exposes response status, content type, and length. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which removes the outbound trackback action and stops dereferencing enclosure URLs.

### References
* https://github.com/apache/roller/pull/175
* https://github.com/apache/roller/pull/163
* https://lists.apache.org/thread/0p7kc0rjcpj3rf00cp96zfkfrz0ns4ny


### Credits
* meifukun (finder)
* n0mi1k (finder)


## Cross-weblog resource tampering via unscoped authoring lookups ## { #CVE-2026-82348 }

CVE-2026-82348 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82348) [\[CVE json\]](./CVE-2026-82348.cve.json) [\[OSV json\]](./CVE-2026-82348.osv.json)



_Last updated: 2026-09-28T07:36:44.678Z_

### Affected

* Apache Roller at 6.1.5


### Description

Authorization Bypass Through User-Controlled Key in Apache Roller 6.1.5 allows an authenticated user with authoring rights on one weblog to read, modify, or delete resources belonging to another weblog through unscoped identifier-based lookups. This affects multi-user installations where users are intended to be isolated between weblogs; no optional feature or non-default configuration is required. A user with administrator rights on their weblog can also overwrite another weblog's Velocity template, whose content is evaluated when the victim weblog renders. Users are recommended to upgrade to Apache Roller 6.1.6 or later, which scopes authoring resource lookups to the acting weblog.

### References
* https://github.com/apache/roller/pull/162
* https://lists.apache.org/thread/3h7zk8dhbt8fj5zdt8cjghx0b807wgy1


### Credits
* meifukun (finder)
* n0mi1k (finder)
* Ivan Iushkevich (Steph) (finder)


## Insufficient Session Expiration on Password Change ## { #CVE-2025-24859 }

CVE-2025-24859 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-24859) [\[CVE json\]](./CVE-2025-24859.cve.json) [\[OSV json\]](./CVE-2025-24859.osv.json)



_Last updated: 2025-04-18T15:26:03.795Z_

### Affected

* Apache Roller from 1.0.0 before 6.1.5


### Description

<p></p><pre><code>A session management vulnerability exists in Apache Roller before version 6.1.5 where active user sessions are not properly invalidated after password changes. When a user's password is changed, either by the user themselves or by an administrator, existing sessions remain active and usable. This allows continued access to the application through old sessions even after password changes, potentially enabling unauthorized access if credentials were compromised.

This issue affects Apache Roller versions up to and including 6.1.4.

The vulnerability is fixed in Apache Roller 6.1.5 by implementing centralized session management that properly invalidates all active sessions when passwords are changed or users are disabled.
</code></pre><br><br><p></p>

### References
* https://lists.apache.org/thread/vxv52vdr8nhtjlj6v02w43fdvo0cxw23
* https://lists.apache.org/thread/4j906k16v21kdx8hk87gl7663sw7lg7f


### Credits
* Haining Meng (finder)


## Weakness in CSRF protection allows privilege escalation ## { #CVE-2024-46911 }

CVE-2024-46911 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-46911) [\[CVE json\]](./CVE-2024-46911.cve.json) [\[OSV json\]](./CVE-2024-46911.osv.json)



_Last updated: 2024-10-11T21:53:17.272Z_

### Affected

* Apache Roller from 1.0.0 before 6.1.4


### Description

<p>Cross-site Resource Forgery (CSRF), Privilege escalation vulnerability in Apache Roller. On multi-blog/user Roller websites, by default weblog owners are trusted to publish arbitrary weblog content and this combined with a deficiency in Roller's CSRF protections allowed an escalation of privileges attack. This issue affects Apache Roller before 6.1.4.</p><p>Roller users who run multi-blog/user Roller websites are recommended to upgrade to version 6.1.4, which fixes the issue.</p>Roller 6.1.4 release announcement:&nbsp;<a target="_blank" rel="nofollow" href="https://lists.apache.org/thread/3c3f6rwqptyw6wdc95654fq5vlosqdpw">https://lists.apache.org/thread/3c3f6rwqptyw6wdc95654fq5vlosqdpw</a><br><br>

### References
* https://lists.apache.org/thread/6m0ghjo9j92qty00t2qb6qf2spds0p5t


### Credits
* Chi Tran from EEVEE (finder)


## Insufficient input validation for some user profile and bookmark fields when Roller in untested-users mode ## { #CVE-2024-25090 }

CVE-2024-25090 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-25090) [\[CVE json\]](./CVE-2024-25090.cve.json) [\[OSV json\]](./CVE-2024-25090.osv.json)



_Last updated: 2024-07-26T08:36:45.293Z_

### Affected

* Apache Roller from 5.0.0 before 6.1.3


### Description

<p>Insufficient input validation and sanitation in Profile name &amp; screenname, Bookmark name &amp; description and blogroll name features in all versions of Apache Roller on all platforms allows an authenticated user to perform an XSS attack. Mitigation: if you do not have Roller configured for untrusted users, then you need to do nothing because you trust your users to author raw HTML and other web content. If you are running with untrusted users then you should upgrade to Roller 6.1.3.</p><p>This issue affects Apache Roller: from 5.0.0 before 6.1.3.</p><p>Users are recommended to upgrade to version 6.1.3, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/lb50jqyxwf8jrfpydl6dc5zpqtpgrrwd


### Credits
* Jacob Hazak (reporter)


## Roller's weblog category, weblog settings and file-upload features did not properly sanitize input could be exploited to perform Reflected Cross Site Scripting (XSS) even on a Roller site configured for untrusted users. ## { #CVE-2023-37581 }

CVE-2023-37581 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-37581) [\[CVE json\]](./CVE-2023-37581.cve.json) [\[OSV json\]](./CVE-2023-37581.osv.json)



_Last updated: 2023-08-24T08:15:22.581Z_

### Affected

* Apache Roller before 6.1.2


### Description

<span style="background-color: rgb(255, 255, 255);">Insufficient input validation and sanitation in Weblog Category name, Website About and File Upload features in all versions of Apache Roller on all platforms allows an authenticated user to perform an XSS attack. </span><span style="background-color: var(--wht);">Mitigation: if you do not have Roller configured for untrusted users, then you need to do nothing because you trust your users to author raw HTML and other web content. If you are running with untrusted users then you should upgrade to Roller 6.1.2 and you should disable Roller's File Upload feature. </span><br><br><p></p>

### References
* https://lists.apache.org/thread/n9mjhhlm7z7b7to646tkvf3otkf21flp
* https://www.openwall.com/lists/oss-security/2023/08/16/1


### Credits
* SecureLayer7 Technologies Pvt Ltd (finder)


## regex injection leading to DoS ## { #CVE-2021-33580 }

CVE-2021-33580 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-33580) [\[CVE json\]](./CVE-2021-33580.cve.json) [\[OSV json\]](./CVE-2021-33580.osv.json)



_Last updated: 2021-08-18T07:43:44.770Z_

### Affected

* Apache Roller from Apache Roller before 6.0.2


### Description

User controlled `request.getHeader("Referer")`, `request.getRequestURL()` and `request.getQueryString()` are used to build and run a regex expression.

The attacker doesn't have to use a browser and may send a specially crafted Referer header programmatically. Since the attacker controls the string and the regex pattern he may cause a ReDoS by regex catastrophic backtracking on the server side.  This problem has been fixed in Roller 6.0.2.





### References
* https://lists.apache.org/thread.html/r9d967d80af941717573e531db2c7353a90bfd0886e9b5d5d79f75506%40%3Cuser.roller.apache.org%3E


### Credits
* Apache Roller would like to thank Ed Ra (https://github.com/edvraa) for reporting this.
