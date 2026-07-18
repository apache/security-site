#!/usr/bin/env python3

import html
import json
import os.path
from operator import itemgetter
from os.path import dirname, realpath
from collections import defaultdict
import subprocess
from urllib.request import urlopen
from urllib.parse import urlparse, quote

# manually maintained
with open('project-coordinates.json', 'r') as p:
    # Drop editor-only meta keys (e.g. "$schema"); every remaining key is a project.
    project_coordinates = {k: v for k, v in json.load(p).items() if not k.startswith('$')}

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

To report a vulnerability in an Apache project that is not listed below, contact the [Apache Security Team](mailto:security@apache.org?subject=Project%20name%20here).

Use the tabs below to jump to projects by their initial. Every project lists a security contact; some also publish a security page and a list of advisories.
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

# Projects overview page, rendered as Ponymail-style alphabetical tabs.
def display_name(name):
    return name[len('Apache '):].lstrip() if name.startswith('Apache ') else name

def project_letter(name):
    d = display_name(name)
    c = d[0].upper() if d else '#'
    return c if c.isalpha() else '#'

def security_models(p):
    # The PMC's own security model first, then one per project it ships that
    # publishes a model of its own. Most PMCs have only the umbrella entry; a
    # PMC with several projects carries a "projects" list in the coordinates.
    models = []
    if p.get('security_model_link'):
        models.append((p['name'], p['security_model_link']))
    for project in p.get('projects') or []:
        if project.get('security_model_link'):
            models.append((project['name'], project['security_model_link']))
    return models

def security_model_md_lines(models, indent):
    # One Markdown list item per security model, each labelled with the name of the project it covers.
    # Callers supply the indent the surrounding list needs.
    return ['%s- [%s security model](%s)' % (indent, name, link) for name, link in models]

def project_md_lines(pmc, p):
    # Each project is a Markdown list item: a bold name plus a nested list of
    # labelled links. Security contact comes first and is always present.
    if not p.get('contact') or p['contact'] == 'security@apache.org':
        # The shared Security Team list handles every project, so name the
        # project in the subject to help routing.
        contact_addr = 'security@apache.org'
    else:
        # A project-specific list already knows which project it is.
        contact_addr = p['contact']
    quoted_subject = quote(display_name(p['name']))
    # Standard mailto: a bare address plus a prefilled subject, so no mail
    # client trips over a non-standard "Name <address>" recipient.
    contact_href = 'mailto:%s?subject=%s' % (quote(contact_addr, safe='@'), quoted_subject)
    # Optional logo floated to the card's right (see custom.css). Only projects
    # that publish a logo carry a logo_link in project-coordinates.json; the
    # inline HTML <img> passes through Goldmark (unsafe=true) and the **name**
    # after it is still parsed as Markdown bold.
    name_md = '**%s**' % p['name']
    if p.get('logo_link'):
        name_md = '<img class="project-logo" src="%s" alt="" loading="lazy"> %s' % (
            html.escape(p['logo_link'], quote=True), name_md)
    lines = [
        '- %s' % name_md,
        # The required contact is shown on its own line as the bare address, so
        # the reader sees exactly where the report goes. The label is bold to
        # stand out.
        '  - **Security contact:**\\',
        '    [%s](%s)' % (contact_addr, contact_href)
    ]
    if p.get('advisory_link'):
        lines.append('  - Advisories:\\')
        lines.append('    [%s](%s)' % (urlparse(p['advisory_link']).netloc or 'advisories', p['advisory_link']))
    else:
        # Fall back to the generated per-project page
        lines.append('  - Advisories (experimental):\\')
        if pmc in advisories:
            # A page exists for this project, so link to it.
            lines.append('    [security.apache.org](/projects/%s/)' % pmc)
        else:
            lines.append('    none so far')
    models = security_models(p)
    if models:
        lines.append('  - Security model:' if len(models) == 1 else '  - Security models:')
        lines += security_model_md_lines(models, '    ')
    return lines

# Group projects by their initial letter (non-letters bucket under '#').
overview = defaultdict(list)
for pmc in sorted(set(list(project_coordinates.keys()) + list(advisories.keys()))):
    if pmc == 'dummy':
        continue
    if pmc in project_committees_retired.keys():
        continue

    p = coordinates(pmc)
    assert p, 'All projects with advisories, including [%s], should have coordinates' % pmc
    overview[project_letter(p['name'])].append((display_name(p['name']).lower(), pmc, p))

# Letters A-Z first, then the '#' bucket for anything non-alphabetic.
letters = sorted(overview.keys(), key=lambda c: (c == '#', c))

# Only the tab controls need to be HTML: the container, nav and buttons. Each
# panel is an HTML <section> so the tab script can show/hide it, but a blank
# line after the opening tag hands control back to Goldmark, so the heading and
# the project list inside are plain Markdown. Wrapper tags stay at column 0 so
# Goldmark keeps recognising them as HTML blocks rather than indented code.
lines = [
    '<div id="project-tabs" class="project-tabs">',
    '<nav class="project-tabs-nav" role="tablist" aria-label="Projects by initial">',
]
for i, letter in enumerate(letters):
    lines.append('  <button type="button" class="project-tab%s" role="tab" data-letter="%s" aria-selected="%s">%s</button>' % (
        ' active' if i == 0 else '', letter, 'true' if i == 0 else 'false', letter))
lines.append('</nav>')
lines.append('<div class="project-tabs-panels">')
for i, letter in enumerate(letters):
    lines.append('<section class="project-tab-panel%s" role="tabpanel" data-letter="%s">' % (
        ' active' if i == 0 else '', letter))
    lines.append('')
    lines.append('## %s {.panel-letter}' % letter)
    lines.append('')
    for _, pmc, p in sorted(overview[letter], key=lambda e: e[0]):
        lines += project_md_lines(pmc, p)
    lines.append('')
    lines.append('</section>')
lines.append('</div>')
lines.append('</div>')
projects_page.write('\n' + '\n'.join(lines) + '\n')

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
    models = security_models(p)
    project_page.write('# Reporting\n\n')
    project_page.write('Do you want disclose a potential security issue for %s? ' % p['name'])
    project_page.write('Send your report to the ')
    quoted_subject = quote(display_name(p['name']))
    if not 'contact' in p.keys() or p['contact'] == 'security@apache.org':
        project_page.write('[Apache Security Team](mailto:security@apache.org?subject=%s).' % quoted_subject)
    else:
        project_page.write('[%s Security Team](mailto:%s?subject=%s).' % (p['name'], quote(p['contact'], safe='@'), quoted_subject))
    if models:
        # A PMC that ships several projects publishes one security model per
        # project, so these are listed rather than woven into the sentence.
        project_page.write("\n\nYou can read more about the security policy on:\n\n")
        project_page.write('\n'.join(security_model_md_lines(models, '')))
        project_page.write('\n')

    project_page.write('\n\n# Advisories')

    project_page.write('\n\nThis section is experimental: it provides advisories since 2023 and ')
    project_page.write('may lag behind the official CVE publications. ')
    if models:
        project_page.write('It may also lack details found on the project security page%s linked above. ' % (
            's' if len(models) > 1 else ''))

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
            if version['status'] != 'affected':
              project_page.write(' ' + version['status'])
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

