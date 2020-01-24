from  flask import Blueprint 

comment = Blueprint ('comment', __name__ , template_folder='templates')
from . import views