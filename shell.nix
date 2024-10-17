{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = [
    (pkgs.python3.withPackages(p: [
      p.beautifulsoup4
      p.requests
      p.packaging
      p.python-dotenv

      p.pygithub

      # for ecosystem.py
      p.lib4sbom
      p.networkx
    ]))
  ];
  shareNet = true;
}
