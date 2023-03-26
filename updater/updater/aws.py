import os
import configparser
import pathlib
from dataclasses import dataclass

AWS_CREDS_PROFILE = "default"
AWS_CREDS_PATH = pathlib.PosixPath("~/.aws/credentials").expanduser()
AWS_DEFAULT_REGION = "eu-west-1"


@dataclass
class AwsCreds:
    aws_access_key_id: str
    aws_secret_access_key: str

    @classmethod
    def resolve_s3_creads(cls) -> "AwsCreds":
        key_id = os.environ.get("AWS_ACCESS_KEY_ID")
        key = os.environ.get("AWS_SECRET_ACCESS_KEY")

        if not key_id or not key:
            return cls.from_fs_config()
        return cls(aws_access_key_id=key_id, aws_secret_access_key=key)

    @classmethod
    def from_fs_config(cls) -> "AwsCreds":
        config = configparser.RawConfigParser()
        config.read(AWS_CREDS_PATH)

        key_id = config.get(AWS_CREDS_PROFILE, "aws_access_key_id")
        key = config.get(AWS_CREDS_PROFILE, "aws_secret_access_key")
        return cls(aws_access_key_id=key_id, aws_secret_access_key=key)


def is_s3_path(path: str) -> bool:
    return str(path).startswith("s3://")
