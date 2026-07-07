{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.hugo
    pkgs.python3
    pkgs.less
    pkgs.curl
    (pkgs.callPackage ./scripts/cve4to5.nix {})
  ];
  shareNet = false;
}
