#!/usr/bin/env python3

from bs4 import BeautifulSoup
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

if len(argv)>1:
    pmc = argv[1]
else:
    pmc = 'commons'

def get_index(url):
    with request.urlopen(url) as resp:
        index = resp.read().decode('utf-8')
        soup = BeautifulSoup(index, 'html.parser')
        def link_to_subproject(tag):
            return tag.name == 'a' and \
                tag.has_attr('href') and \
                not tag.get('href').startswith('.')
        return soup.find_all(link_to_subproject)

def get_dirs(url):
    tags = get_index(url)
    def is_dir(tag):
        return tag.has_attr('href') and tag.get('href').endswith('/')
    return list(filter(is_dir, tags))

def get_files(url):
    tags = get_index(url)
    def is_dir(tag):
        return tag.has_attr('href') and not tag.get('href').endswith('/')
    return list(filter(is_dir, tags))

def project_name(link):
    return link.get('title')[:-1]

def maven_projects(pmc):
    # TODO support deeper hierarchies
    def is_direct(name):
        return name.startswith(f'{pmc}-')
    return list(filter(is_direct, list(map(project_name, get_dirs(f'https://repo1.maven.org/maven2/org/apache/{pmc}/')))))

def get_dt_projects():
    req = request.Request('https://security-tools-ec2-va.apache.org/api/v1/project?excludeInactive=true&onlyRoot=false&pageSize=1000&pageNumber=1')
    req.add_header('X-Api-Key', dt_api_key)
    with request.urlopen(req) as res:
        result = {}
        for p in json.load(res):
            if 'version' in p:
                result[f"{p['name']}-{p['version']}"] = p
        return result

dt_projects = get_dt_projects()

# TODO don't hardcode, maybe add another layer
pmc_uuids = {
    'arrow': '11fd86d9-b646-4808-a731-5ddffe6fb71e',
    'commons': 'c2a20d87-386d-45df-af14-3426b470b4ab'
}

def get_or_create_dt_project(pmc, friendly_name, version):
    global dt_projects, pmc_uuids

    if f"{friendly_name}-{version}" in dt_projects:
        print("Project exists, just update")
    else:
        project = {
            'active': True,
            'name': friendly_name,
            'version': version,
            # TODO don't hardcode
            'classifier': 'LIBRARY',
            'parent': {
                'uuid': pmc_uuids[pmc]
            }
        }
        with requests.put(
            'https://security-tools-ec2-va.apache.org/api/v1/project',
            headers={
                'X-Api-Key': dt_api_key,
                'Content-Type': 'application/json'
            },
            data=json.dumps(project)
        ) as res:
            print(res.status_code)

    dt_projects = get_dt_projects()
    return dt_projects[f"{friendly_name}-{version}"]

for project in maven_projects(pmc):
    friendly_name = 'Apache ' + project.replace('-', ' ').title()
    print(project)

    index = get_dirs(f'https://repo1.maven.org/maven2/org/apache/{pmc}/{project}')
    def version_name(link):
        return link.get('title')[:-1]
    def is_version(v):
        # TODO support milestones?
        return not 'M' in v
    versions = list(filter(is_version, list(map(version_name, index))))
    versions.sort(key=Version)
    if versions:
        lastVersion = versions[-1]
        print(lastVersion)
        index = get_files(f'https://repo1.maven.org/maven2/org/apache/{pmc}/{project}/{lastVersion}')
        def file_name(link):
            return link.get('title')
        def is_sbom(name):
            return name.endswith('-cyclonedx.json')
        sboms = list(filter(is_sbom, map(file_name, index)))
        if sboms:
            dt_project = get_or_create_dt_project(pmc, friendly_name, lastVersion)
            sbom = sboms[0]
            with request.urlopen(f'https://repo1.maven.org/maven2/org/apache/{pmc}/{project}/{lastVersion}/{sbom}') as sbomPayload:
                with requests.post(
                    'https://security-tools-ec2-va.apache.org/api/v1/bom',
                    headers={'X-Api-Key': dt_api_key},
                    files=dict(
                        project=dt_project['uuid'],
                        bom=sbomPayload.read()
                    )
                ) as res:
                    print(res)
