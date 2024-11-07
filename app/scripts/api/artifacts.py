import ahapi
import typing
import aiohttp
import os

async def process(state: typing.Any, request, formdata: dict) -> typing.Any:
    artifacts = []
    for (root, _, files) in os.walk("./sboms/"):
        if len(files) != 0:
            pmc = root.split('/')[2]
            artifact = '/'.join(root.split('/')[3:-1])
            if artifact and not (pmc, artifact) in artifacts:
                artifacts.append((pmc, artifact))
    return artifacts
 
def register(state: typing.Any):
    return ahapi.endpoint(process)
