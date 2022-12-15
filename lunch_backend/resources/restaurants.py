from json import load
from lunch_backend import controller

from flask_restful import Resource


class Restaurants(Resource):

    def get(self):
        with open(controller.RESTAURANTS_JSON, "r") as f:
            rests = load(f)
        return [{k: v['full_name']} for k, v in rests.items()], 200
    