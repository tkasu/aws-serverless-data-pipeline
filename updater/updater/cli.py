from pathlib import Path

import click
from datetime import datetime
from updater import reader, writer
from updater.logger import get_logger

INPUT_FOLDER = Path("../data/raw")


@click.command()
@click.option("--date")
@click.option("--repo")
@click.option("--user")
def cli(date: str, repo: str, user: str):
    logger = get_logger(use_cloudwatch=False)
    logger.info(f"Starting update process for date: {date}, repo: {repo}, user: {user}")
    date_parsed = datetime.strptime(date, "%Y-%m-%d")
    input_path = reader.resolve_path(INPUT_FOLDER, date_parsed, repo, user)
    df = reader.read_json(input_path)
    writer.write_to_delta(df)
    logger.info(f"Update process finished date: {date}, repo: {repo}, user: {user}")


if __name__ == "__main__":
    cli()
