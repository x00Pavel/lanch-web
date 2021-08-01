from pyramid.view import view_config
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from lunch_web.parsers import parse_pages
from lunch_web import (links, weekday_name)
from requests_cache import install_cache

install_cache(cache_name="restaurants_cache", backend="sqlite", expire_after=180)

@view_config(route_name='home', renderer='lunch_web:templates/lunches.jinja2')
def main_view(request):
    today = datetime.today()
    data = get_html(today)
    parsed = parse_pages(data)
    return {'list': parsed,
            'date': today.strftime('%Y-%m-%d'),
            'weekday': weekday_name[today.weekday()]}


def get_html(date):
    pages = list()
    for name, link in links.items():
        respons = requests.get(link)
        print(respons.from_cache)
        page = BeautifulSoup(respons.text, "html.parser")
        pages.append({"name": name, "page": page})
    return pages

