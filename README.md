# ASF SBOM Collection

This repository contains a collection of SBOMs published by ASF projects,
copied and consolidated to provide a series of tools analyzing them:
- [Apache Ecosystem Graph](https://sbom.security.apache.org/),
- [ASF Dependency Version Diff](https://sbom.security.apache.org/version-diff/),
- [OWASP Dependency Track](https://security-tools-ec2-va.apache.org/),
- ...

## What is a Software Bill of Materials (SBOM)?

See [SECURITY/SBOM Software Bill of Materials](https://cwiki.apache.org/confluence/display/SECURITY/SBOM+Software+Bill+of+Materials)
for a quick background on what SBOMs are and how they're produced and
used across the ASF.

## What Projects are Involved?

| TLP                                                                                                               | SBOMs                               | Build       | SBOM Tools | Comments
| ------------------------------------------------------------------------------------------------------------------| ----------------------------------- | ----------- | ---------- | --------
| [Airflow](https://airflow.apache.org/)       [:clipboard:](https://projects.apache.org/committee.html?airflow)    | [:mag:](sboms/README.md#airflow)    | pip<br>npm | cdxgen     | [SBOMs publication](https://airflow.apache.org/docs/apache-airflow/stable/security/sbom.html)
| [Arrow](https://arrow.apache.org/)           [:clipboard:](https://projects.apache.org/committee.html?arrow)      | [:mag:](sboms/README.md#arrow)      | Maven<br>... | CDX Maven P | Go? Python?
| [Avro](https://avro.apache.org/)             [:clipboard:](https://projects.apache.org/committee.html?avro)       | [:mag:](sboms/README.md#avro)       | Maven<br>... | CDX Maven P | Python, C/C++/C#, PHP, ...
| [Camel](https://camel.apache.org/)           [:clipboard:](https://projects.apache.org/committee.html?camel)      | [:mag:](sboms/README.md#camel)      | Maven     | CDX Maven P |
| [Commons](https://commons.apache.org/)       [:clipboard:](https://projects.apache.org/committee.html?commons)    | [:mag:](sboms/README.md#commons)    | Maven     | CDX Maven P<br>SPDX&nbsp;Maven&nbsp;P |
| [CXF](https://cxf.apache.org/)               [:clipboard:](https://projects.apache.org/committee.html?cxf)        | [:mag:](sboms/README.md#cxf)        | Maven     | CDX Maven P |
| [Directory](https://directory.apache.org/)   [:clipboard:](https://projects.apache.org/committee.html?directory)  | [:mag:](sboms/README.md#directory)  | Maven     | CDX Maven P |
| [Druid](https://druid.apache.org/)           [:clipboard:](https://projects.apache.org/committee.html?druid)      | [:mag:](sboms/README.md#druid)      | Maven     | CDX Maven P |
| [Flink](https://flink.apache.org/)           [:clipboard:](https://projects.apache.org/committee.html?flink)      | [:mag:](sboms/README.md#flink)      | Maven<br>... | CDX Maven P | Docker, K8S Operator
| [Groovy](https://groovy.apache.org/)         [:clipboard:](https://projects.apache.org/committee.html?groovy)     | [:mag:](sboms/README.md#groovy)     | Gradle    | CDX Gradle P |
| [Hadoop](https://hadoop.apache.org/)         [:clipboard:](https://projects.apache.org/committee.html?hadoop)     | [:mag:](sboms/README.md#hadoop)     | Maven     | CDX Maven P |
| [HBase](https://hbase.apache.org/)           [:clipboard:](https://projects.apache.org/committee.html?hbase)      | [:mag:](sboms/README.md#hbase)      | Maven     | CDX Maven P |
| [Hop](https://hop.apache.org/)               [:clipboard:](https://projects.apache.org/committee.html?hop)        | [:mag:](sboms/README.md#hop)        | Maven     | CDX Maven P |
| [Jena ](https://jena.apache.org/)            [:clipboard:](https://projects.apache.org/committee.html?jena)       | [:mag:](sboms/README.md#jena)       | Maven     | CDX Maven P |
| [JSPWiki](https://jspwiki.apache.org/)       [:clipboard:](https://projects.apache.org/committee.html?jspwiki)    | [:mag:](sboms/README.md#jspwiki)    | Maven     | CDX Maven P |
| [Logging](https://logging.apache.org/)       [:clipboard:](https://projects.apache.org/committee.html?logging)    | [:mag:](sboms/README.md#logging)    | Maven<br>... | CDX Maven P | C++, .Net, PHP? [VDR](https://logging.apache.org/CDX/vdr.xml)
| [Maven](https://maven.apache.org/)           [:clipboard:](https://projects.apache.org/committee.html?maven)      | [:mag:](sboms/README.md#maven)      | Maven     | CDX Maven P |
| [Orc](https://orc.apache.org/)               [:clipboard:](https://projects.apache.org/committee.html?orc)        | [:mag:](sboms/README.md#orc)        | Maven<br>... | CDX Maven P | Conan, Docker
| [Parquet](https://parquet.apache.org/)       [:clipboard:](https://projects.apache.org/committee.html?parquet)    | [:mag:](sboms/README.md#parquet)    | Maven<br>... | CDX Maven P | C++, Rust
| [Pekko](https://pekko.apache.org/)           [:clipboard:](https://projects.apache.org/committee.html?pekko)      | [:mag:](sboms/README.md#pekko)      | Sbt       | ? | 
| [Ratis](https://ratis.apache.org/)           [:clipboard:](https://projects.apache.org/committee.html?ratis)      | [:mag:](sboms/README.md#ratis)      | Maven     | CDX Maven P |
| [Santuario](https://santuario.apache.org/)   [:clipboard:](https://projects.apache.org/committee.html?santuario)  | [:mag:](sboms/README.md#santuario)  | Maven<br>... | CDX Maven P | C++?
| [Skywalking](https://skywalking.apache.org/) [:clipboard:](https://projects.apache.org/committee.html?skywalking) | [:mag:](sboms/README.md#skywalking) | Maven<br>... | CDX Maven P | Docker, Helm, npm, Rust, ...
| [Spark](https://spark.apache.org/)           [:clipboard:](https://projects.apache.org/committee.html?spark)      | [:mag:](sboms/README.md#spark)      | Maven<br>pip<br>... | CDX Maven P | Python? K8S Operator?
| [Syncope](https://syncope.apache.org/)       [:clipboard:](https://projects.apache.org/committee.html?syncope)    | [:mag:](sboms/README.md#syncope)    | Maven     | CDX Maven P |
| [Turbine](https://turbine.apache.org/)       [:clipboard:](https://projects.apache.org/committee.html?turbine)    | [:mag:](sboms/README.md#turbine)    | Maven     | CDX Maven P |
| [Zookeeper](https://zookeeper.apache.org/)   [:clipboard:](https://projects.apache.org/committee.html?zookeeper)  | [:mag:](sboms/README.md#zookeeper)  | Maven     | CDX Maven P |
