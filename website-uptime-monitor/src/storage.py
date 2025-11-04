import os
import json, csv


def storage_to_json_csv(result: list[dict[str, str | int | float | bool | None]]):
    os.makedirs("data", exist_ok=True)

    with open("data/storage.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)

    with open("data/storage.csv", "w", newline="") as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=result[0].keys())
        csvwriter.writeheader()
        csvwriter.writerows(result)
