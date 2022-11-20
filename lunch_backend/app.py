# pylint: disable=missing-function-docstring, missing-class-docstring, unspecified-encoding
from concurrent.futures import ThreadPoolExecutor
from json import load

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from lunch_backend import controller


class Menu(Resource):
    def get(self):
        name = request.args.get('name', "all")

        with open(controller.RESTAURANTS_JSON, "r") as f:
            rests = load(f)

        result = []
        if name == "all":
            with ThreadPoolExecutor(max_workers=len(rests.keys())) as exe:
                result = list(exe.map(controller.thread_work, rests.keys(), rests.values()))
        else:
            result = controller.thread_work(name, rests[name])
        response = jsonify(result)
        # Required to avoid CORS error https://developer.mozilla.org/en-US/docs/Glossary/CORS
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


def create_app(*args, **kwargs):
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Menu, '/menu')
    return app

if __name__ == '__main__':
    create_app()
