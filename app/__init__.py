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

"""Security issue dashboard for the Apache Software Foundation"""

from app import reports, utils
from app.config import AppConfig
import asfquart
import asfquart.auth
import os
import pathlib
from typing import Any
import quart

def _ensure_state_dir(app_config: AppConfig) -> None:
    state_dir_path = app_config.state_dir_path
    if not state_dir_path.exists():
        state_dir_path.mkdir(parents=True)
    elif not state_dir_path.is_dir():
        raise NotADirectoryError(f"State directory '{state_dir_path}' is not a directory")

CLIENT = quart.Blueprint(
        "client",
        __name__,
        static_folder="static/assets",
        static_url_path="/assets",
        template_folder="templates",
        url_prefix="/",
)

@CLIENT.route("/")
async def home():
    return await quart.render_template("home.html")

@CLIENT.route("/project/<project>")
async def project(project: str):
    user = await utils.UserSession.create()
    if not user.is_authenticated:
        raise asfquart.auth.AuthenticationFailed(asfquart.auth.Requirements.E_NOT_LOGGED_IN)
    if project not in user.pmcs:
        raise asfquart.auth.AuthenticationFailed(f"You are not a member of the {name} PMC.")
    r = await reports.reports_for_pmc(project)
    return await quart.render_template("project.html", project_name=project, reports=r)

def _register_routes(quart_app: asfquart.base.QuartApp) -> None:
    quart_app.register_blueprint(CLIENT)

def _setup_context(quart_app: asfquart.base.QuartApp, app_config: AppConfig) -> None:
    @quart_app.context_processor
    async def app_context() -> dict[str, Any]:
        return {
            "current_user": await utils.UserSession.create()
        }

def create_app(test_environment: bool = False) -> asfquart.base.QuartApp:
    from app import config
    app_dir = None
    cfg_file = asfquart.base.CONFIG_FNAME

    # load the application config first to determine the state directory
    app_path = pathlib.Path(os.getcwd())
    app_config = config.load_app_config(app_path / cfg_file)

    if not test_environment:
        # ensure the state directory exists before proceeding
        _ensure_state_dir(app_config)
        # store the app secret in the state directory
        token_file = str((app_config.state_dir_path / "apptoken.txt").absolute())
    else:
        # no secret in unit tests
        token_file = None

    quart_app = asfquart.construct("security-dashboard", app_dir, cfg_file, token_file)

    _register_routes(quart_app)
    _setup_context(quart_app, app_config)

    return quart_app
