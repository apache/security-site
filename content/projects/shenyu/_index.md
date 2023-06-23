---
title: Apache ShenYu security advisories
description: Security information for Apache ShenYu
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ShenYu? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This page is experimental: it provides consistent access to the advisories for Apache ShenYu since 2023 in text and CVE JSON format. It may lag slighly behind the official CVE publications. 

If you have any feedback on how you would like this data to be presented, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)

## Apache ShenYu Admin ultra vires ## { #CVE-2022-42735 }

[CVE-2022-42735](./CVE-2022-42735.cve.json)

### Affected

* Apache ShenYu versions  including 2.5.0


### Description

Improper Privilege Management vulnerability in Apache Software Foundation Apache ShenYu.<br>

<span style="background-color: rgb(255, 255, 255);">ShenYu Admin allows low-privilege low-level administrators create users with higher privileges than their own.</span>

<p>This issue affects Apache ShenYu: 2.5.0.</p><p>Upgrade to Apache ShenYu 2.5.1 or apply patch <a target="_blank" rel="nofollow" href="https://github.com/apache/shenyu/pull/3958">https://github.com/apache/shenyu/pull/3958</a>.<br></p>