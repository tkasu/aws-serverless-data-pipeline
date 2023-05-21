# Write GitHub statistics from json to Delta

## Development

### Static type checks

`poetry run mypy .`

### Formatting

`poetry run black .`

### Update lambda dependencies

`poetry export --without-hashes --format=requirements.txt > requirements.txt`

## Usage

When running locally, requires the following env variables:

* `OUTPUT_DELTA_PATH` - Path to delta path to update to results, can be local dir (e.g. `../data/processed/gh_hourly_stats`) or s3-path (e.g. `s3://ew1-dev-awskerho-tomi-data/data/processed/gh_hourly_stats`) if the delta table does not exist, it will be created.

Update Delta table:

```
poetry run python -m updater.cli --date 2023-02-25 --user tkasu --repo aws-kerho-serverless-demo
poetry run python -m updater.cli --date 2023-02-25 --user jkainu --repo stock-visualizer
poetry run python -m updater.cli --date 2023-02-25 --user badboogey --repo AWS_demo
```

Check commits:

```
poetry run python -m updater.sandbox
```