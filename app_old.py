from concurrent.futures import ThreadPoolExecutor
from json import load
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_lunch_web import controller


app = Flask(__name__)
api = Api(app)


class Menu(Resource):
    def get(self):
        name = request.args.get('name', "all")

        with open(controller.RESTAURANTS_JSON, "r") as f:
            rests = load(f)
        if name == "all":
            with ThreadPoolExecutor(max_workers=len(rests.keys())) as exec:
                result = list(exec.map(controller.thread_work, list(rests.items())))
        else: 
            result = controller.thread_work((name, rests[name]))
        response = jsonify(result)
        # Required to avoid CORS error https://developer.mozilla.org/en-US/docs/Glossary/CORS
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

api.add_resource(Menu, '/menu')

def create_app():
    return app

if __name__ == '__main__':
    create_app()