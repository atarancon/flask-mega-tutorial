
from datetime import datetime, timedelta
import unittest
from app import create_app,db
from app.models import User, Post
from config.setting import Config

class TestConfig(Config):
    TESTING = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        print("-------------done set up----------")

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    


    def test_password_hashing(self):
        u = User(username='susan',password='cat', email='susan@gmail')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))
    

  


if __name__ == '__main__':
    print("hello")
    unittest.main(verbosity=2)
