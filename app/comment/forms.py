from flask_wtf import FlaskForm

from wtforms import  TextAreaField , SubmitField

from wtforms.validators import Optional , DataRequired, Length




class CommentForm(FlaskForm):
    text = TextAreaField('Add a comment', validators=[DataRequired(),Length(1,140)])
    submit = SubmitField("Comment")
