import pyarrow as pa
import polars as pl
from deltalake.writer import write_deltalake

OUTPUT_DELTA_PATH = "../data/processed/gh_hourly_stats"

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
    df_arrow: pa.Table = df.to_arrow().cast(ARROW_SCHEMA)
    write_deltalake(OUTPUT_DELTA_PATH, df_arrow, mode="append")
