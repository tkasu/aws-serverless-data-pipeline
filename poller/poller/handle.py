from typing import Dict

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

from poller.cli import REPOS_TO_FETCH, fetch_repo

logger = Logger()


@logger.inject_lambda_context
def handler(_event: Dict, _context: LambdaContext):
    for user, repo in REPOS_TO_FETCH:
        fetch_repo(user, repo, logger)
