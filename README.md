# Apache Security Dashboard - Backend

This is the 'backend' of a small web API and UI
to expose an overview of the issues the
Security Team is tracking for ASF PMCs. It
watches our GMail inbox and keeps an index
similar to the `email-classification` branch
of this repo up-to-date with the last state.
A separate front-end will selectively expose
this to PMCs.

## Running

Copy `.env.example` to `.env` and populate it with actual secrets.

Run 2 jobs:

    python3 ./security-dashboard-backend-watch-changes.py
    python3 ./security-dashboard-backend-watch-label-renames.py

If a label is out-of-date for some reason, you can also manually
trigger it to be updated:

    python3 ./security-dashboard-backend-watch-changes.py -s single-label
