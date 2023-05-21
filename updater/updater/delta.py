import os
from functools import lru_cache
from typing import Dict, Optional

from updater.aws import AWS_DEFAULT_REGION, AwsCreds, is_s3_path

OUTPUT_DELTA_PATH = os.environ["OUTPUT_DELTA_PATH"]


@lru_cache(10)
def delta_storage_options(delta_path: str) -> Optional[Dict]:
    if not is_s3_path(delta_path):
        return None
    aws_creds = AwsCreds.resolve_s3_creads()
    config = {
        "AWS_REGION": AWS_DEFAULT_REGION,
        "AWS_ACCESS_KEY_ID": aws_creds.aws_access_key_id,
        "AWS_SECRET_ACCESS_KEY": aws_creds.aws_secret_access_key,
        # TODO, Configure S3 DynamoDB LockClient
        "AWS_S3_ALLOW_UNSAFE_RENAME": "true",
    }
    if aws_creds.aws_session_token:
        config["AWS_SESSION_TOKEN"] = aws_creds.aws_session_token
    return config
