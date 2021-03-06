import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    TESTING = os.environ.get('TESTING') or False
    DEBUG = os.environ.get('DEBUG') or   True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #set configuration for database location
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #set website ip address: local host and port number server listen to 8000
    #flask run -h localhost -p 8000 
    #overriding ip addess: local host and port number 5000 
    #py.test purposes
    #SERVER_NAME = 'localhost:8000'
    

class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(16)

class DevConfig(Config):
    #export 
    FLASK_DEBUG=1
    #give you pin 
    DEBUG = True
    #ENV  = 'development'
    #TESTING = True
    SECRET_KEY = os.urandom(16)

    # User.
    SEED_ADMIN_EMAIL = 'dev@local.host'
    SEED_ADMIN_PASSWORD = 'devpassword'


class TestConfig(Config):
    DEBUG = False
    TESTING = True 
    SECRET_KEY = os.urandom(16)
    WTF_CSRF_ENABLED = False
    SEED_ADMIN_EMAIL = 'dev@local.host'
    SEED_ADMIN_PASSWORD = 'devpassword'
    

    
