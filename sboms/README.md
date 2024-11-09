Apache Software Foundation produced SBOMs
=========================================

| TLP                                                                 | Ecosystems | Build tools | SBOM Tools | Comments
| ------------------------------------------------------------------- | -------    | ------      | -----      | -----
| [Airflow](https://projects.apache.org/committee.html?airflow)       | PyPI, npm   | pip, npm     | cdxgen     | [SBOMs](https://airflow.apache.org/docs/apache-airflow/stable/security/sbom.html)
| [Arrow](https://projects.apache.org/committee.html?arrow)           | Maven Central, ... | Maven, ... | CycloneDX Maven Plugin | Go? Python?
| [Avro](https://projects.apache.org/committee.html?avro)             | Maven Central, ... | Maven, ... | CycloneDX Maven Plugin | Python, C/C++/C#, PHP, Ruby, Rust, JavaScript, and even Perl
| [Camel](https://projects.apache.org/committee.html?camel)           | Maven Central | Maven | CycloneDX Maven Plugin |
| [Commons](https://projects.apache.org/committee.html?commons)       | Maven Central | Maven | CycloneDX Maven Plugin, SPDX Maven Plugin |
| [CXF](https://projects.apache.org/committee.html?cxf)               | Maven Central | Maven | CycloneDX Maven Plugin |
| [Directory](https://projects.apache.org/committee.html?directory)   | Maven Central | Maven | CycloneDX Maven Plugin |
| [Druid](https://projects.apache.org/committee.html?druid)           | Maven Central | Maven | CycloneDX Maven Plugin |
| [Flink](https://projects.apache.org/committee.html?flink)           | Maven Central | Maven, ... | CycloneDX Maven Plugin | Docker, K8S Operator
| [Groovy](https://projects.apache.org/committee.html?groovy)         | Maven Central | Gradle | CycloneDX Gradle Plugin |
| [Hadoop](https://projects.apache.org/committee.html?hadoop)         | Maven Central | Maven | CycloneDX Maven Plugin |
| [HBase](https://projects.apache.org/committee.html?hbase)           | Maven Central | Maven | CycloneDX Maven Plugin |
| [Hop](https://projects.apache.org/committee.html?hop)               | Maven Central | Maven | CycloneDX Maven Plugin |
| [Jena](https://projects.apache.org/committee.html?jena)             | Maven Central | Maven | CycloneDX Maven Plugin |
| [JSPWiki](https://projects.apache.org/committee.html?jspwiki)       | Maven Central | Maven | CycloneDX Maven Plugin |
| [Logging](https://projects.apache.org/committee.html?logging)       | Maven Central | Maven, ... | CycloneDX Maven Plugin | C++, .Net, PHP? [VDR](https://logging.apache.org/cyclonedx/vdr.xml)
| [Maven](https://projects.apache.org/committee.html?maven)           | Maven Central | Maven | CycloneDX Maven Plugin |
| [Orc](https://projects.apache.org/committee.html?orc)               | Maven Central | Maven, ... | CycloneDX Maven Plugin | Conan, Docker
| [Parquet](https://projects.apache.org/committee.html?parquet)       | Maven Central | Maven, ... | CycloneDX Maven Plugin | C++, Rust
| [Pekko](https://projects.apache.org/committee.html?pekko)           | Maven Central | Sbt | ? | 
| [Ratis](https://projects.apache.org/committee.html?ratis)           | Maven Central | Maven | CycloneDX Maven Plugin |
| [Santuario](https://projects.apache.org/committee.html?santuario)   | Maven Central | Maven, ... | CycloneDX Maven Plugin | C++?
| [Skywalking](https://projects.apache.org/committee.html?skywalking) | Maven Central | Maven, ... | CycloneDX Maven Plugin | Docker, Helm, npm, Rust, ...
| [Spark](https://projects.apache.org/committee.html?spark)           | Maven Central, PyPI | Maven, pip, ... | CycloneDX Maven Plugin | Python? K8S Operator?
| [Syncope](https://projects.apache.org/committee.html?syncope)       | Maven Central | Maven | CycloneDX Maven Plugin |
| [Turbine](https://projects.apache.org/committee.html?turbine)       | Maven Central | Maven | CycloneDX Maven Plugin |
| [Zookeeper](https://projects.apache.org/committee.html?zookeeper)   | Maven Central | Maven | CycloneDX Maven Plugin |

<!-- below generated: do not edit, it will be overridden -->

## Airflow
- 2.9.1: [1 SBOM](airflow/airflow-2.9.1.md)
- 2.9.3: [21 SBOMs](airflow/airflow-2.9.3.md)
- 2.10.0: [21 SBOMs](airflow/airflow-2.10.0.md)
- 2.10.2: [21 SBOMs](airflow/airflow-2.10.2.md)

## Arrow
- 11.0.0: [1 SBOM](arrow/arrow-11.0.0.md)
- 15.0.2: [1 SBOM](arrow/arrow-15.0.2.md)
- 16.1.0: [17 SBOMs](arrow/arrow-16.1.0.md)
- 17.0.0: [26 SBOMs](arrow/arrow-17.0.0.md)
- 18.0.0: [23 SBOMs](arrow/arrow-18.0.0.md)

## Avro
- 1.11.3: [18 SBOMs](avro/avro-1.11.3.md)
- 1.12.0: [24 SBOMs](avro/avro-1.12.0.md)

## Camel
- 3.12.0: [1 SBOM](camel/camel-3.12.0.md)
- 3.13.0: [1 SBOM](camel/camel-3.13.0.md)
- 3.14.0: [1 SBOM](camel/camel-3.14.0.md)
- 3.15.0: [1 SBOM](camel/camel-3.15.0.md)
- 4.0.5: [1 SBOM](camel/camel-4.0.5.md)
- 4.0.6: [1 SBOM](camel/camel-4.0.6.md)
- 4.4.2: [1 SBOM](camel/camel-4.4.2.md)
- 4.4.3: [1 SBOM](camel/camel-4.4.3.md)
- 4.4.4: [1 SBOM](camel/camel-4.4.4.md)
- 4.6.0: [4 SBOMs](camel/camel-4.6.0.md)
- 4.7.0: [3 SBOMs](camel/camel-4.7.0.md)
- 4.8.0: [2 SBOMs](camel/camel-4.8.0.md)
- 4.8.1: [1 SBOM](camel/camel-4.8.1.md)

## Commons
### Commons IO
- 2.17.0: [1 SBOM](commons/commons-io-2.17.0.md)

### BCEL
- 6.10.0: [1 SBOM](commons/bcel-6.10.0.md)

### Commons Compress
- 1.26.1: [1 SBOM](commons/commons-compress-1.26.1.md)
- 1.26.2: [1 SBOM](commons/commons-compress-1.26.2.md)
- 1.27.1: [1 SBOM](commons/commons-compress-1.27.1.md)

### Commons Configuration 2
- 2.10.1: [1 SBOM](commons/commons-configuration2-2.10.1.md)
- 2.11.0: [1 SBOM](commons/commons-configuration2-2.11.0.md)

### Commons Crypto
- 1.2.0: [1 SBOM](commons/commons-crypto-1.2.0.md)

### Commons CSV
- 1.11.0: [1 SBOM](commons/commons-csv-1.11.0.md)
- 1.12.0: [1 SBOM](commons/commons-csv-1.12.0.md)

### Commons DBCP 2
- 2.12.0: [1 SBOM](commons/commons-dbcp2-2.12.0.md)

### Commons Email
- 1.6.0: [1 SBOM](commons/commons-email-1.6.0.md)

### Commons Exec
- 1.4.0: [1 SBOM](commons/commons-exec-1.4.0.md)

### Commons Imaging
- 1.0.0-alpha5: [1 SBOM](commons/commons-imaging-1.0.0-alpha5.md)

### Commons JCS 3
- 3.2: [6 SBOMs](commons/commons-jcs3-3.2.md)
- 3.2.1: [6 SBOMs](commons/commons-jcs3-3.2.1.md)

### Commons JEXL 3
- 3.3: [1 SBOM](commons/commons-jexl3-3.3.md)
- 3.4.0: [1 SBOM](commons/commons-jexl3-3.4.0.md)

### Commons Lang 3
- 3.14.0: [1 SBOM](commons/commons-lang3-3.14.0.md)
- 3.15.0: [1 SBOM](commons/commons-lang3-3.15.0.md)
- 3.16.0: [1 SBOM](commons/commons-lang3-3.16.0.md)
- 3.17.0: [1 SBOM](commons/commons-lang3-3.17.0.md)

### Commons Math 4
- 4.0-beta1: [7 SBOMs](commons/commons-math-4.0-beta1.md)

### Commons Parent
- 70: [1 SBOM](commons/commons-parent-70.md)
- 72: [1 SBOM](commons/commons-parent-72.md)
- 74: [1 SBOM](commons/commons-parent-74.md)
- 77: [1 SBOM](commons/commons-parent-77.md)
- 78: [1 SBOM](commons/commons-parent-78.md)

### Commons Pool 2
- 2.12.0: [1 SBOM](commons/commons-pool2-2.12.0.md)

### Commons Release Plugin
- 1.8.2: [1 SBOM](commons/commons-release-plugin-1.8.2.md)

### Commons RNG
- 1.6: [5 SBOMs](commons/commons-rng-1.6.md)

### Commons Statistics
- 1.1: [5 SBOMs](commons/commons-statistics-1.1.md)

### Commons Text
- 1.12.0: [1 SBOM](commons/commons-text-1.12.0.md)

## CXF
- 2.3.0: [1 SBOM](cxf/cxf-2.3.0.md)
- 3.5.9: [1 SBOM](cxf/cxf-3.5.9.md)
- 3.6.4: [15 SBOMs](cxf/cxf-3.6.4.md)
- 4.0.5: [191 SBOMs](cxf/cxf-4.0.5.md)

## Directory
### Directory
- 2.1.7: [33 SBOMs](directory/directory-2.1.7.md)

### Kerby
- 2.1.0: [44 SBOMs](directory/kerby-2.1.0.md)

## Druid
- 28.0.1: [1 SBOM](druid/druid-28.0.1.md)
- 29.0.1: [10 SBOMs](druid/druid-29.0.1.md)
- 30.0.0: [10 SBOMs](druid/druid-30.0.0.md)
- 31.0.0: [79 SBOMs](druid/druid-31.0.0.md)

## Flink
- 1.6.1: [1 SBOM](flink/flink-1.6.1.md)
- 1.8.0: [3 SBOMs](flink/flink-1.8.0.md)
- 1.9.0: [8 SBOMs](flink/flink-1.9.0.md)
- 1.10.0: [8 SBOMs](flink/flink-1.10.0.md)
- 1.17.2: [3 SBOMs](flink/flink-1.17.2.md)
- 1.19.0: [7 SBOMs](flink/flink-1.19.0.md)
- 1.19.1: [127 SBOMs](flink/flink-1.19.1.md)
- 1.20.0: [132 SBOMs](flink/flink-1.20.0.md)
- 2.2.0: [10 SBOMs](flink/flink-2.2.0.md)
- 2.3.0: [36 SBOMs](flink/flink-2.3.0.md)

## Groovy
- 5.0.0-alpha-9: [33 SBOMs](groovy/groovy-5.0.0-alpha-9.md)

## Hadoop
- 3.4.1: [105 SBOMs](hadoop/hadoop-3.4.1.md)

## HBase
- 2.5.8: [3 SBOMs](hbase/hbase-2.5.8.md)
- 2.6.0: [5 SBOMs](hbase/hbase-2.6.0.md)
- 2.6.1: [5 SBOMs](hbase/hbase-2.6.1.md)
- 3.0.0-beta-1: [50 SBOMs](hbase/hbase-3.0.0-beta-1.md)

## Hop
- 2.10.0: [290 SBOMs](hop/hop-2.10.0.md)

## Jena
- 5.0.0: [42 SBOMs](jena/jena-5.0.0.md)
- 5.1.0: [43 SBOMs](jena/jena-5.1.0.md)
- 5.2.0: [48 SBOMs](jena/jena-5.2.0.md)

## JSPWiki
- 2.12.2: [35 SBOMs](jspwiki/jspwiki-2.12.2.md)

## Logging
- 0.9.0: [8 SBOMs](logging/log4j-0.9.0.md)
- 1.4.0: [2 SBOMs](logging/log4j-1.4.0.md)
- 1.5.0: [2 SBOMs](logging/log4j-1.5.0.md)
- 2.22.0: [2 SBOMs](logging/log4j-2.22.0.md)
- 2.23.1: [3 SBOMs](logging/log4j-2.23.1.md)
- 2.24.1: [30 SBOMs](logging/log4j-2.24.1.md)
- 3.0.0-beta1: [4 SBOMs](logging/log4j-3.0.0-beta1.md)
- 3.0.0-beta2: [35 SBOMs](logging/log4j-3.0.0-beta2.md)
- 13.1.0: [6 SBOMs](logging/log4j-13.1.0.md)

## Maven
### Maven
- 4.0.0-beta-5: [34 SBOMs](maven/maven-4.0.0-beta-5.md)

### Maven Archetype
- 3.3.1: [7 SBOMs](maven/maven-archetype-3.3.1.md)

### Maven Archetype Bundles
- 1.5: [11 SBOMs](maven/maven-archetypes-1.5.md)

### Doxia
- 2.0.0: [15 SBOMs](maven/doxia-2.0.0.md)
- 43: [1 SBOM](maven/doxia-43.md)

### Maven Enforcer
- 3.5.0: [5 SBOMs](maven/maven-enforcer-3.5.0.md)

### Maven Build Cache Extension
- 1.2.0: [1 SBOM](maven/maven-build-cache-extension-1.2.0.md)

### Maven Extensions Parent
- 43: [1 SBOM](maven/maven-extensions-43.md)

### Maven Indexer
- 7.1.5: [8 SBOMs](maven/maven-indexer-7.1.5.md)

### Maven JXR
- 3.6.0: [3 SBOMs](maven/maven-jxr-3.6.0.md)

### Maven Plugin Testing
- 4.0.0-beta-1: [2 SBOMs](maven/maven-plugin-testing-4.0.0-beta-1.md)

### Maven Plugin Tools
- 3.15.1: [8 SBOMs](maven/maven-plugin-tools-3.15.1.md)
- 4.0.0-beta-1: [6 SBOMs](maven/maven-plugin-tools-4.0.0-beta-1.md)

### Maven Artifact Plugin
- 3.5.2: [1 SBOM](maven/maven-artifact-plugin-3.5.2.md)

### Maven Assembly Plugin
- 3.7.1: [1 SBOM](maven/maven-assembly-plugin-3.7.1.md)

### Maven Checkstyle Plugin
- 3.6.0: [1 SBOM](maven/maven-checkstyle-plugin-3.6.0.md)

### Maven Clean Plugin
- 4.0.0-beta-1: [1 SBOM](maven/maven-clean-plugin-4.0.0-beta-1.md)

### Maven Compiler Plugin
- 4.0.0-beta-1: [1 SBOM](maven/maven-compiler-plugin-4.0.0-beta-1.md)

### Maven Dependency Plugin
- 3.8.1: [1 SBOM](maven/maven-dependency-plugin-3.8.1.md)

### Maven Deploy Plugin
- 4.0.0-beta-1: [1 SBOM](maven/maven-deploy-plugin-4.0.0-beta-1.md)

### Maven GPG Plugin
- 3.2.7: [1 SBOM](maven/maven-gpg-plugin-3.2.7.md)

### Maven Help Plugin
- 3.5.1: [1 SBOM](maven/maven-help-plugin-3.5.1.md)

### Maven Install Plugin
- 4.0.0-beta-1: [1 SBOM](maven/maven-install-plugin-4.0.0-beta-1.md)

### Maven Invoker Plugin
- 3.8.1: [1 SBOM](maven/maven-invoker-plugin-3.8.1.md)

### Maven Jar Plugin
- 4.0.0-beta-1: [1 SBOM](maven/maven-jar-plugin-4.0.0-beta-1.md)

### Maven Jarsigner Plugin
- 3.1.0: [1 SBOM](maven/maven-jarsigner-plugin-3.1.0.md)

### Maven Javadoc Plugin
- 3.10.1: [1 SBOM](maven/maven-javadoc-plugin-3.10.1.md)

### Maven JLink Plugin
- 3.2.0: [1 SBOM](maven/maven-jlink-plugin-3.2.0.md)

### Maven Plugins Parent
- 43: [1 SBOM](maven/maven-plugins-43.md)

### Maven PMD Plugin
- 3.26.0: [1 SBOM](maven/maven-pmd-plugin-3.26.0.md)

### Maven Project Info Reports Plugin
- 3.8.0: [1 SBOM](maven/maven-project-info-reports-plugin-3.8.0.md)

### Maven Remote Resources Plugin
- 3.2.0: [1 SBOM](maven/maven-remote-resources-plugin-3.2.0.md)

### Maven Resources Plugin
- 4.0.0-beta-1: [1 SBOM](maven/maven-resources-plugin-4.0.0-beta-1.md)

### Maven SCM Publish Plugin
- 3.3.0: [1 SBOM](maven/maven-scm-publish-plugin-3.3.0.md)

### Maven Shade Plugin
- 3.6.0: [1 SBOM](maven/maven-shade-plugin-3.6.0.md)

### Maven Site Plugin
- 3.21.0: [1 SBOM](maven/maven-site-plugin-3.21.0.md)

### Maven Source Plugin
- 4.0.0-beta-1: [1 SBOM](maven/maven-source-plugin-4.0.0-beta-1.md)

### Maven Toolchains Plugin
- 3.2.0: [1 SBOM](maven/maven-toolchains-plugin-3.2.0.md)

### Maven Release
- 3.1.1: [5 SBOMs](maven/maven-release-3.1.1.md)

### Maven Reporting API
- 4.0.0: [1 SBOM](maven/maven-reporting-api-4.0.0.md)

### Maven Reporting Exec
- 2.0.0: [1 SBOM](maven/maven-reporting-exec-2.0.0.md)

### Maven Reporting Implementation
- 4.0.0: [1 SBOM](maven/maven-reporting-impl-4.0.0.md)

### Maven Resolver
- 1.5.1: [1 SBOM](maven/maven-resolver-1.5.1.md)
- 2.0.0-alpha-2: [2 SBOMs](maven/maven-resolver-2.0.0-alpha-2.md)
- 2.0.0-alpha-8: [2 SBOMs](maven/maven-resolver-2.0.0-alpha-8.md)
- 2.0.2: [26 SBOMs](maven/maven-resolver-2.0.2.md)

### Maven SCM
- 2.1.0: [19 SBOMs](maven/maven-scm-2.1.0.md)

### Maven Archiver
- 3.6.2: [1 SBOM](maven/maven-archiver-3.6.2.md)
- 4.0.0-beta-1: [1 SBOM](maven/maven-archiver-4.0.0-beta-1.md)

### Maven Common Artifact Filters
- 3.4.0: [1 SBOM](maven/maven-common-artifact-filters-3.4.0.md)

### Maven Dependency Analyzer
- 1.15.1: [1 SBOM](maven/maven-dependency-analyzer-1.15.1.md)

### Maven Dependency Tree
- 3.3.0: [1 SBOM](maven/maven-dependency-tree-3.3.0.md)

### Maven Filtering
- 4.0.0-beta-1: [1 SBOM](maven/maven-filtering-4.0.0-beta-1.md)

### Maven Invoker
- 3.3.0: [1 SBOM](maven/maven-invoker-3.3.0.md)

### Maven Jarsigner
- 3.1.0: [1 SBOM](maven/maven-jarsigner-3.1.0.md)

### Maven Script Interpreter
- 1.6: [1 SBOM](maven/maven-script-interpreter-1.6.md)

### Maven Shared Parent
- 43: [1 SBOM](maven/maven-shared-components-43.md)

### Maven Shared Jar
- 3.1.1: [1 SBOM](maven/maven-shared-jar-3.1.1.md)

### Maven Shared Resources
- 6: [1 SBOM](maven/maven-shared-resources-6.md)

### Maven Skins Parent
- 43: [1 SBOM](maven/maven-skins-43.md)

### Maven Surefire
- 3.5.1: [25 SBOMs](maven/maven-surefire-3.5.1.md)

### Maven Wrapper
- 3.3.2: [3 SBOMs](maven/maven-wrapper-3.3.2.md)

## Orc
- 1.0.0: [1 SBOM](orc/orc-1.0.0.md)
- 1.9.3: [1 SBOM](orc/orc-1.9.3.md)
- 1.9.4: [1 SBOM](orc/orc-1.9.4.md)
- 2.0.1: [4 SBOMs](orc/orc-2.0.1.md)
- 2.0.2: [5 SBOMs](orc/orc-2.0.2.md)

## Parquet
- 1.14.0: [17 SBOMs](parquet/parquet-1.14.0.md)
- 1.14.1: [17 SBOMs](parquet/parquet-1.14.1.md)
- 1.14.2: [17 SBOMs](parquet/parquet-1.14.2.md)
- 1.14.3: [18 SBOMs](parquet/parquet-1.14.3.md)

## Pekko
- 1.1.2: [84 SBOMs](pekko/pekko-1.1.2.md)

## Ratis
- 3.1.1: [19 SBOMs](ratis/ratis-3.1.1.md)

## Santuario
- 4.0.2: [1 SBOM](santuario/santuario-4.0.2.md)

## Skywalking
- 10.1.0: [91 SBOMs](skywalking/skywalking-10.1.0.md)

## Spark
- 3.5.1: [72 SBOMs](spark/spark-3.5.1.md)
- 3.5.2: [72 SBOMs](spark/spark-3.5.2.md)

## Syncope
- 3.0.6: [8 SBOMs](syncope/syncope-3.0.6.md)
- 3.0.7: [8 SBOMs](syncope/syncope-3.0.7.md)
- 3.0.8: [8 SBOMs](syncope/syncope-3.0.8.md)

## Turbine
### Turbine
- 6.0: [1 SBOM](turbine/turbine-6.0.md)
- 13: [1 SBOM](turbine/turbine-13.md)

### Fulcrum
- 2.0.1: [2 SBOMs](turbine/fulcrum-2.0.1.md)
- 3.0.0: [7 SBOMs](turbine/fulcrum-3.0.0.md)

## Zookeeper
- 3.9.2: [9 SBOMs](zookeeper/zookeeper-3.9.2.md)

