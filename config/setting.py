import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #set configuration for database location
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #set website ip address: local host and port number server listen to 8000
    #flask run -h localhost -p 8000 
    #overriding ip addess: local host and port number 5000 
    #SERVER_NAME = '127.0.0.1:8000'
    

class ProdConfig(Config):
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    #export FLASK_DEBUG=1
    #give you pin 
    ENV  = 'development'
    TESTING = True
    SECRET_KEY = os.urandom(16)

    # User.
    SEED_ADMIN_EMAIL = 'dev@local.host'
    SEED_ADMIN_PASSWORD = 'devpassword'
    
