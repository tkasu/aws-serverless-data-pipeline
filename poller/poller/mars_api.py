from typing import Dict

import requests


API_URL = f"https://mars.nasa.gov/rss/api/?feed=weather&category=insight_temperature&feedtype=json&ver=1.0"


def fetch_weather() -> Dict:
    resp = requests.get(API_URL)
    resp.raise_for_status()
    return resp.json()
