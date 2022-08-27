from concurrent.futures.thread import _worker
from json import load
from dotenv import load_dotenv
from multiprocessing import cpu_count
from os import environ

load_dotenv()

PORT = environ.get("PORT", 8080)
LOG_LEVEL = environ.get("LUNCH_LOG_LEVEL", "info")

bind = f"127.0.0.1:{PORT}"
workers = cpu_count() * 2 + 1
loglevel = LOG_LEVEL