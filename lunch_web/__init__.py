from pyramid.config import Configurator

links = {"portoriko": "https://restauraceportoriko.cz/denni-menu/",
         "jp": "https://www.jpbistro.cz/menu-technopark/index.php",
         "asport": "https://www.a-sporthotel.cz/restaurace/denni-menu/",
         "nepal": "https://nepalbrno.cz/weekly-menu/",
         "u3opic": "https://www.u3opic.cz/denni-menu",
         }

names = {"jp": "Jean Paul's",
         "portoriko": "Restaurace Portoriko",
         "asport": "A-Sport",
         "nepal": "Nepal",
         "u3opic": "U 3 Opic"}

weekday_name = {0: "Pondělí", 1: "Úterý", 2: "Středa",
                3: "Čtvrtek", 4: "Pátek", 5: "Sobota", 6: "Neděle"}


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
