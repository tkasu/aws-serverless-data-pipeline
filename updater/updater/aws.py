import pathlib
from dataclasses import dataclass

import boto3

AWS_CREDS_PROFILE = "default"
AWS_CREDS_PATH = pathlib.PosixPath("~/.aws/credentials").expanduser()
AWS_DEFAULT_REGION = "eu-west-1"


@dataclass
class AwsCreds:
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_session_token: str

    @classmethod
    def resolve_s3_creads(cls) -> "AwsCreds":
        session = boto3.Session()
        creds = session.get_credentials().get_frozen_credentials()
        return cls(
            aws_access_key_id=creds.access_key,
            aws_secret_access_key=creds.secret_key,
            aws_session_token=creds.token,
        )


def is_s3_path(path: str) -> bool:
    return str(path).startswith("s3://")
