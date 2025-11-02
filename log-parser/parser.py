import os
import json
from pathlib import Path
import logging
from datetime import datetime
from typing import Any
import argparse

"""
--- Log Parser Logic ---

1. Read the log file (e.g., server.log).
2. Search for specific lines containing log levels like [ERROR], [WARNING], [INFO].
3. Count the occurrences of each log level.
4. Extract additional details such as timestamps or message sources.
5. Store the summarized results in a JSON file (summary.json).
6. Print a summary report in the terminal.
"""

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[logging.StreamHandler()],
)


def parser(log_file_path: str) -> None:
    try:
        path = Path(log_file_path)
        total_lines = 0
        result_summary: dict[str, int] = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0,
            "DEBUG": 0,
        }

        logger.debug(f"Starting parse process for log file {path.name}.")

        all_dates: list[datetime] = []
        with open(path, mode="r", encoding="utf-8", newline="") as file:

            logger.debug(
                f"Extract Summary , min and max dates and info from file starting. "
            )

            content = file.readlines()

            for line in content:
                total_lines += 1

                if line.strip():
                    date_str = line.split(" - ")[0]
                    log_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                    all_dates.append(log_date)

            joined_content = "".join(content)

            for key in result_summary.keys():
                result_summary[key] = joined_content.count(key)

            logger.debug("Extract Successfully.")
        # export data to json file
        logger.debug(f"Making info ready for export it to json file.")

        os.makedirs("data", exist_ok=True)
        max_key: str = max(result_summary, key=result_summary.get)  # type: ignore

        final_result: dict[str, Any] = {
            "file_name": path.name,
            "total_lines": total_lines,
            "summary": result_summary,
            "first_log_time": min(all_dates).isoformat(),
            "last_log_time": max(all_dates).isoformat(),
            "most_common_level": max_key,
            "exported_at": datetime.now().isoformat(),
        }

        with open("./data/result.json", "w", encoding="utf-8") as file:
            json.dump(final_result, file, ensure_ascii=False, indent=4)

        logger.info("Store information in result.json successfully")

    except FileExistsError as er:
        logger.error(f"File Exists Error: {er}")
    except FileNotFoundError as er:
        logger.error(f"File Not Found Error: {er}")
    except PermissionError as er:
        logger.error(f"Permission Error: {er}")
    except IsADirectoryError as er:
        logger.error(f"Is Directory Error: {er}")
    except ValueError as er:
        logger.error(f"Value Error: {er}")
    except Exception as er:
        logger.error(f"Exception: {er}")


def main():
    parser_arg = argparse.ArgumentParser(
        description="Log Parser — Analyze server logs and export summary as JSON."
    )
    parser_arg.add_argument(
        "--path",
        type=str,
        required=True,
        help="Path to the log file (e.g., ./server.log)",
    )

    args = parser_arg.parse_args()
    parser(args.path)


if __name__ == "__main__":
    main()
