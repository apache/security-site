import ahapi
import aiohttp
import os
from lib4sbom.parser import SBOMParser
import typing

sbomdir = os.path.realpath('./sboms')

def get_purl(package):
    if 'purl' in package:
        return package['purl']
    if 'externalreference' in package:
        for (_, t, r) in package['externalreference']:
            if t == 'purl':
                return r
    print(f"Could not determine purl for {package['name']}")
    return None

def dependency(package):
    purl = get_purl(package)
    if purl:
        pre, post = purl.split("@", 1)
        return pre, post.split("?")[0]
    else:
        return package['name'], package['version']

def load_sbom(artifact, version):
    path = './sboms/' + artifact + '/' + version
    if os.path.commonprefix((os.path.realpath(path), sbomdir)) != sbomdir:
        raise ValueError("Unexpected path")
    for sbom in os.scandir(path):
        print(f"Using {path}/{sbom.name}")
        parser = SBOMParser()
        parser.parse_file(path + '/' + sbom.name)
        return list(map(dependency, parser.get_packages()))
    raise ValueError("No SBOM found")

async def process(state: typing.Any, request, formdata: dict) -> typing.Any:
    sbom1 = load_sbom(formdata['artifact'], formdata['version'])
    if 'version2' in formdata and formdata['version'] != formdata['version2']:
        purls1 = [ purl for (purl, _) in sbom1 ]
        sbom2 = { purl:version for (purl, version) in load_sbom(formdata['artifact'], formdata['version2']) }
        def complete(dep):
            (purl, version) = dep
            if purl in sbom2:
                return (purl, version, sbom2[purl])
            else:
                return (purl, version, None)
        completed = list(map(complete, sbom1))
        extra = [ (purl, None, sbom2[purl]) for purl in sbom2 if purl not in purls1 ]
        return completed + extra
    else:
        return sbom1

def register(state: typing.Any):
    return ahapi.endpoint(process)
