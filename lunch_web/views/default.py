from pyramid.view import view_config
from datetime import datetime
from lunch_web import (TIME_FORMAT, contoller, weekday_name)


@view_config(route_name='home', renderer='lunch_web:templates/lunches.jinja2')
def main_view(request):
    today = datetime.today()
    menus = contoller.get_menu(today)
    return {'list': menus,
            'date': today.strftime(TIME_FORMAT),
            'weekday': weekday_name[today.weekday()]}
