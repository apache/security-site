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
    user = await utils.UserSession.create()
    if user.is_authenticated and len(user.accessible_pmcs) == 1:
        return quart.redirect(quart.url_for("client.project", project=user.accessible_pmcs[0]))
    return await quart.render_template("home.html")

def _state_sort_key(state: str) -> tuple[int, str]:
    if state == "untriaged":
        return (0, "")
    elif state == "confirmed":
        return (1, "")
    elif state == "disclosure":
        return (3, "")
    elif state.startswith("non-issue"):
        return (4, state)
    else:
        return (2, state)

_STATE_TITLES: dict[str, str] = {
    "untriaged": "Untriaged",
    "confirmed": "Confirmed",
    "disclosure": "Waiting for disclosure",
    "non-issue-docs": "Non-issue: pending documentation improvements",
    "non-issue-feedback": "Non-issue: pending feedback to reporter",
    "non-issue-upstream": "Non-issue: pending upstream",
}
_STATE_DESCRIPTIONS: dict[str, str] = {
    "untriaged": "After initial analysis, either reject the issue and provide feedback to the reporter, or accept it and allocate a CVE",
    "confirmed": "The PMC has accepted and is working on these issues. For those that don't have CVEs allocated yet, this can be done now",
    "disclosure": "A fix for these issues has been released. When you are happy with the advisory in the cveprocess tool, you can send them by moving the state to READY and using the 'Send these Emails' button on the 'OSS/ASF Emails' tab in cveprocess.",
    "non-issue-upstream": "Make sure the issue is fixed upstream and a release is made with the fix, or find an alternative to the problematic upstream component",
}

def _state_title(state: str) -> str:
    if state in _STATE_TITLES:
        return _STATE_TITLES[state]
    if state.startswith("non-issue-"):
        return f"Non-issues: {state.removeprefix('non-issue-')}"
    return f"Waiting for {state}"

def _state_description(state: str) -> str:
    return _STATE_DESCRIPTIONS.get(state, "")

def _asf_group_acl(project, pmc_membership, project_membership):
    return (
        project in pmc_membership
        or (
            project in config.get().pmcs_with_security_emails
            and project in project_membership
        )
    )

async def _require_authorization_for(project: str) -> None:
    user = await utils.UserSession.create()
    if not user.is_authenticated:
        raise asfquart.auth.AuthenticationFailed(asfquart.auth.Requirements.E_NOT_LOGGED_IN)
    pmcs = user.accessible_pmcs
    if (not _asf_group_acl(project, pmcs, user.projects)
        and not _asf_group_acl("security", pmcs, user.projects)):
        raise asfquart.auth.AuthenticationFailed(f"You are not a member of the {project} PMC.")

@CLIENT.route("/project/<project>")
async def project(project: str):
    await _require_authorization_for(project)
    r = await reports.load_pmc_reports(project)
    states = sorted(dict.fromkeys(report.state for report in r), key=_state_sort_key)
    sections = [
        (_state_title(state), _state_description(state), [report for report in r if report.state == state])
        for state in states
    ]
    return await quart.render_template("project.html",
        project_name=project,
        sections=sections)

@CLIENT.route("/api/project/<project>/reports")
async def project_reports_api(project: str):
    await _require_authorization_for(project)
    r = await reports.load_project_reports(project)
    return quart.jsonify([
        {
            "cves": report.cves,
            "title": report.title,
            "asf_member_link": report.asf_member_link,
            "state": report.state,
            "date": report.date.isoformat(),
        }
        for report in r
    ])

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

    config.setup_app_config(quart_app, app_config)

    _register_routes(quart_app)
    _setup_context(quart_app, app_config)

    return quart_app
