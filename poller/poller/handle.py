from poller.cli import REPOS_TO_FETCH, fetch_repo


def handler(_event, _context):
    for user, repo in REPOS_TO_FETCH:
        fetch_repo(user, repo)
