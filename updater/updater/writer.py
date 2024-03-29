import deltalake  # type: ignore
import pyarrow as pa  # type: ignore
import polars as pl
from deltalake.writer import write_deltalake  # type: ignore

from updater.delta import delta_storage_options, OUTPUT_DELTA_PATH
from updater.logger import get_logger


ARROW_SCHEMA = pa.schema(
    [
        pa.field("day_index", pa.int8()),
        pa.field("hour_index", pa.int8()),
        pa.field("commit_count", pa.int64()),
        pa.field("repo", pa.string()),
        pa.field("user", pa.string()),
        pa.field("fetch_date", pa.date32()),
    ]
)


def write_to_delta(df: pl.DataFrame):
    if _check_if_data_exist(df):
        get_logger().warning("Data existing already for given date, user, repo. Skipping update.")
        return
    df_arrow: pa.Table = df.to_arrow().cast(ARROW_SCHEMA)
    write_deltalake(
        OUTPUT_DELTA_PATH,
        df_arrow,
        mode="append",
        storage_options=delta_storage_options(OUTPUT_DELTA_PATH),
    )


def _check_if_data_exist(df: pl.DataFrame) -> bool:
    try:
        current_df = pl.scan_delta(
            OUTPUT_DELTA_PATH, storage_options=delta_storage_options(OUTPUT_DELTA_PATH)
        )
    except deltalake.PyDeltaTableError as e:
        if str(e).startswith("Not a Delta table:"):
            return False
        raise e
    except FileNotFoundError:
        return False

    matching_row: pl.DataFrame = (
        current_df.join(
            df.lazy(),
            on=["fetch_date", "user", "repo"],
            how="inner",
        )
        .limit(1)
        .collect()
    )

    return not matching_row.is_empty()
