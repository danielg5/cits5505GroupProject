from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, Regexp

class ThemeForm(FlaskForm):
    theme_name = StringField('Theme Name', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    word1 = StringField('Word 1', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    word2 = StringField('Word 2', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    word3 = StringField('Word 3', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    word4 = StringField('Word 4', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    word5 = StringField('Word 5', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    word6 = StringField('Word 6', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    word7 = StringField('Word 7', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    word8 = StringField('Word 8', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    word9 = StringField('Word 9', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    word10 = StringField('Word 10', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]*$', message="Please enter only alphabetic characters and spaces.")
    ])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search_query = StringField('Search Query', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9\s]*$', message="Please enter only alphabetic characters, numbers, and spaces.")  # Regex updated to allow letters, numbers, and spaces
    ])
    search_option = RadioField('Search Options', choices=[('user', 'User'), ('theme', 'Theme')], validators=[DataRequired()])
    submit = SubmitField('Search')