from flask import Flask
#import Flask class


app=Flask(__name__)
#create instance of Flask class named app

from app import routes
#acquire routes path
