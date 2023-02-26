import flask
import polars as pl


DELTA_PATH = "../data/processed/gh_hourly_stats"


APP = flask.Flask(__name__)


def get_daily_new_commits_df(df: pl.LazyFrame) -> pl.LazyFrame:
    return (
        df.filter(pl.col("commit_count") > 0)
        .groupby(by=["fetch_date", "user", "repo"])
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
        .with_columns(
            [
                (pl.col("commit_count") - pl.col("prev_date_commits")).alias(
                    "new_commits"
                )
            ]
        )
        .drop(["prev_date_commits"])
        .sort(["fetch_date", "user", "repo"])
        .with_columns(
            [pl.col("fetch_date").dt.strftime("%Y-%m-%d").alias("fetch_date")]
        )
    )


@APP.route("/daily_commits")
def daily_commits():
    commits_df = pl.scan_delta(DELTA_PATH)
    daily_commits_df = get_daily_new_commits_df(commits_df).collect()
    return daily_commits_df.to_dict(as_series=False)


@APP.route("/daily_commits/<user>/<repo>")
def daily_commits_repo(user: str, repo: str):
    commits_df = pl.scan_delta(DELTA_PATH)
    daily_commits_df = (
        get_daily_new_commits_df(
            commits_df
            .filter(pl.col("user") == user)
            .filter(pl.col("repo") == repo)
        )
        .drop(["user", "repo"])
        .collect()
    )
    return daily_commits_df.to_dict(as_series=False)


if __name__ == "__main__":
    APP.debug = True
    APP.run()
