import logging
import os
from datetime import datetime
from pathlib import Path
from poller.fs import save_as_json
from poller.github import fetch_commit_stats


EXPORT_DIR = "../data/raw/"


logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

REPOS_TO_FETCH = [
    ("tkasu", "aws-kerho-serverless-demo"),
    ("badboogey", "AWS_demo"),
    ("jkainu", "stock-visualizer"),
]


def get_export_path(user: str, repo: str) -> Path:
    now_iso = datetime.now()
    filename = "github_commit_stats.json"
    return Path(
        os.path.join(
            EXPORT_DIR,
            str(now_iso.year),
            str(now_iso.month),
            str(now_iso.day),
            user,
            repo,
            filename,
        )
    )


def fetch_repo(user: str, repo: str):
    logging.info(f"Starting GitHub commit statistics fetch for {user}/{repo}")
    stats = fetch_commit_stats(user, repo)
    export_path = get_export_path(user, repo)
    save_as_json(stats, export_path)
    logging.info(f"Saved commits stats data to {export_path}.")


def main():
    for user, repo in REPOS_TO_FETCH:
        fetch_repo(user, repo)


if __name__ == "__main__":
    main()
