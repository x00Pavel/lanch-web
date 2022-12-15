from pytest import fixture
from lunch_web.wsgi.app import create_app

@fixture()
def test_app():
    return create_app().test_client()
