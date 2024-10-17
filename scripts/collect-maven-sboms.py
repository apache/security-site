#!/usr/bin/env python3

from common import get_dirs, get_files, get_sbom_cached, dt_pmc, post_sbom
from dotenv import load_dotenv
import json
import os
from packaging.version import Version
import re
from sys import argv

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
        try:
            return json.load(i)
        except Exception as e:
            print(f"Failed to parse {filename}")
            print(f"for {url}")
            raise e


if len(argv)>1:
    pmc = argv[1]
else:
    pmc = 'maven'

if len(argv)>2:
    projects = [ argv[2] ]
elif pmc == 'camel':
    # we switched to getting those from the
    # download page, with collect-camel-sboms.py
    # but spring-boot is not there:
    projects = [
      'springboot/spring-boot',
    ]
elif pmc == 'logging':
    projects = maven_projects(pmc, 'log4j')
elif pmc == 'pekko':
    def eligible(project):
        # these publish CycloneDX 1.0 XML artifacts
        # without a 'components' tag, which is not valid
        return not (project.startswith("pekko-bom") or project.startswith("pekko-protobuf-v3"))
    projects = list(filter(eligible, maven_projects(pmc)))
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

    # TODO probably good to have a custom version splitter/sorter
    # after all
    def parse_version(s):
        from itertools import takewhile
        return Version("".join(takewhile(lambda c: c != '-', s)).replace(".Final", ""))

    versions.sort(key=parse_version)
    if versions:
        lastVersion = versions[-1]
        print(lastVersion)
        index = get_files_cached(f'https://repo1.maven.org/maven2/org/apache/{pmc}/{project}/{lastVersion}')
        def file_name(link):
            return link['title']
        def is_sbom(name):
            # tighten to '-cyclonedx.xml' when Pekko is released with
            # https://github.com/apache/pekko/pull/1536
            return name.endswith('-cyclonedx.json') or name.endswith('.xml')
        sboms = list(filter(is_sbom, map(file_name, index)))
        if sboms:
            sbom = sboms[0]
            url = f'https://repo1.maven.org/maven2/org/apache/{pmc}/{project}/{lastVersion}/{sbom}'
            cache = f'{pmc}/{project}/{lastVersion}/{sbom}'
            sbom = get_sbom_cached(url, cache)
            post_sbom(pmc, pmc_uuid, friendly_name, lastVersion, sbom)
