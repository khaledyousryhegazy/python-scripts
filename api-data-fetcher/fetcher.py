import logging
import requests
import csv
import json
from typing import Any, Union
import os

"""
---logic
    1. create a fetcher function that accept an api url arg
    2. logging logic in stream
    3. create a request and get the data with error handling
    4. check that every thing is good and data is here
    5. store the info in result.json and result.csv
    6. log in terminal the process summary
"""

# logging
logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[logging.StreamHandler()],
    datefmt="%Y-%m-%d %H:%M:%S",
)


# fetcher function
def fetcher(url: str, timeout: int = 5) -> None:
    try:

        logger.debug("Start getting data")
        # start getting data
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()

        if response.ok:
            # import data from url and export data to [json, csv] files
            data: Union[dict[str, Any], list[dict[str, Any]]] = response.json()
            fieldnames: list[str]

            if isinstance(data, list) and data:
                fieldnames = list(data[0].keys())
            elif isinstance(data, dict):
                fieldnames = list(data.keys())
            else:
                raise ValueError("Unexpected data format")

            logger.debug("Start exporting data to [EXCEL] file")

            os.makedirs("data", exist_ok=True)

            with open("./data/data.csv", mode="w", newline="") as csv_file:

                csv_writer = csv.DictWriter(
                    csv_file,
                    fieldnames=fieldnames,
                )
                csv_writer.writeheader()
                csv_writer.writerows(data if isinstance(data, list) else [data])

            logger.debug("Start exporting data to [JSON] file")

            with open("./data/data.json", mode="w", encoding="utf-8") as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)

            logger.info(
                f"Data fetched successfully: {len(data) if isinstance(data, list) else 1} records saved."
            )

    except requests.exceptions.Timeout as e:
        logger.error(f"Timeout : {e}")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection Error : {e}")
    except requests.exceptions.InvalidURL as e:
        logger.error(f"Invalid URL : {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request Error : {e}")


fetcher("https://api.github.com/users/khaledyousryhegazy", 10)
