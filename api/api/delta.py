from functools import lru_cache
from typing import Dict, Optional

from api.aws import AWS_DEFAULT_REGION, AwsCreds, is_s3_path

# DELTA_PATH = "../data/processed/gh_hourly_stats"
DELTA_PATH = "s3://ew1-dev-awskerho-tomi-data/data/processed/gh_hourly_stats"


@lru_cache(10)
def delta_storage_options(delta_path: str) -> Optional[Dict]:
    if not is_s3_path(delta_path):
        return None
    aws_creds = AwsCreds.resolve_s3_creads()
    return {
        "AWS_REGION": AWS_DEFAULT_REGION,
        "AWS_ACCESS_KEY_ID": aws_creds.aws_access_key_id,
        "AWS_SECRET_ACCESS_KEY": aws_creds.aws_secret_access_key,
    }
