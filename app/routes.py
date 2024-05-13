from flask import redirect, render_template, request, url_for
from app import flaskApp
from app.controllers import *
from typing import List
import json, os 

# create directory for temp player files if it does not exist
os.makedirs('./app/temp', exist_ok=True)

# html files must be located in either 'app/templates' or 'app/static'
# remove comments (below) to enable the routes

@flaskApp.route('/')
def index():
    return render_template('index.html')

@flaskApp.route('/signup')
def signup():
        return render_template('signup.html')

#@flaskApp.route('/menu')
#def menu():
#    return render_template('menu.html')

#@flaskApp.route('/leaderboard')
#def leaderboard():
#    return render_template('leaderboard.html')

#@flaskApp.route('/profile')
#def profile():
#    return render_template('profile.html')

@flaskApp.route('/search', methods=['GET', 'POST'])
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
def random():
    creator, theme = get_random_theme()
    return redirect(url_for('game', creator=creator, theme=theme))

@flaskApp.route('/game', methods=['GET']) # need to receive username (theme creator) and theme
def game():
    # TODO: Need search.html to send creator and theme 
    creator = request.args.get('creator')
    theme = request.args.get('theme')
    # TODO: get username(player)
    player = get_player()
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