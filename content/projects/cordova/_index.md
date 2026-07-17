---
title: Apache Cordova security advisories
description: Security information for Apache Cordova
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Cordova? Send your report to the [Apache Security Team](mailto:security@apache.org?subject=%5BFINDING%5D%20Apache%20Cordova).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## iOS: Arbitrary Cordova callback IDs can be dispatched without validation from InAppBrowser WebViews ## { #CVE-2026-47430 }

CVE-2026-47430 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-47430) [\[CVE json\]](./CVE-2026-47430.cve.json) [\[OSV json\]](./CVE-2026-47430.osv.json)



_Last updated: 2026-06-08T11:27:13.460Z_

### Affected

* Cordova Plugin InAppBrowser from 3.1.0 through 6.0.0


### Description

<h2>Summary</h2><p><br>The iOS implementation of `cordova-plugin-inappbrowser` passes the `id` field from a `WKScriptMessage` body to `commandDelegate sendPluginResult:callbackId:` with no format validation (`CDVWKInAppBrowser.m:560–574`). Any web content loaded inside the InAppBrowser can fire any pending Cordova callback in the host app by posting a message whose `id` field is a guessable or enumerated callback identifier. An attack abusing this weakness must be tailored to the specific plugins and callback IDs the host app uses. Though an attacker with knowledge of common Cordova plugin configurations could craft reusable payloads targeting widely-adopted plugins.</p><p><br></p><h2>Impact</h2><p><br>An unauthenticated remote attacker who controls content displayed in the InAppBrowser — via a URL the app opens (OAuth redirect, marketing link, deep-link target) or a network interception — can call `window.webkit.messageHandlers.cordova_iab.postMessage({id: '&lt;victim-callback-id&gt;', d: '...'})` to fire callbacks belonging to any other installed Cordova plugin (Camera, Contacts, File, Geolocation). Cordova callback IDs follow the predictable format `&lt;PluginName&gt;&lt;sequential-integer&gt;`, making enumeration feasible. Successful exploitation allows the attacker to spoof plugin results across trust boundaries — for example, injecting a forged camera approval, a fabricated contacts list, or a crafted file-read response.</p><p>This issue affects Cordova Plugin InAppBrowser: from 3.1.0 through 6.0.0.</p><p>Users are recommended to upgrade to version 6.0.1, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/sb539nss3b0545wnyt1pbh7zgwjvz2qq


### Credits
* Niklas Merz (reporter)
