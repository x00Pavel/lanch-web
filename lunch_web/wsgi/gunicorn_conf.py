from os import environ

PORT = environ.get("PORT", 8080)

bind = f"0.0.0.0:{PORT}"
workers = 1
threads = 10
loglevel = environ.get("LUNCH_LOG_LEVEL", "info")
