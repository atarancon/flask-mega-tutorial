from flask_wtf import FlaskForm 
from wtforms import StringField

from wtforms.validators import Optional, Length

class SearchForm(FlaskForm):
    q = StringField('Search Terms', [Optional(), Length(1, 256)])
