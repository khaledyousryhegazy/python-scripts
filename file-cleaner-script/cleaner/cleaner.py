import os
import logging
import argparse
import time
from datetime import datetime
from pathlib import Path


"""
--- file cleaner script logic:-
        1. file_cleaner function have a dir_path, extension and deletion_date parameter
        2. loop on all files in the entered dir_path
        3. create a full path by Path(dir_path) / filename
        4. check i file extension equal entered extension if true make the found var to true to check the date after that
        5. get the file modification date
        6. convert the entered deletion date to the same format of modification to compare them
        7. check if the found equal true start checking the compare two dates [modification and deletion] 
            also must check the extension of the file equal the entered extension and then start the delete process
--- to make it cli script
        1. create the main function
        2. create argparse parser and add the args to it like -dir, -e, -d
        3. call the function and pass the taken args  
"""

# create cleaner log
console = logging.getLogger("cleaner")
console.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")
handler.setFormatter(formatter)
console.addHandler(handler)


def file_cleaner(dir_path: str, extension: str, deletion_date: str) -> None:
    deletion_files_count: int = 0
    found = False
    try:
        console.debug("Starting deletion process")
        for filename in os.listdir(dir_path):
            # get the file full path
            file_path = Path(dir_path) / filename

            # if not log file skip it
            if file_path.suffix == extension:
                found = True

            # get the modification date of the file
            # os.path.getmtime(file_path) => get the seconds from 1970
            # then the "time.ctime(...)" convert it to "Mon Apr  1 00:00:00 2024" format
            file_modification_date = time.ctime(os.path.getmtime(file_path))

            # datetime.strptime(entered_date, "entered_date format") => format date auto to this form -> 2025-10-01 00:00:00
            modification_date = datetime.strptime(
                file_modification_date, "%a %b %d %H:%M:%S %Y"
            )
            deletion_date_obj = datetime.strptime(deletion_date, "%Y-%m-%d")

            if found:
                # compare deletion date and file modification date
                if (
                    deletion_date_obj > modification_date
                    and file_path.suffix == extension
                ):
                    # delete the file
                    console.debug(f"Delete {filename} starting ...")
                    os.remove(file_path)
                    deletion_files_count += 1

        if not found:
            console.info(f"there's no {extension} files !!")

        console.info(f"{deletion_files_count} files deleted and process is finished.")

    except FileNotFoundError as e:
        console.error(f"Directory not found: {e}")
    except PermissionError as e:
        console.error(f"Permission denied: {e}")
    except ValueError as e:
        console.error(f"Invalid input: {e}")
    except IsADirectoryError as e:
        console.error(f"Skipped a folder: {e}")
    except OSError as e:
        console.error(f"OS error: {e}")
    except Exception as e:
        console.error(f"Unexpected error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Clean old files by extension")

    # add my options
    parser.add_argument("-dir", "--dir-path", required=True, help="Directory path")
    parser.add_argument(
        "-e", "--extension", required=True, help="Files extension (.log, .txt)"
    )
    parser.add_argument(
        "-d", "--deletion-date", required=True, help="Deletion date in YYYY-MM-DD"
    )

    args = parser.parse_args()

    file_cleaner(args.dir_path, args.extension, args.deletion_date)
