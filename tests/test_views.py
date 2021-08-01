from lunch_web.views.default import main_view
from lunch_web.views.notfound import notfound_view


def test_main_view(app_request):
    info = main_view(app_request)
    assert app_request.response.status_int == 200
    assert info['project'] == 'Lunch web'

def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}
