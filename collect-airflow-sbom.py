#!/usr/bin/env python3

from bs4 import BeautifulSoup
from common import get_files, get_sbom_cached, dt_pmc, post_sbom
import os
import re

baseurl = "https://airflow.apache.org/docs/apache-airflow/stable/sbom/"

files = list(map(lambda e: e['href'], get_files(baseurl)))
files.sort()
file = files[0]

match = re.search('apache-airflow-sbom-(.*)-python3.\d+.json', file)
version = match.group(1)

pmc = dt_pmc("airflow")
pmc_uuid = pmc['uuid']
sbom = get_sbom_cached(f'{baseurl}/{file}', f"airflow/{file}")
post_sbom(pmc, pmc_uuid, "Apache Airflow", version, sbom)


