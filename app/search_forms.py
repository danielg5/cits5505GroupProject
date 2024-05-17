from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search_query = StringField('Search Query', validators=[DataRequired()])
    search_option = RadioField('Search Options', choices=[('user', 'User'), ('theme', 'Theme')])
    submit = SubmitField('Search')
