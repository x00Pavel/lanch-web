from os import environ
    
PORT = environ.get("LUNCH_PORT", 8080)
LOG_LEVEL = environ.get("LUNCH_LOG_LEVEL", "info")

bind = f"0.0.0.0:{PORT}"
workers = 4
loglevel = LOG_LEVEL
