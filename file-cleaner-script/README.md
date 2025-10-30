# 🧹 File Cleaner

A lightweight Python CLI tool that automatically deletes old files (like logs or temp files) based on their modification date.
It’s a practical DevOps-style automation project that helps keep directories clean and organized.

---

## 📋 Overview

file-cleaner scans a target directory, finds files with a specific extension (e.g., .log, .txt),
and removes those older than a given date.
It logs each action both to the terminal and a file — making it great for automated cleanup jobs.

---

## 🧰 Technologies Used

- Python 3.x

- Built-in modules: pathlib, os, time, datetime, logging, argparse

---

## ⚙️ Installation

```bash
pip install git+https://github.com/khaledyousryhegazy/file-cleaner.git
```

---

## ▶️ How to run

```bash
# schema
file-cleaner -dir [path] -e [extension] -d [%Y-%m-%d]

# example
file-cleaner -dir log_dir -ex .log -d 2026-05-01
```

## 🧩 Example Output

<pre>
2025-10-29 14:33:21,759 - [DEBUG] - Starting deletion process
2025-10-29 14:33:21,762 - [DEBUG] - Delete old33.log starting ...
2025-10-29 14:33:21,762 - [DEBUG] - Delete old11.log starting ...
2025-10-29 14:33:21,763 - [DEBUG] - Delete old22.log starting ...
2025-10-29 14:33:21,763 - [INFO] - 3 files deleted and process is finished.
</pre>
