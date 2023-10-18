---
title: Apache ShenYu security advisories
description: Security information for Apache ShenYu
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache ShenYu? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache ShenYu Admin bypass JWT authentication ## { #CVE-2021-37580 }

CVE-2021-37580 [\[CVE json\]](./CVE-2021-37580.cve.json)

### Affected

* Apache ShenYu Admin at Apache ShenYu Admin 2.3.0-2.4.0


### Description

A flaw was found in Apache ShenYu Admin. The incorrect use of JWT in ShenyuAdminBootstrap allows an attacker to bypass authentication.  This issue affected Apache ShenYu 2.3.0 and 2.4.0

### References
* https://lists.apache.org/thread/o15j25qwtpcw62k48xw1tnv48skh3zgb


### Credits
* This issue was reported by 伍 雄


## Apache ShenYu (incubating) Groovy Code Injection and SpEL Injection ## { #CVE-2021-45029 }

CVE-2021-45029 [\[CVE json\]](./CVE-2021-45029.cve.json)

### Affected

* Apache ShenYu (incubating)  from Apache ShenYu (incubating) before 2.4.2


### Description

Groovy Code Injection & SpEL Injection which lead to Remote Code Execution.
Apache ShenYu (incubating)  provides some plugins, and we can define our own Selectors And Rules in which we can set some condition match including "match = regEx like contain SpEL Groovy". 
There are no filters to avoid Remote Code Execution before parseExpression and Eval.me.
This issue affects Apache ShenYu (incubating)  2.4.0 and 2.4.1.

### References
* https://lists.apache.org/thread/3zzmwvg3012tg306x8o893fvdcssx639


## Apache ShenYu (incubating) Password leakage ## { #CVE-2022-23223 }

CVE-2022-23223 [\[CVE json\]](./CVE-2022-23223.cve.json)

### Affected

* Apache ShenYu (incubating)  from Apache ShenYu (incubating)  before 2.4.2


### Description

The HTTP response will disclose the user password. 
When users send the request like the following URL "dashboardUser?currentPage=1&pageSize=12", the response will disclose all the passwords of the users.
This issue affects Apache ShenYu (incubating) 2.4.0 and 2.4.1.

### References
* https://lists.apache.org/thread/q2gg6ny6lpkph7nkrvjzqdvqpm805v8s


## Apache ShenYu (incubating) Improper access control ## { #CVE-2022-23944 }

CVE-2022-23944 [\[CVE json\]](./CVE-2022-23944.cve.json)

### Affected

* Apache ShenYu (incubating)  from Apache ShenYu (incubating) before 2.4.2


### Description

Any user can access /plugin API without authentication. The project use Shiro to authenticate, but the default WhiteLists are defineded in application include /plugin path.
So everybody can access /plugin API which will list the details of all  plugins include id, name, config (may include password). We can also add a new plugin with  POST method while using /plugin API. 
This issue affects Apache ShenYu (incubating) 2.4.0 and 2.4.1.

### References
* https://lists.apache.org/thread/dbrjnnlrf80dr0f92k5r2ysfvf1kr67y


## Apache ShenYu (incubating) missing authentication allows gateway registration ## { #CVE-2022-23945 }

CVE-2022-23945 [\[CVE json\]](./CVE-2022-23945.cve.json)

### Affected

* Apache ShenYu (incubating)  from Apache ShenYu (incubating)  before 2.4.2


### Description

Missing  authentication on ShenYu Admin when a gateway registers. So, if ShenYu Admin is exposed to the internet, it will allow any user to register as the gateway.
This issue affects Apache ShenYu (incubating) 2.4.0 and 2.4.1.

### References
* https://lists.apache.org/thread/q2gg6ny6lpkph7nkrvjzqdvqpm805v8s


## Apache ShenYu (incubating) Regular expression denial of service ## { #CVE-2022-26650 }

CVE-2022-26650 [\[CVE json\]](./CVE-2022-26650.cve.json)

### Affected

* Apache ShenYu (incubating)  from unspecified before 2.4.3


### Description

In ShenYu-Bootstrap there's RegexPredicateJudge.java which uses Pattern.matches(conditionData.getParamValue(), realData) to make judgments, where both parameters are controllable by the user. This can cause an attacker pass in malicious regular expressions and characters causing a resource exhaustion. 
This issue affects Apache ShenYu (incubating) 2.4.0, 2.4.1 and 2.4.2.

### Credits
* Apache ShenYu would like to thank Lai Han of NSFOCUS security team <laihan4396@gmail.com> for reporting this issue.


## Apache ShenYu Admin Improper Privilege Management ## { #CVE-2022-37435 }

CVE-2022-37435 [\[CVE json\]](./CVE-2022-37435.cve.json)

### Affected

* Apache ShenYu at Apache ShenYu 2.4.2 and 2.4.3


### Description

Apache ShenYu Admin has insecure permissions, which may allow low-privilege administrators to modify high-privilege administrator's passwords.
This issue affects Apache ShenYu 2.4.2 and 2.4.3.

### References
* https://lists.apache.org/thread/ndblyxr2fdrvjtgbs1bogxgv2cgk7t28


### Credits
* Apache ShenYu would like to thank Lulu Gu <miogulugulu@gmail.com> for reporting this issue.


## Apache ShenYu Admin ultra vires ## { #CVE-2022-42735 }

CVE-2022-42735 [\[CVE json\]](./CVE-2022-42735.cve.json)

### Affected

* Apache ShenYu through 2.5.0


### Description

Improper Privilege Management vulnerability in Apache Software Foundation Apache ShenYu.<br>

<span style="background-color: rgb(255, 255, 255);">ShenYu Admin allows low-privilege low-level administrators create users with higher privileges than their own.</span>

<p>This issue affects Apache ShenYu: 2.5.0.</p><p>Upgrade to Apache ShenYu 2.5.1 or apply patch <a target="_blank" rel="nofollow" href="https://github.com/apache/shenyu/pull/3958">https://github.com/apache/shenyu/pull/3958</a>.<br></p>

### References
* https://lists.apache.org/thread/2k8764jmckmc19qc8x51nlnngq71pcf7


### Credits
* xxhzz (finder)
