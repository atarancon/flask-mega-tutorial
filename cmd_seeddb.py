from datetime import datetime, timedelta
import unittest
from app import create_app,db
from app.models import User, Post
from config.setting import DevConfig

# Create an app context for the database connection.
app = create_app(DevConfig)
app_context = app.app_context()
app_context.push()


def init():
    """
    Initialize the database.

    :param with_testdb: Create a test database
    :return: None
    """
    db.drop_all()
    db.create_all()
    

    return None

def seed():
    """
    Seed the database with an initial user.

    :return: User instance
    """
    if User.find_by_identity(app.config['SEED_ADMIN_EMAIL']) is not None:
        return None
    
    # Create new entries in the database
    admin = User(app.config['SEED_ADMIN_EMAIL'],"admin",app.config['SEED_ADMIN_PASSWORD'],True)
    db.session.add(admin)
    db.session.commit()

    return True 


def main():
    print("initializing")
    init()
    print("seeding")
    if seed() == True :
        print("Sucess")
    elif seed () == None:
        print("Already created ")
    else:
        print("Error")
    

if __name__ == "__main__":
    main()
    
    
    




