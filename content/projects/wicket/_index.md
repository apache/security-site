---
title: Apache Wicket security advisories
description: Security information for Apache Wicket
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Wicket? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=Wicket).

You can read more about the security policy on:

- [Apache Wicket security model](https://github.com/apache/wicket/security/policy)


# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the project security page linked above. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## XSS in AbstractSingleSelectChoice via getNullValidDisplayValue ## { #CVE-2026-76986 }

CVE-2026-76986 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-76986) [\[CVE json\]](./CVE-2026-76986.cve.json) [\[OSV json\]](./CVE-2026-76986.osv.json)



_Last updated: 2026-08-31T13:24:54.231Z_

### Affected

* Apache Wicket from 8.0.0 through 8.18.0
* Apache Wicket from 9.0.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.10.0


### Description

Improper neutralization of input during web page generation in Apache Wicket.<br><br>org.apache.wicket.markup.html.form.AbstractSingleSelectChoice, the base class of DropDownChoice, writes the body of the default option — the entry shown when no choice is selected — into the markup as it is, while every other option body in the same select is escaped according to the escape-model-strings setting. The body comes from getNullValidDisplayValue() or getNullKeyDisplayValue(), both of which are protected, so what they return is not necessarily the plain text the default implementation reads from a resource bundle.<br><br>An application is affected where it overrides one of those methods and returns a value holding data an attacker can influence, or where its own nullValid or null bundle entry holds such a value. The bundles shipped with Wicket contain plain text. RadioChoice overrides getDefaultChoice to emit no default option and is not affected.<br><br>As a workaround, escape the value in the override.<br><br>This issue affects Apache Wicket: from 8.0.0 through 8.18.0, from 9.0.0 through 9.23.0, from 10.0.0 through 10.10.0. Older, unsupported releases from 1.5.0 onwards are also affected. Users are recommended to upgrade to version 8.19.0, 9.24.0 or 10.11.0, which fix the issue.<br>

### References
* https://lists.apache.org/thread/4qltg6wckqz8wbs1f4jzqlc0yccpgvll


### Credits
* Emond Papegaaij (finder)


## XSS in Palette via getAdditionalAttributes ## { #CVE-2026-76985 }

CVE-2026-76985 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-76985) [\[CVE json\]](./CVE-2026-76985.cve.json) [\[OSV json\]](./CVE-2026-76985.osv.json)



_Last updated: 2026-08-31T13:22:10.063Z_

### Affected

* Apache Wicket from 8.0.0 through 8.18.0
* Apache Wicket from 9.0.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.10.0


### Description

Improper neutralization of input during web page generation in Apache Wicket.<br><br>org.apache.wicket.extensions.markup.html.form.palette.component.AbstractOptions, which renders the two option lists of a Palette, escapes the id and the display value of each option according to the escape-model-strings setting, and wrote the attribute names and values returned by getAdditionalAttributes into the &lt;option&gt; tag as they came.<br><br>An application is affected where it overrides Palette.getAdditionalAttributesForChoices, Palette.getAdditionalAttributesForSelection or AbstractOptions.getAdditionalAttributes and returns a value holding data an attacker can influence. These methods return null by default, so an application that does not override them is not affected.<br><br>As a workaround, escape the values in the override.<br><br>This issue affects Apache Wicket: from 8.0.0 through 8.18.0, from 9.0.0 through 9.23.0, from 10.0.0 through 10.10.0. Older, unsupported releases from 1.4.0 onwards are also affected. Users are recommended to upgrade to version 8.19.0, 9.24.0 or 10.11.0, which fix the issue.<br>

### References
* https://lists.apache.org/thread/0x2x12x22ff4yq4rhqokb2fjhtsd0f0j


### Credits
* Emond Papegaaij (finder)


## XSS in MetaDataHeaderItem via addTagAttribute ## { #CVE-2026-76984 }

CVE-2026-76984 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-76984) [\[CVE json\]](./CVE-2026-76984.cve.json) [\[OSV json\]](./CVE-2026-76984.osv.json)



_Last updated: 2026-08-31T11:56:14.047Z_

### Affected

* Apache Wicket from 8.0.0 through 8.18.0
* Apache Wicket from 9.0.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.10.0


### Description

Improper neutralization of input during web page generation in Apache Wicket.<br><br>org.apache.wicket.markup.head.MetaDataHeaderItem generates &lt;meta&gt; and &lt;link&gt; header tags. It escaped the attribute names it wrote, but ran the attribute values through a replacement of " with \". A backslash before a double quote means nothing in HTML, so a value containing a double quote ends its own attribute and what follows is parsed as further attributes of the generated tag.<br><br>An application is affected where it supplies an attribute value holding data an attacker can influence, through addTagAttribute or the forMetaTag and forLinkTag factory methods. A value may be given as an IModel, so it is not necessarily a literal.<br><br>There is no setting to change; an application can only avoid supplying a value that contains a double quote. Note that these values have never been escaped effectively: before the change released in 6.24.0, 7.4.0 and 8.0.0 they were written with no escaping at all.<br><br>This issue affects Apache Wicket: from 8.0.0 through 8.18.0, from 9.0.0 through 9.23.0, from 10.0.0 through 10.10.0. Older, unsupported releases from 6.17.0 onwards are also affected. Users are recommended to upgrade to version 8.19.0, 9.24.0 or 10.11.0, which fix the issue.<br>

### References
* https://lists.apache.org/thread/jt8yxntfjcxnnntth1qjtdo19gzx5n6v


### Credits
* Emond Papegaaij (finder)


## XSS in AutoLabelTextResolver via FormComponent.setLabel ## { #CVE-2026-76983 }

CVE-2026-76983 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-76983) [\[CVE json\]](./CVE-2026-76983.cve.json) [\[OSV json\]](./CVE-2026-76983.osv.json)



_Last updated: 2026-08-31T11:56:37.155Z_

### Affected

* Apache Wicket from 8.0.0 through 8.18.0
* Apache Wicket from 9.0.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.10.0


### Description

Improper neutralization of input during web page generation in Apache Wicket.<br><br>The &lt;wicket:label&gt; tag is provided by org.apache.wicket.markup.html.form.AutoLabelTextResolver, which is registered by default in every WebApplication. The resolver writes the label it finds into the markup as it is, and reads no escaping setting at all, so markup in a label is rendered as markup.<br><br>When the label comes from the labelled component's label model, set through FormComponent#setLabel(IModel), it is written to the markup unescaped.&nbsp;An application is affected where the label of a form component holds data an attacker can influence. Wicket cannot determine where a model value comes from, so whether it reaches the page from a request or from storage is a property of the application.<br><br>There is no workaround. Unlike every other rendering path in Wicket, the resolver never consulted the escape-model-strings setting, so an application had no way to ask for the label to be escaped.<br><br>The body of a &lt;wicket:label&gt; tag is markup by design and is not affected; it remains the supported way to place markup in a label.<br><br>This issue affects Apache Wicket: from 8.0.0 through 8.18.0, from 9.0.0 through 9.23.0, from 10.0.0 through 10.10.0. Older, unsupported releases from 1.5.0 onwards are also affected. Users are recommended to upgrade to version 8.19.0, 9.24.0 or 10.11.0, which fix the issue.<br>

### References
* https://lists.apache.org/thread/lfc9s9qkgxhm8ffscp9b7gjfgj47g25h


### Credits
* Ho1aAs (finder)


## XSS in Button via its model object ## { #CVE-2026-76982 }

CVE-2026-76982 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-76982) [\[CVE json\]](./CVE-2026-76982.cve.json) [\[OSV json\]](./CVE-2026-76982.osv.json)



_Last updated: 2026-08-31T11:52:24.884Z_

### Affected

* Apache Wicket from 8.0.0 through 8.18.0
* Apache Wicket from 9.0.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.10.0


### Description

Improper neutralization of input during web page generation in Apache Wicket.<br><br>org.apache.wicket.markup.html.form.Button clears the escape-model-strings flag in its constructor, so that the value attribute it writes is not encoded twice — ComponentTag already encodes attribute values when it writes the tag. That reasoning holds only for the attribute. When the component is attached to a &lt;button&gt; element rather than an &lt;input&gt;, it writes its model object into the element body instead, and nothing encodes an element body, so markup in the model is rendered as markup.<br><br>An application is affected where it renders a Button on a &lt;button&gt; element and that button's model holds data an attacker can influence. Wicket cannot determine where a model value comes from, so whether it reaches the page from a request or from storage is a property of the application. The subclasses that inherit this constructor — AjaxButton, AjaxFallbackButton and WizardButton — are affected on the same terms.<br><br>As a workaround, calling setEscapeModelStrings(true) on a button that renders as a &lt;button&gt; element escapes the body correctly, and does not cause double encoding, because the value attribute is written only for &lt;input&gt; elements.<br><br>This issue affects Apache Wicket: from 8.0.0 through 8.18.0, from 9.0.0 through 9.23.0, from 10.0.0 through 10.10.0. Older, unsupported releases from 6.25.0 and 7.5.0 onwards are also affected.<br><br>Users are recommended to upgrade to version 8.19.0, 9.24.0 or 10.11.0, which fix the issue.<br>

### References
* https://lists.apache.org/thread/bhcfrz61o4bv0olktybvgqft8km9wfrd


### Credits
* Emond Papegaaij (finder)


## XSS in AjaxEditableLabel and its subclasses via IChoiceRenderer and defaultNullLabel ## { #CVE-2026-75802 }

CVE-2026-75802 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-75802) [\[CVE json\]](./CVE-2026-75802.cve.json) [\[OSV json\]](./CVE-2026-75802.osv.json)



_Last updated: 2026-08-31T11:52:15.765Z_

### Affected

* Apache Wicket from 8.0.0 through 8.18.0
* Apache Wicket from 9.0.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.10.0


### Description

AjaxEditableChoiceLabel in wicket-extensions, when constructed with a non-null IChoiceRenderer, writes the display value obtained from that renderer into the label's markup without applying the HTML escaping Wicket performs by default for component model values. An attacker who can influence the choice or model data rendered by such a label can inject HTML or script that executes in the browser of any user who views the page. The same value is correctly escaped when the component's dropdown editor renders it as an option, so only the label rendering is affected.<br><br>AjaxEditableLabel, AjaxEditableChoiceLabel and AjaxEditableMultiLineLabel write the value returned by the protected defaultNullLabel() method into the label's markup the same way when the component's model is empty, while the model value they show otherwise is escaped. The default implementation returns a constant, so an application is affected where it overrides that method and returns a value an attacker can influence.<br><br>Neither value could be escaped by configuration, because escapeModelStrings had no effect on any of the three components: it is read by the label they render with rather than by the component itself, and nothing carried the setting across.<br><br>This issue affects Apache Wicket: from 8.0.0 through 8.18.0, from 9.0.0 through 9.23.0, from 10.0.0 through 10.10.0. Older, unsupported releases are also affected; the display value from the renderer since 6.22.0 and the null label since 1.4.0. Users are recommended to upgrade to version 8.19.0, 9.24.0 or 10.11.0, which fix the issue.<br>

### References
* https://lists.apache.org/thread/lrmo7mddb4v4ffl36g5b9x8s40tbmw68


### Credits
* Ho1aAs (finder)


## Cross-Site Request Forgery (CSRF) protection bypass in ResourceIsolationRequestCycleListener ## { #CVE-2026-71378 }

CVE-2026-71378 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-71378) [\[CVE json\]](./CVE-2026-71378.cve.json) [\[OSV json\]](./CVE-2026-71378.osv.json)



_Last updated: 2026-08-31T11:46:25.079Z_

### Affected

* Apache Wicket from 9.1.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.10.0


### Description

ResourceIsolationRequestCycleListener protects a Wicket application against cross-site&nbsp;request forgery by rejecting requests that a resource isolation policy judges to come from another origin. Its default policy, FetchMetadataResourceIsolationPolicy, was derived from&nbsp;a reference implementation written to guard static resources, and it inherited two&nbsp;allowances that are unsafe when the thing being guarded is an action on a page:<br><ol><li>Every "simple top-level navigation" was allowed. Any GET request carrying&nbsp;Sec-Fetch-Mode: navigate whose Sec-Fetch-Dest was neither object nor embed was&nbsp;allowed, whatever Sec-Fetch-Site said — including cross-site. Wicket invokes component&nbsp;listeners (Link.onClick(), form submits, behaviour callbacks) through ordinary GET&nbsp;navigations, so a page under an attacker's control could navigate the victim's browser to a&nbsp;listener URL and have that listener run inside the victim's authenticated session. Browsers&nbsp;send SameSite=Lax cookies — the effective default when no SameSite attribute is set — on&nbsp;cross-site top-level GET navigations, so the victim's session cookie accompanied the&nbsp;request.</li><li>Sec-Fetch-Site: same-site was allowed unconditionally. That value means the same&nbsp;registrable domain and scheme but a different origin — another subdomain or another&nbsp;port. Any sibling origin could therefore invoke any listener by any method, POST form&nbsp;submits included, and cookies are always sent on same-site requests regardless of&nbsp;SameSite. A hostile sibling origin obtained through a subdomain takeover, through&nbsp;delegated user content, or through an XSS elsewhere on the site could act as the&nbsp;authenticated user.</li></ol>Users are recommended to upgrade to version 9.24.0 or 10.11.0, which fix the issue.<br><h2><span>Affected versions</span></h2>

<ul><li><span>Apache Wicket 9.1.0 through 9.23.0</span></li><li><span>Apache Wicket 10.0.0 through 10.10.0</span></li></ul>
<h2><span>Not affected</span></h2>

<span><span>Any release older than 9.1.0:</span><br><ul><li><span>Apache Wicket 8.x (8.0.0 through 8.17.0). The resource isolation classes do not exist in</span><span>&nbsp;the 8.x line, which offers only the Origin/Referer-based</span><span>&nbsp;CsrfPreventionRequestCycleListener. </span><span>No 8.x release requires a fix.</span></li><li><span>Apache Wicket 9.0.0. ResourceIsolationRequestCycleListener</span><span>&nbsp;and FetchMetadataResourceIsolationPolicy were introduced by WICKET-6786 and first shipped</span><span>&nbsp;in 9.1.0 (released 2020-10-07).</span></li></ul></span>

### References
* https://lists.apache.org/thread/42d22kyz38td5zkqybw9fwdrvyfd5y62


### Credits
* Darren Carreras (finder)
* Andre Kropp (Nexory) (finder)


## Configured file upload limits are not enforced when the multipart request has already been parsed ## { #CVE-2026-71257 }

CVE-2026-71257 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-71257) [\[CVE json\]](./CVE-2026-71257.cve.json) [\[OSV json\]](./CVE-2026-71257.osv.json)



_Last updated: 2026-08-31T11:45:48.350Z_

### Affected

* Apache Wicket from 8.0.0 through 8.18.0
* Apache Wicket from 9.0.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.10.0


### Description

Apache Wicket enforces the upload limits configured on a form or upload field while parsing a multipart request with Apache Commons FileUpload. If the request body has already been consumed by another component, Commons FileUpload returns no items and Wicket falls back to reading the upload through HttpServletRequest#getParts(). The per-file size limit (for example Form#setFileMaxSize) and the file count limit (Form#setFileCountMax) are not applied to the parts obtained that way, and no exception is raised, so the upload is processed as though those limits had been satisfied. A remote uploader can therefore submit files that are larger, or more numerous, than the application permits, up to whatever the component that parsed the request allows. A part carrying no Content-Type header is additionally read into memory in full during parsing, so the size of that allocation is determined by the request and bounded only by those same external limits.<br><br>The total upload size limit (Form#setMaxSize) is not affected. Commons FileUpload compares the declared Content-Length against it before reading the body, so a request declaring an oversized length is rejected before the fallback is reached.<br><br>The fallback is reached in deployments where a servlet or filter has already parsed the request body — for example a servlet annotated with @MultipartConfig, Spring Boot's multipart resolver, or any filter that calls HttpServletRequest#getParameter() on a multipart request. It applies to the Wicket components that accept uploads on that path, including Form with FileUploadField, FileUploadToResourceField and AjaxFileDropBehavior. Applications that configure neither a per-file nor a file-count limit are not affected, as Wicket applies neither by default.<br><br>This issue affects Apache Wicket: from 8.0.0 through 8.18.0, from 9.0.0 through 9.23.0, from 10.0.0 through 10.10.0.<br><br>Users are recommended to upgrade to version 8.19.0, 9.24.0 or 10.11.0, which fix the issue. Users of Apache Wicket 7.x or older, which are no longer supported, should upgrade to a supported version. As a workaround, configure equivalent limits in the component that parses the request — for example spring.servlet.multipart.max-file-size and max-request-size, or maxFileSize and maxRequestSize in @MultipartConfig or in the web.xml &lt;multipart-config&gt; element.

### References
* https://lists.apache.org/thread/o59f8jz1m09kqdwm73pyyn6hdsxt190q


### Credits
* GitHub: @deprrous (finder)


## Path traversal in resource style/variation/locale ## { #CVE-2026-70449 }

CVE-2026-70449 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-70449) [\[CVE json\]](./CVE-2026-70449.cve.json) [\[OSV json\]](./CVE-2026-70449.osv.json)



_Last updated: 2026-08-31T11:44:41.974Z_

### Affected

* Apache Wicket from 8.0.0 through 8.18.0
* Apache Wicket from 9.0.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.10.0


### Description

Improper validation of resource URL attributes in Apache Wicket allows an unauthenticated remote attacker to read files from the web application, including files under WEB-INF that the servlet container would not otherwise serve.<br><br>The locale, style and variation attributes decoded from a package resource URL are spliced into the resource lookup path without being checked for path separators. The IPackageResourceGuard — whose rejection of .. is one of the two intended controls — is applied to the resource name before those attributes are appended, and WebApplicationPath rejects only paths literally beginning with WEB-INF/. Neither control ever inspects the attacker-controlled portion of the path. On servlet containers that normalize .. in ServletContext.getResource(), a crafted request therefore escapes the intended package directory.<br><br>The set of readable files is limited to the file extensions permitted by the configured IPackageResourceGuard. The default SecurePackageResourceGuard permits only js, css, png, jpg, jpeg, gif, ico, cur, map, html, txt, swf, bmp, svg, avif, eot, ttf, woff and woff2, which excludes configuration formats. Applications that have added patterns to the guard, or replaced it with the blocklist-based PackageResourceGuard, can additionally disclose configuration files such as web.xml. Independently of the extension, the lookup performed before the guard runs acts as an existence oracle for arbitrary paths.<span><br></span><br>This issue affects Apache Wicket 8.18.0 and before, 9.23.0 and before and 10.10.0 and before.<br><br>Users are recommended to upgrade to version 8.19.0, 9.24.0 or 10.11.0, which fix the issue. Users of Apache Wicket 7.x or older, which are no longer supported, should upgrade to a supported version.

### References
* https://lists.apache.org/thread/f4pb2q2ksdsfv1o315slp36dx66bf5vg


### Credits
* Michael Mullins (finder)
* n0mi1k (finder)


## leaked and missing CSP headers ## { #CVE-2026-66391 }

CVE-2026-66391 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66391) [\[CVE json\]](./CVE-2026-66391.cve.json) [\[OSV json\]](./CVE-2026-66391.osv.json)



_Last updated: 2026-07-28T14:49:40.413Z_

### Affected

* Apache Wicket from 9.0.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.9.0


### Description

<p>Use of Insufficiently Random Values, Protection Mechanism Failure vulnerability in Apache Wicket.</p><p>This issue affects Apache Wicket: from 9.0.0 through 9.23.0, from 10.0.0 through 10.9.0.</p><p>Users are recommended to upgrade to version 10.10.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/hfzcgjsbmmthzchtb8b8nv47d95scmqk


## crafted Link URL strings can break out of the JavaScript sequence ## { #CVE-2026-66390 }

CVE-2026-66390 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-66390) [\[CVE json\]](./CVE-2026-66390.cve.json) [\[OSV json\]](./CVE-2026-66390.osv.json)



_Last updated: 2026-07-28T14:49:11.657Z_

### Affected

* Apache Wicket from 9.0.0 through 9.23.0
* Apache Wicket from 10.0.0 through 10.9.0


### Description

<p>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Wicket.</p><p>This issue affects Apache Wicket: from 9.0.0 through 9.23.0, from 10.0.0 through 10.9.0.</p><p>Users are recommended to upgrade to version 10.10.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/67814fo0zocv3161bk1cr0ypvrkxky43


## Possible malicious path traversal in FolderUploadsFileManager ## { #CVE-2026-43975 }

CVE-2026-43975 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43975) [\[CVE json\]](./CVE-2026-43975.cve.json) [\[OSV json\]](./CVE-2026-43975.osv.json)



_Last updated: 2026-05-06T08:28:37.545Z_

### Affected

* Apache Wicket from 10.0.0 through 10.8.0
* Apache Wicket from 9.0.0 through 9.22.0
* Apache Wicket from 8.0.0 through 8.17


### Description

<p><code>FolderUploadsFileManager</code> in Apache Wicket does not validate or sanitize the <code>uploadFieldId</code> parameter or the <code>clientFileName</code>
 before constructing file paths, allowing an unauthenticated attacker to
 write arbitrary files outside the intended upload directory or read 
files from arbitrary locations on the server.</p><p>This issue affects Apache Wicket: from 8.0.0 through 8.17.0, from 9.0.0 through 9.22.0, from 10.0.0 through 10.8.0.</p><p>Users are recommended to upgrade to version 10.9.0, which fixes the issue.</p><br>

### References
* https://github.com/apache/wicket/pull/1432
* https://lists.apache.org/thread/xp2jrdk6ppv1zcmxb4w1mk2lg1dw3hbr


## crafted URLs can bypass PackageResourceGuard ## { #CVE-2026-43646 }

CVE-2026-43646 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-43646) [\[CVE json\]](./CVE-2026-43646.cve.json) [\[OSV json\]](./CVE-2026-43646.osv.json)



_Last updated: 2026-05-06T08:31:55.175Z_

### Affected

* Apache Wicket from 8.0.0 through 8.17.0
* Apache Wicket from 9.0.0 through 9.22.0
* Apache Wicket from 10.0.0 through 10.8.0


### Description

<p>Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Wicket.</p><p>This issue affects Apache Wicket: from 8.0.0 through 8.17.0, from 9.0.0 through 9.22.0, from 10.0.0 through 10.8.0.</p><p>Users are recommended to upgrade to version 10.9.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/6zqcvjyz4lsqty1z2g5hg7pl5fqk88rs


## crafted strings can break out of the JavaScript sequence ## { #CVE-2026-42509 }

CVE-2026-42509 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-42509) [\[CVE json\]](./CVE-2026-42509.cve.json) [\[OSV json\]](./CVE-2026-42509.osv.json)



_Last updated: 2026-05-06T08:34:07.745Z_

### Affected

* Apache Wicket from 8.0.0 through 8.17.0
* Apache Wicket from 9.0.0 through 9.22.0
* Apache Wicket from 10.0.0 through 10.8.0


### Description

<p>Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Wicket.</p><p>This issue affects Apache Wicket: from 8.0.0 through 8.17.0, 9.0.0, from 10.0.0 through 10.8.0.</p><p>Users are recommended to upgrade to version 10.9.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/52nrq4tt07gxz4r6sj5gyocz5s6bprjp


## possible session fixation using AuthenticatedWebSession ## { #CVE-2026-40010 }

CVE-2026-40010 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-40010) [\[CVE json\]](./CVE-2026-40010.cve.json) [\[OSV json\]](./CVE-2026-40010.osv.json)



_Last updated: 2026-05-06T08:34:37.475Z_

### Affected

* Apache Wicket from 10.0.0 through 10.8.0
* Apache Wicket from 8.0.0 through 8.17.0
* Apache Wicket from 9.0.0 through 9.22.0


### Description

<p>Missing invocation of Servlet http web request method changeSessionId after session binding can be exploited for a&nbsp;session fixation attack in Apache Wicket.</p><p>This issue affects Apache Wicket: from 8.0.0 through 8.17.0, 9.0.0, from 10.0.0 through 10.8.0.</p><p>Users are recommended to upgrade to version 10.9.0, which fixes the issue.</p><br>

### References
* https://lists.apache.org/thread/61wsc0xdtfd5oozojfx7by9w3jwgkmv1


## An attacker can intentionally trigger a memory leak ## { #CVE-2024-53299 }

CVE-2024-53299 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-53299) [\[CVE json\]](./CVE-2024-53299.cve.json) [\[OSV json\]](./CVE-2024-53299.osv.json)



_Last updated: 2025-01-23T08:37:04.162Z_

### Affected

* Apache Wicket from 7.0.0 through 7.18.*
* Apache Wicket from 8.0.0-M1 through 8.16.*
* Apache Wicket from 9.0.0-M1 through 9.18.*
* Apache Wicket from 10.0.0-M1 through 10.2.*


### Description

The request handling in the core in Apache Wicket 7.0.0 on any platform allows an attacker to create a DOS via multiple requests to server resources.<br>Users are recommended to upgrade to versions 9.19.0 or 10.3.0, which fixes this issue.

### References
* https://lists.apache.org/thread/gyp2ht00c62827y0379lxh5dbx3hhho5


### Credits
* Pedro Santos (finder)


## Remote code execution via XSLT injection ## { #CVE-2024-36522 }

CVE-2024-36522 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-36522) [\[CVE json\]](./CVE-2024-36522.cve.json) [\[OSV json\]](./CVE-2024-36522.osv.json)



_Last updated: 2024-07-12T12:13:50.122Z_

### Affected

* Apache Wicket from 10.0.0-M1 through 10.0.0
* Apache Wicket from 9.0.0 through 9.17.0
* Apache Wicket from 8.0.0 through 8.15.0


### Description

The default configuration of XSLTResourceStream.java is vulnerable to remote code execution via XSLT injection when <span style="background-color: rgb(255, 255, 255);">processing input from an untrusted source without validation</span>.<br>Users are recommended to upgrade to versions 10.1.0, 9.18.0 or 8.16.0, which fix this issue.

### References
* https://lists.apache.org/thread/w613qh7yors840pbx00l1pq6wkl9jzkc


### Credits
* cigar (finder)


## Possible bypass of CSRF protection ## { #CVE-2024-27439 }

CVE-2024-27439 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2024-27439) [\[CVE json\]](./CVE-2024-27439.cve.json) [\[OSV json\]](./CVE-2024-27439.osv.json)



_Last updated: 2024-03-19T11:07:46.188Z_

### Affected

* Apache Wicket from 9.1.0 through 9.16.0
* Apache Wicket from 10.0.0-M1 before 10.0.0


### Description

An error in the evaluation of the fetch metadata headers could allow a bypass of the CSRF protection in Apache Wicket.<br><p>This issue affects Apache Wicket: from 9.1.0 through 9.16.0, and the milestone releases for the 10.0 series.<br>Apache Wicket 8.x does not support CSRF protection via the fetch metadata headers and as such is not affected.</p><p>Users are recommended to upgrade to version 9.17.0 or 10.0.0, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/o825rvjjtmz3qv21ps5k7m2w9193g1lo


### Credits
* Jo Theunis (finder)


## DNS proxy and possible amplification attack ## { #CVE-2021-23937 }

CVE-2021-23937 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2021-23937) [\[CVE json\]](./CVE-2021-23937.cve.json) [\[OSV json\]](./CVE-2021-23937.osv.json)



_Last updated: 2021-05-25T08:01:09.799Z_

### Affected

* Apache Wicket from Apache Wicket 9.x through 9.2.0
* Apache Wicket from Apache Wicket 8.x through 8.11.0
* Apache Wicket from Apache Wicket 7.x through 7.17.0
* Apache Wicket from 6.2.0 before Apache Wicket 6.x*


### Description

A DNS proxy and possible amplification attack vulnerability in WebClientInfo of Apache Wicket allows an attacker to trigger arbitrary DNS lookups from the server when the X-Forwarded-For header is not properly sanitized. This DNS lookup can be engineered to overload an internal DNS server or to slow down request processing of the Apache Wicket application causing a possible denial of service on either the internal infrastructure or the web application itself.

This issue affects Apache Wicket Apache Wicket 9.x version 9.2.0 and prior versions; Apache Wicket 8.x version 8.11.0 and prior versions; Apache Wicket 7.x version 7.17.0 and prior versions and Apache Wicket 6.x version 6.2.0 and later versions.

### References
* https://lists.apache.org/thread.html/rc2ef22f90793e158cef65a7e370cdbca023c499d1403d65feeca870d%40%3Cusers.wicket.apache.org%3E


### Credits
* Apache Wicket would like to thank Jonathan Juursema from Topicus.Healthcare for reporting this issue.
