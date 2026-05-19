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

class AppConfig(pydantic.BaseModel):
    data_dir: str
    """Base directory of issue metadata"""

    state_dir: str
    """Local persistent data"""

    @property
    def state_dir_path(self) -> pathlib.Path:
        return pathlib.Path(self.state_dir)

def load_app_config(cfg_path: pathlib.Path) -> AppConfig:
    import yaml

    if not cfg_path.exists():
        raise RuntimeError(f"Config file {cfg_path} does not exist")

    return AppConfig.model_validate(yaml.safe_load(cfg_path.read_text()))
