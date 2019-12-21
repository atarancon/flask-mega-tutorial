from flask import Flask
#import Flask class

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#import login 
from flask_login import LoginManager



#create instances of the Flask extension ( flask-sqlalchemy , flask-login, etc.) in the global 
#scope , but w/o any arguments passesd in. Theses instances are not attached to the application 
# at this point 
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


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

    login_manager.init_app(app)

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


def authentication(app , user_model):
    """
    Initialized flask login extension ( mutates the app passed in)
    :param app: Flask application instance
    :param user_model: Model that contains authentication information 
    :type user_model: SQLAlchemy 
    :return None
    """
    #the name of the login view 
    #get redirected
    login_manager.login_view ='user.login'

    #Fetch User from database
    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)
    
    #token for remmembering duration 

    

#create instance of Flask class named app
#from . import models
#acquire routes path
   
