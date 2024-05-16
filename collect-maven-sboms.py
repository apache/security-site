#!/usr/bin/env python3

from bs4 import BeautifulSoup
from common import get_dirs, get_files, get_sbom_cached, dt_pmc, post_sbom
from dotenv import load_dotenv
import json
import os
from packaging.version import Version
import re
import requests
from urllib import request
from sys import argv

load_dotenv()
dt_api_key = os.getenv('DT_API_KEY')

def project_name(link):
    return link.get('title')[:-1]

def maven_projects(pmc, subproject = None):
    # TODO support deeper hierarchies
    def is_direct(name):
        return name.startswith(f'{subproject or pmc}-')

    if subproject:
        url = f'https://repo1.maven.org/maven2/org/apache/{pmc}/{subproject}/'
    else:
        url = f'https://repo1.maven.org/maven2/org/apache/{pmc}/'

    projects = list(filter(is_direct, list(map(project_name, get_dirs(url)))))

    if subproject:
        def prefix_subproject(project):
            return f"{subproject}/{project}"
        return list(map(prefix_subproject, projects))
    else:
        return projects

def get_files_cached(url):
    filename = "cache/" + "".join(x for x in url if x.isalnum())
    if not os.path.exists(filename):
        os.makedirs("cache", exist_ok=True)
        with open(filename, "w") as out:
            json.dump(get_files(url), out)

    with open(filename, "r") as i:
        return json.load(i)

if len(argv)>1:
    pmc = argv[1]
else:
    pmc = 'commons'

if len(argv)>2:
    projects = [ argv[2] ]
elif pmc == 'camel':
    projects = [
      'camel',
      'kamelets/camel-kamelets-parent',
      'quarkus/camel-quarkus',
      'springboot/spring-boot',
    ]
elif pmc == 'logging':
    projects = maven_projects(pmc, 'log4j')
else:
    projects = maven_projects(pmc)

for project in projects:
    friendly_name = 'Apache ' + project.split('/')[-1].replace('-', ' ').title()
    print(project)
    pmc_uuid = dt_pmc(pmc)['uuid']

    index = get_dirs(f'https://repo1.maven.org/maven2/org/apache/{pmc}/{project}')
    def version_name(link):
        return link['title'][:-1]
    def is_version(v):
        # TODO support such versions
        return not 'M' in v and not 'incubating' in v and not 'hadoop' in v and not 'milestone' in v and not 'pre' in v
    versions = list(filter(is_version, list(map(version_name, index))))
    versions.sort(key=Version)
    if versions:
        lastVersion = versions[-1]
        print(lastVersion)
        index = get_files_cached(f'https://repo1.maven.org/maven2/org/apache/{pmc}/{project}/{lastVersion}')
        def file_name(link):
            return link['title']
        def is_sbom(name):
            return name.endswith('-cyclonedx.json') or name.endswith('-cyclonedx.xml')
        sboms = list(filter(is_sbom, map(file_name, index)))
        if sboms:
            sbom = sboms[0]
            url = f'https://repo1.maven.org/maven2/org/apache/{pmc}/{project}/{lastVersion}/{sbom}'
            cache = f'{pmc}/{project}/{lastVersion}/{sbom}'
            sbom = get_sbom_cached(url, cache)
            post_sbom(pmc, pmc_uuid, friendly_name, lastVersion, sbom)
