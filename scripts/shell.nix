{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = [
    (pkgs.python3.withPackages(p: [
      p.python-slugify
      p.rdflib
    ]))
    (pkgs.callPackage ./cve4to5.nix {})
  ];
}
