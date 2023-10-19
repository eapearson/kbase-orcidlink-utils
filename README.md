# README for KBase orcidlink utils

This repo contains standalone utilities for the orcidlink service. They are run in a
"lightweight" container based on Alpine Linux 3.18 and Python 3.12.

At present there is only one useful script, `database-maintenance.py`, which removes expired
linking sessions from the orclink database.

All maintenance tasks are run against the orcidlink service's management api using a
KBase auth token with the "orcidlink_admin" role.

## Using Locally

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

## Deploy Image

The image containing the utils is built by a GitHub Action in the GitHub repo. Images
will be built for pull requests, PR merge to main, manually, and when a release is
created. The release build will have a name like `ghcr.io/kbase/kbase-orcidlink-utils:v1.2.3`.

## Deployment Requirements

The following environment variables must be set:

- `KBASE_AUTH_TOKEN` must be set to a KBase auth token (preferably a service token) with
  the role `orcidlink_manager`

- `KBASE_ENDPOINT` must be set to the KBase services base URL for the given deployment
  environment; e.g. for `ci` it should be `https://ci.kbase.us/services/`. Note that the
  utils are not sensitive to the terminal forward slash `/` as some KBase services are.

