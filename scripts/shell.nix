{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    (pkgs.callPackage ./cve4to5.nix {})
  ];
}
