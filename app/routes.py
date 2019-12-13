from app import app
#from app directory import app variable instance

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
