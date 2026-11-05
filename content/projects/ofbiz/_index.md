---
title: Apache OFBiz security advisories
description: Security information for Apache OFBiz
layout: single
---

# Reporting

Do you want to disclose a potential security issue for Apache OFBiz? Send your report to the [Apache OFBiz Security Team](mailto:security@ofbiz.apache.org?subject=OFBiz).

You can read more about the security policy on:

- [Apache OFBiz security model](https://ofbiz.apache.org/security.html)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Insufficiently Protected Credentials in ViewFile Enable Authentication Bypass ## { #CVE-2026-97356 }

CVE-2026-97356 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97356) [\[CVE json\]](./CVE-2026-97356.cve.json) [\[OSV json\]](./CVE-2026-97356.osv.json)



_Last updated: 2026-11-05T13:44:51.603Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

External Control of File Name or Path vulnerability in the ViewFile component of Label Manager in Apache OFBiz 24.09.07 on all platforms allows an authenticated user holding only the LABEL_MANAGER_VIEW permission to read arbitrary properties and xml files on the server, including the generated JWT signing key, enabling forgery of an authenticated administrator session, via the fileName parameter of a ViewFile request.<br>Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Gaosong Zhang (zhanggaosong@fudan.edu.cn) (reporter)
* Zeo666666 (reporter)


## Hard-coded Credentials in AdminServer Enable Unauthenticated Denial of Service ## { #CVE-2026-97355 }

CVE-2026-97355 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-97355) [\[CVE json\]](./CVE-2026-97355.cve.json) [\[OSV json\]](./CVE-2026-97355.osv.json)



_Last updated: 2026-11-05T13:45:21.148Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Use of Hard-coded Password vulnerability in the AdminServer component in Apache OFBiz 24.09.07 on all platforms allows an attacker able to reach the AdminServer control port to query the server's running state and trigger an unauthenticated shutdown of the instance via the fixed default control key shipped in start.properties.<br>Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Gaosong Zhang (zhanggaosong@fudan.edu.cn) (reporter)


## REST API authentication bypassed by default when the auth attribute is omitted from a .rest.xml operation ## { #CVE-2026-92887 }

CVE-2026-92887 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-92887) [\[CVE json\]](./CVE-2026-92887.cve.json) [\[OSV json\]](./CVE-2026-92887.osv.json)



_Last updated: 2026-11-05T13:45:49.861Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Incorrect default value in the REST API framework's .rest.xml definition parser (ModelApiReader) in Apache OFBiz through 24.09.07 on all platforms allows a remote, unauthenticated attacker to invoke a REST API operation without providing valid credentials via a .rest.xml resource or operation definition that omits the auth attribute, which ModelApiReader incorrectly resolves to false instead of the true default declared by rest-api.xsd.<br><br>Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Wanxin Yin (yaklang.io) (reporter)


## Authenticated Code Execution Vulnerability ## { #CVE-2026-85627 }

CVE-2026-85627 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-85627) [\[CVE json\]](./CVE-2026-85627.cve.json) [\[OSV json\]](./CVE-2026-85627.osv.json)



_Last updated: 2026-11-05T13:53:24.529Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Improper Neutralization of Special Elements Used in a Template Engine ('Server-Side Template Injection') in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated attacker holding only a stock non-administrative account to execute arbitrary operating system commands as the OFBiz process user, by using the updateLayoutImage event, which writes DataResource fields with no permission check, to retype an attacker-created DataResource as an FTL template evaluating its own primary key, then using the resulting FreeMarker evaluation to plant an OFBiz Form Widget whose use-when attribute runs unsandboxed Groovy. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Utku Sen (reporter)
* Krishna Uprit (remediation developer)


## Cross-tenant authorization bypass in mapped-domain login ## { #CVE-2026-84728 }

CVE-2026-84728 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-84728) [\[CVE json\]](./CVE-2026-84728.cve.json) [\[OSV json\]](./CVE-2026-84728.osv.json)



_Last updated: 2026-11-05T13:57:00.589Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

<span></span>Incorrect Authorization in Apache OFBiz 
24.09 before 24.09.08 on all platforms, when documented multitenancy is 
enabled, allows a remote authenticated attacker holding only a valid 
low-privilege account in one tenant to read and write data belonging to a
 different tenant, by submitting their own tenant's userTenantId 
alongside their own credentials to the normal Party Manager login 
against a hostname mapped to a different tenant: ContextFilter resolves 
the tenant from the hostname via TenantDomainName, but LoginWorker gives
 priority to the conflicting userTenantId request parameter and 
authenticates against the attacker's own tenant, so a subsequent 
ordinary request to the same hostname combines the hostname-mapped 
tenant's Entity Engine delegator with the attacker's tenant's session 
dispatcher, security object, and identity, letting the permission check 
run against the attacker's own tenant while the resulting read or write 
is performed against the hostname-mapped tenant's data. Users are 
recommended to upgrade to version 24.09.08, which fixes this issue.<span></span>

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Jonah Burgess (CryptoCat) (reporter)
* Krishna Uprit (remediation developer)


## Content Manager VIEW-only RCE in updateLayout ## { #CVE-2026-84183 }

CVE-2026-84183 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-84183) [\[CVE json\]](./CVE-2026-84183.cve.json) [\[OSV json\]](./CVE-2026-84183.osv.json)



_Last updated: 2026-11-05T13:58:54.081Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Incorrect Authorization in the updateLayout simple-method in applications/content/minilang/layout/LayoutEvents.xml in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated attacker holding only OFBTOOLS_VIEW and CONTENTMGR_VIEW to execute arbitrary commands as the OFBiz process user, by using updateLayout's authorization check — which validates only the fixed CONTENT_CREATE operation rather than an update permission on the actual Content record and an independently selected DataResource — to relink an existing RESPONSE-purpose Content record and convert an arbitrary, independently selected DataResource into an OFBIZ_FILE/FTL resource pointed at the OFBiz access log, poisoned via a crafted User-Agent header and evaluated through the normal authenticated showContent route. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Jonah Burgess (CryptoCat) (reporter)
* Krishna Uprit (remediation developer)


## Unauthenticated RCE via login-page widget injection ## { #CVE-2026-83542 }

CVE-2026-83542 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-83542) [\[CVE json\]](./CVE-2026-83542.cve.json) [\[OSV json\]](./CVE-2026-83542.osv.json)



_Last updated: 2026-11-05T13:59:21.183Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Improper Control of Generation of Code ('Code Injection') in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote unauthenticated attacker to execute arbitrary code on the server by staging crafted widget XML in a multipart upload and overriding the mainDecoratorLocation used by a manager login route through an anonymous JSON request, causing OFBiz to load the staged XML through its live screen descriptor mechanism and evaluate an unsandboxed Groovy expression while rendering the authentication-failure page. Further validation established the following:<br><br>-- The exploit does not require a malformed or incomplete multipart body: a well-formed multipart request that is kept in flight and then allowed to complete normally is sufficient.<br><br>-- The screen loader reads the widget XML from a live process file descriptor while the upload is streaming, rather than from any file the attacker persists to disk.<br><br>-- The same underlying issue is also reachable through the public, explicitly unauthenticated /sfa/control/editPortalPageColumnWidth route, returning command output directly in an HTTP 200 response — it is not limited to the login-failure rendering path used in the original report.<br><br>Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Jonah Burgess (CryptoCat) (reporter)
* Krishna Uprit (remediation developer)
* David Crees, Abstract Shield (reporter)


## Unauthenticated disclosure through HR, Catalog, and Order Manager helpers ## { #CVE-2026-83538 }

CVE-2026-83538 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-83538) [\[CVE json\]](./CVE-2026-83538.cve.json) [\[OSV json\]](./CVE-2026-83538.osv.json)



_Last updated: 2026-11-05T14:00:53.129Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Missing Authorization in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote unauthenticated attacker to disclose internal business records — including organization, employee, product catalog, and product-store data — by requesting several helper endpoints across the Human Resources, Catalog, and Order Manager applications that are configured to skip authentication and perform no permission check before returning the requested record. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Jonah Burgess (CryptoCat) (reporter)
* Krishna Uprit (remediation developer)


## Widget use-when Expression Injection Bypasses Groovy Sandbox for authenticated RCE ## { #CVE-2026-82960 }

CVE-2026-82960 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82960) [\[CVE json\]](./CVE-2026-82960.cve.json) [\[OSV json\]](./CVE-2026-82960.osv.json)



_Last updated: 2026-11-05T14:01:21.652Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Improper Control of Generation of Code ('Code Injection') in ModelFormField in the Apache OFBiz cms plugin before 24.09.08 on all platforms allows a remote authenticated attacker holding only CMS content-editor access to execute arbitrary operating system commands as the OFBiz process user via a single HTTP POST request, by submitting a crafted caContentIdTo parameter to EditAddContent, because the CMS screen copies that parameter into a top-level context variable that is interpolated into a form field's use-when attribute and the resulting string is passed unvalidated to GroovyUtil.eval(), whose compile-time SecureASTCustomizer sandbox does not restrict runtime reflection, allowing a payload that closes the expanded string literal and invokes java.lang.Runtime via reflection. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* MopMonk AI (reporter)
* Krishna Uprit (remediation developer)


## webtools xmldsdump exports any entity to any path ## { #CVE-2026-82916 }

CVE-2026-82916 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82916) [\[CVE json\]](./CVE-2026-82916.cve.json) [\[OSV json\]](./CVE-2026-82916.osv.json)



_Last updated: 2026-11-05T14:01:48.181Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Missing Authorization in XmlDsDump in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated attacker holding only the webtools base permissions (OFBTOOLS_VIEW, WEBTOOLS_VIEW) — explicitly not the ENTITY_MAINT permission the export feature declares and visibly refuses to render for — to export the contents of any database entity, including UserLogin with its currentPassword hashes, to any filesystem path the OFBiz process can write, including a web-served docroot, and to create arbitrary directories or truncate arbitrary existing files at those paths, because the XmlDsDump screen action writes the requested entity data via new FileOutputStream on unvalidated outpath and filename request parameters before the screen's ENTITY_MAINT permission check runs, unlike the equivalent Java service entityExportAll, which enforces both a permission check and a file-path allow-list. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Bartlomiej Dmitruk at striga.ai (reporter)
* Krishna Uprit (remediation developer)


## Unsandboxed Groovy compiled from a service parameter ## { #CVE-2026-82912 }

CVE-2026-82912 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82912) [\[CVE json\]](./CVE-2026-82912.cve.json) [\[OSV json\]](./CVE-2026-82912.osv.json)



_Last updated: 2026-11-05T14:02:26.363Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Improper Neutralization of Special Elements Used in an Expression Language Statement ('Expression Language Injection') in EmailServices in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated attacker holding only OFBTOOLS_VIEW and ACCOUNTING_VIEW, the two view-level permissions that open the Accounting application, to execute arbitrary operating system commands as the account running OFBiz, by submitting a ${groovy:...} expression as the bodyText or subject value to the shipped Send Per Email invoice form, because sendMailFromScreen passes those caller-supplied values through FlexibleStringExpander.expandString, which compiles and evaluates embedded Groovy on a class loader that carries none of the SecureASTCustomizer restrictions GroovyUtil.eval applies elsewhere, behind a service and request-map that declare no permission check beyond base authentication. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Bartlomiej Dmitruk at striga.ai (reporter)
* Ve1ledJustice (reporter)
* Krishna Uprit (remediation developer)


## renderLink compiles link parameters as FreeMarker source ## { #CVE-2026-82910 }

CVE-2026-82910 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82910) [\[CVE json\]](./CVE-2026-82910.cve.json) [\[OSV json\]](./CVE-2026-82910.osv.json)



_Last updated: 2026-11-05T14:03:19.022Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Improper Neutralization of Special Elements Used in a Template Engine ('Server-Side Template Injection') in MacroScreenRenderer in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated attacker holding only the two view permissions of a control-servlet webapp (e.g. CATALOG_VIEW and OFBTOOLS_VIEW on /catalog, held by OFBiz's own shipped order-entry clerk role) to execute arbitrary operating system commands as the OFBiz service account with a single GET request, by placing an apostrophe followed by FreeMarker expression source in a screen link parameter value, because renderLink concatenates link parameter values verbatim between apostrophes into an unquoted, unescaped template-source string that is compiled and evaluated at render time, allowing the injected expression to reach the allow-listed FlexibleStringExpander.expandString call and, through a runtime-assembled Groovy interpolation, unsandboxed code execution. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Bartlomiej Dmitruk at striga.ai (reporter)
* Krishna Uprit (remediation developer)


## externalLoginKey honoured pre-auth, reusable and unbound ## { #CVE-2026-82907 }

CVE-2026-82907 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82907) [\[CVE json\]](./CVE-2026-82907.cve.json) [\[OSV json\]](./CVE-2026-82907.osv.json)



_Last updated: 2026-11-05T14:04:05.629Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Authentication Bypass by Capture-replay in ExternalLoginKeysManager in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote unauthenticated attacker who captures a live externalLoginKey value to obtain a complete, cookie-free, reusable session as the user who issued it, in every webapp that user can reach, because checkExternalLoginKey runs as a global preprocessor ahead of both the CSRF and authentication checks and accepts the key as a bearer credential that is never bound to a client, never expires, and is not invalidated after use, while the framework itself both appends live keys to every cross-webapp link it renders and, via WidgetWorker's unvalidated inter-app link target, lets an authenticated user's key be attached to an attacker-chosen absolute URL and delivered directly to the attacker's own server. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Bartlomiej Dmitruk at striga.ai (reporter)
* Krishna Uprit (remediation developer)


## Unbounded multi-form row count from a parameter name ## { #CVE-2026-82904 }

CVE-2026-82904 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82904) [\[CVE json\]](./CVE-2026-82904.cve.json) [\[OSV json\]](./CVE-2026-82904.osv.json)



_Last updated: 2026-11-05T14:04:38.594Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Uncontrolled Resource Consumption in ServiceMultiEventHandler in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote unauthenticated attacker to pin a server request thread for an attacker-chosen number of synchronous service dispatches, up to the signed-integer maximum, by submitting a single small HTTP request whose parameter names encode a row count via the "o" suffix used by multi-form submissions, because UtilHttp.getMultiFormRowCount derives that count from the largest such suffix with no upper bound and ServiceMultiEventHandler.invoke then loops that many times calling dispatcher.runSync, with the request-map for getFinAccountTransRunningTotalAndBalances reaching this handler with no authentication or CSRF requirement on a stock deployment. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Bartlomiej Dmitruk at striga.ai (reporter)
* CyberLeo (reporter)
* Krishna Uprit (remediation developer)


## Unfiltered server-side URL fetch in webtools viewdatafile ## { #CVE-2026-82902 }

CVE-2026-82902 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82902) [\[CVE json\]](./CVE-2026-82902.cve.json) [\[OSV json\]](./CVE-2026-82902.osv.json)



_Last updated: 2026-11-05T14:05:19.901Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Server-Side Request Forgery in ViewDataFile in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated attacker holding only the base webtools permissions (OFBTOOLS_VIEW, WEBTOOLS_VIEW) to cause the server to issue arbitrary outbound HTTP requests, and an attacker additionally holding ENTITY_MAINT and DATAFILE_MAINT to read arbitrary local files via a file: URL, by supplying the DEFINITION_LOCATION or DATAFILE_LOCATION request parameter to the viewdatafile screen, because ViewDataFile.groovy dereferences both parameters as java.net.URL objects with no scheme allow-list, host filter, or egress control inside a screen action that runs before the screen's and template's permission checks are evaluated, so the fetch executes regardless of whether the requesting account is authorized to view its result. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Bartlomiej Dmitruk at striga.ai (reporter)
* Krishna Uprit (remediation developer)
* David Crees, Abstract Shield (reporter)


## Content renderer runs a service name stored on the row ## { #CVE-2026-82894 }

CVE-2026-82894 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-82894) [\[CVE json\]](./CVE-2026-82894.cve.json) [\[OSV json\]](./CVE-2026-82894.osv.json)



_Last updated: 2026-11-05T14:05:42.909Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Improper Authorization in ContentWorker in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote unauthenticated attacker to trigger arbitrary OFBiz service invocation with attacker-controlled parameters, resulting in arbitrary file write, arbitrary file deletion, and server-side request forgery, by requesting the public showHelpPublic view against a Content row whose serviceName field an account holding only CONTENTMGR_CREATE or CONTENTMGR_UPDATE has set to an attacker-chosen service, causing ContentWorker.renderContentAsText to resolve the service to invoke from that persisted, client-writable field and build its parameters directly from the live HTTP request map with no allow-list, no ownership check, and no requirement that the caller be authenticated. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Bartlomiej Dmitruk at striga.ai (reporter)
* Krishna Uprit (remediation developer)
* Jonah Burgess (CryptoCat) (reporter)


## Server-side request forgery in SurveyWrapper ## { #CVE-2026-81828 }

CVE-2026-81828 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-81828) [\[CVE json\]](./CVE-2026-81828.cve.json) [\[OSV json\]](./CVE-2026-81828.osv.json)



_Last updated: 2026-11-05T14:06:06.140Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Server-Side Request Forgery in SurveyWrapper in Apache OFBiz 24.09 before 24.09.08 on all platforms allows an authenticated back-office user holding catalog permission to cause the server to fetch and render attacker-controlled URLs — including internal network and cloud-metadata endpoints and local files via file:// — by setting an arbitrary URL as a product-store survey's template location, causing SurveyWrapper.getTemplate to call URL.openStream() on the resolved location and compile the fetched content as a FreeMarker template with no scheme or host validation, unlike the sibling widget location-loaders (ScreenFactory, FormFactory, GridFactory, MenuFactory, TreeFactory, ThemeFactory) which validate the resolved location before loading it. The fetched content is rendered into the HTTP response of any shopper who subsequently loads the affected product-store survey, making the disclosure non-blind. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* n0mi1k (reporter)
* Krishna Uprit (remediation developer)


## XML external entity injection (XXE) ## { #CVE-2026-81816 }

CVE-2026-81816 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-81816) [\[CVE json\]](./CVE-2026-81816.cve.json) [\[OSV json\]](./CVE-2026-81816.osv.json)



_Last updated: 2026-11-05T14:06:32.349Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

XML External Entity (XXE) Injection in ContentWorker in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated attacker holding content-author permission to read arbitrary server files and trigger server-side request forgery by storing a crafted text/xml DataResource containing an external entity declaration, causing ContentWorker's rendering of that content — via renderContentAsText and related CMS/help render paths — to parse the stored XML using FreeMarker's default NodeModel.parse DocumentBuilderFactory, which enables neither FEATURE_SECURE_PROCESSING nor external-entity/DTD restrictions, resolving the external entity and returning its content in the rendered response. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* n0mi1k (reporter)
* Krishna Uprit (remediation developer)


## SQL injection  - performFind ignore-case values, MySQL/MariaDB ## { #CVE-2026-81815 }

CVE-2026-81815 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-81815) [\[CVE json\]](./CVE-2026-81815.cve.json) [\[OSV json\]](./CVE-2026-81815.osv.json)



_Last updated: 2026-11-05T14:06:56.979Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

SQL Injection in the entity engine's generic performFind service in Apache OFBiz 24.09 before 24.09.08 on MySQL/MariaDB-backed deployments allows a remote unauthenticated attacker to disclose arbitrary rows from the queried entity by submitting an ignore-case find request (e.g. _ic=Y) with a crafted value, causing SqlJdbcUtil.addValueSingle to inline the EntityFunction-wrapped value directly into the SQL text using ANSI-only single-quote doubling instead of binding it as a parameter, which is insufficient on MySQL/MariaDB because those dialects also honor backslash escapes, letting a backslash-terminated payload break out of the string literal and turn the WHERE clause into a tautology. The default Derby datasource and PostgreSQL are not affected because they do not interpret backslash as an escape character in this context. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* n0mi1k (reporter)
* Krishna Uprit (remediation developer)


## Missing authorization - search-result bulk catalog mutation ## { #CVE-2026-81808 }

CVE-2026-81808 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-81808) [\[CVE json\]](./CVE-2026-81808.cve.json) [\[OSV json\]](./CVE-2026-81808.osv.json)



_Last updated: 2026-11-05T14:07:17.033Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Missing Authorization in ProductSearchEvents in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated attacker holding only catalog view permission to bulk-modify product category and feature associations across arbitrary search results by seeding a broad product search and then invoking search-result mutation events such as searchRemoveFromCategory, searchExpireFromCategory, searchAddToCategory, searchAddFeature, and searchRemoveFeature, causing the servlet to authorize the request against only the base view-level permission declared on the request-map while the underlying event methods perform bulk entity-engine deletes/inserts without checking the DELETE/CREATE permission enforced by the equivalent service-layer operations (e.g. removeProductFromCategory). Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* n0mi1k (reporter)
* Krishna Uprit (remediation developer)


## Authorization bypass - self-grant content OWNER ## { #CVE-2026-81744 }

CVE-2026-81744 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-81744) [\[CVE json\]](./CVE-2026-81744.cve.json) [\[OSV json\]](./CVE-2026-81744.osv.json)



_Last updated: 2026-11-05T14:07:48.296Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Incorrect Authorization in ContentPermissionServices in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated attacker holding only a limited content-create permission to self-grant the OWNER role on arbitrary content by invoking the createContentRole service (e.g. via the createForumGroupRole request), causing the permission check to fall through to a fail-open default-grant branch when no ContentPurposeOperation entry matches the requested operation and content purpose, rather than denying the request. A self-granted OWNER role then satisfies the ownership check used to authorize update, removal, and status changes on that content, giving the attacker full read/write/delete control over content they should not have access to. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* n0mi1k (reporter)
* Krishna Uprit (remediation developer)


## Missing authorization - catalog quick-admin product writes ## { #CVE-2026-81734 }

CVE-2026-81734 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-81734) [\[CVE json\]](./CVE-2026-81734.cve.json) [\[OSV json\]](./CVE-2026-81734.osv.json)



_Last updated: 2026-11-05T14:08:37.646Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Missing Authorization in ProductEvents in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote authenticated attacker holding only catalog view permission to create, modify, or remove arbitrary product, product feature association, and product category association data by directly invoking catalog quick-admin events such as updateProductQuickAdminShipping, causing the servlet to authorize the request against the base view-level permission declared on the request-map while the underlying event methods perform entity-engine writes without checking the catalog update/create permission enforced by equivalent sibling event methods in the same class. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* n0mi1k (reporter)
* Krishna Uprit (remediation developer)


## Authenticated path traversal and missing authorization check in imageCrop and imageRotate services ## { #CVE-2026-76152 }

CVE-2026-76152 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-76152) [\[CVE json\]](./CVE-2026-76152.cve.json) [\[OSV json\]](./CVE-2026-76152.osv.json)



_Last updated: 2026-11-05T14:08:11.509Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Path traversal and missing authorization check in the imageCrop and imageRotate services in Apache OFBiz through 24.09.07 on all platforms allows a remote authenticated attacker with only Catalog view permission to read arbitrary image-parseable files readable by the OFBiz process, disclosed via re-encoded and republished product content, and to write a re-encoded image to an arbitrary directory writable by the OFBiz process via crafted productId and imageName parameters. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* n0mi1k (reporter)


## Authenticated path traversal and missing authorization check in replaceImageToExistImage ## { #CVE-2026-76150 }

CVE-2026-76150 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-76150) [\[CVE json\]](./CVE-2026-76150.cve.json) [\[OSV json\]](./CVE-2026-76150.osv.json)



_Last updated: 2026-11-05T14:09:07.143Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Path traversal and missing authorization check in the replaceImageToExistImage service in Apache OFBiz through 24.09.07 on all platforms allows a remote authenticated attacker with only Catalog view permission to overwrite arbitrary files writable by the OFBiz process with JPEG-encoded content via crafted productId, dataResourceNameExist, and dataResourceNameReplace parameters. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Han, JunGyu (reporter)


## Denial of Service via unauthenticated userTenantId in multitenant mode ## { #CVE-2026-74841 }

CVE-2026-74841 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-74841) [\[CVE json\]](./CVE-2026-74841.cve.json) [\[OSV json\]](./CVE-2026-74841.osv.json)



_Last updated: 2026-11-05T14:09:38.314Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

In multitenant deployments, ContextFilter and LoginWorker built a per-tenant delegator name from a request-supplied userTenantId parameter and requested a delegator for it before confirming the tenant existed. DelegatorFactory's internal cache retains every delegator name it is asked to resolve, including ones that fail to resolve, so an unauthenticated attacker could submit a stream of arbitrary tenant IDs to grow this cache without bound, driving unnecessary memory and database load.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Pavel Kohout, Aisle Research (reporter)


## Unauthenticated HR organization and employee disclosure ## { #CVE-2026-73580 }

CVE-2026-73580 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73580) [\[CVE json\]](./CVE-2026-73580.cve.json) [\[OSV json\]](./CVE-2026-73580.osv.json)



_Last updated: 2026-11-05T14:10:07.922Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Missing authorization check in the getHRChild service in Apache OFBiz through 24.09.07 on all platforms allows a remote unauthenticated attacker to recursively enumerate Human Resources organization and employee data, including department names and identifiers, employment position names and identifiers, employee party identifiers, position occupancy, and organization relationships, via a crafted partyId parameter. Users are recommended to upgrade to version&nbsp;24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Omar Mousa — Red Team & Security Researcher (finder)
* Krishna Uprit (remediation developer)


## Unauthenticated saved-view authorization bypass with RCE impact ## { #CVE-2026-73578 }

CVE-2026-73578 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73578) [\[CVE json\]](./CVE-2026-73578.cve.json) [\[OSV json\]](./CVE-2026-73578.osv.json)



_Last updated: 2026-11-05T14:10:35.040Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Missing authorization enforcement in RequestHandler.renderView in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote unauthenticated attacker to bypass the request-map authentication policy for protected views by supplying a crafted _LAST_VIEW_NAME_ value, which is stored as saved-view state in the anonymous session and later rendered without re-applying the original view's authentication requirement, potentially exposing protected views and associated business data. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Jonah Burgess (CryptoCat) (finder)
* Krishna Uprit (remediation developer)


## Unauthenticated path-suffix view authorization bypass ## { #CVE-2026-73577 }

CVE-2026-73577 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-73577) [\[CVE json\]](./CVE-2026-73577.cve.json) [\[OSV json\]](./CVE-2026-73577.osv.json)



_Last updated: 2026-11-05T14:11:03.359Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Incorrect authorization in RequestHandler in Apache OFBiz 24.09 before 24.09.08 on all platforms allows a remote unauthenticated attacker to bypass the authentication requirement of a protected view by appending it as a path suffix to a public request (e.g., /catalog/control/ListLocales/showPortalPage), causing the servlet to authorize the request based on the public path component while rendering the protected suffix view. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Jonah Burgess (CryptoCat) (reporter)
* Krishna Uprit (remediation developer)


## Dispatch arbitrary internal services on SFA component ## { #CVE-2026-71901 }

CVE-2026-71901 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-71901) [\[CVE json\]](./CVE-2026-71901.cve.json) [\[OSV json\]](./CVE-2026-71901.osv.json)



_Last updated: 2026-11-05T14:11:58.106Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

<p>Improper Control of Resource Identifiers ('Resource Injection') vulnerability in Apache OFBiz.</p><p>An authenticate user with access to sfa component can override the service to use on vcard import and access to other service.</p><p>This issue affects Apache OFBiz: before 24.09.08.</p><p>Users are recommended to upgrade to version 24.09.08, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Charles Vosburgh <trilobyte777@gmail.com> (reporter)
* Bartlomiej Dmitruk at striga.ai (reporter)


## Pre-Authentication Remote Code Execution via Attacker-Controlled Screen Definition Loading ## { #CVE-2026-68524 }

CVE-2026-68524 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-68524) [\[CVE json\]](./CVE-2026-68524.cve.json) [\[OSV json\]](./CVE-2026-68524.osv.json)



_Last updated: 2026-11-05T14:11:31.898Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

<p>An unauthenticated attacker can exploit temporary-file handling, access an open file descriptor, and inject a "file:" URI to cause OFBiz to load an attacker-controlled Screen definition.</p><p>This issue affects Apache OFBiz: before 24.09.08.</p><p>Users are recommended to upgrade to version 24.09.08, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Naoya Takahashi (nakko) (reporter)


## Authenticated Path Traversal in Catalog Image Management ## { #CVE-2026-66903 }

CVE-2026-66903 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66903) [\[CVE json\]](./CVE-2026-66903.cve.json) [\[OSV json\]](./CVE-2026-66903.osv.json)



_Last updated: 2026-11-05T14:12:27.124Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

<p>Authenticated Path Traversal in Catalog Image Management allows writing image files outside the intended directory&nbsp;in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.08.</p><p>Users are recommended to upgrade to version 24.09.08, which fixes the issue.</p>

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Adrián Leal / 4lec4st (reporter)


## DataResource Low-Privileged Authenticated FreeMarker Template Injection Leads to Remote Code Execution ## { #CVE-2026-50223 }

CVE-2026-50223 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-50223) [\[CVE json\]](./CVE-2026-50223.cve.json) [\[OSV json\]](./CVE-2026-50223.osv.json)



_Last updated: 2026-06-10T22:23:48.015Z_

### Affected

* Apache OFBiz before 24.09.07


### Description

<p>Improper Control of Generation of Code ('Code Injection') vulnerability in Apache OFBiz allows a low-privileged authenticated user with Content/DataResource editing privileges to perform template injection attacks that could lead to Remote Code Execution.</p><p>This issue affects Apache OFBiz: before 24.09.07.</p><p>Users are recommended to upgrade to version 24.09.07, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/trr2p4zokg54glqlhjnglt4yr7n8t5xd


### Credits
* yi (reporter)
* Jongyeon Lee (reporter)


## Privilege Escalation via updateOrRemove Authorization Bypass ## { #CVE-2026-47342 }

CVE-2026-47342 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-47342) [\[CVE json\]](./CVE-2026-47342.cve.json) [\[OSV json\]](./CVE-2026-47342.osv.json)



_Last updated: 2026-06-10T22:29:05.548Z_

### Affected

* Apache OFBiz before 24.09.07


### Description

<p></p><p>A privilege escalation vulnerability in Apache OFBiz allows a low-privileged authenticated user to obtain higher privileges</p><p></p><p>This issue affects Apache OFBiz: before 24.09.07.</p><p>Users are recommended to upgrade to version 24.09.07, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/xqph4qjm163kmp0tcg9dodl6js499n75


### Credits
* Le Huynh Duc (lwd3c) (finder)


## Improper Validation in traverseContent Service Enables Authenticated Groovy Code Execution ## { #CVE-2026-46586 }

CVE-2026-46586 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-46586) [\[CVE json\]](./CVE-2026-46586.cve.json) [\[OSV json\]](./CVE-2026-46586.osv.json)



_Last updated: 2026-05-19T09:41:46.590Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Control of Generation of Code ('Code Injection'), Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/7mgjl81nrpxqtfcg6h5qtrx7wztbl4js


### Credits
* lwd3c (finder)


## Authentication Bypass via Password-Change Logic Flaw Leading to RCE ## { #CVE-2026-45434 }

CVE-2026-45434 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45434) [\[CVE json\]](./CVE-2026-45434.cve.json) [\[OSV json\]](./CVE-2026-45434.osv.json)



_Last updated: 2026-05-19T09:40:31.930Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Authentication vulnerability in Apache OFBiz via Password-Change Logic Flaw Leading to Remote Code Execution</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/yw4owrzl0yho1yx7oqxvr6xjkmln9tq8


### Credits
* Mike Cole (reporter)


## Improper Authorization in Scheduled Job Creation Allows Low-Privileged Users to Submit System Jobs ## { #CVE-2026-45187 }

CVE-2026-45187 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45187) [\[CVE json\]](./CVE-2026-45187.cve.json) [\[OSV json\]](./CVE-2026-45187.osv.json)



_Last updated: 2026-05-19T09:39:30.906Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Authorization vulnerability in Apache OFBiz Webtools.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/pcmfyxjyk7dg0btxqg9h7cr30yg8mr7k


### Credits
* Qiulin Deng (reporter)


## Authentication Bypass due to Improper Neutralization of LDAP Special Elements in DN Construction ## { #CVE-2026-41919 }

CVE-2026-41919 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-41919) [\[CVE json\]](./CVE-2026-41919.cve.json) [\[OSV json\]](./CVE-2026-41919.osv.json)



_Last updated: 2026-05-19T09:37:00.903Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/592czh9o69n74c036vy30fnqknocw74p


### Credits
* zhaokaifei (China Telecom) (reporter)


## Authenticated Remote Code Execution via Unsafe Template Expansion in email services ## { #CVE-2026-35086 }

CVE-2026-35086 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-35086) [\[CVE json\]](./CVE-2026-35086.cve.json) [\[OSV json\]](./CVE-2026-35086.osv.json)



_Last updated: 2026-05-19T09:36:05.258Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Control of Generation of Code ('Code Injection') vulnerability in email services of Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/g0s37yhnh2xwfts400crb2w8s337hgjx


### Credits
* Hyunwoo Kim (@v4bel) (reporter)


## Unauthenticated RCE via Default JWT Signing Key and Widget Template Injection ## { #CVE-2026-31986 }

CVE-2026-31986 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31986) [\[CVE json\]](./CVE-2026-31986.cve.json) [\[OSV json\]](./CVE-2026-31986.osv.json)



_Last updated: 2026-05-19T09:34:42.293Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Use of Hard-coded Cryptographic Key vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/2hl9xoqm8tq8b22x6vnmtp7tg3opcqgc


### Credits
* Lidor B / thisis0xczar of Novee Security (reporter)


## Improper Input Validation in UI Factory Classes Leads to SSRF and Blind File Access ## { #CVE-2026-31910 }

CVE-2026-31910 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31910) [\[CVE json\]](./CVE-2026-31910.cve.json) [\[OSV json\]](./CVE-2026-31910.osv.json)



_Last updated: 2026-05-19T09:33:43.399Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Server-Side Request Forgery (SSRF) vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/2smc4c4o056ovd2hoq1l29593y5y29vh


### Credits
* Voyag3r-Security (reporter)


## Unauthenticated Shipment Label Image Disclosure ## { #CVE-2026-31909 }

CVE-2026-31909 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31909) [\[CVE json\]](./CVE-2026-31909.cve.json) [\[OSV json\]](./CVE-2026-31909.osv.json)



_Last updated: 2026-05-19T09:32:51.623Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/0hpopzz1qrhkzsbt3ncofs6qo0545r2h


### Credits
* Dohyun Yun (H4uN) (reporter)


## Reflected XSS via Improper HTML Attribute Escaping in Layered-Modal Dialog Parameters ## { #CVE-2026-31906 }

CVE-2026-31906 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31906) [\[CVE json\]](./CVE-2026-31906.cve.json) [\[OSV json\]](./CVE-2026-31906.osv.json)



_Last updated: 2026-05-19T09:30:23.994Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/1fblqdo89d3ps8kgtcnkcq8sh7gwkcpn


### Credits
* Sho Odagiri of GMO Cybersecurity by Ierae, Inc. (reporter)


## Cross-Tenant Data Exposure via Program Export Feature ## { #CVE-2026-31388 }

CVE-2026-31388 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31388) [\[CVE json\]](./CVE-2026-31388.cve.json) [\[OSV json\]](./CVE-2026-31388.osv.json)



_Last updated: 2026-05-19T09:28:35.638Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Access Control vulnerability in Apache OFBiz in multi-tenant deployments.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/npjchvnpnosoqpto46s2om12jd9s7py7


### Credits
* Krishna Uprit (reporter)


## Cookie Manipulation Allows Authenticated JWT Forgery and Account Impersonation ## { #CVE-2026-31387 }

CVE-2026-31387 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31387) [\[CVE json\]](./CVE-2026-31387.cve.json) [\[OSV json\]](./CVE-2026-31387.osv.json)



_Last updated: 2026-05-19T09:27:10.241Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Authentication vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/3wgybgdvmbfvly24zm4sb4y53fc1pqcf


### Credits
* Sho Odagiri of GMO Cybersecurity by Ierae, Inc. (reporter)


## FreeMarker SSTI via Duplicate Parameter Sanitization Bypass ## { #CVE-2026-31380 }

CVE-2026-31380 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31380) [\[CVE json\]](./CVE-2026-31380.cve.json) [\[OSV json\]](./CVE-2026-31380.osv.json)



_Last updated: 2026-05-19T09:24:43.138Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Neutralization of Special Elements used in an Expression Language Statement ('Expression Language Injection') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/v2brvq1tf4q491obkxv8p7fc5qfshc08


### Credits
* Sho Odagiri of GMO Cybersecurity by Ierae, Inc. (reporter)


## Path Traversal and File Upload Validation Bypass Leading to Arbitrary File Write, Stored XSS and RCE in Catalog Manager ## { #CVE-2026-31379 }

CVE-2026-31379 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31379) [\[CVE json\]](./CVE-2026-31379.cve.json) [\[OSV json\]](./CVE-2026-31379.osv.json)



_Last updated: 2026-05-19T09:22:53.895Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'), Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'), Improper Control of Generation of Code ('Code Injection') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/1tcnkxjm0s6n1ohfb21brl25dt0hv9by


### Credits
* Sho Odagiri of GMO Cybersecurity by Ierae, Inc. (reporter)
* Emily Bishop of 992labs (reporter)


## JSON Attribute Override and URL Allowlist Bypass Leads to Remote Code Execution ## { #CVE-2026-31378 }

CVE-2026-31378 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-31378) [\[CVE json\]](./CVE-2026-31378.cve.json) [\[OSV json\]](./CVE-2026-31378.osv.json)



_Last updated: 2026-05-19T09:21:23.935Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Input Validation vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/cbl8qkqtxv90m6ssfwd58bnoh933v38t


### Credits
* Sho Odagiri of GMO Cybersecurity by Ierae, Inc. (reporter)


## Low-Privilege SSRF in Content Component ## { #CVE-2026-29226 }

CVE-2026-29226 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-29226) [\[CVE json\]](./CVE-2026-29226.cve.json) [\[OSV json\]](./CVE-2026-29226.osv.json)



_Last updated: 2026-05-19T09:19:35.072Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Server-Side Request Forgery (SSRF) vulnerability in Apache OFBiz via Content component operations.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/6707wys8jxzmowxggn4cmtwwk9ygl2tr


### Credits
* Lidor B / thisis0xczar of Novee Security (reporter)
* Sho Odagiri of GMO Cybersecurity by Ierae, Inc. (reporter)
* duanjinshi@163.com (reporter)


## Low-Privilege LFI in Content Component ## { #CVE-2026-29220 }

CVE-2026-29220 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-29220) [\[CVE json\]](./CVE-2026-29220.cve.json) [\[OSV json\]](./CVE-2026-29220.osv.json)



_Last updated: 2026-05-19T09:17:05.818Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

<p>Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.06.</p><p>Users are recommended to upgrade to version 24.09.06, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/5hjnmt9no6mmtg8sxq3mhonzff1vkd5m


### Credits
* Lidor B / thisis0xczar of Novee Security (reporter)
* Venkatraman Kumar, Securin (reporter)


## Low-Privilege SSTI Leading to RCE in the Content Component ## { #CVE-2026-29207 }

CVE-2026-29207 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-29207) [\[CVE json\]](./CVE-2026-29207.cve.json) [\[OSV json\]](./CVE-2026-29207.osv.json)



_Last updated: 2026-05-19T09:18:23.188Z_

### Affected

* Apache OFBiz before 24.09.06


### Description

Improper Neutralization of Special Elements Used in a Template Engine vulnerability in Apache OFBiz.<br><br>This issue affects Apache OFBiz: before 24.09.06.<br><br>Users are recommended to upgrade to version 24.09.06, which fixes the issue.<br><br>Please note that in the updated version, "Data Resource" records with <code>dataTemplateTypeId = "FTL"</code> are no longer supported.<br>
Additionally, in the updated version, the "Ecommerce Customer" security group no longer includes content management grants. Users are advised to remove these permissions from any production site as well.<code></code><code></code><br><p><code></code></p>

### References
* https://lists.apache.org/thread/3rcrp8bh3x6ovrj5xnc0fm1f0nrn52r0


### Credits
* Lidor B / thisis0xczar of Novee Security (reporter)
* Sho Odagiri of GMO Cybersecurity by Ierae, Inc. (reporter)


## Janrain Engage Social Login Improperly Binds External Identities to Local Accounts ## { #CVE-2026-114277 }

CVE-2026-114277 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-114277) [\[CVE json\]](./CVE-2026-114277.cve.json) [\[OSV json\]](./CVE-2026-114277.osv.json)



_Last updated: 2026-11-05T13:33:34.588Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

<p>Authentication bypass by Assumed-Immutable data vulnerability in Apache OFBiz.<br><span>Apache OFBiz's optional Janrain Engage Social Login integration in the ecommerce component improperly binds authenticated external identities to local user accounts.<br></span><span>This issue affects Apache OFBiz: before 24.09.08.<br></span><span>Users are recommended to upgrade to version 24.09.08, which fixes the issue.</span></p>

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* MUTED CYBERSECURITY (reporter)


## Authorization Bypass Through User-Controlled Key in Content Viewing Enables Unauthorized Content Disclosure ## { #CVE-2026-114272 }

CVE-2026-114272 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-114272) [\[CVE json\]](./CVE-2026-114272.cve.json) [\[OSV json\]](./CVE-2026-114272.osv.json)



_Last updated: 2026-11-05T13:34:01.391Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Authorization Bypass Through User-Controlled Key in the content viewing component in Apache OFBiz 24.09 before 24.09.08 on all platforms allows an authenticated user with role-scoped content view permission to read the data of content they are not authorized to view via a ViewSimpleContent request that combines a contentId they can view with the dataResourceId of other content.<br>Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Mathias Conradt (Sonar) (reporter)


## Authorization Bypass Through User-Controlled Key in Shopping Lists Enables Cross-Party Shopping List Modification ## { #CVE-2026-114271 }

CVE-2026-114271 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-114271) [\[CVE json\]](./CVE-2026-114271.cve.json) [\[OSV json\]](./CVE-2026-114271.osv.json)



_Last updated: 2026-11-05T13:34:25.209Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Authorization Bypass Through User-Controlled Key in the shopping list services in Apache OFBiz 24.09 before 24.09.08 on all platforms allows an authenticated low-privileged user, such as a self-registered ecommerce customer, to modify another party's shopping list or take ownership of it, and thereby read its contents, via a request to the shopping list update endpoint that supplies the other party's shopping list ID.<br><br>Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Mathias Conradt (Sonar) (reporter)


## Direct Request in Order Manager Enables Unauthorized Tracking Number Modification ## { #CVE-2026-114235 }

CVE-2026-114235 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-114235) [\[CVE json\]](./CVE-2026-114235.cve.json) [\[OSV json\]](./CVE-2026-114235.osv.json)



_Last updated: 2026-11-05T13:35:11.048Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

<div><span>Direct Request ('Forced Browsing') in the Order component in Apache OFBiz&nbsp;</span>24.09 before 24.09.08<span>&nbsp;on all platforms allows an authenticated user with only view access to the Order Manager to modify the shipment tracking number of any order via a direct request to the updateTrackingNumber endpoint. Users are recommended to upgrade to version&nbsp;</span>24.09.08<span>, which fixes this issue.</span></div>

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* noah (VNCS) (reporter)


## Incorrect Privilege Assignment in Order Manager Enables Unauthorized Modification of Approved Orders ## { #CVE-2026-114233 }

CVE-2026-114233 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-114233) [\[CVE json\]](./CVE-2026-114233.cve.json) [\[OSV json\]](./CVE-2026-114233.osv.json)



_Last updated: 2026-11-05T13:35:44.216Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Incorrect Privilege Assignment in the Order Manager in Apache OFBiz&nbsp;24.09 before 24.09.08&nbsp;on all platforms allows an authenticated user who holds only order view permissions (ORDERMGR_VIEW), without ORDERMGR_UPDATE or any role on the order, to modify approved orders, changing a ship group's shipping address and shipment method or appending items with an overridden price, via the updateShipGroupShipInfo and appendOrderItem services. Users are recommended to upgrade to version&nbsp;24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Javier García Herrera of Muted Cybersecurity (reporter)


## Reflected Cross-site Scripting in Catalog Image Viewer Enables Script Execution in a User Session ## { #CVE-2026-114229 }

CVE-2026-114229 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-114229) [\[CVE json\]](./CVE-2026-114229.cve.json) [\[OSV json\]](./CVE-2026-114229.osv.json)



_Last updated: 2026-11-05T13:36:12.099Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') in the Catalog image viewer in Apache OFBiz 24.09 before 24.09.08 on all platforms allows an unauthenticated attacker to execute arbitrary JavaScript in the browser session of a logged-in back-office user via a crafted viewImage URL that the user opens from within the application.<br>Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* NGUYỄN DUY THẢO | https://github.com/duythao2004 (reporter)


## Incorrect Authentication Algorithm Implementation in Password Reset Enables Full Account Takeover ## { #CVE-2026-109928 }

CVE-2026-109928 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-109928) [\[CVE json\]](./CVE-2026-109928.cve.json) [\[OSV json\]](./CVE-2026-109928.osv.json)



_Last updated: 2026-11-05T13:36:49.154Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Incorrect Implementation of Authentication Algorithm in the password-reset and login JWT validation in Apache OFBiz 24.09 before 24.09.08 on all platforms allows an attacker who has obtained a user's password-reset token (via email interception, log exposure, or a man-in-the-middle on the mail transport) to authenticate as that user and obtain a full, unrestricted session, including administrative access if the targeted account is an administrator, by submitting the token directly to the login endpoint instead of the intended password-change flow. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* CyberLeo (Independent Security Researcher) (reporter)


## Missing Authorization in Financial Account Services Enables Unauthorized Balance Manipulation ## { #CVE-2026-109856 }

CVE-2026-109856 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-109856) [\[CVE json\]](./CVE-2026-109856.cve.json) [\[OSV json\]](./CVE-2026-109856.osv.json)



_Last updated: 2026-11-05T13:37:31.894Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Direct Request ('Forced Browsing') to Financial Account services in Apache OFBiz 24.09 before 24.09.08 on all platforms allows an authenticated user with any valid low-privilege account to create, modify, and cancel financial account transactions and balances without appropriate permission via direct requests to the createFinAccount, updateFinAccount, deleteFinAccount, createFinAccountTrans, createFinAccountRole, createFinAccountAuth, setFinAccountTransStatus, and depositWithdrawPayments services.<br><br>Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Ho1aAs <xxy010605@gmail.com> (reporter)
* Mathias Conradt | Sonar (reporter)


## Authorization Bypass Through User-Controlled Key in Order Returns Enables Cross-Party OrderItem Association ## { #CVE-2026-109837 }

CVE-2026-109837 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-109837) [\[CVE json\]](./CVE-2026-109837.cve.json) [\[OSV json\]](./CVE-2026-109837.osv.json)



_Last updated: 2026-11-05T13:38:00.607Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Authorization Bypass Through User-Controlled Key in Order Returns in Apache OFBiz&nbsp;24.09 before 24.09.08&nbsp;on all platforms allows an authenticated user with low-privileged Order Manager access to associate another party's OrderItem with a ReturnItem on a ReturnHeader they control, via the createReturnItem service. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Omar Mousa — Red Team & Security Researcher, LinkedIn: https://www.linkedin.com/in/omar-mousa15 (reporter)


## Authorization Bypass Through User-Controlled Key in OrderServices Enables Unauthorized Payment Preference Modification ## { #CVE-2026-109129 }

CVE-2026-109129 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-109129) [\[CVE json\]](./CVE-2026-109129.cve.json) [\[OSV json\]](./CVE-2026-109129.osv.json)



_Last updated: 2026-11-05T13:38:51.199Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Authorization Bypass Through User-Controlled Key in the Order Manager component in Apache OFBiz 24.09.07 on all platforms allows an authenticated user with only view-level order permissions to modify or create OrderPaymentPreference records belonging to orders outside their authorized scope via the updateOrderPaymentPreference service, by supplying an orderPaymentPreferenceId belonging to a different order.<br>Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Omar Mousa — Red Team & Security Researcher, LinkedIn: https://www.linkedin.com/in/omar-mousa15 (reporter)


## Missing authorization in updateOrderItems allows view-only users to modify order prices and quantities ## { #CVE-2026-105461 }

CVE-2026-105461 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-105461) [\[CVE json\]](./CVE-2026-105461.cve.json) [\[OSV json\]](./CVE-2026-105461.osv.json)



_Last updated: 2026-11-05T13:39:36.383Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

<div>Missing check for&nbsp;&nbsp;<u>ORDERMGR_UPDATE&nbsp;</u>in ordermgr allows user with only ORDERMGR_VIEW permission to update orders.</div><div>Affected versions before : 24.09.08</div>Users are recommended to upgrade to version 24.09.08 which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Ivan "Steph" Iushkevich (finder)


## Use of Hard-coded Cryptographic Key in JWT Token Authentication Enables Unauthenticated Administrative Access ## { #CVE-2026-105330 }

CVE-2026-105330 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-105330) [\[CVE json\]](./CVE-2026-105330.cve.json) [\[OSV json\]](./CVE-2026-105330.osv.json)



_Last updated: 2026-11-05T13:40:01.630Z_

### Affected

* Apache OFBiz from 24.09.06 before 24.09.08


### Description

Use of Hard-coded Cryptographic Key in JWT token authentication in Apache OFBiz 24.09.06 and 24.09.07 on all platforms allows an unauthenticated, network-reachable attacker to obtain full administrative access via a forged JWT signed with the factory-default security.token.key value that CVE-2026-31986 removed from newly generated configurations, on a deployment that upgraded from a release predating that fix while retaining its existing security.properties with security.internal.sso.enabled set to true. Users are recommended to upgrade to version 24.09.08. Upgrading alone does not replace an already-configured key: deployments that carried framework/security/config/security.properties forward from a release predating the CVE-2026-31986 fix must also run './gradlew rotateSecretKeys' after upgrading, since the existing generateSecretKeys task leaves an already-set value untouched.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* L1nq (https://github.com/L1nq0) (reporter)


## Missing authorization in payment application services allows view-only users to modify payment allocations ## { #CVE-2026-105325 }

CVE-2026-105325 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-105325) [\[CVE json\]](./CVE-2026-105325.cve.json) [\[OSV json\]](./CVE-2026-105325.osv.json)



_Last updated: 2026-11-05T13:40:31.985Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

<div>Missing check for&nbsp;&nbsp;<u>ACCOUNTING_UPDATE /&nbsp;</u> <u>ACCOUNTING_CREATE</u>&nbsp;in accounting in allows user with only ACCOUNTING_VIEW permission to update/create PaymentApplication.</div><div>Affected versions before : 24.09.08</div>Users are recommended to upgrade to version 24.09.08 which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Ivan "Steph" Iushkevich (reporter)


## Improper Input Validation in Order Returns Enables Unauthorized Refund Price Manipulation ## { #CVE-2026-100228 }

CVE-2026-100228 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-100228) [\[CVE json\]](./CVE-2026-100228.cve.json) [\[OSV json\]](./CVE-2026-100228.osv.json)



_Last updated: 2026-11-05T13:43:35.655Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Improper Input Validation in Order Returns in Apache OFBiz 24.09.07 on all platforms allows an authenticated user without the ORDERMGR_CREATE permission to persist an arbitrary price on a return item via the createReturnItem service, bypassing the intended server-computed price ceiling. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Sakil Ahamed (reporter)


## Missing Authorization vulnerability ## { #CVE-2026-100168 }

CVE-2026-100168 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-100168) [\[CVE json\]](./CVE-2026-100168.cve.json) [\[OSV json\]](./CVE-2026-100168.osv.json)



_Last updated: 2026-11-05T13:44:03.331Z_

### Affected

* Apache OFBiz before 24.09.08


### Description

Direct Request ('Forced Browsing') in the Content Manager component in Apache OFBiz 24.09.07 on all platforms allows an authenticated user holding only view-only content permissions (OFBTOOLS_VIEW and CONTENTMGR_VIEW) to re-parent content associations they do not own or manage via a direct POST request to the moveContentJson endpoint, which performs no permission check, unlike the equivalent updateContent/createContentAssoc/removeContentAssoc services that require genericContentPermission UPDATE. Users are recommended to upgrade to version 24.09.08, which fixes this issue.

### References
* https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz


### Credits
* Ivan "Steph" Iushkevich (reporter)


## Reflected Cross-site Scripting ## { #CVE-2025-61623 }

CVE-2025-61623 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-61623) [\[CVE json\]](./CVE-2025-61623.cve.json) [\[OSV json\]](./CVE-2025-61623.osv.json)



_Last updated: 2025-11-12T09:16:48.899Z_

### Affected

* Apache OFBiz before 24.09.03


### Description

<p>Reflected cross-site scripting vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.03.</p><p>Users are recommended to upgrade to version 24.09.03, which fixes the issue.</p>

### References
* https://issues.apache.org/jira/browse/OFBIZ-13295
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-24.09.03.html
* https://lists.apache.org/thread/sb2mngrg766qbqt5g29fo0qblk3v4x5y


### Credits
* RedHive Team (security@hive.red) https://hive.red/en/ (finder)


## Critical Remote Command Execution via Unrestricted File Upload ## { #CVE-2025-59118 }

CVE-2025-59118 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-59118) [\[CVE json\]](./CVE-2025-59118.cve.json) [\[OSV json\]](./CVE-2025-59118.osv.json)



_Last updated: 2025-11-12T09:15:52.459Z_

### Affected

* Apache OFBiz before 24.09.03


### Description

<p>Unrestricted Upload of File with Dangerous Type vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 24.09.03.</p><p>Users are recommended to upgrade to version 24.09.03, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-24.09.03.html
* https://issues.apache.org/jira/browse/OFBIZ-13292
* https://lists.apache.org/thread/202263kpy7g76pzsy1fm96h9lcmhsqpt


### Credits
* RedHive Team (security@hive.red) https://hive.red/en/ (finder)


## RCE Vulnerability in scrum plugin ## { #CVE-2025-54466 }

CVE-2025-54466 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-54466) [\[CVE json\]](./CVE-2025-54466.cve.json) [\[OSV json\]](./CVE-2025-54466.osv.json)



_Last updated: 2025-08-15T14:13:40.046Z_

### Affected

* Apache OFBiz before 24.09.02


### Description

<p>Improper Control of Generation of Code ('Code Injection') vulnerability leading to a possible RCE in Apache OFBiz&nbsp;scrum plugin.<br><br>This issue affects Apache OFBiz: before 24.09.02 only when the&nbsp;scrum plugin is used.</p><p>Even unauthenticated attackers can exploit this vulnerability.<br></p><p>Users are recommended to upgrade to version 24.09.02, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-24.09.02.html
* https://issues.apache.org/jira/browse/OFBIZ-13276
* https://lists.apache.org/thread/14d0yd9co9gx2mctd3vyz1cc8d39n915


### Credits
* Teeramet Eakwilai <teeramet@datafarm.co.th> (finder)
* Thanasin Luangpipat (finder)
* Jarukit Auikritskul (finder)


## Stored XSS Vulnerability ## { #CVE-2025-30676 }

CVE-2025-30676 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-30676) [\[CVE json\]](./CVE-2025-30676.cve.json) [\[OSV json\]](./CVE-2025-30676.osv.json)



_Last updated: 2025-04-01T14:43:47.266Z_

### Affected

* Apache OFBiz before 18.12.19


### Description

<p>Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 18.12.19.</p><p>Users are recommended to upgrade to version 18.12.19, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13219
* https://lists.apache.org/thread/8d718qt8dqthnw1gmyxsq8glfdjklnjf


### Credits
* Khaled Nassar  (@mindpatch) (finder)


## Server-Side Template Injection affecting the ecommerce plugin leading to possible RCE ## { #CVE-2025-26865 }

CVE-2025-26865 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2025-26865) [\[CVE json\]](./CVE-2025-26865.cve.json) [\[OSV json\]](./CVE-2025-26865.osv.json)



_Last updated: 2025-03-10T14:00:48.257Z_

### Affected

* Apache OFBiz from 18.12.17 before 18.12.18


### Description

<p>Improper Neutralization of Special Elements Used in a Template Engine vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: from 18.12.17 before 18.12.18.&nbsp;&nbsp;</p>It's a regression between 18.12.17 and 18.12.18.<br>In case you use something like that, which is not recommended!<br>For security, only official releases should be used.<br><br>In other words, if you use 18.12.17 you are still safe.<br>The version 18.12.17 is not a affected.<br>But something between 18.12.17 and 18.12.18 is.<br><br>In that case, users are recommended to upgrade to version 18.12.18, which fixes the issue.<br>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-12594
* https://lists.apache.org/thread/prb48ztk01bflyyjbl6p56wlcc1n5sz7


### Credits
* Matei "Mal" Badanoiu (finder)


## Bypass SameSite restrictions with target redirection using URL parameters (SSTI and CSRF leading to RCE) ## { #CVE-2024-48962 }

CVE-2024-48962 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-48962) [\[CVE json\]](./CVE-2024-48962.cve.json) [\[OSV json\]](./CVE-2024-48962.osv.json)



_Last updated: 2026-05-04T14:55:18.092Z_

### Affected

* Apache OFBiz before 18.12.17


### Description

<p>Improper Control of Generation of Code ('Code Injection'), Cross-Site Request Forgery (CSRF), : Improper Neutralization of Special Elements Used in a Template Engine vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 18.12.17.</p><p>Users are recommended to upgrade to version 18.12.17, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13162
* https://lists.apache.org/thread/6sddh4pts90cp8ktshqb4xykdp6lb6q6


### Credits
* Sebastiano Sartor <s@sebsrt.xyz> (finder)
* Ryan Chan <https://www.linkedin.com/in/ryanchan07/> (finder)


## URLs allowing remote use of Groovy expressions, leading to RCE ## { #CVE-2024-47208 }

CVE-2024-47208 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-47208) [\[CVE json\]](./CVE-2024-47208.cve.json) [\[OSV json\]](./CVE-2024-47208.osv.json)



_Last updated: 2024-11-18T08:43:11.961Z_

### Affected

* Apache OFBiz before 18.12.17


### Description

<p>Server-Side Request Forgery (SSRF), Improper Control of Generation of Code ('Code Injection') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 18.12.17.</p><p>Users are recommended to upgrade to version 18.12.17, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13158
* https://lists.apache.org/thread/022r19skfofhv3lzql33vowlrvqndh11


### Credits
* 孙相 (Sun Xiang) (finder)


## Prevent use of URLs in files when loading them from Java or Groovy, leading to a RCE ## { #CVE-2024-45507 }

CVE-2024-45507 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45507) [\[CVE json\]](./CVE-2024-45507.cve.json) [\[OSV json\]](./CVE-2024-45507.osv.json)



_Last updated: 2024-09-04T08:08:31.094Z_

### Affected

* Apache OFBiz before 18.12.16


### Description

<p>Server-Side Request Forgery (SSRF), Improper Control of Generation of Code ('Code Injection') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 18.12.16.</p><p>Users are recommended to upgrade to version 18.12.16, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13132
* https://lists.apache.org/thread/o90dd9lbk1hh3t2557t2y2qvrh92p7wy


### Credits
* 孙相 (Sun Xiang) (finder)


## Confused controller-view authorization logic (forced browsing) ## { #CVE-2024-45195 }

CVE-2024-45195 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-45195) [\[CVE json\]](./CVE-2024-45195.cve.json) [\[OSV json\]](./CVE-2024-45195.osv.json)



_Last updated: 2024-09-04T08:08:57.418Z_

### Affected

* Apache OFBiz before 18.12.16


### Description

<p>Direct Request ('Forced Browsing') vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: before 18.12.16.</p><p>Users are recommended to upgrade to version 18.12.16, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13130
* https://lists.apache.org/thread/o90dd9lbk1hh3t2557t2y2qvrh92p7wy


### Credits
* shin24 from National Cyber Security Vietnam (finder)
* LuanPV from National Cyber Security Vietnam (finder)
* Ryan Emmons, Lead Security Researcher at Rapid7 (finder)
* Hasib Vhora, Senior Threat Researcher, SonicWall (finder)
* Xenc from SGLAB of Legendsec at Qi'anxin Group (finder)


## Unauthenticated endpoint could allow execution of screen rendering code ## { #CVE-2024-38856 }

CVE-2024-38856 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-38856) [\[CVE json\]](./CVE-2024-38856.cve.json) [\[OSV json\]](./CVE-2024-38856.osv.json)



_Last updated: 2024-08-05T08:20:16.193Z_

### Affected

* Apache OFBiz through 18.12.14


### Description

<p>Incorrect Authorization vulnerability in Apache OFBiz.</p><p>This issue affects Apache OFBiz: through 18.12.14.</p><p>Users are recommended to upgrade to version 18.12.15, which fixes the issue.</p>Unauthenticated endpoints could allow execution of screen rendering code of screens if some preconditions are met (such as when the screen definitions don't explicitly check user's permissions because they rely on the configuration of their endpoints).<br>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://lists.apache.org/thread/olxxjk6b13sl3wh9cmp0k2dscvp24l7w
* https://issues.apache.org/jira/browse/OFBIZ-13128


### Credits
* unam4 (finder)
* ruozhi (finder)
* m1sn0w (finder)
* kuiplatain (finder)
* PaperPen@Timeline Sec (finder)
* RacerZ (finder)
* e0mlja (finder)
* Donghyun (finder)
* 4ra1n (finder)
* godspeed (finder)
* Hasib Vhora (finder)
* pwnull (finder)
* blckder02-YHLab (finder)
* Xenc from SGLAB of Legendsec at Qi'anxin Group (finder)
* Nicholas Zubrisky. (finder)
* Y4tacker  (finder)


## Path traversal leading to a RCE ## { #CVE-2024-36104 }

CVE-2024-36104 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-36104) [\[CVE json\]](./CVE-2024-36104.cve.json) [\[OSV json\]](./CVE-2024-36104.osv.json)



_Last updated: 2024-06-03T06:55:24.928Z_

### Affected

* Apache OFBiz before 18.12.14


### Description

Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache OFBiz.&nbsp;<p>This issue affects Apache OFBiz: before 18.12.14.</p><p>Users are recommended to upgrade to version 18.12.14, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13092
* https://lists.apache.org/thread/sv0xr8b1j7mmh5p37yldy9vmnzbodz2o


### Credits
* godspeed (AAA@ZJU) (finder)


## Path traversal leading to RCE ## { #CVE-2024-32113 }

CVE-2024-32113 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-32113) [\[CVE json\]](./CVE-2024-32113.cve.json) [\[OSV json\]](./CVE-2024-32113.osv.json)



_Last updated: 2024-05-08T14:49:53.237Z_

### Affected

* Apache OFBiz before 18.12.13


### Description

Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache OFBiz.<p>This issue affects Apache OFBiz: before 18.12.13.</p><p>Users are recommended to upgrade to version 18.12.13, which fixes the issue.</p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://issues.apache.org/jira/browse/OFBIZ-13006
* https://lists.apache.org/thread/w6s60okgkxp2th1sr8vx0ndmgk68fqrd


### Credits
* Qiyi Zhang (RacerZ) @secsys from Fudan (finder)


## Path traversal allowing authentication bypass. ## { #CVE-2024-25065 }

CVE-2024-25065 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-25065) [\[CVE json\]](./CVE-2024-25065.cve.json) [\[OSV json\]](./CVE-2024-25065.osv.json)



_Last updated: 2024-02-28T15:42:48.263Z_

### Affected

* Apache OFBiz before 18.12.12


### Description



Possible path traversal in Apache OFBiz allowing authentication bypass.<br>Users are recommended to upgrade to version 18.12.12, that fixes the issue.



### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.12.html
* https://issues.apache.org/jira/browse/OFBIZ-12887
* https://lists.apache.org/thread/rplfjp7ppn9ro49oo7jsrpj99m113lfc


### Credits
* YunPeng - 郭 运鹏 <puata123@outlook.com> (finder)


## Path traversal or file inclusion ## { #CVE-2024-23946 }

CVE-2024-23946 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-23946) [\[CVE json\]](./CVE-2024-23946.cve.json) [\[OSV json\]](./CVE-2024-23946.osv.json)



_Last updated: 2024-02-28T15:44:32.259Z_

### Affected

* Apache OFBiz before 18.12.12


### Description

Possible path traversal in Apache OFBiz allowing file inclusion.<br>Users are recommended to upgrade to version 18.12.12, that fixes the issue.

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.12.html
* https://issues.apache.org/jira/browse/OFBIZ-12884
* https://lists.apache.org/thread/w4lp5ncpzttf41hn5bsc04mzq4o6lw3g


### Credits
* Arun Shaji from trendmicro.com (finder)


## Pre-authentication Remote Code Execution (RCE) vulnerability ## { #CVE-2023-51467 }

CVE-2023-51467 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-51467) [\[CVE json\]](./CVE-2023-51467.cve.json) [\[OSV json\]](./CVE-2023-51467.osv.json)



_Last updated: 2024-02-02T10:13:56.898Z_

### Affected

* Apache OFBiz before 18.12.11


### Description

<div><span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">The vulnerability permits attackers to circumvent authentication processes, enabling them to remotely <span style="background-color: rgb(255, 255, 255);"><span style="background-color: rgb(255, 255, 255);">execute arbitrary code</span></span><br></span></span></div>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.11.html
* https://issues.apache.org/jira/browse/OFBIZ-12873
* https://lists.apache.org/thread/9tmf9qyyhgh6m052rhz7lg9vxn390bdv
* https://lists.apache.org/thread/oj2s6objhdq72t6g29omqpcbd1wlp48o
* https://www.openwall.com/lists/oss-security/2023/12/26/3


### Credits
* Hasib Vhora, Senior Threat Researcher, SonicWall  (finder)
* Gao Tian (finder)
* L0ne1y (finder)


## Arbitrary file properties reading and SSRF attack ## { #CVE-2023-50968 }

CVE-2023-50968 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-50968) [\[CVE json\]](./CVE-2023-50968.cve.json) [\[OSV json\]](./CVE-2023-50968.osv.json)



_Last updated: 2023-12-26T10:21:57.552Z_

### Affected

* Apache OFBiz through 18.12.10


### Description

<div>Arbitrary file properties reading vulnerability in Apache Software Foundation Apache OFBiz when user operates an uri call without authorizations.<br></div><div><br></div><div>The same uri can be operated to realize a SSRF attack also  without  authorizations.<br></div><div><br></div>Users are recommended to upgrade to version 18.12.11, which fixes this issue.

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.11.html
* https://issues.apache.org/jira/browse/OFBIZ-12875
* https://lists.apache.org/thread/x5now4bk3llwf3k58kl96qvtjyxwp43q


### Credits
* Yun Peng - 郭 运鹏 <puata123@outlook.com> (finder)


## Pre-auth RCE in Apache Ofbiz 18.12.09 due to XML-RPC still present ## { #CVE-2023-49070 }

CVE-2023-49070 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-49070) [\[CVE json\]](./CVE-2023-49070.cve.json) [\[OSV json\]](./CVE-2023-49070.osv.json)



_Last updated: 2023-12-20T10:48:11.952Z_

### Affected

* Apache OFBiz before 18.12.10


### Description



Pre-auth RCE in Apache Ofbiz 18.12.09.<br><br>It's due to XML-RPC&nbsp;<span style="background-color: rgb(255, 255, 255);">no longer maintained</span>&nbsp;still present.<br><p>This issue affects Apache OFBiz: before 18.12.10.&nbsp;<br><span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 18.12.10</span></p>



### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.10.html
* https://issues.apache.org/jira/browse/OFBIZ-12812
* https://lists.apache.org/thread/jmbqk2lp4t4483whzndp5xqlq4f3otg3


### Credits
* Siebene@ (finder)


## Execution of Solr plugin queries without authentication ## { #CVE-2023-46819 }

CVE-2023-46819 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2023-46819) [\[CVE json\]](./CVE-2023-46819.cve.json) [\[OSV json\]](./CVE-2023-46819.osv.json)



_Last updated: 2023-12-04T16:11:06.466Z_

### Affected

* Apache OFBiz before 18.12.09


### Description

Missing Authentication in Apache Software Foundation Apache OFBiz when using the Solr plugin.<br><p>This issue affects Apache OFBiz: before 18.12.09.&nbsp;

<span style="background-color: rgb(255, 255, 255);">Users are recommended to upgrade to version 18.12.09</span></p>

### References
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html
* https://ofbiz.apache.org/release-notes-18.12.09.html
* https://lists.apache.org/thread/mm5j0rsbl22q7yb0nmb6h2swbfjbwv99
* https://issues.apache.org/jira/browse/OFBIZ-12792


### Credits
* Anonymous by demand (finder)


## Arbitrary file reading vulnerability ## { #CVE-2022-47501 }

CVE-2022-47501 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-47501) [\[CVE json\]](./CVE-2022-47501.cve.json) [\[OSV json\]](./CVE-2022-47501.osv.json)



_Last updated: 2023-04-14T15:00:25.628Z_

### Affected

* Apache OFBiz from 18.12.06 before 18.12.07


### Description

Arbitrary file reading vulnerability in Apache Software Foundation Apache OFBiz when using the Solr plugin. This is a&nbsp;
pre-authentication attack.<br><p>This issue affects Apache OFBiz: before 18.12.07.</p>

### References
* https://lists.apache.org/thread/k8s76l0whydy45bfm4b69vq0mf94p3wc
* https://ofbiz.apache.org/download.html
* https://ofbiz.apache.org/security.html


### Credits
* Skay <lhcaomail@gmail.com> (finder)


## Regular Expression Denial of Service (ReDoS) vulnerability in Apache OFBiz ## { #CVE-2022-29158 }

CVE-2022-29158 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-29158) [\[CVE json\]](./CVE-2022-29158.cve.json) [\[OSV json\]](./CVE-2022-29158.osv.json)



_Last updated: 2022-09-02T07:05:27.871Z_

### Affected

* Apache OFBiz from Apache OFBiz through 18.12.05


### Description

Apache OFBiz up to version 18.12.05 is vulnerable to Regular Expression Denial of Service (ReDoS) in the way it handles URLs provided by external, unauthenticated users.
Upgrade to 18.12.06 or apply patches at https://issues.apache.org/jira/browse/OFBIZ-12599

### References
* https://lists.apache.org/thread/7k92rg1o4ql2yw3o0vttkcl2jhq7j928


### Credits
* Tony Torralba and Joseph Farebrother from the GitHub CodeQL team.


## Java Deserialization via RMI Connection from the Solr plugin of Apache OFBiz ## { #CVE-2022-29063 }

CVE-2022-29063 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-29063) [\[CVE json\]](./CVE-2022-29063.cve.json) [\[OSV json\]](./CVE-2022-29063.osv.json)



_Last updated: 2022-09-02T07:04:01.683Z_

### Affected

* Apache OFBiz from Apache OFBiz through 18.12.05


### Description

The Solr plugin of Apache OFBiz is configured by default to automatically make a RMI request on localhost, port 1099. In version 18.12.05 and earlier, by hosting a malicious RMI server on localhost, an attacker may exploit this behavior, at server start-up or on a server restart, in order to run arbitrary code.
Upgrade to at least 18.12.06 or apply patches at https://issues.apache.org/jira/browse/OFBIZ-12646.

### References
* https://lists.apache.org/thread/ytzrjc16pf357zntwk8tjby13kbx9105


### Credits
* Matei "Mal" Badanoiu


## Server-Side Template Injection affecting the ecommerce plugin of Apache OFBiz ## { #CVE-2022-25813 }

CVE-2022-25813 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-25813) [\[CVE json\]](./CVE-2022-25813.cve.json) [\[OSV json\]](./CVE-2022-25813.osv.json)



_Last updated: 2022-09-02T07:01:21.926Z_

### Affected

* Apache OFBiz from Apache OFBiz through 18.12.05


### Description

In Apache OFBiz, versions 18.12.05 and earlier, an attacker acting as an anonymous user of the ecommerce plugin, can insert a malicious content in a message “Subject” field from the "Contact us" page. Then a party
manager needs to list the communications in the party component to activate the SSTI. A RCE is then possible.

### References
* https://lists.apache.org/thread/vmj5s0qb59t0lvzf3vol3z1sc3sgyb2b


### Credits
*  Matei "Mal" Badanoiu


## Unauth Path Traversal with file corruption affecting the Birt plugin of Apache OFBiz ## { #CVE-2022-25371 }

CVE-2022-25371 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-25371) [\[CVE json\]](./CVE-2022-25371.cve.json) [\[OSV json\]](./CVE-2022-25371.osv.json)



_Last updated: 2022-09-02T07:00:04.371Z_

### Affected

* Apache OFBiz from Apache OFBiz through 18.12.05


### Description

Apache OFBiz uses the Birt project plugin (https://eclipse.github.io/birt-website/) to create data visualizations and reports.
By leveraging a bug in Birt (https://bugs.eclipse.org/bugs/show_bug.cgi?id=538142) it is possible to perform a remote code execution (RCE) attack in Apache OFBiz, release 18.12.05 and earlier.


### References
* https://lists.apache.org/thread/bvp3sczqq863lxr1wh7wjvdtjbkcwspq


### Credits
* Nikita Podotykin from Positive Technologies <npodotykin@ptsecurity.com>
* Positive Technologies  zeroday <zeroday@ptsecurity.com>


## Unauth Stored XSS vulnerability in the Birt plugin of Apache OFBiz ## { #CVE-2022-25370 }

CVE-2022-25370 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2022-25370) [\[CVE json\]](./CVE-2022-25370.cve.json) [\[OSV json\]](./CVE-2022-25370.osv.json)



_Last updated: 2022-09-02T06:58:56.611Z_

### Affected

* Apache OFBiz from Apache OFBiz through 18.12.05


### Description

Apache OFBiz uses the Birt plugin (https://eclipse.github.io/birt-website/) to create data visualizations and reports.
In Apache OFBiz release 18.12.05, and earlier versions, by leveraging a vulnerability in Birt (https://bugs.eclipse.org/bugs/show_bug.cgi?id=538142), an unauthenticated malicious user could perform a stored XSS attack in order to inject a malicious payload and execute it using the stored XSS.


### References
* https://lists.apache.org/thread/vrvzokvxqtc4t6d7g8xgz89xpxcvjofh


### Credits
* Nikita Podotykin from Positive Technologies <npodotykin@ptsecurity.com>
* Positive Technologies  zeroday <zeroday@ptsecurity.com>


## Arbitrary file upload vulnerability in OFBiz ## { #CVE-2021-37608 }

CVE-2021-37608 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-37608) [\[CVE json\]](./CVE-2021-37608.cve.json) [\[OSV json\]](./CVE-2021-37608.osv.json)



_Last updated: 2021-08-18T07:45:08.867Z_

### Affected

* Apache OFBiz from unspecified through 17.12.07


### Description

Unrestricted Upload of File with Dangerous Type vulnerability in Apache OFBiz allows an attacker to execute remote commands. This issue affects Apache OFBiz version 17.12.07 and prior versions. Upgrade to at least 17.12.08 or apply patches at https://issues.apache.org/jira/browse/OFBIZ-12297.

### References
* https://ofbiz.apache.org/security.html


### Credits
* Zhujie from Galaxy Security Laboratory <galaxylab@sina.com>


## Unsafe deserialization in Apache OFBiz ## { #CVE-2021-30128 }

CVE-2021-30128 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-30128) [\[CVE json\]](./CVE-2021-30128.cve.json) [\[OSV json\]](./CVE-2021-30128.osv.json)



_Last updated: 2021-04-27T19:47:04.244Z_

### Affected

* Apache OFBiz from Apache OFBiz before 17.12.07


### Description

Apache OFBiz has unsafe deserialization prior to 17.12.07 version

### References
* https://lists.apache.org/thread.html/rb3f5cd65f3ddce9b9eb4d6ea6e2919933f0f89b15953769d11003743%40%3Cdev.ofbiz.apache.org%3E


### Credits
* Apache OFBiz would like to thank Litch1 from the Security Team of Alibaba Cloud <litch1chk@gmail.com> for report


## RCE vulnerability in latest Apache OFBiz due to Java serialisation using RMI ## { #CVE-2021-29200 }

CVE-2021-29200 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-29200) [\[CVE json\]](./CVE-2021-29200.cve.json) [\[OSV json\]](./CVE-2021-29200.osv.json)



_Last updated: 2021-04-27T19:46:30.140Z_

### Affected

* Apache OFBiz from Apache OFBiz before 17.12.07


### Description

Apache OFBiz has unsafe deserialization prior to 17.12.07 version
An unauthenticated user can perform an RCE attack


### References
* https://lists.apache.org/thread.html/re21d25d9fb89e36cea910633779c23f144b9b60596b113b7bf1e8097%40%3Cdev.ofbiz.apache.org%3E


### Credits
* Apache OFBiz would like to thank the first report from "r00t4dm at Cloud-Penetrating Arrow Lab, asd of MoyunSec V-Lab <root@thiscode.cc> and 赖涵 <1044309102@qq.com>  a bit later


## RCE vulnerability in latest Apache OFBiz due to Java serialisation using RMI ## { #CVE-2021-26295 }

CVE-2021-26295 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-26295) [\[CVE json\]](./CVE-2021-26295.cve.json) [\[OSV json\]](./CVE-2021-26295.osv.json)



_Last updated: 2021-03-22T11:54:40.746Z_

### Affected

* Apache OFBiz at 17.12.01 to 17.12.05


### Description

Apache OFBiz has unsafe deserialization prior to 17.12.06. An unauthenticated attacker can use this vulnerability to successfully take over Apache OFBiz.


### References
* https://lists.apache.org/thread.html/r3c1802eaf34aa78a61b4e8e044c214bc94accbd28a11f3a276586a31%40%3Cuser.ofbiz.apache.org%3E


### Credits
* Apache OFBiz would like to thank the first report from "r00t4dm at Cloud-Penetrating Arrow Lab and Longofo at Knownsec 404 Team" and the second report by MagicZero from SGLAB of Legendsec at Qi'anxin Group.
