import pytest 
from config import setting
from app.app import create_app
from app.extensions import db as _db
from app.models import User



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

@pytest.yield_fixture(scope="session")
def db(app):
    """
    Setup our database , this only gets executed once per session.
    :param app: Pytest fixture 
    :return: SQLAlchemy database session
    """

    _db.drop_all()
    _db.create_all()

    #create a single user because a lot of tests do not mutatate this user.
    #It will result in faster tests.

 # Create new entries in the database
    admin = User(app.config['SEED_ADMIN_EMAIL'],"admin",app.config['SEED_ADMIN_PASSWORD'],True)

    _db.session.add(admin)
    _db.session.commit()

    return _db 

@pytest.yield_fixture(scope='function')
def session(db):
    """
    Allow very fast tests by using roll backs and nested sessions. This does require that ypur database support SQL savepoints
    , and Postgres does.

    :param db: Pytest fixture
    :return: None:
    """
    db.session.begin_nested()

    yield db.session

    db.session.rollback()

@pytest.fixture(scope='function')
def users(db):
    """
    Create user fixture. They reset per test.

    :param db: Pytest fixture
    :return: SQLALCHEMY database session
    """

    #delete all users 
    users = db.session.query(User).all()
    db.session.delete(users)
    db.session.commit()

    #create new ones 
    # Create new entries in the database
    admin = User(app.config['SEED_ADMIN_EMAIL'],"admin",app.config['SEED_ADMIN_PASSWORD'],True)
    user = User ( "one@one.com" , "one" , "password" )

    db.session.add(admin)
    db.session.add(user)

    db.session.commit()

    return db



    


