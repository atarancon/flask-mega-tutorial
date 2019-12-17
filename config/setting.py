import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    #export FLASK_DEBUG=1
    #give you pin 
    ENV  = 'development'
    TESTING = True
    SECRET_KEY = os.urandom(16)
    
