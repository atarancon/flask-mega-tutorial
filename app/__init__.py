from flask import Flask
#import Flask class

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__, instance_relative_config=True)
app.config.from_object('config.setting.DevConfig')
#use instance object file sensitive data
#app.config.from_pyfile('flask.cfg')

#app.config.from_pyfile('flask.cfg')
#app.config.from_pyfile('../config.py')
print( app.config['ENV'])
print( app.config['DEBUG'])
print( app.config['SECRET_KEY'])

db = SQLAlchemy(app)
migrate = Migrate(app,db)

#create instance of Flask class named app
from app import routes , models
#acquire routes path


