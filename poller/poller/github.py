import os

from dotenv import load_dotenv
from typing import Dict

import requests
from aws_lambda_powertools.utilities import parameters

load_dotenv()

API_URL_TEMPLATE = "https://api.github.com/repos/{user}/{repo}/stats/punch_card"


def get_api_key():
    try:
        return os.environ["API_KEY"]
    except KeyError:
        return parameters.get_parameter("poller-github-api-key", max_age=7200, decrypt=True)


def fetch_commit_stats(user: str, repo: str) -> Dict:
    api_key = get_api_key()
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {api_key}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    api_url = API_URL_TEMPLATE.format(user=user, repo=repo)
    resp = requests.get(api_url, headers=headers)
    resp.raise_for_status()
    return resp.json()
