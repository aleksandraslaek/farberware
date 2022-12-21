from fixture.application import Application
from model.credentials import Credentials
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
    app.session.login(Credentials("testik123@gmail.com", "Qwerty123"))
    app.gift.add_gift_card()
    app.session.logout()
