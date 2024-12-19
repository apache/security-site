#!/usr/bin/env python3

from bs4 import BeautifulSoup
from common import dt_pmc, get_sbom_cached, post_sbom
import re
import requests

pmc = dt_pmc("camel")

with requests.get("https://camel.apache.org/download/") as res:
    soup = BeautifulSoup(res.text, 'html.parser')
    def link_to_sbom(tag):
        return tag.name == 'a' and \
            tag.has_attr('href') and \
            tag.get('href').endswith('-sbom.json')
    for a in soup.find_all(link_to_sbom):
        url = a.get('href').replace('www.apache.org/dyn/closer.lua', 'dlcdn.apache.org')
        name = url.split('/')[-1]
        match = re.compile("(.*?)-(\\d.*)-sbom.json").match(name)
        friendly_name = {
          "apache-camel": "Apache Camel",
          "apache-camel-quarkus": "Apache Camel Quarkus",
          "camel-kamelets": "Apache Camel Kamelets",
          "camel-kafka-connector": "Apache Camel Kafka Connector",
        }[match.group(1)]
        group_id = {
          "apache-camel": "org.apache.camel",
          "apache-camel-quarkus": "org.apache.camel.quarkus",
          "camel-kamelets": "org.apache.camel.kamelets",
          "camel-kafka-connector": "org.apache.camel.kafkaconnector",
        }[match.group(1)]
        artifact_id = {
          "apache-camel": "camel",
          "apache-camel-quarkus": "camel-quarkus",
          "camel-kamelets": "camel-kamelets",
          "camel-kafka-connector": "camel-kafka-connector",
        }[match.group(1)]
        version = match.group(2)
        sbom = get_sbom_cached(url, f"camel/maven/{group_id}/{artifact_id}/{version}/{name}")
        post_sbom(pmc, pmc['uuid'], friendly_name, version, sbom)

main_sboms = {
    "Apache Camel": "camel",
    "Apache Camel Quarkus": "camel-quarkus",
    "Apache Camel Kamelets": "camel-kamelets",
    "Apache Camel Spring Boot": "camel-spring-boot",
    # Kafka connector is not in version control?
}

for name in main_sboms:
    slug = main_sboms[name]
    url = f"https://raw.githubusercontent.com/apache/{slug}/main/{slug}-sbom/{slug}-sbom.json"
    with requests.get(url) as res:
        if res.status_code == 200:
            post_sbom(pmc, pmc['uuid'], name, "main", res.text)
        else:
            print("Failed to fetch " + url)