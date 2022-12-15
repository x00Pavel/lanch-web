from flusk_restful import Resource
from lunch_backend import controller
from flask import request



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