from pathlib import Path
from typing import Dict

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.data_classes import S3Event

from updater import reader, writer
from updater.logger import get_logger

logger: Logger = get_logger(use_cloudwatch=True)  # type: ignore


@logger.inject_lambda_context
def handler(event: Dict, _context: LambdaContext):
    logger.info(f"Received event: {event}")
    s3_event = S3Event(event)
    s3_path = f"s3://{s3_event.bucket_name}/{s3_event.object_key}"
    logger.info(f"Starting update process for path: {s3_path}")
    df = reader.read_json(s3_path)
    writer.write_to_delta(df)
    logger.info(f"Update process finished date: {s3_path}")
