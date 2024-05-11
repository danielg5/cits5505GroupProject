from flask import redirect, render_template
from app import flaskApp
from typing import List

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

#@flaskApp.route('/search')
#def search():
#    return render_template('search.html')

#@flaskApp.route('/create')
#def icreate():
#    return render_template('create.html')

#@flaskApp.route('/game')
#def game():
    # TODO: get username(player) from cookie, etc.
    # TODO: get username(theme creator; not the current user) with theme from the database
    # TODO: Use username, get random theme
    # TODO: filter out guessed words, and get random secret
    # if all guessed pick any word, set variable to 'guessed_already = True' (otherwise false). 
    # True will launch a "word guessed previously" game, False will launch normal game.
    # save text file, username.txt with data {secret, theme, guessed_already, guesses_made = 0}
    # use same player.txt file for each game, overwrite on new game ('w+')

    #dictionary = {}
    #dictionary['secret'] = 'craze'
    #dictionary['theme'] = 'condition'
    #dictionary['guessed_already'] = False
    #dictionary['guesses_made'] = 0
    # use secret_length = len(secret) to set guess word length
    # player = 'daniel'
    # filename = player + '.txt'
    # f = open(filename, 'w+')
    # f.write('data')
    # f.close()
    #return render_template('game.html')

#@flaskApp.route('/random')
#def random():
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
    #return render_template('game.html')

#@flaskApp.route('/test')
#def test():
    #return render_template('test.html')