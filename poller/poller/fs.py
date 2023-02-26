import json
from pathlib import Path
from typing import Dict


def save_as_json(data: Dict, path: Path):
    data_json = json.dumps(data)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as file:
        file.write(data_json)
