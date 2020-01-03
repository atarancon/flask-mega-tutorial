from flask import url_for 

class TestCore(object):
    def test_home_core(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('core.index'))
        assert response.status_code == 200

        
