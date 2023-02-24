import logging
import os
from datetime import datetime
from poller.fs import save_as_json
from poller.mars_api import fetch_weather


EXPORT_DIR = "../data/raw/"


logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)


def get_export_path() -> str:
    now_iso = datetime.now().isoformat()
    filename = f"{now_iso}_mars_weather_export.json"
    return os.path.join(EXPORT_DIR, filename)


def main():
    logging.info("Starting Mars weather fetch.")
    mars_weather = fetch_weather()
    export_path = get_export_path()
    save_as_json(mars_weather, export_path)
    logging.info(f"Saved Mars weather data to {export_path}.")


if __name__ == "__main__":
    main()
