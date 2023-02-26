import os
import json
from datetime import datetime
from pathlib import Path

import polars as pl


INPUT_FOLDER = Path("../data/raw")
INPUT_FILENAME = "github_commit_stats.json"
DAY_INDEX_COL_NAME = "day_index"
HOUR_INDEX_COL_NAME = "hour_index"
COMMIT_COUNT_COL_NAME = "commit_count"
DAY_INDEX_COL_IDX = 0
HOUR_INDEX_COL_IDX = 1
COMMIT_COUNT_COL_IDX = 2
PATH_REPO_INDEX = 0
PATH_USER_INDEX = 1
PATH_DAY_INDEX = 2
PATH_MONTH_INDEX = 3
PATH_YEAR_INDEX = 4


def get_dir_name_from_index(path: Path, idx: int) -> str:
    return path.parents[idx].name


def read_new_json(path: Path) -> pl.DataFrame:
    with open(path, "r") as file:
        data = json.loads(file.read())

    data_columnar = {
        DAY_INDEX_COL_NAME: [row[DAY_INDEX_COL_IDX] for row in data],
        HOUR_INDEX_COL_NAME: [row[HOUR_INDEX_COL_IDX] for row in data],
        COMMIT_COUNT_COL_NAME: [row[COMMIT_COUNT_COL_IDX] for row in data],
    }
    df = pl.from_dict(data_columnar)

    repo = get_dir_name_from_index(path, PATH_REPO_INDEX)
    user = get_dir_name_from_index(path, PATH_USER_INDEX)
    year = get_dir_name_from_index(path, PATH_YEAR_INDEX)
    month = get_dir_name_from_index(path, PATH_MONTH_INDEX)
    day = get_dir_name_from_index(path, PATH_DAY_INDEX)

    df = df.with_columns(
        pl.lit(repo).alias("repo"),
        pl.lit(user).alias("user"),
        pl.lit(f"{year}-{month}-{day}").str.strptime(pl.Date, fmt="%Y-%m-%d").alias("fetch_date"),
        pl.col(DAY_INDEX_COL_NAME).cast(pl.Int8).alias(DAY_INDEX_COL_NAME),
        pl.col(HOUR_INDEX_COL_NAME).cast(pl.Int8).alias(HOUR_INDEX_COL_NAME),
        pl.col(COMMIT_COUNT_COL_NAME).cast(pl.Int64).alias(COMMIT_COUNT_COL_NAME),
    )
    return df


def resolve_path(date: datetime, repo: str, user: str) -> Path:
    return Path(
        os.path.join(
            INPUT_FOLDER,
            str(date.year),
            str(date.month),
            str(date.day),
            user,
            repo,
            INPUT_FILENAME,
        )
    )
