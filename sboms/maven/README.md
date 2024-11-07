Apache Maven SBOMs
==================

Generated with CycloneDX Maven Plugin, published to Maven Central.

Apache download area [current](https://dlcdn.apache.org/maven/) / [archives](https://archive.apache.org/dist/maven/):
- most releases are libraries published as `-source-release.zip`, with convenience binaries in Maven Central,
- a few releases as src+bin for end users to install: Maven core `maven-2` `maven-3` `maven-4`, Maven Daemon `mvnd`, old `binaries` (Archiva, Continuum)

Only release binaries embed dependency libraries: we should check that SBOMs for these don't miss any embedded library\
=> `check-maven-bin.sh {version}`

Libraries releases don't embed any library in general, just "soft reference" them: only a few cases with shading partially embed a few dependencies (examples TBD...).
