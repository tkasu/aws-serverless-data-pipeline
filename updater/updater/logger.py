import logging
from functools import lru_cache

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)


@lru_cache(1)
def logger() -> logging.Logger:
    return logging.getLogger("updater")
