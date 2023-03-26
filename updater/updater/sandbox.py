import polars as pl

from updater.delta import delta_storage_options, OUTPUT_DELTA_PATH

commits_df = pl.scan_delta(OUTPUT_DELTA_PATH, storage_options=delta_storage_options(OUTPUT_DELTA_PATH))
hourly_commits_df: pl.DataFrame = (
    commits_df.filter(pl.col("commit_count") > 0)
    .sort(["fetch_date", "user", "repo", "day_index", "hour_index"])
    .collect()
)
print(hourly_commits_df)


total_commits: pl.DataFrame = (
    hourly_commits_df.groupby(by=["fetch_date", "user", "repo"])
    .agg([pl.sum("commit_count").alias("commit_count")])
    # sort needed to shift_and_fill to work correctly
    .sort(["user", "repo", "fetch_date"])
    .with_columns(
        [
            pl.col("commit_count").shift_and_fill(1, 0).over(["user", "repo"]).alias("prev_date_commits"),
        ]
    )
    .with_columns([(pl.col("commit_count") - pl.col("prev_date_commits")).alias("new_commits")])
    .drop(["prev_date_commits"])
    .sort(["fetch_date", "user", "repo"])
)
print(total_commits)
