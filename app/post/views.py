

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


#display all blogs list
@post.route('/posts' , defaults = {'page'  : 1} )
@post.route('/post/page/<int:page>')
def posts(page):

    paginated_posts = Post.query.filter(Post.search(text(request.args.get('q','')))).order_by(Post.timestamp.desc()).paginate(page,50,True)
    print("hello posts")
    return render_template('post/index.html' , posts = paginated_posts)


