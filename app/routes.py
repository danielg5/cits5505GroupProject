from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app import flaskApp
from app.controllers import *
from typing import List
import json, os 

# create directory for temp player files if it does not exist
os.makedirs('./app/temp', exist_ok=True)

# html files must be located in either 'app/templates' or 'app/static'
# remove comments (below) to enable the routes


@flaskApp.route('/', methods=['GET', 'POST'])
def index():
    # login user
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Person.get_user_by_email(email)
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('menu'))
        else:
            flash('Invalid email or password')
    return render_template('index.html')

def logout():
    # logout user
    logout_user()
    return redirect(url_for('index'))       

@flaskApp.route('/signup')
def signup():
    # use similar to index() to login user
    return render_template('signup.html')

#@flaskApp.route('/menu')
#@login_required
#def menu():
#    return render_template('menu.html')

#@flaskApp.route('/leaderboard')
#@login_required
#def leaderboard():
#    return render_template('leaderboard.html')

#@flaskApp.route('/profile')
#@login_required
#def profile():
#    return render_template('profile.html')

#@flaskApp.route('/search')
#@login_required
#def search():
# TODO: Need to send to send creator and theme to game.html
#    return render_template('search.html')

#@flaskApp.route('/create')
#@login_required
#def create():
#    return render_template('create.html')

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
    #player = current_user.username
    player = 'daniel'
    filename = './app/temp/' + player + '.txt'
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