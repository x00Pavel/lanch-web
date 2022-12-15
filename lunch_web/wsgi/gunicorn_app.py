from logging import getLogger
from pathlib import Path

from gunicorn.app.wsgiapp import WSGIApplication

logger = getLogger(__name__)
current_dir = Path(__file__).parent


class App(WSGIApplication):
    def __init__(self, app_uri: str, config_file: str = None):
        self.app_uri = app_uri  
        self.config_file = config_file
        super().__init__()
        logger.info('WSGI app initialized')

    def load_config(self):
        logger.debug('Loading config from file: %s', self.config_file)
        self.load_config_from_file(self.config_file)


def run():
    app = App('lunch_web.wsgi.app:create_app()', f'{current_dir}/gunicorn_conf.py')
    logger.debug("Starting server")
    app.run()
