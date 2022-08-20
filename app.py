from concurrent.futures import ThreadPoolExecutor
from json import load
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from lunch_web import controller, parsers

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
        return jsonify(result)


api.add_resource(Menu, '/menu')

if __name__ == '__main__':
    app.run(debug=True)