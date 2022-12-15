# pylint: disable=missing-function-docstring, missing-class-docstring, unspecified-encoding
from flask import Flask
from flask_restful import Api

from lunch_backend.resources.health import HealthCheck
from lunch_backend.resources.menu import Menu
from lunch_backend.resources.restaurants import Restaurants


def _register_resources(api: Api):
    api.add_resource(HealthCheck, "/")
    api.add_resource(Menu, '/menu')
    api.add_resource(Restaurants, '/restaurants')


def create_app():
    app = Flask(__name__)
    api = Api(app)
    _register_resources(api)
    return app

if __name__ == '__main__':
    create_app()
