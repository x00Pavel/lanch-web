import re
from pyramid.view import view_config
from datetime import datetime
import requests
from bs4 import BeautifulSoup

links = {"portoriko": "https://restauraceportoriko.cz/denni-menu/",
         "jp": "https://www.jpbistro.cz/menu-technopark/index.php",
         "asport": "https://www.a-sporthotel.cz/restaurace/denni-menu/"
        }

names = {"jp": "Jean Paul's",
         "portoriko": "Restaurace Portoriko",
         "asport": "A-Sport"}

weekday_name = {0: "Pondělí", 1: "Úterý", 2: "Středa",
            3: "Čtvrtek", 4: "Pátek", 5: "Sobota", 6: "Neděle"}

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
        page = BeautifulSoup(respons.text, "html.parser")
        pages.append({"name": name, "page": page})
    return pages


def parse_pages(data):
    menus = list()
    for rest in data:
        short_name = rest["name"]
        result = dict()
        result["menu"] = dict()
        result['name'] = names[short_name]
        result['short_name'] = short_name
        result['url'] = links[short_name]

        if short_name == "portoriko":
            result["menu"] = __parse_portoriko(rest["page"])
        elif short_name == "jp":
            result["menu"], result["week_menu"] = __parse_jp(rest["page"])
        # elif rest["name"] == "asport":
        #     mils = __parse_asport(rest["page"])
       
        menus.append(result)
    return menus


def __parse_jp(page):
    result = dict()
    denni = page.find_all("div", class_="denni-menu")[0]
    for n in denni.find_all("h2"):
        day = n.get_text()
        result[day] = list()
        table = n.find_next_siblings()[0]

        for tr in table.find_all("tr"):
            print(tr)
            name = tr.find("div", class_="text").get_text()
            price = tr.find("div", class_="price").get_text()
            result[day].append(f"{name} {price}")
    week_menu =  page.find("div", class_="tydenni-menu")
    return (result, week_menu)

def __parse_portoriko(page):   
    result = dict()
    div = page.find("div", class_="print-not")
    for n in div.find_all("h2"):
        day = n.get_text()
        result[day] = list()
        table = n.find_next_siblings()[0]
        for x in table.find_all("td", class_="middle-menu"):
            if len(x.get_text(strip=True)) != 0:
                result[day].append(x.get_text())
    
    return result


def __parse_asport(page):
    return []

