# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import pathlib
import pydantic
from asfquart.base import QuartApp
from typing import cast

class ServerConfig(pydantic.BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080
    access_log: str = "-"
    error_log: str = "-"

    @property
    def bind(self) -> str:
        return f"{self.host}:{self.port}"

class AppConfig(pydantic.BaseModel):
    data_dir: str
    """Base directory of issue metadata"""

    state_dir: str
    """Local persistent data"""

    pmcs_with_security_emails: list[str] = []
    """PMCs that have a dedicated security@ list"""

    pmcs_using_jira: dict[str, str] = {}
    """PMCs that track security issues in (private) Jira issues"""

    pmcs_using_github: dict[str, str] = {}
    """PMCs that track security issues in (private) GitHub issues"""

    pmcs_with_subprojects: list[str] = []
    """PMCs whose reports are split across subprojects."""

    server: ServerConfig = ServerConfig()

    @property
    def data_dir_path(self) -> pathlib.Path:
        return pathlib.Path(self.data_dir)

    @property
    def state_dir_path(self) -> pathlib.Path:
        return pathlib.Path(self.state_dir)

def load_app_config(cfg_path: pathlib.Path) -> AppConfig:
    import yaml

    if not cfg_path.exists():
        raise RuntimeError(f"Config file {cfg_path} does not exist")

    return AppConfig.model_validate(yaml.safe_load(cfg_path.read_text()))

def setup_app_config(quart_app: QuartApp, app_config: AppConfig) -> None:
    quart_app.extensions["app_config"] = app_config

def get() -> AppConfig:
    import asfquart

    return cast("AppConfig", asfquart.APP.extensions["app_config"])

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("--bind", action="store_true")
    parser.add_argument("--access-log", action="store_true")
    parser.add_argument("--error-log", action="store_true")
    parser.add_argument("--pid-file", action="store_true")
    args = parser.parse_args(sys.argv[1:])

    if args.bind:
        config = load_app_config(pathlib.Path("config.yaml"))
        print(config.server.bind)

    if args.access_log:
        config = load_app_config(pathlib.Path("config.yaml"))
        print(config.server.access_log)

    if args.error_log:
        config = load_app_config(pathlib.Path("config.yaml"))
        print(config.server.error_log)

    if args.pid_file:
        config = load_app_config(pathlib.Path("config.yaml"))
        print(config.base.state_dir_path / "dashboard-config.pid")
