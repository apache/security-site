#!/bin/bash

v=$1

[ -z "$v" ] && echo "$0 {version}" && exit 1

major=$(echo $v | cut -d . -f 1)

baseurl="https://archive.apache.org/dist/maven/maven-$major/$v/binaries/"
central_baseurl="https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/$v"

zip=apache-maven-$v-bin.zip
sbom=apache-maven-$v-cyclonedx.json

[ -f $zip ] || wget $baseurl/$zip
[ -f $sbom ] || wget $central_baseurl/$sbom

echo "$(unzip -l $zip | grep .jar | wc -l) *.jar in $zip:"
unzip -l $zip | grep .jar | awk '{print $4}' | sort

echo

echo "$(grep purl $sbom | grep -v .pom | tail -n +1 | wc -l) dependencies in $sbom:"
grep purl $sbom | grep -v .pom | tail -n +1 | sort -t '/' -k3
