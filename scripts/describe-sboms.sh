#!/bin/bash

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

