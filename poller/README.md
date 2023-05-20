# Read GitHub statistics from GitHub API and save to json

## Installation

`poetry install`

## Development

### Static type checks

`poetry run mypy .`

### Formatting

`poetry run black .`

### Update lambda dependencies

`poetry export --without-hashes --format=requirements.txt > requirements.txt`

## Usage

When running locally, requires the following env variables:

* `API_KEY` - GitHub API key that has access to the needed repositories
* `EXPORT_DIR` - Path to export to results, can be local dir (e.g. `../data/raw/`) or s3-path (e.g. `s3://ew1-dev-awskerho-tomi-data/data/raw/`)
* `REPOS_TO_FETCH` - Comma separated list of GitHub username:repo from which the GitHub statistics are fetched (e.g. `tkasu:aws-kerho-serverless-demo,other_username:other_repo`)

The following env variables are optional:

* `PARAM_STORE_API_KEY_NAME` - SecureString name in SSM parameter store, that is used if `API_KEY` is not provided

`.env` files are supported.

```
poetry run python -m poller.cli
```
