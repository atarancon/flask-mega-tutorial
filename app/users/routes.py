from flask import render_template
#blueprint comes in 

from . import  user_blueprint

#from user_blueprint directory import app variable instance

@user_blueprint.route('/')
@user_blueprint.route('/index')
def index():
    print("hello")
    user = {'username' : 'Miguel'}
    print ("YAY")
    return render_template('index.html',title='Home',user=user)
