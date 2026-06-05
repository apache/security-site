---
title: Apache ECharts security advisories
description: Security information for Apache ECharts
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ECharts? You can read more about the projects' security policy on their [security page](https://echarts.apache.org/handbook/en/best-practices/security/#), and email your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://echarts.apache.org/handbook/en/best-practices/security/#). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## XSS in Lines series tooltip rendering ## { #CVE-2026-45249 }

CVE-2026-45249 [\[CVE\]](https://cve.org/CVERecord?id=CVE-2026-45249) [\[CVE json\]](./CVE-2026-45249.cve.json)

_Last updated: 2026-05-25T17:40:58.037Z_

### Affected

* Apache ECharts before 6.1.0


### Description

<p>A cross-site scripting (XSS) vulnerability exists in Apache ECharts in the <b>Lines</b> series tooltip rendering logic.</p><p><br>

<span style="background-color: rgb(255, 255, 255);">This issue affects Apache ECharts: from before 6.1.0.</span></p><p>In versions prior to 6.1.0, if both Lines series&nbsp;and tooltip are used, and no user-specified tooltip.formatter is provided, and series.data[i].name is specified, raw HTML string series.data[i].name can be&nbsp;rendered through innerHTML sink into tooltip content. Although tooltip is allowed to accept user-provided raw HTML via a custom tooltip.formatter, the built-in tooltip formatters conventionally perform HTML escaping automatically. This case breaks that convention and&nbsp;may unexpectedly lead to script execution when tooltips are displayed.</p><p><br>Users are recommended to upgrade to version 6.1.0 if using the Lines series in this way, which fixes the issue.</p>

### References
* https://github.com/apache/echarts/pull/21608
* https://echarts.apache.org/en/option.html#series-lines
* https://echarts.apache.org/handbook/en/best-practices/security/#passing_raw_html_safely
* https://lists.apache.org/thread/1g6xk7gd9vg1c6zyqqt2lnko10zomc3o


### Credits
* Lakshmikanthan K (finder)
