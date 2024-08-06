from bs4 import BeautifulSoup
from dotenv import load_dotenv
import json
import os
import requests
from urllib import request

load_dotenv()
dt_api_key = os.getenv('DT_API_KEY')

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
    def as_dict(tag):
        return {
            'title': tag.get('title'),
            'href': tag.get('href'),
        }
    return list(map(as_dict, filter(is_dir, tags)))

def get_sbom_cached(url, to):
    filename = "sboms/" + to
    if not os.path.exists(filename):
        os.makedirs(os.path.abspath(os.path.join(filename, os.pardir)), exist_ok=True)
        with request.urlopen(url) as sbomPayload:
            with open(filename, "w") as out:
                out.write(sbomPayload.read().decode('utf-8'))
    with open(filename, "r") as i:
        return i.read()

def get_dt_projects():
    req = request.Request('https://security-tools-ec2-va.apache.org/api/v1/project?excludeInactive=true&onlyRoot=false&pageSize=1000&pageNumber=1')
    req.add_header('X-Api-Key', dt_api_key)
    with request.urlopen(req) as res:
        projects = {}
        pmcs = {}
        for p in json.load(res):
            if 'version' in p:
                projects[f"{p['name']}-{p['version']}"] = p
            else:
                pmcs[p['name']] = p
        return projects, pmcs

dt_projects, dt_pmcs = get_dt_projects()

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
        print("Project exists, just update")
    else:
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
            print(res.status_code)

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
        print(sbom)
        if res.status_code != 200:
            raise Exception(f"Submitting SBOM for {friendly_name} failed: {res.status_code}: {res.text}")
