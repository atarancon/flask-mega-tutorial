from flask import Flask
#import Flask class

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#create instances of the Flask extension ( flask-sqlalchemy , flask-login, etc.) in the global 
#scope , but w/o any arguments passesd in. Theses instances are not attached to the application 
# at this point 
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_filename = 'config.setting.DevConfig', settings_override=None):

    app=Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_filename)
    #use instance object file sensitive data
    #app.config.from_pyfile('flask.cfg')

    #app.config.from_pyfile('flask.cfg')
    #app.config.from_pyfile('../config.py')
    print( app.config['ENV'])
    print( app.config['DEBUG'])
    print( app.config['SECRET_KEY'])

    if settings_override:
        app.config.update(settings_override)
    
    initialize_extensions(app)
    register_blueprints(app)

   

    return app

def initialize_extensions(app):
    #Sice application instance created by this point , pass Flask 
    #extensions instance to bind it to the flask instance (app)
    db.init_app(app)
    migrate.init_app(app,db)

    #Flask-login cofiguration
    #import models here
    #define the login loader here

def register_blueprints(app):
    #Register  each Blueprint with the instance (app)
    #import the blueprint creation file
    #and register it 

    #import 
    from app.users import user_blueprint
    #register 
    app.register_blueprint(user_blueprint)
    

#create instance of Flask class named app
#from . import models
#acquire routes path
   
