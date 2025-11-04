import os
import logging
from logging.handlers import RotatingFileHandler

os.makedirs("log", exist_ok=True)

formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_rotating_handler = RotatingFileHandler(
    "log/uptime.log", maxBytes=5 * 1024 * 1024, backupCount=5  # 5 MB
)
file_rotating_handler.setFormatter(formatter)

logger = logging.getLogger("uptime_monitor")
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_rotating_handler)
