# ASF Ecosystem Graph

This script takes the SBOMs from this repository to build a graph showing which of our
artifacts depend on each other, across projects.

![example graph](./sample.png)

## Running

In the root of the repository, run 'python3 -m ecosystem-graph'. This will
(re)generate `ecosystem-graph/ecosystem.json`.

## Viewing

in `ecosystem-graph`, run `python3 -m http.server --bind 127.0.0.1`
and visit http://127.0.0.1:8000
