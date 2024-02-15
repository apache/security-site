---
title: Apache Dubbo security advisories
description: Security information for Apache Dubbo
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Dubbo? You can read more about the projects' security policy on their [security page](https://dubbo.apache.org/en/docs/notices/security/), and email your report to the [Apache Dubbo Security Team](mailto:security@dubbo.apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. It may also lack details found on the [project security page](https://dubbo.apache.org/en/docs/notices/security/). If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Apache Dubbo default deserialization protocol Hessian2 cause CRE ## { #CVE-2020-11995 }

CVE-2020-11995 [\[CVE json\]](./CVE-2020-11995.cve.json)

_Last updated: 2021-01-11T09:22:59.963Z_

### Affected

* Apache Dubbo from Apache Dubbo before 2.6.9


### Description

A deserialization vulnerability existed in dubbo 2.7.5 and its earlier versions, which could lead to malicious code execution. Most Dubbo users use Hessian2 as the default serialization/deserialization protool, during Hessian2 deserializing the HashMap object, some functions in the classes stored in HasMap will be executed after a series of program calls, however, those special functions may cause remote command execution. For example, the hashCode() function of the EqualsBean class in rome-1.7.0.jar will cause the remotely load malicious classes and execute malicious code by constructing a malicious request.  This issue was fixed in Apache Dubbo 2.6.9 and 2.7.8.

### References
* https://lists.apache.org/thread.html/r5b2df4ef479209dc4ced457b3d58a887763b60b9354c3dc148b2eb5b%40%3Cdev.dubbo.apache.org%3E


## Open Redirect or SSRF vulnerability usage of parseURL ## { #CVE-2021-25640 }

CVE-2021-25640 [\[CVE json\]](./CVE-2021-25640.cve.json)

_Last updated: 2021-05-31T07:23:34.814Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x before 2.7.9
* Apache Dubbo from Apache Dubbo 2.6.x before 2.6.9


### Description

In Apache Dubbo prior to 2.6.9 and 2.7.9, the usage of parseURL method will lead to the bypass of white host check which can cause open redirect or SSRF vulnerability.

### References
* https://lists.apache.org/thread.html/re4cab8855361a454d2af106fb3dad76259e723015fd7e09cb4f9eb77%40%3Cdev.dubbo.apache.org%3E


### Credits
* This issue was first reported by Bing Dong


## Dubbo Zookeeper does not check serialization id ## { #CVE-2021-25641 }

CVE-2021-25641 [\[CVE json\]](./CVE-2021-25641.cve.json)

_Last updated: 2021-05-29T07:21:43.205Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x before 2.7.8
* Apache Dubbo from Apache Dubbo 2.6.x before 2.6.9


### Description

Each Apache Dubbo server will set a serialization id to tell the clients which serialization protocol it is working on. But for Dubbo versions before 2.7.8 or 2.6.9, an attacker can choose which serialization id the Provider will use by tampering with the byte preamble flags, aka, not following the server's instruction. This means that if a weak deserializer such as the Kryo and FST are somehow in code scope (e.g. if Kryo is somehow a part of a dependency), a remote unauthenticated attacker can tell the Provider to use the weak deserializer, and then proceed to exploit it. 

### References
* https://lists.apache.org/thread.html/r99ef7fa35585d3a68762de07e8d2b2bc48b8fa669a03e8d84b9673f3%40%3Cdev.dubbo.apache.org%3E


## Apache Dubbo Pre-auth RCE via Java deserialization in the Generic filter ## { #CVE-2021-30179 }

CVE-2021-30179 [\[CVE json\]](./CVE-2021-30179.cve.json)

_Last updated: 2021-05-31T07:20:28.079Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x before 2.7.9
* Apache Dubbo from Apache Dubbo 2.6.x before 2.6.9


### Description

Apache Dubbo prior to 2.6.9 and 2.7.9 by default supports generic calls to arbitrary methods exposed by provider interfaces. These invocations are handled by the GenericFilter which will find the service and method specified in the first arguments of the invocation and use the Java Reflection API to make the final call. The signature for the $invoke or $invokeAsync methods is Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/Object; where the first argument is the name of the method to invoke, the second one is an array with the parameter types for the method being invoked and the third one is an array with the actual call arguments.

In addition, the caller also needs to set an RPC attachment specifying that the call is a generic call and how to decode the arguments. The possible values are:

- true
- raw.return
- nativejava
- bean
- protobuf-json

An attacker can control this RPC attachment and set it to nativejava to force the java deserialization of the byte array located in the third argument.


### References
* https://lists.apache.org/thread.html/rccbcbdd6593e42ea3a1e8fedd12807cb111375c9c40edb005ef36f67%40%3Cdev.dubbo.apache.org%3E


### Credits
* This issue was first reported by GitHub Security Lab


## Apache Dubbo RCE on customers via Condition route poisoning (Unsafe YAML unmarshaling) ## { #CVE-2021-30180 }

CVE-2021-30180 [\[CVE json\]](./CVE-2021-30180.cve.json)

_Last updated: 2021-05-31T07:21:55.266Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x before 2.7.9


### Description

Apache Dubbo prior to 2.7.9 support Tag routing which will enable a customer to route the request to the right server. These rules are used by the customers when making a request in order to find the right endpoint. When parsing these YAML rules, Dubbo customers may enable calling arbitrary constructors.

### References
* https://lists.apache.org/thread.html/raed526465e56204030ddf374b1959478a290e7511971d7aba2e9e39b%40%3Cdev.dubbo.apache.org%3E


### Credits
* This issue was first reported by GitHub Security Lab


## Apache Dubbo RCE on customers via Script route poisoning (Nashorn script injection) ## { #CVE-2021-30181 }

CVE-2021-30181 [\[CVE json\]](./CVE-2021-30181.cve.json)

_Last updated: 2021-05-29T07:19:20.347Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x before 2.7.9
* Apache Dubbo from Apache Dubbo 2.6.x before 2.6.9


### Description

Apache Dubbo prior to 2.6.9 and 2.7.9 supports Script routing which will enable a customer to route the request to the right server. These rules are used by the customers when making a request in order to find the right endpoint. When parsing these rules, Dubbo customers use ScriptEngine and run the rule provided by the script which by default may enable executing arbitrary code.

### References
* https://lists.apache.org/thread.html/re22410dc704a09bc7032ddf15140cf5e7df3e8ece390fc9032ff5587%40%3Cdev.dubbo.apache.org%3E


## Unprotected input value toString cause RCE ## { #CVE-2021-36161 }

CVE-2021-36161 [\[CVE json\]](./CVE-2021-36161.cve.json)

_Last updated: 2021-09-09T07:39:17.113Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x through 2.7.12


### Description

Some component in Dubbo will try to print the formated string of the input arguments, which will possibly cause RCE for a maliciously customized bean with special toString method. In the latest version, we fix the toString call in timeout, cache and some other places. Fixed in Apache Dubbo 2.7.13

### References
* https://lists.apache.org/thread.html/r40212261fd5d638074b65f22ac73eebe93ace310c79d4cfcca4863da%40%3Cdev.dubbo.apache.org%3E


## Unprotected yaml deserialization cause RCE ## { #CVE-2021-36162 }

CVE-2021-36162 [\[CVE json\]](./CVE-2021-36162.cve.json)

_Last updated: 2021-09-07T09:20:04.687Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x through 2.7.12
* Apache Dubbo from Apache Dubbo 3.0.x through 3.0.1


### Description

Apache Dubbo supports various rules to support configuration override or traffic routing (called routing in Dubbo). These rules are loaded into the configuration center (eg: Zookeeper, Nacos, ...) and retrieved by the customers when making a request in order to find the right endpoint.

When parsing these YAML rules, Dubbo customers will use SnakeYAML library to load the rules which by default will enable calling arbitrary constructors. An attacker with access to the configuration center he will be able to poison the rule so when retrieved by the consumers, it will get RCE on all of them.  This was fixed in Dubbo 2.7.13, 3.0.2

### References
* https://lists.apache.org/thread.html/rfa351115a459e214b99ffcc52c35f33359f3370c547d9c6ba1a60037%40%3Cdev.dubbo.apache.org%3E


## Unsafe deserialization in providers using the Hessian protocol ## { #CVE-2021-36163 }

CVE-2021-36163 [\[CVE json\]](./CVE-2021-36163.cve.json)

_Last updated: 2021-09-07T09:21:20.469Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x through 2.7.12
* Apache Dubbo from Apache Dubbo 2.6.x through 2.6.10


### Description

In Apache Dubbo, users may choose to use the Hessian protocol. The Hessian protocol is implemented on top of HTTP and passes the body of a POST request directly to a HessianSkeleton:
New HessianSkeleton are created without any configuration of the serialization factory and therefore without applying the dubbo properties for applying allowed or blocked type lists.
In addition, the generic service is always exposed and therefore attackers do not need to figure out a valid service/method name pair.  This is fixed in 2.7.13, 2.6.10.1

### References
* https://lists.apache.org/thread.html/r8d0adc057bb15a37199502cc366f4b1164c9c536ce28e4defdb428c0%40%3Cdev.dubbo.apache.org%3E


## Bypass deserialization checks in Apache Dubbo ## { #CVE-2021-37579 }

CVE-2021-37579 [\[CVE json\]](./CVE-2021-37579.cve.json)

_Last updated: 2021-09-09T07:40:35.954Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x through 2.7.12
* Apache Dubbo from Apache Dubbo 3.0.x through 3.0.1


### Description

The Dubbo Provider will check the incoming request and the corresponding serialization type of this request meet the configuration set by the server. But there's an exception that the attacker can use to skip the security check (when enabled) and reaching a deserialization operation with native java serialization.

Apache Dubbo 2.7.13, 3.0.2 fixed this issue by quickly fail when any unrecognized request was found.

### References
* https://lists.apache.org/thread.html/r898afa109cdbb4b79724308648ff0718152ebe1d3d6dfc7202d958bc%40%3Cdev.dubbo.apache.org%3E


## Dubbo Hessian cause RCE when parse error ## { #CVE-2021-43297 }

CVE-2021-43297 [\[CVE json\]](./CVE-2021-43297.cve.json)

_Last updated: 2022-01-10T06:23:23.358Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.6.x before 2.6.12
* Apache Dubbo from Apache Dubbo 2.7.x before 2.7.15
* Apache Dubbo from Apache Dubbo 3.0.x before 3.0.5


### Description

A deserialization vulnerability existed in dubbo hessian-lite  3.2.11 and its earlier versions, which could lead to malicious code execution. Most Dubbo users use Hessian2 as the default serialization/deserialization protocol, during Hessian catch unexpected exceptions, Hessian will log out some imformation for users, which may cause remote command execution. This issue affects Apache Dubbo Apache Dubbo 2.6.x versions prior to 2.6.12; Apache Dubbo 2.7.x versions prior to 2.7.15; Apache Dubbo 3.0.x versions prior to 3.0.5.

### References
* https://lists.apache.org/thread/1mszxrvp90y01xob56yp002939c7hlww


### Credits
* There are differences in the use of entrances. The following people or organizations reported security vulnerabilities independently. Sort by discovery time: 1. cxc&yhbl&wh1t3p1g&fynch3r from G5-RD6@IIE 2. yxxx


## bypass of CVE-2021-25640 ## { #CVE-2022-24969 }

CVE-2022-24969 [\[CVE json\]](./CVE-2022-24969.cve.json)

_Last updated: 2022-06-06T21:43:07.547Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x before 2.7.15
* Apache Dubbo from Apache Dubbo 2.6.x through 2.6.12


### Description

bypass CVE-2021-25640 

> In Apache Dubbo prior to 2.6.12 and 2.7.15, the usage of parseURL method will lead to the bypass of the white host check which can cause open redirect or SSRF vulnerability.

### References
* https://lists.apache.org/thread/1xbckc3467wfk5r7n2o44r2brdsbwxgr


## Apache Dubbo Hession Deserialization Vulnerability Gadgets Bypass ## { #CVE-2022-39198 }

CVE-2022-39198 [\[CVE json\]](./CVE-2022-39198.cve.json)

_Last updated: 2022-10-18T18:50:42.549Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x through 2.7.17
* Apache Dubbo from Apache Dubbo 3.0.x through 3.0.11
* Apache Dubbo from Apache Dubbo 3.1.x through 3.1.0


### Description

A deserialization vulnerability existed in dubbo hessian-lite 3.2.12 and its earlier versions, which could lead to malicious code execution. 

This issue affects Apache Dubbo 2.7.x version 2.7.17 and prior versions; Apache Dubbo 3.0.x version 3.0.11 and prior versions; Apache Dubbo 3.1.x version 3.1.0 and prior versions. 

### References
* https://lists.apache.org/thread/8d3zqrkoy4jh8dy37j4rd7g9jodzlvkk


### Credits
* yemoli&cxc


## Apache Dubbo Deserialization Vulnerability Gadgets Bypass ## { #CVE-2023-23638 }

CVE-2023-23638 [\[CVE json\]](./CVE-2023-23638.cve.json)

_Last updated: 2023-03-08T08:51:34.345Z_

### Affected

* Apache Dubbo from Apache Dubbo 2.7.x through 2.7.21
* Apache Dubbo from Apache Dubbo 3.0.x through 3.0.13
* Apache Dubbo from Apache Dubbo 3.1.x through 3.1.5


### Description

A deserialization vulnerability existed when dubbo generic invoke, which could lead to malicious code execution. <br><br>This issue affects Apache Dubbo 2.7.x version 2.7.21 and prior versions; Apache Dubbo 3.0.x version 3.0.13 and prior versions; Apache Dubbo 3.1.x version 3.1.5 and prior versions. 

### References
* https://lists.apache.org/thread/8h6zscfzj482z512d2v5ft63hdhzm0cb


### Credits
* yemoli、R1ckyZ、Koishi、cxc (reporter)


## Bypass serialize checks in Apache Dubbo ## { #CVE-2023-29234 }

CVE-2023-29234 [\[CVE json\]](./CVE-2023-29234.cve.json)

_Last updated: 2023-12-15T05:49:00.876Z_

### Affected

* Apache Dubbo from 3.1.0 through 3.1.10
* Apache Dubbo from 3.2.0 through 3.2.4


### Description

A deserialization vulnerability existed when decode a&nbsp;malicious package.<p>This issue affects Apache Dubbo: from 3.1.0 through 3.1.10, from 3.2.0 through 3.2.4.</p><p>Users are recommended to upgrade to the latest version, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/wb2df2whkdnbgp54nnqn0m94rllx8f77


### Credits
* Bofei Chen, Lei Zhang, Guangliang Yang, Keke Lian and Xinyou Huang (finder)


## Bypass deny serialize list check in Apache Dubbo ## { #CVE-2023-46279 }

CVE-2023-46279 [\[CVE json\]](./CVE-2023-46279.cve.json)

_Last updated: 2023-12-15T05:50:43.130Z_

### Affected

* Apache Dubbo at 3.1.5


### Description

Deserialization of Untrusted Data vulnerability in Apache Dubbo.<p>This issue only affects Apache Dubbo 3.1.5.</p><p>Users are recommended to upgrade to the latest version, which fixes the issue.</p>

### References
* https://lists.apache.org/thread/zw53nxrkrfswmk9n3sfwxmcj7x030nmo
