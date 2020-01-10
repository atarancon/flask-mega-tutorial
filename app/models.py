from app.extensions import db
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from sqlalchemy import or_


#make sure importing only one kind of module
# like app.models everywhere
print('importing module %s' % __name__)


class User(db.Model, UserMixin):

    __tablename__ = 'users'


    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64) , index = True , unique=True)
    email = db.Column(db.String(120), index = True , unique = True )
    password_hash = db.Column(db.String(128))

    #make extra column for admnistrator priviledge
    is_admin = db.Column(db.Boolean , default = False)



    posts = db.relationship('Post',backref='author_p' , lazy = 'dynamic')


    comments = db.relationship('Comment',backref='author_c' , lazy = 'dynamic')


    def __init__ (self, email , username, password , is_admin = False):
        self.email = email 
        self.username = username
        #generate hash and create object
        self.password_hash = generate_password_hash(password)
        self.is_admin =  is_admin
    
    def check_password(self,password):
        return check_password_hash( self.password_hash,password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    @classmethod
    def find_by_identity(cls, identity):
        """
        Find a user by their e-mail or username.

        :param identity: Email or username
        :type identity: str
        :return: User instance
        """
        return User.query.filter(
          (User.email == identity) | (User.username == identity)).first()

    @classmethod
    def search(cls, query):
        """
        Search a resource by 1 or more fields.

        :param query: Search query
        :type query: str
        :return: SQLAlchemy filter

        """
        if query == "":
            return ''
        
        search_query = '%{0}%'.format(query)
        search_chain = (User.email.ilike(search_query),
                        User.username.ilike(search_query))
        return or_(*search_chain)
    
    @classmethod
    def delete(self):
        """
        Delete a model instance.

        :return: db.session.commit()'s result
        """
        db.session.delete(self)
        return db.session.commit()



    
    def authenticated ( self , with_password = True, password=""):
        """ 
        Ensure a user is auntenicated by checking their password 
        Optionally (In case of emergency access account without thier password)
        :param with_password: Optionally check their password
        :type with_password: bool
        :param password: Optionally verify this as their password
        :type password: str
        :return: bool
        """
        if with_password:
            return check_password_hash(self.password_hash, password)

        return True

    @classmethod
    def get_bulk_action_ids(cls, scope, ids, omit_ids=[], query=''):
        """
        Determine which IDs are to be modified.

        :param scope: Affect all or only a subset of items 
        :type scope: str
        :param ids: List of ids to the modified 
        :type ids: list 
        :param omit_ids: Remove 1 or more IDs from the list
        :type omit_ids: list
        :type query:Search query (if applicable)
        :type query: str
        :return query: str
        :return: list

        """
        omit_ids = map(str, omit_ids)
        
        

        if scope == 'all_search_results':
            #Change the scope to go from selected ids to all search results.
            ids = cls.query.with_entities(cls.id).filter(cls.search(query))

            #SQLAlchemy return back  a list of tuples, we want a list of str
            ids = [ str(item[0]) for item in ids ]

        #remove 1 or more items from list , thics could be useful in spots 
        #where you may want to protect the current user for deleting themself 
        #when buk deleting user accounts

        
        if omit_ids:
            print("scure the current log in user")
            ids = [ id for id in ids if id not in omit_ids]
            print(list(omit_ids))
        print("print ommited ids")
        print(list(omit_ids))
        return ids
    

    @classmethod
    def bulk_delete(cls , ids):
        """
        Delete 1 or more model istances

        :param ids: list of ids to be deleted 
        :type ids: list
        :return: Number of deleted instances 
        """

        delete_count = cls.query.filter(cls.id.in_(ids)).delete(synchronize_session=False)
        db.session.commit()

        return delete_count







class Post (db.Model):

    __tablename__ = 'posts'

    


    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text, nullable = False)
    timestamp = db.Column(db.DateTime,index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    #multiple comments 
    comments = db.relationship('Comment' , backref='post' , lazy = 'dynamic')


    def __init__ (self , body , timestamp , user_id ):
        self.body = body 
        self.timestamp = timestamp
        self.user_id = user_id


    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Comment(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(140), nullable = False) 
    timestamp = db.Column(db.DateTime, default= datetime.utcnow)
    #refer back to particular user 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #refer back to particular post 
    post_id = db.Column(db.Integer , db.ForeignKey('posts.id'))


    def __init__ (self , text , timestamp , user_id , post_id):
        self.text = text 
        self.timestamp = timestamp
        self.user_id = user_id 
        self.post_id = post_id 





    def __repr__(self):
        return '<Comments: {} user {} post {} author of post {} >'.format(self.text , self.author_c, self.post , self.post)








