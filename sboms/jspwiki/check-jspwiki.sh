#!/bin/bash

v=$1

[ -z "$v" ] && echo "$0 {version}" && exit 1

baseurl="https://archive.apache.org/dist/jspwiki/$v/binaries/"

portable=jspwiki-portable-$v-woas.zip
sbom_portable=jspwiki-portable-$v-cyclonedx.xml
webapp=JSPWiki.war
war=JSPWiki-$v.war
sbom_war=jspwiki-war-$v-cyclonedx.xml

[ -f $portable ] || wget $baseurl/portable/$portable
[ -f $war ] || wget $baseurl/webapp/$webapp -O $war

[ -f $sbom_portable ] || wget https://repo.maven.apache.org/maven2/org/apache/jspwiki/jspwiki-portable/$v/$sbom_portable
[ -f $sbom_war ] || wget https://repo.maven.apache.org/maven2/org/apache/jspwiki/jspwiki-war/$v/$sbom_war

echo "$(unzip -l $war | grep .jar | wc -l) *.jar in $war:"
unzip -l $war | grep .jar | awk '{print $4}' | sort

echo

echo "$(grep purl $sbom_war | grep -v .pom | tail -n +1 | wc -l) dependencies in $sbom_war:"
grep purl $sbom_war | grep -v .pom | tail -n +1 | sort -t '/' -k3

echo

echo "$(unzip -l $portable | grep .jar | wc -l) *.jar in $portable:"
unzip -l $portable | grep .jar | awk '{print $4}' | sort

echo

echo "$(grep purl $sbom_portable | grep -v .pom | tail -n +1 | wc -l) dependencies in $sbom_portable:"
grep purl $sbom_portable | grep -v .pom | tail -n +1 | sort -t '/' -k3
