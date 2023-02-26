import os
from dotenv import load_dotenv
from typing import Dict

import requests


load_dotenv()


API_KEY = os.environ["API_KEY"]
API_URL_TEMPLATE = "https://api.github.com/repos/{user}/{repo}/stats/punch_card"


def fetch_commit_stats(user: str, repo: str) -> Dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {API_KEY}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    api_url = API_URL_TEMPLATE.format(user=user, repo=repo)
    resp = requests.get(api_url, headers=headers)
    resp.raise_for_status()
    return resp.json()
