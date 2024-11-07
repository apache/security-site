#!/usr/bin/env python3
from common import dt_pmc, post_sbom
import json
import os
import sys

with open("scripts/sboms-from-maven-central.json") as data:
    maven_central = json.load(data)
    data.close()

with open("scripts/committees.json") as data:
    committees = json.load(data)
    data.close()
if len(sys.argv) > 1:
    committees = filter(lambda x: x["id"] == sys.argv[1], committees)

gh = None
def repos(pmc):
    global gh
    import github

    if not gh:
        gh = github.Github(os.environ['GITHUB_TOKEN'])
    repositories = gh.search_repositories(query=f"org:apache {pmc}")
    return filter(lambda x: x.name.startswith(pmc), repositories)

def sbom_from_gh(repo):
    import github
    # endpoint is not supported yet:
    # https://github.com/PyGithub/PyGithub/issues/2730
    # https://github.com/PyGithub/PyGithub/issues/3012
    from github.GithubObject import Attribute, CompletableGithubObject, NotSet
    from typing import Any
    class Sbom(CompletableGithubObject):
        def _initAttributes(self) -> None:
            self._sbom: Attribute[dict] = NotSet
            self._url: Attribute[str] = NotSet
        @property
        def sbom(self) -> dict:
            self._completeIfNotSet(self._sbom)
            return self._sbom
        @property
        def url(self) -> str:
            return self._url.value
        def _useAttributes(self, attributes: dict[str, Any]) -> None:
            print(attributes)
            if "sbom" in attributes:  # pragma no branch
                self._sbom = attributes["sbom"]
            if "url" in attributes:
                self._url = self._makeStringAttribute(attributes["url"])
    global gh
    if not gh:
        gh = github.Github(os.environ['GITHUB_TOKEN'])
    owner = "apache"
    obj = Sbom(gh._Github__requester, {}, {"url": f"/repos/{owner}/{repo}/dependency-graph/sbom"}, completed=False)
    return obj.sbom


for committee in committees:
    pmc = committee["id"]
    bespoke_script = f"scripts/collect-{pmc}-sboms.py"
    if os.path.exists(bespoke_script):
        print(f"exec'ing {bespoke_script}")
        status = os.system(f"python3 {bespoke_script}")
        if status != 0:
            print(f"Failed to execute {bespoke_script}: {status}")
            exit(1)
    elif pmc in maven_central:
        print(f"fetching {pmc} SBOMs from Maven Central")
        status = os.system(f"python3 scripts/collect-sboms-from-maven-central.py {pmc}")
        if status != 0:
            print(f"Failed to execute collect-sboms-from-maven-central.py {pmc}: {status}")
            exit(1)
    else:
        print("Fetching sbom from GitHub is not supported, https://github.com/DependencyTrack/dependency-track/discussions/1222")
        continue

        # TODO
        print(f"Trying to fetch SBOMs for {pmc} from GitHub")
        dtpmc = dt_pmc(pmc)
        for repo in repos(pmc):
            if repo.name == pmc:
                friendly_name = f"{committee["name"]} {repo.name}"
            else:
                friendly_name = f"{committee["name"]} {repo.name.replace(pmc + "-", "")}"
            sbom = json.dumps(sbom_from_gh(repo.name))
            print(f"SBOM to be submitted: {sbom}")
            post_sbom(dtpmc, dtpmc['uuid'], friendly_name, 'main', sbom)
