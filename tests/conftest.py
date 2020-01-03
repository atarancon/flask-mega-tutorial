import pytest 
from app.app import create_app



@pytest.yield_fixture(scope ='session')
def app():
    """
    Set up our flask test app, this gets executed only once
    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
    }

    _app = create_app(settings_override=params)

    #Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function 

    :param app: Pytest fixture
    :return: FLask app client
    """

    yield app.test_client()

