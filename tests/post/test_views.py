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

class TestPostEdit(ViewTestMixin):
    def test_post_edit(self):

        params = {
             'title' : "Number One",
             'body' : "At everything"
        }
        
        self.login()

        response = self.client.post( url_for('admin.post_new') , data=params , follow_redirects=True)

        assert_status_with_message(200 , response , "post has been added")
        assert Post.query.filter(Post.title==params['title'])
        id = Post.query.filter(Post.title==params['title']).all().pop().id

        e_param = {
            'title' : "edit One",
            'body' : "edit everything"
        }

        #call edit route 
        response = self.client.post( url_for('admin.post_edit' , id = id) , data= e_param , follow_redirects=True)
        assert Post.query.filter(Post.title==e_param['title'])
        assert_status_with_message(200 , response , "Post has been updated successfully")



class TestDeletePost(ViewTestMixin):
    def test_delete_post(self):
        params = {
             'title' : "Number One",
             'body' : "At everything"
        }
        
        self.login()

        response = self.client.post( url_for('admin.post_new') , data=params , follow_redirects=True)

        assert_status_with_message(200 , response , "post has been added")
        assert Post.query.filter(Post.title==params['title'])
        post = Post.query.filter(Post.title==params['title']).all().pop()
        id = post.id
        response = self.client.post( url_for('admin.post_delete', post_id = id), follow_redirects = True)

        assert_status_with_message ( 200 , response,"Post title:{0} deleted successfulyl " .format(post.title) )


class TestSearchPost(ViewTestMixin):
    def test_search_post(self):

        params = {
            'q' : ""
        }

        response = self.client.post( url_for('post.posts') , data = params , follow_redirects=True)

    






