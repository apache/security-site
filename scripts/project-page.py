#!/usr/bin/env python3

import json
import os.path
from operator import itemgetter
from os.path import dirname, realpath
from collections import defaultdict
import subprocess
from urllib.request import urlopen

# manually maintained
with open('project-coordinates.json', 'r') as p:
    project_coordinates = json.load(p)

# fetched from https://projects.apache.org/json/foundation/committees.json
with open('committees.json', 'r') as cs:
    project_committees = { c['group']: c for c in json.load(cs) }

# fetched from https://projects.apache.org/json/foundation/committees-retired.json
with open('committees-retired.json', 'r') as cr:
    project_committees_retired = { c['id']: c for c in json.load(cr) }

# fetched from https://projects.apache.org/json/foundation/podlings-history.json
with open('podlings-history.json', 'r') as ph:
    m = json.load(ph)
    podlings_retired = { key: m[key] for key in m.keys() if m[key]['status'] == 'retired' }
    project_committees_retired = {**project_committees_retired, **podlings_retired}

# fetched from https://projects.apache.org/json/foundation/podlings.json
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
  elif pmc in project_committees:
    return project_committees[pmc]
  elif pmc in project_committees_retired:
    return project_committees_retired[pmc]


def fetch_cve(cve_id):
  print(cve_id)
  if not os.path.exists('cache/%s.json' % cve_id):
    f = urlopen('https://cveprocess.apache.org/publicjson/%s' % cve_id)
    with open('cache/%s.json' % cve_id, 'w') as d:
      d.write(f.read().decode('utf-8'))

  with open('cache/%s.json' % cve_id, 'r') as d:
    cve = json.loads(d.read())
    if 'containers' in cve.keys():
      return cve
    else:
      if not os.path.exists('cache-converted/%s.json' % cve_id):
        subprocess.run(['cve4to5up.py', '-i', 'cache/%s.json' % cve_id, '-o' 'cache-converted/'])
      with open('cache-converted/%s.json' % cve_id, 'r') as d:
        cve = json.loads(d.read())
        return cve

# Projects overview page
for pmc in sorted(set(list(project_coordinates.keys()) + list(advisories.keys()))):
    if pmc == 'dummy':
        continue
    if pmc in project_committees_retired.keys():
        continue

    p = coordinates(pmc)
    assert p, 'All projects with advisories, including [%s], should have coordinates' % pmc
    if 'link' in p.keys() and p['link']:
        projects_page.write('| [%s](%s) | ' % (p['name'], p['link']))
    else:
        projects_page.write("| %s | " % p['name'])

    if not 'contact' in p.keys() or p['contact'] == 'security@apache.org':
        projects_page.write(' [Apache Security Team](mailto:security@apache.org) |')
    else:
        projects_page.write(' [%s Security Team](mailto:%s) |' % (p['name'], p['contact']))

    if 'advisory_link' in p.keys() and p['advisory_link']:
        projects_page.write(' [Advisories](%s) |\n' % (p['advisory_link']))
    #elif len(advisories[pmc]) > 0:
    #    projects_page.write(' [Advisories](%s) |\n' % pmc)
    else:
        projects_page.write(' |\n')

for pmc in advisories.keys():
    if pmc == 'dummy':
        continue;
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
    if 'link' in p.keys() and p['link']:
        project_page.write("You can read more about the projects' security policy on their [security page](%s), and email your report to the " % p['link'])
    else:
        project_page.write('Send your report to the ')
    if not 'contact' in p.keys() or p['contact'] == 'security@apache.org':
        project_page.write('[Apache Security Team](mailto:security@apache.org).')
    else:
        project_page.write('[%s Security Team](mailto:%s).' % (p['name'], p['contact']))

    project_page.write('\n\n# Advisories')

    project_page.write('\n\nThis section is experimental: it provides advisories since 2023 and ')
    project_page.write('may lag behind the official CVE publications. ')
    if 'link' in p.keys() and p['link']:
        project_page.write('It may also lack details found on the [project security page](%s). ' % p['link'])

    project_page.write('If you have any feedback on how you would like this data to be provided, ')
    project_page.write('you are welcome to reach out on our public [mailinglist](/mailinglist) or privately ')
    project_page.write('on [security@apache.org](mailto:security@apache.org)')
    project_page.write('\n{.bg-warning}')

    for advisory in sorted(advisories[pmc], key=itemgetter('ID'), reverse=True):
        cve_id = advisory['ID']
        cve = fetch_cve(cve_id)

        with open(staticdir + cve_id + '.cve.json', 'w') as cveFile:
          cve_doc = {
            "containers": cve['containers'],
            "cveMetadata": cve['cveMetadata'],
            "dataType": cve['dataType'],
            "dataVersion": cve['dataVersion'],
          }
          json.dump(cve_doc, cveFile, ensure_ascii=True, indent=2)

        has_osv = True
        if subprocess.call(['./cve2osv.py', staticdir + cve_id + '.cve.json', staticdir + cve_id + '.osv.json']) != 0:
          has_osv = False

        project_page.write("\n\n## %s ## { #%s }\n\n" % (advisory['title'], cve_id))
        project_page.write("%s [\\[CVE\\]](https://cve.org/CVERecord?id=%s) [\\[CVE json\\]](./%s.cve.json)" % (cve_id, cve_id, cve_id))
        if has_osv:
          project_page.write(" [\\[OSV json\\]](./%s.osv.json)\n\n" % cve_id)
        project_page.write("\n\n")
        project_page.write("_Last updated: %s_" % advisory['updated'])
        project_page.write("\n\n")

        cna = cve['containers']['cna']
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
          if 'supportingMedia' in desc.keys():
            for media in desc['supportingMedia']:
              project_page.write(media['value'])
          else:
            project_page.write(desc['value'])

        if 'references' in cna.keys():
          project_page.write('\n\n### References\n')
          for reference in cna['references']:
            project_page.write('* %s\n' % reference['url'])

        if 'credits' in cna.keys():
          project_page.write('\n\n### Credits\n')
          for credit in cna['credits']:
            if 'type' in credit.keys():
              project_page.write('* %s (%s)\n' % (credit['value'], credit['type']))
            else:
              project_page.write('* %s\n' % credit['value'])

