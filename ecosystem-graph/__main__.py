#!/usr/bin/env python3

# Script to analyze ASF SBOMs and draw a project graph

import json
from lib4sbom.parser import SBOMParser
import os
import re
import networkx as nx

def is_sbom(file):
    return not file.endswith("md") and not file.endswith("uploaded")

def list_sboms():
    sboms = []
    for pmc in [ d.name for d in os.scandir("sboms/") if os.path.isdir(d) ]:
        for tpe in [ t.name for t in os.scandir(f"sboms/{pmc}") if os.path.isdir(t) ]:
            if tpe == 'maven':
                for (root, _, files) in os.walk(f"sboms/{pmc}/maven"):
                    for file in filter(is_sbom, files):
                        group_id = root.split('/')[3]
                        artifact_id = root.split('/')[4]
                        purl = f"pkg:maven/{group_id}/{artifact_id}"
                        sboms.append((purl, os.path.join(root, file)))
            elif tpe == 'pypi':
                for (root, _, files) in os.walk(f"sboms/{pmc}/pypi"):
                    for file in filter(is_sbom, files):
                        package_name = root.split('/')[3]
                        purl = f"pkg:pypi/{package_name}"
                        sboms.append((purl, os.path.join(root, file)))
            else:
                print(f"Unexpected type: {tpe}")
    return sboms

def simplify_purl(purl):
    return re.sub(r'_(2.1.|3)$', '', purl.split('@')[0])

sboms = list_sboms();
purls = [ simplify_purl(sbom[0]) for sbom in sboms ]

def get_purl(package):
    if 'purl' in package:
        return package['purl']
    if 'group' in package:
        return f"pkg:maven/{package['group']}/{package['name']}"
    if 'externalreference' in package:
        for (_, t, r) in package['externalreference']:
            if t == 'purl':
                return r
    return None

links = nx.DiGraph()
def parse_sbom(sbom):
    global links
    sbom_purl = simplify_purl(sbom[0])
    parser = SBOMParser()
    try:
        parser.parse_file(sbom[1])
    except Exception as e:
        print('Error parsing ' + sbom[1])
        raise e
    for package in parser.get_packages():
        dep_purl = simplify_purl(get_purl(package))
        if dep_purl and dep_purl in purls:
            links.add_edge(sbom_purl, dep_purl)

list(map(parse_sbom, sboms))

# Hack: remove some 'provided' dependencies causing cycles ;)
links.remove_edge("pkg:maven/org.apache.commons/commons-lang3", "pkg:maven/org.apache.commons/commons-text")
links.remove_edge("pkg:maven/org.apache.commons/commons-lang3", "pkg:maven/org.apache.commons/commons-lang3")
links.remove_edge("pkg:maven/org.apache.camel.kafkaconnector/camel-kafka-connector", "pkg:maven/org.apache.camel.kafkaconnector/camel-kafka-connector")
links.remove_edge("pkg:maven/org.apache.camel.kamelets/camel-kamelets", "pkg:maven/org.apache.camel.kamelets/camel-kamelets")
# will probably have to exclude commons-configuration2 depending on hadoop-hdfs-client
# via commons-vfs once commons-vfs has a release which publishes an SBOM
links.remove_edge("pkg:maven/org.apache.commons/commons-configuration2", "pkg:maven/org.apache.hadoop/hadoop-hdfs-client")

try:
    simplified = nx.transitive_reduction(links)
except Exception:
    print("Found a cyclic dependency.")
    print('''  Unfortunately this makes it hard to remove 'redundant'
  transitive links from the graph (e.g. if 'A' depends on 'B' and 'B' depends
  on 'C', we don't want to see a direct link from 'A' to 'C', and I don't think
  all SBOM formats allow us to detect this otherwise).''')
    print("Cycles:")
    print(nx.find_cycle(links))
    exit(2)

def to_dot(graph):
    result = "strict graph {\n"
    for k, v in graph.edges:
      result += f"  \"{k}\" -- \"{v}\"\n"
    result += "}"
    return result

def to_json(graph):
    purls = []
    nodes = []
    categories = []
    categoryObjects = []
    def node(purl):
        try:
            return purls.index(purl)
        except ValueError: 
            purls.append(purl)
            group = purl.split('/')[1]
            if group.startswith("org.apache"):
                category = group.split('.')[2]
            else:
                category = group.split('.')[-1]
            if category not in categories:
                categories.append(category)
                categoryObjects.append({
                    "name": category,
                    "base": category,
                })
            nodes.append({
                "name": '/'.join(purl.split('/')[1:]),
                "category": categories.index(category)
            })
            return len(purls) - 1
    links = []
    for k, v in graph.edges:
        links.append({
            "source": node(k),
            "target": node(v),
        })
    return {
            "categories": categories,
            "categoryObjects": categoryObjects,
            "nodes": nodes,
            "links": links,
    }

#with open("ecosystem-full.dot", "w") as outfile:
#    outfile.write(to_dot(links))
#with open("ecosystem.dot", "w") as outfile:
#    outfile.write(to_dot(simplified))
with open("app/htdocs/ecosystem.json", "w") as outfile:
    outfile.write(json.dumps(to_json(simplified)))
