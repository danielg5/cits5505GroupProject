from flask import render_template
from app import flaskApp

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

#@flaskApp.route('/game')
#def game():
#    return render_template('game.html')