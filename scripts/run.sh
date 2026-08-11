#!/bin/bash
set -eu

# This script is used by the service in Puppet

# shellcheck source=/dev/null
source .venv/bin/activate

# TODO look into restarting gracefully on failures in either:
python3 security-dashboard-backend-watch-changes.py &
python3 security-dashboard-backend-watch-label-renames.py
