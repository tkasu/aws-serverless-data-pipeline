import json
from functools import lru_cache
from pathlib import Path
from typing import Dict, TYPE_CHECKING
from urllib.parse import urlparse

import boto3

if TYPE_CHECKING:
    from mypy_boto3_s3.service_resource import Object as S3Object
    from mypy_boto3_s3 import S3ServiceResource
else:
    S3Object = object
    S3ServiceResource = object


def save_as_json(data: Dict, path: str):
    data_json = json.dumps(data)
    if _is_s3_path(path):
        _save_to_s3(data_json, path)
    else:
        _save_to_local_fs(data_json, path)


@lru_cache(1)
def _s3_res() -> S3ServiceResource:
    return boto3.resource("s3")


def _is_s3_path(path: str) -> bool:
    return str(path).startswith("s3://")


def _s3_object_from_path(path: str) -> S3Object:
    url_components = urlparse(path)
    return _s3_res().Object(url_components.netloc, url_components.path.lstrip("/"))


def _save_to_local_fs(data_json: str, path: str):
    path_obj = Path(path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    with open(path_obj, "w") as file:
        file.write(data_json)


def _save_to_s3(data_json: str, path: str):
    s3_obj = _s3_object_from_path(path)
    s3_obj.put(Body=data_json.encode("utf-8"))
