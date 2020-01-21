
from flask import (
    render_template,
    request,
    flash,
    url_for,
    redirect,
    abort
)

from flask_login import (
    login_required,
    logout_user,
    login_user,
    current_user
)

from app.users.decorators import permission_required
from app.admin.models import Dashboard

from app.models import User,Post

from . import admin 

from sqlalchemy import text

from app.admin.forms import (
    SearchForm,
    BulkDeleteForm,
    PostForm
)

from datetime import datetime , timezone


@admin.before_request
@login_required
@permission_required()
def before_request():
    """ Protect all of the admin endpoints. """
    pass

@admin.route('')
def dashboard():
    group_and_count_users = Dashboard.group_count_users()
    return render_template ('admin/page/dashboard.html' , group_and_count_users=group_and_count_users)

@admin.route('/users', defaults={'page': 1} )
@admin.route('/users/page/<int:page>')
def users(page):
    
    search_form = SearchForm()
    bulk_form = BulkDeleteForm()

    paginated_users = User.query.filter(User.search( text(request.args.get('q' ,  '')) )).order_by(User.is_admin.desc()).paginate(page, 50, True)
    
    return render_template('admin/user/index.html', users=paginated_users , form=search_form, bulk_form = bulk_form)


@admin.route('/users/bulk_delete', methods=['POST'])
def users_bulk_delete():
    form = BulkDeleteForm()

    if form.validate_on_submit():
        ids = User.get_bulk_action_ids(request.form.get('scope'),
                                                        request.form.getlist('bulk_ids'),
                                                        omit_ids=[current_user.id],
                                                        query=request.args.get('q',''))

        print(ids)
        delete_count = User.bulk_delete(ids)

        flash('{0} were schedule to be deleted '.format(delete_count), 'success')
    else:
        flash('No users were deleted','error')
    
    return redirect(url_for('admin.users'))

@admin.route('/post/edit/<int:id>' , methods=['GET','POST'])
def post_edit(id):
    post = Post.query.get(id)

    #prefill forum with with post object
    form = PostForm(obj=post)

    if form.validate_on_submit():

        print(" form title text")
        print(form.title.data)

        #populate from form to object fields
        form.populate_obj(post)

        #updating the time
        post.timestamp=datetime.now(timezone.utc)

        #update author 
        post.author_p = current_user


        print("done")
        #save the object
        post.save()

        flash("Post has been updated successfully" , 'success')
        return redirect(url_for('post.posts'))
    
    return render_template('admin/post/edit.html' , form=form , post= post)

@admin.route('/post/new' , methods=['POST','GET'])
def post_new():

    form = PostForm()

    if form.validate_on_submit():
        #make a new post
        p= Post(form.title.data , form.body.data ,current_user.id )
        #save the post 
        p.save()
        
        #print post id 
        print(p.id)

        flash("post has been added", 'success')
        return redirect( url_for('post.posts'))

    return render_template("admin/post/new.html" , form = form)

#deleting a single post
@admin.route('/post/<int:post_id>/delete' , methods=['GET','POST'])
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    #only same admin can delete its posts

    #get title 
    post_title = post.title
    
    #check if current admin is author
    if post.author_p != current_user:
        flash("{0} Admin created post" .format(post.author_p) ) 
        abort(403)

    #delete post
    post.delete()

    #confirmation
    flash("Post title:{0} deleted successfulyl " .format(post_title) , 'success' ) 

    return redirect(url_for('post.posts'))



    


        



