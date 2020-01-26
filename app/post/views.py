

from app.models import Post, Comment
from sqlalchemy import text

from flask import (
    render_template,
    request,
    flash,
    url_for,
    redirect
)


from . import post

from app.post.forms import SearchForm
from app.comment.forms import CommentForm


#display all blogs list
@post.route('/posts' , defaults = {'page'  : 1} )
@post.route('page/<int:page>')
def posts(page):

    search_form = SearchForm()
    paginated_posts = Post.query.filter(Post.search(text(request.args.get('q','')))).order_by(Post.timestamp.desc()).paginate(page,50,True)
    return render_template('post/index.html' , posts = paginated_posts , form= search_form)

#display single post 
@post.route('single_post/<int:post_id>' , methods=["POST" , "GET"])
def single_post(post_id):

    blog_post = Post.query.get_or_404(post_id)

    #1++++++#Query the post for comments 
    #paginate the list of comment 
    page = request.args.get('page',1,type=int)

    paginated_comment = Comment.query.filter(Comment.post_id == blog_post.id).order_by(Comment.timestamp.desc()).paginate(page ,50 , True)

    #send it to template

    #2++++#Get Comment Forum 
    form = CommentForm()

    #validate for submision 
    if form.validate_on_submit():
    #fill it up 
       c = Comment(form.text.data , blog_post.user_id , blog_post.id)

       c.save()

       flash("Comment has been added successfully","success")
       #return render_template( url_for('post.single_post' , post_id = post_id))


    #add to database
    #paginated_comment = Comment.query.order_by(Comment.timestamp.desc()).paginate(page ,50 , True)

    #return to same template 
    
    return render_template('post/post.html',post = blog_post , comments =paginated_comment , form = form )



