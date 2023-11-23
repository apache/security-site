{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.hugo
    pkgs.python3
    pkgs.less
  ];
  shareNet = false;
}
