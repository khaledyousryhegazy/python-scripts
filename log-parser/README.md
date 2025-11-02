# 🧠 Log Parser

A lightweight Python automation tool that analyzes server log files, extracts metrics, and exports summarized results in structured format (JSON).
It’s a practical DevOps-style project showcasing automation, logging, and data analysis skills.

---

## 📋 Overview

Log Parser reads any structured server log file (e.g., server.log), detects log levels like [INFO], [WARNING], and [ERROR],
counts their occurrences, extracts timestamps, and generates a summary report including total lines, first and last log times, and the most frequent log level.

💡 Features include detailed logging, robust error handling, type hints, and clean JSON export — ideal for automation or integration with monitoring tools.

---

## 🧰 Technologies Used

- Python 3.x
- logging
- json
- pathlib
- datetime
- argparse

---

## ▶️ How to run

```bash
python parser.py --path ./server.log
```

## 🧩 Example Output

<pre>
{
  "file_name": "server.log",
  "total_lines": 16,
  "summary": {
    "INFO": 10,
    "WARNING": 3,
    "ERROR": 3,
    "CRITICAL": 0,
    "DEBUG": 0
  },
  "first_log_time": "2025-11-01T10:00:12",
  "last_log_time": "2025-11-01T10:45:00",
  "most_common_level": "INFO",
  "exported_at": "2025-11-02T19:53:53.440716"
}
</pre>
