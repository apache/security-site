{ stdenv
, fetchFromGitHub
, python3
, lib
}:

let 
  python = python3.withPackages(p: [
    p.jsonschema
    p.requests
    p.cvss
    p.dateutil
    p.langcodes
    p.progress
  ]);
in
stdenv.mkDerivation {
  pname = "cve4to5up";
  version = "snapshot";

  #src = /home/aengelen/dev/CVEProject/cve-schema;
  src = fetchFromGitHub {
    owner = "raboof";
    repo = "cve-schema";
    # 'standalone-cve4to5' branch
    rev = "ed4bbfa052f69c5ccc574ca312693fc0847e4bcb";
    hash = "sha256-phbT12Cyvvq/WRb804JA+jKv2+HI1VWfPWltU3dotek=";
  };

  sourceRoot = "source/schema/v5.0/support/CVE_4_to_5_converter";

  installPhase = ''
    runHook preInstall

    mkdir -p $out/bin
    cp ref_tag_map.json PUBLISHED_CVE_JSON_5.0_bundled.json $out/bin

    echo '#!${lib.getExe python}' > $out/bin/cve4to5up.py
    cat cve4to5up.py >> $out/bin/cve4to5up.py
    chmod a+x $out/bin/cve4to5up.py

    runHook postInstall
  '';
}
