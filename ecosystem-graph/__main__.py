#!/usr/bin/env python3

# Script to analyze ASF SBOMs and draw a project graph

import json
from lib4sbom.parser import SBOMParser
import os
import re
import networkx as nx

def list_sboms():
    sboms = []
    for pmc in os.scandir("sboms"):
        for tpe in filter(os.path.isdir, os.scandir(f"sboms/{pmc.name}")):
            if tpe.name == 'maven':
                for (root, _, files) in os.walk(f"sboms/{pmc.name}/maven"):
                    for file in files:
                        group_id = root.split('/')[3]
                        artifact_id = root.split('/')[4]
                        purl = f"pkg:maven/{group_id}/{artifact_id}"
                        sboms.append((purl, os.path.join(root, file)))
            elif tpe.name == 'pypi':
                for (root, _, files) in os.walk(f"sboms/{pmc.name}/pypi"):
                    for file in files:
                        package_name = root.split('/')[3]
                        purl = f"pkg:pypi/{package_name}"
                        sboms.append((purl, os.path.join(root, file)))
            else:
                print(f"Unexpected type: {tpe}")
    return sboms

def simplify_purl(purl):
    return re.sub(r'_(2.12|2.13|3)$', '', purl.split('@')[0])

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
    parser.parse_file(sbom[1])
    for package in parser.get_packages():
        dep_purl = simplify_purl(get_purl(package))
        if dep_purl and dep_purl in purls:
            links.add_edge(sbom_purl, dep_purl)

list(map(parse_sbom, sboms))

# Hack: remove some 'provided' dependencies causing cycles ;)
links.remove_edge("pkg:maven/org.apache.commons/commons-lang3", "pkg:maven/org.apache.commons/commons-text")
links.remove_edge("pkg:maven/org.apache.commons/commons-lang3", "pkg:maven/org.apache.commons/commons-lang3")
#print(nx.find_cycle(links))
simplified = nx.transitive_reduction(links)

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

with open("app/htdocs/sbom/ecosystem.json", "w") as outfile:
    outfile.write(json.dumps(to_json(simplified)))
