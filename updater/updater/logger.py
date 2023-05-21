import logging
from functools import lru_cache
from typing import Union

import aws_lambda_powertools


@lru_cache(1)
def get_logger(use_cloudwatch=False) -> Union[logging.Logger, aws_lambda_powertools.Logger]:
    if use_cloudwatch:
        return aws_lambda_powertools.Logger()
    else:
        logging.basicConfig(
            format="%(asctime)s %(levelname)-8s %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        return logging.getLogger("updater")
