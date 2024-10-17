#!/usr/bin/env python3

# Script to analyze ASF SBOMs and draw a project graph

import json
from lib4sbom.parser import SBOMParser
import os
from concurrent.futures import ThreadPoolExecutor
import networkx as nx

def list_sboms():
    sboms = []
    for pmc in os.scandir("sboms"):
        for project in filter(os.path.isdir, os.scandir(f"sboms/{pmc.name}")):
            # TODO assuming Maven and depth 1 here for now...
            purl = f"pkg:maven/org.apache.{pmc.name}/{project.name}"
            for (root, _, files) in os.walk(f"sboms/{pmc.name}/{project.name}"):
                for file in files:
                    sboms.append((purl, os.path.join(root, file)))
    return sboms

sboms = list_sboms();
purls = [ sbom[0] for sbom in sboms ]

def get_purl(package):
    if 'purl' in package:
        return package['purl']
    if 'group' in package:
        return f"pkg:maven/{package['group']}/{package['name']}"
    return None

links = nx.DiGraph()
def parse_sbom(sbom):
    global links
    #print(sbom[1])
    parser = SBOMParser()
    parser.parse_file(sbom[1])
    for package in parser.get_packages():
        purl = get_purl(package)
        if purl and purl in purls:
            links.add_edge(sbom[0], purl)

#print(parse_sbom(('x', "sboms/spark/spark-core_2.12/3.5.2/spark-core_2.12-3.5.2-cyclonedx.json")))
list(map(parse_sbom, sboms))

# Hack: remove some 'provided' dependencies causing cycles ;)
links.remove_edge("pkg:maven/org.apache.commons/commons-lang3", "pkg:maven/org.apache.commons/commons-text")
links.remove_edge("pkg:maven/org.apache.commons/commons-lang3", "pkg:maven/org.apache.commons/commons-lang3")
#print(nx.find_cycle(links))
simplified = nx.transitive_reduction(links)

def to_dot(graph):
    print("strict graph {")
    for k, v in graph.edges:
      print(f"  \"{k}\" -- \"{v}\"")
    print("}")

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
            category = purl.split('/')[1].split('.')[-1]
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

with open("ecosystem-graph/ecosystem.json", "w") as outfile:
    outfile.write(json.dumps(to_json(simplified)))
