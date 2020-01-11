from flask  import url_for

from lib.tests import ViewTestMixin , assert_status_with_message
from app.models import User

class TestDashboard(ViewTestMixin):
    def test_dashboard_page(self):
        self.login()
        response = self.client.get(url_for('admin.dashboard'))

        assert bytes('User'.encode('utf-8')) in response.data 

class TestUsers(ViewTestMixin):
    def test_index_page(self):
        """ Index renders successfully ."""
        self.login()
        response = self.client.get(url_for("admin.users"))

        assert response.status_code == 200
    
    def test_bulk_delete_nothing(self):
        """ Last admin account should not get deleted. """
        old_count = User.query.count()

        params = {
            'bulk_ids' : [1],
            'scope' : 'all_selected_items'
        }

        self.login()
        response = self.client.post(url_for('admin.users_bulk_delete'), 
                                        data=params, follow_redirects=True)
        
        assert_status_with_message(200, response, '0 were schedule to be deleted ')
        new_count = User.query.count()
        assert old_count == new_count

    

