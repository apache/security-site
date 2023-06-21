---
title: Apache Airflow security advisories
description: Security information for Apache Airflow
layout: single
---

# Reporting

Do you want disclose a potential security issue for Apache Airflow? Send your report to the  [Apache Security Team](mailto:security@apache.org).

# Advisories

## Hive Provider RCE vulnerability with hive_cli_params ## { #CVE-2022-46421 }

[CVE-2022-46421](./CVE-2022-46421.cve.json)

### Affected

* Apache Airflow Hive Provider versions  before 5.0.0


### Description

Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<p>This issue affects Apache Airflow Hive Provider: before 5.0.0.</p>

## Arbitrary file read via MySQL provider in Apache Airflow ## { #CVE-2023-22884 }

[CVE-2023-22884](./CVE-2023-22884.cve.json)

### Affected

* Apache Airflow versions  before 2.5.1
* Apache Airflow MySQL Provider versions  before 4.0.0


### Description

Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache Airflow, Apache Software Foundation Apache Airflow MySQL Provider.<p>This issue affects Apache Airflow: before 2.5.1; Apache Airflow MySQL Provider: before 4.0.0.</p>

## Google Cloud Sql Provider Remote Command Execution ## { #CVE-2023-25691 }

[CVE-2023-25691](./CVE-2023-25691.cve.json)

### Affected

* Apache Airflow Google Provider versions  before 8.10.0


### Description

Improper Input Validation vulnerability in the Apache Airflow Google Provider.<br><br><p>This issue affects Apache Airflow Google Provider versions before 8.10.0.</p>

## Google Cloud Sql Provider Denial Of Service ## { #CVE-2023-25692 }

[CVE-2023-25692](./CVE-2023-25692.cve.json)

### Affected

* Apache Airflow Google Provider versions  before 8.10.0


### Description

Improper Input Validation vulnerability in the Apache Airflow Google Provider.<br><br><p>This issue affects Apache Airflow Google Provider versions before 8.10.0.</p>

## Sqoop Apache Airflow Provider Remote Code Execution Vulnerability ## { #CVE-2023-25693 }

[CVE-2023-25693](./CVE-2023-25693.cve.json)

### Affected

* Apache Airflow Sqoop Provider versions  before 3.1.1


### Description

Improper Input Validation vulnerability in the Apache Airflow Sqoop Provider.<br><br><p>This issue affects Apache Airflow Sqoop Provider versions before 3.1.1.</p>

## Information disclosure in Apache Airflow ## { #CVE-2023-25695 }

[CVE-2023-25695](./CVE-2023-25695.cve.json)

### Affected

* Apache Airflow versions  before 2.5.2


### Description

Generation of Error Message Containing Sensitive Information vulnerability in Apache Software Foundation Apache Airflow.<p>This issue affects Apache Airflow: before 2.5.2.</p>

## Apache Airflow Hive Provider Beeline RCE ## { #CVE-2023-25696 }

[CVE-2023-25696](./CVE-2023-25696.cve.json)

### Affected

* Apache Airflow Hive Provider versions  before 5.1.3


### Description

Improper Input Validation vulnerability in the Apache Airflow Hive Provider.<br><br><p>This issue affects Apache Airflow Hive Provider versions before 5.1.3.</p>

## Privilege escalation using airflow logs ## { #CVE-2023-25754 }

[CVE-2023-25754](./CVE-2023-25754.cve.json)

### Affected

* Apache Airflow versions  before 2.6.0


### Description

Privilege Context Switching Error vulnerability in Apache Software Foundation Apache Airflow.<p>This issue affects Apache Airflow: before 2.6.0.</p>

## Arbitrary file read via AWS provider ## { #CVE-2023-25956 }

[CVE-2023-25956](./CVE-2023-25956.cve.json)

### Affected

* Apache Airflow AWS Provider versions  before 7.2.1


### Description

Generation of Error Message Containing Sensitive Information vulnerability in the Apache Airflow AWS Provider.<br><br><p>This issue affects Apache Airflow AWS Provider versions before 7.2.1.</p>

## Apache Airflow Hive Provider Beeline Remote Command Execution ## { #CVE-2023-28706 }

[CVE-2023-28706](./CVE-2023-28706.cve.json)

### Affected

* Apache Airflow Hive Provider versions  before 6.0.0


### Description

Improper Control of Generation of Code ('Code Injection') vulnerability in Apache Software Foundation Apache Airflow Hive Provider.<p>This issue affects Apache Airflow Hive Provider: before 6.0.0.</p>

## Airflow Apache Drill Provider Arbitrary File Read Vulnerability ## { #CVE-2023-28707 }

[CVE-2023-28707](./CVE-2023-28707.cve.json)

### Affected

* Apache Airflow Drill Provider versions  before 2.3.2


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Drill Provider.<p>This issue affects Apache Airflow Drill Provider: before 2.3.2.</p>

## Apache Airflow Spark Provider Arbitrary File Read via JDBC ## { #CVE-2023-28710 }

[CVE-2023-28710](./CVE-2023-28710.cve.json)

### Affected

* Apache Airflow Spark Provider versions  before 4.0.1


### Description

Improper Input Validation vulnerability in Apache Software Foundation Apache Airflow Spark Provider.<p>This issue affects Apache Airflow Spark Provider: before 4.0.1.</p>

## Stored XSS on Apache Airflow ## { #CVE-2023-29247 }

[CVE-2023-29247](./CVE-2023-29247.cve.json)

### Affected

* Apache Airflow versions  before 2.6.0


### Description

Task instance details page in the UI is vulnerable to a stored XSS.<p>This issue affects Apache Airflow: before 2.6.0.</p><br>

## KubernetesPodOperator RCE via connection configuration ## { #CVE-2023-33234 }

[CVE-2023-33234](./CVE-2023-33234.cve.json)

### Affected

* Apache Airflow CNCF Kubernetes Provider versions 5.0.0 including 6.1.0


### Description

Arbitrary code execution in Apache Airflow CNCF Kubernetes provider version 5.0.0 allows user to change xcom sidecar image and resources via Airflow connection.<br><br>In order to exploit this weakness, a user would already need elevated permissions (Op or Admin) to change the connection object in this manner.&nbsp; Operators should upgrade to provider version 7.0.0 which has removed the vulnerability.<br><br>

## Information disclosure on configuration view ## { #CVE-2023-35005 }

[CVE-2023-35005](./CVE-2023-35005.cve.json)

### Affected

* Apache Airflow versions 2.5.0 before 2.6.2


### Description

<div>In Apache Airflow, some potentially sensitive values were being shown to the user in certain situations.</div><div>This vulnerability is mitigated by the fact configuration is not shown in the UI by default (only if `[webserver] expose_config` is set to `non-sensitive-only`), and not all uncensored values are actually sentitive.</div><br><div>This issue affects Apache Airflow: from 2.5.0 before 2.6.2. Users are recommended to update to version 2.6.2 or later.<br></div>