from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired

class ThemeForm(FlaskForm):
    theme_name = StringField('Theme Name', validators=[DataRequired()])
    word1 = StringField('Word 1', validators=[DataRequired()])
    word2 = StringField('Word 2', validators=[DataRequired()])
    word3 = StringField('Word 3', validators=[DataRequired()])
    word4 = StringField('Word 4', validators=[DataRequired()])
    word5 = StringField('Word 5', validators=[DataRequired()])
    word6 = StringField('Word 6', validators=[DataRequired()])
    word7 = StringField('Word 7', validators=[DataRequired()])
    word8 = StringField('Word 8', validators=[DataRequired()])
    word9 = StringField('Word 9', validators=[DataRequired()])
    word10 = StringField('Word 10', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search_query = StringField('Search Query', validators=[DataRequired()])
    search_option = RadioField('Search Options', choices=[('user', 'User'), ('theme', 'Theme')])
    submit = SubmitField('Search')