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
# TODO maven
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
