from functools import wraps

from flask import flash, redirect
from flask_login import current_user


def permission_required():
    """
    Does a user have permission to view this page?

    :param : None
    :return: Function
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.is_admin()  == False :
                flash('You do not have permission to do that.', 'error')
                return redirect('/')

            return f(*args, **kwargs)

        return decorated_function

    return decorator

