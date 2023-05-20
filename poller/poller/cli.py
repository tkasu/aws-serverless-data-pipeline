import logging
import os
from datetime import datetime
from poller.fs import save_as_json
from poller.github import fetch_commit_stats


EXPORT_DIR = os.environ["EXPORT_DIR"]

# Expect format like:
# tkasu:aws-kerho-serverless-demo,other_username:other_repo
REPOS_TO_FETCH = [repo.split(":") for repo in os.environ["REPOS_TO_FETCH"].split(",")]


def get_export_path(user: str, repo: str) -> str:
    now_iso = datetime.now()
    filename = "github_commit_stats.json"
    return os.path.join(
        EXPORT_DIR,
        str(now_iso.year),
        str(now_iso.month),
        str(now_iso.day),
        user,
        repo,
        filename,
    )


def fetch_repo(user: str, repo: str, logger):
    logger.info(f"Starting GitHub commit statistics fetch for {user}/{repo}")
    stats = fetch_commit_stats(user, repo)
    export_path = get_export_path(user, repo)
    save_as_json(stats, export_path)
    logger.info(f"Saved commits stats data to {export_path}.")


def main():
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger(__name__)

    for user, repo in REPOS_TO_FETCH:
        fetch_repo(user, repo, logger)


if __name__ == "__main__":
    main()
