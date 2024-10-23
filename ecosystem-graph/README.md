# ASF Ecosystem Graph

This script takes the SBOMs from this repository to build a graph showing which of our
artifacts depend on each other, across projects.

![example graph](./sample.png)

## Running

In the root of the repository, run 'python3 -m ecosystem-graph'. This will
(re)generate `ecosystem-graph/ecosystem.json`.

## Viewing

in the root of the repository, run `python3 -m app`
and visit http://127.0.0.1:8082/sbom/
