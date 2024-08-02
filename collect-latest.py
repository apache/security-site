import json
import os
import sys

with open("sbom-locations.json") as data:
    locations = json.load(data)
    data.close()

if len(sys.argv) > 1:
    committees = [ { "id": sys.argv[1] } ]
else:
    with open("committees.json") as data:
        committees = json.load(data)
        data.close()

for committee in committees:
    pmc = committee["id"]
    bespoke_script = f"./collect-{pmc}-sboms.py"
    if os.path.exists(bespoke_script):
        print(f"exec'ing {bespoke_script}")
        status = os.system(f"python3 {bespoke_script}")
        if status != 0:
            print(f"Failed to execute {bespoke_script}: {status}")
            exit(1)
    elif pmc in locations and locations[pmc]['type'] == "maven":
        print(f"fetching {pmc} SBOMs from Maven Central")
        status = os.system(f"python3 collect-maven-sboms.py {pmc}")
        if status != 0:
            print(f"Failed to execute {bespoke_script}: {status}")
            exit(1)
    else:
        print(f"Don't know how to fetch SBOM for {pmc}")

