import pytest 
from config import setting
from app.app import create_app



@pytest.yield_fixture(scope ='session')
def app():
    """
    Set up our flask test app, this gets executed only once
    :return: Flask app
    """
   
    b_uri = '{0}_test'.format(setting.TestConfig.SQLALCHEMY_DATABASE_URI)

    setting.TestConfig.SQLALCHEMY_DATABASE_URI = b_uri

    _app = create_app(config_filename = 'config.setting.TestConfig')
    

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

