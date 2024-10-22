#!/usr/bin/env python3

from common import get_dirs, get_files, get_sbom_cached, dt_pmc, post_sbom
from dotenv import load_dotenv
import json
import os
from packaging.version import Version
import re
from sys import argv

class Project:
    def __init__(self, pmc, group_id, artifact_id) -> None:
        self.pmc = pmc
        self.group_id = group_id
        self.artifact_id = artifact_id

    def url(self) -> str:
        group = self.group_id.replace('.', '/')
        return f"https://repo1.maven.org/maven2/{group}/{self.artifact_id}"

    def __str__(self) -> str:
        return f"Project({self.pmc}, {self.group_id}, {self.artifact_id})"

def maven_projects(pmc, prefix = None, subproject = None):
    # TODO support deeper hierarchies
    def is_direct(project):
        return project.artifact_id.startswith(f'{subproject or pmc}')

    prefix = prefix or f"org/apache/{pmc}"
    if subproject:
        url = f'https://repo1.maven.org/maven2/{prefix}/{subproject}'
    else:
        url = f'https://repo1.maven.org/maven2/{prefix}'

    def as_project(link):
        return Project(pmc, '.'.join(url.split('/')[4:]), link.get('title')[:-1])

    return list(filter(is_direct, list(map(as_project, get_dirs(url + '/')))))

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
    projects = maven_projects(pmc, subproject = 'log4j')
elif pmc == 'pekko':
    def eligible(project):
        # these publish CycloneDX 1.0 XML artifacts
        # without a 'components' tag, which is not valid
        return not (project.startswith("pekko-bom") or project.startswith("pekko-protobuf-v3"))
    projects = list(filter(eligible, maven_projects(pmc)))
elif pmc == 'commons':
    projects = maven_projects(pmc) + maven_projects(pmc, prefix = "commons-io")
else:
    projects = maven_projects(pmc)

for project in projects:
    friendly_name = 'Apache ' + project.artifact_id.replace('-', ' ').title()
    print(project)
    pmc_uuid = dt_pmc(pmc)['uuid']

    index = get_dirs(project.url())
    def version_name(link):
        return link['title'][:-1]
    def is_version(v):
        # TODO support such versions
        return not 'M' in v and not 'incubating' in v and not 'hadoop' in v and not 'milestone' in v and not 'pre' in v and not len(v) > 10
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
        index = get_files_cached(f"{project.url()}/{lastVersion}")
        def file_name(link):
            return link['title']
        def is_sbom(name):
            # tighten to '-cyclonedx.xml' when Pekko is released with
            # https://github.com/apache/pekko/pull/1536
            return name.endswith('-cyclonedx.json') or (name.endswith('.xml') and not name.endswith('site.xml') and not name.endswith('metadata.xml'))
        sboms = list(filter(is_sbom, map(file_name, index)))
        if sboms:
            sbom = sboms[0]
            url = f"{project.url()}/{lastVersion}/{sbom}"
            cache = f'{pmc}/maven/{project.group_id}/{project.artifact_id}/{lastVersion}/{sbom}'
            sbom = get_sbom_cached(url, cache)
            post_sbom(pmc, pmc_uuid, friendly_name, lastVersion, sbom)
