import pytest
from flask import url_for

def assert_status_with_message(status_code = 200 , response=None , message=None):
    """
    Check to see if a message is contained  within a response.

    :param status_code: Status code that defaults to 200 
    :type status_code: int 
    :param response: Flask response
    :type response: str
    :param messsage: String to check for
    :type message: str
    :return: None
    """

    assert response.status_code == status_code
    print(response.data)
    print(message)
    assert message in str(response.data)


class ViewTestMixin(object):
    """
    Automatically load in a session and client, this is common for a lot of test that 
    work with views
    """
    @pytest.fixture(autouse=True)
    def set_common_fixture(self,session,client):
        self.session= session
        self.client = client

    def login (self, email="dev@local.host" , password= 'devpassword'):
        """
        Login a specific user.

        :return: Flask response
        """
        return login(self.client , email , password)
    
    def logout(self):
        """
        Logout a specific user.
        
        :return: Flask response 
        """
        return logout(self.client)
    

def login(client, email="" , password=""):
    """
    login a specific user in.

    :param client: Flask client
    :param email: Email
    :type: str
    :param password: the password
    :type: str 
    :return: Flask response
    """
    user = dict(email=email , password=password)
    print(str(email) + str(password))

    response = client.post(url_for('users.login'), data=user,
                            follow_redirects=True)
    
    return response


def logout(client):
    """
    log out user

    :return flask response
    """
    return client.get(url_for('users.logout'), follow_redirects=True)

