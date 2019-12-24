from flask import (
    render_template,
    request,
    flash,
    url_for,
    redirect
)
#blueprint comes in 
from app.users.forms import (
    LoginForm   
)

from flask_login import (
    login_required,
    logout_user,
    login_user
)
from app.models import User

from . import  user_blueprint

#from user_blueprint directory import app variable instance

@user_blueprint.route ('/login' , methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        u = User.find_by_identity(request.form.get('email'))

        if u :
            
            print (" YOU MADE IT")
            login_user(u)
            return  redirect(url_for('core.index'))
    


    return render_template('users/login.html' , form = form )




#logout 
@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('users.login'))



