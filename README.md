# README for KBase orcidlink utils

This repo contains standalone utilities for the orcidlink service. They are run in a
"lightweight" container based on Alpine Linux 3.18 and Python 3.12.

At present there is only one useful script, `database-maintenance.py`, which removes expired
linking sessions from the orclink database.

All maintenance tasks are run against the orcidlink service's management api using a
KBase auth token with the "orcidlink_admin" role.

To run with docker:

```shell
docker build . -t kbase/kbase-orcidlink-utils 
```

```shell
KBASE_AUTH_TOKEN=TOKEN_HERE \
KBASE_ENDPOINT=https://ci.kbase.us/services/  \
docker run -e KBASE_AUTH_TOKEN -e KBASE_ENDPOINT \
kbase/kbase-orcidlink-utils python src/database-maintenance.py
```

or using docker compose, which is handy for development:

```shell
KBASE_AUTH_TOKEN=TOKEN_HERE \
KBASE_ENDPOINT=https://ci.kbase.us/services/  \
docker compose run --rm utils python src/database-maintenance.py
```
