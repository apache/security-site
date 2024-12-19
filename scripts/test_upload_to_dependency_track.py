import pytest
from upload_to_dependency_track import *

def test_friendly_name():
    assert parse_friendly_name_and_version("sboms/maven/maven/org.apache.maven.plugin-tools/maven-plugin-tools-generators/4.0.0-beta-1/maven-plugin-tools-generators-4.0.0-beta-1-cyclonedx.json") == ("Apache Maven Plugin Tools Generators", "4.0.0-beta-1")
    assert parse_friendly_name_and_version("sboms/airflow/pypi/apache-airflow/2.10.4/apache-airflow-sbom-2.10.4-python3.9.json") == ("Apache Airflow python3.9", "2.10.4")
    assert parse_friendly_name_and_version("sboms/camel/maven/org.apache.camel.kamelets/camel-kamelets/4.9.0/camel-kamelets-4.9.0-sbom.json") == ("Apache Camel Kamelets", "4.9.0")
    assert parse_friendly_name_and_version("sboms/camel/maven/org.apache.camel.quarkus/camel-quarkus/3.17.0/apache-camel-quarkus-3.17.0-sbom.json") == ("Apache Camel Quarkus", "3.17.0")
    assert parse_friendly_name_and_version("sboms/camel/maven/org.apache.camel/camel/4.9.0/apache-camel-4.9.0-sbom.json") == ("Apache Camel", "4.9.0")

if __name__ == "__main__":
    pytest.main()
