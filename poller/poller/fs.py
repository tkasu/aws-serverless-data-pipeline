import json
from typing import Dict


def save_as_json(data: Dict, path: str):
    data_json = json.dumps(data)
    with open(path, "w") as file:
        file.write(data_json)
