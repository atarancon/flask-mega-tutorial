

from lib.safe_next_url import safe_next_url



from flask import (
    render_template,
    request,
    flash,
    url_for,
    redirect
)
#blueprint comes in 
from app.users.forms import (
    LoginForm,
    RegistrationForm
)

from flask_login import (
    login_required,
    logout_user,
    login_user
)

from app.models import User

from app.extensions import db

from . import  user_blueprint

#from user_blueprint directory import app variable instance

#sign in
@user_blueprint.route ('/login' , methods=["GET","POST"])
def login():
    form = LoginForm(next = request.args.get('next'))

    if form.validate_on_submit():
        u = User.find_by_identity(request.form.get('email'))

        if u and u.authenticated(password=request.form.get("password")):
            
            print (" YOU MADE IT")
            login_user(u)

            #handle optional redirecting
            next_url = request.form.get('next')
            
            print(next_url)

            #caution checking path of url
            if next_url:
                return redirect(safe_next_url(next_url))
        
            return  redirect(url_for('core.index'))

        else:
            flash("Email or password is incorrect.", "warning")
            print("error")
            


    return render_template('users/login.html' , form = form )


#register
@user_blueprint.route("/signup" , methods =["GET","POST"])
def signup():
    form = RegistrationForm()

    if form.validate_on_submit():
        #add user
        user = User(email = form.email.data, 
        username = form.username.data, 
        password= form.password.data)

        #save
        db.session.add(user)
        db.session.commit()

        #thanks for registering
        flash("Awesome, Thanks for registering")

        return redirect(url_for("users.login"))


    

    return render_template('users/signup.html' , form = form)
    

#logout 
@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('users.login'))



