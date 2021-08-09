from lunch_web import (links, names)
import re


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
        elif short_name == "asport":
            result["menu"] = __parse_asport(rest["page"])

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
            name = tr.find("div", class_="text").get_text().strip()
            price = tr.find("div", class_="price").get_text().strip()
            result[day].append({"type": "Menu", "name": name, "price": price})
    week_menu = page.find("div", class_="tydenni-menu")
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
                txt = x.get_text()
                if re.search('polévka', txt, re.IGNORECASE):
                    result[day].append(
                        {"type": "Polevka", "name": " ".join(txt.split()[0:-2:1]),
                         "price": txt.split()[-1]})
                else:
                    result[day].append(
                        {"type": f"Menu {txt.split()[0]}",
                         "name": " ".join(txt.split()[1:-2:1]),
                         "price": txt.split()[-1]})

    return result


def __parse_asport(page):
    result = dict()
    days = ("pondeli", 'utery', 'streda', 'ctvrtek', 'patek')
    for day in days:
        section = page.find("section", id=f"menu-{day}")
        h2 = section.find("h2", class_="tydenni-menu").get_text()
        tmp = list()
        table = section.find("table", class_="tydenni-menu")
        for tr in table.find_all('tr'):
            typ = tr.find('td', class_="typ").get_text().strip()
            polozka = tr.find('td', class_="polozka").get_text().strip()
            cena = tr.find('td', class_="cena").get_text().strip()
            if polozka != "":
                tmp.append({"type": typ, "name": polozka, "price": cena})
        if tmp:
            result[h2] = tmp
    return result
