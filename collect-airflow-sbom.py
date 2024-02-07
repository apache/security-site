#!/usr/bin/env python3

from bs4 import BeautifulSoup
from common import get_files, dt_pmc, post_sbom
import os
import re

baseurl = "https://airflow.apache.org/docs/apache-airflow/stable/sbom/"

files = list(map(lambda e: e.get('href'), get_files(baseurl)))
files.sort()
file = files[0]

match = re.search('apache-airflow-sbom-(.*)-python3.\d+.json', file)
version = match.group(1)

pmc = dt_pmc("airflow")
pmc_uuid = pmc['uuid']
post_sbom(pmc, pmc_uuid, "Apache Airflow", version, f'{baseurl}/{file}')


