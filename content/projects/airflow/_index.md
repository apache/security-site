---
title: Apache Airflow security advisories
description: Security information for Apache Airflow
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Airflow? Send your report to the [Apache Security Team](mailto:security@apache.org).

# Advisories

This section is experimental: it provides advisories since 2023 and may lag behind the official CVE publications. If you have any feedback on how you would like this data to be provided, you are welcome to reach out on our public [mailinglist](/mailinglist) or privately on [security@apache.org](mailto:security@apache.org)
{.bg-warning}

##  ## { #CVE-2020-17515 }

CVE-2020-17515 [\[CVE json\]](./CVE-2020-17515.cve.json)

### Affected

* Apache Airflow from Apache Airflow before 1.10.13


### Description

The "origin" parameter passed to some of the endpoints like '/trigger' was vulnerable to XSS exploit. This issue affects Apache Airflow versions prior to 1.10.13.

This is same as CVE-2020-13944 but the implemented fix in Airflow 1.10.13 did not fix the issue completely.

### References
* https://lists.apache.org/thread.html/r4656959c8ed06c1f6202d89aa4e67b35ad7bdba5a666caff3fea888e%40%3Cusers.airflow.apache.org%3E


### Credits
* Ali Abdulwahab Ali Al-habsi of Accellion


##  ## { #CVE-2020-17511 }

CVE-2020-17511 [\[CVE json\]](./CVE-2020-17511.cve.json)

### Affected

* Apache Airflow from Apache Airflow before 1.10.13


### Description

In Airflow versions prior to 1.10.13, when creating a user using airflow CLI, the password gets logged in plain text in the Log table in Airflow Metadatase. Same happened when creating a Connection with a password field.


### References
* https://lists.apache.org/thread.html/ree782a29d927b96bf0b39fb92e2f1f09ea3112a985f7a08ce93765ac%40%3Cusers.airflow.apache.org%3E


### Credits
* Ali Al-Habsi of Accellion


##  ## { #CVE-2020-17513 }

CVE-2020-17513 [\[CVE json\]](./CVE-2020-17513.cve.json)

### Affected

* Apache Airflow from Apache Airflow before 1.10.13


### Description

In Apache Airflow versions prior to 1.10.13, the Charts and Query View of the old (Flask-admin based) UI were vulnerable for SSRF attack.

### References
* https://lists.apache.org/thread.html/rb3647269f07cc2775ca6568cbfd4994d862c842a58120d2aba9c658a%40%3Cusers.airflow.apache.org%3E


##  ## { #CVE-2020-17526 }

CVE-2020-17526 [\[CVE json\]](./CVE-2020-17526.cve.json)

### Affected

* Apache Airflow from Apache Airflow before 1.10.14


### Description

Incorrect Session Validation in Apache Airflow Webserver versions prior to 1.10.14 with default config allows a malicious airflow user on site A where they log in normally, to access unauthorized Airflow Webserver on Site B through the session from Site A.  This does not affect users who have changed the default value for `[webserver] secret_key` config.

### References
* https://lists.apache.org/thread.html/rbeeb73a6c741f2f9200d83b9c2220610da314810c4e8c9cf881d47ef%40%3Cusers.airflow.apache.org%3E


### Credits
* Junghan Lee of Deliveryhero Korea Security Team


## CWE-284 Improper Access Control on Configurations Endpoint for the Stable API ## { #CVE-2021-26559 }

CVE-2021-26559 [\[CVE json\]](./CVE-2021-26559.cve.json)

### Affected

* Apache Airflow at 2.0.0


### Description

Improper Access Control on Configurations Endpoint for the Stable API of Apache Airflow allows users with Viewer or User role to get Airflow Configurations including sensitive information even when `[webserver] expose_config` is set to `False` in `airflow.cfg`. 

This allowed a privilege escalation attack.

This issue affects Apache Airflow 2.0.0.

### References
* https://lists.apache.org/thread.html/r3b3787700279ec361308cbefb7c2cce2acb26891a12ce864e4a13c8d%40%3Cusers.airflow.apache.org%3E


### Credits
* Apache Airflow would like to thank Ian Carroll for reporting this issue.


## Apache Airflow: Lineage API endpoint for Experimental API missed authentication check ## { #CVE-2021-26697 }

CVE-2021-26697 [\[CVE json\]](./CVE-2021-26697.cve.json)

### Affected

* Apache Airflow at 2.0.0


### Description

The lineage endpoint of the deprecated Experimental API was not protected by authentication in Airflow 2.0.0. This allowed unauthenticated users to hit that endpoint.

This is low-severity issue as the attacker needs to be aware of certain parameters to pass to that endpoint and even after can just get some metadata about a DAG and a Task.

This issue affects Apache Airflow 2.0.0.

### References
* https://lists.apache.org/thread.html/re21fec81baea7a6d73b0b5d31efd07cc02c61f832e297f65bb19b519%40%3Cusers.airflow.apache.org%3E


### Credits
* Apache Airflow would like to thank Ian Carroll for reporting this issue.


## Apache Airflow Reflected XSS via Origin Query Argument in URL ## { #CVE-2021-28359 }

CVE-2021-28359 [\[CVE json\]](./CVE-2021-28359.cve.json)

### Affected

* Apache Airflow at 2.0.0
* Apache Airflow at 2.0.1
* Apache Airflow from Apache Airflow before 1.10.15


### Description

The "origin" parameter passed to some of the endpoints like '/trigger' was vulnerable to XSS exploit. This issue affects Apache Airflow versions <1.10.15 in 1.x series and affects 2.0.0 and 2.0.1 and 2.x series.

This is the same as CVE-2020-13944 & CVE-2020-17515 but the implemented fix did not fix the issue completely. Update to Airflow 1.10.15 or 2.0.2.

Please also update your Python version to the latest available PATCH releases of the installed MINOR versions, example update to Python 3.6.13 if you are on Python 3.6. (Those contain the fix for CVE-2021-23336 https://nvd.nist.gov/vuln/detail/CVE-2021-23336).

### References
* https://lists.apache.org/thread.html/ra8ce70088ba291f358e077cafdb14d174b7a1ce9a9d86d1b332d6367%40%3Cusers.airflow.apache.org%3E


### Credits
* Vasileios Daskalakis


## No Authentication on Logging Server ## { #CVE-2021-35936 }

CVE-2021-35936 [\[CVE json\]](./CVE-2021-35936.cve.json)

### Affected

* Apache Airflow from Apache Airflow before 2.1.2


### Description

If remote logging is not used, the worker (in the case of CeleryExecutor) or the scheduler (in the case of LocalExecutor) runs a Flask logging server and is listening on a specific port and also binds on 0.0.0.0 by default.
This logging server had no authentication and allows reading log files of DAG jobs.

This issue affects Apache Airflow < 2.1.2.

### References
* https://lists.apache.org/thread.html/r53d6bd7b0a66f92ddaf1313282f10fec802e71246606dd30c16536df%40%3Cusers.airflow.apache.org%3E


### Credits
* Apache Airflow would like to thank Dolev Farhi for reporting this issue.


## Apache Airflow: Variable Import endpoint missed authentication check ## { #CVE-2021-38540 }

CVE-2021-38540 [\[CVE json\]](./CVE-2021-38540.cve.json)

### Affected

* Apache Airflow from Apache Airflow  before 2.1.3


### Description

The variable import endpoint was not protected by authentication in Airflow >=2.0.0, <2.1.3. This allowed unauthenticated users to hit that endpoint to add/modify Airflow variables used in DAGs, potentially
resulting in a denial of service, information disclosure or remote code execution.

This issue affects Apache Airflow >=2.0.0, <2.1.3.

### References
* https://lists.apache.org/thread.html/rb34c3dd1a815456355217eef34060789f771b6f77c3a3dec77de2064%40%3Cusers.airflow.apache.org%3E


### Credits
* Apache Airflow would like to thank Nathan Jones, National Australia Bank’s Offensive Security Team


## Apache Airflow: Reflected XSS via Origin Query Argument in URL ## { #CVE-2021-45229 }

CVE-2021-45229 [\[CVE json\]](./CVE-2021-45229.cve.json)

### Affected

* Apache Airflow from unspecified before 2.2.4


### Description

It was discovered that the "Trigger DAG with config" screen was susceptible to XSS attacks via the `origin` query argument.

This issue affects Apache Airflow versions 2.2.3 and below. 

### References
* https://lists.apache.org/thread/phx76cgtmhwwdy780rvwhobx8qoy4bnk


### Credits
* The Apache Airflow PMC would like to thank both Bogdan Kurinnoy of the Samsung R&D Institute Ukraine (SRK) and Ali Al-Habsi of Accellion for independently discovering and reporting this issue.


## Apache Airflow: Creating DagRuns didn't respect Dag-level permissions in the Webserver ## { #CVE-2021-45230 }

CVE-2021-45230 [\[CVE json\]](./CVE-2021-45230.cve.json)

### Affected

* Apache Airflow at Apache Airflow 1.10 1.10.0 to 1.10.15
* Apache Airflow from Apache Airflow 2 before 2.2.0


### Description

In Apache Airflow prior to 2.2.0.  This CVE applies to a specific case where a User who has "can_create" permissions on DAG Runs can create Dag Runs for dags that they don't have "edit" permissions for. 



### References
* https://lists.apache.org/thread/m778ojn0k595rwco4ht9wjql89mjoxnl


### Credits
* Apache Airflow PMC would like to thank Franco Cano Erazo for reporting this issue.


## Apache Airflow: RCE in example DAGs ## { #CVE-2022-24288 }

CVE-2022-24288 [\[CVE json\]](./CVE-2022-24288.cve.json)

### Affected

* Apache Airflow from unspecified before 2.2.4


### Description

In Apache Airflow, prior to version 2.2.4, some example DAGs did not properly sanitize user-provided params, making them susceptible to OS Command Injection from the web UI.

### References
* https://lists.apache.org/thread/dbw5ozcmr0h0lhs0yjph7xdc64oht23t


### Credits
* The Apache Airflow PMC would like to thank Kai Zhao of the TToU Security Team for reporting this issue.


## Apache Airflow prior to 2.3.1 may include sensitive values in rendered template ## { #CVE-2022-27949 }

CVE-2022-27949 [\[CVE json\]](./CVE-2022-27949.cve.json)

### Affected

* Apache Airflow from unspecified before 2.3.1


### Description

A vulnerability in UI of Apache Airflow allows an attacker to view unmasked secrets in rendered template values for tasks which were not executed (for example when they were depending on past and previous instances of the task failed). This issue affects Apache Airflow prior to 2.3.1.

### References
* https://github.com/apache/airflow/pull/22754
* https://lists.apache.org/thread/n38oc5obb48600fsvnbopxcs0jpbp65p


### Credits
* Apache Airflow PMC would like to thank James Srinivasan for reporting it.


## Session Fixation ## { #CVE-2022-38054 }

CVE-2022-38054 [\[CVE json\]](./CVE-2022-38054.cve.json)

### Affected

* Apache Airflow from 2.2.4 before Apache Airflow*


### Description

In Apache Airflow versions 2.2.4 through 2.3.3, the `database` webserver session backend was susceptible to session fixation.

### References
* https://lists.apache.org/thread/rsd3h89xdp16rg0ltovx3m7q3ypkxsbb


### Credits
* The Apache Airflow PMC would like to thank Kai Zhao for reporting this issue.
* Additoinally we would like to thank Ali Al-Habsi for independently discovering and reporting this issue.


## Overly permissive umask for daemons ## { #CVE-2022-38170 }

CVE-2022-38170 [\[CVE json\]](./CVE-2022-38170.cve.json)

### Affected

* Apache Airflow from Apache Airflow through 2.3.3


### Description

In Apache Airflow prior to 2.3.4, an insecure umask was configured for numerous Airflow components when running with the  `--daemon` flag which could result in a race condition giving world-writable files in the Airflow home directory and allowing local users to expose arbitrary file contents via the webserver.

### References
* https://lists.apache.org/thread/zn8mbbb1j2od5nc9zhrvb7rpsrg1vvzv


### Credits
* The Apache Airflow PMC would like to thank Harry Sintonen for reporting this issue.


## Docker Provider <3.0 RCE vulnerability in example dag ## { #CVE-2022-38362 }

CVE-2022-38362 [\[CVE json\]](./CVE-2022-38362.cve.json)

### Affected

* Apache Airflow from Apache Airflow Docker Provider before 3.0.0


### Description

Apache Airflow Docker's Provider prior to 3.0.0 shipped with an example DAG that was vulnerable to (authenticated) remote code exploit of code on the Airflow worker host.


### References
* https://lists.apache.org/thread/614p38nf4gbk8xhvnskj9b1sqo2dknkb


### Credits
* Thanks to Kai Zhao of 3H Secruity Team for reporting this


## Apache Airflow Pinot provider allowed Command Injection ## { #CVE-2022-38649 }

CVE-2022-38649 [\[CVE json\]](./CVE-2022-38649.cve.json)

### Affected

* Apache Airflow Pinot Provider from unspecified before 4.0.0
* Apache Airflow from unspecified before 2.3.0


### Description

Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Airflow Pinot Provider, Apache Airflow allows an attacker to control commands executed in the task execution context, without write access to DAG files. This issue affects Apache Airflow Pinot Provider versions prior to 4.0.0. It also impacts any Apache Airflow versions prior to 2.3.0 in case Apache Airflow Pinot Provider is installed (Apache Airflow Pinot Provider 4.0.0 can only be installed for Airflow 2.3.0+). Note that you need to manually install the Pinot Provider version 4.0.0 in order to get rid of the vulnerability on top of Airflow 2.3.0+ version.

### References
* https://github.com/apache/airflow/pull/27641
* https://lists.apache.org/thread/033o1gbc4ly6dpd2xf1o201v56fbl4dz


### Credits
* Apache Airflow PMC wants to thank id_No2015429 of 3H Security Team for reporting the issue.


## Apache Airflow <2.4.0 has an RCE in a bash example ## { #CVE-2022-40127 }

CVE-2022-40127 [\[CVE json\]](./CVE-2022-40127.cve.json)

### Affected

* Apache Airflow from Apache Airflow before 2.4.0


### Description

A vulnerability in Example Dags of Apache Airflow allows an attacker with UI access who can trigger DAGs, to execute arbitrary commands via manually provided run_id parameter.  This issue affects Apache Airflow Apache Airflow versions prior to 2.4.0.

### References
* https://github.com/apache/airflow/pull/25960
* https://lists.apache.org/thread/cf132hgm6jvzvsbpsozl3plf1r4cwysy


### Credits
* Apache Airflow PMC would like to thank L3yx of Syclover Security Team.


## Apache Airlfow Pig Provider RCE ## { #CVE-2022-40189 }

CVE-2022-40189 [\[CVE json\]](./CVE-2022-40189.cve.json)

### Affected

* Apache Airlfow Pig Provider from unspecified before 4.0.0
* Apache Airflow  from unspecified before 2.3.0


### Description

Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Airflow Pig Provider, Apache Airflow allows an attacker to control commands executed in the task execution context, without write access to DAG files. This issue affects Pig Provider versions prior to 4.0.0. It also impacts any Apache Airflow versions prior to 2.3.0 in case Pig Provider is installed (Pig Provider 4.0.0 can only be installed for Airflow 2.3.0+). Note that you need to manually install the Pig Provider version 4.0.0 in order to get rid of the vulnerability on top of Airflow 2.3.0+ version.

### References
* https://github.com/apache/airflow/pull/27644
* https://lists.apache.org/thread/yxnfzfw2w9pj5s785k3rlyly4y44sd15


### Credits
* Apache Airflow PMC wants to thank id_No2015429 of 3H Security Team for reporting the issue.


## Format String Vulnerability ## { #CVE-2022-40604 }

CVE-2022-40604 [\[CVE json\]](./CVE-2022-40604.cve.json)

### Affected

* Apache Airflow from unspecified before 2.4.0


### Description

In Apache Airflow 2.3.0 through 2.3.4, part of a url was unnecessarily formatted, allowing for possible information extraction.

### References
* https://github.com/apache/airflow/pull/26337
* https://lists.apache.org/thread/z20x8m16fnhxdkoollv53w1ybsts687t


### Credits
* The Apache Airflow PMC would like to thank L3yx of Syclover Security Team for reporting this issue.


## Open Redirect ## { #CVE-2022-40754 }

CVE-2022-40754 [\[CVE json\]](./CVE-2022-40754.cve.json)

### Affected

* Apache Airflow from unspecified before 2.4.0


### Description

In Apache Airflow 2.3.0 through 2.3.4, there was an open redirect in the webserver's `/confirm` endpoint.

### References
* https://github.com/apache/airflow/pull/26409
* https://lists.apache.org/thread/cn098dcp5x3c402xrb06p3l7nz5goffm


### Credits
* The Apache Airflow PMC would like to thank Konstantin Weddige (Lutra Security) for reporting this issue.


## Apache Airflow Spark Provider RCE that bypass restrictions to read arbitrary files ## { #CVE-2022-40954 }

CVE-2022-40954 [\[CVE json\]](./CVE-2022-40954.cve.json)

### Affected

* Apache Airflow Spark Provider from unspecified before 4.0.0
* Apache Airflow from unspecified before 2.3.0


### Description

Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Airflow Spark Provider, Apache Airflow allows an attacker to read arbtrary files in the task execution context, without write access to DAG files. This issue affects Spark Provider versions prior to 4.0.0. It also impacts any Apache Airflow versions prior to 2.3.0 in case Spark Provider is installed (Spark Provider 4.0.0 can only be installed for Airflow 2.3.0+). Note that you need to manually install the Spark Provider version 4.0.0 in order to get rid of the vulnerability on top of Airflow 2.3.0+ version that has lower version of the Spark Provider installed).

### References
* https://github.com/apache/airflow/pull/27646
* https://lists.apache.org/thread/0tmdlnmjs5t4gsx5fy73tb6zd3jztq45


### Credits
* Apache Airflow PMC wants to thank id_No2015429 of 3H Security Team for reporting the issue.


## Apache Airflow Hive Provider vulnerability (command injection via hive_cli connection) ## { #CVE-2022-41131 }

CVE-2022-41131 [\[CVE json\]](./CVE-2022-41131.cve.json)

### Affected

* Apache Airflow Hive Provider from unspecified before 4.1.0
* Apache Airflow at 2.3.0


### Description

Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in Apache Airflow Hive Provider, Apache Airflow allows an attacker to execute arbtrary commands in the task execution context, without write access to DAG files. This issue affects Hive Provider versions prior to 4.1.0. It also impacts any Apache Airflow versions prior to 2.3.0 in case HIve Provider is installed (Hive Provider 4.1.0 can only be installed for Airflow 2.3.0+). Note that you need to manually install the HIve Provider version 4.1.0 in order to get rid of the vulnerability on top of Airflow 2.3.0+ version that has lower version of the Hive Provider installed).


### References
* https://github.com/apache/airflow/pull/27647
* https://lists.apache.org/thread/wwo3qp0z8gv54yzn7hr04wy4n8gb0vhl


### Credits
* Apache Airflow PMC wants to thank id_No2015429 of 3H Security Team for reporting the issue.


## Session still functional after user is deactivated ## { #CVE-2022-41672 }

CVE-2022-41672 [\[CVE json\]](./CVE-2022-41672.cve.json)

### Affected

* Apache Airflow from unspecified through 2.4.0


### Description

In Apache Airflow, prior to version 2.4.1, deactivating a user wouldn't prevent an already authenticated user from being able to continue using the UI or API.

### References
* https://github.com/apache/airflow/pull/26635
* https://lists.apache.org/thread/ohf3pvd3dftb8zb01yngbn1jtkq5m08y


### Credits
* The Apache Airflow PMC would like to thank Axel Chong (@Haxatron) for reporting this issue.


## Apache Airflow prior to 2.4.2 allows reflected XSS via Origin Query Argument in URL ## { #CVE-2022-43982 }

CVE-2022-43982 [\[CVE json\]](./CVE-2022-43982.cve.json)

### Affected

* Apache Airflow from unspecified before 2.4.2


### Description

In Apache Airflow versions prior to 2.4.2, the "Trigger DAG with config" screen was susceptible to XSS attacks via the `origin` query argument.

### References
* https://github.com/apache/airflow/pull/27143
* https://lists.apache.org/thread/vqnvdrfsw9z7v7c46qh3psjgr7wy959l


### Credits
* The Apache Airflow PMC would like to thank id_No2015429 of 3H Security Team for reporting this issue.


## Apache Airflow prior to 2.4.2 has an open redirect ## { #CVE-2022-43985 }

CVE-2022-43985 [\[CVE json\]](./CVE-2022-43985.cve.json)

### Affected

* Apache Airflow from unspecified before 2.4.2


### Description

In Apache Airflow versions prior to 2.4.2, there was an open redirect in the webserver's `/confirm` endpoint.

### References
* https://github.com/apache/airflow/pull/27143
* https://lists.apache.org/thread/m13y9s5kw92fw9l8j4qd85h0txp4kfcq


### Credits
* The Apache Airflow PMC would like to thank Axel Chong (@Haxatron) [https://hackerone.com/haxatron1] for reporting this issue.


## Apache Airflow: Open redirect during login ## { #CVE-2022-45402 }

CVE-2022-45402 [\[CVE json\]](./CVE-2022-45402.cve.json)

### Affected

* Apache Airflow from unspecified before 2.4.3


### Description

In Apache Airflow versions prior to 2.4.3, there was an open redirect in the webserver's `/login` endpoint.

### References
* https://github.com/apache/airflow/pull/27576
* https://lists.apache.org/thread/nf4xrkoo6c81g6fdn4vj8k9x2686o9nh


### Credits
* The Apache Airflow PMC would like to thank Bugra Eskici for reporting this issue.


## Hive Provider RCE vulnerability with hive_cli_params ## { #CVE-2022-46421 }

CVE-2022-46421 [\[CVE json\]](./CVE-2022-46421.cve.json)

### Affected

* Apache Airflow Hive Provider before 5.0.0


### Description

Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<p>This issue affects Apache Airflow Hive Provider: before 5.0.0.</p>

### References
* https://github.com/apache/airflow/pull/28101
* https://lists.apache.org/thread/09twdoyoybldlfj5gvk0qswtofh0rmp4


### Credits
* id_No2015429 of 3H Security Team (finder)


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


### Credits
* Son Tran from VNPT - VCI (reporter)


## RCE Vulnerability ## { #CVE-2023-22886 }

CVE-2023-22886 [\[CVE json\]](./CVE-2023-22886.cve.json)

### Affected

* Apache Airflow JDBC Provider before 4.0.0


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow JDBC Provider.<br><span style="background-color: rgb(255, 255, 255);">Airflow JDBC Provider Connection’s [Connection URL] parameters had no</span><br><span style="background-color: rgb(255, 255, 255);">restrictions, which made it possible to implement RCE attacks via</span><br><span style="background-color: rgb(255, 255, 255);">different type JDBC drivers, obtain airflow server permission.</span><br><p>This issue affects Apache Airflow JDBC Provider: before 4.0.0.<br></p>

### References
* https://lists.apache.org/thread/ynbjwp4n0vzql0xzhog1gkp1ovncf8j3


### Credits
* heart Y (finder)
* happyhacking (finder)


## Apache Airflow path traversal by authenticated user ## { #CVE-2023-22887 }

CVE-2023-22887 [\[CVE json\]](./CVE-2023-22887.cve.json)

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows an attacker to perform unauthorized file access outside the intended directory structure by manipulating the run_id parameter. This vulnerability is considered low since it requires an authenticated user to exploit it. It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32293
* https://lists.apache.org/thread/rxddqs76r6rkxsg1n24d029zys67qwwo


### Credits
* Zhipeng Zhang (@Timon8) (finder)
* KietNA from National Cyber Security (NCS) (finder)


## Scheduler remote DoS ## { #CVE-2023-22888 }

CVE-2023-22888 [\[CVE json\]](./CVE-2023-22888.cve.json)

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows an attacker to cause a service disruption by manipulating the run_id parameter. This vulnerability is considered low since it requires an authenticated user to exploit it. It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32293
* https://lists.apache.org/thread/dnlht2hvm7k81k5tgjtsfmk27c76kq7z


### Credits
* Zhipeng Zhang (@timon8) (finder)


## Google Cloud Sql Provider Remote Command Execution ## { #CVE-2023-25691 }

CVE-2023-25691 [\[CVE json\]](./CVE-2023-25691.cve.json)

### Affected

* Apache Airflow Google Provider before 8.10.0


### Description

Improper Input Validation vulnerability in the Apache Airflow Google Provider.<br><br><p>This issue affects Apache Airflow Google Provider versions before 8.10.0.</p>

### References
* https://github.com/apache/airflow/pull/29497
* https://lists.apache.org/thread/zdr8ovfttbh7kj0lydgcw88tbt2nmkcy


### Credits
* Xie Jianming of Caiji Sec Team (finder)


## Google Cloud Sql Provider Denial Of Service ## { #CVE-2023-25692 }

CVE-2023-25692 [\[CVE json\]](./CVE-2023-25692.cve.json)

### Affected

* Apache Airflow Google Provider before 8.10.0


### Description

Improper Input Validation vulnerability in the Apache Airflow Google Provider.<br><br><p>This issue affects Apache Airflow Google Provider versions before 8.10.0.</p>

### References
* https://github.com/apache/airflow/pull/29499
* https://lists.apache.org/thread/ks4l78l5rwdpmvfn7y7yhs179nyxtlsh


### Credits
* Xie Jianming of Caiji Sec Team (finder)


## Sqoop Apache Airflow Provider Remote Code Execution Vulnerability ## { #CVE-2023-25693 }

CVE-2023-25693 [\[CVE json\]](./CVE-2023-25693.cve.json)

### Affected

* Apache Airflow Sqoop Provider before 3.1.1


### Description

Improper Input Validation vulnerability in the Apache Airflow Sqoop Provider.<br><br><p>This issue affects Apache Airflow Sqoop Provider versions before 3.1.1.</p>

### References
* https://github.com/apache/airflow/pull/29500
* https://lists.apache.org/thread/79qn8g5xbq036f8crb115obvr22l52q4


### Credits
*  L3yx of Syclover Security Team (finder)


## Information disclosure in Apache Airflow ## { #CVE-2023-25695 }

CVE-2023-25695 [\[CVE json\]](./CVE-2023-25695.cve.json)

### Affected

* Apache Airflow before 2.5.2


### Description

Generation of Error Message Containing Sensitive Information vulnerability in Apache Software Foundation Apache Airflow.<p>This issue affects Apache Airflow: before 2.5.2.</p>

### References
* https://github.com/apache/airflow/pull/29501
* https://lists.apache.org/thread/z8w6ckzs61ql365tv4d19k82o67r15p2


### Credits
* kuteminh11 (finder)


## Apache Airflow Hive Provider Beeline RCE ## { #CVE-2023-25696 }

CVE-2023-25696 [\[CVE json\]](./CVE-2023-25696.cve.json)

### Affected

* Apache Airflow Hive Provider before 5.1.3


### Description

Improper Input Validation vulnerability in the Apache Airflow Hive Provider.<br><br><p>This issue affects Apache Airflow Hive Provider versions before 5.1.3.</p>

### References
* https://github.com/apache/airflow/pull/29502
* https://lists.apache.org/thread/99g0qm56wmgdxmbtdsvhj4rdnxhpzpml


### Credits
* id_No2015429 of 3H Secruity Team (finder)


## Privilege escalation using airflow logs ## { #CVE-2023-25754 }

CVE-2023-25754 [\[CVE json\]](./CVE-2023-25754.cve.json)

### Affected

* Apache Airflow before 2.6.0


### Description

Privilege Context Switching Error vulnerability in Apache Software Foundation Apache Airflow.<p>This issue affects Apache Airflow: before 2.6.0.</p>

### References
* https://github.com/apache/airflow/pull/29506
* https://lists.apache.org/thread/3y83gr0qb8t49ppfk4fb2yk7md8ltq4v


### Credits
* ksw9722@naver.com (finder)


## Arbitrary file read via AWS provider ## { #CVE-2023-25956 }

CVE-2023-25956 [\[CVE json\]](./CVE-2023-25956.cve.json)

### Affected

* Apache Airflow AWS Provider before 7.2.1


### Description

Generation of Error Message Containing Sensitive Information vulnerability in the Apache Airflow AWS Provider.<br><br><p>This issue affects Apache Airflow AWS Provider versions before 7.2.1.</p>

### References
* https://github.com/apache/airflow/pull/29587
* https://lists.apache.org/thread/07pl9y4gdpw2c6rzqm77dvkm2z2kb5gv


### Credits
* Son Tran from VNPT - VCI (finder)
* kuteminh11 (finder)


## Airflow Sqoop Provider RCE Vulnerability ## { #CVE-2023-27604 }

CVE-2023-27604 [\[CVE json\]](./CVE-2023-27604.cve.json)

### Affected

* Apache Airflow Sqoop Provider before 4.0.0


### Description

Apache Airflow Sqoop Provider, versions before 4.0.0, is affected by a vulnerability that allows an attacker pass parameters with the connections, which makes it possible to implement RCE attacks via ‘sqoop import --connect’, obtain airflow server permissions, etc. T<span style="background-color: rgb(255, 255, 255);">he attacker needs to be logged in and have authorization (permissions) to create/edit connections.<br></span><br> It is recommended to upgrade to a version that is not affected.<br>This issue was reported independently by <span style="background-color: rgb(255, 255, 255);">happyhacking-k</span>, And Xie Jianming and LiuHui of Caiji Sec Team also reported it.

### References
* https://github.com/apache/airflow/pull/33039
* https://lists.apache.org/thread/lswlxf11do51ob7f6xyyg8qp3n7wdrgd


### Credits
* happyhacking-k (finder)
* Xie Jianming of Caiji Sec Team (finder)
* Liu Hui of Caiji Sec Team (finder)


## Apache Airflow Hive Provider Beeline Remote Command Execution ## { #CVE-2023-28706 }

CVE-2023-28706 [\[CVE json\]](./CVE-2023-28706.cve.json)

### Affected

* Apache Airflow Hive Provider before 6.0.0


### Description

Improper Control of Generation of Code ('Code Injection') vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<p>This issue affects Apache Airflow Hive Provider: before 6.0.0.</p>

### References
* https://github.com/apache/airflow/pull/30212
* https://lists.apache.org/thread/dl20xxd51xvlx0zzc0wzgxfjwgtbbxo3


### Credits
* sw0rd1ight of Caiji Sec Team and 4ra1n of Chaitin Tech (finder)


## Airflow Apache Drill Provider Arbitrary File Read Vulnerability ## { #CVE-2023-28707 }

CVE-2023-28707 [\[CVE json\]](./CVE-2023-28707.cve.json)

### Affected

* Apache Airflow Drill Provider before 2.3.2


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Drill Provider.<p>This issue affects Apache Airflow Drill Provider: before 2.3.2.</p>

### References
* https://github.com/apache/airflow/pull/30215
* https://lists.apache.org/thread/dfoj7q1nd0vhhsl8fjg63z4j6mfmdxtk


### Credits
* Kai Zhao of 3H Secruity Team (finder)


## Apache Airflow Spark Provider Arbitrary File Read via JDBC ## { #CVE-2023-28710 }

CVE-2023-28710 [\[CVE json\]](./CVE-2023-28710.cve.json)

### Affected

* Apache Airflow Spark Provider before 4.0.1


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Spark Provider.<p>This issue affects Apache Airflow Spark Provider: before 4.0.1.</p>

### References
* https://github.com/apache/airflow/pull/30223
* https://lists.apache.org/thread/lb9w9114ow00h2nkn8bjm106v5x1p1d2


### Credits
* Xie Jianming of  Nsfocus (finder)


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


### Credits
* taidh from VNPT - VCI (finder)
* kuteminh11 (finder)


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


### Credits
* KmhlYXJ0 (finder)


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


### Credits
* Piotr Chomiak from Astro product security team (finder)


## Apache Airflow Hive Provider Beeline RCE with Principal ## { #CVE-2023-35797 }

CVE-2023-35797 [\[CVE json\]](./CVE-2023-35797.cve.json)

### Affected

* Apache Airflow Apache Hive Provider before 6.1.1


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<br><p>This issue affects Apache Airflow Apache Hive Provider: before 6.1.1.<br><br><span style="background-color: rgb(255, 255, 255);">Before version 6.1.1 it was&nbsp;</span><span style="background-color: rgb(255, 255, 255);">possible to bypass the security check to RCE via</span><br><span style="background-color: rgb(255, 255, 255);">principal parameter. For this to be&nbsp;<span style="background-color: rgb(255, 255, 255);">exploited it requires access to modifying the connection details.</span><br></span><br>It is recommended updating provider version to 6.1.1 in order to avoid this&nbsp;vulnerability.</p>

### References
* https://github.com/apache/airflow/pull/31983
* https://lists.apache.org/thread/30y19ok07fw52x5hnkbhwqo3ho0wwc1y


### Credits
* id_No2015429 of 3H Secruity Team (reporter)


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


### Credits
* id_No2015429 of 3H Secruity Team (finder)


## Access to DAGs without relevant permission ## { #CVE-2023-35908 }

CVE-2023-35908 [\[CVE json\]](./CVE-2023-35908.cve.json)

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows unauthorized read access to a DAG through the URL.&nbsp;It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32014
* https://lists.apache.org/thread/vsflptk5dt30vrfggn96nx87d7zr6yvw


### Credits
* Name : Karthikeyan Singaravelan  Employer : Visa (finder)


## ReDoS via dags function ## { #CVE-2023-36543 }

CVE-2023-36543 [\[CVE json\]](./CVE-2023-36543.cve.json)

### Affected

* Apache Airflow before 2.6.3


### Description

Apache Airflow, versions before 2.6.3, has a vulnerability where an authenticated user can use crafted input to make the current request hang.&nbsp;It is recommended to upgrade to a version that is not affected

### References
* https://github.com/apache/airflow/pull/32060
* https://lists.apache.org/thread/tokfs980504ylgk3cv3hjlnrtbv4tng4


### Credits
* National Cyber Security VietNam (NCS VietNam) (finder)
* hungtd (finder)


## Exposure of sensitive connection information, DOS and SSRF on "test connection" feature ## { #CVE-2023-37379 }

CVE-2023-37379 [\[CVE json\]](./CVE-2023-37379.cve.json)

### Affected

* Apache Airflow before 2.7.0


### Description

<p>Apache Airflow, in versions prior to 2.7.0, contains a security vulnerability that can be exploited by an authenticated user possessing Connection edit privileges. This vulnerability allows the user to access connection information and exploit the test connection feature by sending many requests, leading to a denial of service (DoS) condition on the server. Furthermore, malicious actors can leverage this vulnerability to establish harmful connections with the server.</p><p>Users of Apache Airflow are strongly advised to upgrade to version 2.7.0 or newer to mitigate the risk associated with this vulnerability. Additionally, administrators are encouraged to review and adjust user permissions to restrict access to sensitive functionalities, reducing the attack surface.</p><br>

### References
* https://github.com/apache/airflow/pull/32052
* https://lists.apache.org/thread/g5c9vcn27lr14go48thrjpo6f4vw571r


### Credits
* kuteminh11 (finder)
* khoabda of Zalo Security Team (finder)
* Sayooj B Kumar(Team bi0s & CRED Security team) (finder)
* Son Tran from VNPT - VCI (finder)
* KmhlYXJ0 (finder)


## Improper Input Validation in Hive Provider with proxy_user ## { #CVE-2023-37415 }

CVE-2023-37415 [\[CVE json\]](./CVE-2023-37415.cve.json)

### Affected

* Apache Airflow Apache Hive Provider before 6.1.2


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Apache Hive Provider.<br><br>Patching on top of CVE-2023-35797<br><p>Before&nbsp;6.1.2<span style="background-color: rgb(255, 255, 255);">&nbsp;the proxy_user option can also inject semicolon.<br></span><br>This issue affects Apache Airflow Apache Hive Provider: before 6.1.2.<br><br></p><p>It is recommended updating provider version to 6.1.2 in order to avoid this vulnerability.</p><p></p>

### References
* https://lists.apache.org/thread/9wx0jlckbnycjh8nj5qfwxo423zvm41k


### Credits
* Son Tran from VNPT - VCI (reporter)


## SMTP/IMAP client components allowed MITM due to missing Certificate Validation ## { #CVE-2023-39441 }

CVE-2023-39441 [\[CVE json\]](./CVE-2023-39441.cve.json)

### Affected

* Apache Airflow SMTP Provider before 1.30
* Apache Airflow IMAP Provider before 3.3.0
* Apache Airflow before 2.7.0


### Description

<span style="background-color: rgb(255, 255, 255);">Apache Airflow SMTP Provider </span><span style="background-color: rgb(255, 255, 255);">before 1.3.0</span><span style="background-color: rgb(255, 255, 255);">, Apache Airflow IMAP Provider </span><span style="background-color: rgb(255, 255, 255);">before 3.3.0, and</span><span style="background-color: rgb(255, 255, 255);">&nbsp;Apache Airflow </span><span style="background-color: rgb(255, 255, 255);">before 2.7.0 are affected by the&nbsp;</span>Validation of OpenSSL Certificate vulnerability.<br><br><span style="background-color: rgb(255, 255, 255);">The default SSL context with SSL library did not check a server's X.509&nbsp;</span><span style="background-color: rgb(255, 255, 255);">certificate.&nbsp; Instead, the code accepted any certificate, which could&nbsp;</span><span style="background-color: rgb(255, 255, 255);">result in the disclosure of mail server credentials or mail contents&nbsp;</span><span style="background-color: rgb(255, 255, 255);">when the client connects to an attacker in a MITM position.<br><br></span><span style="background-color: var(--wht);">Users are strongly advised to upgrade to Apache Airflow version 2.7.0 or newer, Apache Airflow IMAP Provider version 3.3.0 or newer, and Apache Airflow SMTP Provider version 1.3.0 or newer to mitigate the risk associated with this vulnerability</span>

### References
* https://github.com/apache/airflow/pull/33075
* https://github.com/apache/airflow/pull/33108
* https://github.com/apache/airflow/pull/33070
* https://lists.apache.org/thread/xzp4wgjg2b1o6ylk2595df8bstlbo1lb


### Credits
* Martin Schobert, Pentagrid AG (finder)


## Airflow "Run task" feature allows execution with unnecessary priviledges ## { #CVE-2023-39508 }

CVE-2023-39508 [\[CVE json\]](./CVE-2023-39508.cve.json)

### Affected

* Apache Airflow before 2.6.0


### Description

Execution with Unnecessary Privileges, : Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Software Foundation Apache Airflow.<p>The "Run Task" feature enables authenticated user to bypass some of the restrictions put in place. It allows to execute code in the webserver context as well as allows to bypas limitation of access the user has to certain DAGs. The "Run Task" feature is considered dangerous and it has been removed entirely in Airflow 2.6.0<br></p><p>This issue affects Apache Airflow: before 2.6.0.</p>

### References
* https://github.com/apache/airflow/pull/29706
* https://lists.apache.org/thread/j2nkjd0zqvtqk85s6ywpx3c35pvzyx15


### Credits
* balis0ng (finder)


## Apache Airflow Drill Provider Arbitrary File Read Vulnerability ## { #CVE-2023-39553 }

CVE-2023-39553 [\[CVE json\]](./CVE-2023-39553.cve.json)

### Affected

* Apache Airflow Drill Provider before 2.4.3


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Drill Provider.<br><br><span style="background-color: rgb(255, 255, 255);">Apache Airflow Drill Provider is affected by a vulnerability that allows an attacker to pass in malicious parameters when establishing a connection with DrillHook giving an opportunity to read files on the Airflow server.</span><br><p>This issue affects Apache Airflow Drill Provider: before 2.4.3.<br><span style="background-color: rgb(255, 255, 255);">It is recommended to upgrade to a version that is not affected.</span><br></p>

### References
* https://github.com/apache/airflow/pull/33074
* https://lists.apache.org/thread/ozpl0opmob49rkcz8svo8wkxyw1395sf


### Credits
* sw0rd1ight of Caiji Sec Team and 4ra1n of Chaitin Tech (finder)
* happyhacking (finder)


## Apache Airflow Spark Provider Deserialization Vulnerability RCE ## { #CVE-2023-40195 }

CVE-2023-40195 [\[CVE json\]](./CVE-2023-40195.cve.json)

### Affected

* Apache Airflow Spark Provider before 4.1.3


### Description

Deserialization of Untrusted Data, Inclusion of Functionality from Untrusted Control Sphere vulnerability in Apache Software Foundation Apache Airflow Spark Provider.<br><br><br><span style="background-color: rgb(255, 255, 255);">When the Apache Spark provider is installed on an Airflow deployment, an Airflow user that is authorized to configure Spark hooks can effectively run arbitrary code on the Airflow node by pointing it at a malicious Spark server. Prior to version 4.1.3, this was not called out in the documentation explicitly, so it is possible that administrators provided authorizations to configure Spark hooks without taking this into account. We recommend administrators to review their configurations to make sure the authorization to configure Spark hooks is only provided to fully trusted users.<br><br>To view the warning in the docs please visit&nbsp;<a target="_blank" rel="nofollow" href="https://airflow.apache.org/docs/apache-airflow-providers-apache-spark/4.1.3/connections/spark.html">https://airflow.apache.org/docs/apache-airflow-providers-apache-spark/4.1.3/connections/spark.html</a><br><br><br></span>

### References
* https://github.com/apache/airflow/pull/33233
* https://lists.apache.org/thread/fzy95b1d6zv31j5wrx3znhzcscck2o24


### Credits
* happyhacking-k (finder)


## Apache Airflow Spark Provider Arbitrary File Read via JDBC ## { #CVE-2023-40272 }

CVE-2023-40272 [\[CVE json\]](./CVE-2023-40272.cve.json)

### Affected

* Apache Airflow Spark Provider before 4.1.3


### Description

<p>Apache Airflow Spark Provider, versions before 4.1.3, is affected by a vulnerability that allows an attacker to pass in malicious parameters when establishing a connection giving an opportunity to read files on the Airflow server.<br>It is recommended to upgrade to a version that is not affected.</p><p></p>

### References
* https://lists.apache.org/thread/t03gktyzyor20rh06okd91jtqmw6k1l7


### Credits
* sw0rd1ight (finder)


## Session fixation in Apache Airflow web interface ## { #CVE-2023-40273 }

CVE-2023-40273 [\[CVE json\]](./CVE-2023-40273.cve.json)

### Affected

* Apache Airflow before 2.7.0


### Description

<p>The session fixation vulnerability allowed the authenticated user to continue accessing Airflow webserver even after the password of the user has been reset by the admin - up until the expiry of the session of the user. Other than manually cleaning the session database (for <code>database</code>&nbsp;session backend), or changing the secure_key and restarting the webserver, there were no mechanisms to force-logout the user (and all other users with that).</p><p>With this fix implemented, when using the&nbsp;<code>database</code>&nbsp;session backend, the existing sessions of the user are invalidated when the password of the user is reset. When using the <code>securecookie</code>&nbsp;session backend, the sessions are NOT invalidated and still require changing the secure key and restarting the webserver (and logging out all other users), but the user resetting the password is informed about it with a flash message warning displayed in the UI. Documentation is also updated explaining this behaviour.</p>Users of Apache Airflow are advised to upgrade to version 2.7.0 or newer to mitigate the risk associated with this vulnerability.<br>

### References
* https://github.com/apache/airflow/pull/33347
* https://lists.apache.org/thread/9rdmv8ln4y4ncbyrlmjrsj903x4l80nj
* https://www.openwall.com/lists/oss-security/2023/08/23/1


### Credits
* Yusuf AYDIN (@h1_yusuf) (finder)
* L3yx of Syclover Security Team. (finder)
* Son Tran of VNPT-VCI (finder)
* Thuong Nguyen (@nthuong95) (finder)


## Apache Airflow Dag Runs Broken Access Control Vulnerability ## { #CVE-2023-40611 }

CVE-2023-40611 [\[CVE json\]](./CVE-2023-40611.cve.json)

### Affected

* Apache Airflow before 2.7.1


### Description

Apache Airflow, versions before 2.7.1, is affected by a vulnerability that allows&nbsp;authenticated and DAG-view authorized Users to modify some DAG run detail values when submitting notes. This could have them alter details such as configuration parameters, start date, etc.<br><br>Users should upgrade to version 2.7.1 or later which has removed the vulnerability.<br>

### References
* https://github.com/apache/airflow/pull/33413
* https://lists.apache.org/thread/8y9xk1s3j4qr36yzqn8ogbn9fl7pxrn0


### Credits
* happyhacking (finder)


## Secrets can be unmasked in the "Rendered Template"  ## { #CVE-2023-40712 }

CVE-2023-40712 [\[CVE json\]](./CVE-2023-40712.cve.json)

### Affected

* Apache Airflow before 2.7.1


### Description

Apache Airflow, versions before 2.7.1, is affected by a vulnerability that allows authenticated&nbsp;users who have access to see the task/dag in the UI, to craft a URL, which could lead to unmasking the secret configuration of the task that otherwise would be masked in the UI.<br><br>Users are strongly advised to upgrade to&nbsp;version 2.7.1 or later which has removed the vulnerability.

### References
* https://github.com/apache/airflow/pull/33512
* https://github.com/apache/airflow/pull/33516
* https://lists.apache.org/thread/jw1yv4lt6hpowqbb0x4o3tdp0jhx2bts


### Credits
* klexadoc (finder)


## Apache HDFS Provider error message suggested installation of incorrect pip package ## { #CVE-2023-41267 }

CVE-2023-41267 [\[CVE json\]](./CVE-2023-41267.cve.json)

### Affected

* Apache Airflow HDFS Provider before 4.1.1


### Description

<span style="background-color: rgb(255, 255, 255);">In the Apache Airflow HDFS Provider, versions prior to 4.1.1, a documentation&nbsp;info pointed users to an install incorrect pip package. As this package name was unclaimed, in theory, an attacker could claim this package and provide code that would be executed when this package was installed. The Airflow team has since taken ownership of the package (neutralizing the risk), and fixed the doc strings in version 4.1.1</span><br>

### References
* https://github.com/apache/airflow/pull/33813
* https://lists.apache.org/thread/ggthr5pn42bn6wcr25hxnykjzh4ntw7z


### Credits
* AnupamAs01 (finder)


## Bypass permission verification to view task instances of other dags ## { #CVE-2023-42663 }

CVE-2023-42663 [\[CVE json\]](./CVE-2023-42663.cve.json)

### Affected

* Apache Airflow before 2.7.2


### Description

<p>Apache Airflow, versions before 2.7.2, has a vulnerability that allows an authorized user who has access to read specific DAGs only, to read information about task instances in other DAGs.<br>Users of Apache Airflow are advised to upgrade to version 2.7.2 or newer to mitigate the risk associated with this vulnerability.<br></p>

### References
* https://github.com/apache/airflow/pull/34315
* https://lists.apache.org/thread/xj86cvfkxgd0cyqfmz6mh1bsfc61c6o9


### Credits
* balis0ng (finder)
* Ephraim Anierobi (remediation developer)


## Improper access control vulnerability in the "List dag warnings" feature ## { #CVE-2023-42780 }

CVE-2023-42780 [\[CVE json\]](./CVE-2023-42780.cve.json)

### Affected

* Apache Airflow before 2.7.2


### Description

Apache Airflow, versions prior to 2.7.2, contains a security vulnerability that allows authenticated users of Airflow to list warnings for all DAGs, even if the user had no permission to see those DAGs. It would reveal the dag_ids and the stack-traces of import errors for those DAGs with import errors.<br>Users of Apache Airflow are advised to upgrade to version 2.7.2 or newer to mitigate the risk associated with this vulnerability.<br><br>

### References
* https://github.com/apache/airflow/pull/34355
* https://lists.apache.org/thread/h5tvsvov8j55wojt5sojdprs05oby34d


### Credits
* balis0ng (finder)
* Hussein Awala (remediation developer)


## Permission verification bypass allows viewing dagruns of other dags ## { #CVE-2023-42781 }

CVE-2023-42781 [\[CVE json\]](./CVE-2023-42781.cve.json)

### Affected

* Apache Airflow before 2.7.3


### Description

Apache Airflow, versions before 2.7.3, has a vulnerability that allows an authorized user who has access to read specific DAGs only, to read information about task instances in other DAGs.&nbsp; This is a different issue than CVE-2023-42663 but leading to similar outcome.<br>Users of Apache Airflow are advised to upgrade to version 2.7.3 or newer to mitigate the risk associated with this vulnerability.

### References
* https://github.com/apache/airflow/pull/34939
* https://lists.apache.org/thread/7dnl8nszdxqyns57f3dw0sloy5dfl9o1


### Credits
* balis0ng (finder)
* Hussein Awala (remediation developer)


## Improper access control to DAG resources ## { #CVE-2023-42792 }

CVE-2023-42792 [\[CVE json\]](./CVE-2023-42792.cve.json)

### Affected

* Apache Airflow before 2.7.2


### Description

Apache Airflow, in versions prior to 2.7.2, contains a security vulnerability that allows an authenticated user with limited access to some DAGs, to craft a request that could give the user write access to various DAG resources for DAGs that the user had no access to, thus, enabling the user to clear DAGs they shouldn't.<br><br>Users of Apache Airflow are strongly advised to upgrade to version 2.7.2 or newer to mitigate the risk associated with this vulnerability.<br>

### References
* https://github.com/apache/airflow/pull/34366
* https://lists.apache.org/thread/1spbo9nkn49fc2hnxqm9tf6mgqwp9tjq


### Credits
* balis0ng (finder)
* Jarek Potiuk (remediation developer)


## Configuration information leakage vulnerability ## { #CVE-2023-45348 }

CVE-2023-45348 [\[CVE json\]](./CVE-2023-45348.cve.json)

### Affected

* Apache Airflow from 2.7.0 before 2.7.2


### Description



Apache Airflow, versions 2.7.0 and 2.7.1, is affected by a vulnerability that allows an authenticated user to retrieve sensitive configuration information when the "expose_config" option is set to "non-sensitive-only". The `expose_config` option is False by default.<br>It is recommended to upgrade to a version that is not affected.

### References
* https://github.com/apache/airflow/pull/34712
* https://lists.apache.org/thread/sy4l5d6tn58hr8r61r2fkt1f0qock9z9


### Credits
* L3yx of Syclover Security Team (finder)
* Hussein Awala (remediation developer)


## Sensitive information logged as clear text when rediss, amqp, rpc protocols are used as Celery result backend ## { #CVE-2023-46215 }

CVE-2023-46215 [\[CVE json\]](./CVE-2023-46215.cve.json)

### Affected

* Apache Airflow Celery provider from 3.3.0 through 3.4.0
* Apache Airflow from 1.10.0 before 2.7.0


### Description

Insertion of Sensitive Information into Log File vulnerability in Apache Airflow Celery provider, Apache Airflow.<br><br><p>Sensitive information logged as clear text when rediss, amqp, rpc protocols are used as Celery result backend<br>Note: the&nbsp;vulnerability is about the information exposed in the logs not about accessing the logs.</p><p>This issue affects Apache Airflow Celery provider: from 3.3.0 through 3.4.0; Apache Airflow: from 1.10.0 through 2.6.3.</p><p>Users are recommended to upgrade Airflow Celery provider to version 3.4.1&nbsp;and Apache Airlfow to version 2.7.0 which fixes the issue.</p>

### References
* https://github.com/apache/airflow/pull/34954
* https://lists.apache.org/thread/wm1jfmks7r6m7bj0mq4lmw3998svn46n


### Credits
* husseinawala (finder)


## Sensitive parameters exposed in API when "non-sensitive-only" configuration is set ## { #CVE-2023-46288 }

CVE-2023-46288 [\[CVE json\]](./CVE-2023-46288.cve.json)

### Affected

* Apache Airflow from 2.4.0 before 2.7.0


### Description

Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Airflow.<p>This issue affects Apache Airflow from 2.4.0 to 2.7.0.</p><p>Sensitive configuration information has been exposed to authenticated users with the ability to read configuration via Airflow REST API for configuration even when the <code>expose_config</code>&nbsp;option is set to <code>non-sensitive-only</code>. The expose_config option is False by default. It is recommended to upgrade to a version that is not affected if you set <code>expose_config</code>&nbsp;to <code>non-sensitive-only</code>&nbsp;configuration. This is a different error than CVE-2023-45348&nbsp;which allows authenticated user to retrieve individual configuration values in 2.7.* by specially crafting their request (solved in 2.7.2).</p><p>Users are recommended to upgrade to version 2.7.2, which fixes the issue and additionally fixes&nbsp;CVE-2023-45348.</p>

### References
* https://github.com/apache/airflow/pull/32261
* https://lists.apache.org/thread/yw4vzm0c5lqkwm0bxv6qy03yfd1od4nw


### Credits
* id_No2015429 of 3H Secruity Team (finder)
* Lee, Wei (finder)
* Lee, Wei (remediation developer)


## Apache Airflow missing fix for CVE-2023-40611 in 2.7.1 (DAG run broken access) ## { #CVE-2023-47037 }

CVE-2023-47037 [\[CVE json\]](./CVE-2023-47037.cve.json)

### Affected

* Apache Airflow before 2.7.3


### Description

<p><span style="background-color: rgb(255, 255, 255);">We failed to apply&nbsp;CVE-2023-40611 in 2.7.1 and this vulnerability was marked as fixed then.&nbsp;</span></p><p><span style="background-color: rgb(255, 255, 255);">Apache Airflow, versions before 2.7.3, is affected by a vulnerability that allows authenticated and DAG-view authorized Users to modify some DAG run detail values when submitting notes. This could have them alter details such as configuration parameters, start date, etc.&nbsp;</span></p><p><span style="background-color: rgb(255, 255, 255);">Users should upgrade to version 2.7.3 or later which has removed the vulnerability.</span><br></p><br><br>

### References
* https://github.com/apache/airflow/pull/33413
* https://lists.apache.org/thread/04y4vrw1t2xl030gswtctc4nt1w90cb0


### Credits
* Tareq Ahamed from Hackerone (reporter)
*  Augusto Hidalgo (remediation developer)


## DAG Params alllow to embed unchecked Javascript ## { #CVE-2023-47265 }

CVE-2023-47265 [\[CVE json\]](./CVE-2023-47265.cve.json)

### Affected

* Apache Airflow from 2.6.0 before 2.8.0


### Description

Apache Airflow, versions 2.6.0 through 2.7.3 has a stored XSS vulnerability that allows a DAG author to add an unbounded and not-sanitized javascript in the parameter description field of the DAG.&nbsp;This Javascript can be executed on the client side of any of the user who looks at the tasks in the browser sandbox. While this issue does not allow to exit the browser sandbox or manipulation of the server-side data - more than the DAG author already has, it allows to modify what the user looking at the DAG details sees in the browser - which opens up all kinds of possibilities of misleading other users.<br><br>Users of Apache Airflow are recommended to upgrade to version 2.8.0 or newer to mitigate the risk associated with this vulnerability<br>

### References
* https://github.com/apache/airflow/pull/35460
* https://lists.apache.org/thread/128f3zl375vb1qv93k82zhnwkpl233pr


### Credits
* Jens Scheffler (finder)
* Andrey Anshin (finder)
* Jens Scheffler (remediation developer)


## Improper access control to DAG resources ## { #CVE-2023-48291 }

CVE-2023-48291 [\[CVE json\]](./CVE-2023-48291.cve.json)

### Affected

* Apache Airflow before 2.8.0


### Description

Apache Airflow, in versions prior to 2.8.0, contains a security vulnerability that allows an authenticated user with limited access to some DAGs, to craft a request that could give the user write access to various DAG resources for DAGs that the user had no access to, thus, enabling the user to clear DAGs they shouldn't.<br><br>This is a missing fix for CVE-2023-42792 in Apache Airflow 2.7.2&nbsp;<br><br>Users of Apache Airflow are strongly advised to upgrade to version 2.8.0 or newer to mitigate the risk associated with this vulnerability.

### References
* https://github.com/apache/airflow/pull/34366
* https://lists.apache.org/thread/3nl0h014274yjlt1hd02z0q78ftyz0z3


### Credits
* balis0ng (finder)
* Jarek Potiuk (remediation developer)


## Missing CSRF protection on DAG/trigger ## { #CVE-2023-49920 }

CVE-2023-49920 [\[CVE json\]](./CVE-2023-49920.cve.json)

### Affected

* Apache Airflow from 2.7.0 before 2.8.0


### Description

Apache Airflow, version 2.7.0 through 2.7.3, has a vulnerability that allows an attacker to trigger a DAG in a GET request without CSRF validation.&nbsp;As a result, it was possible for a malicious website opened in the same browser - by the user who also had Airflow UI opened - to trigger the execution of DAGs without the user's consent.<br>Users are advised to upgrade to version 2.8.0 or later which is not affected

### References
* https://github.com/apache/airflow/pull/36026
* https://lists.apache.org/thread/mnwd2vcfw3gms6ft6kl951vfbqrxsnjq


### Credits
* Tareq Ahamed ( 0xt4req) (finder)
* Jens Scheffler (remediation developer)


## Improper access control vulnerability on the "varimport" endpoint ## { #CVE-2023-50783 }

CVE-2023-50783 [\[CVE json\]](./CVE-2023-50783.cve.json)

### Affected

* Apache Airflow before 2.8.0


### Description

Apache Airflow, versions before 2.8.0, is affected by a vulnerability that allows an authenticated user without the variable edit permission, to update a variable.<br>This flaw compromises the integrity of variable management, potentially leading to unauthorized data modification.<br>Users are recommended to upgrade to 2.8.0, which fixes this issue

### References
* https://github.com/apache/airflow/pull/33932
* https://lists.apache.org/thread/rs7cr3yp726mb89s1m844hy9pq7frgcn


### Credits
* balis0ng (finder)
* Ephraim Anierobi (remediation developer)


## Potential pickle deserialization vulnerability in XComs ## { #CVE-2023-50943 }

CVE-2023-50943 [\[CVE json\]](./CVE-2023-50943.cve.json)

### Affected

* Apache Airflow before 2.8.1


### Description

Apache Airflow, versions before 2.8.1, have a vulnerability that allows a potential attacker to poison the XCom data by bypassing the protection of "enable_xcom_pickling=False" configuration setting resulting in poisoned data after XCom deserialization. This vulnerability is considered low since it requires a DAG author to exploit it. Users are recommended to upgrade to version 2.8.1 or later, which fixes this issue.<br>

### References
* https://github.com/apache/airflow/pull/36255
* https://lists.apache.org/thread/fx278v0twqzxkcts70tc04cp3f8p56pn


### Credits
* Peng Zhou (zpbrent@gmail.com) (finder)
* Hussein Awala (remediation developer)


## Bypass permission verification to read code of other dags ## { #CVE-2023-50944 }

CVE-2023-50944 [\[CVE json\]](./CVE-2023-50944.cve.json)

### Affected

* Apache Airflow before 2.8.1


### Description

Apache Airflow, versions before 2.8.1, have a vulnerability that allows an authenticated user to access the source code of a DAG to which they don't have access.&nbsp;This vulnerability is considered low since it requires an authenticated user to exploit it. Users are recommended to upgrade to version 2.8.1, which fixes this issue.<br>

### References
* https://github.com/apache/airflow/pull/36257
* https://lists.apache.org/thread/92krb5mpcq8qrw4t4j5oooqw7hgd8q7h


### Credits
* Timon8 Zhang (finder)


## Kubernetes configuration file saved without encryption in the Metadata and logged as plain text in the Triggerer service ## { #CVE-2023-51702 }

CVE-2023-51702 [\[CVE json\]](./CVE-2023-51702.cve.json)

### Affected

* Apache Airflow CNCF Kubernetes provider from 5.2.0 before 7.0.0
* Apache Airflow from 2.3.0 before 2.6.1


### Description

Since version 5.2.0, when using deferrable mode with the path of a Kubernetes configuration file for authentication, the Airflow worker serializes this configuration file as a dictionary and sends it to the triggerer by storing it in metadata without any encryption. Additionally, if used with an Airflow version between 2.3.0 and 2.6.0, the configuration dictionary will be logged as plain text in the triggerer service without masking. This allows anyone with access to the metadata or triggerer log to obtain the configuration file and use it to access the Kubernetes cluster.<br><br>This behavior was changed in version 7.0.0, which stopped serializing the file contents and started providing the file path instead to read the contents into the trigger. Users are recommended to upgrade to version 7.0.0, which fixes this issue.

### References
* https://github.com/apache/airflow/pull/29498
* https://github.com/apache/airflow/pull/30110
* https://github.com/apache/airflow/pull/36492
* https://lists.apache.org/thread/89x3q6lz5pykrkr1fkr04k4rfn9pvnv9


### Credits
* Hussein Awala (finder)
* Hussein Awala (remediation developer)
