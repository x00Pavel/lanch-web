from os import unlink
from os.path import exists

from lunch_web import links, parsers, log, TIME_FORMAT
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

MENUS_JSON = "menus.json"


def get_menu(date):
    cache = True
    # menus = load_menu(date)
    menus = None
    if menus is None:
        cache = False
        data = get_html(date)
        menus = parsers.parse_pages(data)
        update_menu(menus, date)
    return (menus, cache)


def get_html(date):
    pages = list()
    for name, link in links.items():
        content = requests.get(link)
        # U 3 Opic has specific encoding, so need to decode in specific way.
        # Encoding is set manually based on charset of original site
        if name == "u3opic":
            content.encoding = "windows-1250"
        page = BeautifulSoup(content.text, "html.parser",
                             from_encoding=content.encoding)
        pages.append({"name": name, "page": page})
    return pages


def load_menu(date):
    if not exists(MENUS_JSON):
        log.warning("Menus cache doesn't exists")
        return None
    with open(MENUS_JSON, "r") as f:
        cache = json.load(f)

    start = datetime.strptime(cache["start"], TIME_FORMAT)
    end = datetime.strptime(cache["end"], TIME_FORMAT)
    if start <= date <= end:
        log.info("Menus are loaded from the cache")
        return cache["menus"]

    log.warning("Menus cache is outdated. Need to create a new one")
    return None


def update_menu(menus, date):
    start = date.strftime(TIME_FORMAT)
    end = date + timedelta(days=(6 - date.weekday()))
    end = end.strftime(TIME_FORMAT)
    cache = {"start": start, "end": end, "menus": menus}
    try:
        with open(MENUS_JSON, "w") as f:
            json.dump(cache, f)
        log.info("Cache is updated")
    except:
        if exists(MENUS_JSON):
            unlink(MENUS_JSON)
        log.error("Cache is not updated")
        raise
