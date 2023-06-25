#!/usr/bin/env python3

import json
import os.path
from os.path import dirname, realpath
from collections import defaultdict
from urllib.request import urlopen

# (for now) generated from https://apache.org/security/projects.html by get-projects.py
with open('project-coordinates.json', 'r') as p:
    project_coordinates = json.load(p)

# fetched from https://projects.apache.org/json/foundation/committees.json
with open('committees.json', 'r') as cs:
    project_committees = { c['id']: c for c in json.load(cs) }

with open('podlings.json', 'r') as ps:
    project_committees = {**project_committees, **(json.load(ps))}

# fetched from https://cveprocess.apache.org/publicjson
with open('publicjson', 'r') as p:
    advisories = defaultdict(list)
    for advisory in json.load(p):
        advisories[advisory['owner']].append(advisory)

projects_page = open(dirname(realpath(__file__)) + '/../content/projects/_index.md', 'w')

projects_page.write("""---
title: Apache Project Security Information
description: Security information for individual Apache projects
layout: single
---

Here is a list of pages ASF projects maintain to provide information on known security vulnerabilities. Each entry also has the security contact for reporting new vulnerabilities related to that project. Note that not all project security teams have a dedicated address for reporting new vulnerabilities.

To report a vulnerability in an Apache project that is not listed below, contact the [Apache Security Team](mailto:security@apache.org).

| Project security page | Contact | |
| --- | --- | --- |
""")

def coordinates(pmc):
  if pmc in project_coordinates.keys():
    return project_coordinates[pmc]
  else:
    return project_committees[pmc]

for pmc in sorted(set(list(project_coordinates.keys()) + list(advisories.keys()))):
    p = coordinates(pmc)
    assert p, 'All projects with advisories, including [%s], should have coordinates' % pmc
    if 'link' in p.keys():
        projects_page.write('| [%s](%s) | ' % (p['name'], p['link']))
    else:
        projects_page.write("| %s | " % p['name'])

    if not 'contact' in p.keys() or p['contact'] == 'security@apache.org':
        projects_page.write(' [Apache Security Team](mailto:security@apache.org) |')
    else:
        projects_page.write(' [%s Security Team](mailto:%s) |' % (p['name'], p['contact']))

    #if len(advisories[pmc]) > 0:
    #    projects_page.write(' [Advisories](%s) |\n' % pmc)
    #else:
    projects_page.write(' |\n')

for pmc in advisories.keys():
    basedir = '%s/../content/projects/%s/' % (dirname(realpath(__file__)), pmc)
    os.makedirs(basedir, exist_ok=True)
    staticdir = '%s/../static/projects/%s/' % (dirname(realpath(__file__)), pmc)
    os.makedirs(staticdir, exist_ok=True)

    project_page = open(basedir + '/_index.md', 'w')
    p = coordinates(pmc)
    project_page.write("""---
title: %s security advisories
description: Security information for %s
layout: single
---

""" % (p['name'], p['name']))
    project_page.write('# Reporting\n\n')
    project_page.write('Do you want disclose a potential security issue for %s? ' % p['name'])
    if 'link' in p.keys():
        project_page.write("You can read more about the projects' security policy on their [security page](%s), and email your report to the " % p['link'])
    else:
        project_page.write('Send your report to the ')
    if not 'contact' in p.keys() or p['contact'] == 'security@apache.org':
        project_page.write(' [Apache Security Team](mailto:security@apache.org).')
    else:
        project_page.write(' [%s Security Team](mailto:%s).' % (p['name'], p['contact']))

    project_page.write('\n\n# Advisories')

    project_page.write('\n\nThis page is experimental: it provides consistent access to the advisories for %s since 2023 in text and CVE JSON format. ' % p['name'])
    project_page.write('It may lag slighly behind the official CVE publications. ')
    if 'link' in p.keys():
        project_page.write('It may also lack details found on the [project security page](%s).' % p['link'])

    project_page.write('\n\nIf you have any feedback on how you would like this data to be presented, ')
    project_page.write('you are welcome to reach out on our public [mailinglist](/mailinglist) or privately ')
    project_page.write('on [security@apache.org](mailto:security@apache.org)')

    for advisory in advisories[pmc]:
        cve = advisory['ID']
        project_page.write("\n\n## %s ## { #%s }\n\n" % (advisory['title'], cve))
        project_page.write("[%s](./%s.cve.json)\n\n" % (cve, cve))
        if not os.path.exists('cache/%s.json' % cve):
            f = urlopen('https://cveprocess.apache.org/publicjson/%s' % cve)
            with open('cache/%s.json' % cve, 'w') as d:
                d.write(f.read().decode('utf-8'))


        with open('cache/%s.json' % cve, 'r') as d:
            details = json.loads(d.read())
            cna = details['containers']['cna']
            project_page.write("### Affected\n\n")
            for affected in cna['affected']:
                for version in affected['versions']:
                    project_page.write('* ' + affected['product'])
                    if version['version'] != '0':
                        if 'lessThan' in version.keys() or 'lessThanOrEqual' in version.keys():
                            project_page.write(' from ')
                        else:
                            project_page.write(' at ')
                        project_page.write(version['version'])
                    if 'lessThan' in version.keys():
                        project_page.write(' before ' + version['lessThan'])
                    if 'lessThanOrEqual' in version.keys():
                        project_page.write(' through ' + version['lessThanOrEqual'])
                    project_page.write('\n')
            project_page.write('\n\n### Description\n\n')
            for desc in cna['descriptions']:
                for media in desc['supportingMedia']:
                    project_page.write(media['value'])

            if 'references' in cna.keys():
                project_page.write('\n\n### References\n')
                for reference in cna['references']:
                    project_page.write('* %s\n' % reference['url'])

            with open(staticdir + cve + '.cve.json', 'w') as cveFile:
                cve_doc = {
                    "containers": details['containers'],
                    "cveMetadata": details['cveMetadata'],
                    "dataType": details['dataType'],
                    "dataVersion": details['dataVersion'],
                }
                json.dump(cve_doc, cveFile, ensure_ascii=True, indent=2)
