# 🌐 Website Uptime Monitor

A simple yet powerful Python project that continuously checks website availability and response time — ideal for uptime monitoring and alerting.

---

## 📋 Overview

Website Uptime Monitor takes a list of URLs and verifies if they are reachable and how fast they respond.
It logs results in both the terminal and files (uptime.log, storage.json, and storage.csv) for tracking uptime history.

💡 Features include detailed status logging, response time measurement, and structured data storage for further analysis.

---

## 🧰 Technologies Used

- Python 3.x
- csv & json
- requests
- logging
- pytest

---

## ▶️ How to run

```bash
python -m src.checker
```

## 🧩 Example Output

<pre>
2025-11-04 16:10:09,593 - [DEBUG] - Starting check for https://www.google.com
2025-11-04 16:10:11,930 - [INFO] - https://www.google.com is UP (2337.00 ms)
2025-11-04 16:10:11,930 - [DEBUG] - Starting check for https://www.github.com
2025-11-04 16:10:12,577 - [INFO] - https://www.github.com is UP (647.32 ms)
2025-11-04 16:10:12,578 - [DEBUG] - Starting check for https://www.nonexistentwebsite12345.com
2025-11-04 16:10:12,759 - [ERROR] - https://www.nonexistentwebsite12345.com is DOWN: HTTPSConnectionPool(host='www.nonexistentwebsite12345.com', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7f26daf26710>: Failed to resolve 'www.nonexistentwebsite12345.com' ([Errno -2] Name or service not known)"))
2025-11-04 16:10:12,759 - [DEBUG] - Starting check for https://httpstat.us/404
2025-11-04 16:10:13,612 - [ERROR] - https://httpstat.us/404 is DOWN: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
2025-11-04 16:10:13,612 - [DEBUG] - Starting check for https://httpstat.us/500
2025-11-04 16:10:14,258 - [ERROR] - https://httpstat.us/500 is DOWN: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
2025-11-04 16:10:14,258 - [INFO] - Stored 5 entries to JSON and CSV
</pre>
