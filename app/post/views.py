

from app.models import Post
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


#display all blogs list
@post.route('/posts' , defaults = {'page'  : 1} )
@post.route('page/<int:page>')
def posts(page):

    search_form = SearchForm()
    paginated_posts = Post.query.filter(Post.search(text(request.args.get('q','')))).order_by(Post.timestamp.desc()).paginate(page,50,True)
    return render_template('post/index.html' , posts = paginated_posts , form= search_form)

#display single post 
@post.route('single_post/<int:post_id>')
def single_post(post_id):

    #1++++++#Query the post for comments 

    #paginate the list of comment 

    #send it to template

    #2++++#Get Comment Forum 

    #validate for submision 

    #fill it up 

    #add to database

    #return to same template 
    
    blog_post = Post.query.get_or_404(post_id)
    return render_template('post/post.html',post = blog_post )



