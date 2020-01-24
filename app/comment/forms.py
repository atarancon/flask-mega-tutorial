from flask_wtf import FlaskForm

from wtforms import  TextAreaField

from wtforms.validators import Optional , DataRequired, Length




class CommentForm(FlaskForm):
    text = TextAreaField('title please', validators=[DataRequired(),Length(1,140)])
