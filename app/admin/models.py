from sqlalchemy import func 

from app.models import User, db

class Dashboard (object):
    @classmethod
    def group_count_users(cls):
        """Perform a group/ by count in all users
        :return dict
        """

        return Dashboard._group_and_count(User , User.is_admin)

    @classmethod
    def _group_and_count( cls ,model , field):
        """
        Group result for specific  model and field 
        :param Name of model 
        :type of model: SQLALCHEMY  model
        :param field: Name of field to work on 
        :type field: SQL field 
        :return : Dict 
        """
        count = func.count(field)
        query = db.session.query(count , field).group_by(field).all() 


        results = {
            'query': query ,
            'total': model.query.count()
        }

    
        return results









        



