import polars as pl


OUTPUT_DELTA_PATH = "../data/processed/gh_hourly_stats"

commits_df = pl.scan_delta(OUTPUT_DELTA_PATH)
hourly_commits_df: pl.DataFrame = (
    commits_df.filter(pl.col("commit_count") > 0)
    .sort(["fetch_date", "user", "repo", "day_index", "hour_index"])
    .collect()
)
print(hourly_commits_df)


total_commits: pl.DataFrame = (
    hourly_commits_df.groupby(by=["fetch_date", "user", "repo"])
    .agg([pl.count().alias("commit_count")])
    .with_columns(
        [
            pl.col("commit_count")
            .shift_and_fill(1, 0)
            .sort_by("fetch_date")
            .over(["user", "repo"])
            .alias("prev_date_commits"),
        ]
    )
    .with_columns([(pl.col("commit_count") - pl.col("prev_date_commits")).alias("new_commits")])
    .drop(["prev_date_commits"])
    .sort(["fetch_date", "user", "repo"])
)
print(total_commits)
