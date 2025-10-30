# 🧠 Server Health Checker

A lightweight Python CLI tool that monitors server availability and system resource usage.
It’s a practical DevOps-style automation project that helps ensure servers are running smoothly and resources are healthy.

---

## 📋 Overview

Server Health Checker takes a target server URL, performs HTTP checks, and optionally monitors local system components (CPU, RAM, Disk).
It logs all actions to both the terminal and a file — making it great for automated monitoring and reporting.

💡 Features include configurable check intervals, repeat counts, and color-coded alerts for usage thresholds.

---

## 🧰 Technologies Used

- Python 3.x
- psutil
- requests
- click

---

## ▶️ How to run

```bash
# schema
srvcheck [url] -i [interval:int] -n [count:int] -c [show component => flag]

# example
srvcheck https://example.com -i 2 -n 2 -c
```

## 🧩 Example Output

<pre>
2025-10-30 14:12:25,282 - [DEBUG] - Start checking server availability
2025-10-30 14:12:25,762 - [INFO] - Server Checked --> 200 OK in 479ms
2025-10-30 14:12:26,764 - [DEBUG] - Start checking server components
2025-10-30 14:12:26,764 - [INFO] - CPU: 6.3%, RAM: 37.8%, Disk: 15.5%
2025-10-30 14:12:28,764 - [DEBUG] - Start checking server availability
2025-10-30 14:12:29,196 - [INFO] - Server Checked --> 200 OK in 431ms
2025-10-30 14:12:30,198 - [DEBUG] - Start checking server components
2025-10-30 14:12:30,198 - [INFO] - CPU: 4.8%, RAM: 37.7%, Disk: 15.5%
</pre>
