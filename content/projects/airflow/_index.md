---
title: Apache Airflow security advisories
description: Security information for Apache Airflow
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Airflow? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

## Hive Provider RCE vulnerability with hive_cli_params ## { #CVE-2022-46421 }

CVE-2022-46421 [\[CVE json\]](./CVE-2022-46421.cve.json)

### Affected

* Apache Airflow Hive Provider before 5.0.0


### Description

Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<p>This issue affects Apache Airflow Hive Provider: before 5.0.0.</p>

### References
* https://github.com/apache/airflow/pull/28101
* https://lists.apache.org/thread/09twdoyoybldlfj5gvk0qswtofh0rmp4


## Security vulnerability on AirFlow Connections ## { #CVE-2022-46651 }

CVE-2022-46651 [\[CVE json\]](./CVE-2022-46651.cve.json)

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows an unauthorized actor to gain access to sensitive information in Connection edit view. This vulnerability is considered low since it requires someone with access to Connection resources specifically updating the connection to exploit it. Users should upgrade to version 2.6.3 or later which has removed the vulnerability.<br>

### References
* https://github.com/apache/airflow/pull/32309
* https://lists.apache.org/thread/n45h3y82og125rnlgt6rbm9szfb6q24d


## Arbitrary file read via MySQL provider in Apache Airflow ## { #CVE-2023-22884 }

CVE-2023-22884 [\[CVE json\]](./CVE-2023-22884.cve.json)

### Affected

* Apache Airflow before 2.5.1
* Apache Airflow MySQL Provider before 4.0.0


### Description

Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache Airflow, Apache Software Foundation Apache Airflow MySQL Provider.<p>This issue affects Apache Airflow: before 2.5.1; Apache Airflow MySQL Provider: before 4.0.0.</p>

### References
* https://github.com/apache/airflow/pull/28811
* https://lists.apache.org/thread/0l0j3nt0t7fzrcjl2ch0jgj6c58kxs5h


## RCE Vulnerability ## { #CVE-2023-22886 }

CVE-2023-22886 [\[CVE json\]](./CVE-2023-22886.cve.json)

### Affected

* Apache Airflow JDBC Provider before 4.0.0


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow JDBC Provider.<br><span style="background-color: rgb(255, 255, 255);">Airflow JDBC Provider Connection’s [Connection URL] parameters had no</span><br><span style="background-color: rgb(255, 255, 255);">restrictions, which made it possible to implement RCE attacks via</span><br><span style="background-color: rgb(255, 255, 255);">different type JDBC drivers, obtain airflow server permission.</span><br><p>This issue affects Apache Airflow JDBC Provider: before 4.0.0.<br></p>

### References
* https://lists.apache.org/thread/ynbjwp4n0vzql0xzhog1gkp1ovncf8j3


## Apache Airflow path traversal by authenticated user ## { #CVE-2023-22887 }

CVE-2023-22887 [\[CVE json\]](./CVE-2023-22887.cve.json)

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows an attacker to perform unauthorized file access outside the intended directory structure by manipulating the run_id parameter. This vulnerability is considered low since it requires an authenticated user to exploit it. It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32293
* https://lists.apache.org/thread/rxddqs76r6rkxsg1n24d029zys67qwwo


## Scheduler remote DoS ## { #CVE-2023-22888 }

CVE-2023-22888 [\[CVE json\]](./CVE-2023-22888.cve.json)

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows an attacker to cause a service disruption by manipulating the run_id parameter. This vulnerability is considered low since it requires an authenticated user to exploit it. It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32293
* https://lists.apache.org/thread/dnlht2hvm7k81k5tgjtsfmk27c76kq7z


## Google Cloud Sql Provider Remote Command Execution ## { #CVE-2023-25691 }

CVE-2023-25691 [\[CVE json\]](./CVE-2023-25691.cve.json)

### Affected

* Apache Airflow Google Provider before 8.10.0


### Description

Improper Input Validation vulnerability in the Apache Airflow Google Provider.<br><br><p>This issue affects Apache Airflow Google Provider versions before 8.10.0.</p>

### References
* https://github.com/apache/airflow/pull/29497
* https://lists.apache.org/thread/zdr8ovfttbh7kj0lydgcw88tbt2nmkcy


## Google Cloud Sql Provider Denial Of Service ## { #CVE-2023-25692 }

CVE-2023-25692 [\[CVE json\]](./CVE-2023-25692.cve.json)

### Affected

* Apache Airflow Google Provider before 8.10.0


### Description

Improper Input Validation vulnerability in the Apache Airflow Google Provider.<br><br><p>This issue affects Apache Airflow Google Provider versions before 8.10.0.</p>

### References
* https://github.com/apache/airflow/pull/29499
* https://lists.apache.org/thread/ks4l78l5rwdpmvfn7y7yhs179nyxtlsh


## Sqoop Apache Airflow Provider Remote Code Execution Vulnerability ## { #CVE-2023-25693 }

CVE-2023-25693 [\[CVE json\]](./CVE-2023-25693.cve.json)

### Affected

* Apache Airflow Sqoop Provider before 3.1.1


### Description

Improper Input Validation vulnerability in the Apache Airflow Sqoop Provider.<br><br><p>This issue affects Apache Airflow Sqoop Provider versions before 3.1.1.</p>

### References
* https://github.com/apache/airflow/pull/29500
* https://lists.apache.org/thread/79qn8g5xbq036f8crb115obvr22l52q4


## Information disclosure in Apache Airflow ## { #CVE-2023-25695 }

CVE-2023-25695 [\[CVE json\]](./CVE-2023-25695.cve.json)

### Affected

* Apache Airflow before 2.5.2


### Description

Generation of Error Message Containing Sensitive Information vulnerability in Apache Software Foundation Apache Airflow.<p>This issue affects Apache Airflow: before 2.5.2.</p>

### References
* https://github.com/apache/airflow/pull/29501
* https://lists.apache.org/thread/z8w6ckzs61ql365tv4d19k82o67r15p2


## Apache Airflow Hive Provider Beeline RCE ## { #CVE-2023-25696 }

CVE-2023-25696 [\[CVE json\]](./CVE-2023-25696.cve.json)

### Affected

* Apache Airflow Hive Provider before 5.1.3


### Description

Improper Input Validation vulnerability in the Apache Airflow Hive Provider.<br><br><p>This issue affects Apache Airflow Hive Provider versions before 5.1.3.</p>

### References
* https://github.com/apache/airflow/pull/29502
* https://lists.apache.org/thread/99g0qm56wmgdxmbtdsvhj4rdnxhpzpml


## Privilege escalation using airflow logs ## { #CVE-2023-25754 }

CVE-2023-25754 [\[CVE json\]](./CVE-2023-25754.cve.json)

### Affected

* Apache Airflow before 2.6.0


### Description

Privilege Context Switching Error vulnerability in Apache Software Foundation Apache Airflow.<p>This issue affects Apache Airflow: before 2.6.0.</p>

### References
* https://github.com/apache/airflow/pull/29506
* https://lists.apache.org/thread/3y83gr0qb8t49ppfk4fb2yk7md8ltq4v


## Arbitrary file read via AWS provider ## { #CVE-2023-25956 }

CVE-2023-25956 [\[CVE json\]](./CVE-2023-25956.cve.json)

### Affected

* Apache Airflow AWS Provider before 7.2.1


### Description

Generation of Error Message Containing Sensitive Information vulnerability in the Apache Airflow AWS Provider.<br><br><p>This issue affects Apache Airflow AWS Provider versions before 7.2.1.</p>

### References
* https://github.com/apache/airflow/pull/29587
* https://lists.apache.org/thread/07pl9y4gdpw2c6rzqm77dvkm2z2kb5gv


## Apache Airflow Hive Provider Beeline Remote Command Execution ## { #CVE-2023-28706 }

CVE-2023-28706 [\[CVE json\]](./CVE-2023-28706.cve.json)

### Affected

* Apache Airflow Hive Provider before 6.0.0


### Description

Improper Control of Generation of Code ('Code Injection') vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<p>This issue affects Apache Airflow Hive Provider: before 6.0.0.</p>

### References
* https://github.com/apache/airflow/pull/30212
* https://lists.apache.org/thread/dl20xxd51xvlx0zzc0wzgxfjwgtbbxo3


## Airflow Apache Drill Provider Arbitrary File Read Vulnerability ## { #CVE-2023-28707 }

CVE-2023-28707 [\[CVE json\]](./CVE-2023-28707.cve.json)

### Affected

* Apache Airflow Drill Provider before 2.3.2


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Drill Provider.<p>This issue affects Apache Airflow Drill Provider: before 2.3.2.</p>

### References
* https://github.com/apache/airflow/pull/30215
* https://lists.apache.org/thread/dfoj7q1nd0vhhsl8fjg63z4j6mfmdxtk


## Apache Airflow Spark Provider Arbitrary File Read via JDBC ## { #CVE-2023-28710 }

CVE-2023-28710 [\[CVE json\]](./CVE-2023-28710.cve.json)

### Affected

* Apache Airflow Spark Provider before 4.0.1


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Spark Provider.<p>This issue affects Apache Airflow Spark Provider: before 4.0.1.</p>

### References
* https://github.com/apache/airflow/pull/30223
* https://lists.apache.org/thread/lb9w9114ow00h2nkn8bjm106v5x1p1d2


## Stored XSS on Apache Airflow ## { #CVE-2023-29247 }

CVE-2023-29247 [\[CVE json\]](./CVE-2023-29247.cve.json)

### Affected

* Apache Airflow before 2.6.0


### Description

Task instance details page in the UI is vulnerable to a stored XSS.<p>This issue affects Apache Airflow: before 2.6.0.</p><br>

### References
* https://github.com/apache/airflow/pull/30447
* https://github.com/apache/airflow/pull/30779
* https://lists.apache.org/thread/kqf5lxmko133780clsp827xfsh4xd3fl


## KubernetesPodOperator RCE via connection configuration ## { #CVE-2023-33234 }

CVE-2023-33234 [\[CVE json\]](./CVE-2023-33234.cve.json)

### Affected

* Apache Airflow CNCF Kubernetes Provider from 5.0.0 through 6.1.0


### Description

Arbitrary code execution in Apache Airflow CNCF Kubernetes provider version 5.0.0 allows user to change xcom sidecar image and resources via Airflow connection.<br><br>In order to exploit this weakness, a user would already need elevated permissions (Op or Admin) to change the connection object in this manner.&nbsp; Operators should upgrade to provider version 7.0.0 which has removed the vulnerability.<br><br>

### References
* https://lists.apache.org/thread/n1vpgl6h2qsdm52o9m2tx1oo86tl4gnq


## Remote code execution vulnerability ## { #CVE-2023-34395 }

CVE-2023-34395 [\[CVE json\]](./CVE-2023-34395.cve.json)

### Affected

* Apache Airflow ODBC Provider before 4.0.0


### Description

Improper Neutralization of Argument Delimiters in a Command ('Argument Injection') vulnerability in Apache Software Foundation Apache Airflow ODBC Provider.<br><span style="background-color: rgb(255, 255, 255);">In OdbcHook, A privilege escalation vulnerability exists in a system due to controllable ODBC driver parameters that allow the loading of arbitrary dynamic-link libraries, resulting in command execution.<br></span>Starting version 4.0.0 driver can be set only from the hook constructor.<br><p>This issue affects Apache Airflow ODBC Provider: before 4.0.0.</p>

### References
* https://github.com/apache/airflow/pull/31713
* https://lists.apache.org/thread/l26yykftzbhc9tgcph8cso88bc2lqwwd


## Information disclosure on configuration view ## { #CVE-2023-35005 }

CVE-2023-35005 [\[CVE json\]](./CVE-2023-35005.cve.json)

### Affected

* Apache Airflow from 2.5.0 before 2.6.2


### Description

<div>In Apache Airflow, some potentially sensitive values were being shown to the user in certain situations.</div><div>This vulnerability is mitigated by the fact configuration is not shown in the UI by default (only if `[webserver] expose_config` is set to `non-sensitive-only`), and not all uncensored values are actually sentitive.</div><br><div>This issue affects Apache Airflow: from 2.5.0 before 2.6.2. Users are recommended to update to version 2.6.2 or later.<br></div>

### References
* https://github.com/apache/airflow/pull/31788
* https://github.com/apache/airflow/pull/31820
* https://lists.apache.org/thread/o4f2cxh0054m9tlxpb81c1yhylor5gjd


## Apache Airflow Hive Provider Beeline RCE with Principal ## { #CVE-2023-35797 }

CVE-2023-35797 [\[CVE json\]](./CVE-2023-35797.cve.json)

### Affected

* Apache Airflow Apache Hive Provider before 6.1.1


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<br><p>This issue affects Apache Airflow Apache Hive Provider: before 6.1.1.<br><br><span style="background-color: rgb(255, 255, 255);">Before version 6.1.1 it was&nbsp;</span><span style="background-color: rgb(255, 255, 255);">possible to bypass the security check to RCE via</span><br><span style="background-color: rgb(255, 255, 255);">principal parameter. For this to be&nbsp;<span style="background-color: rgb(255, 255, 255);">exploited it requires access to modifying the connection details.</span><br></span><br>It is recommended updating provider version to 6.1.1 in order to avoid this&nbsp;vulnerability.</p>

### References
* https://github.com/apache/airflow/pull/31983
* https://lists.apache.org/thread/30y19ok07fw52x5hnkbhwqo3ho0wwc1y


## Airflow Apache ODBC and MSSQL Providers Arbitrary File Read Vulnerability ## { #CVE-2023-35798 }

CVE-2023-35798 [\[CVE json\]](./CVE-2023-35798.cve.json)

### Affected

* Apache Airflow ODBC Provider before 4.0.0
* Apache Airflow MSSQL Provider before 3.4.1


### Description

Input Validation vulnerability in Apache Software Foundation Apache Airflow ODBC Provider, Apache Software Foundation Apache Airflow MSSQL Provider.<p>This&nbsp;vulnerability is considered low since it requires DAG code to use `<span style="background-color: rgb(255, 255, 255);">get_sqlalchemy_connection` and someone with access to connection resources specifically&nbsp;updating the connection to <span style="background-color: rgb(255, 255, 255);">exploit it.</span><br></span><br>This issue affects Apache Airflow ODBC Provider: before 4.0.0; Apache Airflow MSSQL Provider: before 3.4.1.<br><br>It is recommended to&nbsp;<span style="background-color: rgb(255, 255, 255);">upgrade to a version that is not affected</span></p>

### References
* https://github.com/apache/airflow/pull/31984
* https://lists.apache.org/thread/951rb9m7wwox5p30tdvcfjxq8j1mp4pj


## Access to DAGs without relevant permission ## { #CVE-2023-35908 }

CVE-2023-35908 [\[CVE json\]](./CVE-2023-35908.cve.json)

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows unauthorized read access to a DAG through the URL.&nbsp;It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32014
* https://lists.apache.org/thread/vsflptk5dt30vrfggn96nx87d7zr6yvw


## ReDoS via dags function ## { #CVE-2023-36543 }

CVE-2023-36543 [\[CVE json\]](./CVE-2023-36543.cve.json)

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, has a vulnerability where an authenticated user can use crafted input to make the current request hang.&nbsp;It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32060
* https://lists.apache.org/thread/tokfs980504ylgk3cv3hjlnrtbv4tng4


## Improper Input Validation in Hive Provider with proxy_user ## { #CVE-2023-37415 }

CVE-2023-37415 [\[CVE json\]](./CVE-2023-37415.cve.json)

### Affected

* Apache Airflow Apache Hive Provider before 6.1.2


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Apache Hive Provider.<br><br>Patching on top of CVE-2023-35797<br><p>Before&nbsp;6.1.2<span style="background-color: rgb(255, 255, 255);">&nbsp;the proxy_user option can also inject semicolon.<br></span><br>This issue affects Apache Airflow Apache Hive Provider: before 6.1.2.<br><br></p><p>It is recommended updating provider version to 6.1.2 in order to avoid this vulnerability.</p><p></p>

### References
* https://lists.apache.org/thread/9wx0jlckbnycjh8nj5qfwxo423zvm41k
