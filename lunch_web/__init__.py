from pyramid.config import Configurator
from requests_cache import install_cache
import logging

log = logging.getLogger(__name__)

TIME_FORMAT = '%Y-%m-%d'

links = {
    "portoriko": "https://restauraceportoriko.cz/denni-menu/",
    "jp": "https://www.jpbistro.cz/menu-technopark/index.php",
    "asport": "https://www.a-sporthotel.cz/restaurace/denni-menu/",
    "nepal": "https://nepalbrno.cz/weekly-menu/",
    "u3opic": "https://www.u3opic.cz/denni-menu",
    "padagali": "https://padagali.cz/denni-menu/",
    }

names = {"jp": "Jean Paul's",
         "portoriko": "Restaurace Portoriko",
         "asport": "A-Sport",
         "nepal": "Nepal",
         "u3opic": "U 3 Opic",
         "padagali": "Padagali"}

weekday_name = {0: "Pondělí", 1: "Úterý", 2: "Středa",
                3: "Čtvrtek", 4: "Pátek", 5: "Sobota", 6: "Neděle"}


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    install_cache(cache_name="restaurants_cache",
                  backend="sqlite", expire_after=360)
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
