from flask import render_template
from app import app


#from app directory import app variable instance

@app.route('/')
@app.route('/index')
def index():
    print("hello")
    user = {'username' : 'Miguel'}
    print ("YAY")
    return render_template('index.html',title='Home',user=user)
