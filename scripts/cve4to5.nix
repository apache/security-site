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
    rev = "9d22833a2cafa48da9bb58479232d09e9b2cd5f2";
    hash = "sha256-Thc7ZOIZZtRiXcCAMuIGJei4tJVeaOfTRrN9YhOftJQ=";
  };

  sourceRoot = "source/schema/v5.0/support/CVE_4_to_5_converter";
  #sourceRoot = "cve-schema/schema/v5.0/support/CVE_4_to_5_converter";

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
