#!/bin/zsh

# look at SBOMs in sboms/{pmc} and generate release SBOMs description in sboms/{pmc}/{project}-{version}.md
# that lists the SBOMs associated to the release, and for each a high-level summary:
# - what is the SBOM describing? = the content of metadata
# - what are the components from the release (the BOM)? = the content of components

describe="$(pwd)/scripts/describe_sboms.java"

function describeReleasesFromBasedir() {
  local pmc=$1
  local name=$2
  local basedir=$3

  echo "> describing $name SBOMs"
  cd sboms/$pmc
  for d in */$basedir/*
  do
    local version=$(basename $d)
    echo "  > describing $name $version"
    $describe $name $version $d/*.(xml|json) > $pmc-$version.md
  done
  cd ../..
}

function describeReleasesFromBase() {
  local pmc=$1
  local name=$2
  local id=$3
  local baseDir=$4
  local baseSub=$5
  [ "$id" = "-" ] && id=$pmc
  [ "$baseSub" = "-" ] && baseSub=$id

  echo "> describing $name SBOMs"
  cd sboms/$pmc
  local version
  for version in $(echo "$(for d in */$baseDir*/$baseSub*/* ; do filename $d ; done)" | sort -u)
  do
    echo "  > describing $name $version"
    $describe $name $version */$baseDir*/$baseSub*/$version/*.(xml|json) > $id-$version.md
  done
  cd ../..
}

describeReleasesFromBasedir airflow Airflow apache-airflow

describeReleasesFromBase arrow Arrow -
describeReleasesFromBase avro Avro -
describeReleasesFromBase camel Camel -

# commons
describeReleasesFromBase commons "Commons IO" commons-io commons-io
describeReleasesFromBase commons BCEL bcel org.apache.bcel
describeReleasesFromBase commons "Commons Compress" commons-compress org.apache.commons -
describeReleasesFromBase commons "Commons Configuration 2" commons-configuration2 org.apache.commons -
describeReleasesFromBase commons "Commons Crypto" commons-crypto org.apache.commons -
describeReleasesFromBase commons "Commons CSV" commons-csv org.apache.commons -
describeReleasesFromBase commons "Commons DBCP 2" commons-dbcp2 org.apache.commons -
describeReleasesFromBase commons "Commons Email" commons-email org.apache.commons -
describeReleasesFromBase commons "Commons Exec" commons-exec org.apache.commons -
describeReleasesFromBase commons "Commons Imaging" commons-imaging org.apache.commons -
describeReleasesFromBase commons "Commons JCS 3" commons-jcs3 org.apache.commons -
describeReleasesFromBase commons "Commons JEXL 3" commons-jexl3 org.apache.commons -
describeReleasesFromBase commons "Commons Lang 3" commons-lang3 org.apache.commons -
describeReleasesFromBase commons "Commons Math 4" commons-math org.apache.commons -
describeReleasesFromBase commons "Commons Parent" commons-parent org.apache.commons -
describeReleasesFromBase commons "Commons Pool 2" commons-pool2 org.apache.commons -
describeReleasesFromBase commons "Commons Release Plugin" commons-release-plugin org.apache.commons -
describeReleasesFromBase commons "Commons RNG" commons-rng org.apache.commons -
describeReleasesFromBase commons "Commons Statistics" commons-statistics org.apache.commons -
describeReleasesFromBase commons "Commons Text" commons-text org.apache.commons -

describeReleasesFromBase cxf CXF -

describeReleasesFromBase directory Directory - org.apache.directory
describeReleasesFromBase directory Kerby kerby org.apache.kerby

describeReleasesFromBase druid Druid -
describeReleasesFromBase flink Flink -
describeReleasesFromBase groovy Groovy -
describeReleasesFromBase hadoop Hadoop -
describeReleasesFromBase hbase HBase -
describeReleasesFromBase hop Hop -
describeReleasesFromBase jena Jena -
describeReleasesFromBase jspwiki JSPWiki -
describeReleasesFromBase logging Log4j log4j

# maven
#describeReleasesFromBase maven Maven - org.apache.maven # need strict equality, not any groupId starting with
describeReleasesFromBase maven "Maven Archetype" maven-archetype org.apache.maven.archetype # missing maven-archetype-plugin
describeReleasesFromBase maven "Maven Archetype Bundles" maven-archetypes org.apache.maven.archetypes
describeReleasesFromBase maven Doxia doxia org.apache.maven.doxia
describeReleasesFromBase maven "Maven Enforcer" maven-enforcer org.apache.maven.enforcer # missing maven-enforcer-plugin and maven-enforcer-extension
describeReleasesFromBase maven "Maven Build Cache Extension" maven-build-cache-extension org.apache.maven.extensions -
describeReleasesFromBase maven "Maven Extensions Parent" maven-extensions org.apache.maven.extensions -
describeReleasesFromBase maven "Maven Indexer" maven-indexer org.apache.maven.indexer
describeReleasesFromBase maven "Maven JXR" maven-jxr org.apache.maven.jxr # missing maven-jxr-plugin
describeReleasesFromBase maven "Maven Plugin Testing" maven-plugin-testing org.apache.maven.plugin-testing
describeReleasesFromBase maven "Maven Plugin Tools" maven-plugin-tools org.apache.maven.plugin-tools # missing maven-plugin-plugin
# plugins
describeReleasesFromBase maven "Maven Artifact Plugin" maven-artifact-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Assembly Plugin" maven-assembly-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Checkstyle Plugin" maven-checkstyle-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Clean Plugin" maven-clean-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Compiler Plugin" maven-compiler-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Dependency Plugin" maven-dependency-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Deploy Plugin" maven-deploy-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven GPG Plugin" maven-gpg-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Help Plugin" maven-help-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Install Plugin" maven-install-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Invoker Plugin" maven-invoker-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Jar Plugin" maven-jar-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Jarsigner Plugin" maven-jarsigner-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Javadoc Plugin" maven-javadoc-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven JLink Plugin" maven-jlink-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Plugins Parent" maven-plugins org.apache.maven.plugins -
describeReleasesFromBase maven "Maven PMD Plugin" maven-pmd-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Project Info Reports Plugin" maven-project-info-reports-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Remote Resources Plugin" maven-remote-resources-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Resources Plugin" maven-resources-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven SCM Publish Plugin" maven-scm-publish-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Shade Plugin" maven-shade-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Site Plugin" maven-site-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Source Plugin" maven-source-plugin org.apache.maven.plugins -
describeReleasesFromBase maven "Maven Toolchains Plugin" maven-toolchains-plugin org.apache.maven.plugins -
# end of plugins
describeReleasesFromBase maven "Maven Release" maven-release org.apache.maven.release # missing maven-release-plugin
describeReleasesFromBase maven "Maven Reporting API" maven-reporting-api org.apache.maven.reporting -
describeReleasesFromBase maven "Maven Reporting Exec" maven-reporting-exec org.apache.maven.reporting -
describeReleasesFromBase maven "Maven Reporting Implementation" maven-reporting-impl org.apache.maven.reporting -
describeReleasesFromBase maven "Maven Resolver" maven-resolver org.apache.maven.resolver
describeReleasesFromBase maven "Maven SCM" maven-scm org.apache.maven.scm
# shared
describeReleasesFromBase maven "Maven Common Artifact Filters" maven-common-artifact-filters org.apache.maven.shared -
describeReleasesFromBase maven "Maven Dependency Analyzer" maven-dependency-analyzer org.apache.maven.shared -
describeReleasesFromBase maven "Maven Dependency Tree" maven-dependency-tree org.apache.maven.shared -
describeReleasesFromBase maven "Maven Filtering" maven-filtering org.apache.maven.shared -
describeReleasesFromBase maven "Maven Invoker" maven-invoker org.apache.maven.shared -
describeReleasesFromBase maven "Maven Jarsigner" maven-jarsigner org.apache.maven.shared -
describeReleasesFromBase maven "Maven Script Interpreter" maven-script-interpreter org.apache.maven.shared -
describeReleasesFromBase maven "Maven Shared Parent" maven-shared-components org.apache.maven.shared -
describeReleasesFromBase maven "Maven Shared Jar" maven-shared-jar org.apache.maven.shared -
describeReleasesFromBase maven "Maven Shared Resources" maven-shared-resources org.apache.maven.shared -
# end of shared
describeReleasesFromBase maven "Maven Skins Parent" maven-skins org.apache.maven.skins
describeReleasesFromBase maven "Maven Surefire" maven-surefire org.apache.maven.surefire # missing maven-failsafe-plugin, maven-surefire-plugin and maven-surefire-report-plugin
describeReleasesFromBase maven "Maven Wrapper" maven-wrapper org.apache.maven.wrapper

describeReleasesFromBase orc ORC -
describeReleasesFromBase parquet Parquet -
describeReleasesFromBase pekko Pekko -
describeReleasesFromBase ratis Ratis -
describeReleasesFromBase santuario Santuario -
describeReleasesFromBase skywalking SkyWalking -
describeReleasesFromBase spark Spark -
describeReleasesFromBase syncope Syncope -

describeReleasesFromBase turbine Turbine - org.apache.turbine
describeReleasesFromBase turbine Fulcrum fulcrum org.apache.fulcrum

describeReleasesFromBase zookeeper Zookeeper -
