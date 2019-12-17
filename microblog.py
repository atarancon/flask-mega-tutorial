from app import app
#shell helper 
from app import db
#create a models table
from app.models import User , Post , Comment

@app.shell_context_processor
def make_shell_context():
    return {'db': db , 'User': User  , 'Post': Post , 'Comment': Comment}

if __name__ == "__main__":
    app.run()
