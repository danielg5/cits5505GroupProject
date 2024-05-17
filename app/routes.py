from flask import flash, session, redirect, render_template, request, url_for, g, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from app import flaskApp, db
from app.controllers import *
from app.gameplay import get_filename
from typing import List
from app.model import Person, Theme
from app.forms import ThemeForm, SearchForm
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
        if user and user.check_password(password, user.salt):
            login_user(user)
            #return redirect(url_for('menu'))
            creator, theme = get_random_theme()
            return redirect(url_for('game', creator=creator, theme=theme))
        else:
            flash('Invalid email or password')
    return render_template('index.html')

@flaskApp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    session.clear()
    flash('You have been successfully logged out.')
    return redirect(url_for('index'))


@flaskApp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['user_email']
        password = request.form['user_pw']
        username = request.form['username']
        add_new_user(username, email, password)
        user = Person.get_user_by_email(email)
        if user and user.check_password(password, user.salt):
            login_user(user)
            #return redirect(url_for('menu'))
            creator, theme = get_random_theme()
            return redirect(url_for('game', creator=creator, theme=theme))
        else:
            flash('Invalid email or password')
    return render_template('signup.html')

# check if email exists
@flaskApp.route('/check_email', methods=['POST'])
def check_email():
    email = request.json.get('email')
    if check_email_exists(email):
        return jsonify({'exists': True})
    else:
        return jsonify({'exists': False})

@flaskApp.route('/check_username', methods=['POST'])
def check_username():
    username = request.json.get('username')
    if check_username_exists(username):
        return jsonify({'exists': True})
    else:
        return jsonify({'exists': False})
    
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

@flaskApp.route('/leaderboard')
@login_required
def leaderboard():
    return render_template('leaderboard.html')

@flaskApp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
#    return render_template('profile.html')


@flaskApp.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    results = []
    if form.validate_on_submit():
        search_query = form.search_query.data.strip()
        search_option = form.search_option.data

        if search_option == 'user':
            user = Person.query.filter(Person.username.ilike(search_query)).first()
            results = user.themes if user else []
        elif search_option == 'theme':
            results = Theme.query.filter(Theme.theme.ilike(f'%{search_query}%')).all()
    else:
        # Load default results, could be all themes or the most recent ones etc.
        results = Theme.query.order_by(Theme.id.desc()).all()  # Example: Get all themes

    return render_template('search.html', form=form, search_results=results, logged_in_username=current_user.username)

@flaskApp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ThemeForm()
    if form.validate_on_submit():
        # Correctly create a new Theme instance with the proper field names
        new_theme = Theme(
            person_id=current_user.id,
            theme=form.theme_name.data,
            word1=form.word1.data,
            word2=form.word2.data,
            word3=form.word3.data,
            word4=form.word4.data,
            word5=form.word5.data,
            word6=form.word6.data,
            word7=form.word7.data,
            word8=form.word8.data,
            word9=form.word9.data,
            word10=form.word10.data
        )
        db.session.add(new_theme)
        db.session.commit()
        flash('Theme created successfully!', 'success')
        return redirect(url_for('search'))  # Adjust to your valid endpoint for redirect
    # Pass the username from current_user if available in your user model
    return render_template('create.html', form=form, username=current_user.username if current_user else 'Guest')

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