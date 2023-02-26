# API on top of Delta Table to query GitHub statistics

## Usage

Launch server:

```
poetry run python -m api.app
```

Get repo daily commits:

```
$ curl http://127.0.0.1:5000/daily_commits/tkasu/aws-kerho-serverless-demo

{
  "commit_count": [
    3,
    3
  ],
  "fetch_date": [
    "2023-02-25",
    "2023-02-26"
  ],
  "new_commits": [
    3,
    0
  ]
}
```