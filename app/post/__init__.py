from  flask import Blueprint 

post = Blueprint ('post', __name__ , template_folder='templates', url_prefix='/post')
from . import views