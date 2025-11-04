import requests
from datetime import datetime
import time
from .storage import storage_to_json_csv
from utils.main_logger import logger

"""
--- checker logic ---

    1. create a function that take list of urls and timeout
    2. make request to this urls
    3. create a list for result contain [timestamp, url, status_code, is_up, response_time, error]
"""


def checker(
    urls: list[str], timeout: int
) -> list[dict[str, str | int | float | bool | None]]:

    result: list[dict[str, str | int | float | bool | None]] = []
    current_url = ""
    for url in urls:
        try:
            current_url = url
            time_start = time.time()
            logger.debug(f"Starting check for {url}")
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            response_time = (time.time() - time_start) * 1000
            if response.ok:
                logger.info(f"{url} is UP ({response_time:.2f} ms)")

            result.append(
                {
                    "timestamp": datetime.now().isoformat(),
                    "url": url,
                    "status_code": response.status_code if response.ok else None,
                    "is_up": response.ok,
                    "response_time_ms": round(response_time, 2),
                    "error": None,
                }
            )

        except requests.exceptions.ConnectTimeout as er:
            logger.error(f"{current_url} is DOWN: {er}")
            result.append(
                {
                    "timestamp": datetime.now().isoformat(),
                    "url": url,
                    "status_code": None,
                    "is_up": False,
                    "response_time_ms": None,
                    "error": "Connection Timeout",
                }
            )
        except requests.exceptions.ConnectionError as er:
            logger.error(f"{current_url} is DOWN: {er}")
            result.append(
                {
                    "timestamp": datetime.now().isoformat(),
                    "url": url,
                    "status_code": None,
                    "is_up": False,
                    "response_time_ms": None,
                    "error": "Connection Error",
                }
            )
        except requests.exceptions.HTTPError as er:
            logger.error(f"{current_url} is DOWN: {er}")
            result.append(
                {
                    "timestamp": datetime.now().isoformat(),
                    "url": url,
                    "status_code": None,
                    "is_up": False,
                    "response_time_ms": None,
                    "error": "Http Error",
                }
            )
        except requests.exceptions.InvalidURL as er:
            logger.error(f"{current_url} is DOWN: {er}")
            result.append(
                {
                    "timestamp": datetime.now().isoformat(),
                    "url": url,
                    "status_code": None,
                    "is_up": False,
                    "response_time_ms": None,
                    "error": "Invalid Url",
                }
            )
        except requests.exceptions.RequestException as er:
            logger.error(f"{current_url} is DOWN: {er}")
            result.append(
                {
                    "timestamp": datetime.now().isoformat(),
                    "url": url,
                    "status_code": None,
                    "is_up": False,
                    "response_time_ms": None,
                    "error": "Request Error",
                }
            )
        except Exception as er:
            logger.error(f"{current_url} is DOWN: {er}")
            result.append(
                {
                    "timestamp": datetime.now().isoformat(),
                    "url": url,
                    "status_code": None,
                    "is_up": False,
                    "response_time_ms": None,
                    "error": str(er),
                }
            )

    # export data to json and csv files
    storage_to_json_csv(result)
    logger.info(f"Stored {len(result)} entries to JSON and CSV")
    return result


list_urls = [
    "https://www.google.com",  # success
    "https://www.github.com",  # success
    "https://www.nonexistentwebsite12345.com",  # invalid
    "https://httpstat.us/404",  # returns 404
    "https://httpstat.us/500",  # returns 500
]

checker(list_urls, 5)
