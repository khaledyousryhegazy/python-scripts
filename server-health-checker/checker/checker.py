import logging
import click
import psutil
import requests
import time
import os
from logging.handlers import RotatingFileHandler

"""
--- Server Health Check Logic:
    1. Server Availability Check: Sends HTTP GET to the provided server_url and measures response time.
    2. Local Component Monitoring: Checks CPU, RAM, and Disk usage on the machine running the script.
    3. Threshold Alerts: Uses color-coded CLI output and logging for normal, warning, and critical usage levels.
    4. Logging: Detailed logs for debug, info, warning, and error events saved to a log file.
    5. CLI Interface: Built with Click, accepts server_url, optional --components, --interval, and --count.
    6. Repeatable Checks: Supports looping the health check multiple times with configurable intervals.
    7. Extensible: Can be extended for uptime, load average, or remote server component monitoring.
"""

# creating the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

os.makedirs("log", exist_ok=True)
file_handler = RotatingFileHandler("log/health.log", maxBytes=1024, backupCount=3)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def check_srv_url(server_url: str):
    srv_status: str = "UNKNOWN"
    fb_color = ""

    logger.debug("Start checking server availability")
    try:
        time_start = time.time()
        get_srv = requests.get(server_url, timeout=5)
        res_time = (time.time() - time_start) * 1000

        if get_srv.ok:
            srv_status = f"{get_srv.status_code} OK in {res_time:.0f}ms"
            logger.info(f"Server Checked --> {srv_status}")
            fb_color = "green"
        else:
            srv_status = f"{get_srv.status_code} {get_srv.reason}"
            logger.info(f"Server Checked --> {srv_status}")
            fb_color = "red"

    except requests.exceptions.ConnectionError:
        srv_status = "CONNECTION_ERROR"
        logger.error(srv_status)
        fb_color = "red"
    except requests.exceptions.Timeout:
        srv_status = "TIMEOUT"
        logger.error(srv_status)
        fb_color = "red"
    except requests.exceptions.RequestException:
        srv_status = "REQUEST_ERROR"
        logger.error(srv_status)
        fb_color = "red"

    click.secho(f"Server Checked --> {srv_status}", fg=fb_color)


def check_srv_components():
    # get server components
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    status = "green"

    logger.debug("Start checking server components")

    if cpu > 75 or ram > 75 or disk > 75:
        status = "yellow"
        logger.warning(f"High usage detected!")

    if cpu > 90 or ram > 90 or disk > 90:
        status = "red"
        logger.error(f"Critical Usage!")

    click.secho(f"CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%", fg=status)
    logger.info(f"CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%")


@click.command()
@click.argument("server_url")
@click.option(
    "--interval",
    "-i",
    type=int,
    default=0,
    help="Interval between checks (0 = run once)",
)
@click.option(
    "--count", "-n", type=int, default=1, help="Number of times to run (for loop)"
)
@click.option("--components", "-c", is_flag=True, help="Check local components")
def main(server_url: str, count: int, components: bool, interval: int = 5):
    for _ in range(count):
        check_srv_url(server_url)
        if components:
            check_srv_components()
        if interval > 0:
            time.sleep(interval)
