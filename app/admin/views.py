
from flask import (
    render_template,
    request,
    flash,
    url_for,
    redirect
)

from flask_login import (
    login_required,
    logout_user,
    login_user
)

from app.users.decorators import permission_required
from app.admin.models import Dashboard

from app.models import User

from . import admin 


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
    users = User.query.all()





