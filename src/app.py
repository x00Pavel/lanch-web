import json
from pathlib import Path
from app_backend.controller import thread_work, RESTAURANTS_JSON

def handler(event, context):
    with open(RESTAURANTS_JSON) as f:
        restaurants = json.load(f)
    url = restaurants[event["name"]]["url"]
    result = thread_work(event["name"], url)
    result["short_name"] = event["name"]

    return f"Result is {str(result)}"