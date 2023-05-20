# AWS Serverless Data pipeline

Hobby project that is used to teach AWS Serverless techonologies for frieds and how it can be used with modern data technologies.

## Architecture

### Poller

Fetches data from confired GitHub repositorys and saves the data as json

### Updater

Reads the json from Poller and saves updates a Delta-table to contain the new data

### API

Provides API that can be used to query the Delta table

## Development

See READMEs in:

* poller/README.md
* updater/README.md
* api/README.md

## Deployment

`sam build && sam deploy`

Ready:

- [x] Poller Lambda
- [ ] Updater Lambda
- [ ] API Lambda