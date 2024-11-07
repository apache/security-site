#!/bin/bash

# look at SBOMs in sboms/{pmc} and generate release SBOMs description in sboms/{pmc}/{project}-{version}.md
# that lists the SBOMs associated to the release, and for each a high-level summary:
# - what is the SBOM describing? = the content of metadata
# - what are the components from the release (the BOM)? = the content of components

describe="$(pwd)/scripts/describe_sboms.java"

echo "> describing Airflow SBOMs"
cd sboms/airflow
for d in */apache-airflow/2.*
do
  version=$(basename $d)
  echo "  > describing Airflow $version"
  $describe Airflow $version $d/*.json > airflow-$version.md
done
cd ../..

echo "> describing Flink SBOMs"
cd sboms/flink
for d in */org.apache.flink/flink-core/*
do
  version=$(basename $d)
  echo "  > describing Flink $version"
  $describe Flink $version */org.apache.flink/flink*/$version/*.json > flink-$version.md
done
cd ../..

echo "> describing Groovy SBOMs"
cd sboms/groovy
for d in */org.apache.groovy/groovy/*
do
  version=$(basename $d)
  echo "  > describing Groovy $version"
  $describe Groovy $version */org.apache.groovy/groovy*/$version/*.json > groovy-$version.md
done
cd ../..

echo "> describing JSPWiki SBOMs"
cd sboms/jspwiki
for d in */org.apache.jspwiki/jspwiki-war/2.*
do
  version=$(basename $d)
  echo "  > describing JSPWiki $version"
  $describe JSPWiki $version */org.apache.jspwiki*/jspwiki-*/$version/*.xml > jspwiki-$version.md
done
cd ../..

echo "> describing Logging SBOMs"
cd sboms/logging
for d in */org.apache.logging.log4j/log4j-api/*
do
  version=$(basename $d)
  echo "  > describing Log4j $version"
  $describe Log4j $version */org.apache.logging.log4j/log4j-*/$version/*.xml > log4j-$version.md
done
cd ../..

echo "> describing Pekko SBOMs"
cd sboms/pekko
for d in */org.apache.pekko/pekko-bom_2.13/*
do
  version=$(basename $d)
  echo "  > describing Pekko $version"
  $describe Pekko $version */org.apache.pekko/pekko-*/$version/*.xml > pekko-$version.md
done
cd ../..

echo "> describing Turbine SBOMs"
cd sboms/turbine
for d in */org.apache.turbine/turbine/*
do
  version=$(basename $d)
  echo "  > describing Turbine $version"
  $describe Turbine $version */org.apache.turbine/turbine*/$version/*.json > turbine-$version.md
done
for d in */org.apache.fulcrum/fulcrum-security/*
do
  version=$(basename $d)
  echo "  > describing Fulcrum $version"
  $describe Fulcrum $version */org.apache.fulcrum/fulcrum*/$version/*.json > fulcrum-$version.md
done
cd ../..

echo "> describing Zookeeper SBOMs"
cd sboms/zookeeper
for d in */org.apache.zookeeper/zookeeper-jute/*
do
  version=$(basename $d)
  echo "  > describing Zookeeper $version"
  $describe Zookeeper $version */org.apache.zookeeper/zookeeper*/$version/*.json > zookeeper-$version.md
done
cd ../..
