#!/usr/bin/env python3

# Script to convert CVEs as published for Apache projects
# from CVE JSON 5.0 format to OSV format.

import json
import sys

# TODO get from arg
cve = json.load(open(sys.argv[1]))

def mavenPackage(groupId, artifactId):
  return {
    'ecosystem': 'Maven',
    'name': f"{groupId}:{artifactId}",
    'purl': f"pkg:maven/{groupId}/{artifactId}"
  }

def package(product):
  if product == 'Apache Commons IO':
    return mavenPackage('org.apache.commons', 'commons-io')
  else:
    raise ValueError(f'Cannot infer package for product {product}')

def range(versions):
  if versions['status'] != 'affected':
    raise "TODO support for explicitly 'unaffected' ranges"
  if 'lessThan' in versions:
    events = [{
        'introduced': versions['version']
    },{
        'fixed': versions['lessThan']
    }]
  else:
    events = [{
        'introduced': versions['version']
    },{
        'last_affected': versions['version']
    }]

  return {
    'type': 'SEMVER',
    'events': events
  }

def convert_affected(affected):
  return {
    'package': package(affected['product']),
    # TODO severity
    'ranges': list(map(range, affected['versions'])),
  }

def reference(reference):
  url = reference['url']
  if 'jira' in url:
    t = 'REPORT'
  elif 'x_refsource_CONFIRM' in reference['tags']:
    t = 'ADVISORY'
  else:
    t = 'WEB'
  return {
    'type': t,
    'url': reference['url']
  }

cna = cve['containers']['cna']
osv = {
  'schema_version': '1.6.1',
  'id': cve['cveMetadata']['cveId'],
  'summary': cna['title'],
  'details': cna['descriptions'][0]['value'],
  # TODO 'severity'
  'affected': list(map(convert_affected, cna['affected'])),
  'references': list(map(reference, cna['references']))
  # TODO 'credits'
}

with open(sys.argv[2], 'w', encoding='utf-8') as f:
    json.dump(osv, f, ensure_ascii=False)
