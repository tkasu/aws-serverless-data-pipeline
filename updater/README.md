# Write GitHub statistics from json to Delta

## Usage

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