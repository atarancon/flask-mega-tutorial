from flask import url_for
from app.models import User
from lib.tests import assert_status_with_message, ViewTestMixin
from config.setting import TestConfig


class TestLogin(ViewTestMixin):
    def test_login_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('users.login'))
        assert response.status_code == 200
    
    def test_login(self):
        """ Login Succcessfully. """
        response = self.login()
        assert response.status_code == 200
    
    def test_login_fail(self):
        """ Login Failure due to invalid login credentials """
        response = self.login(email='foo@bar.com')
        assert_status_with_message(200,response, "Email or password is incorrect.")
    
    def test_logout(self):
        """ Logout successfully. """
        self.login()

        response =self.logout()
        assert_status_with_message(200,response,'You have been logged out.')


class TestSignup(ViewTestMixin):
    def  test_signup_page(self):
        """ Signup renders succesfully """
        response = self.client.get(url_for('users.signup'))
        assert response.status_code==200
    
    def test_begin_signup_fail(self):
        """ Signup failure due to using an account that already exists. """
        user = { 'email' : TestConfig.SEED_ADMIN_EMAIL , 'username:' : "admin", 'password' : TestConfig.SEED_ADMIN_PASSWORD ,
               'pass_conf' : TestConfig.SEED_ADMIN_PASSWORD }
        response = self.client.post(url_for('users.signup'), data=user , follow_redirects=True)

        assert_status_with_message(200 , response ,"Your Email has been already register")

    def test_begin_signup_username_fail(self):
        """ Sign up failure due to inputting an username already exist"""

        user = { 'email' : "foo@foo.com" , 'username' : "admin", 'password' : TestConfig.SEED_ADMIN_PASSWORD ,
               'pass_conf' : TestConfig.SEED_ADMIN_PASSWORD }
        response = self.client.post(url_for('users.signup'), data=user , follow_redirects=True)

        assert_status_with_message(200 , response ,"Your username has been already register")
    
    def test_signup(self, users):
        """ Sign up succesfully """
        old_user_count = User.query.count()

        user = { 'email': "new@local.host" , 'username' : "newuser" , 'password': 'password' , 
                    'pass_conf': 'password'}
        response = self.client.post(url_for("users.signup"), data=user, follow_redirects=True)

        assert_status_with_message( 200, response, "Awesome, Thanks for registering")

        # new user got addded to table and increment number of users by one
        new_user_count = User.query.count()
        assert (old_user_count + 1) == new_user_count

        #ensure password has been hashed 
        new_user = User.find_by_identity('new@local.host')
        assert new_user.password_hash != 'password'

    def test_redirect_signup(self, users):
        """ Sign up makes it to login page """
        user = { 'email': "new@local.host" , 'username' : "newuser" , 'password': 'password' , 
                    'pass_conf': 'password'}
        response = self.client.post(url_for("users.signup"), data=user, follow_redirects=False)
        assert response.status_code == 302

        assert response.location == url_for("users.login")
        




        



        

    

    

    


    