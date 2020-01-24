
from app.models import Comment 

from . import comment

from flask import (
    render_template,
    request,
    flash,
    url_for,
    redirect
)


#update comment
@comment.route("/update/<int:id>" , methods=["POST" , "GET"])
def comment_update(id):
    #Query comment from database 

    #get forum 

    #prefill form 

    #validate for submision
        # make necessary changes 

        #redirect to user page
    return "Made it to update comment"
    

#delete comment
@comment.route("/delete/<int:id>" , methods=["POST" , "GET"])
def comment_delete(id):
    #Query comment from database 

    #if user is author 

        #delete posts 
    
    return "Comment Delete"
    


