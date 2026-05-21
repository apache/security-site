#!/bin/bash
set -eu

# This script is used by the service in Puppet

# shellcheck source=/dev/null
source .venv/bin/activate

BIND=$(python3 app/config.py --bind)
ACCESS_LOG=$(python3 app/config.py --access-log)
PID_FILE=$(python3 app/config.py --pid-file)

# The worker count defaults to 1
# This is intentional
exec hypercorn server:application -b "${BIND}" --access-logfile "${ACCESS_LOG}" --pid "${PID_FILE}" --worker-class uvloop
