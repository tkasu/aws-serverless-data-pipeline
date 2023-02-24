import os
from typing import Dict

import requests
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.environ["API_KEY"]
API_URL = (
    f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0"
)


def fetch_weather() -> Dict:
    resp = requests.get(API_URL)
    resp.raise_for_status()
    return resp.json()
