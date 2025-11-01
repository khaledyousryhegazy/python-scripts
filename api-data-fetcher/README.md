# 🧠 Server Health Checker

A lightweight Python automation tool that fetches data from public APIs and stores it locally in structured formats (JSON & CSV).
It’s a practical DevOps-style project showcasing automation, logging, and data handling skills.

---

## 📋 Overview

API Data Fetcher takes any public API endpoint, retrieves the data with proper error handling,
then logs each step of the process while exporting the results into both JSON and CSV files inside a /data directory.

💡 Features include detailed logging, type hints, and dual-format data export for easy integration with other tools.ds.

---

## 🧰 Technologies Used

- Python 3.x
- requests
- json
- csv
- logging

---

## ▶️ How to run

```bash
python fetcher.py
```

## 🧩 Example Output

<pre>
2025-11-01 20:03:00 - [DEBUG] - Start getting data
2025-11-01 20:03:00 - [DEBUG] - Starting new HTTPS connection (1): api.github.com:443
2025-11-01 20:03:01 - [DEBUG] - https://api.github.com:443 "GET /users/khaledyousryhegazy HTTP/1.1" 200 577
2025-11-01 20:03:01 - [DEBUG] - Start exporting data to [EXCEL] file
2025-11-01 20:03:01 - [DEBUG] - Start exporting data to [JSON] file
2025-11-01 20:03:01 - [INFO] - Data fetched successfully: 1 records saved.
</pre>
