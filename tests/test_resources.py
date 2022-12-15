from json import load

from lunch_web import controller


def test_restaurants_endpoint(test_app):
    response = test_app.get("/restaurants")
    assert response.status_code == 200

    with open(controller.RESTAURANTS_JSON, "r") as f:
        rests = load(f)
    assert response.json == [{k: v['full_name']} for k, v in rests.items()]
