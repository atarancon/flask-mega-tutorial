from flask_wtf import FlaskForm 
from wtforms import StringField,SelectField,TextField,TextAreaField

from wtforms.validators import Optional, Length,DataRequired

from collections import OrderedDict


def choices_from_dict (source , prepend_blank=True):
        """ Convert a dict to a format that's compatible with WTFORMS's choices. It also 
        optionally prepends a "Please select one .." value.

        Example:
        #Convert 
        STATUS = OrderDict([
            ('unread' , 'Unread'),
            ('open; , 'Open')
        ])

        #into 
        choices = [('' , 'Please selct one ...') , ('unread', 'Unread') ]

        :param source: Input sources
        :type source: dict
        :param prepend_blank: An optional blank item 
        :type prepend_blank: bool 
        :return a list of tuple
        """
        choices = []

        if prepend_blank:
            choices.append( ('' , 'Please Select one..'))
        
        for key , value in source.items():
            pair = (key , value)
            choices.append(pair)
        
        return choices


class SearchForm(FlaskForm):
    q = StringField('Search Terms', [Optional(), Length(1, 256)])


class BulkDeleteForm(FlaskForm):
    SCOPE = OrderedDict([
       ('all_selected_items', 'All selected items'),
        ('all_search_results', 'All search results')
    ])

    scope = SelectField('Privileges', [DataRequired()] , choices= choices_from_dict(SCOPE,prepend_blank=False))

class PostForm(FlaskForm):
    
    title = TextAreaField('title please', validators=[DataRequired(),Length(1,140)])
    body = TextAreaField('say somethig', validators=[DataRequired()])
    

    