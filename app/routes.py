from flask import redirect, render_template
from app import flaskApp
from typing import List
import json, os 

# create directory for temp player files if it does not exist
os.makedirs('./app/temp', exist_ok=True)

# html files must be located in either 'app/templates' or 'app/static'
# remove comments (below) to enable the routes

@flaskApp.route('/')
def index():
    return "Hello World!"
#    return render_template('index.html')

#@flaskApp.route('/signup')
#def signup():
#    return render_template('signup.html')

#@flaskApp.route('/menu')
#def menu():
#    return render_template('menu.html')

#@flaskApp.route('/leaderboard')
#def leaderboard():
#    return render_template('leaderboard.html')

#@flaskApp.route('/profile')
#def profile():
#    return render_template('profile.html')

#@flaskApp.route('/search')
#def search():
#    return render_template('search.html')

#@flaskApp.route('/create')
#def icreate():
#    return render_template('create.html')


@flaskApp.route('/random')
def random():
    # TODO: get username(player) from cookie, etc.
    # TODO: get a random username(theme creator; not the current user) with theme from the database
    # TODO: Use random username, get random theme
    # TODO: filter out guessed words, and get random secret
    # if all guessed pick any word, set variable to 'guessed_already = True' (otherwise false). 
    # True will launch a "word guessed previously" game, False will launch normal game.
    # save text file, username.txt with data {secret, theme, guessed_already, guesses_made = 0}
    # use same player.txt file for each game, overwrite on new game ('w+')
    # filename = player + '.txt'
    # f = open(filename, 'w+')
    # f.write('data')
    # f.close()
    return render_template('game.html')

@flaskApp.route('/game')
def game():
    player = 'daniel'
    filename = './app/temp/' + player + '.txt'
    # TODO: get theme
    theme = 'condition'
    # TODO: get secret word
    secret_word = 'craze'
    # TODO: check if guessed_already
    guessed_already = False # word has been guessed already
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