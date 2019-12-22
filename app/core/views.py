from flask import render_template
#blueprint comes in 

from . import  core

#from user_blueprint directory import app variable instance

@core.route('/')
def index():
    return render_template('core/home.html')