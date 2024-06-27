#!/usr/bin/env python3

# Cross-reference the 'project-coordinates.json' with DOAP

import os
import json
import pprint
from rdflib import Graph
from rdflib.namespace import RDF, DOAP
from slugify import slugify
from urllib.request import urlopen
import xml.etree.ElementTree as ET

def fetch_doap(url):
    filename = 'cache/doap/%s.xml' % (slugify(url))
    if not os.path.exists(filename):
        os.makedirs('cache/doap', exist_ok = True)
        f = urlopen(url)
        with open(filename, 'w') as d:
          d.write(f.read().decode('utf-8'))
    with open(filename, 'r') as d:
        f = Graph()
        f.parse(data=d.read(), format='xml')
        return f

# manually maintained
with open('project-coordinates.json', 'r') as p:
    project_coordinates = json.load(p)

from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef
class ASFEXT(DefinedNamespace):
    pmc: URIRef
    _NS = Namespace("http://projects.apache.org/ns/asfext#")
# https://github.com/RDFLib/rdflib/issues/2811
class MYDOAP(DefinedNamespace):
    _extras = [
      "security-contact",
      "security-policy",
    ]
    _NS = Namespace("http://usefulinc.com/ns/doap#")

for location in ET.parse('projects.xml').getroot():
    #print(location.text)
    # https://github.com/apache/cordova-docs/pull/1353
    if (location.text == "https://cordova.apache.org/infra/doap_Cordova.rdf" or 

        # https://github.com/apache/doris/pull/36956
        location.text == "https://gitbox.apache.org/repos/asf?p=doris.git;a=blob_plain;f=doap_Doris.rdf;hb=HEAD" or
        # https://github.com/apache/kafka/pull/16472
        location.text == "https://gitbox.apache.org/repos/asf?p=kafka.git;a=blob_plain;f=doap_Kafka.rdf;hb=HEAD" or
        # https://github.com/apache/olingo-site/pull/6
        location.text == "http://olingo.apache.org/doap_Olingo.rdf" or
        # https://github.com/apache/orc/pull/1964
        location.text == "http://orc.apache.org/doap_orc.rdf" or
        # https://github.com/apache/sis-site/pull/3
        location.text == "http://sis.apache.org/DOAP.rdf" or
        # https://github.com/apache/yunikorn-site/pull/444
        location.text == "https://gitbox.apache.org/repos/asf?p=yunikorn-site.git;a=blob_plain;f=doap_YuniKorn.rdf;hb=HEAD" or

        # https://github.com/apache/kibble-website/pull/15
        location.text == "https://kibble.apache.org/doap.rdf" or
        # https://github.com/apache/hudi/pull/11533
        location.text == "https://gitbox.apache.org/repos/asf?p=hudi.git;a=blob_plain;f=doap_HUDI.rdf;hb=HEAD" or
        # https://issues.apache.org/jira/browse/GORA-716
        location.text == "http://svn.apache.org/repos/asf/gora/cms_site/trunk/content/current/doap_Gora.rdf" or
        # https://github.com/apache/gobblin-site/pull/2
        location.text == "https://gobblin.apache.org/doap_Gobblin.rdf"):
        continue
    d = fetch_doap(location.text)
    #pprint.pprint(d)
    
    for project in d.subjects(RDF.type, DOAP.Project):
        for contact in d.objects(project, MYDOAP['security-contact']):
            pprint.pprint(project)
            pprint.pprint(contact)
        for policy in d.objects(project, MYDOAP['security-policy']):
            pprint.pprint(project)
            pprint.pprint(policy)
