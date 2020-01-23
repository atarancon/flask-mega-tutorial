from app.models import Post
from flask  import url_for
 

from lib.tests import  assert_status_with_message, ViewTestMixin

class TestPosts(ViewTestMixin):
    def test_posts(self):
        self.login()
        response = self.client.get( url_for("post.posts"))

        assert bytes('User'.encode('utf-8')) in response.data
    

#post creation  / editing / deleting are only done by Admins user , Then i put them
# i decided to put them in admin route 
class TestPostNew(ViewTestMixin):
    def test_post_new(self):
        """ creatinfg brand new posts """
        old_count = Post.query.count()
        print("old_count" + str(old_count) )


        params = {
             'title' : "Number One",
             'body' : "At everything"
        }
        
        self.login()

        response = self.client.post( url_for('admin.post_new') , data=params , follow_redirects=True)

        assert_status_with_message(200 , response , "post has been added")
        new_count = Post.query.count()
        assert old_count + 1 == new_count



