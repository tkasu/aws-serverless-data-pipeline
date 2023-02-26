import click
from datetime import datetime
from updater import reader, writer


@click.command()
@click.option("--date")
@click.option("--repo")
@click.option("--user")
def cli(date: str, repo: str, user: str):
    date = datetime.strptime(date, "%Y-%m-%d")
    input_path = reader.resolve_path(date, repo, user)
    df = reader.read_new_json(input_path)
    print(df)
    writer.write_to_delta(df)
    # print(df.filter(pl.col("commit_count") > 0))


if __name__ == "__main__":
    cli()
