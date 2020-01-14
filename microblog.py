#grab the initailization __init__ file from app 
from app.app import create_app
#shell helper 
from app.extensions import db  
#create a models table
from app.models import User , Post , Comment

app = create_app('config.setting.DevConfig')


@app.shell_context_processor
def make_shell_context():
    return {'db': db , 'User': User  , 'Post': Post , 'Comment': Comment}
    #cal the application factory function to construct flask application instance 
    # using the standard configuration defined in  specific file




