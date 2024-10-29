import ahapi
import typing
import aiohttp
import os

sbomdir = os.path.realpath('./sboms')

async def process(state: typing.Any, request, formdata: dict) -> typing.Any:
    versions = []
    artifact = formdata['artifact']
    path = './sboms/' + artifact
    if os.path.commonprefix((os.path.realpath(path), sbomdir)) != sbomdir:
        raise ValueError("unexpected path")
    for (root, dirnames, files) in os.walk(path):
        if len(files) != 0:
            version = root.split('/')[-1]
            if not version in versions:
                versions.append(version)
    return versions
 
def register(state: typing.Any):
    return ahapi.endpoint(process)
