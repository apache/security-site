#!/usr/bin/env python3

# Upload all sboms (that aren't yet) to dependency-track

from dotenv import load_dotenv
import json
import os
from pathlib import Path
import requests
from urllib import error, request

load_dotenv()
dt_api_key = os.getenv('DT_API_KEY')

def get_dt_projects():
    req = request.Request('https://security-tools-ec2-va.apache.org/api/v1/project?excludeInactive=true&onlyRoot=false&pageSize=5000&pageNumber=1')
    if not dt_api_key:
        raise ValueError("This script wants to write to DependencyTrack, but DT_API_KEY was not set.")
    req.add_header('X-Api-Key', dt_api_key)
    with request.urlopen(req) as res:
        projects = {}
        pmcs = {}
        for p in json.load(res):
            if 'version' in p:
                projects[f"{p['name']}-{p['version']}"] = p
            else:
                pmcs[p['name']] = p
        print(f"Number of projects: {len(projects)}")
        print(f"Number of PMCs: {len(pmcs)}")
        return projects, pmcs

def dt_pmc(pmc):
    global dt_pmcs
    friendly_name = 'Apache ' + pmc.title()
    if not friendly_name in dt_pmcs:
        project = {
            'active': True,
            'name': friendly_name,
            # TODO don't hardcode
            'classifier': 'LIBRARY',
        }
        with requests.put(
            'https://security-tools-ec2-va.apache.org/api/v1/project',
            headers={
                'X-Api-Key': dt_api_key,
                'Content-Type': 'application/json'
            },
            data=json.dumps(project)
        ) as res:
            if res.status_code == 403:
                print(f"403 creating PMC: missing authorization PORTFOLIO_MANAGEMENT")
            else:
                print(f"Created PMC: {res.status_code}")
        _, dt_pmcs = get_dt_projects()

    return dt_pmcs[friendly_name]

def get_or_create_dt_project(pmc, pmc_uuid, project_friendly_name, version):
    global dt_projects

    if f"{project_friendly_name}-{version}" in dt_projects:
        print(f"Updating {project_friendly_name} {version}")
    else:
        print(f"Creating {project_friendly_name} {version}")
        project = {
            'active': True,
            'name': project_friendly_name,
            'version': version,
            # TODO don't hardcode
            'classifier': 'LIBRARY',
            'parent': {
                'uuid': pmc_uuid
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
            if res.status_code != 201:
                print(f"Unexpected result code: {res.status_code}")

        # TODO optimization: instead of fetching the projects again,
        # we could get the uuid from the res.text
        dt_projects, _ = get_dt_projects()
    return dt_projects[f"{project_friendly_name}-{version}"]

def post_sbom(pmc, pmc_uuid, friendly_name, lastVersion, sbom):
    dt_project = get_or_create_dt_project(pmc, pmc_uuid, friendly_name, lastVersion)
    with requests.post(
        'https://security-tools-ec2-va.apache.org/api/v1/bom',
        headers={'X-Api-Key': dt_api_key},
        files=dict(
            project=dt_project['uuid'],
            bom=sbom
        )
    ) as res:
        if res.status_code != 200:
            raise Exception(f"Submitting SBOM for {friendly_name} failed: {res.status_code}: {res.text}")

def parse_friendly_name_and_version(sbom):
    parts = sbom.split("/")
    pmc = parts[1].capitalize()
    purl_type = parts[2]
    if len(parts) == 7:
        purl_namespace = parts[3]
        purl_name = parts[4]
        purl_version = parts[5]
        filename = parts[6]
    else:
        purl_namespace = None
        purl_name = parts[3]
        purl_version = parts[4]
        filename = parts[5]
    component = purl_name.replace('apache-', '').replace('-', ' ').title().replace(f"{pmc}", '').strip()
    if component != '':
        component = ' ' + component
    split = filename.replace('cyclonedx', '').replace('spdx', '').replace('sbom', '').split(purl_version + "-")
    variant = ''
    if len(split) > 1:
        variant = '.'.join(split[-1].split('.')[:-1])
        if variant != '':
            variant = ' ' + variant
    return ("Apache " + pmc.capitalize() + component + variant, purl_version)

if __name__ == "__main__":
    dt_projects, dt_pmcs = get_dt_projects()

    for pmcdir in os.scandir("sboms/"):
        pmc = pmcdir.name
        for (root, _, files) in os.walk(f"sboms/{pmc}/"):
            for file in files:
                marker = Path(f"{root}/{file}.uploaded")
                if (not file.endswith("md") and
                        not file.endswith("uploaded") and
                        not marker.exists()):
                    pmc_uuid = dt_pmc(pmc)['uuid']
                    filename = f"{root}/{file}"
                    (friendly_name, version) = parse_friendly_name_and_version(filename)
                    with open(filename, "r") as i:
                        sbom = i.read()
                        post_sbom(pmc, pmc_uuid, friendly_name, version, sbom)
                        marker.touch()
