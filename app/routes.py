from flask import flash, session, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app import flaskApp, db
from app.controllers import *
from app.gameplay import get_filename
from typing import List
from app.model import Person, Theme
from app.forms import ThemeForm
import json, os 
from app.model import Person

# create directory for temp player files if it does not exist
os.makedirs('./app/temp', exist_ok=True)

# html files must be located in either 'app/templates' or 'app/static'
# remove comments (below) to enable the routes


@flaskApp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Person.get_user_by_email(email)
        
        if not user:
            
            flash('No user found with that email', 'error')
        else:
            
            salt = user.salt
            if user.check_password(password, salt):
                login_user(user)
                
                creator, theme = get_random_theme()
                return redirect(url_for('game', creator=creator, theme=theme))
            else:
                
                flash('Invalid password', 'error')
                
    return render_template('index.html')



def logout():
    # logout user
    logout_user()
    return redirect(url_for('index'))       



@flaskApp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['user_email']
        password = request.form['user_pw']
        username = request.form['username']

        # check if email already exists
        if check_email_exists(email):
            flash('Email already registered.', 'error')
            return render_template('signup.html')
        
        # check if username already exists
        if check_username_exists(username):
            flash('Username already taken.', 'error')
            return render_template('signup.html')

        # add new user
        add_new_user(username, email, password)
        user = Person.get_user_by_email(email)
        
        # login user
        if user and user.check_password(password, user.salt):
            login_user(user)
            creator, theme = get_random_theme()
            return redirect(url_for('game', creator=creator, theme=theme))
        else:
            flash('Signup failed. Please try again.', 'error')

    return render_template('signup.html')


#@flaskApp.route('/test')
#@login_required
#def test():
#    return render_template('test.html')

#@flaskApp.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        email = request.form['email']
#        password = request.form['password']
#        user = Person.get_user_by_email(email)
#        if not user:
            
#            flash('No user found with that email', 'error')
#            return redirect(url_for('login'))
#        else:
           
#            salt = user.salt
#            if not Person.check_password(user, password, salt):
                
#                flash('Invalid password', 'error')
#                return redirect(url_for('login'))
#            else:
               
#                login_user(user)
#                return redirect(url_for('menu'))
#    else:
#        return render_template('index.html')       

@flaskApp.route('/menu')
@login_required
def menu():
    return render_template('menu.html')

#@flaskApp.route('/leaderboard')
#@login_required
#def leaderboard():
#    return render_template('leaderboard.html')

#@flaskApp.route('/profile')
#@login_required
#def profile():
#    return render_template('profile.html')


@flaskApp.route('/search', methods=['GET', 'POST'])
#@login_required
def search():
    search_query = ''
    search_option = 'theme'  # Default search option
    results = []

    if request.method == 'POST':
        search_query = request.form['search_query']
        search_option = request.form.get('searchOption', 'theme')

        if search_option == 'user':
            # Search for themes by username
            user = Person.query.filter_by(username=search_query).first()
            if user:
                results = user.themes
            else:
                results = []
        elif search_option == 'theme':
            # Search themes by theme name
            results = Theme.query.filter(Theme.theme.like(f'%{search_query}%')).all()

    return render_template('search.html', search_results=results, search_query=search_query, search_option=search_option)

@flaskApp.route('/create')
def create():
    return render_template('create.html')


@flaskApp.route('/random')
#@login_required
def random():
    creator, theme = get_random_theme()
    return redirect(url_for('game', creator=creator, theme=theme))

@flaskApp.route('/game', methods=['GET']) # need to receive username (theme creator) and theme
#@login_required
def game():
    # TODO: Need search.html to send creator and theme 
    creator = request.args.get('creator')
    theme = request.args.get('theme')
    # TODO: get username(player)
    player = current_user.username
    filename = get_filename(player)
    #filename = './app/temp/' + player + '.txt'
    # secret_word = 'craze'
    # guessed_already = False
    secret_word, guessed_already = get_random_word(player, creator, theme)
    if guessed_already:
        game_points = 0
    else:
        game_points = len(secret_word)
    data = {}
    data['secret'] = secret_word
    data['theme'] = theme
    data['guessed_already'] = guessed_already
    # TODO: add hints variable for future feature 
    data['guesses_remain'] = len(secret_word) # when 0, game is over
    data['game_points'] = game_points
    data['game_won'] = False
    f = open(filename, 'w+')
    json.dump(data, f)
    f.close()
    return render_template('game.html', length=len(data['secret']), theme=data['theme'], user=player, points=data['game_points'], guessLeft=len(data['secret']), guessedAlreadyJ=data['guessed_already'])