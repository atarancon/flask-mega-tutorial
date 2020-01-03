from flask import url_for
from app.models import User
from lib.tests import assert_status_with_message, ViewTestMixin


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
    

    

    


    